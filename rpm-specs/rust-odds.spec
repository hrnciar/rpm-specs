# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate odds

Name:           rust-%{crate}
Version:        0.4.0
Release:        1%{?dist}
Summary:        Odds and ends — collection miscellania

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/odds
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Odds and ends — collection miscellania. Extra functionality for slices
(`.find()`, `RevSlice`), strings and other things. Things in odds may move to
more appropriate crates if we find them.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.rst
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+docs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+docs-devel %{_description}

This package contains library source intended for building other packages
which use "docs" feature of "%{crate}" crate.

%files       -n %{name}+docs-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-string-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-string-devel %{_description}

This package contains library source intended for building other packages
which use "std-string" feature of "%{crate}" crate.

%files       -n %{name}+std-string-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-vec-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-vec-devel %{_description}

This package contains library source intended for building other packages
which use "std-vec" feature of "%{crate}" crate.

%files       -n %{name}+std-vec-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages
which use "unstable" feature of "%{crate}" crate.

%files       -n %{name}+unstable-devel
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
* Tue Apr 14 2020 Josh Stone <jistone@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Thu Feb 20 2020 Josh Stone <jistone@redhat.com> - 0.3.1-4
- Bump dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 17:05:59 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-1
- Initial package