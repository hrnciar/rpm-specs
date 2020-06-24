# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate cast

Name:           rust-%{crate}
Version:        0.2.3
Release:        2%{?dist}
Summary:        Ergonomic, checked cast functions for primitive types

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/cast
Source:         %{crates_source}
# Initial patched metadata
# * Remove CI files, https://github.com/japaric/cast.rs/pull/18
Patch0:         cast-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Ergonomic, checked cast functions for primitive types.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+x128-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+x128-devel %{_description}

This package contains library source intended for building other packages
which use "x128" feature of "%{crate}" crate.

%files       -n %{name}+x128-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 08:09:59 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-3
- Fix description

* Fri Nov 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.2-2
- Adapt to new packaging

* Tue Sep 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-1
- Initial package