#	The original source of this package contains a font with a forbidden
#		license.
#	The attached source tarball does not contain this font and has been
#		produced from the original by executing the following commands:
#
#	wget https://milki.include-once.org/captcha/captcha-%{version}.tgz
#	tar xzf captcha-%{version}.tgz
#	rm -f captcha-%{version}/MyUnderwood.*
#	tar czf captcha-%{version}.nofont.tar.gz captcha-%{version}
#
#	SHA1 sums:
#	facfe0f57adddd4e278852abd5499177f03a0c1f captcha-2.3.tgz
#	5387d2972766d5109cb4ae8572350a2229a89705 captcha-2.3.nofont.tar.gz

%global fontdir		%{_datadir}/fonts/*

Name:		php-captchaphp
Summary:	PHP very user-friendly CAPTCHA solution
Version:	2.3
Release:	16%{?dist}

#	Public Domain or any FOSS License, see README
#	We're choosing MIT because it is universally compatible with other FOSS 
#		licenses.
License:	Public Domain or MIT

URL:		https://milki.include-once.org/captcha/
Source0:	captcha-%{version}.nofont.tar.gz
Patch1:		captcha-2.3-24pre.patch
Patch2:		captcha-2.3-emptypathparent.patch
Patch3:		captcha-2.3-php71.patch
Requires:	php-gd >= 4.3.2
Requires:	fontpackages-filesystem
Buildarch:	noarch

%description
  This PHP script provides a very user-friendly CAPTCHA solution.
You can easily embed it into your <form> generation scripts to
prevent spam-bot access.

It strives to be accessible and implements an arithmetic riddle
as alternative for visually impaired users. It does not require
cookies, but makes use of "AJAX" to give users visual feedback
for solving the CAPTCHA. It grants access fuzzily (when single
letters were outguessed) instead of frustrating people. And it
can be customized rather easily.


#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------

%setup -q -n captcha-%{version}
%patch1 -p 1
%patch2 -p 1
%patch3 -p 1


#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------

#	Replace the font path by our (arbitrary) default font directory.

sed -i -e "/CAPTCHA_FONT_DIR/s#,.*#, '%{fontdir}/');#" captcha.php


#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------

#	Install directory.

install -p -d -m 755 "${RPM_BUILD_ROOT}/%{_datadir}/php/captchaphp/"


#	Install file.

install -p -m 644 captcha.php "${RPM_BUILD_ROOT}/%{_datadir}/php/captchaphp/"


#-------------------------------------------------------------------------------
%files
#-------------------------------------------------------------------------------

%doc README index.php
%{_datadir}/php/captchaphp


#-------------------------------------------------------------------------------
%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

#-------------------------------------------------------------------------------

* Mon Jul 22 2019 Patrick Monnerat <patrick@monnerat.net> 2.3-14
- Patch "emptypathparent" to fix handling of initial ".." in path.
- Patch "php71" for PHP 7.1 compatibility.
- Modernize spec file.
- Do not require specific font path.
  https://bugzilla.redhat.com/show_bug.cgi?id=1731699

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue May  3 2011 Patrick Monnerat <pm@datasphere.ch> 2.3-1
- New upstream release.
- Patch "24pre" to apply pre 2.4 updates.

* Mon Jun 14 2010 Patrick Monnerat <pm@datasphere.ch> 2.2-2
- Using MIT license.

* Tue May 25 2010 Patrick Monnerat <pm@datasphere.ch> 2.2-1
- New upstream release.

* Mon Jul 13 2009 Patrick Monnerat <pm@datasphere.ch> 2.0-3
- Depends on font directory rather than font package: this circumvents the
  font package name change done between F10 and F11.

* Tue Jun 23 2009 Patrick Monnerat <pm@datasphere.ch> 2.0-2
- Move class files to a package-specific sub-directory.
- Get rid of build dependence on "ed".

* Mon Jun  8 2009 Patrick Monnerat <pm@datasphere.ch> 2.0-1
- Initial RPM spec file.
- Patch "nodeferror" to allow predefining CAPTCHA_* constants without
  issuing an error at include time.
- Patch "https" to detect SSL use automatically.
- Patch "undef" to fix an undefined index error.
- Patch "directcall" to improve direct call detection.
- Patch "translatable" to make module translatable through the use of
  additional CAPTCHA_* defines for texts.
- Font included in original package has an incompatible license: thus it
  is not packaged. Instead, we use a reasonable default ttf font package and
  directory.
