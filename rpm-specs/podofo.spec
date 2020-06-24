Name:           podofo
Version:        0.9.6
Release:        10%{?dist}
Summary:        Tools and libraries to work with the PDF file format

# The library is licensed under the LGPL.
# The tests and tools which are included in PoDoFo are licensed under the GPL.
# See the files COPYING and COPYING.LIB for details, see COPYING.exception.
License:        GPLv2+ and LGPLv2+ with exceptions
URL:            http://podofo.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Fix failure to detect FreeType
Patch0:         podofo-0.9.4-freetype.patch
# Don't attempt to copy non-existing testdata dir
Patch1:         podofo_tests.patch
# Fix pkg-config file
Patch2:         podofo_pkgconfig.patch

# Backport patch for CVE-2018-5783
# https://sourceforge.net/p/podofo/code/1949
Patch10:        podofo_CVE-2018-5783.patch
# Backport patch for CVE-2018-11254
# https://sourceforge.net/p/podofo/code/1941
Patch11:        podofo_CVE-2018-11254.patch
# Backport patch for CVE-2018-11255
# https://sourceforge.net/p/podofo/code/1952
Patch12:        podofo_CVE-2018-11255.patch
# Backport patch for CVE-2018-11256
# https://sourceforge.net/p/podofo/code/1938
Patch13:        podofo_CVE-2018-11256.patch
# Backport patch for CVE-2018-12982
# https://sourceforge.net/p/podofo/code/1948
Patch14:        podofo_CVE-2018-12982.patch
# Backport patch for CVE-2018-14320
# https://sourceforge.net/p/podofo/code/1953
Patch15:        podofo_CVE-2018-14320.patch
# Backport patch for CVE-2018-19532
# https://sourceforge.net/p/podofo/code/1950
Patch16:        podofo_CVE-2018-19532.patch
# Backport patch for CVE-2018-20751
# https://sourceforge.net/p/podofo/code/1954
Patch17:        podofo_CVE-2018-20751.patch
# Backport patch for CVE-2019-9199
# https://sourceforge.net/p/podofo/code/1971/
Patch18:        podofo_CVE-2019-9199.patch
# Backport patch for CVE-2019-9687
# https://sourceforge.net/p/podofo/code/1969
Patch19:        podofo_CVE-2019-9687.patch

# Downstream patch for CVE-2019-20093
# https://sourceforge.net/p/podofo/tickets/75/
Patch20:        podofo_CVE-2019-20093.patch

BuildRequires:  gcc-c++
%if %{?el7:1}%{!?el7:0}
BuildRequires:  cmake3
%else
BuildRequires:  cmake
%endif
BuildRequires:  cppunit-devel
BuildRequires:  doxygen
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  ghostscript
BuildRequires:  libidn-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  lua-devel
BuildRequires:  openssl-devel
BuildRequires:  texlive-epstopdf-bin
BuildRequires:  zlib-devel


%description
PoDoFo is a library to work with the PDF file format. The name comes from
the first letter of PDF (Portable Document Format). A few tools to work
with PDF files are already included in the PoDoFo package.

The PoDoFo library is a free, portable C++ library which includes classes
to parse PDF files and modify their contents into memory. The changes can be
written back to disk easily. The parser can also be used to extract
information from a PDF file (for example the parser could be used in a PDF
viewer). Besides parsing PoDoFo includes also very simple classes to create
your own PDF files. All classes are documented so it is easy to start writing
your own application using PoDoFo.


%package libs
Summary:        Runtime library for %{name}
License:        LGPLv2+

%description libs
Runtime library for %{name}.


%package devel
Summary:        Development files for %{name} library
License:        LGPLv2+
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       openssl-devel%{?_isa}

%description devel
Development files and documentation for the %{name} library.


%prep
%autosetup -p1

# disable timestamps in docs
echo "HTML_TIMESTAMP = NO" >> Doxyfile

# switch to system provided files
rm cmake/modules/FindFREETYPE.cmake
rm cmake/modules/FindZLIB.cmake


%build
%if %{?el7:1}%{!?el7:0}
%cmake3 -DPODOFO_BUILD_SHARED=1 \
%else
%cmake -DPODOFO_BUILD_SHARED=1 \
%endif
%if 0%{?__isa_bits} == 64
-DWANT_LIB64=1 \
%endif
.
%make_build

# build the docs
doxygen

# set timestamps on generated files to some constant
find doc/html -exec touch -r %{SOURCE0} {} \;


%install
%make_install


%check
# Takes ages on x86_64....
# ./test/unit/podofo-test || :


%files
%license COPYING
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}*.1*

%files libs
%doc AUTHORS ChangeLog FAQ.html README.html TODO
%license COPYING.LIB COPYING.exception
%{_libdir}/*.so.0.9.6

%files devel
%doc doc/html examples
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/lib%{name}.pc


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Sandro Mani <manisandro@gmail.com> - 0.9.6-9
- Add patch for CVE-2019-20093

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Sandro Mani <manisandro@gmail.com> - 0.9.6-7
- Fix pkg-config file

* Wed Mar 13 2019 Sandro Mani <manisandro@gmail.com> - 0.9.6-6
- Backport security fixes: CVE-2019-9199, CVE-2019-9687

* Tue Feb 05 2019 Sandro Mani <manisandro@gmail.com> - 0.9.6-5
- Backport security fix for CVE-2018-20751

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Sandro Mani <manisandro@gmail.com> - 0.9.6-3
- Backport security fixes:
   CVE-2018-5783, CVE-2018-11254, CVE-2018-11255, CVE-2018-11256,
   CVE-2018-12982, CVE-2018-14320, CVE-2018-19532
- Run unit tests

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Sandro Mani <manisandro@gmail.com> - 0.9.6-1
- Update to 0.9.6
- Fixes: CVE-2018-5309, CVE-2018-8001

* Fri Jun 15 2018 Sandro Mani <manisandro@gmail.com> - 0.9.5-9
- Backport security fixes (taken from debian package):
   CVE-2017-7380, CVE-2017-7381, CVE-2017-7382, CVE-2017-7383, CVE-2017-5852,
   CVE-2017-5853, CVE-2017-6844, CVE-2017-5854, CVE-2017-5855, CVE-2017-5886,
   CVE-2018-8000, CVE-2017-6840, CVE-2017-6842, CVE-2017-6843, CVE-2017-6845,
   CVE-2017-6847, CVE-2017-6848, CVE-2017-7378, CVE-2017-7379, CVE-2017-7994,
   CVE-2017-8054, CVE-2017-8378, CVE-2017-8787, CVE-2018-5295, CVE-2018-5308

* Wed May 16 2018 Kevin Fenzi <kevin@scrye.com> - 0.9.5-8
- Rebuild for new libidn

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Sandro Mani <manisandro@gmail.com> - 0.9.5-3
- Drop -std=c++98 from CXXFLAGS

* Fri Feb 03 2017 Sandro Mani <manisandro@gmail.com> - 0.9.5-2
- Add Requires: openssl-devel to -devel

* Thu Feb 02 2017 Sandro Mani <manisandro@gmail.com> - 0.9.5-1
- Update to 0.9.5

* Fri Sep 23 2016 Sandro Mani <manisandro@gmail.com> - 0.9.4-1
- Update to 0.9.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 20 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.9.1-15
- Fix FTBFS on aarch64 (#1111745)

* Tue Jun 10 2014 Dan Horák <dan[at]danny.cz> - 0.9.1-14
- fix FTBFS (#1106651)
- spec cleanup

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 20 2013 Dan Horák <dan[at]danny.cz> - 0.9.1-12
- fix build with Lua 5.2 (#992811)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.9.1-9
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.9.1-8
- rebuild against new libjpeg

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 03 2012 Dan Horák <dan[at]danny.cz> - 0.9.1-6
- disable timestamps in docs (#565683)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for c++ ABI breakage

* Mon Jan 16 2012 Dan Horák <dan[at]danny.cz> - 0.9.1-4
- build fix for unistd.h

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.1-2
- Rebuild for new libpng

* Thu Apr 28 2011 Dan Horák <dan[at]danny.cz> 0.9.1-1
- updated to 0.9.1

* Thu Apr 14 2011 Dan Horák <dan[at]danny.cz> 0.9.0-1
- updated to 0.9.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov  2 2010 Dan Horák <dan[at]danny.cz> 0.8.4-1
- updated to 0.8.4

* Fri Oct 22 2010 Dan Horák <dan[at]danny.cz> 0.8.3-1
- updated to 0.8.3

* Tue Jun  8 2010 Dan Horák <dan[at]danny.cz> 0.8.1-2
- fix building tests

* Mon Jun  7 2010 Dan Horák <dan[at]danny.cz> 0.8.1-1
- updated to 0.8.1

* Thu Apr 29 2010 Dan Horák <dan[at]danny.cz> 0.8.0-1
- updated to 0.8.0

* Tue Feb 16 2010 Dan Horák <dan[at]danny.cz> 0.7.0-4
- set timestamp on generated docs (#565683)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 30 2009 Dan Horák <dan[at]danny.cz> 0.7.0-2
- remove BR: openssl-devel, it could be required in the future (but then
    an exception clause will be added to the licenses)
- add missing doc files

* Sun Mar 29 2009 Dan Horák <dan[at]danny.cz> 0.7.0-1
- initial Fedora package
