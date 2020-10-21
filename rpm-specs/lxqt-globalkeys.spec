Name:    lxqt-globalkeys
Summary: Global keys utility for LXQt desktop suite
Version: 0.15.0
Release: 2%{?dist}
License: LGPLv2+
URL:     http://lxqt.org/
Source0: https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: %{?fedora:cmake}%{!?fedora:cmake3} >= 3.1.0
BuildRequires: pkgconfig(lxqt) >= 0.15.0
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Xdg) >= 1.0.0
BuildRequires: kf5-kwindowsystem-devel >= 5.5
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(glib-2.0)
%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
%endif

Requires: dbus-x11

%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-globalkeys
Requires:       lxqt-globalkeys
%description l10n
This package provides translations for the lxqt-globalkeys package.

%prep
%setup -q

%build
%if 0%{?el7}
scl enable devtoolset-7 - <<\EOF
%endif

mkdir -p %{_target_platform}
pushd %{_target_platform}
   %{cmake_lxqt} -DUSE_QT5=TRUE -DPULL_TRANSLATIONS=NO ..
popd

make %{?_smp_mflags} -C %{_target_platform}
%if 0%{?el7}
EOF
%endif

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

desktop-file-edit --remove-category=LXQt --add-category=X-LXQt \
    --remove-only-show-in=LXQt --add-only-show-in=X-LXQt %{buildroot}%{_datadir}/applications/lxqt-config-globalkeyshortcuts.desktop

%find_lang lxqt-config-globalkeyshortcuts --with-qt

%ldconfig_scriptlets

%files
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{_bindir}/lxqt-globalkeysd
%{_bindir}/lxqt-config-globalkeyshortcuts
%{_datadir}/applications/lxqt-config-globalkeyshortcuts.desktop
%{_libdir}/liblxqt-globalkeys.so.0*
%{_libdir}/liblxqt-globalkeys-ui.so.0*
%{_sysconfdir}/xdg/autostart/lxqt-globalkeyshortcuts.desktop
%{_datadir}/lxqt/globalkeyshortcuts.conf

%files devel
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{_includedir}/lxqt-globalkeys
%{_includedir}/lxqt-globalkeys-ui
%{_libdir}/liblxqt-globalkeys.so
%{_libdir}/liblxqt-globalkeys-ui.so
%{_libdir}/pkgconfig/*.pc
%dir %{_datadir}/cmake/lxqt-globalkeys
%dir %{_datadir}/cmake/lxqt-globalkeys-ui
%{_datadir}/cmake/lxqt-globalkeys/*
%{_datadir}/cmake/lxqt-globalkeys-ui/*

%files l10n -f lxqt-config-globalkeyshortcuts.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/lxqt/translations/lxqt-config-globalkeyshortcuts
%{_datadir}/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_ast.qm
%{_datadir}/lxqt/translations/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_arn.qm

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Zamir SUN <sztsian@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Zamir SUN <sztsian@gmail.com> - 0.14.1-1
- Update to version 0.14.1

* Wed Feb 13 2019 Zamir SUN <zsun@fedoraproject.org>  - 0.14.0-1
- Prepare for LXQt 0.14.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-1
- Update to version 0.13.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-3
- rebuilt

* Wed Jan 18 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-2
- moved translations to lxqt-l10n

* Sat Jan 07 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-1
- new version

* Thu Sep 29 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.0-2
- Fix some rpmlint issues

* Thu Sep 29 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.0-1
- New upstream version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Helio Chissini de Castro <helio@kde.org> - 0.10.0-4
- Another razorqt conflicts

* Sun Dec 13 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-3
- Prepare to epel 7

* Wed Dec 09 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-2
- Use new cmake_lxqt infra

* Mon Nov 02 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-1
- New upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.0-6
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 18 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-5
- Rebuild (gcc5)

* Tue Feb 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-4
- Added missing requires. Closed bug https://bugzilla.redhat.com/show_bug.cgi?id=1191113

* Tue Feb 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-3
- Obsoletes razorqt-globalkeyshortcuts

* Mon Feb 09 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-2
- Proper add locale for Qt tm files

* Sun Feb 08 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-1
- New upstream release 0.9.0

* Tue Feb 03 2015 Helio Chissini de Castro <hcastro@redhat.com> - 0.9.0-0.1
- Preparing for 0.9.0 release

* Mon Dec 29 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-6
- Rebuild against new Qt 5.4.0

* Fri Dec 19 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-5
- Unify naming as discussed on Fedora IRC

* Mon Nov 10 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-4
- Update with fixes from review request on https://bugzilla.redhat.com/show_bug.cgi?id=1159826
- removed autosetup in favor of standard setup macro
- Fix cmake install dir

* Mon Nov 03 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-3
- Update for fedora review

* Tue Oct 28 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-2
- Need specific version requires for QtXdg

* Mon Oct 27 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-1
- First release to LxQt new base

