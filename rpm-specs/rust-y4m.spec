# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate y4m

Name:           rust-%{crate}
Version:        0.6.0
Release:        1%{?dist}
Summary:        YUV4MPEG2 (.y4m) Encoder/Decoder

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/y4m
Source:         %{crates_source}
# Initial patched metadata
# * Update resize to 0.4, https://github.com/image-rs/y4m/pull/26
Patch0:         y4m-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
YUV4MPEG2 (.y4m) Encoder/Decoder.}

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
* Mon May 18 10:57:23 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 05 18:27:01 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.0-1
- Release 0.5.0

* Sun Sep 15 20:49:04 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-1
- Release 0.4.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 17:31:31 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.3-1
- Release 0.3.3

* Wed Mar 20 09:48:46 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-2
- Run tests in infrastructure

* Sat Mar 09 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.2-1
- Initial package
