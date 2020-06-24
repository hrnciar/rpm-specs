%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       nodejs-node-expat
Version:    2.3.18
Release:    4%{?dist}
Summary:    Fast libexpat XML SAX parser binding for Node.js
License:    MIT
URL:        https://github.com/node-xmpp/node-expat
Source0:    https://github.com/node-xmpp/node-expat/archive/v%{version}/node-expat-%{version}.tar.gz
# Use the system expat library
Patch0:     %{name}-2.3.18-system-expat.patch
# https://github.com/node-xmpp/node-expat/issues/125
Patch1:     %{name}-2.3.18-timing.patch

BuildRequires:  expat-devel
BuildRequires:  nodejs-packaging
BuildRequires:  node-gyp
BuildRequires:  npm(nan) >= 2.0.9

%if 0%{?enable_tests}
BuildRequires:  npm(vows)
BuildRequires:  npm(bindings)
BuildRequires:  npm(debug)
BuildRequires:  npm(iconv)
%endif

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches}
%else
ExclusiveArch: %{ix86} x86_64 %{arm}
%endif

%description
%{summary}.


%prep
%autosetup -p 1 -n node-expat-%{version}
%nodejs_fixdep bindings "^1.3.0"
rm -rf deps/


%build
%nodejs_symlink_deps --build
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags} -Wl,-z,undefs"
node-gyp rebuild


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/node-expat
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/node-expat
mkdir -p %{buildroot}%{nodejs_sitelib}/node-expat/build
install -p -m0755 build/Release/node_expat.node \
    %{buildroot}%{nodejs_sitelib}/node-expat/build/node_expat.node
sed -i -e 's|build/Release|build|g' \
    %{buildroot}%{nodejs_sitelib}/node-expat/lib/node-expat.js

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/vows/bin/vows --spec ./test/**/*.js
%endif


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/node-expat


%changelog
* Mon May 11 2020 Tom Hughes <tom@compton.nu> - 2.3.18-4
- Update npm(bindings) dependency

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Tom Hughes <tom@compton.nu> - 2.3.18-1
- Update to 2.3.18 upstream release

* Fri Jun 14 2019 Tom Hughes <tom@compton.nu> - 2.3.11-19
- Rebuild for Node.js 12.4.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Tom Hughes <tom@compton.nu> - 2.3.11-16
- Rebuild for Node.js 10.5.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Tom Hughes <tom@compton.nu> - 2.3.11-14
- Export LDFLAGS for hardened build support
- Allow undefined symbols in the shared object

* Thu Aug 10 2017 Tom Hughes <tom@compton.nu> - 2.3.11-13.2
- Rebuild for Node.js 8.3.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-12.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-11.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Tom Hughes <tom@compton.nu> - 2.3.11-10.2
- Rebuild for Node.js 8.1.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-10.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 29 2016 Tom Hughes <tom@compton.nu> - 2.3.11-9.1
- Rebuild for Node.js 6.5.0

* Mon May 09 2016 Stephen Gallagher <sgallagh@redhat.com> - 2.3.11-8.1
- Rebuild for Node.js 6.1.0 upgrade

* Tue Mar 29 2016 Tom Hughes <tom@compton.nu> - 2.3.11-8
- Rebuild for Node.js 5.x

* Wed Mar 23 2016 Tom Hughes <tom@compton.nu> - 2.3.11-7
- Rebuild for Node.js 4.4.x

* Wed Feb 10 2016 Tom Hughes <tom@compton.nu> - 2.3.11-6
- Rebuild for Node.js 4.3.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec  4 2015 Tom Hughes <tom@compton.nu> - 2.3.11-4
- Rebuild for nodejs 4.2.3

* Wed Dec  2 2015 Tom Hughes <tom@compton.nu> - 2.3.11-3
- Rebuild for nodejs 4.2

* Fri Nov 27 2015 Tom Hughes <tom@compton.nu> - 2.3.11-2
- Enable tests

* Mon Nov 23 2015 Tom Hughes <tom@compton.nu> - 2.3.11-1
- Update to 2.3.11 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1.4-7
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.4-4
- fix nan dep properly

* Sun May 25 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.4-3
- rebuild to use nodejs-nan0
- copy correct version of nan
- fix nan dep

* Mon Apr 21 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.1.4-2
- fix version of npm(nan) dependency

* Fri Apr 18 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.1.4-2
- update to upstream release 2.1.4

* Sun Jul 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.0.0-6
- add ExclusiveArch logic

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.0-5
- rebuild for missing npm(node-expat) provides on EL6

* Wed Mar 20 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.0.0-4
- remove v8 dependencies which are now automatic

* Tue Mar 12 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.0.0-3
- bump v8 version for nodejs-0.10.0

* Sun Mar 10 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.0.0-2
- fix file permissions
- link against system expat

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.0.0-1
- initial package
