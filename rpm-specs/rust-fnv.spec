# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate fnv

Name:           rust-%{crate}
Version:        1.0.7
Release:        2%{?dist}
Summary:        Fowler–Noll–Vo hash function

# Upstream license specification: Apache-2.0 / MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/fnv
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Fowler–Noll–Vo hash function.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
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

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 14 2020 Josh Stone <jistone@redhat.com> - 1.0.7-1
- Update to 1.0.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 23:17:11 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.6-9
- Regenerate

* Sun Jun 09 09:53:48 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.6-8
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.6-6
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.6-5
- Run tests in infrastructure

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.6-2
- Rebuild for rust-packaging v5

* Fri Nov 10 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.5-2
- Port to use rust-packaging

* Sat Feb 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.5-1
- Initial package
