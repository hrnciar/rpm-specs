# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate quick-xml

Name:           rust-%{crate}
Version:        0.18.1
Release:        1%{?dist}
Summary:        High performance xml reader and writer

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/quick-xml
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
High performance xml reader and writer.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT.md
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

%package     -n %{name}+encoding-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+encoding-devel %{_description}

This package contains library source intended for building other packages
which use "encoding" feature of "%{crate}" crate.

%files       -n %{name}+encoding-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+encoding_rs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+encoding_rs-devel %{_description}

This package contains library source intended for building other packages
which use "encoding_rs" feature of "%{crate}" crate.

%files       -n %{name}+encoding_rs-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serialize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serialize-devel %{_description}

This package contains library source intended for building other packages
which use "serialize" feature of "%{crate}" crate.

%files       -n %{name}+serialize-devel
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
* Wed Sep 16 2020 Fabio Valentini <decathorpe@gmail.com> - 0.18.1-1
- Initial package
