# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate encoding-index-japanese

Name:           rust-%{crate}
Version:        1.20141219.5
Release:        11%{?dist}
Summary:        Index tables for Japanese character encodings

# Upstream license specification: CC0-1.0
# https://github.com/lifthrasiir/rust-encoding/issues/111
License:        CC0
URL:            https://crates.io/crates/encoding-index-japanese
Source:         %{crates_source}
# Initial patched metadata
# * No paths
# * Make dev-dependency as dev one
Patch0:         encoding-index-japanese-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Index tables for Japanese character encodings.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version}/

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
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20141219.5-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20141219.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20141219.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20141219.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 11:35:54 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.20141219.5-7
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20141219.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.20141219.5-5
- Adapt to new packaging

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20141219.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20141219.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.20141219.5-2
- Rebuild for rust-packaging v5

* Sun Nov 12 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.20141219.5-1
- Initial package
