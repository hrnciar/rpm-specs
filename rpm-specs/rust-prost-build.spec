# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate prost-build

Name:           rust-%{crate}
Version:        0.6.1
Release:        3%{?dist}
Summary:        Protocol Buffers implementation for the Rust Language

# Upstream license specification: Apache-2.0
# https://github.com/danburkert/prost/issues/353
License:        ASL 2.0
URL:            https://crates.io/crates/prost-build
Source:         %{crates_source}
# Initial patched metadata
# * bump which to 4: https://github.com/danburkert/prost/pull/358
Patch0:         prost-build-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  rust-packaging

%global _description %{expand:
Protocol Buffers implementation for the Rust Language.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
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

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
rm -rf third-party/
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Fri Sep 18 2020 Fabio Valentini <decathorpe@gmail.com> - 0.6.1-3
- Bump to which 4.

* Mon Sep 07 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.6.1-2
- Review updates

* Tue Aug 25 15:31:56 BST 2020 Peter Robinson <pbrobinson@gmail.com> - 0.6.1-1
- Initial package
