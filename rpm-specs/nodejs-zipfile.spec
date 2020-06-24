Name:           nodejs-zipfile
Version:        0.5.12
Release:        6%{?dist}
Summary:        C++ library for handling zipfiles in Node.js

License:        BSD
URL:            https://github.com/mapbox/node-zipfile
Source0:        https://github.com/mapbox/node-zipfile/archive/v%{version}/node-zipfile-%{version}.tar.gz
Patch0:         nodejs-zipfile-pregyp.patch
# https://github.com/mapbox/node-zipfile/pull/82
Patch1:         nodejs-zipfile-node12.patch
ExclusiveArch:  %{nodejs_arches}

BuildRequires:  nodejs-devel
BuildRequires:  node-gyp
BuildRequires:  libzip-devel >= 0.11.2
BuildRequires:  zlib-devel

BuildRequires:  npm(nan) >= 2.14.0
BuildRequires:  npm(mocha)
BuildRequires:  npm(mkdirp)

%{?nodejs_default_filter}

%description
Bindings to libzip for handling zipfile archives in Node.js.


%prep
%autosetup -p 1 -n node-zipfile-%{version}
%nodejs_fixdep -r nan
%nodejs_fixdep --dev nan "^2.4.0"
rm -rf deps/* node_modules
echo "{}" > deps/common-libzip.gypi


%build
%nodejs_symlink_deps --build
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags} -Wl,-z,undefs"
node-gyp configure -- -Dshared_libzip=true -Dmodule_name=zipfile -Dmodule_path=lib/binding
node-gyp build


%install
mkdir -p %{buildroot}/%{nodejs_sitearch}/zipfile
cp -pr package.json lib %{buildroot}/%{nodejs_sitearch}/zipfile
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha -R spec


%files
%doc README.md
%license LICENSE.txt
%{nodejs_sitearch}/zipfile


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Tom Hughes <tom@compton.nu> - 0.5.12-4
- Rebuild for Node.js 12.4.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul  5 2018 Tom Hughes <tom@compton.nu> - 0.5.12-1
- Update to 0.5.12 upstream release

* Fri Jun 22 2018 Tom Hughes <tom@compton.nu> - 0.5.11-10
- Rebuild for Node.js 10.5.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Tom Hughes <tom@compton.nu> - 0.5.11-7
- Allow undefined symbols in the shared object

* Thu Aug 10 2017 Tom Hughes <tom@compton.nu> - 0.5.11-6.1
- Rebuild for Node.js 8.3.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Tom Hughes <tom@compton.nu> - 0.5.11-3.1
- Rebuild for Node.js 8.1.2

* Tue Feb 28 2017 Remi Collet <remi@fedoraproject.org> - 0.5.11-3
- rebuild for new libzip

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Tom Hughes <tom@compton.nu> - 0.5.11-1
- Update to 0.5.11 upstream release

* Wed Dec 14 2016 Tom Hughes <tom@compton.nu> - 0.5.10-1.1
- Update to 0.5.10 upstream release

* Mon Aug 29 2016 Tom Hughes <tom@compton.nu> - 0.5.9-8.1
- Rebuild for Node.js 6.5.0

* Mon May 09 2016 Stephen Gallagher <sgallagh@redhat.com> - 0.5.9-7.1
- Rebuild for Node.js 6.1.0 upgrade

* Tue Mar 29 2016 Tom Hughes <tom@compton.nu> - 0.5.9-7
- Rebuild for Node.js 5.x

* Wed Mar 23 2016 Tom Hughes <tom@compton.nu> - 0.5.9-6
- Rebuild for Node.js 4.4.x

* Wed Feb 10 2016 Tom Hughes <tom@compton.nu> - 0.5.9-5
- Rebuild for Node.js 4.3.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec  4 2015 Tom Hughes <tom@compton.nu> - 0.5.9-3
- Rebuild for nodejs 4.2.3

* Wed Dec  2 2015 Tom Hughes <tom@compton.nu> - 0.5.9-2
- Rebuild for nodejs 4.2

* Wed Dec  2 2015 Tom Hughes <tom@compton.nu> - 0.5.9-1
- Update to 0.5.9 upstream release

* Wed Nov 25 2015 Tom Hughes <tom@compton.nu> - 0.5.7-6
- Export LDFLAGS for hardened build support

* Mon Nov 23 2015 Tom Hughes <tom@compton.nu> - 0.5.7-5
- Update npm(nan) dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Remi Collet <remi@fedoraproject.org> - 0.5.7-3
- rebuild for new libzip

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.7-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 19 2015 Tom Hughes <tom@compton.nu> - 0.5.7-1
- Update to 0.5.7 upstream release

* Wed Jan 14 2015 Tom Hughes <tom@compton.nu> - 0.5.5-1
- Update to 0.5.5 upstream release

* Thu Nov 20 2014 Tom Hughes <tom@compton.nu> - 0.5.4-1
- Update to 0.5.4 upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug  1 2014 Tom Hughes <tom@compton.nu> - 0.5.3-1
- Update to 0.5.3 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Tom Hughes <tom@compton.nu> - 0.5.2-1
- Update to 0.5.2 upstream release
- Switch to source from github as npm no longer includes tests

* Fri Mar 14 2014 Tom Hughes <tom@compton.nu> - 0.5.0-1
- Update to 0.5.0 upstream release

* Fri Feb 14 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.3-2
- rebuild for icu-53 (via v8)

* Fri Dec 20 2013 Tom Hughes <tom@compton.nu> - 0.4.3-1
- Update to 0.4.3 upstream release

* Wed Oct 30 2013 Tom Hughes <tom@compton.nu> - 0.4.2-1
- Update to 0.4.2 upstream release

* Tue Oct  1 2013 Tom Hughes <tom@compton.nu> - 0.4.1-1
- Update to 0.4.1 upstream release

* Wed Aug 21 2013 Remi Collet <rcollet@redhat.com> - 0.4.0-2
- rebuild for new libzip

* Sun Aug 11 2013 Tom Hughes <tom@compton.nu> - 0.4.0-1
- Update to 0.4.0 upstream release
- Update to latest nodejs packaging standards

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr  3 2013 Tom Hughes <tom@compton.nu> - 0.3.4-4
- Filter out provide for Node.js native extension
- Enable tests

* Wed Mar 13 2013 Tom Hughes <tom@compton.nu> - 0.3.4-3
- Restrict supported architectures using ExclusiveArch
- Rebuild against node 0.10

* Sat Mar  2 2013 Tom Hughes <tom@compton.nu> - 0.3.4-2
- Fix permissions on _zipfile.node
- BuildRequire zlib-devel
- BuildRequire mkdirp for tests
- Link node_modules for tests
- Set NODE_PATH when running tests

* Sun Feb 10 2013 Tom Hughes <tom@compton.nu> - 0.3.4-1
- Initial build of 0.3.4
