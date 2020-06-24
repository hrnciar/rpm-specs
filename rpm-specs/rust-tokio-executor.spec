# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate tokio-executor

Name:           rust-%{crate}
Version:        0.1.10
Release:        1%{?dist}
Summary:        Future execution primitives

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/tokio-executor
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Future execution primitives.}

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
* Thu Feb 06 2020 Josh Stone <jistone@redhat.com> - 0.1.10-1
- Update to 0.1.10

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Josh Stone <jistone@redhat.com> - 0.1.9-1
- Update to 0.1.9

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 06 11:27:32 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.8-1
- Update to 0.1.8

* Fri Jun 21 22:08:24 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.7-2
- Regenerate

* Sun Mar 24 19:33:00 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7

* Mon Mar 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.6-3
- Adapt to new packaging

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.1.6-1
- Update to 0.1.6

* Thu Nov 08 2018 Josh Stone <jistone@redhat.com> - 0.1.5-2
- Adapt to new packaging

* Fri Sep 28 2018 Josh Stone <jistone@redhat.com> - 0.1.5-1
- Update to 0.1.5

* Sat Sep 08 2018 Josh Stone <jistone@redhat.com> - 0.1.4-1
- Update to 0.1.4

* Wed Aug 08 2018 Josh Stone <jistone@redhat.com> - 0.1.3-1
- Update to 0.1.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Fri Mar 23 2018 Josh Stone <jistone@redhat.com> - 0.1.1-1
- Update to 0.1.1

* Fri Mar 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-1
- Initial package