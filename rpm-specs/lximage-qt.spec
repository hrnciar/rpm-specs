Name:           lximage-qt
Version:        0.15.0
Release:        2%{?dist}
Summary:        The image viewer and screenshot tool for LXQt
License:        GPLv2+
URL:            http://lxqt.org/
Source0: https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  qt5-linguist
BuildRequires:  kf5-kwindowsystem-devel >= 5.5
BuildRequires:  pkgconfig(lxqt) >= 0.14.0
BuildRequires:  pkgconfig(libfm-qt) >= 0.14.0
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  desktop-file-utils
%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
%endif

# we place additional files in icons/hicolor
Requires:       hicolor-icon-theme

%description
The Qt port of LXImage, a simple and fast image viewer.

%package l10n
BuildArch:      noarch
Summary:        Translations for lximage-qt
Requires:       lximage-qt
%description l10n
This package provides translations for the lximage-qt package.

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

for desktop in %{buildroot}/%{_datadir}/applications/*.desktop; do
    # Exclude category as been Service
    desktop-file-edit --remove-category=LXQt --remove-only-show-in=LXQt --add-only-show-in=X-LXQt ${desktop}
done

%find_lang lximage-qt --with-qt

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
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}

%files l10n -f lximage-qt.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lximage-qt/translations

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

* Wed Feb 13 2019 Zamir SUN <sztsian@gmail.com> - 0.14.0-2
- Add l10n sub package

* Wed Feb 13 2019 Zamir SUN <zsun@fedoraproject.org>  - 0.14.0-1
- Prepare for LXQt 0.14.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.7.0-1
- Update to version 0.7.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.5.1-3
- rebuilt

* Wed Jan 18 2017 Christian Dersch <lupinix@mailbox.org> - 0.5.1-2
- moved translations to lxqt-l10n

* Sat Jan 07 2017 Christian Dersch <lupinix@mailbox.org> - 0.5.1-1
- new version

* Mon Oct 10 2016 Builder <projects.rg@smart.ms> - 0.5.0-2
- add BR: pkgconfig(Qt5Svg), rhbz#1382475

* Tue Sep 27 2016 Helio Chissini de Castro <helio@kde.org> - 0.5.0-1
- New upstream version tied to lxqt 0.11.0

* Mon Feb 15 2016 Helio Chissini de Castro <helio@kde.org> - 0.4.0-6
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=1307006

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Helio Chissini de Castro <helio@kde.org> - 0.4.0-4
- Adapt for the new lxqt build that allows usage on epel as well (cmake3)

* Wed Jan 13 2016 Raphael Groner <projects.rg@smart.ms> - 0.4.0-3
- fix R: hicolor-icon-theme

* Sat Jan 09 2016 Raphael Groner <projects.rg@smart.ms> - 0.4.0-2
- own translations folder and README file

* Sat Dec 19 2015 Raphael Groner <projects.rg@smart.ms> - 0.4.0-1
- initial
