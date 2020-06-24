%{?nodejs_find_provides_and_requires}

Name:           nodejs-nan1
Version:        1.9.0
Release:        9%{?dist}
Summary:        Native Abstractions for Node.js

License:        MIT
URL:            https://github.com/nodejs/nan
Source0:        https://registry.npmjs.org/nan/-/nan-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

# nan is a header only library statically included by dependents
Provides:      nodejs-nan-devel = %{version}-%{release}
Provides:      nodejs-nan-static = %{version}-%{release}


%description
A header file filled with macro and utility goodness
for making add on development for Node.js easier across
versions 0.8, 0.10 and 0.11, and eventually 0.12.

Thanks to the crazy changes in V8 (and some in Node core),
keeping native add-on compiling happily across versions,
particularly 0.10 to 0.11/0.12, is a minor nightmare. 
The goal of this project is to store all logic necessary
to develop native Node.js add-on without having to inspect 
NODE_MODULE_VERSION and get yourself into a macro-tangle.


%prep
%setup -q -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/nan@1
cp -pr include_dirs.js nan*.h package.json  %{buildroot}%{nodejs_sitelib}/nan@1


%files
%doc CHANGELOG.md README.md
%license LICENSE.md
%{nodejs_sitelib}/nan@1


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Tom Hughes <tom@compton.nu> - 1.9.0-1
- Initial build of 1.9.0
