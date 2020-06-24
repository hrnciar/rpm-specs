%global __cargo_skip_build 0

Name:           newsflash
Version:        1.0~rc1
Release:        5%{?dist}
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
Source0:        https://gitlab.com/news-flash/news_flash_gtk/-/archive/%{version_no_tilde}/news_flash_gtk-%{version_no_tilde}.tar.gz
# https://gitlab.com/news-flash/news_flash_gtk/-/issues/66
# https://gitlab.com/news-flash/news_flash_gtk/-/commit/38361e7c8d644b10d9b6747c26eeec2b50d42845
Patch0001:      0001-use-usize-where-possible.patch
# https://gitlab.com/news-flash/news_flash_gtk/-/issues/74
# https://gitlab.com/news-flash/news_flash_gtk/-/commit/dfea2df583a9995796bc7ac01f6048d47f35393a
Patch0002:      0001-dont-inhibit-all-key-press-signals-in-webview.patch
# https://gitlab.com/news-flash/news_flash_gtk/-/issues/77
# https://gitlab.com/news-flash/news_flash_gtk/-/commit/2a9405ea8148329fa8973b7d7098a8b6ba6495a8
Patch0003:      0001-dont-call-show_all-in-app-constructor.patch

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
  -e 's/news-flash = .*/news-flash = "1"/' \
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
