Name:           nodejs-sqlite3
Version:        4.2.0
Release:        1%{?dist}
Summary:        Asynchronous, non-blocking SQLite3 bindings for Node.js

License:        BSD
URL:            https://github.com/mapbox/node-sqlite3
Source0:        https://github.com/mapbox/node-sqlite3/archive/v%{version}/%{name}-%{version}.tar.gz
# Patch out use node-pre-gyp
Patch0:         nodejs-sqlite3-pregyp.patch
# Patch out setting of rpath
Patch1:         nodejs-sqlite3-rpath.patch
# Fix for mocha 2.x support
Patch2:         nodejs-sqlite3-mocha.patch
ExclusiveArch:  %{nodejs_arches}

BuildRequires:  nodejs-devel
BuildRequires:  node-gyp
BuildRequires:  sqlite-devel >= 3.10.2-3

BuildRequires:  npm(nan) >= 2.12.1
BuildRequires:  npm(mocha)

%{?nodejs_default_filter}

%description
%{summary}.


%prep
%autosetup -p 1 -n node-sqlite3-%{version}
%nodejs_fixdep --dev --move nan
rm -rf deps/* node_modules
echo "{}" > deps/common-sqlite.gypi


%build
%nodejs_symlink_deps --build
%set_build_flags
node-gyp configure -- -Dsqlite=/usr -Dmodule_name=node_sqlite3 -Dmodule_path=lib/binding
node-gyp build


%install
mkdir -p %{buildroot}/%{nodejs_sitearch}/sqlite3
cp -pr package.json lib %{buildroot}/%{nodejs_sitearch}/sqlite3
%nodejs_symlink_deps


%check
%ifnarch s390x
%nodejs_symlink_deps --check
%{__nodejs} test/support/createdb.js
mkdir test/tmp
NODE_PATH=lib %{nodejs_sitelib}/mocha/bin/mocha -R spec -t 1000000
%endif


%files
%doc README.md CHANGELOG.md examples
%license LICENSE
%{nodejs_sitearch}/sqlite3


%changelog
* Mon Apr 27 2020 Tom Hughes <tom@compton.nu> - 4.2.0-1
- Update to 4.2.0 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec  5 2019 Tom Hughes <tom@compton.nu> - 4.1.1-1
- Update to 4.1.1 upstream release

* Fri Aug 23 2019 Tom Hughes <tom@compton.nu> - 4.1.0-1
- Update to 4.1.0 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Tom Hughes <tom@compton.nu> - 4.0.9-2
- Rebuild for Node.js 12.4.0

* Thu Jun 13 2019 Tom Hughes <tom@compton.nu> - 4.0.9-1
- Update to 4.0.9 upstream release

* Tue May 14 2019 Tom Hughes <tom@compton.nu> - 4.0.8-1
- Update to 4.0.8 upstream release

* Wed May  8 2019 Tom Hughes <tom@compton.nu> - 4.0.7-1
- Update to 4.0.7 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Tom Hughes <tom@compton.nu> - 4.0.2-1
- Update to 4.0.2 upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 24 2018 Tom Hughes <tom@compton.nu> - 4.0.1-1
- Update to 4.0.1 upstream release

* Fri Jun 22 2018 Tom Hughes <tom@compton.nu> - 4.0.0-3
- Rebuild for Node.js 10.5.0

* Fri Mar 16 2018 Tom Hughes <tom@compton.nu> - 4.0.0-1
- Update to 4.0.0 upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Tom Hughes <tom@compton.nu> - 3.1.13-2
- Allow undefined symbols in the shared object

* Fri Sep 29 2017 Tom Hughes <tom@compton.nu> - 3.1.13-1
- Update to 3.1.13 upstream release

* Sat Sep 23 2017 Tom Hughes <tom@compton.nu> - 3.1.12-1
- Update to 3.1.12 upstream release

* Wed Sep 13 2017 Tom Hughes <tom@compton.nu> - 3.1.11-1
- Update to 3.1.11 upstream release

* Sat Sep  9 2017 Tom Hughes <tom@compton.nu> - 3.1.10-1
- Update to 3.1.10 upstream release

* Sat Aug 12 2017 Tom Hughes <tom@compton.nu> - 3.1.9-1
- Update to 3.1.9 upstream release

* Thu Aug 10 2017 Tom Hughes <tom@compton.nu> - 3.1.8-5.1
- Rebuild for Node.js 8.3.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Tom Hughes <tom@compton.nu> - 3.1.8-2.1
- Rebuild for Node.js 8.1.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 28 2016 Tom Hughes <tom@compton.nu> - 3.1.8-1
- Update to 3.1.8 upstream release

* Tue Oct 25 2016 Tom Hughes <tom@compton.nu> - 3.1.7-1
- Update to 3.1.7 upstream release

* Thu Oct  6 2016 Tom Hughes <tom@compton.nu> - 3.1.5-1
- Update to 3.1.5 upstream release

* Mon Aug 29 2016 Tom Hughes <tom@compton.nu> - 3.1.4-2
- Rebuild for Node.js 6.5.0

* Mon May 16 2016 Tom Hughes <tom@compton.nu> - 3.1.4-1
- Update to 3.1.4 upstream release

* Mon May 09 2016 Stephen Gallagher <sgallagh@redhat.com> - 3.1.3-1.1
- Rebuild for Node.js 6.1.0 upgrade

* Sat Apr  2 2016 Tom Hughes <tom@compton.nu> - 3.1.3-1
- Update to 3.1.3 upstream release

* Tue Mar 29 2016 Tom Hughes <tom@compton.nu> - 3.1.2-3
- Rebuild for Node.js 5.x

* Wed Mar 23 2016 Tom Hughes <tom@compton.nu> - 3.1.2-2
- Rebuild for Node.js 4.4.x

* Tue Mar 22 2016 Tom Hughes <tom@compton.nu> - 3.1.2-1
- Update to 3.1.2 upstream release

* Wed Feb 10 2016 Tom Hughes <tom@compton.nu> - 3.1.1-8
- Rebuild for Node.js 4.3.x

* Mon Feb  8 2016 Tom Hughes <tom@compton.nu> - 3.1.1-7
- Enable JSON test

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec  4 2015 Tom Hughes <tom@compton.nu> - 3.1.1-5
- Rebuild for nodejs 4.2.3

* Wed Dec  2 2015 Tom Hughes <tom@compton.nu> - 3.1.1-4
- Rebuild for nodejs 4.2

* Wed Nov 25 2015 Tom Hughes <tom@compton.nu> - 3.1.1-3
- Export LDFLAGS for hardened build support

* Mon Nov 23 2015 Tom Hughes <tom@compton.nu> - 3.1.1-2
- Updated to build using nan 2.x

* Tue Nov  3 2015 Tom Hughes <tom@compton.nu> - 3.1.1-1
- Update to 3.1.1 upstream release

* Thu Sep 10 2015 Tom Hughes <tom@compton.nu> - 3.1.0-1
- Update to 3.1.0 upstream release

* Sun Aug  9 2015 Tom Hughes <tom@compton.nu> - 3.0.10-1
- Update to 3.0.10 upstream relase

* Tue Jul 14 2015 Tom Hughes <tom@compton.nu> - 3.0.9-1
- Update to 3.0.9 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May  9 2015 Tom Hughes <tom@compton.nu> - 3.0.8-1
- Update to 3.0.8 upstream release

* Wed May  6 2015 Tom Hughes <tom@compton.nu> - 3.0.7-1
- Update to 3.0.7 upstream release

* Tue May  5 2015 Tom Hughes <tom@compton.nu> - 3.0.6-1
- Update to 3.0.6 upstream release

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.0.5-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 11 2015 Tom Hughes <tom@compton.nu> - 3.0.5-1
- Update to 3.0.5 upstream releae

* Fri Nov 14 2014 Tom Hughes <tom@compton.nu> - 3.0.4-1
- Update to 3.0.4 upstream release

* Tue Sep 30 2014 Tom Hughes <tom@compton.nu> - 3.0.2-1
- Update to 3.0.2 upstream release

* Mon Sep 22 2014 Tom Hughes <tom@compton.nu> - 3.0.0-1
- Update to 3.0.0 upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug  7 2014 Tom Hughes <tom@compton.nu> - 2.2.7-1
- Update to 2.2.7 upstream release

* Wed Jul 16 2014 Tom Hughes <tom@compton.nu> - 2.2.4-1
- Update to 2.2.4 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Tom Hughes <tom@compton.nu> - 2.2.3-1
- Update to 2.2.3 upstream release

* Mon Apr 14 2014 Tom Hughes <tom@compton.nu> - 2.2.2-1
- Update to 2.2.2 upstream release
- Switch to source from github as npm no longer includes tests

* Fri Feb 14 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.2.0-3
- rebuild for icu-53 (via v8)

* Wed Jan 15 2014 Tom Hughes <tom@compton.nu> - 2.2.0-2
- Remove nodejs-pre-gyp dependency

* Tue Jan 14 2014 Tom Hughes <tom@compton.nu> - 2.2.0-1
- Update to 2.2.0 upstream release

* Sun Nov  3 2013 Tom Hughes <tom@compton.nu> - 2.1.19-1
- Update to 2.1.19 upstream release

* Wed Oct 30 2013 Tom Hughes <tom@compton.nu> - 2.1.18-1
- Update to 2.1.18 upstream release

* Thu Sep 12 2013 Tom Hughes <tom@compton.nu> - 2.1.17-1
- Update to 2.1.17 upstream release

* Tue Sep 10 2013 Tom Hughes <tom@compton.nu> - 2.1.16-1
- Update to 2.1.16 upstream release

* Thu Aug  8 2013 Tom Hughes <tom@compton.nu> - 2.1.15-1
- Update to 2.1.15 upstream release

* Sat Aug  3 2013 Tom Hughes <tom@compton.nu> - 2.1.14-3
- Increase test timeout further for ARM builds

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Tom Hughes <tom@compton.nu> - 2.1.14-1
- Update to 2.1.14 upstream release

* Mon Jul 15 2013 Tom Hughes <tom@compton.nu> - 2.1.12-1
- Update to 2.1.12 upstream release
- Increase test timeout for ARM builds

* Wed Jun 19 2013 Tom Hughes <tom@compton.nu> - 2.1.10-1
- Update to 2.1.10 upstream release

* Thu Jun 13 2013 Tom Hughes <tom@compton.nu> - 2.1.9-1
- Update to 2.1.9 upstream release
- Drop patches which have been merged upstream

* Thu Mar 21 2013 Tom Hughes <tom@compton.nu> - 2.1.7-1
- Update to 2.1.7 upstream release
- Switch to running tests using mocha
- Filter out provide for Node.js native extension

* Wed Mar 13 2013 Tom Hughes <tom@compton.nu> - 2.1.5-5
- Restrict supported architectures using ExclusiveArch
- Rebuild against node 0.10

* Tue Mar  5 2013 Tom Hughes <tom@compton.nu> - 2.1.5-4
- Enable tests

* Mon Mar  4 2013 Tom Hughes <tom@compton.nu> - 2.1.5-3
- Fix gcc 4.8 compilation issues

* Sat Mar  2 2013 Tom Hughes <tom@compton.nu> - 2.1.5-2
- Fix permissions on node_sqite3.node
- Improve description

* Sun Feb 10 2013 Tom Hughes <tom@compton.nu> - 2.1.5-1
- Initial build of 2.1.5
