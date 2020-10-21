%undefine __cmake_in_source_build

Name:           xtensor
Version:        0.21.7
Release:        3%{?dist}
Summary:        C++ tensors with broadcasting and lazy computing
License:        BSD
URL:            http://xtensor.readthedocs.io/

%global github  https://github.com/QuantStack/xtensor
Source0:        %{github}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  xtl-devel
BuildRequires:  xsimd-devel
BuildRequires:  python3-numpy

Patch0:		test_portability.patch
Patch1:		0001-Fix-xnpy-save-padding-computation.patch
Patch2:		disable_arch_native.patch

# there is no actual arched content - this is a header only library
%global debug_package %{nil}

%global _description %{expand:
xtensor is a C++ library meant for numerical analysis with multi-dimensional
array expressions.

xtensor provides:
- an extensible expression system enabling lazy broadcasting.
- an API following the idioms of the C++ standard library.
- tools to manipulate array expressions and build upon xtensor.}


%description %_description

%package devel
Summary:        %{summary}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
Requires:       xtl-devel
Requires:       xsimd-devel

%description devel %_description


%prep
%autosetup -p1

%ifarch s390x
find -name '*.npy' -exec %{__python3} -c "import numpy as np; np.save('{}', np.load('{}').byteswap().newbyteorder())" \;
%endif

%build
%cmake -DBUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%make_build -C %{_vpath_builddir} xtest

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}.hpp
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Oct 06 2020 sguelton@redhat.com - 0.21.7-3
- Activate all architectures, fixing the remaining issues in the test suite

* Mon Oct 05 2020 sguelton@redhat.com - 0.21.7-2
- Fix UB in upstream testsuite, see https://github.com/xtensor-stack/xtensor/pull/2175
- Activates armv7hl

* Sat Oct 3 2020 sguelton@redhat.com - 0.21.7-1
- Upstream version bump

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 16 2020 sguelton@redhat.com - 0.21.2-1
- Upstream version bump

* Tue Sep 3 2019 sguelton@redhat.com - 0.20.8-1
- Initial package
