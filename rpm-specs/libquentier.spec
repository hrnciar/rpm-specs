# Force out of source build
%undefine __cmake_in_source_build

%global commit          9f79dc4d3a93ee5be601ac436d382a52876be071
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20200617

Name:       libquentier
Summary:    Set of Qt/C++ APIs for feature rich desktop clients for Evernote service
Version:    0.5.0
Release:    0.3.%{snapshotdate}git%{shortcommit}%{?dist}

License:    GPLv3 or LGPLv3
URL:        https://github.com/d1vanov/libquentier
Source0:    %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Patch0:     libquentier-4ce8e3b-fix_translations_install.patch

ExclusiveArch: %{qt5_qtwebengine_arches}

BuildRequires: cmake
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5WebEngine)
BuildRequires: cmake(Qt5WebEngineCore)
BuildRequires: cmake(Qt5WebEngineWidgets)
BuildRequires: cmake(Qt5WebSockets)
BuildRequires: cmake(Qt5WebChannel)
BuildRequires: cmake(libxml2)
BuildRequires: cmake(QEverCloud-qt5)
BuildRequires: cmake(Qt5Keychain)
BuildRequires: pkgconfig(hunspell)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: boost-devel
BuildRequires: libtidy-devel
BuildRequires: doxygen
BuildRequires: graphviz

%description
This library presents a set of Qt/C++ APIs useful for applications working as
feature rich desktop clients for Evernote service. The most important and
useful components of the library are the following:

 - Local storage - persistence of data downloaded from Evernote service in
   a local SQLite database
 - Synchronization - the logics of exchanging new and/or modified data
   with Evernote service
 - Note editor - the UI component capable for notes displaying and editing

The library is based on the lower level functionality provided by QEverCloud
library. It also serves as the functional core of Quentier application.

%package devel
Summary:       Headers files for developing with %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for developing applications that use %{name}.

%package doc
Summary: Documentation for %{name}

%description doc
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%cmake -DUSE_QT5=1 \
       -DCMAKE_INSTALL_LIBDIR=%{_qt5_libdir} \
       -DQt5_LUPDATE_EXECUTABLE=%{_bindir}/lupdate-qt5 \
       -DQt5_LRELEASE_EXECUTABLE=%{_bindir}/lrelease-qt5
%cmake_build
cd %{_vpath_builddir}
make lupdate
make lrelease
make doc

%install
%cmake_install
cd %{_vpath_builddir}
mkdir -p %{buildroot}%{_qt5_docdir}/%{name}
cp -aR doc/html/* %{buildroot}%{_qt5_docdir}/%{name}

%files
%doc CONTRIBUTING.md README.md
%license COPYING.LESSER COPYING.txt
%{_qt5_libdir}/libqt5quentier.so.0*
%dir %{_datadir}/libquentier
%{_datadir}/libquentier/translations

%files devel
%{_includedir}/quentier
%{_qt5_libdir}/libqt5quentier.so
%{_qt5_libdir}/cmake/Libquentier-qt5/

%files doc
%doc CONTRIBUTING.md README.md
%license COPYING.LESSER COPYING.txt
%{_qt5_docdir}/%{name}

%changelog
* Wed Jul 29 14:20:28 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.0-0.3.20200617git9f79dc4
- Fix FTBFS

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.2.20200617git9f79dc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 18:33:52 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.0-0.1.20200617git6d3c37b
- Bump to commit 9f79dc4d3a93ee5be601ac436d382a52876be071

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.13.20190730git6d3c37b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jul 30 20:02:38 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-0.12.20190730git6d3c37b
- Add missing BR

* Tue Jul 30 18:17:10 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-0.11.20190730git6d3c37b
- Bump to commit 6d3c37b20a711817bc774f8fe61b746e005d834d

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.10.20190311git625eb28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-0.9.20190311git625eb28
- Bump to 625eb2864605588b4ffa0562fe8cf06b17395a6b
- Remove hunspell patch as it has been upstreamed

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.8.20180903gitcba4ada
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Caolán McNamara <caolanm@redhat.com> - 0.4.0-0.7.20180903gitcba4ada
- rebuild for hunspell-1.7.0

* Mon Sep 03 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-0.6.20180903gitcba4ada
- Bump to commit cba4adad116ad7b7b026974be72490e82885eeff

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.5.20180622git4e41420
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-0.4.20180622git4e41420
- Bump to commit 4e414201883d4ec3966f30b2e384c5182034589f

* Mon Mar 05 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-0.3.20180301git4ce8e3b
- Bump to commit 4ce8e3b76bd9bedd75fe8cb398ddf2a91556b59a

* Tue Feb 27 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-0.2.20180226git5db522e
- Bump to commit 5db522e5257001f65fdcae6bc8f49956ed264623

* Fri Feb 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-0.1.20180130git45bb65b
- Initial RPM release.
