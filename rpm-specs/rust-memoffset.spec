# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate memoffset

Name:           rust-%{crate}
Version:        0.5.4
Release:        1%{?dist}
Summary:        Offset_of functionality for Rust structs

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/memoffset
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Offset_of functionality for Rust structs.}

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

%package     -n %{name}+unstable_const-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable_const-devel %{_description}

This package contains library source intended for building other packages
which use "unstable_const" feature of "%{crate}" crate.

%files       -n %{name}+unstable_const-devel
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
* Tue Mar 17 16:46:04 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.5.4-1
- Update to 0.5.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Josh Stone <jistone@redhat.com> - 0.5.3-1
- Update to 0.5.3

* Fri Aug 30 08:55:30 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 23:29:12 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-7
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-5
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-4
- Run tests in infrastructure

* Fri Sep 07 2018 Josh Stone <jistone@redhat.com> - 0.2.1-3
- Fix a const_err FTBFS

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-1
- Initial package
