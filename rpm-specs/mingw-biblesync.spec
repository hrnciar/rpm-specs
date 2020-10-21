%?mingw_package_header

%global __soversion 2.0
%global _pkg_name biblesync

Name:		mingw-%{_pkg_name}
Version:	2.1.0
Release:	3%{?dist}
Summary:	A Cross-platform library for sharing Bible navigation

Group:		System Environment/Libraries
License:	Public Domain
URL:		http://www.xiphos.org
Source0:	https://github.com/karlkleinpaste/%{_pkg_name}/releases/download/%{version}/%{_pkg_name}-%{version}.tar.gz

BuildArch:		noarch


BuildRequires:	cmake

BuildRequires:	mingw32-gcc
BuildRequires:	mingw32-gcc-c++
BuildRequires:	mingw32-gettext

BuildRequires:	mingw64-gcc
BuildRequires:	mingw64-gcc-c++
BuildRequires:	mingw64-gettext

%description
BibleSync is a multicast protocol to support Bible software shared co-
navigation. It uses LAN multicast in either a personal/small team mutual
navigation motif or in a classroom environment where there are Speakers plus
the Audience. It provides a complete yet minimal public interface to support
mode setting, setup for packet reception, transmit on local navigation, and
handling of incoming packets.

This library is not specific to any particular Bible software framework,
completely agnostic as to structure of layers above BibleSync.

# Win32
%package -n mingw32-%{_pkg_name}
Summary:	A MinGW build of the biblesync library

%description -n mingw32-%{_pkg_name}
BibleSync is a multicast protocol to support Bible software shared co-
navigation. It uses LAN multicast in either a personal/small team mutual
navigation motif or in a classroom environment where there are Speakers plus
the Audience. It provides a complete yet minimal public interface to support
mode setting, setup for packet reception, transmit on local navigation, and
handling of incoming packets.

This library is not specific to any particular Bible software framework,
completely agnostic as to structure of layers above BibleSync.


# Win64
%package -n mingw64-%{_pkg_name}
Summary:	A MinGW build of the biblesync library

%description -n mingw64-%{_pkg_name}
BibleSync is a multicast protocol to support Bible software shared co-
navigation. It uses LAN multicast in either a personal/small team mutual
navigation motif or in a classroom environment where there are Speakers plus
the Audience. It provides a complete yet minimal public interface to support
mode setting, setup for packet reception, transmit on local navigation, and
handling of incoming packets.

This library is not specific to any particular Bible software framework,
completely agnostic as to structure of layers above BibleSync.


%?mingw_debug_package


%prep
%setup -q -n %{_pkg_name}-%{version}


%build
%mingw_cmake -DBIBLESYNC_SOVERSION=%{__soversion}
%mingw_make


%install
%mingw_make install DESTDIR=%{buildroot}

find "%{buildroot}" -name man7 | xargs rm -rf
mkdir -p "%{buildroot}%{mingw32_bindir}"
mkdir -p "%{buildroot}%{mingw64_bindir}"
mv "%{buildroot}%{mingw32_libdir}/"*.dll "%{buildroot}%{mingw32_bindir}/"
mv "%{buildroot}%{mingw64_libdir}/"*.dll "%{buildroot}%{mingw64_bindir}/"

%files -n mingw32-%{_pkg_name}
%doc AUTHORS ChangeLog README.md WIRESHARK
%license COPYING
%license LICENSE
%{mingw32_bindir}/lib%{_pkg_name}.dll
%{mingw32_includedir}/%{_pkg_name}
%{mingw32_libdir}/pkgconfig/%{_pkg_name}.pc
%{mingw32_libdir}/lib%{_pkg_name}.dll.a

%files -n mingw64-%{_pkg_name}
%doc AUTHORS ChangeLog README.md WIRESHARK
%license COPYING
%license LICENSE
%{mingw64_bindir}/lib%{_pkg_name}.dll
%{mingw64_includedir}/%{_pkg_name}
%{mingw64_libdir}/pkgconfig/%{_pkg_name}.pc
%{mingw64_libdir}/lib%{_pkg_name}.dll.a

%changelog
* Wed Aug 12 13:34:45 GMT 2020 Sandro Mani <manisandro@gmail.com> - 2.1.0-3
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Greg Hellings <greg.hellings@gmail.com> - 2.1.0-1
- Upstream version 2.1.0
- Remove patch

* Mon Apr 27 2020 Greg Hellings <greg.hellings@gmail.com> - 2.0.1-2
- Properly label license files

* Fri Apr 24 2020 Greg Hellings <greg.hellings@gmail.com> - 2.0.1-1
- Initial build for MinGW
