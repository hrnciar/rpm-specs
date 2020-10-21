Summary:        Secure HTTP request signing using the HTTP Signature draft specification
Name:           python-httpsig-cffi
Version:        15.0.0
Release:        10%{?dist}
License:        MIT
URL:            https://github.com/hawkowl/httpsig_cffi
Source0:        https://files.pythonhosted.org/packages/source/h/httpsig-cffi/httpsig_cffi-%{version}.tar.gz
BuildArch:      noarch 
BuildRequires:  python3-devel
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
%description
Sign HTTP requests with secure signatures according to the IETF HTTP
Signatures specification (Draft 3_). This is a fork of the fork of the
original module that was made to fully support both RSA and HMAC
schemes as well as unit test both schemes to prove they work. This
particular fork moves from PyCrypto to Cryptography, which provides
PyPy support.

%package -n     python3-httpsig-cffi
Summary:        %{summary}
%{?python_provide:%python_provide python3-httpsig-cffi} 
Requires:       python3dist(cryptography)
Requires:       python3dist(requests)
Requires:       python3dist(six)
%description -n python3-httpsig-cffi
Sign HTTP requests with secure signatures according to the IETF HTTP
Signatures specification (Draft 3_). This is a fork of the fork of the
original module that was made to fully support both RSA and HMAC
schemes as well as unit test both schemes to prove they work. This
particular fork moves from PyCrypto to Cryptography, which provides
PyPy support.

%prep
%autosetup -n httpsig_cffi-%{version}

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/httpsig_cffi/tests

%check
%{__python3} setup.py test

%files -n python3-httpsig-cffi
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/httpsig_cffi
%{python3_sitelib}/httpsig_cffi-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 15.0.0-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 15.0.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 15.0.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 15.0.0-2
- Rebuilt for Python 3.7

* Wed Jun 06 2018 Terje Rosten <terje.rosten@ntnu.no> - 15.0.0-1
- Initial package
