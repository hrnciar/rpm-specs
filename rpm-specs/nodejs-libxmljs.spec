%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-libxmljs
Version:        0.19.7
Release:        1%{?dist}
Summary:        Node.js module that provides libxml bindings for the v8 javascript engine

License:        MIT
URL:            https://www.npmjs.com/package/libxmljs
Source0:        https://registry.npmjs.org/libxmljs/-/libxmljs-%{version}.tgz
# Remove dependency on bundled libxml2
Patch0:         nodejs-libxmljs-libxml.patch
# Adapt to change in error message in libxml2
Patch1:         nodejs-libxmljs-error.patch
ExclusiveArch:  %{nodejs_arches}

BuildRequires:  nodejs-packaging
BuildRequires:  node-gyp
BuildRequires:  libxml2-devel
BuildRequires:  npm(nan) >= 2.14.0

%if 0%{?enable_tests}
BuildRequires:  npm(bindings)
BuildRequires:  npm(nodeunit)
%endif

%description
%{summary}.


%prep
%autosetup -p 1 -n package
%nodejs_fixdep bindings
%nodejs_fixdep --dev --move nan
%nodejs_fixdep --remove node-pre-gyp
rm -rf node_modules vendor


%build
%nodejs_symlink_deps --build
%set_build_flags
node-gyp configure
node-gyp build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/libxmljs
cp -pr package.json index.js lib/ \
    %{buildroot}%{nodejs_sitelib}/libxmljs
mkdir -p %{buildroot}%{nodejs_sitelib}/libxmljs/build
install -p -D -m0755 build/Release/lib.target/xmljs.node \
    %{buildroot}%{nodejs_sitelib}/libxmljs/build/xmljs.node
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
ln -s Release/lib.target/xmljs.node build/xmljs.node
%__nodejs --expose_gc %{nodejs_sitelib}/nodeunit/bin/nodeunit test
%endif


%files
%doc README.md examples/
%license LICENSE
%{nodejs_sitelib}/libxmljs


%changelog
* Fri Feb  7 2020 Tom Hughes <tom@compton.nu> - 0.19.7-1
- Update to 0.19.7 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Tom Hughes <tom@compton.nu> - 0.19.5-1
- Update to 0.19.5 upstream release

* Fri Jun 14 2019 Tom Hughes <tom@compton.nu> - 0.18.7-8
- Rebuild for Node.js 12.4.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Tom Hughes <tom@compton.nu> - 0.18.7-5
- Rebuild for Node.js 10.5.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Tom Hughes <tom@compton.nu> - 0.18.7-2
- Allow undefined symbols in the shared object

* Thu Aug 10 2017 Tom Hughes <tom@compton.nu> - 0.18.7-1
- Update to 0.18.7 upstream release
- Disable failing memory leak tests

* Thu Aug 10 2017 Tom Hughes <tom@compton.nu> - 0.18.2-6.1
- Rebuild for Node.js 8.3.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Tom Hughes <tom@compton.nu> - 0.18.2-3.1
- Rebuild for Node.js 8.1.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Tom Hughes <tom@compton.nu> - 0.18.2-2
- Drop node-pre-gyp dependency

* Thu Jan 12 2017 Tom Hughes <tom@compton.nu> - 0.18.2-1
- Update to 0.18.2 upstream release

* Thu Dec 22 2016 Tom Hughes <tom@compton.nu> - 0.18.0-3
- Relax tolerance in memory tests

* Mon Aug 29 2016 Tom Hughes <tom@compton.nu> - 0.18.0-2
- Rebuild for Node.js 6.5.0

* Mon Jul 11 2016 Tom Hughes <tom@compton.nu> - 0.18.0-1
- Update to 0.18.0 upstream release

* Mon May 09 2016 Stephen Gallagher <sgallagh@redhat.com> - 0.17.1-4.1
- Rebuild for Node.js 6.1.0 upgrade

* Tue Mar 29 2016 Tom Hughes <tom@compton.nu> - 0.17.1-4
- Rebuild for Node.js 5.x

* Wed Mar 23 2016 Tom Hughes <tom@compton.nu> - 0.17.1-3
- Rebuild for Node.js 4.4.x

* Wed Feb 10 2016 Tom Hughes <tom@compton.nu> - 0.17.1-2
- Rebuild for Node.js 4.3.x

* Wed Feb  3 2016 Tom Hughes <tom@compton.nu> - 0.17.1-1
- Update to 0.17.1 upstream release

* Tue Jan 19 2016 Tom Hughes <tom@compton.nu> - 0.17.0-1
- Update to 0.17.0 upstream release

* Thu Dec  3 2015 Tom Hughes <tom@compton.nu> - 0.15.0-2
- Rebuild for nodejs 4.2

* Thu Dec  3 2015 Tom Hughes <tom@compton.nu> - 0.15.0-1
- Update to 0.15.0 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.0-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.9.0-1
- update to upstream release 0.9.0

* Fri Feb 14 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.1-4
- rebuild for icu-53 (via v8)

* Sat Jul 27 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.8.1-3
- add ExclusiveArch logic

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.1-2
- restrict to compatible arches

* Sat May 25 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.8.1-1
- update to upstream release 0.8.1

* Sun Mar 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.1-1
- update to upstream release 0.7.1
- make the versioned dependency on npm(bindings) less specific
- remove dependencies on v8 as these are now automatic

* Sun Feb 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.0-2
- add npm(bindings) to BuildRequires

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.0-1
- initial package
