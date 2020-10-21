%bcond_with static_libs # don't build static libraries

Summary:        Library providing a collection of special mathematical functions
Name:           openspecfun
Version:        0.5.3
Release:        12%{?dist}
License:        MIT and Public Domain
Source0:        https://github.com/JuliaLang/openspecfun/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL:            https://github.com/JuliaLang/openspecfun
BuildRequires:  gcc-gfortran

%description
Currently provides AMOS and Faddeeva. AMOS (from Netlib) is a
portable package for Bessel Functions of a Complex Argument and
Nonnegative Order; it contains subroutines for computing Bessel
functions and Airy functions. Faddeeva allows computing the
various error functions of arbitrary complex arguments (Faddeeva
function, error function, complementary error function, scaled
complementary error function, imaginary error function, and Dawson function);
given these, one can also easily compute Voigt functions, Fresnel integrals,
and similar related functions as well.

%package devel
Summary:    Library providing a collection of special mathematical functions
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Contains header files for developing applications that use the %{name}
library.

%package static
Summary:    Library providing a collection of special mathematical functions
Requires:   %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static %{name} library.

%prep
%setup -q %{name}-%{version}

%build
make %{?_smp_mflags} \
      FFLAGS="%{optflags}" \
      CFLAGS="%{optflags}" \
      USE_OPENLIBM=0 \
      includedir=%{_includedir}

%install
make install prefix=%{_prefix} \
             libdir=%{_libdir} \
             includedir=%{_includedir} \
             DESTDIR=%{buildroot}

%if ! %{with static_libs}
rm %{buildroot}/%{_libdir}/libopenspecfun.a
%endif

%ldconfig_scriptlets

%files
%doc LICENSE.md README.md
%{_libdir}/libopenspecfun.so.1*

%files devel
%{_libdir}/libopenspecfun.so
%{_includedir}/Faddeeva.h

%if %{with static_libs}
%files static
%{_libdir}/libopenspecfun.a
%endif

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 4 2018 Milan Bouchet-Valat <nalimilan@club.fr> - 0.5.3-6
- Rebuilt for libgfortran.so.4.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Milan Bouchet-Valat <nalimilan@club.fr> - 0.5.3-2
- Rebuild for gfortran 7.

* Wed Jul 27 2016 Milan Bouchet-Valat <nalimilan@club.fr> - 0.5.3-1
- New upstream release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 27 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.4-1
- New upstream release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 1 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3-1
- New upstream release.
- Use Group System Environment/Libraries for base package.

* Fri Feb 14 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.2-2
- Don't build static libraries package by default.

* Sat Feb 8 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.2-1
- Initial version.
