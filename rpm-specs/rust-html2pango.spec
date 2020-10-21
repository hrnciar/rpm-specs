# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate html2pango

Name:           rust-%{crate}
Version:        0.3.3
Release:        1%{?dist}
Summary:        Library to convert html to pango

# Upstream license specification: GPL-3.0
License:        GPLv3
URL:            https://crates.io/crates/html2pango
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library to convert html to pango.}

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
* Wed Sep 16 2020 Fabio Valentini <decathorpe@gmail.com> - 0.3.3-1
- Update to version 0.3.3.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 01 00:23:14 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.2-3
- Bump linkify to 0.4.0
- Rebuild for F32 Mass Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 18:52:19 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.2-1
- Update to 0.3.2
- Bump ammonia to 3.0.0
- Bump html5ever to 0.24

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 16:31:57 EEST 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.1-1
- Initial package
