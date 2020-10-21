Name:		qtermwidget
Version:	0.15.0
Release:	3%{?dist}
License:	GPLv2+
Summary:	Qt5 terminal widget
URL:		https://github.com/lxqt/%{name}/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{?fedora:cmake}%{!?fedora:cmake3} >= 3.0
BuildRequires:  pkgconfig(lxqt) >= 0.13.0
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:  lxqt-build-tools
BuildRequires:  qt5-qttools-devel
%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
%endif

# Provide and Obsolete the old -qt5 name
Provides:       qtermwidget-qt5 = %{version}-%{release}
Obsoletes:      qtermwidget-qt5 < %{version}-%{release}


%description
QTermWidget is an open-source project originally based on KDE4 Konsole
application, but it took its own direction later.
The main goal of this project is to provide Unicode-enabled, embeddable
Qt widget for using as a built-in console (or terminal emulation widget)


%package	devel
Summary:	Qt5 terminal widget - devel package
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:       qtermwidget-qt5-devel = %{version}-%{release}
Obsoletes:	qtermwidget-qt5-devel < %{version}-%{release}

%description	devel
Development files for qtermwidget-qt5 library.


%package l10n
BuildArch:      noarch
Summary:        Translations for qtermwidget
Requires:       qtermwidget
%description l10n
This package provides translations for the qtermwidget package.

%prep
%setup -q

%build
%if 0%{?el7}
scl enable devtoolset-7 - <<\EOF
%endif
mkdir -p %{_target_platform}
pushd %{_target_platform}
    %{cmake_lxqt} -DPULL_TRANSLATIONS=NO ..
popd

make %{?_smp_mflags} -C %{_target_platform}
%if 0%{?el7}
EOF
%endif

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang qtermwidget --with-qt

%ldconfig_scriptlets

%files
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{_libdir}/lib%{name}5.so.*
%{_datadir}/%{name}5

%files devel
%{_includedir}/%{name}5
%{_libdir}/lib%{name}5.so
%{_libdir}/pkgconfig/%{name}5.pc
%{_libdir}/cmake/qtermwidget5


%files l10n -f qtermwidget.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/qtermwidget5/translations

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Zamir SUN <sztsian@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 0.14.1-3
- Fix missing #include for gcc-10

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Zamir SUN <sztsian@gmail.com> - 0.14.1-1
- Update to version 0.14.1

* Wed Feb 13 2019 Zamir SUN <sztsian@gmail.com>
- Add l10n sub package

* Wed Feb 13 2019 Zamir SUN <zsun@fedoraproject.org>  - 0.14.0-1
- Prepare for LXQt 0.14.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 04 2018 Zamir SUN <zsun@fedoraproject.org> - 0.9.0-1
- Update to version 0.9.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-5
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 24 2017 Christian Dersch <lupinix@mailbox.org> - 0.7.1-2
- fix provides and obsoletes

* Wed Apr 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.7.1-1
- updated to 0.7.1
- removed Qt4 build (now in package qtermwidget-qt4)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 10 2015 TI_Eugene <ti.eugene@gmail.com> - 0.6.0-2
- qt-virt-manager compatible patch added

* Tue Nov 04 2014 TI_Eugene <ti.eugene@gmail.com> - 0.6.0-1
- Version bump
- qt5 packages added

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-6
- Next git snapshot
- Source0 URL changed
- patch removed

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-4
- _isa added to -devel Requires.

* Thu Apr 18 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-3
- all cmake flags removed. "%%cmake .." is the best.

* Thu Apr 18 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-2
- release added to -devel Requires
- dist tag added
- patch link to upstream issue added
- -devel description changed (environment > files)
- designer plugin moved to main package

* Tue Apr 16 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-1
- Initial Fedora packaging
