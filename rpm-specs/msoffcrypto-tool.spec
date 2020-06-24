%global modulename msoffcrypto

Summary:        Python tool for decrypting MS Office files with passwords or other keys
Name:           msoffcrypto-tool
Version:        4.10.1
Release:        3%{?dist}
License:        MIT
URL:            https://github.com/nolze/msoffcrypto-tool
Source:         https://github.com/nolze/msoffcrypto-tool/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-cryptography >= 2.3
BuildRequires:  python%{python3_pkgversion}-olefile >= 0.45
# Tests
%if 0%{?fedora}
BuildRequires:  python%{python3_pkgversion}-coverage >= 4.5.1
BuildRequires:  python%{python3_pkgversion}-nose >= 1.3.7
%endif
%if 0%{?rhel} >= 8
BuildRequires:  python3.6dist(coverage) >= 4.5.1
BuildRequires:  python%{python3_pkgversion}-nose >= 1.3.7
%endif
Requires:       python%{python3_pkgversion}-%{modulename}

%description
The msoffcrypto-tool (formerly ms-offcrypto-tool) is a Python tool and
library for decrypting encrypted Microsoft Office files with password,
intermediate key, or private key which generated its escrow key.

%package -n python%{python3_pkgversion}-%{modulename}
Summary:        Python library for decrypting MS Office files with passwords or other keys
Requires:       python%{python3_pkgversion}-cryptography >= 2.3
Requires:       python%{python3_pkgversion}-olefile >= 0.45
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modulename}}

%description -n python%{python3_pkgversion}-%{modulename}
The msoffcrypto-tool (formerly ms-offcrypto-tool) is a Python tool and
library for decrypting encrypted Microsoft Office files with password,
intermediate key, or private key which generated its escrow key.

%prep
%setup -q

%build
%py3_build

%install
%py3_install

%if 0%{?fedora} || 0%{?rhel} >= 8
%check
%{__python3} setup.py test
%endif

%files
%doc README.md
%{_bindir}/%{name}

%files -n python%{python3_pkgversion}-%{modulename}
%license LICENSE.txt
%{python3_sitelib}/%{modulename}/
%{python3_sitelib}/%{modulename}_tool-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.10.1-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 10 2019 Robert Scheck <robert@fedoraproject.org> 4.10.1-1
- Upgrade to 4.10.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.10.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.10.0-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Robert Scheck <robert@fedoraproject.org> 4.10.0-1
- Upgrade to 4.10.0
- Initial spec file for Fedora and Red Hat Enterprise Linux
