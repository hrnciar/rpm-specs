# Header only lib.  Package is build archful to run the tests
# on all available architectures, thus we disable debug packages.
%global debug_package %{nil}

# Reduce debuginfo for testsuite.
%global optflags %(echo %{optflags} | %{__sed} -e 's! -g ! -g0 !g')

# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

# Package name in lowercase.  %%global won't work here.
%define lc_name %{lua:print(rpm.expand("%{name}"):lower())}


# Set include directory for catch-devel.
%if 0%{?fedora} >= 29
%global catch_includedir %{_includedir}/catch2
%else
%global catch_includedir %{_includedir}/catch
%endif


Name:           RxCpp
Version:        4.1.0
Release:        7%{?dist}
Summary:        Reactive Extensions for C++

License:        ASL 2.0
URL:            https://github.com/Reactive-Extensions/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# 0 - 999: Cherry-picked from upstream.
Patch0:         %{url}/compare/v4.1.0...master.patch#/%{name}-4.1.0-to_master.patch

# 1000 - 1999: Upstreamed.

# 2000 - 2999: Upstreamable.

# 3000 - 3999: Downstream / not upstreamable.

BuildRequires:  catch-devel
BuildRequires:  cmake3
BuildRequires:  gcc-c++

%description
The Reactive Extensions for C++ (RxCpp) is a library of algorithms
for values-distributed-in-time.


%package devel
Summary:        Reactive Extensions for C++
BuildArch:      noarch

Provides:       %{name}           == %{version}-%{release}
Provides:       %{name}-static    == %{version}-%{release}
Provides:       %{lc_name}        == %{version}-%{release}
Provides:       %{lc_name}-devel  == %{version}-%{release}
Provides:       %{lc_name}-static == %{version}-%{release}

%description devel
The Reactive Extensions for C++ (RxCpp) is a library of algorithms
for values-distributed-in-time.


%package doc
Summary:        API-documentation for %{name}
BuildArch:      noarch

BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  hardlink

Provides:       %{lc_name}-doc == %{version}-%{release}

%description doc
This package contains the API-documentation for %{name}.


%prep
%autosetup -p 1

# Rename toplevel license file.
%{__mv} license.md ASL-2.0.txt

# Fix path to catch.
%{__sed} -e 's!\${RXCPP_DIR}/ext/catch/single_include/catch2!%{catch_includedir}!g' \
  -i.catch projects/CMake/shared.cmake


%build
%cmake3 -DCMAKE_BUILD_TYPE=Release .
%make_build all doc


%install
%make_install

# Install docs.
%{__mkdir_p} %{buildroot}%{_pkgdocdir}
%{__cp} -pr DeveloperManual.md README.md Readme.html   \
%if 0%{?rhel} && 0%{?rhel} <= 6
       AUTHORS.txt ASL-2.0.txt Rx/v2/license.txt       \
%endif
       projects/doxygen/html %{buildroot}%{_pkgdocdir}
%{_bindir}/find %{buildroot}%{_pkgdocdir} -type f | \
  %{_bindir}/xargs %{__chmod} -c 0644
%{_bindir}/find %{buildroot}%{_pkgdocdir} -type d | \
  %{_bindir}/xargs %{__chmod} -c 0755
%{_bindir}/hardlink -fv %{buildroot}%{_pkgdocdir}


%check
pushd build/test
%{_bindir}/ctest3 %{_smp_mflags} --output-on-failure
popd


%files devel
%if 0%{?fedora} || 0%{?rhel} >= 7
%license AUTHORS.txt
%license ASL-2.0.txt
%license Rx/v2/license.txt
%else
%doc %{_pkgdocdir}/AUTHORS.txt
%doc %{_pkgdocdir}/ASL-2.0.txt
%doc %{_pkgdocdir}/license.txt
%endif
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/DeveloperManual.md
%doc %{_pkgdocdir}/README.md
%doc %{_pkgdocdir}/Readme.html
%{_includedir}/%{lc_name}


%files doc
%if 0%{?fedora} || 0%{?rhel} >= 7
%license %{_datadir}/licenses/%{name}-devel*
%endif
%doc %{_pkgdocdir}


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 15 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.1.0-4
- Fix FTBFS - updated path of hardlink

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Björn Esser <besser82@fedoraproject.org> - 4.1.0-2
- Update Patch0, remove other patches

* Mon Feb 11 2019 Björn Esser <besser82@fedoraproject.org> - 4.1.0-1
- New upstream release
- Update Patch0
- Reduce debuginfo for testsuite
- Add patch to fix -Wcatch-value
- Build documentation using the doc target in Makefile

* Mon Feb 11 2019 Björn Esser <besser82@fedoraproject.org> - 4.0.0-5
- Fix path to catch.hpp (#1603318)
- Build testsuite with regular system flags again

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 19 2018 Björn Esser <besser82@fedoraproject.org> - 4.0.0-2
- Reduce memory consumption during build
- Run testsuite with mutiple threads and less verbose

* Fri May 18 2018 Björn Esser <besser82@fedoraproject.org> - 4.0.0-1
- Initial import (rhbz#1579523)
- Build single threaded

* Wed May 02 2018 Björn Esser <besser82@fedoraproject.org> - 4.0.0-0.1
- Initial rpm release (rhbz#1579523)
