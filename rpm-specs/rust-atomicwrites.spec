# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate atomicwrites

Name:           rust-%{crate}
Version:        0.2.5
Release:        2%{?dist}
Summary:        Atomic file-writes

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/atomicwrites
Source:         %{crates_source}
# Initial patched metadata
# - Remove Windows-only dependencies
Patch0:         atomicwrites-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Atomic file-writes.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%license LICENSE
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Josh Stone <jistone@redhat.com> - 0.2.5-1
- Update to 0.2.5

* Wed Sep 11 22:53:14 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.4-1
- Update to 0.2.4 (#1750822)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 17:43:13 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3

* Wed Jun 05 2019 Josh Stone <jistone@redhat.com> - 0.2.2-3
- Bump nix to 0.14

* Tue Apr 23 15:02:56 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-2
- Run tests in infrastructure

* Sat Apr 13 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.2-1
- Initial package