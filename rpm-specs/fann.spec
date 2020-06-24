Name:       fann
Summary:    A fast artificial neural network library
Version:    2.2.0
Release:    18%{?dist}
License:    LGPLv2+
URL:        http://leenissen.dk/fann/wp/

Source:     http://downloads.sourceforge.net/fann/fann/2.2.0/FANN-%{version}-Source.tar.gz
Patch0:     fann-2.2.0-pkgconfig.patch
Patch1:     fann-memcorruption.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: cmake

%description
Fast Artificial Neural Network (FANN) Library is written in ANSI C.
The library implements multilayer feedforward ANNs, up to 150 times faster
than other libraries. FANN supports execution in fixed point, for fast 
execution on systems like the iPAQ.

%package devel
Summary: Development libraries for FANN
Requires: %{name} = %{version}-%{release} pkgconfig

%description devel
This package is only needed if you intend to develop and/or compile programs 
based on the FANN library.

%prep
%setup -q -n FANN-%{version}-Source
%patch0 -p1
%patch1 -p1 -b .memcorruption

LIBS=-lm
export LIBS

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} -DPKGCONFIG_INSTALL_DIR=/%{_lib}/pkgconfig ..
popd

%build
make %{?_smp_mflags} -C %{_target_platform}

%install
make DESTDIR=$RPM_BUILD_ROOT -C %{_target_platform} install
find $RPM_BUILD_ROOT -name "*.la" -exec rm {} \;


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING.txt
%doc README.txt
%{_libdir}/libdoublefann.so.2
%{_libdir}/libdoublefann.so.2.2.0
%{_libdir}/libfloatfann.so.2
%{_libdir}/libfloatfann.so.2.2.0
%{_libdir}/libfixedfann.so.2
%{_libdir}/libfixedfann.so.2.2.0
%{_libdir}/libfann.so.2
%{_libdir}/libfann.so.2.2.0

%files devel
%{_libdir}/pkgconfig/fann.pc
%{_libdir}/libdoublefann.so
%{_libdir}/libfann.so
%{_libdir}/libfixedfann.so
%{_libdir}/libfloatfann.so
%{_includedir}/*.h

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 25 2017 Peter Robinson <pbrobinson@fedoraproject.org> 2.2.0-13
- Modernise spec

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 01 2014 Remi Collet <rcollet@redhat.com> - 2.2.0-5
- fix memory corruption in fann_error, #1047627

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Tomas Smetana <tsmetana@redhat.com> - 2.2.0-1
- update to the version 2.2.0 (thanks to Jaroslav Reznik)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 11 2009 Tomas Smetana <tsmetana@redhat.com> 2.0.0-6
- There is no html documentation, don't try to build it

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 12 2008 Tomas Smetana <tsmetana@redhat.com> 2.0.0-4.1
- rebuild (gcc-4.3)

* Mon Aug 20 2007 Tomas Smetana <tsmetana@redhat.com> 2.0.0-4
- License tag update

* Wed Aug 01 2007 Tomas Smetana <tsmetana@redhat.com> 2.0.0-3
- Ensure linking against libm

* Mon Jul 09 2007 Tomas Smetana <tsmetana@redhat.com> 2.0.0-2
- Disable static libraries, fix BuildRoot, move headers to subdirectory

* Thu Jun 21 2007 Tomas Smetana <tsmetana@redhat.com> 2.0.0-1
- Bump release

* Thu Jun 21 2007 Tomas Smetana <tsmetana@redhat.com> 2.0.0-0
- Updated spec file.

* Fri Mar 30 2004 Evan Nemerson <evan@coeus-group.com>
- Build and install HTML documentation.

* Fri Jan 16 2004 Evan Nemerson <evan@coeus-group.com>
- Added activation header.

* Mon Jan 10 2004 Evan Nemerson <evan@coeus-group.com>
- RPM created
