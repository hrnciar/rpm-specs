%if 0%{?fedora} >= 33
%global blaslib flexiblas
%global blasvar %{nil}
%else
%global blaslib openblas
%global blasvar o
%endif

Name:           libcint
Version:        4.0.3
Release:        1%{?dist}
Summary:        General Gaussian-type orbitals integrals for quantum chemistry

License:        BSD
URL:            https://github.com/sunqm/libcint
Source0:        https://github.com/sunqm/libcint/archive/v%{version}/libcint-%{version}.tar.gz

# qcint is a drop-in replacement of the same library with architecture dependent optimizations
Conflicts:      qcint

BuildRequires:  gcc-gfortran
BuildRequires:  %{blaslib}-devel
BuildRequires:  cmake 
BuildRequires:  python3-devel 
BuildRequires:  python3-numpy 

# For documentation
BuildRequires:  pandoc
BuildRequires:  tex(latex)

# ppc64 doesn't appear to have floats beyond 64 bits, so ppc64 is
# disabled as per upstream's request
ExcludeArch:    %{power64}

%description    
libcint is an open source library for analytical Gaussian integrals.
It provides C/Fortran API to evaluate one-electron / two-electron
integrals for Cartesian / real-spherical / spinor Gaussian type functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      qcint-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -Wl,--as-needed"
%cmake -DENABLE_EXAMPLE=1 -DWITH_F12=1 -DWITH_COULOMB_ERF=1 -DWITH_RANGE_COULOMB=1 -DENABLE_TEST=1 -DQUICK_TEST=1 -DBLAS_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so -S . -B %{_host}
%make_build -C %{_host}

# Build documentation
cd doc
bash compile.sh

%install
%make_install -C %{_host}

%check
make -C %{_host} test ARGS=-V

%files
%doc README ChangeLog
%license LICENSE
%{_libdir}/libcint.so.*

%files devel
%doc doc/program_ref.pdf
%{_includedir}/cint.h
%{_includedir}/cint_funcs.h
%{_libdir}/libcint.so

%changelog
* Thu Oct 08 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.2-1
- Update to 4.0.3.

* Mon Oct 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.2-1
- Update to 4.0.2.
- Make CMake build work also on released branches.

* Sat Oct 03 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.1-1
- Update to 4.0.1.

* Sun Sep 27 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0.0-1
- Update to 4.0.0.

* Wed Aug 26 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1.

* Thu Aug 13 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.0.20-6
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Wed Aug 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.20-5
- Adapt to new CMake macros.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.20-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.20-2
- Add missing conflicts: qcint-devel to libcint-devel.

* Thu May 14 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.20-1
- Update to 3.0.20, fixing a bug in magnetizabilities.

* Sun Feb 02 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.19-6
- Use OpenBLAS instead of ATLAS.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.19-4
- Include documentation.

* Sat Jan 18 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.19-3
- Use %%make_build and %%make_install, remove %%ldconfig_scriptlets.

* Sat Jan 18 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.19-2
- Fix typo in buildrequirements; python2 instead of python3.

* Tue Jan 14 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.19-1
- Update to 3.0.19.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 09 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.4-2
- Disable build on ppc64.

* Mon Oct 09 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.4-1
- Update to 3.0.4.

* Thu Oct 05 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.3-1
- Update to 3.0.3.

* Wed Oct 04 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2.

* Wed Sep 27 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1.

* Tue Sep 26 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.0-1
- Update to libcint version 3, based on patch sent by Qiming Sun.
- Enabled F12 integrals.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 19 2016 Matt Chan <talcite@gmail.com> - 2.8.7-3
- Disable aarch64 builds because of missing dependency
* Mon Sep 19 2016 Matt Chan <talcite@gmail.com> - 2.8.7
- Disable ppc64(LE) builds because of missing dependency
* Tue Jul 19 2016 Matt Chan <talcite@gmail.com> - 2.8.6
- Initial build
