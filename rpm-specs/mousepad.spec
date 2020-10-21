%global minorversion 0.4

Name:           mousepad
Version:        0.4.2
Release:        3%{?dist}
Summary:        Simple text editor for Xfce desktop environment

License:        GPLv2+
URL:            http://xfce.org/
Source0:        http://archive.xfce.org/src/apps/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2
Source1:        %{name}.appdata.xml

BuildRequires:  gcc
BuildRequires:  libxfce4util-devel
BuildRequires:  gettext 
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  gtksourceview3-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  glib2-devel
BuildRequires:  exo-devel
BuildRequires:  xfconf-devel
BuildRequires:  libappstream-glib

%description
Mousepad aims to be an easy-to-use and fast editor. It's target is an editor for
quickly editing text files, not a development environment or an editor with a
huge bunch of plugins.

Mousepad is based on Leafpad. The initial reason for Mousepad was to provide
printing support, which would have been difficult for Leafpad for various
reasons.

Although some features are under development, currently Mousepad has following
features:

    * Complete support for UTF-8 text
    * Cut/Copy/Paste and Select All text
    * Search and Replace
    * Font selecton
    * Word Wrap
    * Character coding selection
    * Auto character coding detection (UTF-8 and some codesets)
    * Manual codeset setting
    * Infinite Undo/Redo by word
    * Auto Indent
    * Multi-line Indent
    * Display line numbers
    * Drag and Drop
    * Printing

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%find_lang %{name}

desktop-file-install \
    --remove-category="Application" \
    --delete-original \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop


mkdir -p %{buildroot}%{_metainfodir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.appdata.xml

%if 0%{?el7}
%post
update-desktop-database &> /dev/null ||:
 
%postun
update-desktop-database &> /dev/null ||:
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi
 
%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
%endif

%files -f %{name}.lang
%doc AUTHORS NEWS README TODO THANKS
%license COPYING
%{_bindir}/mousepad 
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.xfce.mousepad.gschema.xml
%{_datadir}/polkit-1/actions/org.xfce.mousepad.policy

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jul 30 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2
- Add xfconf-devel as buildrequires
- Change appdata install location

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.1-3
- Add el conditional to fix schema compilation

* Thu Jun 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.1-2
- Add proper appdata file
- Add proper schema handling

* Sat Jun 02 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1
 
* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.4.0-10
- Spec modernization + Switch to gtk3

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.4.0-3
- Add an AppData file for the software center

* Sun Mar 01 2015 Kevin Fenzi <kevin@scrye.com> 0.4.0-2
- Fix glib schemas

* Sat Feb 28 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 30 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0 final
- Clean up spec file

* Mon Sep 03 2012 Kevin Fenzi <kevin@scrye.com> 0.3.0-0.1
- Update to pre-release git snapshot of 0.3.0

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 04 2012 Kevin Fenzi <kevin@scrye.com> - 0.2.16-7
- Rebuild for Xfce 4.10

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.2.16-5
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 01 2010 Kevin Fenzi <kevin@tummy.com> - 0.2.16-3
- Add patch to fix find bug (#648560)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Kevin Fenzi <kevin@tummy.com> - 0.2.16-1
- Update to 0.2.16

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 27 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.14-1
- Update to 0.2.14
- BuildRequire intltool
- Drop category X-Fedora from desktop file

* Sun Feb 10 2008 Kevin Fenzi <kevin@tummy.com> - 0.2.13-2
- Rebuild for gcc43

* Sun Nov 18 2007 Kevin Fenzi <kevin@tummy.com> - 0.2.13-1
- Update to 0.2.13

* Mon Aug 27 2007 Kevin Fenzi <kevin@tummy.com> - 0.2.12-3
- Update License tag

* Mon May 14 2007 Kevin Fenzi <kevin@tummy.com> - 0.2.12-2
- Rebuild for ppc64

* Sun Jan 21 2007 Kevin Fenzi <kevin@tummy.com> - 0.2.12-1
- Update to 0.2.12

* Fri Nov 10 2006 Kevin Fenzi <kevin@tummy.com> - 0.2.10-1
- Update to 0.2.10

* Thu Oct  5 2006 Kevin Fenzi <kevin@tummy.com> - 0.2.8-2
- Fix typo in description 

* Sun Sep  3 2006 Kevin Fenzi <kevin@tummy.com> - 0.2.8-1
- Update to 0.2.8

* Thu Aug 31 2006 Kevin Fenzi <kevin@tummy.com> - 0.2.6-2
- Add update-desktop-database

* Sun Aug 27 2006 Kevin Fenzi <kevin@tummy.com> - 0.2.6-1
- Inital package for fedora extras

