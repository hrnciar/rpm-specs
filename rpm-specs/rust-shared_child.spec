# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate shared_child

Name:           rust-%{crate}
Version:        0.3.4
Release:        3%{?dist}
Summary:        Library for using child processes from multiple threads

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/shared_child
Source:         %{crates_source}
# Initial patched metadata
# * No windows
Patch0:         shared_child-fix-metadata.diff
# https://github.com/oconnor663/shared_child.rs/issues/16
Patch0001:      0001-Avoid-using-python-in-the-tests.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library for using child processes from multiple threads.}

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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 15:57:19 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.4-1
- Update to 0.3.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 07 16:17:02 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.3-1
- Initial package
