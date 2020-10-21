Name: xtuple-openrpt
Version: 3.3.14
Release: 5%{?dist}
Summary: xTuple / PostBooks reporting utility and libraries
License: CPAL
Url: http://www.xtuple.com/openrpt/
Source: https://github.com/xtuple/openrpt/archive/v%version.tar.gz

## upstream patches
Patch25: 0025-Qt-5.11.0-update.patch

BuildRequires: desktop-file-utils
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: pkgconfig(Qt5UiTools)
BuildRequires: zlib-devel
BuildRequires: fontconfig-devel
BuildRequires: libdmtx-devel

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%global _docdir_fmt %{name}

%description
Graphical SQL report writer, designer and rendering engine, optimized
for PostgreSQL. WYSIWYG display, GUI built with Qt. Reports can be saved
as XML, either as files or in a database.

%package images
BuildArch: noarch
Summary: Images for xTuple products

%description images
Graphical SQL report writer, designer and rendering engine, optimized
for PostgreSQL. WYSIWYG display, GUI built with Qt. Reports can be saved
as XML, either as files or in a database.
This package provides images used by OpenRPT and dependencies.

%package libs
Summary: Shared libraries for OpenRPT
Requires: %{name}-images = %{version}-%{release}

%description libs
Graphical SQL report writer, designer and rendering engine, optimized
for PostgreSQL. WYSIWYG display, GUI built with Qt. Reports can be saved
as XML, either as files or in a database.
This package provides the core libraries: libopenrpt

%package devel
Summary: OpenRPT development files
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel
Requires: qt5-linguist
Requires: libdmtx-devel

%description devel
Graphical SQL report writer, designer and rendering engine, optimized
for PostgreSQL. WYSIWYG display, GUI built with Qt. Reports can be saved
as XML, either as files or in a database.
This package provides the header files used by developers.

%prep
%autosetup -n openrpt-%{version} -p1

%build
export USE_SYSTEM_DMTX=1

lrelease-qt5 */*/*.ts */*.ts

%{qmake_qt5} .

%make_build

%install
# make install doesn't do anything for this qmake project so we do
# the installs manually
#make INSTALL_ROOT=%{buildroot} install
#rm -f %{buildroot}%{_libdir}/lib*.a
mv bin/graph bin/openrpt-graph
mkdir -p %{buildroot}%{_bindir}
install bin/* %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
cp -dp lib/lib*.so* %{buildroot}%{_libdir}
find %{buildroot}%{_libdir} -name 'lib*.so*' -exec chmod 0755 {} \;
mkdir -p %{buildroot}%{_includedir}/openrpt
find . -name '*.h' -exec install -m 0644 -D {} %{buildroot}%{_includedir}/openrpt/{} \;
mkdir -p %{buildroot}%{_datadir}/openrpt/OpenRPT/images
cp -r OpenRPT/images/* %{buildroot}%{_datadir}/openrpt/OpenRPT/images
rm %{buildroot}%{_datadir}/openrpt/OpenRPT/images/icons_24x24/Thumbs.db
rm %{buildroot}%{_datadir}/openrpt/OpenRPT/images/openrpt_qembed.h
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications *.desktop


%files 
%{_bindir}/exportrpt
%{_bindir}/importmqlgui
%{_bindir}/importrpt
%{_bindir}/importrptgui
%{_bindir}/metasql
%{_bindir}/openrpt
%{_bindir}/openrpt-graph
%{_bindir}/rptrender
%{_datadir}/applications/importmqlgui.desktop
%{_datadir}/applications/importrptgui.desktop
%{_datadir}/applications/openrpt.desktop

%ldconfig_scriptlets libs

%files libs
%{_libdir}/libopenrptcommon.so.1*
%{_libdir}/libMetaSQL.so.1*
%{_libdir}/librenderer.so.1*
%{_libdir}/libwrtembed.so.1*
%{_libdir}/libqzint.so.1*

%files images
%license COPYING
%dir %{_datadir}/openrpt/
%dir %{_datadir}/openrpt/OpenRPT/
%{_datadir}/openrpt/OpenRPT/images/

%files devel
%{_includedir}/openrpt/
%{_libdir}/libopenrptcommon.so
%{_libdir}/libMetaSQL.so
%{_libdir}/librenderer.so
%{_libdir}/libwrtembed.so
%{_libdir}/libqzint.so

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.3.14-1
- use %%autosetup, %%make_build %%ldconfig_scriptlets
- xtuple-openrpt-v3.3.14 is available (#1242106)
- xtuple-openrpt: FTBFS in Fedora rawhide (#1606761)
- tighten %%files (less globs mostly)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 14 2017 Daniel Pocock <daniel@pocock.pro> - 3.3.12-8
- New upstream release.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 3.3.10-5
- use %%qmake_qt4 macro to ensure proper build flags

* Fri Sep 04 2015 Daniel Pocock <daniel@pocock.pro> - 3.3.10-4
- Fix release number.

* Thu Sep  3 2015 Daniel Pocock <daniel@pocock.pro> - 3.3.10-3
- New upstream release.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 25 2015 Daniel Pocock <daniel@pocock.pro> - 3.3.9-1
- Initial RPM packaging.

