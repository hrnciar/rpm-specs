# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate assert_fs

Name:           rust-%{crate}
Version:        1.0.0
Release:        2%{?dist}
Summary:        Filesystem fixtures and assertions for testing

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/assert_fs
Source:         %{crates_source}
# Initial patched metadata
# * Update globwalk to 0.8, https://github.com/assert-rs/assert_fs/pull/57
Patch0:         assert_fs-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Filesystem fixtures and assertions for testing.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
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
* Sun Mar 29 16:30:50 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.0-2
- Update globwalk to 0.8

* Fri Mar 27 11:03:45 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Wed Mar 04 12:57:53 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.1-1
- Initial package
