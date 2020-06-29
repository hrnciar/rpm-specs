# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate zip

Name:           rust-%{crate}
Version:        0.5.6
Release:        1%{?dist}
Summary:        Library to support the reading and writing of zip files

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/zip
Source:         %{crates_source}
# Update walkdir to the version in Fedora
# https://github.com/mvdnes/zip-rs/pull/169
Patch0:         zip-update-walkdir.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library to support the reading and writing of zip files.}

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

%package     -n %{name}+deflate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deflate-devel %{_description}

This package contains library source intended for building other packages
which use "deflate" feature of "%{crate}" crate.

%files       -n %{name}+deflate-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+deflate-miniz-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deflate-miniz-devel %{_description}

This package contains library source intended for building other packages
which use "deflate-miniz" feature of "%{crate}" crate.

%files       -n %{name}+deflate-miniz-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+deflate-zlib-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deflate-zlib-devel %{_description}

This package contains library source intended for building other packages
which use "deflate-zlib" feature of "%{crate}" crate.

%files       -n %{name}+deflate-zlib-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+flate2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+flate2-devel %{_description}

This package contains library source intended for building other packages
which use "flate2" feature of "%{crate}" crate.

%files       -n %{name}+flate2-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+time-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+time-devel %{_description}

This package contains library source intended for building other packages
which use "time" feature of "%{crate}" crate.

%files       -n %{name}+time-devel
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
* Sat Jun 27 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.5.6-1
- Update to 0.5.6

* Sat May 23 13:25:44 PDT 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.5.5-1
- Initial package