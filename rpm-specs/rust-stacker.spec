# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate stacker

Name:           rust-%{crate}
Version:        0.1.12
Release:        1%{?dist}
Summary:        Stack growth library useful when implementing deeply recursive algorithms

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/stacker
Source:         %{crates_source}
# Initial patched metadata
# * No windows
Patch0:         stacker-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Stack growth library useful when implementing deeply recursive algorithms that
may accidentally blow the stack.}

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
* Sun Sep 20 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.12-1
- Update to version 0.1.12.

* Wed Aug 26 2020 Josh Stone <jistone@redhat.com> - 0.1.11-1
- Update to 0.1.11

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Josh Stone <jistone@redhat.com> - 0.1.9-1
- Update to 0.1.9

* Tue May 05 2020 Josh Stone <jistone@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Mon Mar 30 08:09:53 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Josh Stone <jistone@redhat.com> - 0.1.6-1
- Update to 0.1.6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-1
- Initial package
