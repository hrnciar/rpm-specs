%{?nodejs_find_provides_and_requires}

Name:           nodejs-i2c
Version:        0.2.3
Release:        16%{?dist}
Summary:        Node.js native bindings for i2c-dev
# package.json indicates BSD, but no license file included
# upstream notified in https://github.com/korevec/node-i2c/pull/9
# we're including a copy of the BSD license in order to comply with the terms of 
# the BSD license, as required by:
# https://fedoraproject.org/wiki/Packaging:LicensingGuidelines#License_Text
#
# src/i2c-dev.(cc|h) are GPLv2+, everything else is BSD
License:        BSD and GPLv2+
URL:            https://github.com/korevec/node-i2c
Source0:        https://registry.npmjs.org/i2c/-/i2c-%{version}.tgz
# Update for Node.js 12.x support
Patch0:         nodejs-i2c-node12.patch
ExclusiveArch:  %{nodejs_arches}

BuildRequires:  nodejs-devel
BuildRequires:  node-gyp

BuildRequires:  npm(nan) >= 2.3.5
BuildRequires:  npm(coffee-script)
BuildRequires:  npm(underscore)

%description
%{summary}.

Plays well with Raspberry Pi and Beaglebone.


%prep
%autosetup -p1 -n package
%nodejs_fixdep --dev --move nan
%nodejs_fixdep bindings "^1.2.1"
%nodejs_fixdep coffee-script "^1.9.1"
%nodejs_fixdep underscore "^1.8.2"


%build
%nodejs_symlink_deps --build
%set_build_flags
node-gyp rebuild


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/i2c
cp -pr lib main.js package.json %{buildroot}%{nodejs_sitelib}/i2c
mkdir -p %{buildroot}%{nodejs_sitelib}/i2c/build/Release
cp -pr build/Release/i2c.node %{buildroot}%{nodejs_sitelib}/i2c/build/Release
chmod 0755 %{buildroot}%{nodejs_sitelib}/i2c/build/Release/i2c.node
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs -e "require('./')"


%files
%doc README.md examples
%license LICENSE
%{nodejs_sitelib}/i2c


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Tom Hughes <tom@compton.nu> - 0.2.3-14
- Rebuild for Node.js 12.4.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Tom Hughes <tom@compton.nu> - 0.2.3-11
- Rebuild for Node.js 10.5.0

* Thu Mar  8 2018 Tom Hughes <tom@compton.nu> - 0.2.3-9
- Relax npm(bindings) dependency

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Tom Hughes <tom@compton.nu> - 0.2.3-7
- Export CFLAGS to get standard optimisation flags
- Export LDFLAGS for hardened build support
- Allow undefined symbols in the shared object

* Thu Aug 10 2017 Tom Hughes <tom@compton.nu> - 0.2.3-6.1
- Rebuild for Node.js 8.3.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Tom Hughes <tom@compton.nu> - 0.2.3-3.1
- Rebuild for Node.js 8.1.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 29 2016 Tom Hughes <tom@compton.nu> - 0.2.3-2
- Rebuild for Node.js 6.5.0

* Thu Jun 16 2016 Tom Hughes <tom@compton.nu> - 0.2.3-1
- Update to 0.2.3 upstream release

* Mon May 09 2016 Stephen Gallagher <sgallagh@redhat.com> - 0.2.1-6.1
- Rebuild for Node.js 6.1.0 upgrade

* Tue Mar 29 2016 Tom Hughes <tom@compton.nu> - 0.2.1-6
- Rebuild for Node.js 5.x

* Wed Mar 23 2016 Tom Hughes <tom@compton.nu> - 0.2.1-5
- Rebuild for Node.js 4.4.x

* Wed Feb 10 2016 Tom Hughes <tom@compton.nu> - 0.2.1-4
- Rebuild for Node.js 4.3.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Stephen Gallagher <sgallagh@redhat.com> - 0.2.1-2
- Rebuild against the correct nodejs(abi)

* Wed Dec  2 2015 Tom Hughes <tom@compton.nu> - 0.2.1-1
- Update to 0.2.1 upstream release
- Patch for nodejs 4.2 support

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.4-12
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.4-9
- fix version of npm(underscore) dependency

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.4-8
- put nodejs_default_filter before nodejs_find_provides_and_requires

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.4-7
- fix version of npm(bindings) dependency

* Fri Apr 18 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.4-6
- fix version of npm(underscore) dependency

* Fri Feb 14 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.4-5
- rebuild for icu-53 (via v8)

* Sun Jan 19 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.4-4
- fix underscore for 1.5.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.4-2
- add macro for Provides and Requires

* Wed Jul 10 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.4-1
- update to upstream release 0.1.4
- fix version of coffee-script dependency

* Wed Jun 26 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.3-2
- fix permissions on shared object

* Fri Jun 21 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.3-1
- initial package
