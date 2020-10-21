# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate bytemuck

Name:           rust-%{crate}
Version:        1.4.1
Release:        1%{?dist}
Summary:        Crate for mucking around with piles of bytes

# Upstream license specification: Zlib OR Apache-2.0 OR MIT
License:        zlib or ASL 2.0 or MIT
URL:            https://crates.io/crates/bytemuck
Source:         %{crates_source}
# Initial patched metadata
# * Exclude unneeded files, https://github.com/Lokathor/bytemuck/pull/23
Patch0:         bytemuck-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Crate for mucking around with piles of bytes.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT LICENSE-ZLIB
%doc README.md changelog.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+bytemuck_derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bytemuck_derive-devel %{_description}

This package contains library source intended for building other packages
which use "bytemuck_derive" feature of "%{crate}" crate.

%files       -n %{name}+bytemuck_derive-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+derive-devel %{_description}

This package contains library source intended for building other packages
which use "derive" feature of "%{crate}" crate.

%files       -n %{name}+derive-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+extern_crate_alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+extern_crate_alloc-devel %{_description}

This package contains library source intended for building other packages
which use "extern_crate_alloc" feature of "%{crate}" crate.

%files       -n %{name}+extern_crate_alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+extern_crate_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+extern_crate_std-devel %{_description}

This package contains library source intended for building other packages
which use "extern_crate_std" feature of "%{crate}" crate.

%files       -n %{name}+extern_crate_std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+zeroable_maybe_uninit-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+zeroable_maybe_uninit-devel %{_description}

This package contains library source intended for building other packages
which use "zeroable_maybe_uninit" feature of "%{crate}" crate.

%files       -n %{name}+zeroable_maybe_uninit-devel
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
* Wed Sep 23 2020 Fabio Valentini <decathorpe@gmail.com> - 1.4.1-1
- Update to version 1.4.1.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 11:01:24 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.2.0-1
- Initial package
