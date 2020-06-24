# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate dav1d-sys

Name:           rust-%{crate}
Version:        0.3.2
Release:        1%{?dist}
Summary:        FFI bindings to dav1d

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/dav1d-sys
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
FFI bindings to dav1d.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(dav1d) >= 0.1.0

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+build-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+build-devel %{_description}

This package contains library source intended for building other packages
which use "build" feature of "%{crate}" crate.

%files       -n %{name}+build-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(dav1d) >= 0.1.0'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Sat May 30 2020 Josh Stone <jistone@redhat.com> - 0.3.2-1
- Update to 0.3.2

* Wed Apr 29 2020 Josh Stone <jistone@redhat.com> - 0.3.1-1
- Update to 0.3.1

* Wed Feb 26 2020 Josh Stone <jistone@redhat.com> - 0.3.0-2
- Bump bindgen to 0.53.1, https://github.com/rust-av/dav1d-rs/pull/28

* Tue Feb 11 01:35:53 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.0-1
- Update to 0.3.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 07 00:54:43 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.1-2
- Bump bindgen to 0.52

* Wed Sep 11 21:06:10 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.1-1
- Release 0.2.1 (#1750927)

* Wed Jul 31 18:52:26 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-3
- Bump bindgen to 0.51

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 14 20:29:58 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Release 0.2.0 (#1699642)

* Wed Mar 20 09:32:55 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-2
- Run tests in infrastructure

* Sat Mar 09 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.2-1
- Initial package
