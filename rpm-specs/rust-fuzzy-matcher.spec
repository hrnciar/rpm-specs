# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate fuzzy-matcher

Name:           rust-%{crate}
Version:        0.3.7
Release:        1%{?dist}
Summary:        Fuzzy Matching Library

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/fuzzy-matcher
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Fuzzy Matching Library.}

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

%package     -n %{name}+compact-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compact-devel %{_description}

This package contains library source intended for building other packages
which use "compact" feature of "%{crate}" crate.

%files       -n %{name}+compact-devel
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
* Sun Oct 04 2020 Fabio Valentini <decathorpe@gmail.com> - 0.3.7-1
- Update to version 0.3.7.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Josh Stone <jistone@redhat.com> - 0.3.5-1
- Update to 0.3.5

* Sun Feb 23 10:33:39 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.3.4-1
- Update to 0.3.4

* Thu Feb 06 2020 Josh Stone <jistone@redhat.com> - 0.3.3-1
- Update to 0.3.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Josh Stone <jistone@redhat.com> - 0.3.1-1
- Update to 0.3.1

* Thu Dec 05 18:19:12 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.2-1
- Release 0.2.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 18:56:04 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-3
- Regenerate

* Tue Apr 23 15:07:33 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-2
- Run tests in infrastructure

* Sun Apr 14 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.1-1
- Initial package
