# https://github.com/anrieff/libcpuid/commit/2f1031543caac4b4d2ebc3d7bea3dabf09f10965
%global commit 2f1031543caac4b4d2ebc3d7bea3dabf09f10965
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20171023

Name:           libcpuid
Version:        0.4.1
#Release:        8.%%{commitdate}git%%{shortcommit}%%{?dist}
Release:        3%{?dist}
Summary:        Provides CPU identification for x86
License:        BSD
URL:            https://github.com/anrieff/libcpuid
#Source0:        https://github.com/anrieff/libcpuid/archive/%%{commit}/%%{name}-%%{shortcommit}.tar.gz
Source0:        https://github.com/anrieff/libcpuid/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
ExcludeArch:    aarch64 %arm ppc64le ppc64 s390x

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  libtool
BuildRequires:  make

%description
Libcpuid provides CPU identification for the x86 (and x86_64).

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
For details about the programming API, please see the docs
on the project's site (http://libcpuid.sourceforge.net/)

%prep
#%%autosetup -n %%{name}-%%{commit}
%autosetup -n %{name}-%{version}

%build
autoreconf -vfi
%configure  --disable-static
%make_build

%install
%make_install
# WARNING: empty dependency_libs variable. remove the pointless .la
rm %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc Readme.md
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_bindir}/cpuid_tool
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*.3.*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8.20171023git2f10315
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7.20171023git2f10315
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6.20171023git2f10315
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5.20171023git2f10315
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 23 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-4.20171023git2f10315
- Update to 0.4.0-4.20171023git2f10315
- Dropped %%{name}-not-use-4m-macro.patch
- Add ExcludeArch: aarch64 %%arm ppc64le ppc64 s390x

* Mon Oct 23 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-3.20170504git57298c6
- Add BR doxygen
- disable build of static lib
- don't remove %%exclude %%{_libdir}/%%{name}.so
- Add %%{name}-not-use-4m-macro.patch

* Mon Oct 23 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-2.20170504git57298c6
- Add BR gcc-c++
- replace libtoolize and autoreconf --install with autoreconf -vfi
- remove %%exclude %%{_libdir}/%%{name}.so.* not needed

* Sun Oct 22 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-1.20170504git57298c6
- Initial build.
