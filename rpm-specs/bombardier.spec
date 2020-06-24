Name: bombardier
Version:  0.8.3
Release:  13%{?dist}
Summary: The GNU Bombing utility

License: GPLv2+        
URL: http://packages.debian.org/stable/source/bombardier
Source0: http://http.debian.net/debian/pool/main/b/bombardier/bombardier_0.8.3+nmu2.tar.xz
Source1: bombardier.desktop
Source2: bombardier-logo.png
Patch0: bombardier-height.patch
Patch1: bombardier-rpm_opt_flags.patch
#Patch2: bombardier-hof-open-mode.patch
Patch3: bombardier-0.8.2-string-format.patch
BuildRequires: ncurses-devel, desktop-file-utils, gcc
Requires: hicolor-icon-theme


%description
Fly an ncurses plane over an ncurses city, and try to level the buildings.

%prep


%setup -qn bombardier-0.8.3+nmu2

%patch0 -p0
%patch1 -p0
#%patch2 -p0
%patch3 -p0

%build
make CFLAGS="$RPM_OPT_FLAGS"


%install
install -pD -m 755 bombardier %{buildroot}%{_bindir}/bombardier
install -pD -m 644 bombardier.6 %{buildroot}%{_mandir}/man6/bombardier.6

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install            \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps


%files
%{_bindir}/bombardier
%license COPYING
%doc README DEDICATION VERSION
%{_datadir}/applications/bombardier.desktop
%{_datadir}/icons/hicolor/32x32/apps/bombardier-logo.png
%{_mandir}/man6/bombardier.6.gz


%changelog
* Fri Feb 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.8.3-13
- New minor release.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.8.3-9
- BR fix.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.3-6
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Jon Ciesla <limburgher@gmail.com> - 0.8.3-1
- Latest upstream, BZ 1295157.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 11 2014 Jon Ciesla <limburgher@gmail.com> - 0.8.2.2-16
- Patch for format string vulnerability.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.8.2.2-14
- Drop desktop vendor tag.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 08 2008 Jon Ciesla <limb@jcomserv.net> - 0.8.2.2-8
- GCC 4.3 rebuild.

* Fri Aug 17 2007 Jon Ciesla <limb@jcomserv.net> - 0.8.2.2-7
- Corrected hof.c open mode.

* Mon Aug 13 2007 Jon Ciesla <limb@jcomserv.net> - 0.8.2.2-6
- Fixed license tag.
- Rebuilding due to mass rebuild failure.
- Applied patch for glibc open change.

* Fri Jul 27 2007 Jon Ciesla <limb@jcomserv.net> - 0.8.2.2-5
- Finished fixing macros.
- Dropped superfluous mkdir.

* Fri Jul 27 2007 Jon Ciesla <limb@jcomserv.net> - 0.8.2.2-4
- Fixed .desktop version.
- Macroized mandir.
- Corrected rpm_opt_flags usage.

* Thu Jul 26 2007 Jon Ciesla <limb@jcomserv.net> - 0.8.2.2-3
- Added height patch.
- Added man page.
- Added rpm_opt_flags.
- Simplified install.

* Thu Jul 26 2007 Jon Ciesla <limb@jcomserv.net> - 0.8.2.2-2
- Added desktop file, icon.

* Thu Jul 26 2007 Jon Ciesla <limb@jcomserv.net> - 0.8.2.2-1
- Initial packaging.
