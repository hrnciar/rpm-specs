%global srcname msal
%global _description %{expand:The Microsoft Authentication Library for Python enables applications to
integrate with the Microsoft identity platform. It allows you to sign in users
or apps with Microsoft identities (Azure AD, Microsoft Accounts and Azure AD B2C
accounts) and obtain tokens to call Microsoft APIs such as Microsoft Graph or
your own APIs registered with the Microsoft identity platform. It is built using
industry standard OAuth2 and OpenID Connect protocols.}

Name:           python-%{srcname}
Version:        1.3.0
Release:        2%{?dist}
Summary:        Microsoft Authentication Library (MSAL) for Python

License:        MIT
URL:            https://github.com/AzureAD/microsoft-authentication-library-for-python/
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildArch:      noarch

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -n microsoft-authentication-library-for-python-%{version}

# Remove bundled egg-info
rm -rf *.egg-info


%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/


%changelog
* Sun May 31 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.3.0-2
- Rebuild for Python 3.9

* Fri May 29 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.3.0-1
- Initial RPM release
