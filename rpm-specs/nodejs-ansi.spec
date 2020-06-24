%{?nodejs_find_provides_and_requires}

Name:           nodejs-ansi
Version:        0.3.0
Release:        9%{?dist}
Summary:        ANSI escape codes for Node.js

License:        MIT
URL:            https://github.com/TooTallNate/ansi.js
Source0:        https://registry.npmjs.org/ansi/-/ansi-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging


%description
ansi.js is a module for Node.js that provides an easy-to-use API for writing
ANSI escape codes to Stream instances. ANSI escape codes are used to do fancy
things in a terminal window, like render text in colors, delete characters,
lines, the entire window, or hide and show the cursor, and lots more!


%prep
%setup -q -n package
chmod a-x examples/*.js examples/*/*


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/ansi
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/ansi
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs -e "require('./')"


%files
%doc README.md History.md examples
%{nodejs_sitelib}/ansi


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 0.3.0-1
- Update to 0.3.0 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 06 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.1-1
- update to upstream release 0.2.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-1
- new upstream release 0.2.0

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-8.1
- restrict to compatible arches

* Thu May 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-7.1
- rebuild for missing npm(ansi) provides (RHBZ#968531)

* Fri May 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-7
- remove nonfree image

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-6
- add macro for EPEL6 dependency generation

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-4
- fix permissions correctly

* Fri Jan 11 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-3
- fix permissions in example

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-2
- add missing build section
- fix incorrect summary

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-1
- New upstream release 0.1.2

* Thu Mar 22 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.0-1
- new upstream release 0.1.0

* Fri Mar 16 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.4-1
- initial package
