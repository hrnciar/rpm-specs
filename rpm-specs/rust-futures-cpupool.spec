# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate futures-cpupool

Name:           rust-%{crate}
Version:        0.1.8
Release:        9%{?dist}
Summary:        Implementation of thread pools which hand out futures

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/futures-cpupool
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Implementation of thread pools which hand out futures to the results of the
computation on the threads themselves.}

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

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+with-deprecated-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-deprecated-devel %{_description}

This package contains library source intended for building other packages
which use "with-deprecated" feature of "%{crate}" crate.

%files       -n %{name}+with-deprecated-devel
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 22:29:30 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.8-7
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.8-5
- Adapt to new packaging

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.8-2
- Rebuild for rust-packaging v5

* Thu Jan 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.8-1
- Update to 0.1.8

* Fri Dec 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.7-1
- Initial package
