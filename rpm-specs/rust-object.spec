# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate object

Name:           rust-%{crate}
Version:        0.20.0
Release:        1%{?dist}
Summary:        Unified interface for reading and writing object file formats

# Upstream license specification: Apache-2.0/MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/object
Source:         %{crates_source}
# Initial patched metadata
# * Remove wasm deps
Patch0:         object-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
A unified interface for reading and writing object file formats.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/
%exclude %{cargo_registry}/%{crate}-%{version_no_tilde}/coverage

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+all-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+all-devel %{_description}

This package contains library source intended for building other packages
which use "all" feature of "%{crate}" crate.

%files       -n %{name}+all-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+cargo-all-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cargo-all-devel %{_description}

This package contains library source intended for building other packages
which use "cargo-all" feature of "%{crate}" crate.

%files       -n %{name}+cargo-all-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+coff-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+coff-devel %{_description}

This package contains library source intended for building other packages
which use "coff" feature of "%{crate}" crate.

%files       -n %{name}+coff-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+compression-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compression-devel %{_description}

This package contains library source intended for building other packages
which use "compression" feature of "%{crate}" crate.

%files       -n %{name}+compression-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+crc32fast-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crc32fast-devel %{_description}

This package contains library source intended for building other packages
which use "crc32fast" feature of "%{crate}" crate.

%files       -n %{name}+crc32fast-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+elf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+elf-devel %{_description}

This package contains library source intended for building other packages
which use "elf" feature of "%{crate}" crate.

%files       -n %{name}+elf-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+flate2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+flate2-devel %{_description}

This package contains library source intended for building other packages
which use "flate2" feature of "%{crate}" crate.

%files       -n %{name}+flate2-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+indexmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+indexmap-devel %{_description}

This package contains library source intended for building other packages
which use "indexmap" feature of "%{crate}" crate.

%files       -n %{name}+indexmap-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+macho-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+macho-devel %{_description}

This package contains library source intended for building other packages
which use "macho" feature of "%{crate}" crate.

%files       -n %{name}+macho-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pe-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pe-devel %{_description}

This package contains library source intended for building other packages
which use "pe" feature of "%{crate}" crate.

%files       -n %{name}+pe-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+read-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+read-devel %{_description}

This package contains library source intended for building other packages
which use "read" feature of "%{crate}" crate.

%files       -n %{name}+read-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+read_core-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+read_core-devel %{_description}

This package contains library source intended for building other packages
which use "read_core" feature of "%{crate}" crate.

%files       -n %{name}+read_core-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unaligned-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unaligned-devel %{_description}

This package contains library source intended for building other packages
which use "unaligned" feature of "%{crate}" crate.

%files       -n %{name}+unaligned-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+write-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+write-devel %{_description}

This package contains library source intended for building other packages
which use "write" feature of "%{crate}" crate.

%files       -n %{name}+write-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+write_core-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+write_core-devel %{_description}

This package contains library source intended for building other packages
which use "write_core" feature of "%{crate}" crate.

%files       -n %{name}+write_core-devel
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
* Mon Jun 15 2020 Josh Stone <jistone@redhat.com> - 0.20.0-1
- Update to 0.20.0

* Tue May 12 2020 Josh Stone <jistone@redhat.com> - 0.19.0-1
- Update to 0.19.0

* Tue May 05 2020 Josh Stone <jistone@redhat.com> - 0.18.0-1
- Update to 0.18.0

* Wed Feb 26 2020 Josh Stone <jistone@redhat.com> - 0.17.0-2
- Bump goblin to 0.2

* Wed Feb 19 2020 Josh Stone <jistone@redhat.com> - 0.17.0-1
- Update to 0.17.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 15:33:29 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.0-1
- Update to 0.12.0

* Sat Apr 20 17:45:43 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.0-4
- Update goblin to 0.0.22

* Fri Apr 05 16:26:43 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.0-3
- Run tests in infrastructure

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Josh Stone <jistone@redhat.com> - 0.11.0-1
- Update to 0.11.0

* Tue Nov 13 2018 Josh Stone <jistone@redhat.com> - 0.10.0-2
- Adapt to new packaging

* Tue Oct 02 2018 Josh Stone <jistone@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-2
- Bump goblin to 0.0.17

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-5
- Bump goblin to 0.0.15

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-3
- Bump goblin to 0.0.14

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-2
- Rebuild for rust-packaging v5

* Mon Jan 01 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Sun Dec 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-1
- Initial package