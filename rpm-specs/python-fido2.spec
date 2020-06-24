%{?python_enable_dependency_generator}
%if 0%{?fedora}
%bcond_with python2
# Missing pyfakefs >= 3.4 on F30
%if 0%{?fedora} >= 31
%bcond_without python_tests
%else
%bcond_with python_tests
%endif
%else
%bcond_without python2
# Missing pyfakefs on EPEL7
%bcond_with python_tests
%endif

%global srcname fido2

Name:           python-%{srcname}
Version:        0.8.1
Release:        4%{?dist}
Summary:        Functionality for FIDO 2.0, including USB device communication

# Main code is BSD
# pyu2f is APLv2
# public_suffix_list.dat is MPLv2
License:        BSD and ASL 2.0 and MPLv2.0
URL:            https://github.com/Yubico/python-fido2
Source0:        https://github.com/Yubico/python-%{srcname}/archive/%{version}/python-%{name}-%{version}.tar.gz
# Deal with old setuptools on EPEL7
Patch0:         python-fido2-setup.patch
BuildArch:      noarch

%global _description\
Provides library functionality for communicating with a FIDO device over USB\
as well as verifying attestation and assertion signatures.\
\
WARNING: This project is in beta. Expect things to change or break at any time!\
\
This library aims to support the FIDO U2F and FIDO 2.0 protocols for\
communicating with a USB authenticator via the Client-to-Authenticator\
Protocol (CTAP 1 and 2). In addition to this low-level device access, classes\
defined in the fido2.client and fido2.server modules implement higher level\
operations which are useful when interfacing with an Authenticator, or when\
implementing a Relying Party.\
\
For usage, see the examples/ directory.

%description %_description

%if %{with python2}
%package -n python2-%{srcname}
Summary: %summary
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-cryptography
BuildRequires:  python2-six
BuildRequires:  python2-enum34
# For tests
BuildRequires:  python2-mock
%if %{with python_tests}
BuildRequires:  python2-pyfakefs >= 3.4
%endif
%if %{undefined __pythondist_requires}
Requires:       python2-enum34
Requires:       python2-cryptography
Requires:       python2-pyscard
Requires:       python2-six
%endif
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname} %_description
%endif

%package -n python%{python3_pkgversion}-%{srcname}
Summary: %summary
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-cryptography
BuildRequires:  python%{python3_pkgversion}-six
# For tests
BuildRequires:  python%{python3_pkgversion}-mock
%if %{with python_tests}
BuildRequires:  python%{python3_pkgversion}-pyfakefs >= 3.4
%endif
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-cryptography
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     python%{python3_pkgversion}-pyscard
%else
Requires:       python%{python3_pkgversion}-pyscard
%endif
Requires:       python%{python3_pkgversion}-six
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname} %_description

%if 0%{?python3_other_pkgversion}
%package -n python%{python3_other_pkgversion}-%{srcname}
Summary: %summary
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-cryptography
BuildRequires:  python%{python3_other_pkgversion}-six
# For tests
BuildRequires:  python%{python3_other_pkgversion}-mock
%if %{with python_tests}
BuildRequires:  python%{python3_other_pkgversion}-pyfakefs >= 3.4
%endif
%if %{undefined __pythondist_requires}
Requires:       python%{python3_other_pkgversion}-cryptography
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     python%{python3_other_pkgversion}-pyscard
%else
Requires:       python%{python3_other_pkgversion}-pyscard
%endif
Requires:       python%{python3_other_pkgversion}-six
%endif
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{srcname}}

%description -n python%{python3_other_pkgversion}-%{srcname} %_description
%endif

%prep
%autosetup -p1


%build
%if %{with python2}
%py2_build
%endif
%py3_build
%if 0%{?python3_other_pkgversion}
%py3_other_build
%endif


%install
%if %{with python2}
%py2_install
%endif
%py3_install
%if 0%{?python3_other_pkgversion}
%py3_other_install
%endif


%check
%if %{with python2} && %{with python_tests}
%{__python2} setup.py test
%endif
%{__python3} setup.py test
%if 0%{?python3_other_pkgversion}
%{__python3_other} setup.py test
%endif


%if %{with python2}
%files -n python2-%{srcname}
%license COPYING*
%doc NEWS README.adoc examples
%{python2_sitelib}/%{srcname}-*.egg-info/
%{python2_sitelib}/%{srcname}/
%endif

%files -n python%{python3_pkgversion}-%{srcname}
%license COPYING*
%doc NEWS README.adoc examples
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%if 0%{?python3_other_pkgversion}
%files -n python%{python3_other_pkgversion}-%{srcname}
%license COPYING*
%doc NEWS README.adoc examples
%{python3_other_sitelib}/%{srcname}-*.egg-info/
%{python3_other_sitelib}/%{srcname}/
%endif


%changelog
* Wed Jun 24 2020 Orion Poplawski <orion@nwra.com> - 0.8.1-4
- Add BR on python-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Orion Poplawski <orion@nwra.com> - 0.8.1-1
- Update to 0.8.1

* Thu Oct 24 2019 Orion Poplawski <orion@nwra.com> - 0.7.2-1
- Update to 0.7.2

* Thu Sep 26 2019 Orion Poplawski <orion@nwra.com> - 0.7.1-1
- Update to 0.7.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-2
- Rebuilt for Python 3.8

* Sun Aug 11 2019 Orion Poplawski <orion@nwra.com> - 0.7.0-1
- Update to 0.7.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Orion Poplawski <orion@nwra.com> - 0.6.0-1
- Update to 0.6.0

* Thu Mar 14 2019 Orion Poplawski <orion@nwra.com> - 0.5.0-4
- Fix for python3 on EPEL

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 01 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-2
- Enable python dependency generator

* Mon Dec 31 2018 Orion Poplawski <orion@nwra.com> - 0.5.0-1
- Update to 0.5.0

* Mon Dec 3 2018 Orion Poplawski <orion@nwra.com> - 0.4.0-2
- Fix License
- Remove tab and fix permissions

* Fri Nov 30 2018 Orion Poplawski <orion@nwra.com> - 0.4.0-1
- Initial Fedora package
