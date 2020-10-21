# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=173658

%global _hardened_build 1
%global minorversion 1.1
%global xfceversion 4.13

Name:           xfce4-cpugraph-plugin
Version:        1.1.0
Release:        4%{?dist}
Summary:        CPU monitor for the Xfce panel

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-cpugraph-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel
BuildRequires:  xfce4-panel-devel
BuildRequires:  intltool
BuildRequires:  gettext
Requires:       xfce4-panel >= %{xfceversion}

%description
A CPU monitor plugin for the Xfce panel. It offers multiple display modes 
(LED, gradient, fire, etc...) to show the current CPU load of the system. The 
colors and the size of the plugin are customizable.


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install
# remove la file
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# make sure debuginfo is generated properly
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}


%check
make check


%files -f %{name}.lang
%doc AUTHORS ChangeLog README NEWS
%license COPYING
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/*/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.5-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.0.5-14
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 1.0.5-7
- Rebuild for Xfce 4.12

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5

* Sat Jun 30 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.3-2
- Define the Xfce version conditionally

* Sat Jun 30 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Mon Apr 30 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2 (Xfce 4.10 final)
- Add VCS key

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 1.0.1-7
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 1.0.1-6
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0.1-4
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 10 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.1-2
- Rebuild for xfce4-panel 4.7

* Sun Dec 05 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Thu Oct 07 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0
- License change: GPLv2+ instead of BSD
- Update Source URL
- BR intltool instead of perl(XML::Parser)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-4
- Rebuild for Xfce 4.6 (Beta 3)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.0-3
- Autorebuild for GCC 4.3

* Fri Dec 07 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-2
- Rebuild for Xfce 4.4.2

* Sat Nov 24 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0
- Remove asneeded patch, fixed upstream
- drop --disable-static

* Sat Apr 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-5
- Rebuild for Xfce 4.4.1

* Mon Jan 22 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-4
- Rebuild for Xfce 4.4.
- Patch to compile with -Wl,--as-needed (bugzilla.xfce.org #2785)

* Thu Oct 05 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-3
- Bump release for devel checkin.

* Wed Sep 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-2
- Rebuild for XFCE 4.3.99.1.
- BR perl(XML::Parser).

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-1
- Update to 0.3 on XFCE 4.3.90.2.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.2-7
- Mass rebuild for Fedora Core 6.

* Tue Apr 11 2006 Christoph Wickert <fedora wickert at arcor de> - 0.2.2-6
- Require xfce4-panel.

* Thu Feb 16 2006 Christoph Wickert <fedora wickert at arcor de> - 0.2.2-5
- Rebuild for Fedora Extras 5.

* Mon Nov 28 2005 Christoph Wickert <fedora wickert at arcor de> - 0.2.2-4
- Rebuild with new source because of md5sum mismatch.
- Add libxfcegui4-devel BuildReqs.

* Mon Nov 14 2005 Christoph Wickert <fedora wickert at arcor de> - 0.2.2-3
- Initial Fedora Extras version.
- Rebuild for XFCE 4.2.3.
- disable-static instead of removing .a files.

* Fri Sep 23 2005 Christoph Wickert <fedora wickert at arcor de> - 0.2.2-2.fc4.cw
- Add libxml2 BuildReqs.

* Sat Jul 09 2005 Christoph Wickert <fedora wickert at arcor de> - 0.2.2-1.fc4.cw
- Rebuild for Core 4.

* Wed Apr 13 2005 Christoph Wickert <fedora wickert at arcor de> - 0.2.2-1.fc3.cw
- Initial RPM release.
