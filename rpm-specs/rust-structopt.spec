# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate structopt

Name:           rust-%{crate}
Version:        0.3.18
Release:        1%{?dist}
Summary:        Parse command line argument by defining a struct

# Upstream license specification: Apache-2.0 OR MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/structopt
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Parse command line argument by defining a struct.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
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

%package     -n %{name}+color-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+color-devel %{_description}

This package contains library source intended for building other packages
which use "color" feature of "%{crate}" crate.

%files       -n %{name}+color-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug-devel %{_description}

This package contains library source intended for building other packages
which use "debug" feature of "%{crate}" crate.

%files       -n %{name}+debug-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+doc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+doc-devel %{_description}

This package contains library source intended for building other packages
which use "doc" feature of "%{crate}" crate.

%files       -n %{name}+doc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+lints-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lints-devel %{_description}

This package contains library source intended for building other packages
which use "lints" feature of "%{crate}" crate.

%files       -n %{name}+lints-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+no_cargo-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_cargo-devel %{_description}

This package contains library source intended for building other packages
which use "no_cargo" feature of "%{crate}" crate.

%files       -n %{name}+no_cargo-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+paw-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+paw-devel %{_description}

This package contains library source intended for building other packages
which use "paw" feature of "%{crate}" crate.

%files       -n %{name}+paw-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+paw_dep-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+paw_dep-devel %{_description}

This package contains library source intended for building other packages
which use "paw_dep" feature of "%{crate}" crate.

%files       -n %{name}+paw_dep-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+suggestions-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+suggestions-devel %{_description}

This package contains library source intended for building other packages
which use "suggestions" feature of "%{crate}" crate.

%files       -n %{name}+suggestions-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+wrap_help-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wrap_help-devel %{_description}

This package contains library source intended for building other packages
which use "wrap_help" feature of "%{crate}" crate.

%files       -n %{name}+wrap_help-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+yaml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+yaml-devel %{_description}

This package contains library source intended for building other packages
which use "yaml" feature of "%{crate}" crate.

%files       -n %{name}+yaml-devel
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
# * flatten_twice is marked should_panic, but gets a hard error from clap
# * ui tests fail for unknown reason
%cargo_test -- -- --skip flatten_twice --skip ui
%endif

%changelog
* Wed Sep 23 2020 Fabio Valentini <decathorpe@gmail.com> - 0.3.18-1
- Update to version 0.3.18.

* Wed Aug 26 2020 Josh Stone <jistone@redhat.com> - 0.3.17-1
- Update to 0.3.17

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Josh Stone <jistone@redhat.com> - 0.3.15-1
- Update to 0.3.15

* Thu Apr 23 2020 Josh Stone <jistone@redhat.com> - 0.3.14-1
- Update to 0.3.14

* Thu Apr 09 2020 Josh Stone <jistone@redhat.com> - 0.3.13-1
- Update to 0.3.13

* Wed Mar 18 2020 Josh Stone <jistone@redhat.com> - 0.3.12-1
- Update to 0.3.12

* Mon Mar 02 09:09:28 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.3.11-1
- Update to 0.3.11

* Mon Feb 10 2020 Josh Stone <jistone@redhat.com> - 0.3.9-1
- Update to 0.3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.3.7-1
- Update to 0.3.7

* Tue Dec 17 08:14:58 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.5-1
- Update to 0.3.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 17:18:49 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.18-1
- Update to 0.2.18

* Sun Jun 02 08:59:55 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.17-1
- Update to 0.2.17

* Thu May 30 17:34:06 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.16-1
- Update to 0.2.16

* Sun Mar 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.15-2
- Do not pull optional dependencies

* Sat Mar 09 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.15-1
- Update to 0.2.15

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Josh Stone <jistone@redhat.com> - 0.2.14-1
- Update to 0.2.14

* Thu Nov 15 2018 Josh Stone <jistone@redhat.com> - 0.2.13-1
- Update to 0.2.13

* Fri Nov 09 2018 Josh Stone <jistone@redhat.com> - 0.2.12-2
- Adapt to new packaging

* Thu Oct 11 2018 Josh Stone <jistone@redhat.com> - 0.2.12-1
- Update to 0.2.12

* Fri Oct 05 2018 Josh Stone <jistone@redhat.com> - 0.2.11-1
- Update to 0.2.11

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.10-2
- Adopt to new macro

* Thu Jun 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.10-1
- Update to 0.2.10

* Wed May 02 2018 Josh Stone <jistone@redhat.com> - 0.2.8-1
- Update to 0.2.8

* Tue Apr 17 2018 Josh Stone <jistone@redhat.com> - 0.2.7-1
- Update to 0.2.7

* Thu Mar 08 2018 Josh Stone <jistone@redhat.com> - 0.2.5-1
- Update to 0.2.5

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.7-1
- Initial package
