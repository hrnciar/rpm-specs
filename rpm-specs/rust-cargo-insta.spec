# Generated by rust2rpm 13
%bcond_without check
%global __cargo_skip_build 0

%global crate cargo-insta

Name:           rust-%{crate}
Version:        0.16.0
Release:        2%{?dist}
Summary:        Review tool for the insta snapshot testing library for Rust

# Upstream license specification: Apache-2.0
# * https://github.com/mitsuhiko/insta/issues/125
License:        ASL 2.0
URL:            https://crates.io/crates/cargo-insta
Source:         %{crates_source}
# Initial patched metadata
# * https://github.com/mitsuhiko/insta/pull/124
# - Bump 'console' to 0.11.0
Patch0:         cargo-insta-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Review tool for the insta snapshot testing library for Rust.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# ASL 2.0
# ASL 2.0 or Boost
# MIT
# MIT or ASL 2.0
# Unlicense or MIT
License:        MIT and ASL 2.0

%description -n %{crate} %{_description}

%files       -n %{crate}
%doc README.md
%{_bindir}/cargo-insta

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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 23:56:08 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.16.0-1
- Initial package
