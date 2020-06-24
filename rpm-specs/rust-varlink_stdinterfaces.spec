# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate varlink_stdinterfaces

Name:           rust-%{crate}
Version:        11.0.0
Release:        2%{?dist}
Summary:        Varlink common interfaces

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/varlink_stdinterfaces
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Varlink common interfaces.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 15:09:20 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 11.0.0-1
- Update to 11.0.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 2019 Harald Hoyer <harald@redhat.com> - 8.0.0-1
- Update to 8.0.0

* Sat Feb 16 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.0.0-1
- Update to 7.0.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Josh Stone <jistone@redhat.com> - 5.0.4-1
- Update to 5.0.4

* Mon Nov 26 2018 Josh Stone <jistone@redhat.com> - 5.0.3-1
- Update to 5.0.3

* Sat Nov 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.0.2-2
- Adapt to new packaging

* Tue Oct 09 2018 Josh Stone <jistone@redhat.com> - 5.0.2-1
- Update to 5.0.2

* Mon Oct 08 2018 Josh Stone <jistone@redhat.com> - 5.0.1-1
- Update to 5.0.1

* Sun Sep 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.0.0-1
- Update to 5.0.0

* Sat Aug 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-1
- Initial package
