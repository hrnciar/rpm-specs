# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate wayland-sys

Name:           rust-%{crate}
Version:        0.26.6
Release:        1%{?dist}
Summary:        FFI bindings to the various libwayland-*.so libraries

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/wayland-sys
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
FFI bindings to the various libwayland-*.so libraries. You should only need
this crate if you are working on custom wayland protocol extensions. Look at
the crate wayland-client for usable bindings.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
# one license file for a repo with multiple crates
# https://github.com/Smithay/wayland-rs/pull/323
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+client-devel %{_description}

This package contains library source intended for building other packages
which use "client" feature of "%{crate}" crate.

%files       -n %{name}+client-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+cursor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cursor-devel %{_description}

This package contains library source intended for building other packages
which use "cursor" feature of "%{crate}" crate.

%files       -n %{name}+cursor-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dlib-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dlib-devel %{_description}

This package contains library source intended for building other packages
which use "dlib" feature of "%{crate}" crate.

%files       -n %{name}+dlib-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dlopen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dlopen-devel %{_description}

This package contains library source intended for building other packages
which use "dlopen" feature of "%{crate}" crate.

%files       -n %{name}+dlopen-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+egl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+egl-devel %{_description}

This package contains library source intended for building other packages
which use "egl" feature of "%{crate}" crate.

%files       -n %{name}+egl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+lazy_static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lazy_static-devel %{_description}

This package contains library source intended for building other packages
which use "lazy_static" feature of "%{crate}" crate.

%files       -n %{name}+lazy_static-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+libc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libc-devel %{_description}

This package contains library source intended for building other packages
which use "libc" feature of "%{crate}" crate.

%files       -n %{name}+libc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+server-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+server-devel %{_description}

This package contains library source intended for building other packages
which use "server" feature of "%{crate}" crate.

%files       -n %{name}+server-devel
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
* Thu Jun 04 2020 Michel Alexandre Salim <michel@michel-slm.name> - 0.26.6-1
- Update to 0.26.6

* Fri May 22 14:31:57 PDT 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.26.5-1
- Initial package