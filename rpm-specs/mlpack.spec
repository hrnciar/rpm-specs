Name:           mlpack
Version:        3.4.1
Release:        1%{?dist}
Summary:        Scalable, fast C++ machine learning library

License:        BSD
URL:            http://www.mlpack.org
Source0:        http://www.mlpack.org/files/%{name}-%{version}.tar.gz
Source1:        http://www.mlpack.org/files/stb_image.h
Source2:        http://www.mlpack.org/files/stb_image_write.h

# By default the mlpack Doxyfile excludes all files in the directory pattern
# */build/*.  Well, on Koji, that's everything.  So we need to not exclude
# that.
Patch0:		no_exclude_build.patch

# Fix OpenMP build.
#Patch1:         omp.patch

# Make sure CXXFLAGS get set for Python binding builds.
#Patch1:         python_cxxflags.patch

BuildRequires:  gcc-c++
# Use cmake28 package on RHEL.
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  cmake28 >= 2.8.5
%else
BuildRequires:  cmake >= 2.8.5
%endif

BuildRequires:  armadillo-devel >= 8.400.0
BuildRequires:  ensmallen-devel >= 2.10.0
BuildRequires:  boost-devel, cli11-devel, boost-math, boost-serialization >= 1.49
BuildRequires:  pkg-config

# For generating man pages (CMake configuration takes care of this assuming
# txt2man is installed).  It is possible that we could just add all the man
# pages, generated offline, as a patch to this SRPM, but txt2man seems to exist
# in repos.
BuildRequires:  txt2man
# For generation of Doxygen HTML documentation.
BuildRequires:  doxygen
BuildRequires:  graphviz

# Required for building Python bindings.
BuildRequires: 	python3, python3-Cython, python3-setuptools, python3-numpy,
BuildRequires:	python3-pandas, python3-pytest-runner
BuildRequires:  python-rpm-macros

# something doesn't like size_t being unsigned long on s390
ExcludeArch:    s390

%description
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use. Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users. mlpack outperforms competing machine learning libraries by large
margins.

# Executables.
%package bin
Summary:        Command-line executables for mlpack (machine learning library)
Requires:       %{name}%{_isa} = %{version}-%{release}

%description bin
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use. Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users. mlpack outperforms competing machine learning libraries by large
margins.  This package provides the command-line executables which run mlpack
methods and related documentation.

# Development headers.
%package devel
Summary:        Development headers for mlpack (C++ machine learning library)
Requires:       %{name} = %{version}-%{release}
Requires:       armadillo-devel >= 8.400.0
Requires:	ensmallen-devel >= 2.10.0
Requires:       boost-devel, boost-program-options, boost-math
Requires:       libxml2-devel
Requires:       lapack-devel
Requires:	pkg-config

%description devel
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use. Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users. mlpack outperforms competing machine learning libraries by large
margins.  This package provides the headers to compile applications against
mlpack.



%package doc
Summary:        Doxygen documentation for mlpack (C++ machine learning library)

%description doc
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use.  Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users.  mlpack outperforms competing machine learning libraries by large
margins.  This package provides the Doxygen-generated documentation for mlpack.

%package python3
Summary:	Python 3 bindings for mlpack (C++ machine learning library)
Requires:	python3
Requires:	python3-numpy
Requires:	python3-pandas
Requires:	python3-Cython

%description python3
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use.  Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users.  mlpack outperforms competing machine learning libraries by large
margins.  This package provides the Python bindings for mlpack.


# For the F20 unversioned documentation change.  This evaluates to
# %%{_pkgdocdir} if on F20 and %%{_docdir}/%%{name}-%%{version} otherwise.
%global our_docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}

# Disable LTO: it takes too much memory.
%define _lto_cflags %{nil}

%prep
%autosetup -p1

mkdir stb/;
cp %SOURCE1 stb/;
cp %SOURCE2 stb/;

# Disable Doxygen warnings being fatal.
sed -i 's/WARN_AS_ERROR          = YES/WARN_AS_ERROR = NO/' Doxyfile;

%build
%if 0%{?rhel} && 0%{?rhel} <= 7
# On RHEL6, the Boost CMake scripts fail for some reason.  I don't have the
# time (or patience) to investigate, but if we force CMake to find Boost "the
# hard way" by specifying Boost_NO_BOOST_CMAKE=1, it works.
%{cmake28} -D Boost_NO_BOOST_CMAKE=1 -D CMAKE_INSTALL_LIBDIR=%{_libdir} -D DEBUG=OFF -D PROFILE=OFF -D BUILD_TESTS=OFF -D BUILD_PYTHON_BINDINGS=ON -D PYTHON_EXECUTABLE=$(which python3) -D BUILD_GO_BINDINGS=OFF -D BUILD_JULIA_BINDINGS=OFF -D STB_IMAGE_INCLUDE_DIR=stb/
%else
%{cmake} -D CMAKE_INSTALL_LIBDIR=%{_libdir} -D DEBUG=OFF -D PROFILE=OFF -D BUILD_TESTS=OFF -D BUILD_PYTHON_BINDINGS=ON -D PYTHON_EXECUTABLE=$(which python3) -D BUILD_GO_BINDINGS=OFF -D BUILD_JULIA_BINDINGS=OFF -D STB_IMAGE_INCLUDE_DIR=stb/
%endif

# Try and reduce RAM usage.
%ifarch armv7hl
cd %{_vpath_builddir};
cmake -D CMAKE_C_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" -D CMAKE_CXX_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" .
cd ..;
%endif

%ifarch i686
cd %{_vpath_builddir};
cmake -D CMAKE_C_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" -D CMAKE_CXX_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" .
cd ..;
%endif

# Don't use %make because it could use too much RAM with multiple cores on Koji...
%{cmake_build}
# Build documentation ('doc' is not in the list of default targets).
cd %{_vpath_builddir};
make doc
cd ..;

%install
%{cmake_install}

cp stb/stb_image.h $RPM_BUILD_ROOT/%{_includedir}/;
cp stb/stb_image_write.h $RPM_BUILD_ROOT/%{_includedir}/;

# Put the license file and documentation in place.
if [ "%{our_docdir}" != "%{_docdir}/mlpack" ]; then
  mv $RPM_BUILD_ROOT/%{_docdir}/mlpack $RPM_BUILD_ROOT/%{our_docdir}
fi
mkdir -p $RPM_BUILD_ROOT/%{our_docdir}
cp LICENSE.txt $RPM_BUILD_ROOT/%{our_docdir}

%ldconfig_scriptlets


%files
%{_libdir}/libmlpack.so.3
%{_libdir}/libmlpack.so.3.4
%{our_docdir}/LICENSE.txt

%files bin
%{_bindir}/mlpack_adaboost
%{_bindir}/mlpack_approx_kfn
%{_bindir}/mlpack_bayesian_linear_regression
%{_bindir}/mlpack_cf
%{_bindir}/mlpack_dbscan
%{_bindir}/mlpack_decision_stump
%{_bindir}/mlpack_decision_tree
%{_bindir}/mlpack_det
%{_bindir}/mlpack_emst
%{_bindir}/mlpack_fastmks
%{_bindir}/mlpack_gmm_generate
%{_bindir}/mlpack_gmm_probability
%{_bindir}/mlpack_gmm_train
%{_bindir}/mlpack_hmm_generate
%{_bindir}/mlpack_hmm_loglik
%{_bindir}/mlpack_hmm_train
%{_bindir}/mlpack_hmm_viterbi
%{_bindir}/mlpack_hoeffding_tree
%{_bindir}/mlpack_image_converter
%{_bindir}/mlpack_kde
%{_bindir}/mlpack_kernel_pca
%{_bindir}/mlpack_kfn
%{_bindir}/mlpack_kmeans
%{_bindir}/mlpack_knn
%{_bindir}/mlpack_krann
%{_bindir}/mlpack_lars
%{_bindir}/mlpack_linear_regression
%{_bindir}/mlpack_linear_svm
%{_bindir}/mlpack_lmnn
%{_bindir}/mlpack_local_coordinate_coding
%{_bindir}/mlpack_logistic_regression
%{_bindir}/mlpack_lsh
%{_bindir}/mlpack_mean_shift
%{_bindir}/mlpack_nbc
%{_bindir}/mlpack_nca
%{_bindir}/mlpack_nmf
%{_bindir}/mlpack_pca
%{_bindir}/mlpack_perceptron
%{_bindir}/mlpack_preprocess_binarize
%{_bindir}/mlpack_preprocess_describe
%{_bindir}/mlpack_preprocess_imputer
%{_bindir}/mlpack_preprocess_one_hot_encoding
%{_bindir}/mlpack_preprocess_scale
%{_bindir}/mlpack_preprocess_split
%{_bindir}/mlpack_radical
%{_bindir}/mlpack_random_forest
%{_bindir}/mlpack_range_search
%{_bindir}/mlpack_softmax_regression
%{_bindir}/mlpack_sparse_coding
%{_mandir}/mlpack_adaboost.1*
%{_mandir}/mlpack_approx_kfn.1*
%{_mandir}/mlpack_bayesian_linear_regression.1*
%{_mandir}/mlpack_cf.1*
%{_mandir}/mlpack_dbscan.1*
%{_mandir}/mlpack_decision_stump.1*
%{_mandir}/mlpack_decision_tree.1*
%{_mandir}/mlpack_det.1*
%{_mandir}/mlpack_emst.1*
%{_mandir}/mlpack_fastmks.1*
%{_mandir}/mlpack_gmm_generate.1*
%{_mandir}/mlpack_gmm_probability.1*
%{_mandir}/mlpack_gmm_train.1*
%{_mandir}/mlpack_hmm_generate.1*
%{_mandir}/mlpack_hmm_loglik.1*
%{_mandir}/mlpack_hmm_train.1*
%{_mandir}/mlpack_hmm_viterbi.1*
%{_mandir}/mlpack_hoeffding_tree.1*
%{_mandir}/mlpack_image_converter.1*
%{_mandir}/mlpack_kde.1*
%{_mandir}/mlpack_kernel_pca.1*
%{_mandir}/mlpack_kfn.1*
%{_mandir}/mlpack_kmeans.1*
%{_mandir}/mlpack_knn.1*
%{_mandir}/mlpack_krann.1*
%{_mandir}/mlpack_lars.1*
%{_mandir}/mlpack_linear_regression.1*
%{_mandir}/mlpack_linear_svm.1*
%{_mandir}/mlpack_lmnn.1*
%{_mandir}/mlpack_local_coordinate_coding.1*
%{_mandir}/mlpack_logistic_regression.1*
%{_mandir}/mlpack_lsh.1*
%{_mandir}/mlpack_mean_shift.1*
%{_mandir}/mlpack_nbc.1*
%{_mandir}/mlpack_nca.1*
%{_mandir}/mlpack_nmf.1*
%{_mandir}/mlpack_pca.1*
%{_mandir}/mlpack_perceptron.1*
%{_mandir}/mlpack_preprocess_binarize.1*
%{_mandir}/mlpack_preprocess_describe.1*
%{_mandir}/mlpack_preprocess_imputer.1*
%{_mandir}/mlpack_preprocess_one_hot_encoding.1*
%{_mandir}/mlpack_preprocess_scale.1*
%{_mandir}/mlpack_preprocess_split.1*
%{_mandir}/mlpack_radical.1*
%{_mandir}/mlpack_random_forest.1*
%{_mandir}/mlpack_range_search.1*
%{_mandir}/mlpack_softmax_regression.1*
%{_mandir}/mlpack_sparse_coding.1*

%files devel
%{_libdir}/libmlpack.so
%{_includedir}/mlpack/
%{_libdir}/pkgconfig/mlpack.pc
%{_includedir}/stb_image.h
%{_includedir}/stb_image_write.h
%{_libdir}/cmake/mlpack/mlpack-config-version.cmake
%{_libdir}/cmake/mlpack/mlpack-config.cmake
%{_libdir}/cmake/mlpack/mlpack-targets-noconfig.cmake
%{_libdir}/cmake/mlpack/mlpack-targets.cmake

%files doc
%{our_docdir}

%files python3
%{python3_sitearch}/mlpack/
%{python3_sitearch}/mlpack-*.egg-info

%changelog
* Wed Sep 09 2020 Ryan Curtin <ryan@ratml.org> - 3.4.1-1
- Update to latest stable version.

* Tue Aug 04 2020 Ryan Curtin <ryan@ratml.org> - 3.3.2-4
- Update for CMake out-of-source build fixes.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Ryan Curtin <ryan@ratml.org> - 3.3.2-1
- Update to latest stable version.

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 3.3.0-3
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-2
- Rebuilt for Python 3.9

* Wed Apr 08 2020 Ryan Curtin <ryan@ratml.org> - 3.3.0-1
- Update to latest stable version.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Ryan Curtin <ryan@ratml.org> - 3.2.2-1
- Update to latest stable version.

* Tue Nov 05 2019 Ryan Curtin <ryan@ratml.org> - 3.2.1-1
- Update to latest stable version.

* Thu Sep 26 2019 Ryan Curtin <ryan@ratml.org> - 3.2.0-1
- Update to latest stable version.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-2
- Rebuilt for Python 3.8

* Fri Aug 02 2019 Ryan Curtin <ryan@ratml.org> - 3.1.1-1
- Update to latest stable version.

* Thu Jul 25 2019 Ryan Curtin <ryan@ratml.org> - 3.1.0-3
- Add ensmallen dependency correctly.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 Ryan Curtin <ryan@ratml.org> - 3.1.0-1
- Update to latest stable version.

* Sun Mar 10 2019 Ryan Curtin <ryan@ratml.org> - 3.0.4-3
- Remove Python2 packages.

* Thu Feb 07 2019 Ryan Curtin <ryan@ratml.org> - 3.0.4-2
- Add Python packages.
- A few simple fixes.

* Thu Feb 07 2019 Tomas Popela <tpopela@redhat.com> - 3.0.4-1
- Update to 3.0.4

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 2.2.5-9
- Rebuilt for Boost 1.69

* Fri Aug 17 2018 José Abílio Matos <jamatos@fc.up.pt> - 2.2.5-8
- rebuild for armadillo soname bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.2.5-6
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.5-5
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 2.2.5-3
- Rebuilt for Boost 1.66

* Fri Dec 01 2017 Ryan Curtin <ryan@ratml.org> - 2.2.5-2
- Rebuild for Armadillo soname bump.

* Wed Sep 13 2017 Ryan Curtin <ryan@ratml.org> - 2.2.5-1
- Update to latest stable version.
- Add pkg-config dependency.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 2.0.1-6
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 2.0.1-5
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 30 2016 José Matos <jamatos@fedoraproject.org> - 2.0.1-2
- Rebuild for armadillo 7.x and remove BR SuperLU as armadillo takes care of that

* Thu Feb 11 2016 Ryan Curtin <ryan@ratml.org> - 2.0.1-1
- Update to latest stable version.
- Add doxygen.patch for bug with newer Doxygen versions.

* Thu Feb 11 2016 José Matos <jamatos@fedoraproject.org> - 1.0.11-11
- rebuild for armadillo 6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.0.11-9
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.0.11-8
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.0.11-6
- rebuild for Boost 1.58

* Fri Jul  3 2015 José Matos <jamatos@fedoraproject.org> - 1.0.11-5
- Rebuild for armadillo 5(.xxx.y)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.11-3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.0.11-2
- Rebuild for boost 1.57.0

* Thu Dec 11 2014 Ryan Curtin <ryan@ratml.org> - 1.0.11-1
- Update to latest stable release.

* Fri Aug 29 2014 Ryan Curtin <ryan@ratml.org> - 1.0.10-1
- Update to latest stable release.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Ryan Curtin <ryan@ratml.org> - 1.0.9-1
- Update to latest stable release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.0.8-3
- Rebuild for boost 1.55.0

* Wed Mar 19 2014 José Matos <jamatos@fedoraproject.org> - 1.0.8-2
- Rebuild for Armadillo 4.1 on Fedora 19, 20 and rawhide.

* Fri Jan 10 2014 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.8-1
- Update to latest stable release.
- Rebuild for Armadillo 4.0 on rawhide.

* Sun Nov 03 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.7-1
- Update to latest stable release.

* Tue Aug 06 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.6-6
- Add no_exclude_build.patch so that Koji builds don't exclude all the code from Doxygen.

* Tue Aug 06 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.6-5
- Require graphviz (dot) for generation of Doxygen graphs.

* Tue Aug 06 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.6-4
- Use %%{our_docdir} for F20 change to unversioned documentation directory names.
- Do not package HTML documentation in main package.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 1.0.6-2
- Rebuild for boost 1.54.0

* Thu Jun 13 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.6-1
- Update to latest stable release.

* Sat May 25 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.5-1
- Update to latest stable release.
- Add new executables that version 1.0.5 provides.

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.0.4-3
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.0.4-2
- Rebuild for Boost-1.53.0

* Fri Feb 08 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.4-1
- Update to latest stable release.
- Update dependencies to new minimum requirements.

* Wed Jan 02 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.3-4
- Use cmake28 in RHEL packages.

* Wed Jan 02 2013 Dan Horák <dan[at]danny.cz> - 1.0.3-3
- Exclude s390, something doesn't like size_t being unsigned long

* Tue Jan 01 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.3-2
- Add u64_s64.patch.
- Fix bogus dates in changelog.
- Add new executables and man pages to files list.

* Tue Jan 01 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.3-1
- Update to version 1.0.3.
- Remove now-unnecessary packages.

* Wed Sep 26 2012 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.1-5
- Simplify LICENSE.txt installation.
- Install doxygen documentation.

* Sun Sep 16 2012 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.1-4
- Distribute LICENSE.txt.

* Sun Jul 29 2012 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.1-3
- Fix group names for packages.
- Comment patches more verbosely.
- Rename exectuables to mlpack_* to avoid possible naming conflicts.

* Sat Jul 21 2012 Sterling Lewis Peet <sterling.peet@gatech.edu> - 1.0.1-2
- Include GetKernelMatrix patch so that mlpack builds using fedora flags.

* Thu Mar 08 2012 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.1-1
- Initial packaging of mlpack.
