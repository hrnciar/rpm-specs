%undefine __cmake_in_source_build
%global debug_package %{nil}
%global test_data_version 3.0.0

Name:           json
Version:        3.9.1
Release:        1%{?dist}
Summary:        JSON for Modern C++
License:        MIT
## Not installed
# test/catch.hpp: Boost Software License, Version 1.0
URL:            https://github.com/nlohmann/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz
Source1:        https://github.com/nlohmann/json_test_data/archive/v%{test_data_version}/json_test_data-%{test_data_version}.tar.gz

BuildRequires:  ninja-build
BuildRequires:  gcc-c++
%if 0%{?rhel} && 0%{?rhel} == 7
BuildRequires:  cmake3
%else
BuildRequires:  cmake
%endif

%description
This is a packages version of the nlohmann/json header-only C++
library available at Github.

%package devel
Summary:        Development files for %{name}
Provides:       %{name}-static%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libstdc++-devel%{?_isa}

%description devel
The %{name}-devel package contains C++ header files for developing
applications that use %{name}.

%prep
%autosetup -p1
%setup -q -D -T -a1

%build
%if 0%{?rhel} && 0%{?rhel} == 7
%cmake3 -G Ninja \
%else
%cmake -G Ninja \
%endif
    -DJSON_BuildTests:BOOL=ON \
    -DJSON_TestDataDirectory:STRING=json_test_data-%{test_data_version} \
%cmake_build

%check
%ctest --label-exclude 'git_required' --timeout 3600

%install
%cmake_install

%files devel
%doc README.md
%license LICENSE.MIT
%{_includedir}/nlohmann
%{_libdir}/cmake/nlohmann_json
%{_libdir}/pkgconfig/nlohmann_json.pc

%changelog
* Thu Aug 06 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.9.1-1
- Updated to version 3.9.1.

* Mon Jul 27 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.9.0-1
- Updated to version 3.9.0.

* Wed Jun 24 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.8.0-2
- Backported upstream patches with build and tests fixes.

* Mon Jun 15 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.8.0-1
- Updated to version 3.8.0.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.7.3-1
- Updated to version 3.7.3.

* Mon Nov 11 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.7.2-1
- Updated to version 3.7.2.

* Thu Nov 07 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.7.1-1
- Updated to version 3.7.1.

* Sat Aug 17 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.7.0-1
- Updated to version 3.7.0.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 21 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.1-1
- Updated to version 3.6.1.

* Wed Mar 20 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.0-1
- Updated to version 3.6.0.

* Mon Feb 04 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.5.0-3
- Fixed FTBFS on Fedora 30.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.5.0-1
- Updated to version 3.5.0.

* Mon Nov 05 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.4.0-1
- Updated to version 3.4.0.

* Mon Oct 08 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.3.0-1
- Updated to version 3.3.0.

* Thu Oct 04 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.0-3
- Fixed build under RHEL/CentOS 7 due to missing ctest executable.

* Thu Oct 04 2018 Simone Caronni <negativo17@gmail.com> - 3.2.0-2
- Add support for RHEL/CentOS 7.
- Remove unneeded build requirement.
- Remove obsolete group tag.

* Tue Aug 21 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.0-1
- Updated to version 3.2.0.

* Wed Jul 25 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.2-2
- Added symlink to legacy path.

* Tue Jul 17 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.2-1
- Updated to version 3.1.2.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 02 2016 Daniel Kopecek <dkopecek@redhat.com> - 2.0.2-1
- update to latest upstream release v2.0.2

* Thu Jul 07 2016 Daniel Kopecek <dkopecek@redhat.com> - 2.0.1-1
- update to latest upstream release v2.0.1

* Mon May 16 2016 Daniel Kopecek <dkopecek@redhat.com> - 1.1.0-1
- update to latest upstream release v1.1.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20151110git3948630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-6.20151110git3948630
- update to rev 3948630

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-5.20150410gitd7d0509
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-4.20150410gitd7d0509
- don't build the base package
- removed a dot from the release tag
- corrected -devel subpackage description

* Tue Apr 14 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-3.20150410git.d7d0509
- added patch to fix compilation of json_unit with gcc-5.x

* Tue Apr 14 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-2.20150410git.d7d0509
- run json_unit target from the check section
- document catch.hpp license
- don't build the debuginfo subpackage
- don't generate a distribution specific pkg-config file

* Fri Apr 10 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-1.20150410git.d7d0509
- Initial package
