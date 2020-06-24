Name:           CTL
Version:        1.5.2
Release:        9%{?dist}
Summary:        The Color Transformation Language

License:        AMPAS BSD
URL:            http://github.com/ampas/CTL
Source0:        %{url}/archive/ctl-%{version}/%{name}-%{version}.tar.gz
Patch0:         ctl-1.5.2-dpx.patch
Patch1:         ctl-1.5.2-ilmctl.patch
# https://github.com/ampas/CTL/issues/71
Patch2:         ctl-1.5.2-ilm_230.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake

# http://bugzilla.redhat.com/357461
# The CTL license is ok, Free but GPL Incompatible.
BuildRequires:  aces_container-devel
BuildRequires:  ilmbase-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  libtiff-devel

# Provide this package as case-insensitive
Provides: ctl = %{version}-%{release}
# Obsoletes old libraries - rhbz#1644764
Provides:       OpenEXR_CTL-libs = %{version}-%{release}
Obsoletes:      OpenEXR_CTL-libs < 1.5.2-1


%description
The Color Transformation Language, or CTL, is a programming language
for digital color management.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ilmbase-devel%{?_isa}
Requires:       OpenEXR-devel%{?_isa}
Provides:       OpenEXR_CTL-devel = %{version}-%{release}
Obsoletes:      OpenEXR_CTL-devel < 1.5.2-1

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package docs
Summary:        Documentation for %{name}

%description docs
This package contains documentation files for %{name}.

%package -n     OpenEXR_CTL
Summary:        A simplified OpenEXR interface to CTL
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n  OpenEXR_CTL
exrdpx is an initial version of a CTL-driven file converter
that translates DPX files into OpenEXR files and vice versa.
The conversion between the DPX and OpenEXR color spaces is
handled by CTL transforms.

exr_ctl_exr is an initial version of a program that can bake
the effect of a series of CTL transforms into the pixels of
an OpenEXR file.


%prep
%autosetup -p1 -n CTL-ctl-%{version}


%build
mkdir -p build
pushd build
%cmake \
 -DINSTALL_LIB_DIR:PATH=%{_lib} \
 -DINSTALL_CMAKE_DIR:PATH=%{_lib}/cmake/%{name} \
  ..

%make_build


%install
cd build
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Move libraries in the correct place
%if "%{_lib}" == "lib64"
mv  %{buildroot}%{_prefix}/lib/* \
  %{buildroot}%{_prefix}/%{_lib}
rmdir %{buildroot}%{_prefix}/lib
%endif

# Remove installed docs
rm -rf %{buildroot}%{_docdir}
rm -rf %{buildroot}%{_prefix}/doc


%ldconfig_scriptlets


%files
%doc AUTHORS CHANGELOG README.md
%license LICENSE
%{_libdir}/*.so.*
%{_libdir}/CTL

%files devel
%{_includedir}/CTL/
%{_includedir}/OpenEXR/ImfCtlApplyTransforms.h
%{_libdir}/*.so
%{_libdir}/cmake/CTL/*.cmake
%{_libdir}/pkgconfig/CTL.pc
%{_libdir}/pkgconfig/OpenEXR_CTL.pc

%files docs
%doc doc/CtlManual.pdf doc/CtlManual.doc

%files -n OpenEXR_CTL
%{_bindir}/ctlrender
%{_bindir}/exr_ctl_exr
%{_bindir}/exrdpx


%changelog
* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 1.5.2-9
- Fix string quoting for rpm >= 4.16

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Richard Shaw <hobbes1069@gmail.com> - 1.5.2-6
- Rebuild for OpenEXR 2.3.0.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 05 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.5.2-4
- Obsoletes old libraries - rhbz#1644764

* Mon Oct 01 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.5.2-3
- Fix soname

* Thu Jul 19 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.5.2-2
- Add Obsoletes/Provides for OpenEXR_CTL

* Tue Jul 17 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.5.2-1
- Update to 1.5.2
- Merge OpenEXR_CTL into CTL

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4.1-23
- Rebuilt for GCC 5 C++11 ABI change

* Tue Nov 25 2014 Rex Dieter <rdieter@fedoraproject.org> 1.4.1-22
- rebuild (ilmbase)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> 1.4.1-19
- rebuild (ilmbase)

* Sun Sep 08 2013 Rex Dieter <rdieter@fedoraproject.org> 1.4.1-18
- rebuild (ilmbase)

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-14
- Rebuilt for c++ ABI breakage

* Thu Jan 19 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.4.1-13
- Add ctl-1.4.1-gcc47.patch (Fix mass rebuild FTBFS).

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb  3 2009 kwizart < kwizart at gmail.com > - 1.4.1-8
- Rebuild for pkgconfig(CTL)

* Fri Oct  3 2008 kwizart < kwizart at gmail.com > - 1.4.1-7
- Rebuild for F-10

* Sat Feb  9 2008 kwizart < kwizart at gmail.com > - 1.4.1-6
- Rebuild for gcc43

* Wed Jan  9 2008 kwizart < kwizart at gmail.com > - 1.4.1-5
- clean unused-direct-shlib-dependencies

* Tue Jan  8 2008 kwizart < kwizart at gmail.com > - 1.4.1-4
- Fix gcc43

* Fri Nov  9 2007 kwizart < kwizart at gmail.com > - 1.4.1-3
- Change package name from ctl to CTL

* Wed Nov  7 2007 kwizart < kwizart at gmail.com > - 1.4.1-2
- Improve license URL
- Use IlmBase.pc for pkg-config
- Fix perms in debuginfo

* Mon Oct 29 2007 kwizart < kwizart at gmail.com > - 1.4.1-1
- Initial package for Fedora

