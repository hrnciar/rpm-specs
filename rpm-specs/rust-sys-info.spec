# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate sys-info

Name:           rust-%{crate}
Version:        0.6.1
Release:        1%{?dist}
Summary:        Get system information in Rust

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/sys-info
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Get system information in Rust.}

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
* Tue May 05 2020 Josh Stone <jistone@redhat.com> - 0.6.1-1
- Update to 0.6.1

* Mon Mar 02 09:07:49 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.5.10-1
- Update to 0.5.10

* Sat Feb 15 11:01:51 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.5.9-1
- Update to 0.5.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 10:24:11 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.8-1
- Update to 0.5.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Josh Stone <jistone@redhat.com> - 0.5.7-1
- Update to 0.5.7

* Sat Mar 09 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.6-5
- Adapt to new packaging

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.6-1
- Update to 0.5.6

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.5-2
- Rebuild for rust-packaging v5

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.5-1
- Update to 0.5.5

* Mon Jan 01 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.4-1
- Update to 0.5.4

* Mon Dec 04 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.3-1
- Initial package