# necessary since commit string is part of release tar ball - Roland
%global _commit_string ea93b21f9498

Name:           speedcrunch
Version:        0.12
Release:        7%{?dist}
Summary:        A fast power user calculator

License:        GPLv2+
URL:            http://www.speedcrunch.org
Source0:        https://bitbucket.org/heldercorreia/speedcrunch/get/release-%{version}.0.tar.bz2

BuildRequires:  cmake qt5-devel desktop-file-utils ImageMagick gcc-c++

# to be paranoid and include a minimal qt4 dep (ie, require at least the
# same or higher qt4 version than what was used to build it) -- Rex
%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}

%description
SpeedCrunch is a fast, high precision and powerful desktop calculator.
Among its distinctive features are a scrollable display, up to 50 decimal
precisions, unlimited variable storage, intelligent automatic completion
full keyboard-friendly and more than 15 built-in math function.

%prep
%setup -q -n heldercorreia-%{name}-%{_commit_string}

%build

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ../src
popd

make %{?_smp_mflags} -C %{_target_platform} VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT
make install/fast DESTDIR=$RPM_BUILD_ROOT -C %{_target_platform}

# Create icons on the fly
pushd src/resources
for size in 16 24 32 48; do
    mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${size}x${size}/apps
    convert -resize ${size}x${size} speedcrunch.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${size}x${size}/apps/speedcrunch.png
    touch --reference speedcrunch.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${size}x${size}/apps/speedcrunch.png
done
popd

desktop-file-install --vendor=""                              \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications         \
        pkg/speedcrunch.desktop

%check
make test -C %{_target_platform}

%files
%doc README.md pkg/COPYING.rtf
%{_bindir}/speedcrunch
%{_datadir}/applications/speedcrunch.desktop
%{_datadir}/icons/hicolor/*/apps/speedcrunch.png
%{_datadir}/pixmaps/speedcrunch.png
%{_datadir}/appdata/speedcrunch.appdata.xml

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12-2
- Remove obsolete scriptlets

* Mon Nov 13 2017 Roland Wolters <roland.wolters@bayz.de> - 0.12-1
- Update to 0.12
- update to Qt5
- user manual: in-app (with context help) and on-line
- user-defined functions
- complex numbers
- unit support, including conversions
- implicit multiplication
- bitfield widget, for people who deal with binary math
- virtual keypad is back
- double-click to insert into editor is back
- more color schemes, including Solarized alternatives
- currency symbols are ignored, you can now safely paste them into the editor

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 03 2015 Kalev Lember <kalevlember@gmail.com> - 0.11-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 20 2014 Roland Wolters <roland.wolters@bayz.de> - 0.11-0.1
- Update to 0.11

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-0.9.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 16 2013 Roland Wolters <roland.wolters@bayz.de> - 0.11-0.8.alpha
- Fixed bug 1040687

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-0.7.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-0.6.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-0.5.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-0.4.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 08 2011 Daniel Drake <dsd@laptop.org> - 0.11-0.3.alpha
- Fix build on platforms where char is unsigned, thanks to Henrik Nordström

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-0.2.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jun 24 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.11-0.1.alpha
- speedcrunch-0.11-alpha
- update cmake-related macros
- optimize scriptlets
- %%summary: drop 'for KDE', should be quite usable on any DE
- use upstream-provided .desktop file
- %%check: make test

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Apr 17 2008 Roland Wolters <wolters.liste@gmx.net> - 0.10-1
- update to version 0.10

* Fri Feb 22 2008 Roland Wolters <wolters.liste@gmx.net> - 0.9-3
- rebuild for fixed dependencies

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9-2
- Autorebuild for GCC 4.3

* Thu Nov 22 2007 Roland Wolters <wolters.liste@gmx.net> - 0.9-1
- update to version 0.9 including a new math engine and inverse hyperbolic
  functions

* Thu Aug 16 2007 Roland Wolters <wolters.liste@gmx.net> - 0.8-5
- licence tag corrected

* Thu Jul 26 2007 Roland Wolters <wolters.liste@gmx.net> 0.8-1
- update to upstream 0.8
- various new features and bugfixes

* Mon Apr 23 2007 Roland Wolters <wolters.liste@gmx.net> 0.7-1
- update to upstream 0.7
- icon scriplets for spec file added

* Sat Apr 21 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.7-0.10.beta2
- add icon to the desktop file

* Thu Feb 22 2007 Roland Wolters <wolters.liste@gmx.net> 0.7-0.9.beta2
- bumped version due to cvs problems

* Thu Feb 22 2007 Roland Wolters <wolters.liste@gmx.net> 0.7-0.4.beta2
- changed the version numbering

* Thu Feb 22 2007 Roland Wolters <wolters.liste@gmx.net> 0.7-beta2.3
- Added main category to desktop file

* Thu Feb 15 2007 Roland Wolters <wolters.liste@gmx.net> 0.7-beta2.2
- corrected spaces/tabs mixing in spec file
- corrected end-line-encoding

* Tue Feb 13 2007 Roland Wolters <wolters.liste@gmx.net> 0.7-beta2.1
- initial build

