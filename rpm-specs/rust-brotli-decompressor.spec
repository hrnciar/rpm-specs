# Generated by rust2rpm 13
# * Tarball on crates.io does not ship test files
%bcond_with check
%global debug_package %{nil}

# The binary is useless
%global __cargo_is_bin() false

%global crate brotli-decompressor

Name:           rust-%{crate}
Version:        2.3.1
Release:        1%{?dist}
Summary:        Brotli decompressor that with an interface avoiding the rust stdlib

# Upstream license specification: BSD-3-Clause/MIT
# * https://github.com/dropbox/rust-brotli-decompressor/issues/9
License:        BSD
URL:            https://crates.io/crates/brotli-decompressor
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Brotli decompressor that with an interface avoiding the rust stdlib. This makes
it suitable for embedded devices and kernels. It is designed with a pluggable
allocator so that the standard lib's allocator may be employed. The default
build also includes a stdlib allocator and stream interface. Disable this with
--features=no-stdlib. Alternatively, --features=unsafe turns off array bounds
checks and memory initialization but provides a safe interface for the caller.
Without adding the --features=unsafe argument, all included code is safe. For
compression in addition to this library, download
https://github.com/dropbox/rust-brotli.}

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

%package     -n %{name}+alloc-stdlib-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-stdlib-devel %{_description}

This package contains library source intended for building other packages
which use "alloc-stdlib" feature of "%{crate}" crate.

%files       -n %{name}+alloc-stdlib-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+benchmark-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+benchmark-devel %{_description}

This package contains library source intended for building other packages
which use "benchmark" feature of "%{crate}" crate.

%files       -n %{name}+benchmark-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+disable-timer-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+disable-timer-devel %{_description}

This package contains library source intended for building other packages
which use "disable-timer" feature of "%{crate}" crate.

%files       -n %{name}+disable-timer-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pass-through-ffi-panics-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pass-through-ffi-panics-devel %{_description}

This package contains library source intended for building other packages
which use "pass-through-ffi-panics" feature of "%{crate}" crate.

%files       -n %{name}+pass-through-ffi-panics-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+seccomp-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+seccomp-devel %{_description}

This package contains library source intended for building other packages
which use "seccomp" feature of "%{crate}" crate.

%files       -n %{name}+seccomp-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unsafe-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unsafe-devel %{_description}

This package contains library source intended for building other packages
which use "unsafe" feature of "%{crate}" crate.

%files       -n %{name}+unsafe-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
# https://github.com/dropbox/rust-brotli-decompressor/pull/8
find -type f -name '*.rs' -executable -exec chmod -x '{}' +
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
* Fri May 29 2020 Josh Stone <jistone@redhat.com> - 2.3.1-1
- Update to 2.3.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 17:46:40 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.3.0-1
- Initial package
