Name:           rcssmonitor
Version:        16.0.0
Release:        2%{?dist}
Summary:        RoboCup 2D Soccer Simulator Monitor

License:        GPLv2+
URL:            http://sourceforge.net/projects/sserver/
Source0:        http://downloads.sourceforge.net/sserver/%{name}-%{version}.tar.gz
# Source 1 is created by me.
Source1:        %{name}.desktop
Provides:       rcsslogplayer = %{version}-%{release}
Obsoletes:      rcsslogplayer <= 15.1.1-30

BuildRequires:  gcc-c++ automake boost-devel qt5-qtbase-devel desktop-file-utils

%description
The RoboCup Soccer Simulator Monitor is a viewer for moved 2d vector graphics.
You can use it to watch 2D soccer games running on rcssserver. However, The
architecture of The RoboCup Soccer Simulator Monitor was from the beginning
kept as general and modular as possible and not just hacked to fit the  needs
of the robocup soccer server (rcssserver). So by now The RoboCup Soccer
Simulator Monitor is also used to visualize many other two dimensional system.

You can use UDP/IP communication sockets to send commands to The RoboCup Soccer
Simulator Monitor. A generic communication device is also included. It
understands a very easy description language to build and move 2d objects.

%prep
%setup -q
sed -i.lib \
    -e 's|\$ac_boost_path/lib|\$libdir|' \
    -e 's|$ac_boost_path_tmp/lib|\$libdir|' \
    m4/ax_boost_base.m4
sed -i.newarchs \
    "s|-o \$ax_arch = ppc64|-o \$ax_arch = aarch64 -o \$ax_arch = ppc64 -o \$ax_arch = ppc64le|" \
    m4/ax_boost_base.m4
sed -i.nostatic \
    -e 's|--static||g' m4/qt.m4
autoreconf -if

%build
%configure --with-boost-program-options=boost_program_options	\
	--with-qt-moc=%{_bindir}/moc-qt5
make %{?_smp_mflags} 

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"

mkdir -p %{buildroot}/%{_datadir}/pixmaps/
cp -p icons/rcss.xpm %{buildroot}/%{_datadir}/pixmaps/

desktop-file-install \
  --dir=%{buildroot}/%{_datadir}/applications %{SOURCE1}

%files
%doc AUTHORS ChangeLog COPYING NEWS README.md
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 16.0.0-2
- Rebuilt for Boost 1.73

* Fri May 08 2020 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 16.0.0-1
- Update to 16.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 15.1.1-26
- Rebuilt for Boost 1.69

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 15.1.1-24
- Add gcc-c++ build dependency

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 15.1.1-22
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 15.1.1-19
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 15.1.1-18
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 15.1.1-16
- Rebuilt for Boost 1.63

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 15.1.1-15
- Rebuilt for linker errors in boost (#1331983)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 15.1.1-13
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 15.1.1-12
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 15.1.1-10
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 15.1.1-8
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 15.1.1-7
- Rebuild for boost 1.57.0

* Tue Sep 09 2014 Karsten Hopp <karsten@redhat.com> 15.1.1-6
- fix libdir on ppc64le

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 15.1.1-4
- Fix boost detection on aarch64 platform

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 15.1.1-2
- Rebuild for boost 1.55.0

* Fri Apr 25 2014 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 15.1.1-1
- Update to 15.1.1 to fix a locale dependent bug

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 Petr Machata <pmachata@redhat.com> - 15.0.0-10
- Rebuild for boost 1.54.0
- Change configure invocation to avoid Boost -mt libraries, which are
  not shipped anymore.

* Wed May 01 2013 Jon Ciesla <limburgher@gmail.com> - 15.0.0-9
- Drop desktop vendor tag.

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 15.0.0-8
- Rebuild for Boost-1.53.0

* Tue Aug 21 2012 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 15.0.0-7
- Rebuild for Boost 1.50

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.0.0-5
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 21 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 15.0.0-3
- Rebuild for Boost 1.48

* Fri Jul 22 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 15.0.0-2
- Rebuild for Boost 1.47

* Thu May 19 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 15.0.0-1
- Updated to new upstream version 15.0.0

* Sun Apr 17 2011 Kalev Lember <kalev@smartlink.ee> - 14.1.0-4
- Rebuilt for boost 1.46.1 soname bump

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 04 2010 Hedayat Vatankhah <hedayat@fedoraproject.org> - 14.1.0-2
- Rebuild for the new boost

* Fri Jun 04 2010 Hedayat Vatankhah <hedayat@grad.com> - 14.1.0-1
- Updated to version 14.1.0
- Fixed qt.m4 to avoid pulling private libs (Thanks to Mamoru Tasaka)

* Mon Jan 18 2010 Hedayat Vatankhah <hedayat@grad.com> - 14.0.1-1
- Updated to version 14.0.1

* Thu Nov 19 2009 Hedayat Vatankhah <hedayat@grad.com> - 14.0.0-1
- Updated to version 14.0.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 07 2009 Hedayat Vatankhah <hedayat@grad.com> 13.1.0-2
- Added a patch for gcc4.4 compilation fixing.

* Tue Apr 07 2009 Hedayat Vatankhah <hedayat@grad.com> 13.1.0-1
- Updated to new upstream release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Hedayat Vatankhah <hedayat@grad.com> 13.0.0-3
- Added xorg-x11-fonts-misc as a requirement.

* Wed Nov 5 2008 Hedayat Vatankhah <hedayat@grad.com> 13.0.0-2
- New release because of incorrect tagging.

* Wed Nov 5 2008 Hedayat Vatankhah <hedayat@grad.com> 13.0.0-1
- Updated to the new released version: 13.0.0

* Tue Aug 26 2008 Hedayat Vatankhah <hedayat@grad.com> 12.1.0-2
- Fixed source no. in the Source1 comment
- Fixed the .desktop file

* Tue Aug 12 2008 Hedayat Vatankhah <hedayat@grad.com> 12.1.0-1
- Completed the description
- Added icon and .desktop file installation

* Sat Jul 12 2008 Hedayat Vatankhah <hedayat@grad.com> 12.1.0-1
- Initial version
