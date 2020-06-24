# Generated by rust2rpm 15
%bcond_without check
%global debug_package %{nil}

%global crate asyncgit

Name:           rust-%{crate}
Version:        0.7.0
Release:        1%{?dist}
Summary:        Allow using git2 in a asynchronous context

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/asyncgit
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Allow using git2 in a asynchronous context.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE.md
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
%if %{with check}
echo '/usr/bin/git'
%endif

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Mon Jun 15 12:48:42 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Wed Jun 10 2020 Josh Stone <jistone@redhat.com> - 0.6.0-1
- Update to 0.6.0

* Mon Jun 01 2020 Josh Stone <jistone@redhat.com> - 0.5.0-1
- Update to 0.5.0

* Thu May 28 15:47:15 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 0.4.0-1
- Initial package
