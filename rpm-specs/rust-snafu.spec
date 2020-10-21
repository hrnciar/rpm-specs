# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate snafu

Name:           rust-%{crate}
Version:        0.6.9
Release:        1%{?dist}
Summary:        Ergonomic error handling library

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/snafu
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Ergonomic error handling library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
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

%package     -n %{name}+backtraces-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backtraces-devel %{_description}

This package contains library source intended for building other packages
which use "backtraces" feature of "%{crate}" crate.

%files       -n %{name}+backtraces-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+backtraces-impl-backtrace-crate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backtraces-impl-backtrace-crate-devel %{_description}

This package contains library source intended for building other packages
which use "backtraces-impl-backtrace-crate" feature of "%{crate}" crate.

%files       -n %{name}+backtraces-impl-backtrace-crate-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-devel %{_description}

This package contains library source intended for building other packages
which use "futures" feature of "%{crate}" crate.

%files       -n %{name}+futures-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-01-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-01-devel %{_description}

This package contains library source intended for building other packages
which use "futures-01" feature of "%{crate}" crate.

%files       -n %{name}+futures-01-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-01-crate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-01-crate-devel %{_description}

This package contains library source intended for building other packages
which use "futures-01-crate" feature of "%{crate}" crate.

%files       -n %{name}+futures-01-crate-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-core-crate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-core-crate-devel %{_description}

This package contains library source intended for building other packages
which use "futures-core-crate" feature of "%{crate}" crate.

%files       -n %{name}+futures-core-crate-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-crate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-crate-devel %{_description}

This package contains library source intended for building other packages
which use "futures-crate" feature of "%{crate}" crate.

%files       -n %{name}+futures-crate-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+guide-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+guide-devel %{_description}

This package contains library source intended for building other packages
which use "guide" feature of "%{crate}" crate.

%files       -n %{name}+guide-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+internal-dev-dependencies-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+internal-dev-dependencies-devel %{_description}

This package contains library source intended for building other packages
which use "internal-dev-dependencies" feature of "%{crate}" crate.

%files       -n %{name}+internal-dev-dependencies-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pin-project-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pin-project-devel %{_description}

This package contains library source intended for building other packages
which use "pin-project" feature of "%{crate}" crate.

%files       -n %{name}+pin-project-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unstable-backtraces-impl-std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-backtraces-impl-std-devel %{_description}

This package contains library source intended for building other packages
which use "unstable-backtraces-impl-std" feature of "%{crate}" crate.

%files       -n %{name}+unstable-backtraces-impl-std-devel
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
* Wed Sep 23 2020 Fabio Valentini <decathorpe@gmail.com> - 0.6.9-1
- Update to version 0.6.9.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 2020 Josh Stone <jistone@redhat.com> - 0.6.8-1
- Update to 0.6.8

* Mon May 04 2020 Josh Stone <jistone@redhat.com> - 0.6.7-1
- Update to 0.6.7

* Wed Apr 08 2020 Josh Stone <jistone@redhat.com> - 0.6.6-1
- Update to 0.6.6

* Wed Apr 01 2020 Josh Stone <jistone@redhat.com> - 0.6.3-1
- Update to 0.6.3

* Wed Mar 18 14:32:01 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.2-1
- Initial package
