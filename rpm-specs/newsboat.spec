# Not all test dependencies are packaged for fedora
%bcond_with check

Name:    newsboat
Version: 2.21
Release: 1%{?dist}
Summary: RSS/Atom feed reader for the text console

License: MIT
URL:     https://www.newsboat.org
Source0: https://newsboat.org/releases/%{version}/%{name}-%{version}.tar.xz
Source1: https://newsboat.org/releases/%{version}/%{name}-%{version}.tar.xz.asc
Source2: https://newsboat.org/newsboat.pgp

Patch:  make-do-not-require-Cargo-lock.patch

# Source file verification
BuildRequires: gnupg2

BuildRequires: asciidoctor
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: pkgconfig
BuildRequires: pkgconfig(json-c) >= 0.11
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(ncursesw)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(stfl)
# Rust parts
BuildRequires:  git
BuildRequires:  rust-packaging
# libnewsboat
BuildRequires: (crate(chrono/default) >= 0.4.0 with crate(chrono/default) < 0.5.0)
BuildRequires: (crate(clap) >= 2.33.0 with crate(clap) < 3.0.0)
BuildRequires: (crate(curl-sys/default) >= 0.4.5 with crate(curl-sys/default) < 0.5.0)
BuildRequires: (crate(gettext-rs/default) >= 0.5.0 with crate(gettext-rs/default) < 0.6.0)
BuildRequires: (crate(gettext-sys/default) >= 0.19.9 with crate(gettext-sys/default) < 0.20.0)
BuildRequires: (crate(gettext-sys/gettext-system) >= 0.19.9 with crate(gettext-sys/gettext-system) < 0.20.0)
BuildRequires: (crate(lazy_static/default) >= 1.4.0 with crate(lazy_static/default) < 2.0.0)
BuildRequires: (crate(libc/default) >= 0.2.0 with crate(libc/default) < 0.3.0)
BuildRequires: (crate(natord/default) >= 1.0.9 with crate(natord/default) < 2.0.0)
BuildRequires: (crate(nom/default) >= 5.0.0 with crate(nom/default) < 6.0.0)
BuildRequires: (crate(once_cell/default) >= 1.4.1 with crate(once_cell/default) < 2.0.0)
BuildRequires: (crate(percent-encoding/default) >= 2.0.0 with crate(percent-encoding/default) < 3.0.0)
BuildRequires: (crate(rand/default) >= 0.7.0 with crate(rand/default) < 0.8.0)
BuildRequires: (crate(unicode-width/default) >= 0.1.8 with crate(unicode-width/default) < 0.2.0)
BuildRequires: (crate(url/default) >= 2.0.0 with crate(url/default) < 3.0.0)
BuildRequires: (crate(xdg/default) >= 2.2.0 with crate(xdg/default) < 3.0.0)
BuildRequires: crate(backtrace/default) >= 0.3.0
%if %{with check}
BuildRequires: (crate(section_testing/default) >= 0.0.4 with crate(section_testing/default) < 0.0.5)
BuildRequires: (crate(tempfile/default) >= 3.0.0 with crate(tempfile/default) < 4.0.0)
BuildRequires: crate(proptest/default) >= 0.9.6
%endif
# libnewsboat-ffi
BuildRequires: (crate(libc/default) >= 0.2.0 with crate(libc/default) < 0.3.0)
# strprintf
BuildRequires: (crate(libc/default) >= 0.2.0 with crate(libc/default) < 0.3.0)
# regex-rs
BuildRequires: (crate(bitflags/default) >= 1.2.0 with crate(bitflags/default) < 2.0.0)
BuildRequires: (crate(gettext-rs/default) >= 0.5.0 with crate(gettext-rs/default) < 0.6.0)
BuildRequires: crate(libc/default) >= 0.2.69

Provides: podboat = %{version}-%{release}

%description
Newsboat is a fork of Newsbeuter, an RSS/Atom feed reader for the text console.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
%cargo_prep
# Remove executable bit from example scripts
find contrib/ -type f -exec chmod -x '{}' +

%build
# Respect RPM settings
%set_build_flags
# Do not fail build because our GCC emits different warnings
export CFLAGS="-Wno-error ${CFLAGS}" CXXFLAGS="-Wno-error ${CXXFLAGS}"
# CARGO_FLAGS is used/appended to by this Makefile
export CARGO_FLAGS="%{__cargo_common_opts}"

# Verify non-rust deps and setup LDFLAGS
sh config.sh

# Build the project
# Replace bare `cargo` with the one used by %%cargo_* macros
%make_build CARGO="%{__cargo}" all %{?with_check:test}

%install
%make_install prefix="%{_prefix}"

%find_lang %{name}

%check
%if %{with check}
# TMPDIR=%%{_tmppath} ./test/test  # Have issues with permission in tpmdir
%cargo_test
%endif

%files -f %{name}.lang
%license LICENSE
%doc README.md

%{_bindir}/newsboat
%{_bindir}/podboat

%{_mandir}/man1/newsboat.1*
%{_mandir}/man1/podboat.1*
%{_pkgdocdir}
%{_datadir}/icons/hicolor/scalable/apps/newsboat.svg

%changelog
* Tue Oct 20 2020 Jan Staněk <jstanek@redhat.com> - 2.21-1
- Upgrade to version 2.21

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jan Staněk <jstanek@redhat.com> - 2.20.1-1
- Upgrade to version 2.20.1

* Mon Jun 22 2020 Jan Staněk <jstanek@redhat.com> - 2.20-1
- Upgrade to version 2.20, remove upstreamed patches
- Enable source GPG signature verification

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 2.19-3
- Rebuild (json-c)

* Mon Apr 13 2020 Björn Esser <besser82@fedoraproject.org> - 2.19-2
- Add support for upcoming json-c 0.14.0

* Mon Mar 23 2020 Jan Staněk <jstanek@redhat.com> - 2.19-1
- Upgrade to version 2.19

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Jan Staněk <jstanek@redhat.com> - 2.17.1-1
- Upgrade to version 2.17.1

* Mon Sep 23 2019 Jan Staněk <jstanek@redhat.com> - 2.17-1
- Upgrade to version 2.17

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Jan Staněk <jstanek@redhat.com> - 2.16.1-2
- Import upstream fix for evaluated commands in configuration comments

* Thu Jun 27 2019 Jan Staněk <jstanek@redhat.com> - 2.16.1-1
- Upgrade to version 2.16.1
- Add %%check section

* Mon Mar 25 2019 Jan Staněk <jstanek@redhat.com> - 2.15-1
- Upgrade to version 2.15

* Mon Feb 18 2019 Jan Staněk <jstanek@redhat.com> - 2.14.1-1
- Upgrade to version 2.14.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Lee Keitel <keitellf@fedoraproject.org> - 2.12-1
- Bumped version to 2.12

* Wed Jun 13 2018 Lee Keitel <keitellf@fedoraproject.org> - 2.11.1-1
- Initial version 2.11.1
