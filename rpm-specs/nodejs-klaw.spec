Name:           nodejs-klaw
Version:        3.0.0
Release:        2%{?dist}
Summary:        File system walker with Readable stream interface

License:        MIT
URL:            https://www.npmjs.com/package/klaw
Source0:        https://github.com/jprichardson/node-klaw/archive/%{version}/node-klaw-%{version}.tar.gz
# https://github.com/jprichardson/node-klaw/pull/33
Patch0:         nodejs-klaw-sort.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tap)
BuildRequires:  npm(graceful-fs)
BuildRequires:  npm(mkdirp)
BuildRequires:  npm(rimraf)
BuildRequires:  npm(tape)


%description
%{summary}.


%prep
%autosetup -p 1 -n node-klaw-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/klaw
cp -pr package.json src %{buildroot}%{nodejs_sitelib}/klaw
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%tap tests/**/*.js


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/klaw


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug  1 2019 Tom Hughes <tom@compton.nu> - 3.0.0-1
- Update to 3.0.0 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Tom Hughes <tom@compton.nu> - 2.0.0-2
- Fix npm(graceful-fs) dependency

* Sun Jun 25 2017 Tom Hughes <tom@compton.nu> - 2.0.0-1
- Update to 2.0.0 upstream release

* Mon Feb  6 2017 Tom Hughes <tom@compton.nu> - 1.3.1-2
- Patch tests for changes in mock-fs 4.x

* Fri Oct 28 2016 Tom Hughes <tom@compton.nu> - 1.3.1-1
- Update to 1.3.1 upstream release

* Wed Jun 15 2016 Tom Hughes <tom@compton.nu> - 1.3.0-1
- Update to 1.3.0 upstream release

* Sun Apr 17 2016 Tom Hughes <tom@compton.nu> - 1.2.0-1
- Update to 1.2.0 upstream release

* Fri Mar  4 2016 Tom Hughes <tom@compton.nu> - 1.1.3-3
- Use correct license file

* Fri Feb 26 2016 Tom Hughes <tom@compton.nu> - 1.1.3-2
- Fix URL for license file

* Thu Feb 25 2016 Tom Hughes <tom@compton.nu> - 1.1.3-1
- Initial build of 1.1.3
