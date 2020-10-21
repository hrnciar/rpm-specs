Name:           viewnior
Version:        1.7
Release:        9%{?dist}
Summary:        Elegant image viewer

License:        GPLv3+
URL:            http://siyanpanayotov.com/project/viewnior/
Source0:        https://github.com/hellosiyan/Viewnior/archive/%{name}-%{version}.tar.gz
# Backported from upstream
Patch0:         fix-appdata.patch

BuildRequires:  pkgconfig(gtk+-2.0) >= 2.20
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gio-2.0) >= 2.32
BuildRequires:  pkgconfig(shared-mime-info) >= 0.20
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.4.0
BuildRequires:  pkgconfig(exiv2) >= 0.21
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  gnome-common
BuildRequires:  gcc-c++

%description 
Viewnior is an image viewer program. Created to be simple, fast and elegant. 
It's minimalistic interface provides more screen space for your images. Among 
its features are:

* Fullscreen & Slideshow
* Rotate, flip, save, delete images
* Animation support
* Browse only selected images
* Navigation window
* Simple interface
* Configurable mouse actions


%prep
%autosetup -n Viewnior-%{name}-%{version} -p1

%build
%meson

%meson_build

%install
%meson_install

%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS TODO
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%{_mandir}/man*/%{name}*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 05 2019 Kalev Lember <klember@redhat.com> - 1.7-7
- Use upstream appdata file

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.7-4
- rebuild (exiv2)

* Mon Jul 16 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.7-3
- Add gcc-c++ as BR

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.7-1
- Update to 1.7
- Update spec to use meson build system

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6-7
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.6-4
- rebuild (exiv2)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Christoph Wickert <cwickert@fedoraproject.org> - 1.6-1
- Update to 1.6

* Wed Jun 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 1.5-3
- rebuild (exiv2)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Christoph Wickert <cwickert@fedoraproject.org> - 1.5-1
- Update to 1.5

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.4-3
- Add an AppData file for the software center

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 26 2014 Christoph Wickert <cwickert@fedoraproject.org> - 1.4-1
- Update to 1.4
- Fix Source0 URL and website
- Update BuildRequires
- Drop obsolete aarch64 patch
- Fix changelog

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 12 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.3-4
- Add aarch64 support (#926697)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.3-1
- Update to 1.3
- Drop BR of GConf2-devel (no longer needed)
- As dep on GConf2-(devel) is obsolet, we can now remove the bcond clause, too

* Sat Feb 25 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.2-1
- Update to 1.2

* Sat Feb 25 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.1-4
- Fix DSO linking error

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.1-3
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.1-1
- Update to 1.1
- Remove obsolete DSO patch
- Add new manpage

* Wed Mar 31 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0-1
- Update to 1.0

* Tue Feb 16 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7-2
- Add patch to fix DSO linking (#565018)
- Switch to %%bcond macro

* Mon Sep 07 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.7-1
- Update to 0.7

* Sat Sep 05 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6-2
- Spec file cleanups from review.

* Mon Aug 03 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6-1
- Initial package
