%global forgeurl https://github.com/fcitx/xcb-imdkit
%global commit 33f5c35daf543c0faac1041c2896306b82baff64
%forgemeta

Name:       xcb-imdkit
Version:    0
Release:    0.4%{?dist}
Summary:    Input method development support for xcb
# source files in src/xlibi18n use the "old style" MIT license known as NTP.
License:    LGPLv2 and MIT
URL:        %{forgeurl}
Source:     %{forgesource}

BuildRequires:  cmake,
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-util)

%description
xcb-imdkit is an implementation of xim protocol in xcb, 
comparing with the implementation of IMDkit with Xlib, 
and xim inside Xlib, it has less memory foot print, 
better performance, and safer on malformed client.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Devel files for xcb-imdkit

%prep
%forgesetup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSES/LGPL-2.1-only.txt
%doc README.md
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/xcb-imdkit/
%{_libdir}/cmake/XCBImdkit/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/xcb-imdkit.pc

%changelog
* Fri Oct 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.4.20201016git33f5c35
- update to upstream commit
- commit 33f5c35daf543c0faac1041c2896306b82baff64

* Sun Aug 30 23:37:45 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3.20200811gitd6609a7
- rebuilt to push

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200811gitd6609a7
- Change according to review 

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811gitd6609a7
- initial package

