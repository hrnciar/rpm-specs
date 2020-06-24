# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate cookie

Name:           rust-%{crate}
Version:        0.12.0
Release:        2%{?dist}
Summary:        Crate for parsing HTTP cookie headers and managing a cookie jar

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/cookie
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Crate for parsing HTTP cookie headers and managing a cookie jar. Supports
signed and private (encrypted + signed) jars.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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

%package     -n %{name}+base64-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+base64-devel %{_description}

This package contains library source intended for building other packages
which use "base64" feature of "%{crate}" crate.

%files       -n %{name}+base64-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+percent-encode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+percent-encode-devel %{_description}

This package contains library source intended for building other packages
which use "percent-encode" feature of "%{crate}" crate.

%files       -n %{name}+percent-encode-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ring-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ring-devel %{_description}

This package contains library source intended for building other packages
which use "ring" feature of "%{crate}" crate.

%files       -n %{name}+ring-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+secure-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+secure-devel %{_description}

This package contains library source intended for building other packages
which use "secure" feature of "%{crate}" crate.

%files       -n %{name}+secure-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+url-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+url-devel %{_description}

This package contains library source intended for building other packages
which use "url" feature of "%{crate}" crate.

%files       -n %{name}+url-devel
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 20:10:36 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.12.0-1
- Initial package
