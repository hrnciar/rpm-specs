# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate tokio-core

Name:           rust-%{crate}
Version:        0.1.17
Release:        12%{?dist}
Summary:        Core I/O and event loop primitives for asynchronous I/O in Rust

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/tokio-core
Source:         %{crates_source}
# Initial patched metadata
# * Update scoped-tls to 1
Patch0:         tokio-core-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Core I/O and event loop primitives for asynchronous I/O in Rust. Foundation for
the rest of the tokio crates.}

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
%{cargo_registry}/%{crate}-%{version}/
%exclude %{cargo_registry}/%{crate}-%{version}/appveyor.yml

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
# deny(warnings) is just bad
sed -i -e '/deny(warnings)/d' src/lib.rs
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 19:30:09 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.17-10
- Regenerate

* Sun Apr 21 07:11:40 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.17-9
- Update scoped-tls to 1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.1.17-7
- Allow deprecated warnings

* Fri Nov 09 2018 Josh Stone <jistone@redhat.com> - 0.1.17-6
- Adapt to new packaging

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.17-5
- Rebuild to trigger tests

* Sat Jul 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.17-4
- Rebuild to trigger tests

* Sat Jul 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.17-3
- Run tests in infrastructure

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.17-1
- Update to 0.1.17

* Fri Mar 23 2018 Josh Stone <jistone@redhat.com> - 0.1.16-1
- Update to 0.1.16

* Mon Mar 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.15-1
- Update to 0.1.15

* Fri Mar 09 2018 Josh Stone <jistone@redhat.com> - 0.1.12-3
- Use an explicit call to resolve tokio-io conflict

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.12-1
- Update to 0.1.12

* Fri Jun 16 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.8-1
- Initial package