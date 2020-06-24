# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate psutil

Name:           rust-%{crate}
Version:        3.1.0
Release:        1%{?dist}
Summary:        Process and system monitoring library

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/psutil
Source:         %{crates_source}
# Initial patched metadata
# * No Mac deps
Patch0:         psutil-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Process and system monitoring library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md CHANGELOG.md platform-support.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+cpu-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cpu-devel %{_description}

This package contains library source intended for building other packages
which use "cpu" feature of "%{crate}" crate.

%files       -n %{name}+cpu-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+derive_more-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+derive_more-devel %{_description}

This package contains library source intended for building other packages
which use "derive_more" feature of "%{crate}" crate.

%files       -n %{name}+derive_more-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+disk-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+disk-devel %{_description}

This package contains library source intended for building other packages
which use "disk" feature of "%{crate}" crate.

%files       -n %{name}+disk-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+glob-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+glob-devel %{_description}

This package contains library source intended for building other packages
which use "glob" feature of "%{crate}" crate.

%files       -n %{name}+glob-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+host-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+host-devel %{_description}

This package contains library source intended for building other packages
which use "host" feature of "%{crate}" crate.

%files       -n %{name}+host-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+memory-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+memory-devel %{_description}

This package contains library source intended for building other packages
which use "memory" feature of "%{crate}" crate.

%files       -n %{name}+memory-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+network-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+network-devel %{_description}

This package contains library source intended for building other packages
which use "network" feature of "%{crate}" crate.

%files       -n %{name}+network-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+num_cpus-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+num_cpus-devel %{_description}

This package contains library source intended for building other packages
which use "num_cpus" feature of "%{crate}" crate.

%files       -n %{name}+num_cpus-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+platforms-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+platforms-devel %{_description}

This package contains library source intended for building other packages
which use "platforms" feature of "%{crate}" crate.

%files       -n %{name}+platforms-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+process-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+process-devel %{_description}

This package contains library source intended for building other packages
which use "process" feature of "%{crate}" crate.

%files       -n %{name}+process-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+sensors-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sensors-devel %{_description}

This package contains library source intended for building other packages
which use "sensors" feature of "%{crate}" crate.

%files       -n %{name}+sensors-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+signal-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+signal-devel %{_description}

This package contains library source intended for building other packages
which use "signal" feature of "%{crate}" crate.

%files       -n %{name}+signal-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unescape-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unescape-devel %{_description}

This package contains library source intended for building other packages
which use "unescape" feature of "%{crate}" crate.

%files       -n %{name}+unescape-devel
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
* Mon May 11 07:45:56 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0

* Wed Mar 18 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.0.1-2
- Backport features needed for ytop

* Wed Mar 18 14:57:17 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.1-1
- Initial package
