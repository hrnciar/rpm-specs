# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate tokio-reactor

Name:           rust-%{crate}
Version:        0.1.12
Release:        1%{?dist}
Summary:        Event loop that drives Tokio I/O resources

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/tokio-reactor
Source:         %{crates_source}
# Initial patched metadata
# * Don't pin exact dependencies
# * Update parking_lot to 0.10
Patch0:         tokio-reactor-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Event loop that drives Tokio I/O resources.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc CHANGELOG.md README.md
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
* Thu Feb 06 2020 Josh Stone <jistone@redhat.com> - 0.1.12-1
- Update to 0.1.12

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 12:13:22 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.11-2
- Update parking_lot to 0.10

* Fri Dec 13 2019 Josh Stone <jistone@redhat.com> - 0.1.11-1
- Update to 0.1.11

* Sat Nov 23 2019 Josh Stone <jistone@redhat.com> - 0.1.10-1
- Update to 0.1.10

* Sun Aug 04 15:57:52 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.9-6
- Really build

* Sun Aug 04 15:40:06 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.9-1
- Update parking_lot to 0.9

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 19:28:17 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.9-3
- Regenerate

* Mon May 06 22:01:18 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.9-2
- Update parking_lot to 0.8

* Mon Mar 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Sat Dec 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7

* Fri Nov 09 2018 Josh Stone <jistone@redhat.com> - 0.1.6-3
- Enable checks

* Thu Nov 08 2018 Josh Stone <jistone@redhat.com> - 0.1.6-2
- Adapt to new packaging

* Thu Sep 27 2018 Josh Stone <jistone@redhat.com> - 0.1.6-1
- Initial package