Name:           focuswriter
Version:        1.7.6
Release:        1%{?dist}
Summary:        A full screen, distraction-free writing program
License:        GPLv3+
URL:            http://gottcode.org/%{name}/
Source0:        http://gottcode.org/%{name}/%{name}-%{version}-src.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  libao-devel
BuildRequires:  libzip-devel
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  hunspell-devel

%description
A full screen, distraction-free writing program. You can customize your
environment by changing the font, colors, and background image to add ambiance
as you type. FocusWriter features an on-the-fly updating word count, optional
auto-save, optional daily goals, and an interface that hides away to allow you
to focus more clearly; additionally, when you open the program your current
work-in-progress will automatically load and position you at the end of your
document, so that you can immediately jump back in.

%prep
%setup -q

%build
%{qmake_qt5} PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_ROOT=$RPM_BUILD_ROOT
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files
%doc COPYING ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/icons/hicolor/1024x1024/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/%{name}.1.gz

%changelog
* Wed Apr 22 2020 Vojtech Trefny <vtrefny@redhat.com> - 1.7.6-1
- Update to 1.7.6

* Mon Feb 24 2020 Vojtech Trefny <vtrefny@redhat.com> - 1.7.5-1
- Update to 1.7.5

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Vojtech Trefny <vtrefny@redhat.com> - 1.7.4-1
- Update to 1.7.4

* Sat Sep 28 2019 Vojtech Trefny <vtrefny@redhat.com> - 1.7.3-1
- Update to 1.7.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.5-7
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.5.5-2
- use %%qmake_qt4 macro to ensure proper build flags

* Thu Dec 24 2015 Jean-Francois Saucier <jsaucier@gmail.com> - 1.5.5-1
- Update to the new upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Remi Collet <remi@fedoraproject.org> - 1.4.6-5
- rebuild for new libzip

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4.6-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Richard Hughes <richard@hughsie.com> - 1.4.6-1
- Update to the new upstream version

* Thu Jan  9 2014 Jean-Francois Saucier <jsaucier@gmail.com> - 1.4.4-1
- Update to the new upstream version

* Wed Aug 21 2013 Remi Collet <rcollet@redhat.com> - 1.3.5.1-6
- rebuild for new libzip

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Feb 04 2012 Remi Collet <remi@fedoraproject.org> - 1.3.5.1-2
- rebuild for new libzip

* Wed Jan 11 2012 Jean-Francois Saucier <jsaucier@gmail.com> - 1.3.5.1-1
- Update to the new upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Jean-Francois Saucier <jsaucier@gmail.com> - 1.3.2.1-1
- Update to the new upstream version

* Thu Dec 23 2010 Jean-Francois Saucier <jsaucier@gmail.com> - 1.3.1-3
- Remove the qt-devel version number
- Reorder the files section at the end of the spec

* Wed Nov 24 2010 Jean-Francois Saucier <jsaucier@gmail.com> - 1.3.1-2
- Fix as per suggestion in bug #652257

* Wed Nov 10 2010 Jean-Francois Saucier <jsaucier@gmail.com> - 1.3.1-1
- Initial build for Fedora
