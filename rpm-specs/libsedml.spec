%global __cmake_in_source_build 1

# Documents generation and Octave binding look not available yet
%global with_python  1
%global with_ruby    1

%ifarch s390x %{arm} aarch64 %{power64}
%global with_java    0
%else
%global with_java    0
%endif

%global with_octave  0
%global with_perl    1
%global with_r       1

%if 0%{?fedora} && 0%{?fedora} >= 30
%ifarch %{ix86} x86_64 sparc sparcv9 ia64 %{arm} aarch64 alpha s390x ppc
%global with_mono    1
%else
%global with_mono    0

Obsoletes: libsedml-sharp < 1:0.4.4-1
%endif
%endif
#

%global with_doc     0
%global with_check   1

%global octpkg SEDML
%if 0%{?with_octave}
# Exclude .oct files from provides
%global __provides_exclude_from ^%{octpkglibdir}/.*\\.oct$
%endif

%global _docdir_fmt %{name}

Name:           libsedml
Summary:        Library that fully supports SED-ML for SBML
Version:        0.4.4
Release:        12%{?dist}
Epoch:          1
URL:            https://github.com/fbergmann/libSEDML
Source0:        https://github.com/fbergmann/libSEDML/archive/v%{version}/libSEDML-%{version}.tar.gz
License:        BSD

BuildRequires: cmake
BuildRequires: zlib-devel
BuildRequires: swig
BuildRequires: libsbml-devel
BuildRequires: libnuml-devel
BuildRequires: libxml2-devel
BuildRequires: bzip2-devel
BuildRequires: xerces-c-devel
BuildRequires: minizip-devel

%if 0%{?with_check}
BuildRequires: check-devel
%endif

Obsoletes:     python2-libsedml < 1:0.4.4-2
Obsoletes:     java-SEDML < 1:0.4.4-12

##This patch sets libraries' installation paths
Patch0: %{name}-fix_install_libpaths.patch

# See https://github.com/fbergmann/libSEDML/issues/55
Patch1: %{name}-fix_string_format.patch

%description
C++ library that fully supports SED-ML 
(Simulation Experiment Description Markup Language) for SBML as well as 
CellML models for creation of the description just as for
the execution of Simulation Experiments. 
This project makes use of libSBML XML layer as well as code generation 
as starting point to produce a library for reading and writing of SED-ML models.
This package provides header and library files of libsedml.

%package devel
Summary: Library that fully supports SED-ML for SBML
Requires: %{name}%{?_isa} = 1:%{version}-%{release}
%description devel
This package provides header and library files of libsedml.

%package static
Summary: Library that fully supports SED-ML for SBML
Provides: %{name}-static = 1:%{version}-%{release}
%description static
This package provides static library of libsedml.

%if 0%{?with_python}
%package -n python3-libsedml
Summary: Python3 library that fully supports SED-ML for SBML
BuildRequires: python3-devel
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-libsedml
The %{octpkg} python package contains the libraries to 
develop applications with libSEDML Python3 bindings.
%endif

%if 0%{?with_java}
%package -n java-%{octpkg}
Summary: Java library that fully supports SED-ML for SBML
BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  java-devel
Requires:       java-headless
Requires:       jpackage-utils
%description -n java-%{octpkg}
The %{octpkg} java package contains the libraries to 
develop applications with libSEDML Java bindings.
%endif

%if 0%{?with_octave}
%package -n octave-%{octpkg}
Summary: Octave library that fully supports SED-ML for SBML
BuildRequires:  octave-devel
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
%description -n octave-%{octpkg}
The %{octpkg} octave package contains the libraries to 
develop applications with libSEDML Octave bindings.
%endif

%if 0%{?with_perl}
%package -n perl-%{octpkg}
Summary: Perl library that fully supports SED-ML for SBML
BuildRequires: perl-interpreter
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
Requires:      perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
%description -n perl-%{octpkg}
The %{octpkg} perl package contains the libraries to 
develop applications with libSEDML Perl bindings.
%endif

%if 0%{?with_ruby}
%package -n ruby-%{octpkg}
Summary: Ruby library that fully supports SED-ML for SBML
BuildRequires: ruby-devel
Requires: ruby(release)
Provides: ruby(SBML) = %{version}
%description -n ruby-%{octpkg}
The %{octpkg} ruby package contains the libraries to 
develop applications with libSEDML Ruby bindings.
%endif

%if 0%{?with_r}
%package -n R-%{octpkg}
Summary: R library that fully supports SED-ML for SBML
BuildRequires: R-devel, R-core-devel, tex(latex)
Requires:      R-core
%description -n R-%{octpkg}
The %{octpkg} R package contains the libraries to 
develop applications with libSEDML R bindings.
%endif

%if 0%{?with_mono}
%package sharp
Summary: Mono library that fully supports SED-ML for SBML
BuildRequires: xerces-c-devel, libxml2-devel, expat-devel
BuildRequires: mono-core
Requires: mono-core
%description sharp
The %{octpkg} csharp package contains the libraries to 
develop applications with libSEDML C# bindings.
%endif

%if 0%{?with_doc}
%package -n libsedml-javadoc
Summary: Library that fully supports SED-ML for SBML
BuildRequires: doxygen
BuildArch: noarch
%description -n libsedml-javadoc
The %{octpkg} doc package contains the documentation
of libSEDML libraries.
%endif

%prep
%autosetup -n libSEDML-%{version} -p0

# Fix where CMake config files are installed
sed -e 's| lib/cmake | %{_lib}/cmake |g' -i CMakeLists.txt
sed -e 's| /usr/lib/cmake | %{_libdir}/cmake |g' -i CMakeModules/FindLIBNUML.cmake
sed -e 's| /usr/lib/cmake | %{_libdir}/cmake |g' -i CMakeModules/FindLIBSBML.cmake

%build
######################################################################################################
## ----> Move to build directory ##

mkdir build && pushd build
export LDFLAGS="$RPM_LD_FLAGS -lpthread"
%cmake -Wno-dev \
%if 0%{?with_python}
 -DWITH_PYTHON:BOOL=ON \
 -DWITH_SWIG:BOOL=ON \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DPYTHON_INCLUDE_DIR:PATH=%{_includedir}/python%{python3_version}%(python3-config --abiflags) \
 -DPYTHON_LIBRARY:FILEPATH=%{_libdir}/libpython%{python3_version}%(python3-config --abiflags).so \
%endif
%if 0%{?with_java}
 -DWITH_JAVA:BOOL=ON \
 -DWITH_SWIG:BOOL=ON \
%endif
%if 0%{?with_octave}
 -DWITH_OCTAVE:BOOL=ON \
%endif
%if 0%{?with_perl}
 -DWITH_PERL:BOOL=ON \
%endif
%if 0%{?with_ruby}
 -DWITH_RUBY:BOOL=ON \
%endif
%if 0%{?with_r}
 -DWITH_R:BOOL=ON \
 -DR_INCLUDE_DIRS:PATH=%{_includedir}/R \
%endif
%if 0%{?with_mono}
 -DWITH_CSHARP:BOOL=ON \
 -DWITH_SWIG:BOOL=ON \
%endif
 -DCSHARP_COMPILER:FILEPATH=%{_bindir}/mcs \
%if 0%{?with_doc}
 -DWITH_DOXYGEN:BOOL=ON \
%endif
%if 0%{?with_check}
 -DWITH_CHECK:BOOL=ON \
 -DWITH_EXAMPLES:BOOL=ON \
%endif
 -DLIBSBML_LIBRARY:FILEPATH=%{_libdir}/libsbml.so -DLIBSBML_INCLUDE_DIR:PATH=%{_includedir} \
 -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DLIBSEDML_SHARED_VERSION:BOOL=ON \
 -DEXTRA_LIBS:STRING="numl;sbml;xml2;bz2;z;m;dl" -DLIBSBML_STATIC:BOOL=OFF \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="`pkg-config --cflags libxml-2.0`" \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCPACK_BINARY_TZ:BOOL=OFF -DCPACK_BINARY_TGZ:BOOL=OFF \
 -DCPACK_SOURCE_TBZ2:BOOL=OFF -DCPACK_SOURCE_TGZ:BOOL=OFF \
 -DCPACK_SOURCE_TZ:BOOL=OFF -DWITH_ZLIB:BOOL=ON -DWITH_CPP_NAMESPACE:BOOL=OFF \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES ..

##'Parallel make' breaks Java library's building
## And mono build seems no good on s390x with parallel build
%if 0%{?with_java} || 0%{?with_mono}
make -j1
%else
%make_build
%endif

####################################################################################################

%install
%make_install -C build

mkdir -p $RPM_BUILD_ROOT%{_datadir}/libsedml

##Only for R library
%if 0%{?with_r}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library build/bindings/r/libSEDML_%{version}_R_*.tar.gz
test -d %{octpkg}/src && (cd %{octpkg}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/%{octpkg}/R.css

# Make symlink instead hard-link
ln -sf %{_libdir}/libSEDML.so $RPM_BUILD_ROOT%{_libdir}/R/library/libSEDML/libs/libSEDML.so
%endif
##

%if 0%{?with_octave}
mkdir -p $RPM_BUILD_ROOT%{octpkgdir}/packinfo
install -pm 644 LICENSE.txt *.md $RPM_BUILD_ROOT%{octpkgdir}/packinfo
%endif

## Remove libtool archives
find $RPM_BUILD_ROOT -name '*.la' -delete

%ldconfig_scriptlets

%if 0%{?with_r}
%ldconfig_scriptlets -n R-%{octpkg}
%endif

%if 0%{?with_octave}
%post -n octave-%{octpkg}
%octave_cmd pkg rebuild

%postun -n octave-%{octpkg}
%octave_cmd pkg rebuild

%preun -n octave-%{octpkg}
%octave_pkg_preun
%endif

%if 0%{?with_check}
%check
pushd build
ctest -V --force-new-ctest-process --stop-time 2000
%endif

%files
%doc *.md
%license LICENSE.txt
%{_libdir}/libsedml.so.*
##This directory provides just some txt documentation files
%exclude %{_datadir}/libsedml

%files devel
%{_libdir}/libsedml.so
%{_libdir}/cmake/sedml-config*.cmake
%{_includedir}/sedml/

%files static
%doc *.md
%license LICENSE.txt
%{_libdir}/%{name}-static.a
%{_libdir}/cmake/sedml-static-config*.cmake

%if 0%{?with_python}
%files -n python3-libsedml
%doc *.md
%license LICENSE.txt
%{python3_sitearch}/libsedml/
%{python3_sitearch}/*.pth
%endif

%if 0%{?with_java}
%files -n java-%{octpkg}
%{_javadir}/libsedmlj.jar
%{_libdir}/libsedml/
%endif

%if 0%{?with_octave}
%files -n octave-%{octpkg}
%{octpkgdir}/packinfo
%{octpkglibdir}/
%endif

%if 0%{?with_perl}
%files -n perl-%{octpkg}
%doc *.md
%license LICENSE.txt
%{perl_vendorarch}/LibSEDML.*
%exclude %dir %{perl_vendorarch}/auto/
%{perl_vendorarch}/auto/libSEDML/
%endif

%if 0%{?with_ruby}
%files -n ruby-%{octpkg}
%doc *.md
%license LICENSE.txt
%{ruby_vendorarchdir}/*.so
%endif

%if 0%{?with_r}
%files -n R-%{octpkg}
%doc *.md
%license LICENSE.txt
%{_libdir}/R/library/libSEDML/
%{_libdir}/libSEDML.so
%endif

%if 0%{?with_mono}
%files sharp
%doc *.md
%license LICENSE.txt
##DLL library cannot be registered because not signed
##https://github.com/fbergmann/libSEDML/issues/10
#%%{_monogacdir}/libsedmlcsP
%{_monodir}/libsedmlcsP/
%endif

%if 0%{?with_doc}
%files -n libsedml-javadoc
%doc *.md
%license LICENSE.txt
%doc 00README*
%doc index.html src formatted
%endif

%changelog
* Tue Aug 04 2020 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
- Enable cmake_in_source_build
- Disable Java binding

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.4.4-11
- Perl 5.32 rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:0.4.4-10
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.4.4-8
- F-32: rebuild against ruby27

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1:0.4.4-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:0.4.4-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.4.4-4
- Perl 5.30 rebuild

* Wed May 22 2019 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.4-3
- Use Python3 abiflags

* Sun May 05 2019 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.4-2
- Rebuild for libsbml-5.18.0
- Obsolete python2-libsedml

* Fri Mar 22 2019 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.4-1
- Release 0.4.4
- Obsolete libsedml-sharp on fedora 30+/pp64* (rhbz#1588734,#1686738)
- Disable -Werror=format-security for ruby- builds (upstream bug #55)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.4.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.4.3-19
- F-30: rebuild against ruby26
- Disable parallel build for mono bindings (build fails randomly on s390x)

* Mon Sep 24 2018 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.3-18
- Bundle minizip on fedora 30+ (rhbz#1632191) (upstream bug #466)

* Tue Sep 04 2018 Patrik Novotný <panovotn@redhat.com> - 1:0.4.3-17
- change requires to minizip-compat(-devel), rhbz#1609830, rhbz#1615381

* Sun Sep 02 2018 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.3-16
- Deprecate python2 on fedora 30+

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 1:0.4.3-14
- Perl 5.28 rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.4.3-13
- Perl 5.28 rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:0.4.3-12
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.3-11
- Rebuild for libsbml-5.17.0

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 1:0.4.3-10
- add minizip-devel as explicit BR, probably a broken .pc file in something else though

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 1:0.4.3-9
- rebuild for R 3.5.0

* Thu Feb 15 2018 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.3-8
- Rebuild for libsbml-5.16.0
- Use %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.4.3-6
- F-28: rebuild for ruby25

* Sun Dec 10 2017 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.3-5
- Rebuild for libsbml-5.16.0

* Wed Oct 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.3-4
- Split off the static library

* Wed Oct 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.3-3
- Fix dependency's Epoch

* Wed Oct 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.3-2
- Fix dependencies

* Sun Oct 01 2017 Antonio Trande <sagitter@fedoraproject.org> - 1:0.4.3-1
- Update to 0.4.3
- Set new Epoch
- Add new dependency (libnuml)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.1-21
- Perl 5.26 rebuild

* Fri Apr 14 2017 Antonio Trande <sagitter@fedoraproject.org> - 0.3.1-20
- Rebuild for libsbml-5.15.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.1-18
- F-26: rebuild for ruby24

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-17
- Rebuild for Python 3.6

* Tue Aug 16 2016 Antonio Trande <sagitter@fedoraproject.org> - 0.3.1-16
- Rebuild for Python 3.5.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-15
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.1-14
- Perl 5.24 rebuild

* Tue Apr 19 2016 Antonio Trande <sagitter@fedoraproject.org> - 0.3.1-13
- Rebuild for libSBML 5.13.0

* Sat Apr 09 2016 Antonio Trande <sagitter@fedoraproject.org> - 0.3.1-12
- Fixed Python2 sub-package
- Documentation/License files moved to octpkgdir/packinfo
 -Added post/postun/preun scriptlets for Octave sub-package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Vít Ondruch <vondruch@redhat.com> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Sat Dec 12 2015 Antonio Trande <sagitter@fedoraproject.org> - 0.3.1-9
- Rebuilt with GCC-5.3
- Added python-provides

* Sat Nov 14 2015 Antonio Trande <sagitter@fedoraproject.org> - 0.3.1-8
- Rebuilt for libsbml-5.12.0 and Python3.5

* Wed Nov 11 2015 Antonio Trande <sagitter@fedoraproject.org> - 0.3.1-7
- Set manually CC/CXX variable

* Tue Nov 10 2015 Antonio Trande <sagitter@fedoraproject.org> - 0.3.1-6
- Rebuilt again

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Nov 01 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.1-4
- Built with clang++ on aarch64

* Sun Nov 01 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.1-3
- Hardened builds on <F23

* Sat Sep 19 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.1-2
- Disabled C++ namespaces (Bug2188 on copasi bug tracker)

* Fri Sep 18 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.1-1
- Update to 0.3.1
- Enabled tests

* Sun Jul 26 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-13.20150422git235bb5
- Rebuild after libsbml update

* Fri Jun 19 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-12.20150422git235bb5
- Debug undefined references
- Built with clang on F23 64bit

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-11.20150422git235bb5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-10.20150422git235bb5
- Fixed octpkg macro

* Thu Jun 11 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-9.20150422git235bb5
- Added missing linkage to libsbml
- Fixed Python variables

* Mon Jun 08 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-8.20150422git235bb5
- Python2 package is named python-libsedml
- Forced same documentation directory for all sub-packages
- Make symlink between R libraries

* Fri Jun 05 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-7.20150422git235bb5
- Description improved
- Sub-packages main name changed to libsedml for Python, Java
- Packaged Python3 bindings

* Fri Jun 05 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-6.20150422git235bb5
- Set CSHARP compiler on F23

* Fri May 29 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-5.20150422git235bb5
- Update to commit 235bb5

* Mon Feb 02 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-4.20141230gitb455cd
- Set installation directory of the java library

* Fri Jan 09 2015 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-3.20141230gitb455cd
- Package name modified

* Wed Dec 31 2014 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-2.20141230gitb455cd
- Excluded packaging of static file

* Tue Dec 30 2014 Antonio Trande <sagitter@fedoraproject.org> 0.3.0-1.20141230gitb455cd
- Update to the commit fb91ad (post-release 0.3.0)

* Sun Dec 28 2014 Antonio Trande <sagitter@fedoraproject.org> - 5.11.0-1
- First package

