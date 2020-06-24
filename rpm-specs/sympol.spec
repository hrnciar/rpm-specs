# There is currently no check script because upstream's tests have bitrotted.
# Upstream has been informed of the situation.

Name:           sympol
Version:        0.1.9
Release:        19%{?dist}
Summary:        Symmetric polyhedra tool

License:        GPLv2+
URL:            http://www.math.uni-rostock.de/~rehn/software/sympol.html
Source0:        https://github.com/tremlin/SymPol/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        http://www.math.uni-rostock.de/~rehn/software/%{name}-manual-0.1.pdf
# Adapt to changes in libstdc++ headers
Patch0:         %{name}-cpp.patch

BuildRequires:  bliss-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cddlib-devel
BuildRequires:  eigen3-static
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  lrslib-devel
BuildRequires:  permlib-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
SymPol is a C++ tool to work with symmetric polyhedra.  It helps to
compute restricted automorphisms (parts of the linear symmetry group) of
polyhedra and performs polyhedral description conversion up to a given
or computed symmetry group.

%package libs
Summary:        Symmetric polyhedra library

%description libs
This package contains the SymPol library.

%package devel
Summary:        Headers and libraries for developing SymPol applications
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       eigen3-devel
Requires:       gmp-devel%{?_isa}
Requires:       permlib-devel

%description devel
This package contains the headers and library files needed to develop
SymPol applications.

%prep
%setup -q -n SymPol-%{version}
%patch0
cp -p %{SOURCE1} .

# Do not use the bundled cddlib, lrslib, or permlib
rm -fr external/{cddlib-094f,lrslib-042c,permlib}
sed -e "/(external/d" \
    -e "s|-O3 -g|-I%{_includedir}/cddlib -I%{_includedir}/lrslib -DMA -DGMP -DBLISS_USE_GMP|" \
    -i CMakeLists.txt

# Adapt to lrslib 0.5.0
sed -i.orig '/lrs_mp_close/d' sympol/raycomputationlrs.cpp
touch -r sympol/raycomputationlrs.cpp.orig sympol/raycomputationlrs.cpp
rm -f sympol/raycomputationlrs.cpp.orig

# Adapt to lrslib 0.7.0
sed -i '/TARGET_LIBS/s/lrsgmp/lrs/' sympol/CMakeLists.txt

# Eigen3 3.1.2 adds the need to link explicitly with -lpthread
sed -i 's/{Boost_LIBRARIES}/& pthread/' sympol/CMakeLists.txt
sed -i 's/{GMP_LIBRARIES}/& pthread/' test/CMakeLists.txt

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Fix some header files with broken includes
cd %{buildroot}%{_includedir}/%{name}
for f in *.h; do
  sed -r -e 's|(#include ").*/(.*")|\1\2|' -i.orig $f
  touch -r $f.orig $f
  rm -f $f.orig
done

%ldconfig_scriptlets libs

%files
%doc %{name}-manual-0.1.pdf
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files libs
%doc AUTHORS
%license COPYING
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/

%changelog
* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 0.1.9-19
- Rebuilt for Boost 1.73

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Jerry James <loganjerry@gmail.com> - 0.1.9-15
- Rebuild for lrslib 070

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 0.1.9-14
- Rebuild for cddlib 0.94j

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb  1 2018 Jerry James <loganjerry@gmail.com> - 0.1.9-11
- Rebuild for Boost 1.66

* Thu Sep 28 2017 Jerry James <loganjerry@gmail.com> - 0.1.9-10
- Rebuild for cddlib

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.1.9-7
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 0.1.9-6
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.1.9-4
- Rebuilt for Boost 1.63

* Thu Dec 29 2016 Rich Mattes <richmattes@gmail.com> - 0.1.9-3
- Rebuild for eigen3-3.3.1

* Wed Jul 20 2016 Jerry James <loganjerry@gmail.com> - 0.1.9-2
- Rebuild for permlib 0.2.9

* Fri May 27 2016 Jerry James <loganjerry@gmail.com> - 0.1.9-1
- New upstream release

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 0.1.8-28
- Rebuilt for linker errors in boost (#1331983)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 0.1.8-26
- Rebuilt for Boost 1.60

* Fri Dec  4 2015 Jerry James <loganjerry@gmail.com> - 0.1.8-25
- Rebuild for lrslib 061

* Sat Sep 19 2015 Jerry James <loganjerry@gmail.com> - 0.1.8-24
- Rebuild for lrslib 060

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.1.8-23
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-22
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.1.8-21
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.8-19
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 04 2015 Petr Machata <pmachata@redhat.com> - 0.1.8-18
- Bump for rebuild.

* Mon Feb  2 2015 Jerry James <loganjerry@gmail.com> - 0.1.8-17
- Rebuild for lrslib 051 and eigen3 3.2.4

* Wed Jan 28 2015 Petr Machata <pmachata@redhat.com> - 0.1.8-16
- Rebuild for boost 1.57.0

* Thu Jan 15 2015 Jerry James <loganjerry@gmail.com> - 0.1.8-15
- Rebuild for lrslib 050a and eigen3 3.2.3

* Mon Nov 10 2014 Jerry James <loganjerry@gmail.com> - 0.1.8-14
- Rebuild for lrslib 050

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug  8 2014 Jerry James <loganjerry@gmail.com> - 0.1.8-12
- Rebuild for eigen3-3.2.2
- Fix license handling

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.1.8-10
- Rebuild for boost 1.55.0

* Mon Mar 10 2014 Jerry James <loganjerry@gmail.com> - 0.1.8-9
- Rebuild for eigen3-3.2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.1.8-7
- Rebuild for boost 1.54.0

* Sun Jul 21 2013 Rich Mattes <richmattes@gmail.com> - 0.1.8-6
- Rebuild for eigen3-3.1.3

* Wed Mar  6 2013 Jerry James <loganjerry@gmail.com> - 0.1.8-5
- Rebuild for eigen3-3.1.2

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.1.8-4
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.1.8-3
- Rebuild for Boost-1.53.0

* Wed Dec  5 2012 Jerry James <loganjerry@gmail.com> - 0.1.8-2
- Add -DBLISS_USE_GMP to CFLAGS to avoid segfaults

* Thu Sep 27 2012 Jerry James <loganjerry@gmail.com> - 0.1.8-1
- New upstream release

* Wed Sep 26 2012 Jerry James <loganjerry@gmail.com> - 0.1.7-3
- Rebuild for permlib 0.2.7

* Mon Aug 20 2012 Jerry James <loganjerry@gmail.com> - 0.1.7-2
- Move COPYING to the -libs subpackage

* Mon Apr 30 2012 Jerry James <loganjerry@gmail.com> - 0.1.7-1
- Initial RPM
