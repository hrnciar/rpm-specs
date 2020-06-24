# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate arrayvec

Name:           rust-%{crate}
Version:        0.5.1
Release:        2%{?dist}
Summary:        Vector with fixed capacity, backed by an array

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/arrayvec
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Vector with fixed capacity, backed by an array (it can be stored on the stack
too). Implements fixed capacity ArrayVec and ArrayString.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.rst
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+array-sizes-129-255-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+array-sizes-129-255-devel %{_description}

This package contains library source intended for building other packages
which use "array-sizes-129-255" feature of "%{crate}" crate.

%files       -n %{name}+array-sizes-129-255-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+array-sizes-33-128-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+array-sizes-33-128-devel %{_description}

This package contains library source intended for building other packages
which use "array-sizes-33-128" feature of "%{crate}" crate.

%files       -n %{name}+array-sizes-33-128-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 17:32:46 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.1-1
- Release 0.5.1

* Sun Jul 28 18:26:46 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.11-1
- Update to 0.4.11

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 11:38:19 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.10-4
- Regenerate

* Sun Mar 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.10-3
- Do not pull optional dependencies

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Josh Stone <jistone@redhat.com> - 0.4.10-1
- Update to 0.4.10

* Mon Nov 26 2018 Josh Stone <jistone@redhat.com> - 0.4.8-1
- Update to 0.4.8

* Sat Oct 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.7-5
- Adapt to new packaging

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.7-4
- Rebuild to trigger tests

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.7-1
- Update to 0.4.7

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.6-2
- Rebuild for rust-packaging v5

* Sun Dec 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.6-1
- Initial package
