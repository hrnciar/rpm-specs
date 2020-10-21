Name:           qmmp-plugin-pack
Version:        1.4.0
Release:        1%{?dist}
Summary:        A set of extra plugins for Qmmp

License:        GPLv2+
URL:            http://qmmp.ylsoftware.com/plugins.php
Source0:        http://qmmp.ylsoftware.com/files/plugins/%{name}-%{version}.tar.bz2

BuildRequires:  qmmp-devel >= 1.4.0
BuildRequires:  cmake
BuildRequires:  libsamplerate-devel
BuildRequires:  libxmp-devel
BuildRequires:  qt5-linguist
BuildRequires:  taglib-devel
BuildRequires:  yasm

%description
Plugin pack is a set of extra plugins for Qmmp.

 * FFap - enhanced Monkey's Audio (APE) decoder
   (24-bit samples and embedded cue support)
 * SRC - sample rate converter
 * XMP - module player with use of the libxmp library
 * Goom - audio visualization based on goom project
 * Ytb - audio playback from YouTube (uses youtube-dl)


%prep
%setup -q


%build
%cmake \
        -D USE_FFVIDEO:BOOL=FALSE \
        -D PLUGIN_DIR=%{_lib}/qmmp \
        .
%cmake_build %{?_smp_mflags}


%install
%cmake_install


%files
%doc AUTHORS ChangeLog.rus README README.RUS
%license COPYING
%{_libdir}/qmmp/Effect/*.so
%{_libdir}/qmmp/Input/*.so
%{_libdir}/qmmp/Transports/*.so
%{_libdir}/qmmp/Visual/*.so
%{_metainfodir}/%{name}.appdata.xml


%changelog
* Fri Jul 31 2020 Karel Volný <kvolny@redhat.com> 1.4.0-1
- new version 1.4.0 (rhbz#1828956)
- see the upstream changelog at http://qmmp.ylsoftware.com/
- adds YouTube plugin
- adds appdata

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Karel Volný <kvolny@redhat.com> 1.3.2-1
- new version 1.3.2 (rhbz#1817642)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 08 2019 Karel Volný <kvolny@redhat.com> 1.3.1-1
- new version 1.3.1
- see the upstream changelog at http://qmmp.ylsoftware.com/
- define unversioned plugin dir
# ^ I will NOT support parallel installs
- history plugin and mpg123 support moved to qmmp

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 30 2018 Karel Volný <kvolny@redhat.com> 1.2.3-1
- new version 1.2.3
- see the upstream changelog at http://qmmp.ylsoftware.com/
- drop Provides/Obsoletes, after four releases

* Thu Jul 26 2018 Karel Volný <kvolny@redhat.com> 1.2.2-1
- new version 1.2.2 (#1604794)
- fixes Goom plugin crash (#1601271)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 20 2018 Karel Volný <kvolny@redhat.com> 1.2.1-1
- new version 1.2.1

* Tue Apr 17 2018 Karel Volný <kvolny@redhat.com> 1.2.0-1
- new version 1.2.0
- adds history and Goom plugins
- disable ffvideo plugin
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 Karel Volný <kvolny@redhat.com> 1.1.5-1
- new version 1.1.5 (#1505140)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Mon Aug 07 2017 Karel Volný <kvolny@redhat.com> 1.1.4-1
- new version 1.1.4
- see the upstream changelog at http://qmmp.ylsoftware.com/
- don't change Provides version for the transition period

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 24 2016 Karel Volný <kvolny@redhat.com> 1.1.3-4
- use hardcoded Obsoletes version (oops, should have been part of the previous change)

* Thu Nov 24 2016 Karel Volný <kvolny@redhat.com> 1.1.3-3
- use hardcoded Provides version not to conflict in the future
  (as suggested by Michael Mráka)

* Thu Nov 24 2016 Karel Volný <kvolny@redhat.com> 1.1.3-2
- enable mpg123 plugin and replace qmmp-plugin-pack-freeworld (#1395861)
  thanks to Yaakov Selkowitz

* Thu Oct 06 2016 Karel Volný <kvolny@redhat.com> 1.1.3-1
- new version 1.1.3 (#1370808)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Mon Jul 11 2016 Karel Volný <kvolny@redhat.com> 1.1.1-1
- new version 1.1.1 (#1352737)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Thu Jun 23 2016 Karel Volný <kvolny@redhat.com> 1.1.0-1
- new version 1.1.0 (#1348549)
- see the upstream changelog at http://qmmp.ylsoftware.com/
- adds SRC (removed from qmmp)

* Fri Jun 03 2016 Karel Volný <kvolny@redhat.com> 1.0.4-1
- new version 1.0.4 (#1341422)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Mon May 02 2016 Karel Volný <kvolny@redhat.com> 1.0.3-1
- new version 1.0.3 (#1332177)
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Karel Volný <kvolny@redhat.com> 1.0.2-1
- new version 1.0.2
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Mon Oct 12 2015 Karel Volný <kvolny@redhat.com> 1.0.1-1
- new version 1.0.1
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Wed Oct 07 2015 Karel Volný <kvolny@redhat.com> 1.0.0-1
- new version 1.0.0
- see the upstream changelog at http://qmmp.ylsoftware.com/
- uses Qt5

* Wed Sep 09 2015 Karel Volný <kvolny@redhat.com> 0.9.0-1
- new version 0.9.0
- see the upstream changelog at http://qmmp.ylsoftware.com/
- removes QSUI (added to qmmp)
- adds XMP

* Tue Aug 25 2015 Karel Volný <kvolny@redhat.com> 0.8.6-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/
- some specfile improvements

* Wed Jun 24 2015 Karel Volný <kvolny@redhat.com> 0.8.4-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.3-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 03 2015 Karel Volný <kvolny@redhat.com> 0.8.3-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 14 2014 Karel Volný <kvolny@redhat.com> 0.8.1-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Tue Jul 15 2014 Karel Volný <kvolny@redhat.com> 0.8.0-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Mon Jun 09 2014 Karel Volný <kvolny@redhat.com> 0.7.7-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 17 2014 Karel Volný <kvolny@redhat.com> 0.7.4-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Wed Dec 11 2013 Karel Volný <kvolny@redhat.com> 0.7.3-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Tue Aug 27 2013 Karel Volný <kvolny@redhat.com> 0.7.2-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Karel Volný <kvolny@redhat.com> 0.7.1-1
- new version
- see upstream changelog at http://qmmp.ylsoftware.com/

* Sun Apr 28 2013 Karel Volný <kvolny@redhat.com> 0.7.0-1
- new version
- see upstream changelog at http://qmmp.ylsoftware.com/
- project URLs changes

* Tue Apr 02 2013 Karel Volný <kvolny@redhat.com> 0.6.6-1
- new version
- see upstream changelog at http://qmmp.ylsoftware.com/index_en.php

* Tue Jan 29 2013 Karel Volný <kvolny@redhat.com> 0.6.4-1
- new version
- see upstream changelog at http://qmmp.ylsoftware.com/index_en.php

* Tue Dec 11 2012 Karel Volný <kvolny@redhat.com> 0.6.3-1
- new version
- see upstream changelog at http://qmmp.ylsoftware.com/index_en.php

* Fri Aug 24 2012 Karel Volný <kvolny@redhat.com> 0.6.2-2
- update spec to newer style as suggested in package review
- removed %%buildroot actions
- removed %%clean section which got empty
- removed %%defattr

* Fri Aug 17 2012 Karel Volný <kvolny@redhat.com> 0.6.2-1
- new version
- fixes FSF address and execstack issues found by rpmlint
- see upstream changelog at http://qmmp.ylsoftware.com/index_en.php

* Tue Jul 31 2012 Karel Volný <kvolny@redhat.com> 0.6.1-1
- initial Fedora release
