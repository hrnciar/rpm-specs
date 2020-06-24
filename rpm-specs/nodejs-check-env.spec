%global npmname check-env

Name:           nodejs-%{npmname}
Version:        1.3.0
Release:        4%{?dist}
Summary:        Makes sure that all required environment variables are set

License:        MIT
URL:            https://www.npmjs.com/package/%{npmname}

Source0:        https://registry.npmjs.org/%{npmname}/-/%{npmname}-%{version}.tgz

BuildRequires:  nodejs-packaging
BuildRequires:  dos2unix

BuildRequires:  mocha

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

%description
Makes sure that all required environment variables are set.

%prep
%autosetup -n package

# Remove the cowsay dependency.
%nodejs_fixdep -r cowsay

# dos2unix the README.
dos2unix README.md

%build
# Nothing to build, this is a noarch package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
# Don't package bin.js. I think we can get away with this.
# (This is the script that includes the 'cowsay' module).
# If we want to package that script, bin.js should be patched to not use
# node-cowsay.
cp -a index.js %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
mocha

%files
%{nodejs_sitelib}/%{npmname}/
%doc README.md
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 16 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.3.0-1
- Initial package.
