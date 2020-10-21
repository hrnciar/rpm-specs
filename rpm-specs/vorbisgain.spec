Name:           vorbisgain
Version:        0.36
Release:        28%{?dist}
Summary:        Adds tags to Ogg Vorbis files to adjust the volume

License:        LGPLv2
URL:            http://sjeng.org/vorbisgain.html
Source0:	http://sjeng.org/ftp/vorbis/%{name}-%{version}.zip
Patch0:		%{name}-spelling.patch
Patch1:         001-fprintf_fix.patch
Patch2:         vorbisgain-c99.patch

BuildRequires:  gcc
BuildRequires:	libvorbis-devel
BuildRequires:	libogg-devel


%description
VorbisGain is a utility that uses a psychoacoustic method to correct the
volume of an Ogg Vorbis file to a predefined standardized loudness.

It needs player support to work. Non-supporting players will play back
the files without problems, but you'll miss out on the benefits.
Nowadays most good players such as ogg123, xmms and mplayer are already
compatible. 


%prep
%setup -q
%patch0 -p1 -b .spelling
%patch1 -p1 -b .fprintf
%patch2 -p1 -b .c99


%build
chmod 755 configure
%configure --enable-recursive
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep  9 2019 Florian Weimer <fweimer@redhat.com> - 0.36-26
- Second part of C99 mode build fix

* Mon Sep  9 2019 Florian Weimer <fweimer@redhat.com> - 0.36-25
- Fix building in C99 mode

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 31 2013 Brian Pepple <bpepple@fedoraproject.org> - 0.36-13
- Add patch to fix build failure. (#1025254)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Brian Pepple <bpepple@fedoraproject.org> - 0.36-11
- Remove some old depreciated cruft from the spec file.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 09 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.36-8
- Rebuild for new gcc.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 20 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.36-6
- Drop buildroot & clean section since they are no longer necessary.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  8 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.36-3
- Rebuild for gcc-4.3.

* Tue Aug 21 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.36-2
- Rebuild.
- Update license tag.

* Fri Oct 13 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.36-1
- Update to 0.36.
- Add patch to fix spelling errors in manpage.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.34-3
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.34-2
- Rebuild for FC6.
- Minor formatting changes.

* Sat May 13 2006 Noa Resare <noa@resare.com> 0.34-1
- Initial spec
