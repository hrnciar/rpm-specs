Name:           nodejs-proxyquire
Version:        2.0.1
Release:        6%{?dist}
Summary:        Proxies Node.js require to allow overriding dependencies

License:        MIT
URL:            https://github.com/thlorenz/proxyquire
Source0:        http://registry.npmjs.org/proxyquire/-/proxyquire-%{version}.tgz
# Drop test that needs native-hello-world
Patch0:         nodejs-proxyquire-helloworld.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(fill-keys)
BuildRequires:  npm(module-not-found-error)
BuildRequires:  npm(mocha)
BuildRequires:  npm(resolve)
BuildRequires:  npm(should)

%description
Proxies Node,js's require in order to make overriding dependencies
during testing easy while staying totally unobstrusive.


%prep
%autosetup -p 1 -n package
%nodejs_fixdep resolve "^1.1.7"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/proxyquire
cp -pr package.json index.js lib %{buildroot}%{nodejs_sitelib}/proxyquire
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha


%files
%doc README.md examples
%license LICENSE
%{nodejs_sitelib}/proxyquire


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Tom Hughes <tom@compton.nu> - 2.0.1-2
- Update npm(resolve) dependency

* Tue Mar 20 2018 Tom Hughes <tom@compton.nu> - 2.0.1-1
- Update to 2.0.1 upstream release

* Sat Mar  3 2018 Tom Hughes <tom@compton.nu> - 2.0.0-1
- Update to 2.0.0 upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Tom Hughes <tom@compton.nu> - 1.8.0-1
- Update to 1.8.0 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Tom Hughes <tom@compton.nu> - 1.7.11-1
- Update to 1.7.11 upstream release

* Mon Jul  4 2016 Tom Hughes <tom@compton.nu> - 1.7.10-1
- Update to 1.7.10 upstream release

* Wed May 11 2016 Tom Hughes <tom@compton.nu> - 1.7.9-1
- Update to 1.7.9 upstream release

* Tue May 10 2016 Tom Hughes <tom@compton.nu> - 1.7.8-1
- Update to 1.7.8 upstream release

* Fri May  6 2016 Tom Hughes <tom@compton.nu> - 1.7.7-1
- Update to 1.7.7 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb  2 2016 Tom Hughes <tom@compton.nu> - 1.7.4-1
- Update to 1.7.4 upstream release

* Tue Oct 13 2015 Tom Hughes <tom@compton.nu> - 1.7.3-1
- Update to 1.7.3 upstream release
- Switch to %%license for the license file

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar  5 2015 Tom Hughes <tom@compton.nu> - 1.4.0-1
- Update to 1.4.0 upstream release

* Wed Mar  4 2015 Tom Hughes <tom@compton.nu> - 1.3.2-1
- Update to 1.3.2 upstream release

* Mon Jan 19 2015 Tom Hughes <tom@compton.nu> - 1.3.1-1
- Update to 1.3.1 upstream release

* Wed Dec 17 2014 Tom Hughes <tom@compton.nu> - 1.3.0-1
- Update to 1.3.0 upstream release

* Thu Nov 20 2014 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Update to 1.1.0 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun  2 2014 Tom Hughes <tom@compton.nu> - 1.0.1-1
- Update to 1.0.1 upstream release

* Fri May 23 2014 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Update to 1.0.0 upstream release

* Thu Apr  3 2014 Tom Hughes <tom@compton.nu> - 0.6.0-1
- Update to 0.6.0 upstream release

* Fri Mar  7 2014 Tom Hughes <tom@compton.nu> - 0.5.3-1
- Update to 0.5.3 upstream release

* Sun Jan 26 2014 Tom Hughes <tom@compton.nu> - 0.5.2-1
- Initial build of 0.5.2
