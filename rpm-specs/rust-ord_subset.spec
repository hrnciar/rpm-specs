# Generated by rust2rpm
%bcond_with check
%global debug_package %{nil}

%global crate ord_subset

Name:           rust-%{crate}
Version:        3.1.1
Release:        5%{?dist}
Summary:        Tools for working with the Ord subset of certain PartialOrd types, like floats

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/ord_subset
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description \
Tools for working with the Ord subset of certain PartialOrd types, like floats.

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+ops-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ops-devel %{_description}

This package contains library source intended for building other packages
which use "ops" feature of "%{crate}" crate.

%files       -n %{name}+ops-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+unchecked_ops-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unchecked_ops-devel %{_description}

This package contains library source intended for building other packages
which use "unchecked_ops" feature of "%{crate}" crate.

%files       -n %{name}+unchecked_ops-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages
which use "unstable" feature of "%{crate}" crate.

%files       -n %{name}+unstable-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 24 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.1-3
- Adapt to new packaging

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1

* Mon Sep 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.0-1
- Initial package
