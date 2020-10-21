# Generated by rust2rpm 15
# * Missing webpki
%bcond_with check
%global debug_package %{nil}

%global crate awc

Name:           rust-%{crate}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Async HTTP client library that uses the Actix runtime

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/awc
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Async HTTP client library that uses the Actix runtime.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md CHANGES.md
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
* Mon Sep 21 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.0-1
- Update to version 2.0.0.

* Sat Aug 29 08:43:05 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.0.0~beta.3-1
- Update to 2.0.0-beta.3

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0~alpha.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0~alpha.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 12:35:20 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.0.0~alpha.2-1
- Update to 2.0.0-alpha.2

* Sun Mar 15 09:18:50 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.0.0~alpha.1-1
- Update to 2.0.0-alpha.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 18:54:21 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-2
- Regenerate

* Sun Dec 15 08:48:23 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Fri Dec 13 20:30:47 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Sun Sep 01 17:22:59 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.4-1
- Update to 0.2.4

* Sat Aug 03 13:46:21 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 06 11:32:50 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2

* Tue Jun 18 11:20:33 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-2
- Update derive_more to 0.15

* Wed Jun 05 17:45:35 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Fri May 31 18:57:01 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-1
- Initial package
