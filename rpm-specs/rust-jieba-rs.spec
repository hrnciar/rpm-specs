# Generated by rust2rpm 13
# * unit tests require files not shipped with the crate
# * integration tests are only for WASM
# * doc tests are out of date
%bcond_with check
%global debug_package %{nil}

%global crate jieba-rs

Name:           rust-%{crate}
Version:        0.6.1
Release:        1%{?dist}
Summary:        Jieba Chinese Word Segmentation Implemented in Rust

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/jieba-rs
Source:         %{crates_source}
# Initial patched metadata
# * no wasm dependencies
# * no jemallocator dependency
Patch0:         jieba-rs-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Jieba Chinese Word Segmentation Implemented in Rust.}

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

%package     -n %{name}+default-dict-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-dict-devel %{_description}

This package contains library source intended for building other packages
which use "default-dict" feature of "%{crate}" crate.

%files       -n %{name}+default-dict-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ordered-float-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ordered-float-devel %{_description}

This package contains library source intended for building other packages
which use "ordered-float" feature of "%{crate}" crate.

%files       -n %{name}+ordered-float-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+textrank-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+textrank-devel %{_description}

This package contains library source intended for building other packages
which use "textrank" feature of "%{crate}" crate.

%files       -n %{name}+textrank-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tfidf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tfidf-devel %{_description}

This package contains library source intended for building other packages
which use "tfidf" feature of "%{crate}" crate.

%files       -n %{name}+tfidf-devel
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
* Thu Oct 15 2020 Fabio Valentini <decathorpe@gmail.com> - 0.6.1-1
- Initial package