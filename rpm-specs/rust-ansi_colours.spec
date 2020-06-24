# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate ansi_colours

Name:           rust-%{crate}
Version:        1.0.1
Release:        6%{?dist}
Summary:        True-colour ↔ ANSI terminal palette converter

# Upstream license specification: LGPL-3.0-or-later
# FIXME: Upstream uses unknown SPDX tag LGPL-3.0-or-later!
License:        LGPLv3+
URL:            https://crates.io/crates/ansi_colours
Source:         %{crates_source}
# Initial patched metadata
# * Bump lab to 0.7, https://github.com/mina86/ansi_colours/commit/7a0e18b5b55b1b5ca378a198b56f3793c5e5f81d
Patch0:         ansi_colours-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
True-colour ↔ ANSI terminal palette converter.}

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
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 19:02:10 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-4
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-2
- Adapt to new packaging

* Thu Oct 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-1
- Initial package
