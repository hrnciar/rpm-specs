%global _hardened_build 1
%global minor_version 4.5
%global xfceversion 4.13

Name:           xfce4-eyes-plugin
Version:        4.5.1
Release:        1%{?dist}
Summary:        Eyes for the Xfce panel

License:        GPLv2+
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libxml2-devel
BuildRequires:  intltool
BuildRequires:  gettext

Requires:       xfce4-panel >= %{xfceversion}

%description
A xfce4 panel plugin that adds eyes which watch your every step. Scary!

%prep
%autosetup

%build
%configure --disable-static
%make_build

%install
%make_install
%find_lang %{name}

find %{buildroot} -name \*.la -exec rm {} \;


%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_libdir}/xfce4/panel/plugins/libeyes.so
%{_datadir}/icons/hicolor/*/apps/xfce4-eyes.png
%{_datadir}/xfce4/eyes

%changelog
* Sun Jun 21 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.5.1-1
- Update to 4.5.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.5.0-20
- Rebuilt (xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 08 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.5.0-2
- Fix icon files installation

* Sun Apr 08 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.5.0-1
- Update to 4.5.0

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 4.4.5-6
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr 25 2016 Kevin Fenzi <kevin@scrye.com> - 4.4.5-1
- Update to 4.4.5. Translation updates

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 15 2015 Kevin Fenzi <kevin@scrye.com> 4.4.4-2
- Rebuild for build failure

* Sun Mar 15 2015 Kevin Fenzi <kevin@scrye.com> 4.4.4-1
- Update to 4.4.4 with some translation fixes. 

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 4.4.3-2
- Rebuild for Xfce 4.12

* Tue Dec 23 2014 Kevin Fenzi <kevin@scrye.com> 4.4.3-1
- Update to 4.4.3

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 06 2013 Kevin Fenzi <kevin@scrye.com> 4.4.2-1
- Update to 4.4.2

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 15 2012 Kevin Fenzi <kevin@scrye.com> - 4.4.1-7
- Rebuild for Xfce 4.10(pre2)

* Thu Apr 05 2012 Kevin Fenzi <kevin@scrye.com> - 4.4.1-6
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 4.4.1-4
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 18 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.4.1-2
- Rebuild for xfce4-panel 4.7

* Sat Dec 18 2010 Christoph Wickert <cwickert@fedoraproject.org> - 4.4.1-1
- Update to 4.4.1
- Fix Source0 URL
- Update icon-cache scriptlets

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 4.4.0-5
- Rebuild for Xfce 4.6 (Beta 3)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.4.0-4
- Autorebuild for GCC 4.3

* Sat Aug 25 2007 Christoph Wickert <cwickert@fedoraproject.org> - 4.4.0-3
- Rebuild for BuildID feature
- Update license tag

* Sat Apr 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 4.4.0-2
- Rebuild for Xfce 4.4.1

* Mon Jan 22 2007 Christoph Wickert <cwickert@fedoraproject.org> - 4.4.0-1
- Update to 4.4.0 on Xfce 4.4.
- Update gtk-icon-cache scriptlets.

* Sun Nov 12 2006 Christoph Wickert <cwickert@fedoraproject.org> - 4.3.99.1-2
- Add %%defattr.

* Sat Sep 23 2006 Christoph Wickert <cwickert@fedoraproject.org> - 4.3.99.1-1
- Initial Fedora Extras version.
