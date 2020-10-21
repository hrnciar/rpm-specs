Name:           obconf-qt
Version:        0.15.0
Release:        2%{?dist}
Summary:        A configuration editor for the OpenBox window manager

License:        GPLv2+
URL:            https://github.com/lxde/obconf-qt
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  pkgconfig(obrender-3.5)
BuildRequires:  pkgconfig(obt-3.5)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(sm)
%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
BuildRequires:  cmake3
%endif

Requires:       hicolor-icon-theme
Requires:       openbox

%description
%{summary}.


%package l10n
BuildArch:      noarch
Summary:        Translations for obconf-qt
Requires:       obconf-qt
%description l10n
This package provides translations for the obconf-qt package.

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
%make_install -C %{_target_platform}

desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

%find_lang obconf-qt --with-qt

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
%doc AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/%{name}

%files l10n -f obconf-qt.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/obconf-qt/translations

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

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-3
- rebuilt

* Wed Jan 18 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-2
- moved translations to lxqt-l10n

* Sat Jan 07 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-1
- new version

* Wed Sep 28 2016 Christian Dersch <lupinix@mailbox.org> - 0.11.0-1
- Initial package import
- Removed debuginfo patch (applied upstream)

* Mon Jul 18 2016 Christian Dersch <lupinix@fedoraproject.org> - 0.9.0-2
- Added patch for debuginfo

* Sun Jul 17 2016 Christian Dersch <lupinix@fedoraproject.org> - 0.9.0-1
- initial package
