Name:           qtspell
Version:        0.9.0
Release:        2%{?dist}
Summary:        Spell checking for Qt text widgets

License:        GPLv3+
URL:            https://github.com/manisandro/qtspell
Source0:        https://github.com/manisandro/qtspell/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  enchant2-devel
BuildRequires:  doxygen

Requires:       iso-codes

%description
QtSpell adds spell-checking functionality to Qt's text widgets, using the
enchant spell-checking library.


%package        qt5
Summary:        Spell checking for Qt5 text widgets

%description    qt5
QtSpell adds spell-checking functionality to Qt5's text widgets, using the
enchant spell-checking library.


%package        qt5-devel
Summary:        Development files for %{name}-qt5
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}

%description    qt5-devel
The %{name}-qt5-devel package contains libraries and header files for
developing applications that use %{name}-qt5.


%package        qt5-translations
Summary:        Translations for %{name}-qt5
BuildArch:      noarch
Requires:       %{name}-qt5 = %{version}-%{release}
Requires:       qt5-qttranslations

%description    qt5-translations
The %{name}-qt5-translations contains translations for %{name}-qt5.


%package        doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains the documentation for developing applications
that use %{name}.


%prep
%autosetup


%build
%cmake
%cmake_build
make doc -C %{__cmake_builddir}


%install
%cmake_install


%ldconfig_scriptlets qt5


%files qt5
%license COPYING
%{_libdir}/libqtspell-qt5.so.*

%files qt5-devel
%{_includedir}/QtSpell-qt5/
%{_libdir}/libqtspell-qt5.so
%{_libdir}/pkgconfig/QtSpell-qt5.pc

%files qt5-translations
%{_qt5_translationdir}/QtSpell_*.qm

%files doc
%license COPYING
%doc %{__cmake_builddir}/doc/html


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 21 2020 Sandro Mani <manisandro@gmail.com> - 0.9.0-1
- Update to 0.9.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Sandro Mani <manisandro@gmail.com> - 0.8.5-1
- Update to 0.8.5

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.com> - 0.8.4-3
- Add missing BR: gcc-c++, make

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 15 2017 Sandro Mani <manisandro@gmail.com> - 0.8.4-1
- Update to 0.8.4

* Fri Dec 15 2017 Sandro Mani <manisandro@gmail.com> - 0.8.3-1
- Update to 0.8.3

* Mon Aug 07 2017 Sandro Mani <manisandro@gmail.com> - 0.8.2-5
- Rebuild for ppc64le binutils bug

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 08 2016 Sandro Mani <manisandro@gmail.com> - 0.8.2-1
- QtSpell 0.8.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Sandro Mani <manisandro@gmail.com> - 0.8.1-1
- QtSpell 0.8.1

* Fri Oct 16 2015 Sandro Mani <manisandro@gmail.com> - 0.8.0-1
- QtSpell 0.8.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Sandro Mani <manisandro@gmail.com> - 0.7.4-1
- QtSpell 0.7.4

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 30 2015 Sandro Mani <manisandro@gmail.com> - 0.7.2-1
- QtSpell 0.7.2

* Mon Feb 09 2015 Sandro Mani <manisandro@gmail.com> - 0.7.1-1
- QtSpell 0.7.1

* Thu Feb 05 2015 Sandro Mani <manisandro@gmail.com> - 0.7.0-1
- QtSpell 0.7.0

* Sat Dec 27 2014 Sandro Mani <manisandro@gmail.com> - 0.6.0-1
- QtSpell 0.6.0

* Fri Dec 12 2014 Sandro Mani <manisandro@gmail.com> - 0.5.0-2
- Use %%license
- Add -Wl,--as-needed

* Fri Dec 12 2014 Sandro Mani <manisandro@gmail.com> - 0.5.0-1
- QtSpell 0.5.0
