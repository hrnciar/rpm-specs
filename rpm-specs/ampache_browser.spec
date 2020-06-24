Name: ampache_browser

# Lib and several dirs use this derived name. A change of this name
# is likely to break API users due to not finding files any longer.
%global vername %{name}_1

Version: 1.0.2
Release: 6%{?dist}
Summary: C++ and Qt based client library for Ampache access

License: GPLv3
URL: http://ampache-browser.org
Source0: https://github.com/ampache-browser/ampache_browser/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Source0: https://github.com/ampache-browser/ampache_browser/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires: cmake3
%endif
BuildRequires: gcc-c++
BuildRequires: qt5-qtbase-devel
Patch0: include.patch
%description
Ampache Browser is a library that implements desktop client access to
the Ampache service (http://ampache.org). It provides end-user Qt UI and
has a simple C++ interface that allows easy integration into client
applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%if 0%{?rhel} && 0%{?rhel} < 8
%global __cmake %{_bindir}/cmake3
%endif

%cmake .
%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/lib%{vername}.so.*

%files devel
%dir %{_includedir}/%{vername}
%{_includedir}/%{vername}/%{name}/
%{_libdir}/lib%{vername}.so
%{_libdir}/pkgconfig/%{vername}.pc
%{_libdir}/cmake/%{vername}

%changelog
* Tue Jun 23 2020 Robert Scheck <robert@fedoraproject.org> - 1.0.2-6
- Added build-time conditionals for RHEL/CentOS 7 (#1846719)
- Corrected build requirement from qt5-devel to qt5-qtbase-devel

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 1.0.2-4
- Add missing #include for gcc-10

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 30 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4.20180408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr  7 2018 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.0-3.20180408
- Merge fixes from v1.0 branch.
- Replace ldconfig scriptlets with %%ldconfig_scriptlets macro.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Michael Schwendt <mschwendt@fedoraproject.org> 1.0.0-1
- Create package.
