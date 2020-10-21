# https://github.com/hluk/qxtglobalshortcut/commit/16446200b699e0610b8a5fb20b74938225d81d87
%global commit 16446200b699e0610b8a5fb20b74938225d81d87
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20171021

Name:           qxtglobalshortcut
Version:        0.0.1
Release:        0.14.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Cross-platform library for handling system-wide shortcuts in Qt applications
License:        BSD
URL:            https://github.com/hluk/qxtglobalshortcut
Source0:        https://github.com/hluk/qxtglobalshortcut/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5)
%if 0%{?fedora} > 32
BuildRequires:  qt5-qtbase-private-devel
%endif

%description
Cross-platform library for handling system-wide shortcuts in Qt applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       cmake-filesystem%{?_isa}

%description devel
This package provides libraries, header files and documentation for developing
applications using qxtglobalshortcut library.

%prep
%autosetup -p1 -n %{name}-%{commit}

# remove windows files
rm -rf utils/appveyor/
rm -f appveyor.yml

%build
%cmake \
 -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed"
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc AUTHORS README.md
%license COPYING
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.14.20171021git1644620
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.0.1-0.13.20171021git1644620
- Rebuild for rawhide
- Add BR qt5-qtbase-private-devel for fedora > 32

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.12.20171021git1644620
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.11.20171021git1644620
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.10.20171021git1644620
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.9.20171021git1644620
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.8.20171021git1644620
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.0.1-0.7.20171021git1644620
- Add RR cmake-filesystem%{?_isa}
- Remove %%dir %%{_includedir}/%%{name,private}
- Remove %%dir %%{_libdir}/cmake/%%{name}/
  Package owns this directory and all files/directories inside it

* Tue Nov 14 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.0.1-0.6.20171021git1644620
- Remove BR pkgconfig(Qt5Widgets)
- Remove RR qt-devel from subpackage devel
- Add BR pkgconfig(Qt5)

* Sun Oct 29 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.0.1-0.5.20171021git1644620
- Don't include COPYING in %%doc, only in %%license
- Move Unversioned so-files directly in %%_libdir
- Use correct license tag BSD

* Tue Oct 24 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.0.1-0.4.20171021git1644620
- Add BR cmake
- Add BR pkgconfig(Qt5Widgets)

* Tue Oct 24 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.0.1-0.3.20171021git1644620
- Disable qt4 build
- Add BR cmake

* Sat Oct 21 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.0.1-0.2.20171021git1644620
- Update to 0.0.1-0.1.20171021git1644620

* Fri Oct 20 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.0.1-0.1.20171013git2a6f890
- Initial build
