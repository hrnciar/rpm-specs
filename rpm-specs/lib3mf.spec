Name:           lib3mf
Version:        2.0.0
Release:        4%{?dist}
Summary:        Implementation of the 3D Manufacturing Format file standard
License:        BSD
URL:            https://3mf.io

Source0:        https://github.com/3MFConsortium/lib3mf/archive/v%{version}/lib3mf-%{version}.tar.gz

# Adjust the cmake files to:
#  - not strip the library (breaks debuginfo)
#  - work with cmake3 command (EPEL 7)
#  - do not attempt to build missing bundled googletest (upstream uses a git submodule)
#  - ship the lib3MF.pc file
# https://github.com/3MFConsortium/lib3mf/issues/8#issuecomment-605889424
Patch1:         lib3mf-cmake-adjustments.patch

BuildRequires:  act
BuildRequires:  cmake3
BuildRequires:  gcc-c++

%bcond_without  tests
%if %{with tests}
BuildRequires:  gtest-devel
%endif

# Get the pre-Fedora 33 behavior for now until diverged from EPEL 7
%define __cmake_in_source_build 1

%global _description %{expand:
lib3mf is a C++ implementation of the 3D Manufacturing Format standard.
This is a 3D printing standard for representing geometry as meshes.}

%description %_description


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel %_description


%prep
%autosetup -p1
%if 0%{?fedora} < 33 && 0%{?rhel} < 9
# The tests FTBFS with old gtest
# https://github.com/google/googletest/issues/2065
sed -i 's/INSTANTIATE_TEST_SUITE_P/INSTANTIATE_TEST_CASE_P/' Tests/CPP_Bindings/Source/*.cpp
%endif

# A bundled x86 executable, we use the packaged one instead
# https://github.com/3MFConsortium/lib3mf/issues/199
rm AutomaticComponentToolkit/bin/act.linux
ln -s /usr/bin/act AutomaticComponentToolkit/bin/act.linux

%build
mkdir -p build
cd build
%cmake3 %{!?with_tests:-DLIB3MF_TESTS=OFF} ..
%make_build
cd ..


%install
%make_install -C build

# https://github.com/3MFConsortium/lib3mf/issues/8#issuecomment-605931967
mkdir -p %{buildroot}%{_includedir}/%{name}
mv -n %{buildroot}%{_includedir}/Bindings/*/*.{h,hpp} %{buildroot}%{_includedir}/%{name}
rm -rf %{buildroot}%{_includedir}/Bindings

# Also include the other headers
cp -a Include/* %{buildroot}%{_includedir}/%{name}/
# ...but not the 3rd party libraries
rm -r %{buildroot}%{_includedir}/%{name}/Libraries

# Match Debian
sed -i 's|include$|include/%{name}|' %{buildroot}%{_libdir}/pkgconfig/lib3MF.pc


%if %{with tests}
%check
%make_build test -C build
%endif


%ldconfig_scriptlets


%files
%doc README.md
%license LICENSE
%{_libdir}/%{name}.so.2
%{_libdir}/%{name}.so.2.0.0.0


%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/lib3MF.pc


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Include lib3MF.pc file
- Include all headers

* Mon Mar 30 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-2
- Minor packaging adjustments (#1818945)

* Fri Feb 14 2020 Danny Hindson <danny.hindson@stfc.ac.uk> - 2.0.0-1
- Initial Fedora/EPEL RPM
