# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate envsubst

Name:           rust-%{crate}
Version:        0.2.0
Release:        2%{?dist}
Summary:        Variables substitution

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/envsubst
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Variables substitution.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version}/
%license COPYRIGHT LICENSE-APACHE-2.0 LICENSE-MIT

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
* Wed Apr 15 Robert Fairley <rfairley@redhat.com> - 0.2.0-2
- Add back license files

* Wed Apr 15 02:09:32 UTC 2020 Robert <rfairley@redhat.com> - 0.2.0-1
- Update to 0.2.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 17:16:10 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-3
- Regenerate

* Mon Jun 10 12:38:00 UTC 2019 Robert Fairley <rfairley@redhat.com> - 0.1.1-2
- Add license files

* Sun Jun 09 17:52:49 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-1
- Initial package
