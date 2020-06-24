# Use the forge macros to simplify packaging.
# See https://fedoraproject.org/wiki/Forge-hosted_projects_packaging_automation 
%global forgeurl https://github.com/orosp/ddiskit
# When we no longer need to build against a git commit, 
# Simply remove the commit variable and update the Version
# Then forge will pick up the release
%global commit de1f6847223085dcdd177e02a7298c835fae12a3

Name:           ddiskit
Version:        3.6

%forgemeta -i

Release:        8%{?dist}
Summary:        Tool for Red Hat Enterprise Linux Driver Update Disk creation

License:        GPLv3
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch
%if 0%{?fedora} >= 25
%if 0%{?fedora} >= 30
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%else
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif
%else
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
%endif

Requires:       rpm createrepo genisoimage
%if 0%{?fedora} >= 23
Suggests:       quilt git
Recommends:     kernel-devel redhat-rpm-config rpm-build
Recommends:     mock
%else
Requires:       kernel-devel redhat-rpm-config rpm-build
Requires:       mock
%endif

%description -n %{name}
Ddiskit is a little framework for simplifying creation of proper
Driver Update Disks (DUD) used for providing new or updated out-of-tree
kernel modules.

%prep
%forgesetup

%build
%if 0%{?fedora} >= 30
sed -i "s|/usr/bin/python$|/usr/bin/python3|g" bin/ddiskit
sed -i "s|/usr/bin/python$|/usr/bin/python3|g" setup.py
%py3_build
%else
%py2_build
%endif

%install
%if 0%{?fedora} >= 30
%py3_install
%else
%py2_install
%endif
find %{buildroot} -size 0 -delete

%check
%if 0%{?fedora} >= 30
%{__python3} setup.py test
%else
%{__python2} setup.py test
%endif

%files -n %{name}
%doc README
%license COPYING
%if 0%{?fedora} >= 30
%{python3_sitelib}/*
%else
%{python2_sitelib}/*
%endif
%{_bindir}/ddiskit
%{_mandir}/man1/ddiskit.1*
%{_datadir}/bash-completion/completions/ddiskit

%dir %{_datadir}/ddiskit
%dir %{_datadir}/ddiskit/keyrings
%dir %{_datadir}/ddiskit/keyrings/rh-release
%dir %{_datadir}/ddiskit/profiles
%dir %{_datadir}/ddiskit/templates
%{_datadir}/ddiskit/templates/spec
%{_datadir}/ddiskit/templates/config
%{_datadir}/ddiskit/profiles/*
%{_datadir}/ddiskit/keyrings/rh-release/*.key
%{_datadir}/ddiskit/ddiskit.config

%config(noreplace) /etc/ddiskit.config

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - Packaging variables read or set by %forgemeta
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - Packaging variables read or set by %forgemeta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Zamir SUN <zsun@fedoraproject.org> - 3.6-6.20191129gitde1f684
- Update to Python3 support in de1f6847223085dcdd177e02a7298c835fae12a3
- Fixes RHBZ#1777623

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 17 2017 Petr Oros <poros@redhat.com> - 3.6-1
- New upstream release

* Mon Jun 26 2017 Petr Oros <poros@redhat.com> - 3.5-1
- New upstream release

* Thu Jun 22 2017 Petr Oros <poros@redhat.com> - 3.4-1
- New upstream release

* Mon Apr 24 2017 Petr Oros <poros@redhat.com> - 3.3-1
- New upstream release

* Tue Mar 14 2017 Petr Oros <poros@redhat.com> - 3.2-1
- New upstream release

* Tue Feb 28 2017 Petr Oros <poros@redhat.com> - 3.1-1
- New upstream release

* Mon Feb 13 2017 Petr Oros <poros@redhat.com> - 3.0-2
- Bump version after few important fixes

* Mon Sep 5 2016 Petr Oros <poros@redhat.com> - 3.0-1
- Initial package.

