# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate tiff

Name:           rust-%{crate}
Version:        0.5.0
Release:        1%{?dist}
Summary:        TIFF decoding and encoding library in pure Rust

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/tiff
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
TIFF decoding and encoding library in pure Rust.}

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
# Test files are missing
%cargo_test -- --doc
%endif

%changelog
* Thu Jun 11 2020 Josh Stone <jistone@redhat.com> - 0.5.0-1
- Update to 0.5.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Josh Stone <jistone@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Fri Nov 22 2019 Josh Stone <jistone@redhat.com> - 0.3.1-2
- Bump to num-derive 0.3

* Sun Sep 01 20:58:56 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 10:28:28 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-2
- Regenerate

* Fri Mar 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-1
- Initial package
