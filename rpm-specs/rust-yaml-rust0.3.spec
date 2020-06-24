# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate yaml-rust

Name:           rust-%{crate}0.3
Version:        0.3.5
Release:        15%{?dist}
Summary:        YAML 1.2 parser for rust

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/yaml-rust
Source:         %{crates_source}
# Initial patched metadata
# * latest linked-hash-map, https://github.com/chyh1990/yaml-rust/commit/b2ebf74c2f6dfcc081c3bead1a70ca59ae2e576c#diff-80398c5faae3c069e4e6aa2ed11b28c0
# * Exclude CI files
Patch0:         yaml-rust-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Missing YAML 1.2 parser for rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clippy-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+clippy-devel %{_description}

This package contains library source intended for building other packages
which use "clippy" feature of "%{crate}" crate.

%files       -n %{name}+clippy-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+linked-hash-map-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+linked-hash-map-devel %{_description}

This package contains library source intended for building other packages
which use "linked-hash-map" feature of "%{crate}" crate.

%files       -n %{name}+linked-hash-map-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+preserve_order-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+preserve_order-devel %{_description}

This package contains library source intended for building other packages
which use "preserve_order" feature of "%{crate}" crate.

%files       -n %{name}+preserve_order-devel
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
* Tue Feb 18 04:04:49 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.3.5-15
- Disable tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 19:36:57 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.5-12
- Regenerate

* Sun Jul 14 12:12:50 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.5-11
- Regenerate

* Sun Mar 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.5-10
- Do not pull optional dependencies

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.5-8
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.5-7
- Run tests in infrastructure

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenko@redhat.com> - 0.3.5-4
- Rebuild for rust-packaging v5

* Thu Nov 09 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.5-3
- Exclude unneeded files

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.5-2
- Port to use rust-packaging

* Sat Feb 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.5-1
- Initial package
