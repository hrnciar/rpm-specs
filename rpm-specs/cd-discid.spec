Name:           cd-discid
Version:        1.4
Release:        17%{?dist}
Summary:        Utility to get CDDB discid information

# Also "Larry Wall's Artistic" upstream, but that's not accepted in Fedora
License:        GPLv2+
URL:            http://linukz.org/cd-discid.shtml
Source0:        http://linukz.org/download/%{name}-%{version}.tar.gz
BuildRequires:  gcc

%description
cd-discid is a backend utility to get CDDB discid information for a
CD-ROM disc.  It was originally designed for cdgrab (now abcde), but
can be used for any purpose requiring CDDB data.


%prep
%setup -q


%build
%set_build_flags
make %{?_smp_mflags}


%install
%make_install PREFIX=%{_prefix} STRIP=:


%files
%license COPYING
%doc changelog README
%{_bindir}/cd-discid
%{_mandir}/man1/cd-discid.1*


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.4-13
- Add BR: gcc for https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot
- Clean-up: drop obsolete stuff, use modern macros to simplify build

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Ville Skyttä <ville.skytta@iki.fi> - 1.4-5
- Ship COPYING as %%license where available

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.4-1
- Update to 1.4.
- Fix bogus date in %%changelog.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.3.1-1
- Update to 1.3.1.
- Build with $RPM_LD_FLAGS.
- Clean up specfile constructs no longer needed in Fedora or EL6+.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep  2 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.1-1
- Update to 1.1 (#520781).

* Wed Aug 26 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.0-1
- Update to 1.0 (#519289).
- Update URLs.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.9-9
- Update source tarball URL.

* Sat Feb  9 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.9-8
- Rebuild.

* Thu Aug 16 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.9-7
- License: GPLv2+
- Add URL.

* Tue Aug 29 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.9-6
- Rebuild.

* Wed Feb 15 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.9-5
- Rebuild, specfile cleanup.

* Tue Jul 26 2005 Nils Philippsen <nphilipp@redhat.com>
- install proper man page (#164105, fix by Paul W. Frields)

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Jan 17 2005 Ville Skyttä <ville.skytta@iki.fi> - 0.9-2
- Honor $RPM_OPT_FLAGS.
- Improve description.
- "Fix" man page permissions.

* Wed Apr 14 2004 Nils Philippsen <nphilipp@redhat.com>
- version 0.9

* Tue May 21 2002 Nils Philippsen <nphilipp@redhat.com>
- version 0.7

* Wed Apr 25 2001 Nils Philippsen <nphilipp@redhat.com>
- version 0.6

* Tue Jan 09 2001 Nils Philippsen <nphilipp@redhat.com>
- version 0.4
- initial build

