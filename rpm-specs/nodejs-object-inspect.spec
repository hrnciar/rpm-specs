Name:           nodejs-object-inspect
Version:        1.6.0
Release:        5%{?dist}
Summary:        String representations of objects in node and the browser

License:        MIT
URL:            https://github.com/substack/object-inspect
Source0:        https://registry.npmjs.org/object-inspect/-/object-inspect-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)

%description
%{summary}.


%prep
%autosetup -p 1 -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/object-inspect
cp -pr package.json index.js util.inspect.js %{buildroot}%{nodejs_sitelib}/object-inspect
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/tape/bin/tape test/*.js


%files
%doc readme.markdown example
%license LICENSE
%{nodejs_sitelib}/object-inspect


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May  3 2018 Tom Hughes <tom@compton.nu> - 1.6.0-1
- Update to 1.6.0 upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 27 2017 Tom Hughes <tom@compton.nu> - 1.5.0-1
- Update to 1.5.0 upstream release

* Thu Dec 21 2017 Tom Hughes <tom@compton.nu> - 1.4.1-1
- Update to 1.4.1 upstream release

* Thu Nov 16 2017 Tom Hughes <tom@compton.nu> - 1.4.0-3
- Re-enable tests

* Thu Nov 16 2017 Tom Hughes <tom@compton.nu> - 1.4.0-2
- Include util.inspect.js in package

* Wed Nov  1 2017 Tom Hughes <tom@compton.nu> - 1.4.0-1
- Update to 1.4.0 upstream release

* Tue Aug  1 2017 Tom Hughes <tom@compton.nu> - 1.3.0-1
- Update to 1.3.0 upstream release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-2
- Add upstream patch to fix tests on Node.js 6.5+

* Sun Apr 10 2016 Tom Hughes <tom@compton.nu> - 1.2.1-1
- Update to 1.2.1 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Update to 1.1.0 upstream release

* Wed Aug 26 2015 Tom Hughes <tom@compton.nu> - 1.0.2-1
- Update to 1.0.2 upstream release

* Sun Jul  5 2015 Tom Hughes <tom@compton.nu> - 1.0.0-3
- Fix FTBFS due to test failure with tape 3.x

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 23 2014 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Update to 1.0.0 upstream release

* Thu Jul 24 2014 Tom Hughes <tom@compton.nu> - 0.4.0-1
- Initial build of 0.4.0
