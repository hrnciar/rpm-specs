# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate getrandom

Name:           rust-%{crate}
Version:        0.1.14
Release:        2%{?dist}
Summary:        Small cross-platform library for retrieving random data from system source

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/getrandom
Source:         %{crates_source}
# Initial patched metadata
# * No non-unix deps
Patch0:         getrandom-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Small cross-platform library for retrieving random data from system source.}

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

%package     -n %{name}+compiler_builtins-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compiler_builtins-devel %{_description}

This package contains library source intended for building other packages
which use "compiler_builtins" feature of "%{crate}" crate.

%files       -n %{name}+compiler_builtins-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+core-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+core-devel %{_description}

This package contains library source intended for building other packages
which use "core" feature of "%{crate}" crate.

%files       -n %{name}+core-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dummy-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dummy-devel %{_description}

This package contains library source intended for building other packages
which use "dummy" feature of "%{crate}" crate.

%files       -n %{name}+dummy-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+log-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+log-devel %{_description}

This package contains library source intended for building other packages
which use "log" feature of "%{crate}" crate.

%files       -n %{name}+log-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rustc-dep-of-std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustc-dep-of-std-devel %{_description}

This package contains library source intended for building other packages
which use "rustc-dep-of-std" feature of "%{crate}" crate.

%files       -n %{name}+rustc-dep-of-std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Josh Stone <jistone@redhat.com> - 0.1.14-1
- Update to 0.1.14

* Fri Dec 20 19:11:37 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.13-2
- Regenerate

* Fri Oct 25 19:13:03 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.13-1
- Update to 0.1.13

* Sun Aug 25 14:41:06 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.11-1
- Update to 0.1.11

* Sun Aug 18 11:36:10 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.10-1
- Update to 0.1.10

* Sat Aug 03 15:41:17 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7

* Sun Jul 28 14:47:44 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.6-1
- Initial package