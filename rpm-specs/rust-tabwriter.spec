# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate tabwriter

Name:           rust-%{crate}
Version:        1.2.1
Release:        2%{?dist}
Summary:        Elastic tabstops

# Upstream license specification: Unlicense/MIT
License:        Unlicense or MIT
URL:            https://crates.io/crates/tabwriter
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Elastic tabstops.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license COPYING LICENSE-MIT UNLICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/
%exclude %{cargo_registry}/%{crate}-%{version}/{Makefile,session.vim}

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ansi_formatting-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ansi_formatting-devel %{_description}

This package contains library source intended for building other packages
which use "ansi_formatting" feature of "%{crate}" crate.

%files       -n %{name}+ansi_formatting-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+lazy_static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lazy_static-devel %{_description}

This package contains library source intended for building other packages
which use "lazy_static" feature of "%{crate}" crate.

%files       -n %{name}+lazy_static-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+regex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+regex-devel %{_description}

This package contains library source intended for building other packages
which use "regex" feature of "%{crate}" crate.

%files       -n %{name}+regex-devel
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 1.2.1-1
- Update to 1.2.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 09 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-4
- Adapt to new packaging

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Thu Jun 14 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.4-2
- Bump regex to 1

* Thu Mar 08 2018 Josh Stone <jistone@redhat.com> - 1.0.4-1
- Update to 1.0.4

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-1
- Initial package
