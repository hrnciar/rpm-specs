# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate time

Name:           rust-%{crate}
Version:        0.2.16
Release:        1%{?dist}
Summary:        Date and time library

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/time
Source:         %{crates_source}
# Initial patched metadata
# * No windows or wasm
Patch0:         time-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Date and time library. Fully interoperable with the standard library. Mostly
compatible with #![no_std].}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-Apache
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+__doc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+__doc-devel %{_description}

This package contains library source intended for building other packages
which use "__doc" feature of "%{crate}" crate.

%files       -n %{name}+__doc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+deprecated-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deprecated-devel %{_description}

This package contains library source intended for building other packages
which use "deprecated" feature of "%{crate}" crate.

%files       -n %{name}+deprecated-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+libc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libc-devel %{_description}

This package contains library source intended for building other packages
which use "libc" feature of "%{crate}" crate.

%files       -n %{name}+libc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+panicking-api-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+panicking-api-devel %{_description}

This package contains library source intended for building other packages
which use "panicking-api" feature of "%{crate}" crate.

%files       -n %{name}+panicking-api-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rand-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rand-devel %{_description}

This package contains library source intended for building other packages
which use "rand" feature of "%{crate}" crate.

%files       -n %{name}+rand-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
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
* Tue May 12 2020 Josh Stone <jistone@redhat.com> - 0.2.16-1
- Update to 0.2.16

* Mon May 04 2020 Josh Stone <jistone@redhat.com> - 0.2.15-1
- Update to 0.2.15

* Wed Apr 29 2020 Josh Stone <jistone@redhat.com> - 0.2.11-1
- Update to 0.2.11

* Fri Apr 17 2020 Josh Stone <jistone@redhat.com> - 0.2.9-1
- Update to 0.2.9

* Sun Feb 23 10:26:00 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.7-1
- Update to 0.2.7

* Wed Feb 12 2020 Josh Stone <jistone@redhat.com> - 0.2.6-1
- Update to 0.2.6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.42-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.42-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 22:09:19 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.42-6
- Regenerate

* Sun Jun 09 21:44:41 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.42-5
- Regenerate

* Sun Mar 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.42-4
- Do not pull optional dependencies

* Tue Mar 05 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.42-3
- Run tests in infrastructure

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.1.42-1
- Update to 0.1.42

* Thu Dec 13 2018 Josh Stone <jistone@redhat.com> - 0.1.41-1
- Update to 0.1.41

* Wed Oct 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.40-3
- Adapt to new packaging

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.40-1
- Update to 0.1.40

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.39-2
- Rebuild for rust-packaging v5

* Thu Jan 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.39-1
- Update to 0.1.39

* Mon Nov 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.38-2
- Exclude unneeded files

* Fri Jul 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.38-1
- Update to 0.1.38

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.36-3
- Port to use rust-packaging

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.36-2
- Use rich dependencies

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.36-1
- Initial package
