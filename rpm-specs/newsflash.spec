%global __cargo_skip_build 0

Name:           newsflash
Version:        1.0.5
Release:        3%{?dist}
Summary:        Modern feed reader

# (MIT or ASL 2.0) and BSD
# ASL 2.0
# ASL 2.0 or Boost
# ASL 2.0 or MIT or MPLv2.0
# BSD
# GPLv3+
# MIT
# MIT or ASL 2.0
# Unlicense
# Unlicense or MIT
# zlib
License:        GPLv3+ and BSD and ASL 2.0 and MIT and Unlicense and zlib
URL:            https://gitlab.com/news-flash/news_flash_gtk
Source0:        https://gitlab.com/news-flash/news_flash_gtk/-/archive/%{version_no_tilde}/news_flash_gtk-%{version_no_tilde}.tar.bz2

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  meson
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

%description
A modern feed reader designed for the GNOME desktop. NewsFlash is a program
designed to complement an already existing web-based RSS reader account.

It combines all the advantages of web based services like syncing across all
your devices with everything you expect from a modern desktop program:
Desktop notifications, fast search and filtering, tagging, handy keyboard
shortcuts and having access to all your articles as long as you like.

%prep
%autosetup -n news_flash_gtk-%{version_no_tilde} -p1
# Use packaged crates with proper versions
sed -i \
  -e '/tokio/s/=0.2/0.2/' \
  -e '/gettext-rs/s/0\.4/0.5/' \
  Cargo.toml
# We will build by cargo ourselves
sed -i -e '/\(build_by_default\|install\)/s/true/false/' src/meson.build
sed -i -e '/dependency/d' meson.build
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%meson
%meson_build
export FEEDLY_CLIENT_ID="boutroue"
export FEEDLY_CLIENT_SECRET="FE012EGICU4ZOBDRBEOVAJA1JZYH"
export PASSWORD_CRYPT_KEY="ypsSXCLhJngks9qGUAqShd8JjRaZ824wT3e"
export MERCURY_PARSER_USER="newsflash"
export MERCURY_PARSER_KEY="R4qcKEHpr9RTq6YuRAPkm9kMhjp4GuxiWG44VDk3Na4ZsN7F"
%cargo_build

%install
%meson_install
%cargo_install
mv %{buildroot}%{_bindir}/{news_flash_gtk,com.gitlab.newsflash}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.gitlab.newsflash.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.gitlab.newsflash.appdata.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/com.gitlab.newsflash
%{_datadir}/applications/com.gitlab.newsflash.desktop
%{_datadir}/dbus-1/services/com.gitlab.newsflash.service
%{_datadir}/icons/hicolor/*/apps/com.gitlab.newsflash*
%{_datadir}/metainfo/com.gitlab.newsflash.appdata.xml

%changelog
* Fri Oct 09 2020 Jan Staněk <jstanek@redhat.com> - 1.0.5-3
- Bump gettext-rs dependency to 0.5

* Fri Sep 11 2020 Josh Stone <jistone@redhat.com> - 1.0.5-2
- Update to

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0~rc1-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0~rc1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Josh Stone <jistone@redhat.com> - 1.0~rc1-6
- Update gtk-rs

* Sat Jun 13 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0~rc1-5
- Add secrets for various services

* Sat Jun 13 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0~rc1-4
- Make copying text with keyboard possible

* Fri Jun 12 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0~rc1-3
- Backport fix for 32bit platforms
- Update fix for missing icon in GNOME Shell

* Fri Jun 12 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0~rc1-2
- Fixup showing icon

* Sun Jun 07 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0~rc1-1
- Initial package
