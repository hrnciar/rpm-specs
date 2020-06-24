# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate wild

Name:           rust-%{crate}
Version:        2.0.4
Release:        1%{?dist}
Summary:        Glob (wildcard) expanded command-line arguments

# Upstream license specification: Apache-2.0 OR MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/wild
Source:         %{crates_source}
# Initial patched metadata
# * No windows
Patch0:         wild-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Glob (wildcard) expanded command-line arguments on Windows.}

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
* Sat Jun 06 2020 Josh Stone <jistone@redhat.com> - 2.0.4-1
- Update to 2.0.4

* Sat May 16 22:07:24 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Josh Stone <jistone@redhat.com> - 2.0.2-1
- Update to 2.0.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 18:59:29 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.1-5
- Regenerate

* Sun Jun 09 21:58:38 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.1-4
- Regenerate

* Tue May 07 14:13:33 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.1-3
- Update glob to 0.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.1-1
- Initial package
