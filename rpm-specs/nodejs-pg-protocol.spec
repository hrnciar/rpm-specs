%{?nodejs_find_provides_and_requires}

Name:           nodejs-pg-protocol
Version:        1.2.4
Release:        1%{?dist}
Summary:        The postgres client/server binary protocol

License:        MIT
URL:            https://www.npmjs.com/package/pg-protocol
Source0:        https://registry.npmjs.org/pg-protocol/-/pg-protocol-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs nodejs-packaging


%description
The postgres client/server binary protocol, implemented in TypeScript.


%prep
%autosetup -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/pg-protocol
cp -pr package.json %{buildroot}%{nodejs_sitelib}/pg-protocol
mkdir -p %{buildroot}%{nodejs_sitelib}/pg-protocol/dist
cp -pr dist/*.js %{buildroot}%{nodejs_sitelib}/pg-protocol/dist
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs -e "require('./')"


%files
%license LICENSE
%{nodejs_sitelib}/pg-protocol


%changelog
* Sun Mar  4 2018 Tom Hughes <tom@compton.nu> - 1.2.3-1
- Initial build of 1.2.3.
