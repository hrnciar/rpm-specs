Name: libresample
Version: 0.1.3
Summary: A real-time library for audio sampling rate conversion
Release: 33%{?dist}
License: LGPLv2+
URL: https://ccrma.stanford.edu/~jos/resample/Free_Resampling_Software.html
Source0: http://ccrma.stanford.edu/~jos/gz/libresample-%{version}.tgz
Source1: libresample.pc
Patch1: libresample_shared-libs.patch
BuildRequires: cmake >= 2.4
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel

%description
A real-time library for audio sampling rate conversion providing
several useful features relative to resample-1.7 on which it is based:

    * It should build "out of the box" on more platforms, including
      Linux, Solaris, and Mac OS X (using the included configure
      script). There is also a Visual C++ project file for building
      under Windows.

    * Input and output signals are in memory (as opposed to sound
      files).

    * Computations are in floating-point (instead of fixed-point).

    * Filter table increased by a factor of 32, yielding more accurate
      results, even without linear interpolation (which also makes it
      faster).

    * Data can be processed in small chunks, enabling time-varying
      resampling ratios (ideal for time-warping applications and
      supporting an ``external clock input'' in software).

    * Easily applied to any number of simultaneous data channels 

%package devel
Summary: Development files for libresample
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libresample.

%prep
%autosetup
mkdir pkgconfig
cp %{SOURCE1} pkgconfig/

%configure

%build
%make_build VERBOSE=1

%install
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_libdir}/pkgconfig/
mkdir -p %{buildroot}%{_includedir}
cp tests/resample-sndfile %{buildroot}%{_bindir}/
cp libresample.so.0 %{buildroot}%{_libdir}/
cp include/libresample.h %{buildroot}%{_includedir}/
cp libresample.so %{buildroot}%{_libdir}/
cp pkgconfig/libresample.pc %{buildroot}%{_libdir}/pkgconfig/

%check
export LD_LIBRARY_PATH=.
make tests

%ldconfig_scriptlets

%files
%doc LICENSE.txt README.txt
%{_bindir}/resample-sndfile
%{_libdir}/libresample.so.0

%files devel
%doc README.txt
%license LICENSE.txt
%{_includedir}/libresample.h
%{_libdir}/libresample.so
%{_libdir}/pkgconfig/libresample.pc

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct  9 2019 Jared K. Smith <jsmith@fedoraproject.org> - 0.1.3-32
- Fix to build from source again

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Jared Smith <jsmith@fedoraproject.org> - 0.1.3-28
- Add missing BuildRequires on gcc and gcc-c++

* Thu Feb 15 2018 Jared Smith <jsmith@fedoraproject.org> - 0.1.3-27
- Use ldconfig_scriptlets macro

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Apr 11 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 0.1.3-14
- Fix pkgconfig --libs and --cflags (#550885).

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 10 2010 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.3-12
- Fix URL (upstream changed URLs), not issuing build at this time.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 21 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.1.3-11
- Fix FTBFS: fixed failing tests in %%check

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 16 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.3-9
- Update patch

* Thu Oct 16 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.3-8
- Add patch

* Wed Oct 15 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.3-7
- Relax CMake requirements

* Thu Sep 11 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.3-6
- Add a patch that switches to cmake for building and build a shared library.

* Mon Feb 11 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.3-5
- Rebuild for GCC 4.3

* Tue Aug 28 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.3-4
- Update license tag.

* Mon Aug 28 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.3-3
- Bump release and rebuild.

* Thu Feb 16 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.3-2
- Expanded %%description.
- Add %%{?dist} to release.

* Sun Jan  8 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.1.3-1
- Initial build.

