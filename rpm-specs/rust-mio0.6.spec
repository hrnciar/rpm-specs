# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate mio

Name:           rust-%{crate}0.6
Version:        0.6.22
Release:        3%{?dist}
Summary:        Lightweight non-blocking IO

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/mio
Source:         %{crates_source}
# Initial patched metadata
# * No windows or fuchsia
Patch0:         mio-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Lightweight non-blocking IO.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+with-deprecated-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-deprecated-devel %{_description}

This package contains library source intended for building other packages
which use "with-deprecated" feature of "%{crate}" crate.

%files       -n %{name}+with-deprecated-devel
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
# Tests below depend on having networking present
%cargo_test -- -- --skip poll::Poll --skip poll::Poll::deregister --skip poll::Poll::register --skip poll::Poll::reregister --skip sys::unix::ready::UnixReady --skip test_multicast::test_multicast
%endif

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.22-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Josh Stone <cuviper@gmail.com> - 0.6.22-1
- Update to 0.6.22

* Thu Apr 30 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.6.21-2
- Regenerate

* Wed Apr 29 21:19:34 CEST 2020 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.6.21-1
- Fork from rust-mio package for 0.6 branch
