%global sum An httplib2 transport for google-auth
%global srcname google-auth-httplib2

Name:           google-auth-httplib2
Summary:        %{sum}
Version:        0.0.3
Release:        2%{?dist}

License:        ASL 2.0
URL:            https://github.com/GoogleCloudPlatform/google-auth-library-python-httplib2
Source0:        https://files.pythonhosted.org/packages/e7/32/ac7f30b742276b4911a1439c5291abab1b797ccfd30bc923c5ad67892b13/google-auth-httplib2-0.0.3.tar.gz
BuildArch:      noarch

%description 
httplib has lots of problems such as lack of threadsafety and insecure usage
of TLS. Using it is highly discouraged. This library is intended to help
existing users of oauth2client migrate to google-auth.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-httplib2
Requires:       python3-httplib2

%description -n python3-%{srcname}
Written by Google, this library provides a small, flexible, and powerful 
Python 3 client library for accessing Google APIs.

%prep
%setup -q

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{srcname}
%license LICENSE 
%doc README.rst
%{python3_sitelib}/google_auth_httplib2.py
%{python3_sitelib}/google_auth_httplib2-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/__pycache__/google_auth_httplib2.cpython-*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.0.3-1
- Initial build
