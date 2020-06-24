%{?nodejs_find_provides_and_requires}

Name:           nodejs-mock-fs
Version:        4.12.0
Release:        1%{?dist}
Summary:        A configurable mock file system

License:        MIT
URL:            https://www.npmjs.com/package/mock-fs
Source0:        https://github.com/tschaub/mock-fs/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(chai)
BuildRequires:  npm(semver)


%description
The mock-fs module allows Node's built-in fs module to be backed
temporarily by an in-memory, mock file system. This lets you run
tests against a set of mock files and directories instead of lugging
around a bunch of test fixtures.


%prep
%autosetup -p 1 -n mock-fs-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/mock-fs
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/mock-fs
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha --recursive test


%files
%doc readme.md changelog.md
%license license.md
%{nodejs_sitelib}/mock-fs


%changelog
* Fri Apr 24 2020 Tom Hughes <tom@compton.nu> - 4.12.0-1
- Update to 4.12.0 upstream release

* Mon Feb 24 2020 Tom Hughes <tom@compton.nu> - 4.11.0-1
- Update to 4.11.0 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Tom Hughes <tom@compton.nu> - 4.10.4-1
- Update to 4.10.4 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Tom Hughes <tom@compton.nu> - 4.10.1-1
- Update to 4.10.1 upstream release

* Mon May 20 2019 Tom Hughes <tom@compton.nu> - 4.10.0-1
- Update to 4.10.0 upstream release

* Mon Apr 22 2019 Tom Hughes <tom@compton.nu> - 4.9.0-1
- Update to 4.9.0 upstream release

* Mon Feb  4 2019 Tom Hughes <tom@compton.nu> - 4.8.0-1
- Update to 4.8.0 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug  6 2018 Tom Hughes <tom@compton.nu> - 4.6.0-1
- Update to 4.6.0 upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May  8 2018 Tom Hughes <tom@compton.nu> - 4.5.0-1
- Update to 4.5.0 upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 20 2017 Tom Hughes <tom@compton.nu> - 4.4.2-1
- Update to 4.4.2 upstream release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Tom Hughes <tom@compton.nu> - 4.4.1-1
- Update to 4.4.1 upstream release

* Mon May  1 2017 Tom Hughes <tom@compton.nu> - 4.3.0-1
- Update to 4.3.0 upstream release

* Tue Mar 14 2017 Tom Hughes <tom@compton.nu> - 4.2.0-1
- Update to 4.2.0 upstream release

* Sun Feb 26 2017 Tom Hughes <tom@compton.nu> - 4.1.0-1
- Update to 4.1.0 upstream release

* Mon Feb  6 2017 Tom Hughes <tom@compton.nu> - 4.0.0-1
- Update to 4.0.0 upstream release

* Tue Nov  1 2016 Tom Hughes <tom@compton.nu> - 3.12.1-1
- Update to 3.12.1 upstream release

* Fri Oct 28 2016 Tom Hughes <tom@compton.nu> - 3.12.0-1
- Update to 3.12.0 upstream release

* Sun Jul 10 2016 Tom Hughes <tom@compton.nu> - 3.11.0-1
- Update to 3.11.0 upstream release

* Sat Jul  9 2016 Tom Hughes <tom@compton.nu> - 3.10.0-2
- Update npm(semver) dependency

* Sat Jul  9 2016 Tom Hughes <tom@compton.nu> - 3.10.0-1
- Update to 3.10.0 upstream release

* Mon Jul  4 2016 Tom Hughes <tom@compton.nu> - 3.9.0-2
- Update npm(rewire) dependency

* Sat Apr 30 2016 Tom Hughes <tom@compton.nu> - 3.9.0-1
- Update to 3.9.0 upstream release

* Tue Mar  8 2016 Tom Hughes <tom@compton.nu> - 3.8.0-1
- Update to 3.8.0 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Tom Hughes <tom@compton.nu> - 3.7.0-1
- Update to 3.7.0 upstream release

* Tue Jan 19 2016 Tom Hughes <tom@compton.nu> - 3.6.0-2
- Remove npm(semver) fixdep

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 3.6.0-1
- Initial build of 3.6.0
