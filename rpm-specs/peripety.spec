Name:           peripety
Version:        0.1.2
Release:        9%{?dist}
Summary:        Storage event notification daemon
License:        MIT
URL:            https://github.com/cathay4t/peripety
Source0:        https://github.com/cathay4t/peripety/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/cathay4t/peripety/pull/6
Patch0001:      0001-Be-more-specific-about-dependencies.patch
ExclusiveArch:  %{rust_arches}
BuildRequires:  rust-packaging
%{?systemd_requires}
BuildRequires:  systemd systemd-devel
# src/peripety/Cargo.toml
BuildRequires:  (crate(libc/default) >= 0.2.0 with crate(libc/default) < 0.3.0)
BuildRequires:  (crate(regex/default) >= 1.0.0 with crate(regex/default) < 2.0.0)
BuildRequires:  (crate(serde/default) >= 1.0.0 with crate(serde/default) < 2.0.0)
BuildRequires:  (crate(serde_derive/default) >= 1.0.0 with crate(serde_derive/default) < 2.0.0)
BuildRequires:  (crate(serde_json/default) >= 1.0.0 with crate(serde_json/default) < 2.0.0)
# src/peripetyd/Cargo.toml
BuildRequires:  (crate(chrono/default) >= 0.4.0 with crate(chrono/default) < 0.5.0)
BuildRequires:  (crate(libc/default) >= 0.2.0 with crate(libc/default) < 0.3.0)
BuildRequires:  (crate(nix/default) >= 0.14.0 with crate(nix/default) < 0.15.0)
BuildRequires:  (crate(regex/default) >= 1.0.0 with crate(regex/default) < 2.0.0)
BuildRequires:  (crate(serde/default) >= 1.0.0 with crate(serde/default) < 2.0.0)
BuildRequires:  (crate(serde_derive/default) >= 1.0.46 with crate(serde_derive/default) < 2.0.0)
BuildRequires:  (crate(toml/default) >= 0.5.0 with crate(toml/default) < 0.6.0)
# src/prpt/Cargo.toml
BuildRequires:  (crate(chrono/default) >= 0.4.0 with crate(chrono/default) < 0.5.0)
BuildRequires:  (crate(clap/default) >= 2.31.2 with crate(clap/default) < 3.0.0)
BuildRequires:  (crate(nix/default) >= 0.14.0 with crate(nix/default) < 0.15.0)
# src/sdjournal/Cargo.toml
BuildRequires:  (crate(libc/default) >= 0.2.30 with crate(libc/default) < 0.3.0)

%description
Peripety is designed to parse system storage logging into structured storage
event helping user investigate storage issues.

%prep
%autosetup -p1
%cargo_prep

%build
%cargo_build

%install
%make_install

%files
%doc README.md
%license LICENSE
%{_bindir}/prpt
%{_bindir}/peripetyd
%{_mandir}/man1/prpt.1*
%config(noreplace) %{_sysconfdir}/peripetyd.conf
%{_unitdir}/peripetyd.service

%post
%systemd_post peripetyd.service

%preun
%systemd_preun peripetyd.service

%postun
%systemd_postun_with_restart peripetyd.service

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-6
- Rework spec to be more rusty

* Sat Jul 13 2019 Gris Ge <fge@redhat.com> - 0.1.2-5
- Fix missing dependency.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Gris Ge <fge@redhat.com> - 0.1.2-3
- Fix cargo dependency.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 Gris Ge <fge@redhat.com> - 0.1.2-1
- Initial release.
