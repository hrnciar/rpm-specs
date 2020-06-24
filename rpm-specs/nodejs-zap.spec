%global enable_tests 0

Name:           nodejs-zap
Version:        0.2.9
Release:        10%{?dist}
Summary:        A tiny test runner

License:        MIT
URL:            https://github.com/nornagon/node-zap
Source0:        http://registry.npmjs.org/zap/-/zap-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%description
A tiny test runner. Each test is run in a separate node
instance - zap require()s your module once to work out what
tests are in it, then once for each test in a new node process.


%prep
%setup -q -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/zap
cp -pr package.json bin %{buildroot}/%{nodejs_sitelib}/zap
mkdir -p %{buildroot}/%{_bindir}
ln -s  %{nodejs_sitelib}/zap/bin/zap %{buildroot}/%{_bindir}/nodejs-zap
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
./bin/zap
%endif


%files
%doc LICENSE README.md
%{nodejs_sitelib}/zap
%{_bindir}/nodejs-zap


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun  8 2015 Tom Hughes <tom@compton.nu> - 0.2.9-1
- Update to 0.2.9 upstream release

* Fri Feb 20 2015 Tom Hughes <tom@compton.nu> - 0.2.8-1
- Update to 0.2.8 upstream release

* Thu Feb 19 2015 Tom Hughes <tom@compton.nu> - 0.2.7-1
- Update to 0.2.7 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 11 2014 Tom Hughes <tom@compton.nu> - 0.2.6-1
- Update to 0.2.6 upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 27 2013 Tom Hughes <tom@compton.nu> - 0.2.5-3
- Rename /usr/bin/zap to /usr/bin/nodejs-zap to avoid conflict with xbase

* Mon Mar  4 2013 Tom Hughes <tom@compton.nu> - 0.2.5-2
- Add copy of license file from upstream
- Improve description

* Sun Feb 24 2013 Tom Hughes <tom@compton.nu> - 0.2.5-1
- Initial build of 0.2.5
