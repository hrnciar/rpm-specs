# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate ctrlc

Name:           rust-%{crate}
Version:        3.1.4
Release:        1%{?dist}
Summary:        Easy Ctrl-C handler for Rust projects

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/ctrlc
Source:         %{crates_source}
# Initial patched metadata
# * No Windows deps
Patch0:         ctrlc-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Easy Ctrl-C handler for Rust projects.}

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
%exclude %{cargo_registry}/%{crate}-%{version_no_tilde}/appveyor.yml

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+termination-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+termination-devel %{_description}

This package contains library source intended for building other packages
which use "termination" feature of "%{crate}" crate.

%files       -n %{name}+termination-devel
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
* Fri Feb 21 2020 Josh Stone <jistone@redhat.com> - 3.1.4-1
- Update to 3.1.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 11:03:51 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.3-2
- Regenerate

* Sun Jun 09 13:56:41 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.3-1
- Update to 3.1.3

* Tue Jun 04 2019 Josh Stone <jistone@redhat.com> - 3.1.2-2
- Bump nix to 0.14

* Wed Apr 24 08:33:38 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.2-1
- Update to 3.1.2

* Mon Feb 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.1-4
- Update nix to 0.13

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Josh Stone <jistone@redhat.com> - 3.1.1-2
- Adapt to new packaging

* Tue Jul 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.0-3
- Bump nix to 0.10

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.3-2
- Rebuild for rust-packaging v5

* Thu Jan 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.3-1
- Initial package
