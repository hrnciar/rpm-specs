#global pre beta.4

Name:          tesseract
Version:       4.1.1
Release:       3%{?pre:.%pre}%{?dist}
Summary:       Raw OCR Engine

License:       ASL 2.0
URL:           https://github.com/tesseract-ocr/%{name}
Source0:       https://github.com/tesseract-ocr/tesseract/archive/%{version}%{?pre:-%pre}/%{name}-%{version}%{?pre:-%pre}.tar.gz

# Tweak location of tessdata folder
Patch0:        tesseract_datadir.patch

BuildRequires: automake
BuildRequires: autoconf-archive
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: libtiff-devel
BuildRequires: leptonica-devel
BuildRequires: cairo-devel
BuildRequires: libicu-devel
BuildRequires: pango-devel

Requires:      tesseract-langpack-eng


%description
A commercial quality OCR engine originally developed at HP between 1985 and
1995. In 1995, this engine was among the top 3 evaluated by UNLV. It was
open-sourced by HP and UNLV in 2005.


%package devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains header file for
developing applications that use %{name}.


%package tools
Summary:       Training tools for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description tools
The %{name}-tools package contains tools for training %{name}.


%prep
%autosetup -p1 -n %{name}-%{version}%{?pre:-%pre}


%build
autoreconf -ifv
%configure --disable-static

%make_build
%make_build training


%install
%make_install
%make_install training-install

find %{buildroot}%{_libdir} -type f -name '*.la' -delete

# Create directory for tessdata
mkdir -p %{buildroot}/%{_datadir}/%{name}/tessdata/



%ldconfig_scriptlets


%files
%license LICENSE
%doc AUTHORS ChangeLog README.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/tessdata
%{_datadir}/%{name}/tessdata/configs/
%{_datadir}/%{name}/tessdata/tessconfigs/
%{_datadir}/%{name}/tessdata/pdf.ttf
%{_libdir}/lib%{name}*.so.4*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/ambiguous_words
%{_bindir}/classifier_tester
%{_bindir}/cntraining
%{_bindir}/combine_lang_model
%{_bindir}/combine_tessdata
%{_bindir}/dawg2wordlist
%{_bindir}/language-specific.sh
%{_bindir}/lstmeval
%{_bindir}/lstmtraining
%{_bindir}/merge_unicharsets
%{_bindir}/mftraining
%{_bindir}/set_unicharset_properties
%{_bindir}/shapeclustering
%{_bindir}/tesstrain.sh
%{_bindir}/tesstrain_utils.sh
%{_bindir}/text2image
%{_bindir}/unicharset_extractor
%{_bindir}/wordlist2dawg


%changelog
* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 4.1.1-3
- Rebuild for ICU 67

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 27 2019 Sandro Mani <manisandro@gmail.com> - 4.1.1-1
- Update to 4.1.1

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 4.1.0-2
- Rebuild for ICU 65

* Sun Jul 28 2019 Sandro Mani <manisandro@gmail.com> - 4.1.0-1
- Update to 4.1.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Sandro Mani <manisandro@gmail.com> - 4.0.0-6
- Add Requires: tesseract-langpack-eng

* Mon Jul 22 2019 Sandro Mani <manisandro@gmail.com> - 4.0.0-5
- Drop langpack and script subpackages, moved to separate tesseract-tessdata package

* Mon Jul 01 2019 Sandro Mani <manisandro@gmail.com> - 4.0.0-4
- Fix -frk subpackage description (#1721228)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 4.0.0-2
- Rebuild for ICU 63

* Tue Nov 13 2018 Sandro Mani <manisandro@gmail.com> - 4.0.0-1
- Update to 4.0.0

* Tue Sep 25 2018 Sandro Mani <manisandro@gmail.com> - 4.0.0-0.3.beta.4
- Update to 4.0.0-beta.4

* Sat Aug 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.05.02-1
- Update to latest version
- Fix descriptions of language packs

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.05.01-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 3.05.01-8
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 3.05.01-7
- Rebuild for ICU 61.1

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.coM> - 3.05.01-6
- Add missing BR: gcc-c++, make

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.05.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 3.05.01-4
- Rebuild for ICU 60.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.05.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.05.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Sandro Mani <manisandro@gmail.com> - 3.05.01-1
- Update to 3.05.01

* Tue Feb 21 2017 Sandro Mani <manisandro@gmail.com> - 3.05.00-1
- Update to 3.05.00

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.04.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Adam Williamson <awilliam@redhat.com> - 3.04.01-3
- Rebuild (to fix behaviour on big-endian arches after leptonica endianness fix)

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 3.04.01-2
- rebuild for ICU 57.1

* Fri Feb 19 2016 Sandro Mani <manisandro@gmail.com> - 3.04.01-1
- Update to 3.04.01

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.04.00-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Sandro Mani <manisandro@gmail.com> - 3.04.00-5
- Rebuild (leptonica)

* Tue Jan 26 2016 Sandro Mani <manisandro@gmail.com> - 3.04.00-4
- Rebuild (leptonica)

* Mon Jan 25 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.04.00-3
- Added virtual provides to follow langpacks naming guidelines
- Added Supplements tag for new way of langpacks installation

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 3.04.00-2
- rebuild for ICU 56.1

* Sat Sep 12 2015 Sandro Mani <manisandro@gmail.com> - 3.04.00-1
- Update to 3.04.00

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-0.6.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.03-0.5.rc1
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 3.03-0.4.rc1
- rebuild for ICU 54.1

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 3.03-0.3.rc1
- rebuild for ICU 53.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Sandro Mani <manisandro@gmail.com> - 3.03-0.1.rc1
- Update to v3.03-rc1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 27 2014 Karol Trzcionka <karlik at fedoraproject.org> - 3.02.02-3
- Fix rhbz#1037350 (-Werror=format-security)
- Add OSD data
- Remove BuildRoot tag

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 27 2013 Karol Trzcionka <karlik at fedoraproject.org> - 3.02.02-1
- Update to v3.02.02
- Apply pkgconfig patch rhbz#904806

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 06 2012 Karol Trzcionka <karlik at fedoraproject.org> - 3.01-1
- Update to v3.01
- Add manual pages
- Add BRs leptonica, automake

* Tue Jul 31 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.00-6
- Fix FTBFS with g++ 4.7

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.00-4
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 16 2010 Karol Trzcionka <karlikt at gmail.com> - 3.00-1
- Update to v3.00
- Remove static libs and add dynamic

* Wed Oct 21 2009 Karol Trzcionka <karlikt at gmail.com> - 2.04-1
- Update to v2.04
- Add static libraries to -devel subpackage

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 04 2009 Caolán McNamara <caolanm@redhat.com> - 2.03-3
- include stdio.h for snprintf

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun May 04 2008 Karol Trzcionka <karlikt at gmail.com> - 2.03-1
- Update to v2.03
* Sat Feb 09 2008 Karol Trzcionka <karlikt at gmail.com> - 2.01-2
- Rebuild for gcc43
* Fri Sep 07 2007 Karol Trzcionka <karlikt at gmail.com> - 2.01-1
- Upgrade to v2.01
* Tue Aug 21 2007 Karol Trzcionka <karlikt at gmail.com> - 2.00-1
- Upgrade to v2.00
* Thu Mar 22 2007 Karol Trzcionka <karlikt at gmail.com> - 1.04-1
- Change url and source
- Update to v1.04
- Make patch bases on upstream's v1.04b
- Change compilefix patch
- Adding -devel subpackage
* Thu Mar 22 2007 Karol Trzcionka <karlikt at gmail.com> - 1.03-2
- Including patch bases on cvs
* Tue Feb 13 2007 Karol Trzcionka <karlikt at gmail.com> - 1.03-1
- Update to v1.03
* Sat Jan 27 2007 Karol Trzcionka <karlikt at gmail.com> - 1.02-3
- Update BRs
- Fix x86_64 compile
* Sat Dec 30 2006 Karol Trzcionka <karlikt at gmail.com> - 1.02-2
- Fixed rpmlint warning in SRPM
* Fri Dec 29 2006 Karol Trzcionka <karlikt at gmail.com> - 1.02-1
- Initial Release
