Name:           scim-m17n
Version:        0.2.3
Release:        24%{?dist}
Summary:        SCIM IMEngine for m17n-lib

License:        GPLv2+
URL:            http://www.scim-im.org/projects/imengines
Source0:        %{name}-%{version}.tar.gz

Buildrequires:  scim-devel, m17n-lib-devel
BuildRequires:  gcc-c++

Obsoletes:      iiimf-le-unit <= 1:12.2
Requires:       scim >= 1.4.4

Patch0:         %{name}-no-M17N-prefix.patch
Patch1:         %{name}-aarch64.patch

%description
scim-m17n provides a SCIM IMEngine for m17n-lib, which allows
input of many languages using the input table maps from m17n-db.


%prep
%autosetup -p1

%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

rm $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/IMEngine/m17n.la


%files
%doc AUTHORS README THANKS
%license COPYING
%{_libdir}/scim-1.0/*/IMEngine/m17n.so
%{_datadir}/scim/icons/*


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-24
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.2.3-18
- Add BuildRequires: gcc-c++ as per packaging guidelines

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.3-11
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 24 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.2.3-7
- Resolves:rh#926496 - Does not support aarch64 in f19 and rawhide

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May  2 2009 Jens Petersen <petersen@redhat.com> - 0.2.3-1
- update to 0.2.3
- scim-m17n-0.2.2-gcc43.patch upstream

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 11 2008 Parag <pnemade@redhat.com> - 0.2.2-3
- Rebuild for gcc 4.3

* Wed Aug 22 2007 Parag Nemade <pnemade@redhat.com> - 0.2.2-2
- rebuild against new rpm package

* Mon Aug 13 2007 Parag Nemade <pnemade@redhat.com> 
- update License tag

* Mon May 21 2007 Jens Petersen <petersen@redhat.com> - 0.2.2-1
- update to 0.2.2
- scim-m17n-US-keyboard-211266.patch is no longer needed

* Tue Oct 24 2006 Jens Petersen <petersen@redhat.com> - 0.2.1-1
- update to 0.2.1 release
- scim-m17n-0.2.0-unique-uuid.patch no longer needed
- add scim-m17n-us-keyboard-211266.patch to follow scim keyboard config
  (suzhe, #211266)

* Mon Aug 28 2006 Jens Petersen <petersen@redhat.com> - 0.2.0-6
- require scim >= 1.4.4 (#181751)

* Tue Jul 18 2006 Jens Petersen <petersen@redhat.com> - 0.2.0-5
- remove common prefix from IME names with scim-m17n-no-M17N-prefix.patch

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.2.0-4.1
- rebuild

* Tue Jul  4 2006 Jens Petersen <petersen@redhat.com> - 0.2.0-4
- add scim-m17n-0.2.0-unique-uuid.patch to make factory ids unique

* Fri Mar 31 2006 Jens Petersen <petersen@redhat.com> - 0.2.0-3
- rebuild without libstdc++so7

* Thu Mar  2 2006 Jens Petersen <petersen@redhat.com> - 0.2.0-2
- obsolete iiimf-le-unitle for upgrades (#181479,#183305)

* Sun Feb 12 2006 Jens Petersen <petersen@redhat.com> - 0.2.0-1
- update to 0.2.0 release

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.1.4-3.1
- bump again for double-long bug on ppc(64)

* Thu Feb  9 2006 Jens Petersen <petersen@redhat.com> - 0.1.4-3
- build conditionally with libstdc++so7 preview library (#166041)
  - add with_libstdc_preview switch and tweak libtool to link against newer lib
- specify filelist more precisely

* Fri Dec 16 2005 Jens Petersen <petersen@redhat.com> - 0.1.4-2
- import to Fedora Core

* Wed Oct  5 2005 Jens Petersen <petersen@redhat.com> - 0.1.4-1
- initial packaging for Fedora Extras

* Mon Jun 20 2005 Jens Petersen <petersen@redhat.com>
- rebuild against scim-1.3.1

* Fri Jun  3 2005 Jens Petersen <petersen@redhat.com>
- Initial build.
