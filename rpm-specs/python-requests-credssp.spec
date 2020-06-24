%global srcname requests_credssp
%global gh_owner jborean93
%global gh_name requests-credssp


%if 0%{?fedora}
# escaping for EPEL.
%endif

Name:       python-%{gh_name}
Version:    1.0.0
Release:	  8%{?dist}
Summary:    This package allows for HTTPS CredSSP authentication using the requests library.

License:    MIT
URL:        https://pypi.python.org/pypi/%{srcname}
Source0:    https://github.com/%{gh_owner}/%{gh_name}/archive/v%{version}.tar.gz#/%{gh_name}-%{version}.tar.gz
BuildArch:  noarch

%if 0%{?fedora}
%else
BuildRequires:  pyOpenSSL
%endif

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

# For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-cryptography
BuildRequires:  python3-requests
BuildRequires:  python3-pyOpenSSL
BuildRequires:  python3-pyasn1
BuildRequires:  python3-ntlm-auth


%description
This package allows for HTTPS CredSSP authentication using the requests library. CredSSP is a Microsoft authentication that allows your credentials to be delegated to a server giving you double hop authentication.

%package -n python3-%{gh_name}
Requires:  python3-cryptography
Requires:  python3-requests
Requires:  python3-pyOpenSSL
Requires:  python3-pyasn1
Requires:  python3-ntlm-auth
Summary:  Python 3 credssp library
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{gh_name}
This package allows for HTTPS CredSSP authentication using the requests library. CredSSP is a Microsoft authentication that allows your credentials to be delegated to a server giving you double hop authentication.

%prep
%autosetup -n %{gh_name}-%{version}
# Remove bundled egg-info, it's not there yet but just in case it gets added upstream
rm -rf %{gh_name}.egg-info


%build
%py3_build


%install
%py3_install

%check
%{__python3} -m pytest tests

%files -n python3-%{gh_name}
%license LICENSE
%doc CHANGES.md README.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 25 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-3
- Subpackage python2-requests-credssp has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon May 21 2018 James Hogarth <james.hogarth@gmail.com> - 1.0.0-1
- Initial package
