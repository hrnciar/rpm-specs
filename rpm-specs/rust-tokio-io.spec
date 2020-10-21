# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate tokio-io

Name:           rust-%{crate}
Version:        0.1.13
Release:        3%{?dist}
Summary:        Core I/O primitives for asynchronous I/O in Rust

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/tokio-io
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Core I/O primitives for asynchronous I/O in Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md CHANGELOG.md
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
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 2020 Josh Stone <jistone@redhat.com> - 0.1.13-1
- Update to 0.1.13

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 19:51:19 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.12-2
- Regenerate

* Mon Mar 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.12-1
- Update to 0.1.12

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.1.11-1
- Update to 0.1.11

* Sun Nov 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.10-2
- Adapt to new packaging

* Thu Oct 25 2018 Josh Stone <jistone@redhat.com> - 0.1.10-1
- Update to 0.1.10

* Fri Sep 28 2018 Josh Stone <jistone@redhat.com> - 0.1.9-1
- Update to 0.1.9

* Sat Sep 08 2018 Josh Stone <jistone@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7

* Thu May 03 2018 Josh Stone <jistone@redhat.com> - 0.1.6-2
- Stop using deprecated APIs

* Fri Mar 09 2018 Josh Stone <jistone@redhat.com> - 0.1.6-1
- Update to 0.1.6

* Thu Feb 08 2018 Josh Stone <jistone@redhat.com> - 0.1.5-1
- Update to 0.1.5

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-2
- Rebuild for rust-packaging v5

* Wed Nov 22 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Fri Jun 16 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-1
- Initial package
