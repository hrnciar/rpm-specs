Name:           xsimd
Version:        7.4.8
Release:        2%{?dist}
Summary:        C++ wrappers for SIMD intrinsics
License:        BSD
URL:            https://xsimd.readthedocs.io/
%global github  https://github.com/QuantStack/xsimd
Source0:        %{github}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-gcc11.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel

%ifarch %{arm}
# Only used for testing, as it's a header-only package.
%global optflags %(echo %{optflags} -mfpu=neon)
%endif

# there is no actual arched content - this is a header only library
%global debug_package %{nil}

# Get Fedora 33++ behavior on anything older
%undefine __cmake_in_source_build

%global _description \
SIMD (Single Instruction, Multiple Data) is a feature of microprocessors that \
has been available for many years. SIMD instructions perform a single operation \
on a batch of values at once, and thus provide a way to significantly \
accelerate code execution. However, these instructions differ between \
microprocessor vendors and compilers. \
 \
xsimd provides a unified means for using these features for library authors. \
Namely, it enables manipulation of batches of numbers with the same arithmetic \
operators as for single values. It also provides accelerated implementation \
of common mathematical functions operating on batches. \

%description %_description

%package devel
Summary:        %{summary}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
%description devel %_description


%prep
%autosetup -p1

%build
%cmake -DBUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
# Explicitly not supported upstream for simd mode. Still valuable for scalar mode layer.
%ifnarch ppc64le s390x
%cmake_build -- xtest
%endif

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sat Oct 17 2020 sguelton@redhat.com - 7.4.8-2
- Fix missing #include for gcc-11

* Sat Oct 3 2020 sguelton@redhat.com - 7.4.8-1
- Update to latest version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 16 2020 sguelton@redhat.com - 7.4.6-1
- Update to latest version

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 Miro Hrončok <mhroncok@redhat.com> - 7.2.3-3
- Allow all architectures

* Wed Jul 03 2019 Miro Hrončok <mhroncok@redhat.com> - 7.2.3-2
- Apply upstream workaround for armv7
- Reenable tests (commented out by mistake)

* Fri Jun 28 2019 Miro Hrončok <mhroncok@redhat.com> - 7.2.3-1
- Initial package
