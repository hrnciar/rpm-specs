# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate alga

Name:           rust-%{crate}
Version:        0.9.3
Release:        1%{?dist}
Summary:        Abstract algebra for Rust

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/alga
Source:         %{crates_source}
# Initial patched metadata
# * Update quickcheck to 0.9, https://github.com/rustsim/alga/pull/95
Patch0:         alga-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Abstract algebra for Rust.}

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

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+decimal-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+decimal-devel %{_description}

This package contains library source intended for building other packages
which use "decimal" feature of "%{crate}" crate.

%files       -n %{name}+decimal-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
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
* Mon Mar 02 16:56:53 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.9.3-1
- Update to 0.9.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.9.2-2
- Indirectly update to libm 0.2

* Fri Nov 15 2019 Josh Stone <jistone@redhat.com> - 0.9.2-1
- Update to 0.9.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 21:13:34 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1

* Thu Apr 04 07:58:28 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.2-1
- Update to 0.8.2

* Mon Feb 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.2-1
- Update to 0.7.2

* Tue Sep 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-1
- Initial package
