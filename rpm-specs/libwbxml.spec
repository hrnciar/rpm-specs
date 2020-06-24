Name:           libwbxml
Version:        0.11.7
Release:        1%{?dist}
Summary:        Library and tools to parse, encode and handle WBXML documents
## Used and installed:
# NEWS:                             ???
# GNU-LGPL:                         LGPLv2+
# COPYING:                          LGPLv2+
# Other files:                      LGPLv2+
## Not installed:
# cmake/modules/FindECal1.2.cmake:  BSD
# cmake/modules/FindIconv.cmake:    GPLv3+
## Not used:
# win32/leaktrack/leaktrack.h:      GPLv2+
# win32/leaktrack/COPYING.txt:      BSD with advertising
# win32/expat/README.txt:           MIT
License:        LGPLv2+
URL:            https://github.com/%{name}/%{name}
Source:         %{url}/archive/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 2.4
BuildRequires:  coreutils
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(check)
# Tests:
BuildRequires:  perl-interpreter
Obsoletes:      wbxml2 <= 0.9.3

%description
The WBXML Library (libwbxml) contains a library and its associated tools to
parse, encode and handle WBXML documents. The WBXML format is a binary
representation of XML, defined by the Wap Forum, and used to reduce
bandwidth in mobile communications.

%package devel
Summary:       Development files of %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      pkgconfig
Provides:      wbxml2-devel = %{version}-%{release}
Obsoletes:     wbxml2-devel <= 0.9.3

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
# Upstream does not support in-source-directory building
mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DBUILD_STATIC_LIBS:BOOL=OFF \
    -DENABLE_INSTALL_DOC:BOOL=OFF \
    -DENABLE_UNIT_TEST:BOOL=ON \
    -DWBXML_ENCODER_USE_STRTBL:BOOL=ON \
    -DWBXML_INSTALL_FULL_HEADERS:BOOL=OFF \
    -DWBXML_LIB_VERBOSE:BOOL=OFF \
    -DWBXML_SUPPORT_AIRSYNC:BOOL=ON \
    -DWBXML_SUPPORT_CO:BOOL=ON \
    -DWBXML_SUPPORT_CONML=ON \
    -DWBXML_SUPPORT_DRMREL:BOOL=ON \
    -DWBXML_SUPPORT_EMN:BOOL=ON \
    -DWBXML_SUPPORT_OTA_SETTINGS:BOOL=ON \
    -DWBXML_SUPPORT_PROV:BOOL=ON \
    -DWBXML_SUPPORT_SI:BOOL=ON \
    -DWBXML_SUPPORT_SL:BOOL=ON \
    -DWBXML_SUPPORT_SYNCML:BOOL=ON \
    -DWBXML_SUPPORT_WML:BOOL=ON \
    -DWBXML_SUPPORT_WTA:BOOL=ON \
    -DWBXML_SUPPORT_WV:BOOL=ON \
    ..
popd
%{make_build} -C %{_target_platform}

%install
make %{?_smp_mflags} -C %{_target_platform} install/fast DESTDIR=$RPM_BUILD_ROOT

%check
cd %{_target_platform}
ctest %{?_smp_mflags}

%files
%license COPYING GNU-LGPL
%doc BUGS ChangeLog README References THANKS TODO
%{_bindir}/*
%{_libdir}/libwbxml2.so.*

%files devel
# In order not to run-require cmake, own the directory
%{_datadir}/cmake
%{_includedir}/*
%{_libdir}/libwbxml2.so
%{_libdir}/pkgconfig/libwbxml2.pc

%changelog
* Thu Apr 16 2020 Petr Pisar <ppisar@redhat.com> - 0.11.7-1
- 0.11.7 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Petr Pisar <ppisar@redhat.com> - 0.11.6-3
- Modernize a spec file

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 16 2017 Petr Pisar <ppisar@redhat.com> - 0.11.6-1
- 0.11.6 bump

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Petr Pisar <ppisar@redhat.com> - 0.11.5-1
- 0.11.5 bump

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Petr Pisar <ppisar@redhat.com> - 0.11.3-3
- Require gcc instead of glibc-headers (bug #1230475)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 08 2015 Petr Pisar <ppisar@redhat.com> - 0.11.3-1
- 0.11.3 bump

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 03 2012 Petr Pisar <ppisar@redhat.com> - 0.11.2-1
- 0.11.2 bump

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 04 2012 Petr Pisar <ppisar@redhat.com> - 0.11.1-1
- 0.11.1 bump
- The license is LGPLv2+ only for all the code

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 23 2011 Petr Pisar <ppisar@redhat.com> - 0.11.0-1
- 0.11.0 bump: This version breaks API
- Add GPLv2+ to license tag because of xml2wbxml_tool
- Remove explicit defattr spec code

* Thu Feb 10 2011 Petr Pisar <ppisar@redhat.com> - 0.10.9-3
- Correct devel dependency typo

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 08 2011 Petr Pisar <ppisar@redhat.com> - 0.10.9-1
- 0.10.9 bump
- Remove BuildRoot stuff
- Make devel subpackage ISA specific

* Tue Aug 10 2010 Petr Pisar <ppisar@redhat.com> - 0.10.8-1
- 0.10.8 import
- based on and obsoletes wbxml2-0.9.2-16
