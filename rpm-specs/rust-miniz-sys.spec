# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate miniz-sys

Name:           rust-%{crate}
Version:        0.1.12
Release:        4%{?dist}
Summary:        Bindings to the miniz library

# miniz is Public Domain
# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/miniz-sys
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Bindings to the miniz.c library.}

%description %{_description}

%package        devel
Summary:        %{summary}
# https://github.com/alexcrichton/flate2-rs/issues/143
Provides:       bundled(miniz) = 2.0.7
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 11:24:07 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.12-2
- Regenerate

* Sat Jun 01 2019 Josh Stone <jistone@redhat.com> - 0.1.12-1
- Update to 0.1.12

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.11-3
- Run tests in infrastructure

* Sun Nov 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.11-2
- Adapt to new packaging

* Mon Oct 22 2018 Josh Stone <jistone@redhat.com> - 0.1.11-1
- Update to 0.1.11

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.10-1
- Initial package
