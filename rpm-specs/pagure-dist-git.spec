%{?python_enable_dependency_generator}

%if 0%{?rhel} && 0%{?rhel} < 8
# Since the Python 3 stack in EPEL is missing too many dependencies,
# we're sticking with Python 2 there for now.
%global __python %{__python2}
%global python_pkgversion 2
%else
# Default to Python 3 when F29+
%global __python %{__python3}
%global python_pkgversion %{python3_pkgversion}
%endif

Name:               pagure-dist-git
Version:            1.7.0
Release:            2%{?dist}
Summary:            Pagure Git auth backend for Dist-Git setups

License:            GPLv2+
URL:                https://pagure.io/pagure-dist-git
Source0:            https://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz
BuildArch:          noarch

BuildRequires:      python%{python_pkgversion}-devel
BuildRequires:      python%{python_pkgversion}-setuptools

%if 0%{?rhel} && 0%{?rhel} < 8
Requires:           pagure >= 5.2
%else
Recommends:         python%{python_pkgversion}-pdc-client
%endif

# This is actually an extension to Pagure itself and can't be built this way
# So we're changing it all up..
Obsoletes:          python-%{name} < 0.12
Obsoletes:          python2-%{name} < 0.12
Obsoletes:          python3-%{name} < 0.12
# However, we'll preserve some backwards compatibility here
Provides:           python%{python_pkgversion}-%{name} = %{version}-%{release}

%description
This project hosts the logic to generate gitolite's configuration file for
Dist-Git, which has a different access model than regular Pagure Git systems.


%prep
%autosetup


%build
%py_build


%install
%py_install


# Install the different cron job scripts
mkdir -p $RPM_BUILD_ROOT/%{_libexecdir}/pagure-dist-git/
install -p -m 644 scripts/*.py $RPM_BUILD_ROOT/%{_libexecdir}/pagure-dist-git/

%if 0%{?fedora} || 0%{?rhel} >= 8
# Byte compile everything not in sitelib
%py_byte_compile %{__python} %{buildroot}%{_libexecdir}/pagure-dist-git/
%endif

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/pagure_distgit/
%{python_sitelib}/dist_git_auth.py*
%{python_sitelib}/pagure_dist_git-%{version}*
%if 0%{?python_pkgversion} != 2
%{python3_sitelib}/__pycache__/dist_git_auth*.pyc
%endif
%{_libexecdir}/pagure-dist-git/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-2
- Rebuilt for Python 3.9

* Thu May 14 2020 Neal Gompa <ngompa13@gmail.com> - 1.7.0-1
- Update to 1.7.0

* Mon Mar 30 2020 Neal Gompa <ngompa13@gmail.com> - 1.6.1-1
- Update to 1.6.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Neal Gompa <ngompa13@gmail.com> - 1.5.0-1
- Rebase to 1.5.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Neal Gompa <ngompa13@gmail.com> - 1.2.1-1
- Rebase to 1.2.1

* Tue Sep 18 2018 Neal Gompa <ngompa13@gmail.com> - 0.12-1
- Rework and simplify packaging to mimic pagure's package setup
- Rebase to the latest version of the extension
- Drop Python 2 build for F29+ (#1627133)

* Mon Sep 10 2018 Ralph Bean <rbean@redhat.com> - 0.1-4
- Enable python 3.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jun 30 2017 Ralph Bean <rbean@redhat.com> - 0.1-1
- Initial packaging for Fedora
