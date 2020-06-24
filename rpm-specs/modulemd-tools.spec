Name: modulemd-tools
Version: 0.1
Release: 1%{?dist}
Summary: Collection of tools for parsing and generating modulemd YAML files
License: MIT
BuildArch: noarch

URL: https://github.com/rpm-software-management/modulemd-tools
Source0: https://github.com/rpm-software-management/modulemd-tools/archive/%{version}/%{name}-%{version}.tar.gz

# Source1 is a temporary thing until we merge it with modulemd-tools upstream
Source1: https://github.com/FrostyX/dir2module/archive/v0.1/dir2module-0.1.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-click
BuildRequires: python3-dnf
BuildRequires: python3-libmodulemd
BuildRequires: python3-hawkey
BuildRequires: python3-createrepo_c

Requires: python3-click
Requires: python3-dnf
Requires: python3-libmodulemd
Requires: python3-hawkey
Requires: python3-createrepo_c


%description
Tools provided by this package:

repo2module - Takes a YUM repository on its input and creates modules.yaml
    containing YAML module definitions generated for each package.

dir2module - Generates a module YAML definition based on essential module
    information provided via command-line parameters. The packages provided by
    the module are found in a specified directory or a text file containing
    their list.


%prep
%setup -q
%setup -T -D -a 1


%build
%py3_build


%install
%py3_install
cp dir2module-0.1/dir2module.py %{buildroot}%{_bindir}/dir2module


%check
%{python3} setup.py test


%files
%doc README.md
%license LICENSE
%{python3_sitelib}/repo2module
%{python3_sitelib}/repo2module-*.egg-info/
%{_bindir}/repo2module
%{_bindir}/dir2module


%changelog
* Tue Jun 09 2020 Jakub Kadlčík <jkadlcik@redhat.com> - 0.1-1
- Initial package
