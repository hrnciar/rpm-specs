%{?nodejs_find_provides_and_requires}

Name:           nodejs-tmp
Version:        0.1.0
Release:        1%{?dist}
Summary:        Temporary file and directory creator

License:        MIT
URL:            https://www.npmjs.com/package/tmp
Source0:        https://github.com/raszi/node-tmp/archive/v%{version}/%{name}-%{version}.tar.gz
# Disable failing tests
Patch0:         nodejs-tmp-tests.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(rimraf)


%description
This is a widely used library to create temporary files and
directories in a node.js environment.

Tmp offers both an asynchronous and a synchronous API. For
all API calls, all the parameters are optional.

Tmp uses crypto for determining random file names, or, when
using templates, a six letter random identifier. And just in
case that you do not have that much entropy left on your
system, Tmp will fall back to pseudo random numbers.

You can set whether you want to remove the temporary file
on process exit or not, and the destination directory can
also be set.


%prep
%autosetup -p 1 -n node-tmp-%{version}
%nodejs_fixdep rimraf "^2.6.1"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/tmp
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/tmp
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha test/*-test.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/tmp


%changelog
* Wed Feb  5 2020 Tom Hughes <tom@compton.nu> - 0.1.0-1
- Update to 0.1.0 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.30-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov  2 2016 Tom Hughes <tom@compton.nu> - 0.0.30-1
- Update to 0.0.30 upstream release

* Mon Sep 19 2016 Tom Hughes <tom@compton.nu> - 0.0.29-1
- Update to 0.0.29 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec  3 2015 Tom Hughes <tom@compton.nu> - 0.0.28-1
- Initial build of 0.0.28
