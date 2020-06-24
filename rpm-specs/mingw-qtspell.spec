%{?mingw_package_header}

%global pkgname qtspell

Name:          mingw-%{pkgname}
Version:       0.9.0
Release:       2%{?dist}
Summary:       Spell checking for Qt text widgets

License:       GPLv3+
BuildArch:     noarch
URL:           https://github.com/manisandro/qtspell
Source0:       https://github.com/manisandro/qtspell/archive/%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires: cmake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-enchant2
BuildRequires: mingw32-qt5-qtbase
BuildRequires: mingw32-qt5-qttools
BuildRequires: mingw32-qt5-qttools-tools

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-enchant2
BuildRequires: mingw64-qt5-qtbase
BuildRequires: mingw64-qt5-qttools
BuildRequires: mingw64-qt5-qttools-tools


%description
QtSpell adds spell-checking functionality to Qt's text widgets, using the
enchant spell-checking library.


%package -n mingw32-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname}-Qt5 library
Requires:      mingw32-qt5-qttranslations

%description -n mingw32-%{pkgname}-qt5
MinGW Windows %{pkgname}-Qt5 library.

###############################################################################

%package -n mingw32-%{pkgname}-qt5-static
Summary:       Static version of the MinGW Windows %{pkgname}-Qt5 library
Requires:      mingw32-%{pkgname}-qt5 = %{version}-%{release}

%description -n mingw32-%{pkgname}-qt5-static
Static version of the MinGW Windows %{pkgname}-Qt5 library.

###############################################################################

%package -n mingw64-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname}-Qt5 library
Requires:      mingw64-qt5-qttranslations

%description -n mingw64-%{pkgname}-qt5
MinGW Windows %{pkgname}-Qt5 library.

###############################################################################

%package -n mingw64-%{pkgname}-qt5-static
Summary:       Static version of the MinGW Windows %{pkgname}-Qt5 library
Requires:      mingw64-%{pkgname}-qt5 = %{version}-%{release}

%description -n mingw64-%{pkgname}-qt5-static
Static version of the MinGW Windows %{pkgname}-Qt5 library.

###############################################################################

%{?mingw_debug_package}


%prep
%setup -q -n %{pkgname}-%{version}


%build
mkdir build_qt5
pushd build_qt5
%mingw_cmake -DBUILD_STATIC_LIBS=ON -DUSE_QT5=ON ../..
%mingw_make %{?_smp_mflags}
popd


%install
pushd build_qt5
%mingw_make DESTDIR=%{buildroot} install
popd


%files -n mingw32-%{pkgname}-qt5
%license COPYING
%{mingw32_bindir}/libqtspell-qt5-0.dll
%{mingw32_libdir}/libqtspell-qt5.dll.a
%{mingw32_libdir}/pkgconfig/QtSpell-qt5.pc
%{mingw32_includedir}/QtSpell-qt5/
%{mingw32_datadir}/qt5/translations/QtSpell_*.qm

%files -n mingw32-%{pkgname}-qt5-static
%{mingw32_libdir}/libqtspell-qt5.a

%files -n mingw64-%{pkgname}-qt5
%license COPYING
%{mingw64_bindir}/libqtspell-qt5-0.dll
%{mingw64_libdir}/libqtspell-qt5.dll.a
%{mingw64_libdir}/pkgconfig/QtSpell-qt5.pc
%{mingw64_includedir}/QtSpell-qt5/
%{mingw64_datadir}/qt5/translations/QtSpell_*.qm

%files -n mingw64-%{pkgname}-qt5-static
%{mingw64_libdir}/libqtspell-qt5.a


%changelog
* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 0.9.0-2
- Rebuild (gettext)

* Sat Mar 21 2020 Sandro Mani <manisandro@gmail.com> - 0.9.0-1
- Update to 0.9.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.8.5-5
- Rebuild (Changes/Mingw32GccDwarf2)
- Drop Qt4 build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Sandro Mani <manisandro@gmail.com> - 0.8.5-1
- Update to 0.8.5

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 15 2017 Sandro Mani <manisandro@gmail.com> - 0.8.4-1
- Update to 0.8.4

* Fri Dec 15 2017 Sandro Mani <manisandro@gmail.com> - 0.8.3-2
- Fix incorrect macro syntax

* Fri Dec 15 2017 Sandro Mani <manisandro@gmail.com> - 0.8.3-1
- Update to 0.8.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 08 2016 Sandro Mani <manisandro@gmail.com> - 0.8.2-1
- QtSpell 0.8.2

* Sat Jul 30 2016 Sandro Mani <manisandro@gmail.com> - 0.8.1-3
- Fix requires

* Wed Jul 20 2016 Sandro Mani <manisandro@gmail.com> - 0.8.1-2
- Use %%license
- Use build subdirs instead of copying the entire source tree

* Mon Nov 16 2015 Sandro Mani <manisandro@gmail.com> - 0.8.1-1
- QtSpell 0.8.1

* Wed Apr 29 2015 Sandro Mani <manisandro@gmail.com> - 0.7.2-1
- QtSpell 0.7.2
