%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-node-stringprep
Version:        0.8.0
Release:        15%{?dist}
Summary:        ICU StringPrep profiles for Node.js

License:        MIT
URL:            https://github.com/node-xmpp/node-stringprep
Source0:        https://registry.npmjs.org/node-stringprep/-/node-stringprep-%{version}.tgz
# Allow nodejs 4
Patch0:         nodejs-node-stringprep-engine.patch
# Fix to work with node 12
Patch1:         nodejs-node-stringprep-node12.patch
# Workaround strange issue building in koji
Patch2:         nodejs-node-stringprep-koji.patch
ExclusiveArch:  %{nodejs_arches}

BuildRequires:  nodejs-devel
BuildRequires:  node-gyp
BuildRequires:  libicu-devel

BuildRequires:  npm(nan) >= 2.1.0
BuildRequires:  npm(bindings)

# The project uses Grunt, but there isn't anything fancy being done so we
# can just use mocha directly.
%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(should)
BuildRequires:  npm(proxyquire)
%endif

%description
This module exposes predefined Unicode normalization functions that are
required by many protocols. This is just a binding to ICU, which is said
to be fast.


%prep
%autosetup -p1 -n package
%nodejs_fixdep bindings "^1.3.0"
%nodejs_fixdep debug "^2.2.0"
%nodejs_fixdep --dev --move nan


%build
%nodejs_symlink_deps --build
%set_build_flags
CXXFLAGS="${CXXFLAGS} -DUCHAR_TYPE=uint16_t"
node-gyp configure
node-gyp build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/node-stringprep
cp -p package.json index.js \
    %{buildroot}%{nodejs_sitelib}/node-stringprep
install -p -D -m0755 build/Release/node_stringprep.node \
    %{buildroot}%{nodejs_sitelib}/node-stringprep/build/node_stringprep.node
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
# fallback test needs to be run in a separate process
/usr/bin/mocha -R spec --ui tdd --require should test/fallback.js
/usr/bin/mocha -R spec --ui tdd test/leakcheck.js test/toascii.js test/tounicode.js
%endif


%files
%doc README.markdown
%license LICENSE
%{nodejs_sitelib}/node-stringprep


%changelog
* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 0.8.0-15
- Rebuild for ICU 67

* Mon May 11 2020 Tom Hughes <tom@compton.nu> - 0.8.0-14
- Update npm(bindings) dependency

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 0.8.0-12
- Rebuild for ICU 65

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Tom Hughes <tom@compton.nu> - 0.8.0-10
- Rebuild for Node.js 12.4.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 0.8.0-8
- Rebuild for ICU 63

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 0.8.0-7
- Rebuild for ICU 62

* Fri Jun 22 2018 Tom Hughes <tom@compton.nu> - 0.8.0-6
- Rebuild for Node.js 8.3.0

* Mon Apr 30 2018 Tom Hughes <tom@compton.nu> - 0.8.0-5
- Correct name of installed binary module

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 0.8.0-4
- Rebuild for ICU 61.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Tom Hughes <tom@compton.nu> - 0.8.0-2
- Move nan to be a build time dependency

* Tue Jan 23 2018 Tom Hughes <tom@compton.nu> - 0.8.0-1
- Update to 0.8.0 upstream release
- Force icu to use uint16_t for characters
- Allow undefined symbols in the shared object

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 0.7.3-17
- Rebuild for ICU 60.1

* Mon Oct 30 2017 Tom Hughes <tom@compton.nu> - 0.7.3-16
- Relax npm(debug) dependency

* Thu Aug 10 2017 Tom Hughes <tom@compton.nu> - 0.7.3-15.2
- Rebuild for Node.js 8.3.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-14.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-13.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Tom Hughes <tom@compton.nu> - 0.7.3-12.2
- Rebuild for Node.js 8.1.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-12.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 29 2016 Tom Hughes <tom@compton.nu> - 0.7.3-11.1
- Rebuild for Node.js 6.5.0

* Mon May 09 2016 Stephen Gallagher <sgallagh@redhat.com> - 0.7.3-10.1
- Rebuild for Node.js 6.1.0 upgrade

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 0.7.3-10
- rebuild for ICU 57.1

* Tue Mar 29 2016 Tom Hughes <tom@compton.nu> - 0.7.3-9
- Rebuild for Node.js 5.x

* Wed Mar 23 2016 Tom Hughes <tom@compton.nu> - 0.7.3-8
- Rebuild for Node.js 4.4.x

* Wed Feb 10 2016 Tom Hughes <tom@compton.nu> - 0.7.3-7
- Rebuild for Node.js 4.3.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Tom Hughes <tom@compton.nu> - 0.7.3-5
- Patch package.json to allow nodejs 4

* Mon Dec  7 2015 Tom Hughes <tom@compton.nu> - 0.7.3-4
- Rebuild for nodejs 4.2

* Mon Dec  7 2015 Tom Hughes <tom@compton.nu> - 0.7.3-3
- Patch in support for nan 2.x

* Wed Nov 25 2015 Tom Hughes <tom@compton.nu> - 0.7.3-2
- Export LDFLAGS for hardened build support

* Mon Nov 23 2015 Tom Hughes <tom@compton.nu> - 0.7.3-1
- Update to 0.7.3 upstream release
- Enable tests

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 0.2.3-11
- rebuild for ICU 56.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.3-9
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 0.2.3-8
- rebuild for ICU 54.1

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 0.2.3-7
- rebuild for ICU 53.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.3-4
- patch for new Nan 1.0.0 API

* Sat May 10 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.3-3
- fix version of npm(nan)

* Mon Apr 21 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.3-2
- fix version of npm(nan) and npm(bindings) dependencies

* Sat Apr 19 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.3-1
- update to upstream release 0.2.3

* Fri Feb 14 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.8-2
- rebuild for icu-53 (via v8)

* Sun Jul 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.8-1
- update to upstream release 0.1.8
- add ExclusiveArch logic
- enable tests

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.5-5
- rebuild for missing npm(node-stringprep) provides on EL6

* Sun Mar 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.5-4
- remove npm(bindings) from Requires

* Sun Mar 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.5-3
- remove dependencies on v8 as these are now automatic
- remove redundant comments
- add libicu-devel to BuildRequires
- fix the test in %%check
- move library to %%{nodejs_sitelib}/node-stringprep/node-stringprep.node
  to comply with packaging guidelines

* Thu Feb 14 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.5-2
- make use of %%nodejs_fixdep

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.5-1
- initial package
