# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate pangocairo

Name:           rust-%{crate}
Version:        0.9.0
Release:        2%{?dist}
Summary:        Rust bindings for the PangoCairo library

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/pangocairo
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust bindings for the PangoCairo library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/
%exclude %{cargo_registry}/%{crate}-%{version_no_tilde}/{appveyor.yml,Gir.toml,Makefile}

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

%package     -n %{name}+gtk-rs-lgpl-docs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gtk-rs-lgpl-docs-devel %{_description}

This package contains library source intended for building other packages
which use "gtk-rs-lgpl-docs" feature of "%{crate}" crate.

%files       -n %{name}+gtk-rs-lgpl-docs-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+purge-lgpl-docs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+purge-lgpl-docs-devel %{_description}

This package contains library source intended for building other packages
which use "purge-lgpl-docs" feature of "%{crate}" crate.

%files       -n %{name}+purge-lgpl-docs-devel
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.9.0-1
- Update to 0.9.0

* Tue Dec 10 2019 Josh Stone <jistone@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 15:52:41 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Mon Feb 18 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 08 2018 Igor Gnatenko <ignatenko@redhat.com> - 0.5.0-1
- Initial package