%global srcname msal-extensions
%global _description %{expand:The Microsoft Authentication Extensions for Python offers secure mechanisms for
client applications to perform cross-platform token cache serialization and
persistence. It gives additional support to the Microsoft Authentication Library
for Python (MSAL).

MSAL Python supports an in-memory cache by default and provides the
SerializableTokenCache to perform cache serialization. You can read more about
this in the MSAL Python documentation. Developers are required to implement
their own cache persistance across multiple platforms and Microsoft
Authentication Extensions makes this simpler.}

Name:           python-%{srcname}
Version:        0.2.2
Release:        1%{?dist}
Summary:        Microsoft Authentication extensions for MSAL Python

License:        MIT
URL:            https://github.com/AzureAD/microsoft-authentication-extensions-for-python/
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildArch:      noarch

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       libsecret
Requires:       %{py3_dist pygobject}

%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -n microsoft-authentication-extensions-for-python-%{version}

# Remove bundled egg-info
rm -rf *.egg-info

# Remove DOS line endings
sed "s|\r||g" README.md >README.md.new && \
touch -r README.md README.md.new && \
mv README.md.new README.md


%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/msal_extensions/
%{python3_sitelib}/msal_extensions-*.egg-info/


%changelog
* Mon Jun 01 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.2-1
- Initial RPM release
