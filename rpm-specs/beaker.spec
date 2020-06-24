%global upstream_name beaker
%global with_docs 1

Name:           %{upstream_name}
Version:        27.4
Release:        2%{?dist}
Summary:        Full-stack software and hardware integration testing system
License:        GPLv2+ and BSD
URL:            https://beaker-project.org/

# To generate git snapshot, see beaker-snapshot.sh
Source0:        https://beaker-project.org/releases/%{upstream_name}-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-mock
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
%if 0%{with_docs}
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-httpdomain
%endif

%package common
Summary:        Common components for Beaker packages
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < 0.17.0-1

%package client
Summary:        Command-line client for interacting with Beaker
Requires:       %{name}-common = %{version}-%{release}
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  python3-gssapi
BuildRequires:  python3-lxml
BuildRequires:  python3-prettytable
BuildRequires:  python3-libxml2
Requires:       python3-six
Requires:       python3-setuptools
Requires:       python3-gssapi
Requires:       python3-lxml
Requires:       python3-requests
Requires:       python3-libxml2
Requires:       python3-prettytable
Requires:       python3-jinja2
# beaker-wizard was moved from rhts-devel to here in 4.52
Conflicts:      rhts-devel < 4.52

%description
Beaker is a full stack software and hardware integration testing system, with
the ability to manage a globally distributed network of test labs.

%description common
Python modules which are used by other Beaker packages.

%description client
The bkr client is a command-line tool for interacting with Beaker servers. You
can use it to submit Beaker jobs, fetch results, and perform many other tasks.

%prep
%setup -q -n %{upstream_name}-%{version}
%if !0%{with_docs}
rm -rf documentation
%endif
# The server relies on a great many packages which are intended to be bundled
# source, and its documentation greatly inflates the number of BR packages
# required. Until those are packaged separately, building those subpackages is
# unnnecessary
rm -r Server IntegrationTests LabController #documentation/server-api

%build
export BKR_PY3=1
make

%install
# RHEL 8 python3-nose removed unversioned executables
%if 0%{?rhel} >= 8
ln -sf %{_bindir}/nosetests-%{python3_version} %{buildroot}/nosetests-3
%endif

export BKR_PY3=1
DESTDIR=%{buildroot} make install

rm -rf %{buildroot}%{_datadir}/beaker-integration-tests/
rm -rf %{buildroot}%{python3_sitelib}/bkr/inttest
rm -rf %{buildroot}%{python3_sitelib}/beaker_integration_tests*
# These are for lab-controller stuff, which depends on server
rm -rf %{buildroot}%{_mandir}/man8/

%check
export BKR_PY3=1
make check
# Running the checks generates some .pyc files - burn them!
find %{buildroot} -name '__pycache__' | xargs rm -rf

%files common
%doc README.md
%license COPYING
%dir %{python3_sitelib}/bkr/
%{python3_sitelib}/bkr/__init__.py*
%{python3_sitelib}/bkr/common/
%{python3_sitelib}/bkr/log.py*
%{python3_sitelib}/%{name}_common-%{version}-py?.?.egg-info/

%files client
%dir %{_sysconfdir}/%{name}
%doc Client/client.conf.example
%{python3_sitelib}/bkr/client/
%{python3_sitelib}/%{name}_client-%{version}-py?.?-nspkg.pth
%{python3_sitelib}/%{name}_client-%{version}-py?.?.egg-info/
%{_bindir}/%{name}-wizard
%{_bindir}/bkr
%if 0%{with_docs}
%{_mandir}/man1/beaker-wizard.1.gz
%{_mandir}/man1/bkr.1.gz
%{_mandir}/man1/bkr-*.1.gz
%endif
%{_datadir}/bash-completion

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 27.4-2
- Rebuilt for Python 3.9

* Mon Mar 30 2020 Martin Styk <mastyk@redhat.com> - 27.4-1:
- Update to 27.4 (#1818717)

* Wed Mar 18 2020 Martin Styk <mastyk@redhat.com> - 27.3-1:
- Update to 27.3 (#1814828)

* Thu Feb 27 2020 Martin Styk <mastyk@redhat.com> - 27.2-1
- Update to 27.2 (#1808021)

* Wed Jan 29 2020 Martin Styk <mastyk@redhat.com> - 27.1-1
- Update to 27.1 (#1795942)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 27.0-2
- Remove dependency on unittest2 (#1789200)

* Thu Dec 19 2019 Greg Hellings <greg.hellings@gmail.com> - 27.0-1
- Upstream release 27.0
- Drop git chasing
- Python 3 support at last?

* Thu Sep 26 2019 Greg Hellings <greg.hellings@gmail.com> - 26.5-49-g97e14daec
- Upstream unrelased version
- Updated spec file to match new deps
- Brought spec file in line with upstream file where necessary
- Remove python2 dependency in favor of python3
- Added shell script to srpm to generate new git file

* Tue Jul 16 2019 Greg Hellings <greg.hellings@gmail.com> - 26.5-1
- Upstream version 26.5

* Sun Mar 31 2019 Greg Hellings <greg.hellings@gmail.com> - 26.4-1
- Upstream version 26.4

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 26.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Greg Hellings <greg.hellings@gmail.com> - 26.3-1
- New upstream 26.3

* Fri Nov 02 2018 Greg Hellings <greg.hellings@gmail.com> - 26.0-1
- New upstream 26.0

* Wed Sep 05 2018 Greg Hellings <greg.hellings@gmail.com> - 25.6-1
- New upstream 25.6

* Fri Aug 03 2018 Greg Hellings <greg.hellings@gmail.com> - 25.5-2
- Remove lab-controller, which depends on server
- Remove integration tests, which are designed for server use
- Shuffle BR/Requires to bring into line with upstream

* Wed Jul 25 2018 Greg Hellings <greg.hellings@gmail.com> - 25.5-1
- Upstream version 25.5
- Fixes BZ1607380
- Added deps for gevent and werkzeug
- Added labcontroller subpackage

* Fri Jul 13 2018 Dan Callaghan <dcallagh@redhat.com> - 25.4-3
- Explicitly invoke python2 instead of python:
  https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 25.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Greg Hellings <greg.hellings@gmail.com> - 25.4-1
- Upstream version 25.4
- Fixes BZ 1579575

* Mon May 14 2018 Greg Hellings <greg.hellings@gmail.com> - 25.2-1
- Upstream version 25.2
- Fixes BZ1566043

* Tue Mar 13 2018 Greg Hellings <greg.hellings@gmail.com> - 25.0-1
- Upstream version 25.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 24.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Greg Hellings <greg.hellings@gmail.com> - 24.5-1
- Upstream release 24.5

* Tue Oct 03 2017 Greg Hellings <greg.hellings@gmail.com> - 24.4-1
- Upstream release 24.4

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 24.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Greg Hellings <greg.hellings@gmail.com> - 24.3-1
- Upstream release 24.3

* Thu Apr 06 2017 Greg Hellings <greg.hellings@gmail.com> - 24.2-1
- Upstream release 24.2

* Mon Mar 06 2017 Greg Hellings <greg.hellings@gmail.com> - 24.1-2
- Fixed broken dependency

* Mon Mar 06 2017 Greg Hellings <greg.hellings@gmail.com> - 24.1-1
- New upstream release 24.1
- Imported to official builds

* Wed Mar 01 2017 Greg Hellings <greg.hellings@gmail.com> - 24.0-2
- Renamed child packages per review

* Thu Feb 23 2017 Greg Hellings <greg.hellings@gmail.com> - 24.0-1
- Upgraded to upstream 24.0

* Wed Dec 21 2016 Greg Hellings <greg.hellings@gmail.com> - 23.3-1
- Initial build
