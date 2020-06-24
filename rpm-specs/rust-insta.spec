# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate insta

Name:           rust-%{crate}
Version:        0.16.0
Release:        1%{?dist}
Summary:        Snapshot testing library for Rust

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/insta
Source:         %{crates_source}
# Initial patched metadata
# * https://github.com/mitsuhiko/insta/pull/124
# - Bump 'console' to 0.11.0
Patch0:         insta-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Snapshot testing library for Rust.}

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

%package     -n %{name}+backtrace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backtrace-devel %{_description}

This package contains library source intended for building other packages
which use "backtrace" feature of "%{crate}" crate.

%files       -n %{name}+backtrace-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+glob-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+glob-devel %{_description}

This package contains library source intended for building other packages
which use "glob" feature of "%{crate}" crate.

%files       -n %{name}+glob-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+globwalk-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+globwalk-devel %{_description}

This package contains library source intended for building other packages
which use "globwalk" feature of "%{crate}" crate.

%files       -n %{name}+globwalk-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pest-devel %{_description}

This package contains library source intended for building other packages
which use "pest" feature of "%{crate}" crate.

%files       -n %{name}+pest-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pest_derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pest_derive-devel %{_description}

This package contains library source intended for building other packages
which use "pest_derive" feature of "%{crate}" crate.

%files       -n %{name}+pest_derive-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+redactions-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+redactions-devel %{_description}

This package contains library source intended for building other packages
which use "redactions" feature of "%{crate}" crate.

%files       -n %{name}+redactions-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ron-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ron-devel %{_description}

This package contains library source intended for building other packages
which use "ron" feature of "%{crate}" crate.

%files       -n %{name}+ron-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serialization-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serialization-devel %{_description}

This package contains library source intended for building other packages
which use "serialization" feature of "%{crate}" crate.

%files       -n %{name}+serialization-devel
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
# thread 'runtime::test_format_rust_expression' panicked at 'snapshot assertion
# for 'format_rust_expression' failed in line 90', src/runtime.rs:995:9
# * https://github.com/mitsuhiko/insta/issues/126
%cargo_test -- -- --skip runtime::test_format_rust_expression
%endif

%changelog
* Wed Jun 17 22:28:51 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.16.0-1
- Initial package