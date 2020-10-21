# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate gstreamer-audio

Name:           rust-%{crate}
Version:        0.16.4
Release:        1%{?dist}
Summary:        Rust bindings for GStreamer Audio library

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/gstreamer-audio
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust bindings for GStreamer Audio library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%license LICENSE-APACHE LICENSE-MIT
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dox-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dox-devel %{_description}

This package contains library source intended for building other packages
which use "dox" feature of "%{crate}" crate.

%files       -n %{name}+dox-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+embed-lgpl-docs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+embed-lgpl-docs-devel %{_description}

This package contains library source intended for building other packages
which use "embed-lgpl-docs" feature of "%{crate}" crate.

%files       -n %{name}+embed-lgpl-docs-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+gstreamer-rs-lgpl-docs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gstreamer-rs-lgpl-docs-devel %{_description}

This package contains library source intended for building other packages
which use "gstreamer-rs-lgpl-docs" feature of "%{crate}" crate.

%files       -n %{name}+gstreamer-rs-lgpl-docs-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+purge-lgpl-docs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+purge-lgpl-docs-devel %{_description}

This package contains library source intended for building other packages
which use "purge-lgpl-docs" feature of "%{crate}" crate.

%files       -n %{name}+purge-lgpl-docs-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_10-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v1_10-devel %{_description}

This package contains library source intended for building other packages
which use "v1_10" feature of "%{crate}" crate.

%files       -n %{name}+v1_10-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_12-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v1_12-devel %{_description}

This package contains library source intended for building other packages
which use "v1_12" feature of "%{crate}" crate.

%files       -n %{name}+v1_12-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_14-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v1_14-devel %{_description}

This package contains library source intended for building other packages
which use "v1_14" feature of "%{crate}" crate.

%files       -n %{name}+v1_14-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_16-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v1_16-devel %{_description}

This package contains library source intended for building other packages
which use "v1_16" feature of "%{crate}" crate.

%files       -n %{name}+v1_16-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_18-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v1_18-devel %{_description}

This package contains library source intended for building other packages
which use "v1_18" feature of "%{crate}" crate.

%files       -n %{name}+v1_18-devel
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
* Sun Oct 11 2020 Fabio Valentini <decathorpe@gmail.com> - 0.16.4-1
- Update to version 0.16.4.

* Wed Sep 09 2020 Josh Stone <jistone@redhat.com> - 0.16.3-1
- Update to 0.16.3

* Wed Jul 29 2020 Josh Stone <jistone@redhat.com> - 0.16.2-1
- Update to 0.16.2

* Thu Jul 09 2020 Josh Stone <jistone@redhat.com> - 0.16.0-1
- Update to 0.16.0

* Wed Jun 10 2020 Josh Stone <jistone@redhat.com> - 0.15.7-1
- Update to 0.15.7

* Tue May 05 2020 Josh Stone <cuviper@gmail.com> - 0.15.5-1
- Update to 0.15.5

* Mon Feb 17 11:22:30 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.15.3-1
- Update to 0.15.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Josh Stone <jistone@redhat.com> - 0.15.0-1
- Update to 0.15.0

* Tue Dec 10 2019 Josh Stone <jistone@redhat.com> - 0.14.5-1
- Update to 0.14.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 05 19:53:36 EEST 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.0-1
- Initial package
