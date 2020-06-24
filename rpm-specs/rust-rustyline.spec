# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate rustyline

Name:           rust-%{crate}
Version:        6.1.2
Release:        1%{?dist}
Summary:        Readline implementation based on Antirez's Linenoise

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/rustyline
Source:         %{crates_source}

# fixup Cargo.toml metadata:
# - drop windows-specific dependencies
# - adapt to versions of dependencies available on fedora
Patch0:         00-fixup-cargo-toml.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Readline implementation based on Antirez's Linenoise.}

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

%package     -n %{name}+dirs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dirs-devel %{_description}

This package contains library source intended for building other packages
which use "dirs" feature of "%{crate}" crate.

%files       -n %{name}+dirs-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+skim-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+skim-devel %{_description}

This package contains library source intended for building other packages
which use "skim" feature of "%{crate}" crate.

%files       -n %{name}+skim-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+with-dirs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-dirs-devel %{_description}

This package contains library source intended for building other packages
which use "with-dirs" feature of "%{crate}" crate.

%files       -n %{name}+with-dirs-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+with-fuzzy-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-fuzzy-devel %{_description}

This package contains library source intended for building other packages
which use "with-fuzzy" feature of "%{crate}" crate.

%files       -n %{name}+with-fuzzy-devel
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
* Thu Apr 23 2020 Josh Stone <jistone@redhat.com> - 6.1.2-1
- Update to 6.1.2

* Mon Apr 13 2020 Fabio Valentini <decathorpe@gmail.com> - 6.1.1-1
- Update to version 6.1.1.

* Fri Apr 03 2020 Fabio Valentini <decathorpe@gmail.com> - 6.1.0-1
- Update to version 6.1.0.

* Sun Feb 02 2020 Fabio Valentini <decathorpe@gmail.com> - 6.0.0-1
- Initial package

