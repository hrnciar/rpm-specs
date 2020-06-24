Name:           teampulls
Version:        0.2.2
Release:        3%{?dist}
Summary:        CLI tool that lists pull requests from GitHub

License:        GPLv3
URL:            https://github.com/brejoc/teampulls
Source0:        https://files.pythonhosted.org/packages/source/t/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
teampulls lists all of the pull requests for a list of users and repositories.
On top of that every pull requests that is older than 14 days is
printed in red.


%prep
%autosetup
# Remove bundled egg-info
rm -rf %{name}.egg-info

%build
%py3_build

%install
%py3_install
install -Dpm 0644 teampulls.toml %{buildroot}%{_sysconfdir}/teampulls.toml

%files
%doc README.md
%license LICENSE
%{_bindir}/teampulls

%config(noreplace) %{_sysconfdir}/teampulls.toml
%{python3_sitelib}/%{name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-3
- Rebuilt for Python 3.9

* Sat Mar 21 2020 Jochen Breuer <brejoc@gmail.com> - 0.2.2-2
- Rebuild with sources properly uploaded
* Sun Mar 08 2020 Jochen Breuer <brejoc@gmail.com> - 0.2.2-1
- Initial package of version 0.2.2
