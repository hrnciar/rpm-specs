Name: dmapd
Version: 0.0.86
Release: 3%{?dist}
Summary: A server that provides DAAP and DPAP shares

License: GPLv2+
URL: http://www.flyn.org/projects/dmapd/
Source0: http://www.flyn.org/projects/%name/%{name}-%{version}.tar.gz

%{?systemd_requires}
BuildRequires: libdmapsharing4-devel >= 3.9.3
BuildRequires: vips-devel >= 7.38
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
BuildRequires: systemd
Requires(pre): shadow-utils
Requires(post): systemd-units systemd-sysv
Requires(preun): systemd-units
Requires(postun): systemd-units

%description 
The dmapd project provides a GObject-based, Open Source implementation 
of DMAP sharing with the following features:

 o Support for both DAAP and DPAP

 o Support for realtime transcoding of media formats not natively 
 supported by clients

 o Support for many metadata formats, such as those associated with Ogg 
 Vorbis and MP3 (e.g., ID3)

 o Detection of video streams so that clients may play them as video

 o Use of GStreamer to support a wide range of audio and video CODECs

 o Caching of photograph thumbnails to avoid regenerating them each time 
 the server restarts

Dmapd runs on Linux and other POSIX operating systems. It has been 
used on OpenWrt Linux-based systems with as little as 32MB of memory 
to serve music, video and photograph libraries containing thousands of 
files.

%prep
%setup -q

%build
%configure                                      \
	--disable-static                        \
	--disable-tests                         \
	--with-systemdsystemunitdir=%{_unitdir} \

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}%{_libdir}/libdmapd.la
rm -f %{buildroot}%{_libdir}/dmapd/%{version}/modules/*.la
rm -f %{buildroot}%{_sbindir}/dmapd-test
mkdir -p %{buildroot}%{_localstatedir}/cache/dmapd/DAAP
mkdir -p %{buildroot}%{_localstatedir}/cache/dmapd/DPAP
mkdir -p %{buildroot}%{_localstatedir}/run/dmapd
install -D -p -m 644 distro/dmapd.conf %{buildroot}%{_sysconfdir}/dmapd.conf

%files 
%{_libdir}/*.so.0
%{_libdir}/*.so.%{version}
%{_libdir}/dmapd
%{_sbindir}/dmapd
%{_bindir}/dmapd-transcode
%{_bindir}/dmapd-hashgen
%config(noreplace) %{_sysconfdir}/dmapd.conf
%attr(0700,dmapd,root) %{_localstatedir}/cache/dmapd/
%attr(0700,dmapd,root) %{_localstatedir}/run/dmapd
%{_mandir}/*/*
%{_unitdir}/dmapd.service
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README FAQ 

%pre
getent group dmapd >/dev/null || groupadd -r dmapd
getent passwd dmapd >/dev/null || useradd -r -g dmapd -d / -s /sbin/nologin -c "dmapd Daemon" dmapd
exit 0

%post
/sbin/ldconfig
%systemd_post dmapd.service

%preun
%systemd_preun dmapd.service

%postun
/sbin/ldconfig
%systemd_postun_with_restart dmapd.service

# FIXME: Remove once Fedora 15 EOL'ed.
# See http://fedoraproject.org/wiki/Packaging:ScriptletSnippets
%triggerun -- dmapd < 0.0.37-2
%{_bindir}/systemd-sysv-convert --save dmapd >/dev/null 2>&1 || :
/bin/systemctl --no-reload enable dmapd.service >/dev/null 2>&1 || :
/sbin/chkconfig --del dmapd >/dev/null 2>&1 || :
/bin/systemctl try-restart dmapd.service >/dev/null 2>&1 || :

%package devel
Summary: Files needed to develop modules using dmapd's libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the libraries, include files, and other 
resources needed for developing modules using dmapd's API.

%files devel
%{_libdir}/pkgconfig/dmapd.pc
%{_includedir}/dmapd-*/
%{_libdir}/*.so
%ghost %attr(0755,dmapd,dmapd) %dir %{_localstatedir}/run/dmapd
%ghost %attr(0600,root,root) %{_localstatedir}/lock/subsys/dmapd

%changelog
* Mon Aug 20 2020 W. Michael Petullo <mike@flyn.org> - 0.0.86-3
- Add missing changelog entry

* Mon Aug 20 2020 W. Michael Petullo <mike@flyn.org> - 0.0.86-2
- Fix date on changelog entry

* Mon Aug 20 2020 W. Michael Petullo <mike@flyn.org> - 0.0.86-1
- New upstream version

* Mon Aug 03 2020 W. Michael Petullo <mike@flyn.org> - 0.0.85-1
- New upstream version

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.84-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.84-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.84-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 26 2019 W. Michael Petullo <mike[@]flyn.org> - 0.0.84-1
- New upstream version

* Sun Oct 13 2019 W. Michael Petullo <mike[@]flyn.org> - 0.0.83-1
- New upstream version

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 19 2019 W. Michael Petullo <mike[@]flyn.org> 0.0.82-2
- New upstream version

* Sun Mar 17 2019 W. Michael Petullo <mike[@]flyn.org> 0.0.80-1
- New upstream version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 16 2018 W. Michael Petullo <mike[@]flyn.org> 0.0.77-1
- New upstream version
- Set BuildRequires to ensure newest API

* Sat Aug 11 2018 W. Michael Petullo <mike[@]flyn.org> 0.0.76-1
- New upstream version
- Set BuildRequires to ensure newest API

* Thu Jul 19 2018 W. Michael Petullo <mike[@]flyn.org> - 0.0.75-3
- Add systemd to BuildRequires for %{_unitdir}

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.75-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 W. Michael Petullo <mike[@]flyn.org> - 0.0.75-1
- New upstream version
- Build against new libdmapsharing package with new API

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.72-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.72-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.72-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.72-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 31 2016 W. Michael Petullo <mike[@]flyn.org> - 0.0.72-5
- Fix Bugzilla #1074763

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.72-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.72-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 19 2015 W. Michael Petullo <mike[@]flyn.org> - 0.0.72-2
- Rebuild for VIPS 8.0

* Sun Apr 19 2015 W. Michael Petullo <mike[@]flyn.org> - 0.0.72-1
- New upstream version

* Mon Dec 29 2014 W. Michael Petullo <mike[@]flyn.org> - 0.0.70-3
- Rebuild for VIPS 7.42

* Wed Nov 26 2014 Rex Dieter <rdieter@fedoraproject.org> 0.0.70-2
- rebuild (openexr,vips)

* Mon Sep 01 2014 W. Michael Petullo <mike[@]flyn.org> 0.0.70-1
- New upstream version
- Do not build tests

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.69-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 W. Michael Petullo <mike[@]flyn.org> - 0.0.69-5
- Rebuild for VIPS 7.40

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.69-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 08 2014 W. Michael Petullo <mike[@]flyn.org> - 0.0.69-3
- Rebuilt for ImageMagick soname bump

* Sat Mar 15 2014 W. Michael Petullo <mike[@]flyn.org> 0.0.69-2
- Add gstreamer1-plugins-base-devel dependency for GstDiscoverer

* Sat Mar 15 2014 W. Michael Petullo <mike[@]flyn.org> 0.0.69-1
- New upstream version

* Sun Mar 09 2014 W. Michael Petullo <mike[@]flyn.org> 0.0.68-1
- New upstream version

* Sun Mar 09 2014 W. Michael Petullo <mike[@]flyn.org> 0.0.67-1
- New upstream version

* Sat Mar 08 2014 W. Michael Petullo <mike[@]flyn.org> 0.0.66-1
- New upstream version

* Tue Jan 21 2014 W. Michael Petullo <mike[@]flyn.org> 0.0.65-1
- New upstream version

* Sat Jan 11 2014 W. Michael Petullo <mike[@]flyn.org> 0.0.63-1
- New upstream version
- Drop dmapd-vips736.patch

* Fri Jan 10 2014 Orion Poplawski <orion@cora.nwra.com> - 0.0.62-1
- Update to 0.0.62
- Add patch to compile with vips 7.36

* Fri Jan 03 2014 Kalev Lember <kalevlember@gmail.com> - 0.0.55-7
- Rebuilt for libwebp soname bump

* Thu Nov 28 2013 Rex Dieter <rdieter@fedoraproject.org> 0.0.55-6
- rebuild (openexr)

* Sun Oct 06 2013  W. Michael Petullo <mike[@]flyn.org> 0.0.55-5
- Rebuild for VIPS 7.36

* Sat Sep 14 2013 Bruno Wolff III <bruno@wolff.to> - 0.0.55-4
- Rebuild for ilmbase related soname bumps

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 05 2013 W. Michael Petullo <mike[@]flyn.org> 0.0.55-2
- Remove dmapd-vips-7.32.patch

* Fri Jul 05 2013 W. Michael Petullo <mike[@]flyn.org> 0.0.55-1
- New upstream version

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 0.0.51-2
- Rebuild for hdf5 1.8.11

* Thu Apr 11 2013 W. Michael Petullo <mike[@]flyn.org> 0.0.51-1
- New upstream version
- Build against GStreamer 1.0

* Sun Mar 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.0.50-7
- rebuild (libcfitsio)

* Mon Mar 11 2013 Rex Dieter <rdieter@fedoraproject.org> - 0.0.50-6
- rebuild (OpenEXR)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.50-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.0.50-4
- rebuild due to "jpeg8-ABI" feature drop

* Mon Oct 29 2012 W. Michael Petullo <mike[@]flyn.org> - 0.0.50-3
- Another change to VIPS patch

* Mon Oct 29 2012 W. Michael Petullo <mike[@]flyn.org> - 0.0.50-2
- Update dmapd-vips-7.30.patch

* Mon Oct 29 2012 W. Michael Petullo <mike[@]flyn.org> - 0.0.50-1
- New upstream version
- Patch to use VIPS 7.30

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 W. Michael Petullo <mike[@]flyn.org> - 0.0.48-1
- New upstream version
- No longer need sed modification of configure.ac for VIPS 7.28
- No longer run autotools
- Do not require GraphicsMagick-devel; vips-devel will pull in requirements

* Fri Apr 13 2012 Tom Callaway <spot@fedoraproject.org> - 0.0.47-3
- rebuild for new ImageMagick

* Fri Mar 30 2012 W. Michael Petullo <mike[@]flyn.org> - 0.0.47-2
- Create /var/cache/dmapd/DAAP and DPAP

* Fri Mar 30 2012 W. Michael Petullo <mike[@]flyn.org> - 0.0.47-1
- New upstream version
- Apply database directory patch
- Apply glib include patch

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.0.45-2
- Rebuild for new libpng

* Mon Dec 05 2011 W. Michael Petullo <mike[@]flyn.org> - 0.0.45-1
- New upstream version
- Remove systemd conditionals

* Mon Sep 26 2011 W. Michael Petullo <mike[@]flyn.org> - 0.0.37-3
- Patch to use VIPS 7.26

* Mon Jul 11 2011 W. Michael Petullo <mike[@]flyn.org> - 0.0.37-2
- Use systemd on Fedora > 15

* Fri Feb 11 2011 W. Michael Petullo <mike[@]flyn.org> - 0.0.37-1
- New upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 30 2010 W. Michael Petullo <mike[@]flyn.org> - 0.0.34-3
- Add file attributes for lock/subsys/dmapd

* Thu Dec 30 2010 W. Michael Petullo <mike[@]flyn.org> - 0.0.34-2
- Fix Bugzilla #656575

* Sun Nov 28 2010 W. Michael Petullo <mike[@]flyn.org> - 0.0.34-1
- New upstream version

* Sun Nov 28 2010 W. Michael Petullo <mike[@]flyn.org> - 0.0.33-1
- New upstream version

* Mon Nov 01 2010 W. Michael Petullo <mike[@]flyn.org> - 0.0.31-1
- New upstream version

* Wed Sep 29 2010 jkeating <> - 0.0.25-5
- Rebuilt for gcc bug 634757

* Thu Sep 16 2010 W. Michael Petullo <mike[@]flyn.org> - 0.0.25-4
- Bump release in an attempt to build on Rawhide

* Wed Aug 04 2010 W. Michael Petullo <mike[@]flyn.org> - 0.0.25-3
- Use VIPS instead of GraphicsMagick

* Tue Jun 22 2010 W. Michael Petullo <mike[@]flyn.org> - 0.0.25-2
- Don't install dmapd-test

* Tue Jun 22 2010 W. Michael Petullo <mike[@]flyn.org> - 0.0.25-1
- New upstream version

* Fri Jun 04 2010 W. Michael Petullo <mike[@]flyn.org> - 0.0.24-1
- New upstream version

* Wed Feb 17 2010 W. Michael Petullo <mike[@]flyn.org> - 0.0.23-1
- New upstream version, set User= in dmapd.conf

* Fri Feb 05 2010 W. Michael Petullo <mike[@]flyn.org> - 0.0.22-1
- New upstream version

* Thu Jan 28 2010 W. Michael Petullo <mike[@]flyn.org> - 0.0.21-1
- New upstream version
- no longer install /etc/sysconfig/dmapd, use /etc/dmapd.conf
- no longer create /var/db/dmapd*

* Thu Jan 14 2010 W. Michael Petullo <mike[@]flyn.org> - 0.0.18-2
- use macro for init directory throughout

* Fri Dec 04 2009 W. Michael Petullo <mike[@]flyn.org> - 0.0.18-1
- New upstream version
- reorder specfile blocks to resemble output of rpmdev-newspec
- add noreplace to config file
- do not depend on avahi-, dbus- or libsoup-devel, just libdmapsharing
- make pre, post, etc. requirements satisfy Fedora SysV init docs

* Sun Nov 22 2009 W. Michael Petullo <mike[@]flyn.org> - 0.0.17-1
- New upstream version
- Fix ldconfig placement
- No empty NEWS
- Move data directory to /var/db/dmapd

* Sat Nov 21 2009 W. Michael Petullo <mike[@]flyn.org> - 0.0.16-1
- New upstream version
- Move %%doc to %%files
- No empty FAQ
- Require GraphicsMagick-devel

* Tue Nov 10 2009 W. Michael Petullo <mike[@]flyn.org> - 0.0.15-1
- New upstream version
- Require dbus-devel to build
- Properly set permissions of /etc/sysconfig/dmapd
- Run ldconfig
- Fix user creation

* Thu Jul 23 2009 W. Michael Petullo <mike[@]flyn.org> - 0.0.14-1
- New upstream version
- Fix URL

* Thu May 07 2009 W. Michael Petullo <mike[@]flyn.org> - 0.0.10-1
- New upstream version
- Use %%{buildroot} exclusively
- Add requirements for pre, post, preun and postun
- Remove disttags from changelog
- Remove extra defattr

* Sun Jan 11 2009 W. Michael Petullo <mike[@]flyn.org> - 0.0.8-1
- Initial package for Fedora

