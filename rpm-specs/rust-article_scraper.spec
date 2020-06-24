# Generated by rust2rpm 15
# * Tests require internet and a token
%bcond_with check
%global debug_package %{nil}

%global crate article_scraper

Name:           rust-%{crate}
Version:        1.1.2
Release:        1%{?dist}
Summary:        Scrap article contents from the web

# Upstream license specification: GPL-3.0-or-later
License:        GPLv3+
URL:            https://crates.io/crates/article_scraper
Source:         %{crates_source}
# Initial patched metadata
# * Fixup deps, https://pagure.io/fedora-rust/rust2rpm/issue/109
Patch0:         article_scraper-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Scrap article contents from the web. Powered by fivefilters full text feed
configurations.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

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
* Sun Jun 07 11:47:32 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 1.1.2-1
- Initial package