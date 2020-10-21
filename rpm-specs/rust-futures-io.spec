# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate futures-io

Name:           rust-%{crate}
Version:        0.3.6
Release:        1%{?dist}
Summary:        AsyncRead, AsyncWrite, AsyncSeek, and AsyncBufRead traits

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/futures-io
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
`AsyncRead`, `AsyncWrite`, `AsyncSeek`, and `AsyncBufRead` traits for the
futures-rs library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+read-initializer-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+read-initializer-devel %{_description}

This package contains library source intended for building other packages
which use "read-initializer" feature of "%{crate}" crate.

%files       -n %{name}+read-initializer-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages
which use "unstable" feature of "%{crate}" crate.

%files       -n %{name}+unstable-devel
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
* Wed Oct 07 2020 Fabio Valentini <decathorpe@gmail.com> - 0.3.6-1
- Update to version 0.3.6.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 09 2020 Josh Stone <jistone@redhat.com> - 0.3.5-1
- Update to 0.3.5

* Mon Feb 10 2020 Josh Stone <jistone@redhat.com> - 0.3.4-1
- Update to 0.3.4

* Thu Feb 06 2020 Josh Stone <jistone@redhat.com> - 0.3.3-1
- Update to 0.3.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 20:50:48 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.1-1
- Initial package
