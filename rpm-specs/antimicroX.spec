# Force out of source build
%undefine __cmake_in_source_build

%global snap       20200617
%global gitcommit  c6d79008dfb9fa393eb467ae17201fc693f19f47
%global shortcommit %(c=%{gitcommit}; echo ${c:0:5})

%global appname com.github.juliagoda.antimicroX
%global libname libantilib

Name:         antimicroX
Version:      3.0
Release:      4%{?snap:.%{snap}git%{shortcommit}}%{?dist}
Summary:      Graphical program used to map keyboard buttons and mouse controls to a gamepad
# Build failure, https://bugzilla.redhat.com/show_bug.cgi?id=1849216
ExcludeArch:  %{arm}

License:  GPLv3+
URL:      https://github.com/juliagoda/%{name}

%if 0%{?snap}
%global archivename %{name}-%{gitcommit}
%else
%global archivename %{name}-%{version}
%endif

%if 0%{?snap}
Source0:        %{url}/archive/%{gitcommit}/%{archivename}.tar.gz  
%else
Source0:        %{url}/archive/%{version}/%{archivename}.tar.gz
%endif

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libXtst-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  SDL2-devel
BuildRequires:  itstool
BuildRequires:  gettext
# For desktop file & AppData
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

Requires: %{name}-%{libname}%{?_isa} = %{version}-%{release}
# Icon folder
Requires: hicolor-icon-theme
Requires: shared-mime-info

%description
%{name} is a graphical program used to map keyboard keys and mouse controls 
to a gamepad. This program is useful for playing PC games using a gamepad that 
do not have any form of built-in gamepad support. %{name} is a fork of 
AntiMicro which was inspired by QJoyPad but has additional features.

%package %{libname}
Summary:  %{name} libraries

%description %{libname}
Contains library files required for running %{name}.

%package %{libname}-devel
Summary:  Development files for %{libname}
Requires: %{name}-%{libname}%{?_isa} = %{version}-%{release}

%description %{libname}-devel
The %{libname}-devel package contains libraries and header files for %{libname}.

%prep
%setup -n %{archivename} -q

%build
%cmake3
%cmake3_build

%install
%cmake3_install

%find_lang %{name} --with-qt

%files -f %{name}.lang
# Redundant
%exclude %{_datadir}/%{name}/Changelog
%exclude %dir %{_datadir}/%{name}/translations
%exclude %{_datadir}/%{name}/translations/*
%license LICENSE
%doc Changelog README.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/%{appname}.appdata.xml
%{_datadir}/mime/packages/%{appname}.xml
%{_mandir}/man1/%{name}.1*

%files %{libname}
%license LICENSE
%{_libdir}/%{libname}.so.1

%files %{libname}-devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/%{libname}.so

%check
%{_bindir}/desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appname}.desktop
%{_bindir}/appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{appname}.appdata.xml

%changelog
* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4.20200617gitc6d79
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3.20200617gitc6d79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Gergely Gombos <gombosg@disroot.org> - 3.0-2.20200617gitc6d79
- Final review fixes, first build

* Wed Jun 17 2020 Gergely Gombos <gombosg@disroot.org> - 3.0-1.20200617gitc6d79
- Fix review items, 3.0-master contains soname patch

* Fri Jun 12 2020 Gergely Gombos <gombosg@disroot.org> - 3.0-1
- 3.0

* Sat Jun 06 2020 Gergely Gombos <gombosg@disroot.org> - 2.25-1
- Initial package