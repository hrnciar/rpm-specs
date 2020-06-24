Name:           lxqt-themes
Version:        0.15.0
Release:        1%{?dist}
Summary:        LXQt standard themes

License:        LGPLv2+
URL:            https://lxqt.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Pagure do not provide tarballs yet.
# To generate this tarball, clone from pagure
# https://pagure.io/lxqt-themes-fedora/
# Remove the .git dir and manual compress it
Source1:        lxqt-themes-fedora-1.0.tar.xz

BuildArch:      noarch

BuildRequires:  lxqt-build-tools >= 0.6.0
BuildRequires:  pkgconfig(lxqt) >= 0.14.0

Requires:       hicolor-icon-theme
Requires:       fedora-logos
Requires:       desktop-backgrounds-compat
Requires:       breeze-cursor-themes
Requires:       breeze-icon-theme

# The themes were essential part of the previous lxqt-common package which
# no longer exists. Therefore we obsolete and provide it here:
Provides:       lxqt-common = %{version}-%{release}
Obsoletes:      lxqt-common < 0.12.0
# The old name for the theme subpackage was lxqt-theme
Provides:       lxqt-theme = %{version}-%{release}
Obsoletes:      lxqt-theme < 0.12.0

%description
This package contains the standard themes for the LXQt desktop, namely
ambiance, dark, frost, kde-plasma, light and system.

%package fedora
Summary: Default Fedora theme for LXQt
Requires: lxqt-theme = %{version}
Requires: breeze-cursor-theme
Requires: breeze-icon-theme
# Obsolete and provide the old subpackage of lxqt-common
Provides:       lxqt-theme-fedora = %{version}-%{release}
Obsoletes:      lxqt-theme-fedora < %{version}-%{release}

%description fedora
%{summary}.

%prep
%autosetup
%setup -b 1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
#    %%{cmake_lxqt} -DPULL_TRANSLATIONS=NO ..
     %{cmake} ..
popd
make %{?_smp_mflags} -C %{_target_platform}

%if 0%{?fedora} >= 29

pushd %{_builddir}/lxqt-themes-fedora-1.0
tar Jxf %{SOURCE1}
mkdir -p %{_target_platform}
pushd %{_target_platform}
     %{cmake} ..
popd
popd

%endif

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
pushd %{_builddir}/lxqt-themes-fedora-1.0
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
popd
exit

%files
%license COPYING
%doc AUTHORS CHANGELOG README.md
%{_datadir}/lxqt/graphics
%dir %{_datadir}/lxqt/themes
%{_datadir}/lxqt/themes/{ambiance,dark,frost,kde-plasma,light,system}
%{_datadir}/icons/hicolor/scalable/*/*.svg

%files fedora
%{_datadir}/sddm/themes/02-lxqt-fedora/
%{_datadir}/lxqt/themes/fedora-lxqt

%changelog
* Sun May 03 2020 Zamir SUN <sztsian@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Zamir SUN <zsun@fedoraproject.org>  - 0.14.0-1
- Prepare for LXQt 0.14.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-5
- Obsolete and provide the old subpackage of lxqt-common
- Fixes RHBZ 1624739

* Sun Aug 26 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-4
- Merge lxqt-themes-fedora into lxqt-themes

* Fri Aug 24 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-3
- Bump for package review

* Sun Jun 03 2018 Christian Dersch <lupinix@mailbox.org> - 0.13.0-2
- add requirements for the themes

* Sun Jun  3 2018 Christian Dersch <lupinix@mailbox.org> - 0.13.0-1
- initial package

