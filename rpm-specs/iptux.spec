%define bugfix 2
Name:           iptux
Version:        0.5.1
Release:        24%{?dist}
Summary:        A software for sharing in LAN
License:        GPLv2+
URL:            http://code.google.com/p/iptux/
Source0:        http://iptux.googlecode.com/files/%{name}-%{version}-%{?bugfix}.tar.gz 
BuildRequires:  gcc-c++
BuildRequires:  GConf2-devel, gtk2-devel, desktop-file-utils
BuildRequires:  gettext, dbus-devel, gstreamer-devel

%description
A software for sharing and transporting files and
directories in LAN. It is written by C++ and the 
skin is designed by gtk. Iptux is based on ipmsg,
so you can use it send files to a Windows PC which 
has an ipmsg Windows edition in Lan.


%prep
%setup -q -n %{name}-%{version}


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
%find_lang %{name}
desktop-file-install \
  --delete-original \
  --dir ${RPM_BUILD_ROOT}/%{_datadir}/applications \
  ${RPM_BUILD_ROOT}/%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%doc ChangeLog style
%{_bindir}/%{name}
%{_bindir}/ihate%{name}
%{_datadir}/applications/iptux.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/64x64/apps/i-tux.png
%{_datadir}/icons/hicolor/64x64/apps/ip-tux.png
%{_datadir}/icons/hicolor/16x16/apps/i-tux.png
%{_datadir}/icons/hicolor/16x16/apps/ip-tux.png
%{_datadir}/icons/hicolor/22x22/apps/i-tux.png
%{_datadir}/icons/hicolor/22x22/apps/ip-tux.png
%{_datadir}/icons/hicolor/24x24/apps/i-tux.png
%{_datadir}/icons/hicolor/24x24/apps/ip-tux.png
%{_datadir}/icons/hicolor/32x32/apps/i-tux.png
%{_datadir}/icons/hicolor/32x32/apps/ip-tux.png
%{_datadir}/icons/hicolor/48x48/apps/i-tux.png
%{_datadir}/icons/hicolor/48x48/apps/ip-tux.png

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.1-14
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.5.1-7
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 23 2009 Liang Suilong <liangsuilong@gmail.com> 0.5.1-5
- Fix some bugs
- Update RPM Spec file

* Mon Nov 2 2009 Liang Suilong <liangsuilong@gmail.com> 0.5.1-4
- Tag for Fedora 11 again

* Mon Nov 2 2009 Liang Suilong <liangsuilong@gmail.com> 0.5.1-3
- Tag for Fedora 11 again

* Mon Nov 2 2009 Liang Suilong <liangsuilong@gmail.com> 0.5.1-2
- Update RPM Spec file

* Mon Nov 2 2009 Liang Suilong <liangsuilong@gmail.com> 0.5.1-1
- Upstream to 0.5.1

* Thu Oct 8 2009 Liang Suilong <liangsuilong@gmail.com> 0.5.0-1
- Upstream to 0.5.0

* Tue Mar 3 2009 Liang Suilong <liangsuilong@gmail.com> 0.4.5-2
- Fix the spec file

* Tue Mar 3 2009 Liang Suilong <liangsuilong@gmail.com> 0.4.5-1
- Upstream to 0.4.5

* Fri Feb 27 2009 Liang Suilong <liangsuilong@gmail.com> 0.4.5-0.1.rc3
- Upstream to 0.4.5-rc4
- Remove the iptux-0.4.5-rc1-revert-using-ipv4_order.patch
- Remove the iptux-0.4.4-g++44.patch

* Sun Feb 15 2009 Liang Suilong <liangsuilong@gmail.com> 0.4.5-0.1.rc3
- Upstream to 0.4.5-rc3

* Sun Feb 15 2009 Liang Suilong <liangsuilong@gmail.com> 0.4.5-0.1.rc1
- Upstream to 0.4.5-rc1

* Tue Jan 19 2009 Liang Suilong <liangsuilong@gmail.com> 0.4.4-2
- Fix  build error with g++44

* Tue Jan 19 2009 Liang Suilong <liangsuilong@gmail.com> 0.4.4-1
- Upstream to 0.4.4

* Wed Dec 24 2008 Liang Suilong <liangsuilong@gmail.com> -0.4.3-1
- Initial Package.
