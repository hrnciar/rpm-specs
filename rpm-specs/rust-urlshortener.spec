# Generated by rust2rpm 13
# * Tests require network
%bcond_with check
%global debug_package %{nil}

%global crate urlshortener

Name:           rust-%{crate}
Version:        3.0.0
Release:        1%{?dist}
Summary:        Very simple url shortener client library

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/urlshortener
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Very simple url shortener client library.}

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

%package     -n %{name}+client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+client-devel %{_description}

This package contains library source intended for building other packages
which use "client" feature of "%{crate}" crate.

%files       -n %{name}+client-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+reqwest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+reqwest-devel %{_description}

This package contains library source intended for building other packages
which use "reqwest" feature of "%{crate}" crate.

%files       -n %{name}+reqwest-devel
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
* Sat Mar 07 2020 Josh Stone <jistone@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Sun Feb 16 13:11:36 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1

* Sun Feb 16 11:12:58 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.1.0-3
- Update reqwest to 0.10

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Josh Stone <jistone@redhat.com> - 2.1.0-1
- Update to 2.1.0

* Thu Dec 05 14:44:09 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 16:55:41 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.0-2
- Regenerate

* Fri Mar 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Fri Mar 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-1
- Initial package
