%global srcname academic-admin

Name:           %{srcname}
Version:        0.5.1
Release:        1%{?dist}
Summary:        Admin tool for the Academic website builder

License:        MIT
URL:            https://github.com/sourcethemes/%{srcname}
Source0:        https://github.com/sourcethemes/%{srcname}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         academic-admin-0.5.1-shebang-fix.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-toml
BuildRequires:  python3-requests
BuildRequires:  python3-bibtexparser

%description
An admin tool for the Academic website builder.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%files -n %{srcname}
%doc README.md
%license LICENSE.md
%{python3_sitelib}/academic-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/academic/
%{_bindir}/*

%changelog
* Wed Mar 25 2020 W. Michael Petullo <mike@flyn.org> - 0.5.1-1
- New upstream version
- Patch out shebang lines from non-executable Python files
- Update Source0

* Thu Mar 12 2020 W. Michael Petullo <mike@flyn.org> - 0.5.0-1
- Initial package
