Name:           xtensor
Version:        0.21.2
Release:        1%{?dist}
Summary:        C++ tensors with broadcasting and lazy computing
License:        BSD
URL:            http://xtensor.readthedocs.io/

%global github  https://github.com/QuantStack/xtensor
Source0:        %{github}/archive/%{version}/%{name}-%{version}.tar.gz

# because xtl does so for armv7hl && ppc64le
# because tests fail for s390x
ExcludeArch:    armv7hl ppc64le s390x

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  xtl-devel
BuildRequires:  xsimd-devel


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

%build
%cmake -DBUILD_TESTS=ON .
%make_build

%install
%make_install

%check
%make_build xtest

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jan 16 2020 sguelton@redhat.com - 0.21.2-1
- Upstream version bump

* Tue Sep 3 2019 sguelton@redhat.com - 0.20.8-1
- Initial package
