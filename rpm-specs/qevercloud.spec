# Force out of source build
%undefine __cmake_in_source_build

%global altname  QEverCloud

Name:       qevercloud
Summary:    Unofficial Evernote Cloud API for Qt5
Version:    6.1.0
Release:    2%{?dist}

License:    MIT
URL:        https://github.com/d1vanov/QEverCloud
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch: %{qt5_qtwebengine_arches}

BuildRequires: cmake
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5WebEngineCore)
BuildRequires: cmake(Qt5WebEngineWidgets)
BuildRequires: doxygen
BuildRequires: qt5-doctools

%description
This library presents the complete Evernote SDK for Qt. All the functionality
that is described on Evernote site is implemented and ready to use.
In particular OAuth authentication is implemented.

%package devel
Summary:       Headers files for developing with %{altname}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for developing applications that use %{altname}.

%package doc
Summary: Documentation for %{altname}
BuildArch: noarch
Requires: qt5-qtbase

%description doc
%{summary}.

%prep
%autosetup -n %{altname}-%{version}

%build
%cmake -DBUILD_QCH_DOCUMENTATION=ON \
       -DCMAKE_INSTALL_LIBDIR=%{_qt5_libdir} \
       -DQHELPGENERATOR_EXECUTABLE=%{_bindir}/qhelpgenerator-qt5
%cmake_build
make doc -C %{_vpath_builddir}

%install
%cmake_install

install -Dpm0644 -t %{buildroot}%{_qt5_docdir} \
  %{_vpath_builddir}/%{altname}.qch
mkdir -p %{buildroot}%{_qt5_docdir}/%{altname}
cp -aR %{_vpath_builddir}/doc/html/* %{buildroot}%{_qt5_docdir}/%{altname}

%check
%{_vpath_builddir}/QEverCloud/test_QEverCloud

%files
%license LICENSE
%{_qt5_libdir}/libqt5qevercloud.so.6*

%files devel
%{_includedir}/qt5qevercloud
%{_qt5_libdir}/libqt5qevercloud.so
%{_qt5_libdir}/cmake/QEverCloud-qt5/

%files doc
%doc docs CHANGELOG.md README.md
%license LICENSE
%{_qt5_docdir}/%{altname}.qch
%{_qt5_docdir}/%{altname}

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 17:31:31 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 6.1.0-1
- Update to 6.1.0 (#1790089)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 12 16:20:54 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 4.1.0-1
- Release 4.1.0 (#1750142)

* Tue Jul 30 17:52:13 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 4.0.0-7.20190730git82d0e5c
- Bump to commit 82d0e5c706324c7af188199d32739e9ed237c5d2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6.20190428git256e2f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 19:58:04 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 4.0.0-5.20190428git256e2f5
- Bump to commit 256e2f533fbc7becf78c0c34a446075e7f0af0bd

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4.20180622git238ca5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3.20180622git238ca5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 4.0.0-2.20180622git238ca5f
- Bump to commit 238ca5f9a5e419a50227286bf12b543597b2998c

* Fri Feb 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 4.0.0-1
- Initial RPM release.
