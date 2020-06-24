# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate addr2line

Name:           rust-%{crate}
Version:        0.12.1
Release:        2%{?dist}
Summary:        Cross-platform symbolication library written in Rust, using `gimli`

# Upstream license specification: Apache-2.0/MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/addr2line
Source:         %{crates_source}
# Initial patched metadata
# * Bump to object 0.20
Patch0:         addr2line-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
A cross-platform symbolication library written in Rust, using `gimli`.}

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
%exclude %{cargo_registry}/%{crate}-%{version_no_tilde}/{benchmark.sh,bench.plot.r,coverage,memory.png,time.png}

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+cpp_demangle-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cpp_demangle-devel %{_description}

This package contains library source intended for building other packages
which use "cpp_demangle" feature of "%{crate}" crate.

%files       -n %{name}+cpp_demangle-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+fallible-iterator-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fallible-iterator-devel %{_description}

This package contains library source intended for building other packages
which use "fallible-iterator" feature of "%{crate}" crate.

%files       -n %{name}+fallible-iterator-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+object-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+object-devel %{_description}

This package contains library source intended for building other packages
which use "object" feature of "%{crate}" crate.

%files       -n %{name}+object-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rustc-demangle-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustc-demangle-devel %{_description}

This package contains library source intended for building other packages
which use "rustc-demangle" feature of "%{crate}" crate.

%files       -n %{name}+rustc-demangle-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+smallvec-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+smallvec-devel %{_description}

This package contains library source intended for building other packages
which use "smallvec" feature of "%{crate}" crate.

%files       -n %{name}+smallvec-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-object-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-object-devel %{_description}

This package contains library source intended for building other packages
which use "std-object" feature of "%{crate}" crate.

%files       -n %{name}+std-object-devel
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
* Mon Jun 15 2020 Josh Stone <jistone@redhat.com> - 0.12.1-2
- Bump to object 0.20

* Tue May 19 2020 Josh Stone <jistone@redhat.com> - 0.12.1-1
- Update to 0.12.1

* Tue May 12 2020 Josh Stone <jistone@redhat.com> - 0.12.0-1
- Update to 0.12.0

* Tue May 05 2020 Josh Stone <jistone@redhat.com> - 0.11.0-2
- Bump to object 0.18

* Wed Feb 19 2020 Josh Stone <jistone@redhat.com> - 0.11.0-1
- Update to 0.11.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Josh Stone <jistone@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 15:32:08 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Josh Stone <jistone@redhat.com> - 0.7.0-4
- Bump to object 0.11

* Tue Nov 13 2018 Josh Stone <jistone@redhat.com> - 0.7.0-3
- Adapt to new packaging

* Tue Oct 02 2018 Josh Stone <jistone@redhat.com> - 0.7.0-2
- Bump object to 0.10

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 14 2018 Josh Stone <jistone@redhat.com> - 0.6.0-1
- Update to 0.6.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-2
- Rebuild for rust-packaging v5

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Initial package
