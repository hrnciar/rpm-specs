# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate tracing-core

Name:           rust-%{crate}
Version:        0.1.17
Release:        1%{?dist}
Summary:        Core primitives for application-level tracing

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/tracing-core
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Core primitives for application-level tracing.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE LICENSE-lazy_static LICENSE-spin
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/
# Don't ship our manual license copies in the devel package.
%exclude %{cargo_registry}/%{crate}-%{version_no_tilde}/LICENSE-*

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+lazy_static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lazy_static-devel %{_description}

This package contains library source intended for building other packages
which use "lazy_static" feature of "%{crate}" crate.

%files       -n %{name}+lazy_static-devel
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

# These "inner" licenses are also MIT, but with different copyright statements.
# Copy them to distinct names for normal license installation.
cp -p src/lazy_static/LICENSE LICENSE-lazy_static
cp -p src/spin/LICENSE LICENSE-spin

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
* Thu Oct 01 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.17-1
- Update to version 0.1.17.

* Wed Sep 09 2020 Josh Stone <jistone@redhat.com> - 0.1.16-1
- Update to 0.1.16

* Tue Aug 25 2020 Josh Stone <jistone@redhat.com> - 0.1.15-1
- Update to 0.1.15

* Thu Jul 23 2020 Josh Stone <jistone@redhat.com> - 0.1.11-1
- Initial package
