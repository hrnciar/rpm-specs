# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate nalgebra

Name:           rust-%{crate}
Version:        0.20.0
Release:        1%{?dist}
Summary:        Linear algebra library with transformations and matrices

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            https://crates.io/crates/nalgebra
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Linear algebra library with transformations and statically-sized or
dynamically-sized matrices.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
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

%package     -n %{name}+abomonation-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+abomonation-devel %{_description}

This package contains library source intended for building other packages
which use "abomonation" feature of "%{crate}" crate.

%files       -n %{name}+abomonation-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+abomonation-serialize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+abomonation-serialize-devel %{_description}

This package contains library source intended for building other packages
which use "abomonation-serialize" feature of "%{crate}" crate.

%files       -n %{name}+abomonation-serialize-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages
which use "alloc" feature of "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+arbitrary-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+arbitrary-devel %{_description}

This package contains library source intended for building other packages
which use "arbitrary" feature of "%{crate}" crate.

%files       -n %{name}+arbitrary-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug-devel %{_description}

This package contains library source intended for building other packages
which use "debug" feature of "%{crate}" crate.

%files       -n %{name}+debug-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+io-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+io-devel %{_description}

This package contains library source intended for building other packages
which use "io" feature of "%{crate}" crate.

%files       -n %{name}+io-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+matrixmultiply-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+matrixmultiply-devel %{_description}

This package contains library source intended for building other packages
which use "matrixmultiply" feature of "%{crate}" crate.

%files       -n %{name}+matrixmultiply-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+mint-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mint-devel %{_description}

This package contains library source intended for building other packages
which use "mint" feature of "%{crate}" crate.

%files       -n %{name}+mint-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pest-devel %{_description}

This package contains library source intended for building other packages
which use "pest" feature of "%{crate}" crate.

%files       -n %{name}+pest-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pest_derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pest_derive-devel %{_description}

This package contains library source intended for building other packages
which use "pest_derive" feature of "%{crate}" crate.

%files       -n %{name}+pest_derive-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+quickcheck-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+quickcheck-devel %{_description}

This package contains library source intended for building other packages
which use "quickcheck" feature of "%{crate}" crate.

%files       -n %{name}+quickcheck-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rand_distr-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rand_distr-devel %{_description}

This package contains library source intended for building other packages
which use "rand_distr" feature of "%{crate}" crate.

%files       -n %{name}+rand_distr-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-serialize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-serialize-devel %{_description}

This package contains library source intended for building other packages
which use "serde-serialize" feature of "%{crate}" crate.

%files       -n %{name}+serde-serialize-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_derive-devel %{_description}

This package contains library source intended for building other packages
which use "serde_derive" feature of "%{crate}" crate.

%files       -n %{name}+serde_derive-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+sparse-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sparse-devel %{_description}

This package contains library source intended for building other packages
which use "sparse" feature of "%{crate}" crate.

%files       -n %{name}+sparse-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+stdweb-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+stdweb-devel %{_description}

This package contains library source intended for building other packages
which use "stdweb" feature of "%{crate}" crate.

%files       -n %{name}+stdweb-devel
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
* Mon Mar 02 17:15:39 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.20.0-1
- Update to 0.20.0

* Thu Feb 20 2020 Josh Stone <jistone@redhat.com> - 0.19.0-1
- Update to 0.19.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 21:08:31 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.18.1-1
- Update to 0.18.1
- Bump quickcheck to 0.9

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 04 08:06:20 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.18.0-1
- Update to 0.18.0

* Tue Mar 19 2019 Josh Stone <jistone@redhat.com> - 0.17.3-1
- Update to 0.17.3

* Tue Feb 19 2019 Josh Stone <jistone@redhat.com> - 0.17.2-1
- Update to 0.17.2

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.17.1-1
- Update to 0.17.1

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.17.0-1
- Initial package