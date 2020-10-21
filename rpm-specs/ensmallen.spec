Name:           ensmallen
Version:        2.14.2
Release:        1%{?dist}
Summary:        Header-only C++ library for efficient mathematical optimization

License:        BSD
URL:            https://www.ensmallen.org
Source0:        https://www.ensmallen.org/files/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 2.8.5
BuildRequires:	gcc-c++
BuildRequires:	armadillo-devel >= 8.400.0
Requires:       armadillo-devel >= 8.400.0

Patch0:         random_tests.patch

# ensmallen is header-only, and the build just builds the tests, so there's no
# use for a debuginfo package.
%global debug_package %{nil}

%description
ensmallen is a header-only C++ library for efficient mathematical optimization.
It provides a simple set of abstractions for writing an objective function to
optimize. It also provides a large set of standard and cutting-edge optimizers
that can be used for virtually any mathematical optimization task.  These
include full-batch gradient descent techniques, small-batch techniques,
gradient-free optimizers, and constrained optimization.

%prep
%autosetup -p1

%build
%cmake -DENSMALLEN_CMAKE_DIR=%{_libdir}/cmake/ensmallen/

# Technically we don't need to build anything but it's a good sanity check to
# just build the tests to make sure they compile.
%cmake_build

%install
%cmake_install

%check
# Disable the SmallLovaszThetaSdp test---it exposes a bug in one of ensmallen's
# dependencies.  In addition, sometimes the tests may fail, as they are
# probabilistic---so just make sure the test suite passes at least once out of
# five runs.
%ifarch armv7hl
# There's an issue with the tests on armv7hl.
%else
success=0;
cd %{_vpath_builddir};
for i in `seq 1 5`; do
  code=""; # Reset exit code.
  ./ensmallen_tests ~SmallLovaszThetaSdp ~BBSBBLogisticRegressionTest || code=$?
  if [ "a$code" == "a" ]; then
    success=1;
    break;
  fi
done
if [ $success -eq 0 ]; then
  false # Force a build error.
fi
cd ..;
%endif

%package devel
Summary:  Header-only C++ library for efficient mathematical optimization
Provides: ensmallen-static = %{version}-%{release}

%description devel
ensmallen is a header-only C++ library for efficient mathematical optimization.
It provides a simple set of abstractions for writing an objective function to
optimize. It also provides a large set of standard and cutting-edge optimizers
that can be used for virtually any mathematical optimization task.  These
include full-batch gradient descent techniques, small-batch techniques,
gradient-free optimizers, and constrained optimization.

%files devel
%license LICENSE.txt
%{_includedir}/ensmallen.hpp
%{_includedir}/ensmallen_bits/
%{_libdir}/cmake/ensmallen/ensmallen-config-version.cmake
%{_libdir}/cmake/ensmallen/ensmallen-config.cmake
%{_libdir}/cmake/ensmallen/ensmallen-targets.cmake

%changelog
* Mon Sep 07 2020 Ryan Curtin <ryan@ratml.org> - 2.14.2-1
- Update to latest stable version.

* Mon Aug 03 2020 Ryan Curtin <ryan@ratml.org> - 2.12.0-4
- Fix build failures for mass rebuild issues.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 08 2020 Ryan Curtin <ryan@ratml.org> - 2.12.0-0
- Update to latest stable version.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2019 Ryan Curtin <ryan@ratml.org> - 2.11.1-1
- Update to latest stable version.

* Tue Dec 17 2019 Ryan Curtin <ryan@ratml.org> - 2.10.5-1
- Update to latest stable version.

* Thu Sep 26 2019 Ryan Curtin <ryan@ratml.org> - 2.10.3-1
- Update to latest stable version.

* Wed Sep 11 2019 Ryan Curtin <ryan@ratml.org> - 2.10.2-1
- Update to latest stable version.

* Fri Aug 16 2019 Ryan Curtin <ryan@ratml.org> - 1.16.2-1
- Update to latest stable version.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Ryan Curtin <ryan@ratml.org> - 1.15.1-1
- Update to latest stable version.

* Mon May  6 2019 Ryan Curtin <ryan@ratml.org> - 1.14.2-1
- Initial packaging.
