# Generated by rust2rpm 15
%bcond_without check
%global debug_package %{nil}

%global crate actix-web

Name:           rust-%{crate}
Version:        3.1.0
Release:        1%{?dist}
Summary:        Powerful, pragmatic, and extremely fast web framework for Rust

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/actix-web
Source:         %{crates_source}
# Initial patched metadata
# * add missing test dependencies (missing from processed Cargo.toml)
Patch0:         actix-web-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Actix web is a powerful, pragmatic, and extremely fast web framework for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md CHANGES.md MIGRATION.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+compress-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compress-devel %{_description}

This package contains library source intended for building other packages
which use "compress" feature of "%{crate}" crate.

%files       -n %{name}+compress-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+open-ssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+open-ssl-devel %{_description}

This package contains library source intended for building other packages
which use "open-ssl" feature of "%{crate}" crate.

%files       -n %{name}+open-ssl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+openssl-devel %{_description}

This package contains library source intended for building other packages
which use "openssl" feature of "%{crate}" crate.

%files       -n %{name}+openssl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rust-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rust-tls-devel %{_description}

This package contains library source intended for building other packages
which use "rust-tls" feature of "%{crate}" crate.

%files       -n %{name}+rust-tls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rustls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustls-devel %{_description}

This package contains library source intended for building other packages
which use "rustls" feature of "%{crate}" crate.

%files       -n %{name}+rustls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+secure-cookies-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+secure-cookies-devel %{_description}

This package contains library source intended for building other packages
which use "secure-cookies" feature of "%{crate}" crate.

%files       -n %{name}+secure-cookies-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Oct 07 2020 Fabio Valentini <decathorpe@gmail.com> - 3.1.0-1
- Update to version 3.1.0.

* Mon Sep 21 2020 Fabio Valentini <decathorpe@gmail.com> - 3.0.2-1
- Update to version 3.0.2.

* Sat Aug 29 08:41:00 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.0.0~beta.3-1
- Update to 3.0.0-beta.3

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0~alpha.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0~alpha.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 12:30:02 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.0.0~alpha.3-1
- Update to 3.0.0-alpha.3

* Thu May 14 22:44:25 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.0.0~alpha.2-1
- Update to 3.0.0-alpha.2

* Thu May 14 19:40:08 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0~rc-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 18:44:27 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0~rc-2
- Regenerate

* Fri Dec 20 13:20:35 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0~rc-1
- Update to 2.0.0~rc

* Mon Dec 16 08:08:31 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0~alpha.6-1
- Update to 2.0.0~alpha.6

* Sat Dec 14 00:51:38 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.0~alpha.5-1
- Update to 2.0.0~alpha.5

* Sun Sep 01 17:16:23 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7

* Tue Aug 06 10:01:45 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 11:56:48 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Tue Jun 18 08:39:38 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Wed Jun 05 17:52:04 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Fri May 31 19:20:55 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0~rc-1
- Initial package
