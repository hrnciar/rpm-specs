Name:           ccls
Version:        0.20190823.6
Release:        4%{?dist}
Summary:        C/C++/ObjC language server

# main package is Apache 2.0
# bundled dependencies are Boost (macro_map) and CC0 (siphash)
License:        ASL 2.0 and CC0 and Boost
URL:            https://github.com/MaskRay/ccls
Source0:        %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/Stop-Shipping-Individual-Component-Libraries-In-clang-lib-Package
Patch0:         0001-cmake-support-CLANG_LINK_CLANG_DYLIB.patch

BuildRequires:  cmake >= 3.8
BuildRequires:  gcc-c++ >= 7.2
BuildRequires:  llvm-devel >= 7.0
BuildRequires:  clang-devel >= 7.0
BuildRequires:  rapidjson-devel
BuildRequires:  zlib-devel

Requires:       llvm >= 7.0

Provides:       bundled(siphash)
Provides:       bundled(macro_map)

%description
ccls, which originates from cquery, is a C/C++/Objective-C language server.

- code completion (with both signature help and snippets)
- definition/references, and other cross references
- cross reference extensions: $ccls/call $ccls/inheritance $ccls/member
  $ccls/vars ...
- formatting
- hierarchies: call (caller/callee) hierarchy, inheritance (base/derived)
  hierarchy, member hierarchy
- symbol rename
- document symbols and approximate search of workspace symbol
- hover information
- diagnostics and code actions (clang FixIts)
- semantic highlighting and preprocessor skipped regions
- semantic navigation: $ccls/navigate


%prep
%autosetup -p1
rm -rf third_party/rapidjson

%build
export CLANG_MAJOR_VERSION=$(clang --version|head -1|awk '{print $3}'|awk -F'.' '{print $1}')

%cmake -DCLANG_LINK_CLANG_DYLIB=ON -DCLANG_RESOURCE_DIR=%{_libdir}/clang/$CLANG_MAJOR_VERSION
%cmake_build

%install
%cmake_install

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
* Tue Aug  4 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190823.6-4
- Fix building with the new cmake macros (rhbz#1863312)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20190823.6-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20190823.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190823.6-2
- Add link to persistent clang resource directory (proper fix for rhbz#1807574)

* Wed May  6 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190823.6-1
- New upstream release 0.20190823.6

* Sun Mar 15 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190823.5-4
- Fix dependency on the current clang version (fix for rhbz#1807574)

* Fri Jan 31 2020 Tom Stellard <tstellar@redhat.com> - 0.20190823.5-3
- Link against libclang-cpp.so
- https://fedoraproject.org/wiki/Changes/Stop-Shipping-Individual-Component-Libraries-In-clang-lib-Package

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20190823.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190823.5-1
- New upstream release 20190823.5

* Sun Oct 27 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190823.4-1
- New upstream release 20190823.4

* Mon Sep 30 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190823.3-1
- New upstream release 20190823.3

* Sun Sep 29 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190823.2-1
- New upstream release 20190823.2

* Sat Sep  7 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190823.1-1
- New upstream release 20190823.1

* Sat Aug 24 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190823-1
- New upstraem release 20190823

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20190314-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 24 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.20190314-1
- Bump version to the Pi Day Release

* Thu Mar  7 2019 Dan Čermák <dcermak@suse.com> - 0.20181225.8-1
- Initial package version for Fedora & openSUSE
