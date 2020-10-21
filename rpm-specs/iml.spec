%if 0%{?fedora} >= 33
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

Name:           iml
Version:        1.0.5
Release:        15%{?dist}
Summary:        Finds solutions to systems of linear equations over integers
License:        BSD
URL:            https://cs.uwaterloo.ca/~astorjoh/iml.html
Source0:        https://cs.uwaterloo.ca/~astorjoh/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  %{blaslib}-devel


%description
IML provides efficient routines to compute exact solutions to dense
systems of linear equations over the integers.  The following
functionality is provided:
- Nonsingular rational system solving.
- Compute the right nullspace of an integer matrix.
- Certified linear system solving.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}, %{blaslib}-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        static
Summary:        Static library for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
The %{name}-static package contains a static library for %{name}.


%prep
%setup -q

%build
%configure --enable-shared --with-cblas="-l%{blaslib}" \
  --with-cblas-include=%{_includedir}/%{blaslib}

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool

%make_build


%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -fr $RPM_BUILD_ROOT%{_datadir}/%{name}


%check
export LD_LIBRARY_PATH=$PWD/src/.libs
make check


%ldconfig_scriptlets


%files
%doc AUTHORS README
%{_libdir}/lib%{name}.so.*


%files devel
%doc doc/liblink doc/libroutines examples
%{_includedir}/*
%{_libdir}/lib%{name}.so


%files static
%{_libdir}/lib%{name}.a


%changelog
* Thu Aug 13 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.0.5-15
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Tom Stellard <tstellar@redhat.com> - 1.0.5-13
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct  2 2018 Jerry James <loganjerry@gmail.com> - 1.0.5-9
- Try again to build with openblas instead of atlas (bz 1618946)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 28 2017 Jerry James <loganjerry@gmail.com> - 1.0.5-6
- Revert to atlas; openblas caused problems on s390x

* Wed Sep 27 2017 Jerry James <loganjerry@gmail.com> - 1.0.5-5
- Build with openblas instead of atlas

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jerry James <loganjerry@gmail.com> - 1.0.5-1
- New upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug  4 2014 Jerry James <loganjerry@gmail.com> - 1.0.4-1
- New upstream release
- All patches and typo fixes have been applied upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct  3 2013 Jerry James <loganjerry@gmail.com> - 1.0.3-8
- Update project and source URLs

* Sat Sep 21 2013 Jerry James <loganjerry@gmail.com> - 1.0.3-7
- Rebuild for atlas 3.10.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Jerry James <loganjerry@gmail.com> - 1.0.3-5
- Support building on aarch64 (bz 925584)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 1.0.3-2
- Rebuild for GCC 4.7

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.0.3-1.1
- rebuild with new gmp

* Tue Apr 26 2011 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- New upstream release
- Fix URL
- Update description from the web site
- Drop BuildRoot tag, clean script, and clean at start of install script
- Move static library into a -static subpackage
- Fix code typo in iml 1.0.3

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Conrad Meyer <konrad@tylerc.org> - 1.0.2-6
- Fix FTBFS errors.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 27 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.2-4
- Oops, don't depend on the main package which no longer exists in -devel.

* Fri Oct 17 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.2-2
- Only generate one binary package.
- Add %%check.

* Sun Oct 12 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.2-1
- Initial package.
