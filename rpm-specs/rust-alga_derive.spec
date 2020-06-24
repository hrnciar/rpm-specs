# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate alga_derive

Name:           rust-%{crate}
Version:        0.9.2
Release:        1%{?dist}
Summary:        Derive attribute for implementing algebraic traits from the alga crate

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/alga_derive
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Derive attribute for implementing algebraic traits from the alga crate.}

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
%cargo_test
%endif

%changelog
* Mon Mar 02 17:08:31 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.9.2-1
- Update to 0.9.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 17:15:20 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.9.1-3
- Bump quickcheck to 0.9

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 21:14:31 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1

* Thu Apr 04 08:02:48 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.2-1
- Update to 0.8.2

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-2
- Update quickcheck to 0.8

* Mon Feb 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-1
- UPdate to 0.8.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-2
- Adapt to new packaging

* Mon Sep 17 2018 Josh Stone <jistone@redhat.com> - 0.7.1-1
- Update to 0.7.1

* Mon Sep 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-1
- Initial package