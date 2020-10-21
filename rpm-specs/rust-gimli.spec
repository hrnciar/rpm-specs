# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate gimli

Name:           rust-%{crate}
Version:        0.22.0
Release:        2%{?dist}
Summary:        Library for reading and writing the DWARF debugging format

# Upstream license specification: Apache-2.0/MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/gimli
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
A library for reading and writing the DWARF debugging format.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md CONTRIBUTING.md README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+endian-reader-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+endian-reader-devel %{_description}

This package contains library source intended for building other packages
which use "endian-reader" feature of "%{crate}" crate.

%files       -n %{name}+endian-reader-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+fallible-iterator-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fallible-iterator-devel %{_description}

This package contains library source intended for building other packages
which use "fallible-iterator" feature of "%{crate}" crate.

%files       -n %{name}+fallible-iterator-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+indexmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+indexmap-devel %{_description}

This package contains library source intended for building other packages
which use "indexmap" feature of "%{crate}" crate.

%files       -n %{name}+indexmap-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+read-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+read-devel %{_description}

This package contains library source intended for building other packages
which use "read" feature of "%{crate}" crate.

%files       -n %{name}+read-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+stable_deref_trait-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+stable_deref_trait-devel %{_description}

This package contains library source intended for building other packages
which use "stable_deref_trait" feature of "%{crate}" crate.

%files       -n %{name}+stable_deref_trait-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+write-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+write-devel %{_description}

This package contains library source intended for building other packages
which use "write" feature of "%{crate}" crate.

%files       -n %{name}+write-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
find -type f -name '*.rs' -exec chmod -c -x '{}' '+'
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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Josh Stone <jistone@redhat.com> - 0.22.0-1
- Update to 0.22.0

* Tue May 12 2020 Josh Stone <jistone@redhat.com> - 0.21.0-1
- Update to 0.21.0

* Wed Feb 19 2020 Josh Stone <jistone@redhat.com> - 0.20.0-1
- Update to 0.20.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 20:55:53 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.19.0-2
- Bump arrayvec to 0.5

* Mon Dec 16 2019 Josh Stone <jistone@redhat.com> - 0.19.0-1
- Update to 0.19.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 15:36:43 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.18.0-1
- Update to 0.18.0

* Sat Apr 20 15:24:33 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.17.0-1
- Update to 0.17.0

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.16.1-3
- Adapt to new packaging

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 08 2018 Josh Stone <jistone@redhat.com> - 0.16.1-1
- Update to 0.16.1

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.16.0-1
- Update to 0.16.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.0-2
- Rebuild for rust-packaging v5

* Sun Dec 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.0-1
- Initial package
