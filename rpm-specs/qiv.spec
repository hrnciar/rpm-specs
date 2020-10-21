Name:           qiv
Version:        2.3.1
Release:        12%{?dist}

Summary:        Quick Image Viewer

License:        GPLv2
URL:            http://spiegl.de/qiv/
Source0:        http://spiegl.de/qiv/download/%{name}-%{version}.tgz
Patch0:         %{name}-optflags.patch
# call exit instead of abort on child error
Patch1:         %{name}-exit-on-child-error.patch
Patch2:         %{name}-2.3.1-remove-unused-vars.patch

BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  imlib2-devel
BuildRequires:  file-devel
BuildRequires:  lcms2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libexif-devel
BuildRequires:  libtiff-devel

%description
qiv is a very small and pretty fast gdk2/Imlib2 image viewer.


%prep
%setup -q
%patch0 -p1 -b .optflags
%patch1 -p1 -b .childexit
%patch2 -p1 -b .unused

%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 qiv $RPM_BUILD_ROOT%{_bindir}/qiv
install -Dpm 644 qiv.1 $RPM_BUILD_ROOT%{_mandir}/man1/qiv.1
chmod 644 contrib/qiv-command.example


%files

%doc README Changelog README.COPYING README.TODO contrib/qiv-command.example
%{_bindir}/qiv
%{_mandir}/man1/qiv.1*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 22 2015 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 2.3.1-1
- version upgrade

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov 30 2013 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.3-1
- version upgrade

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.2.4-2
- Rebuild for new libpng

* Thu May 05 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.2.4-1
- version upgrade (#701603)

* Wed Mar 02 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.2.3-2
- exit instead of abort on child error (#680602)

* Mon Mar 29 2010 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 2.2.3-1
- version upgrade (#560965)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 11 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 2.0-9
- Rebuilt for gcc43

* Wed Aug 22 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> 2.0-8
- new license tag
- rebuild for buildid

* Tue Nov 07 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> 2.0-7
- fix #213581

* Fri Sep 15 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> 2.0-6
- FE6 rebuild

* Sun Jun 18 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> 2.0-5
- bump

* Thu Feb 16 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> 2.0-4
- Rebuild for Fedora Extras 5

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 2.0-3
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sat Jun 12 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.0-0.fdr.1
- Update to 2.0.

* Tue Jan 27 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.9-0.fdr.1
- Update to 1.9.

* Wed Jul 09 2003 Andreas Bierfert (awjb) <andreas.bierfert[AT]awbsworld.de>
0:1.8-0.fdr.2
- Fixed minor issues
* Mon Jun 30 2003 Andreas Bierfert (awjb) <andreas.bierfert[AT]awbsworld.de>
0:1.8-0.fdr.1
- Initial RPM release.
