Name:    lxqt-powermanagement
Summary: Powermanagement daemon for LXQt desktop suite
Version: 0.15.0
Release: 1%{?dist}
License: LGPLv2+
URL:     http://lxqt.org/
Source0: https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Xdg) >= 1.0.0
BuildRequires: pkgconfig(Qt5Svg) >= 1.0.0
BuildRequires: pkgconfig(lxqt) >= 0.15.0
BuildRequires: desktop-file-utils
BuildRequires: kf5-kwindowsystem-devel >= 5.5
BuildRequires: kf5-solid-devel >= 5.5
Buildrequires: kf5-kidletime-devel >= 5.5
BuildRequires: pkgconfig(glib-2.0)
%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
%endif

%description
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-powermanagement
Requires:       lxqt-powermanagement
%description l10n
This package provides translations for the lxqt-powermanagement package.

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

desktop-file-edit --remove-category=LXQt --add-category=X-LXQt \
   --remove-only-show-in=LXQt --add-only-show-in=X-LXQt %{buildroot}%{_datadir}/applications/lxqt-config-powermanagement.desktop

%find_lang lxqt-powermanagement --with-qt
%find_lang lxqt-config-powermanagement --with-qt

%post
%if 0%{?el7}
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-desktop-database &> /dev/null || :
%endif

%postun
%if 0%{?el7}
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
/usr/bin/update-desktop-database &> /dev/null || :
%endif

%posttrans
%if 0%{?el7}
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%files
%{_bindir}/lxqt-powermanagement
%{_bindir}/lxqt-config-powermanagement
%{_datadir}/applications/lxqt-config-powermanagement.desktop
%{_datadir}/icons/hicolor/*
%{_sysconfdir}/xdg/autostart/lxqt-powermanagement.desktop

%files l10n -f lxqt-powermanagement.lang -f lxqt-config-powermanagement.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/lxqt/translations/lxqt-powermanagement
%dir %{_datadir}/lxqt/translations/lxqt-config-powermanagement
%{_datadir}/lxqt/translations/lxqt-powermanagement/lxqt-powermanagement_ast.qm
%{_datadir}/lxqt/translations/lxqt-powermanagement/lxqt-powermanagement_arn.qm
%{_datadir}/lxqt/translations/lxqt-config-powermanagement/lxqt-config-powermanagement_ast.qm
%{_datadir}/lxqt/translations/lxqt-config-powermanagement/lxqt-config-powermanagement_arn.qm

%changelog
* Sun May 03 2020 Zamir SUN <sztsian@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Zamir SUN <sztsian@gmail.com> - 0.14.1-1
- Update to version 0.14.1

* Fri Feb 15 2019 Zamir SUN <zsun@fedoraproject.org>  - 0.14.0-2
- Fix translation package

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

* Tue Sep 27 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.0-1
- New upstream release 0.11.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Helio Chissini de Castro <helio@kde.org> - 0.10.0-3
- Another razorqt obsoletes

* Thu Dec 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-2
- Use new cmake_lxqt infra

* Mon Nov 02 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-1
- New upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 18 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-4
- Rebuild (gcc5)

* Tue Feb 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-3
- Obsoletes razorqt-power as migrated to lxqt

* Mon Feb 09 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-2
- Proper add locale for Qt tm files

* Sun Feb 08 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-1
- New upstream release 0.9.0

* Tue Feb 03 2015 Helio Chissini de Castro <hcastro@redhat.com> - 0.9.0-0.1
- Prepare 0.9.0 release

* Mon Dec 29 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-5
- Rebuild against new Qt 5.4.0

* Sat Dec 20 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-4
- Unify naming as discussed on Fedora IRC

* Mon Nov 10 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-3
- Updates on review https://bugzilla.redhat.com/show_bug.cgi?id=1159877

* Mon Nov 03 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-2
- Update to Fedora package review

* Mon Oct 27 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-1
- First release to LxQt new base
