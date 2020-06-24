# Generated by rust2rpm 12
%bcond_without check
%global debug_package %{nil}

%global crate inotify-sys

Name:           rust-%{crate}
Version:        0.1.3
Release:        5%{?dist}
Summary:        Inotify bindings for the Rust programming language

# Upstream license specification: ISC
# https://github.com/inotify-rs/inotify-sys/issues/12
License:        ISC
URL:            https://crates.io/crates/inotify-sys
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Inotify bindings for the Rust programming language.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 10:26:17 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-4
- Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 10:24:32 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-2
- Regenerate

* Mon Mar 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-1
- Initial package