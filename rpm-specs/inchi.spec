%define inchi_so_ver 1.05.00
%define url_ver 105

Summary: The IUPAC International Chemical Identifier library
Name: inchi
Version: 1.0.5
Release: 10%{?dist}
URL: https://www.inchi-trust.org/about-the-inchi-standard/
Source0: https://www.inchi-trust.org/download/%{url_ver}/INCHI-1-SRC.zip
Source1: https://www.inchi-trust.org/download/%{url_ver}/INCHI-1-DOC.zip
Source2: https://www.inchi-trust.org/download/%{url_ver}/INCHI-1-TEST.zip
Patch0: %{name}-rpm.patch
License: LGPLv2+
BuildRequires: dos2unix
BuildRequires: gcc

%description
The IUPAC International Chemical Identifier (InChITM) is a non-proprietary
identifier for chemical substances that can be used in printed and
electronic data sources thus enabling easier linking of diverse data
compilations. It was developed under IUPAC Project 2000-025-1-800 during
the period 2000-2004. Details of the project and the history of its
progress are available from the project web site.

This package contains the command line conversion utility.

%package libs
Summary: The IUPAC International Chemical Identifier library

%description libs
The IUPAC International Chemical Identifier (InChITM) is a non-proprietary
identifier for chemical substances that can be used in printed and
electronic data sources thus enabling easier linking of diverse data
compilations. It was developed under IUPAC Project 2000-025-1-800 during
the period 2000-2004. Details of the project and the history of its
progress are available from the project web site.

%package devel
Summary: Development headers for the InChI library
Requires: %{name}-libs%{_isa} = %{version}-%{release}

%description devel
The inchi-devel package includes the header files and libraries
necessary for developing programs using the InChI library.

If you are going to develop programs which will use this library
you should install inchi-devel.  You'll also need to have the
inchi package installed.

%package doc
Summary: Documentation for the InChI library
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
The inchi-doc package contains user documentation for the InChI software
and InChI library API reference for developers.

%prep
%setup -q -n INCHI-1-SRC -a 1 -a 2
%patch0 -p1 -b .r
for file in LICENCE readme.txt ; do
  dos2unix -k $file
done
pushd INCHI-1-TEST/test
unzip -d reference -qq -a InChI_TestSet-result.zip
dos2unix -k reference/*.txt
sed -i -e 's,./inchi-1,../../INCHI_API/bin/Linux/inchi_main,g' TestSet2InChI.sh
popd

%build
pushd INCHI_API/demos/inchi_main/gcc
%{__make} OPTFLAGS="$RPM_OPT_FLAGS -Wno-comment -Wno-parentheses -Wno-unused -Wno-unused-but-set-variable" %{?_smp_mflags}
popd

%install
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}/inchi}
install -pm 755 INCHI_API/bin/Linux/inchi_main $RPM_BUILD_ROOT%{_bindir}/inchi-1
install -p INCHI_API/bin/Linux/libinchi.so.%{inchi_so_ver} $RPM_BUILD_ROOT%{_libdir}
ln -s libinchi.so.%{inchi_so_ver} $RPM_BUILD_ROOT%{_libdir}/libinchi.so.1
ln -s libinchi.so.1               $RPM_BUILD_ROOT%{_libdir}/libinchi.so
install -pm644 INCHI_BASE/src/{inchi_api,ixa}.h $RPM_BUILD_ROOT%{_includedir}/inchi

%check
export LD_LIBRARY_PATH=$(pwd)/INCHI_API/bin/Linux/
pushd INCHI-1-TEST/test
sh ./TestSet2InChI.sh
for t in its-*.txt ; do cmp $t reference/$t ; done
popd

%files
%{_bindir}/inchi-1

%files libs
%license LICENCE
%doc readme.txt
%{_libdir}/libinchi.so.1*

%files devel
%{_includedir}/inchi
%{_libdir}/libinchi.so

%files doc
%doc INCHI-1-DOC/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Dominik Mierzejewski <rpm@greysector.net> 1.0.5-6
- Add BR: gcc for https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot
- Drop unnecessary scriptlets
- Drop ancient Obsoletes:
- Switch to HTTPS in URLs

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Dominik Mierzejewski <rpm@greysector.net> 1.0.5-1
- update to 1.05 (final)
- drop obsolete patch

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 11 2016 Dominik Mierzejewski <rpm@greysector.net> 1.0.5-0.2
- fix some misc issues (patch by Burt Leland and Noel O'Boyle)
- silence some harmless warnings to reduce gcc warning spam

* Fri Oct 07 2016 Dominik Mierzejewski <rpm@greysector.net> 1.0.5-0.1
- update to 1.05 (pre-release)
- update URLs
- include new IXA API header
- use license macro
- drop obsolete defattr

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 01 2014 Dominik Mierzejewski <rpm@greysector.net> 1.0.4-6
- update source URLs
- drop obsolete specfile parts
- enable testsuite
- build CLI tool and move libinchi to -libs subpackage
- fix undefined weak symbol warnings for libinchi

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 12 2011 Dominik Mierzejewski <rpm@greysector.net> 1.0.4-1
- update to 1.04
- update homepage and source URLs
- use dos2unix for EOL conversion

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 07 2010 Dominik Mierzejewski <rpm@greysector.net> 1.0.3-1
- updated to 1.03 (ABI break)
- rebased patch

* Thu Oct 08 2009 Dominik Mierzejewski <rpm@greysector.net> 1.0.2-2
- added doc subpackage (based on a patch by Takanori MATSUURA)

* Wed Aug 26 2009 Dominik Mierzejewski <rpm@greysector.net> 1.0.2-1
- updated to final 1.02 release (unfortunately, it breaks ABI)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.2-0.3
- Autorebuild for GCC 4.3

* Mon Oct 01 2007 Dominik Mierzejewski <rpm@greysector.net> 1.0.2-0.2
- updated license tag
- fixed non-Unix EOLs in docs
- fixed dangling symlinks

* Thu Sep 06 2007 Dominik Mierzejewski <rpm@greysector.net> 1.0.2-0.1
- updated to 1.02b
- dropped WDI patch (upstream'd)
- updated license tag

* Sun Jul 01 2007 Dominik Mierzejewski <rpm@greysector.net> 1.0.1-8
- initial build
