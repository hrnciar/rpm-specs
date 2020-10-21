%undefine __cmake_in_source_build

Name:            polkit-qt-1
Version:         0.113.0
Release:         5%{?dist}
Summary:         Qt bindings for PolicyKit

License:         GPLv2+
URL:             https://api.kde.org/kdesupport-api/polkit-qt-1-apidocs/
Source0:         http://download.kde.org/stable/%{name}/polkit-qt-1-%{version}.tar.xz

BuildRequires:   cmake
BuildRequires:   gcc-c++
BuildRequires:   pkgconfig(polkit-agent-1) pkgconfig(polkit-gobject-1)
BuildRequires:   pkgconfig(Qt5DBus) pkgconfig(Qt5Gui) pkgconfig(Qt5Widgets)
# when/if building docs
#BuildRequires:  doxygen
# when/if building examples too
#pkgconfig(Qt5Xml)

%description
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

%package doc
Summary: Doxygen documentation for the PolkitQt API
Obsoletes: polkit-qt-doc < %{version}-%{release}
Provides:  polkit-qt-doc = %{version}-%{release}
BuildArch: noarch
%description doc
%{summary}.

%package -n polkit-qt5-1
Summary: PolicyKit Qt5 bindings
Obsoletes: polkit-qt5 < 0.112.0-3
Provides:  polkit-qt5 = %{version}-%{release}
%description -n polkit-qt5-1
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

%package -n polkit-qt5-1-devel
Summary: Development files for PolicyKit Qt5 bindings
Obsoletes: polkit-qt5-devel < 0.112.0-3
Provides:  polkit-qt5-devel = %{version}-%{release}
Requires: polkit-qt5-1%{?_isa} = %{version}-%{release}
%description -n polkit-qt5-1-devel
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake -DBUILD_EXAMPLES:BOOL=OFF
%make_build -C %{_target_platform}

## build docs, needswork
#doxygen Mainpage.dox
# Remove installdox file - it is not necessary here
#rm -fv html/installdox


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


#files doc
#doc html/*

%ldconfig_scriptlets -n polkit-qt5-1

%files -n polkit-qt5-1
%doc AUTHORS README
%license COPYING
%{_libdir}/libpolkit-qt5-core-1.so.1*
%{_libdir}/libpolkit-qt5-gui-1.so.1*
%{_libdir}/libpolkit-qt5-agent-1.so.1*

%files -n polkit-qt5-1-devel
%{_includedir}/polkit-qt5-1/
%{_libdir}/libpolkit-qt5-core-1.so
%{_libdir}/libpolkit-qt5-gui-1.so
%{_libdir}/libpolkit-qt5-agent-1.so
%{_libdir}/pkgconfig/polkit-qt5-1.pc
%{_libdir}/pkgconfig/polkit-qt5-core-1.pc
%{_libdir}/pkgconfig/polkit-qt5-gui-1.pc
%{_libdir}/pkgconfig/polkit-qt5-agent-1.pc
%{_libdir}/cmake/PolkitQt5-1/


%changelog
* Fri Aug 21 2020 Troy Dawson <tdawson@redhat.com> - 0.113.0-5
- Fix FTBFS - cmake issues (#1863703)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.113.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.113.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.113.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.113.0-1
- new qt5-only polkit-qt-1 package, let polkit-qt remain for qt4 legacy
