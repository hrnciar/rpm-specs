# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate itoa

Name:           rust-%{crate}
Version:        0.4.6
Release:        1%{?dist}
Summary:        Fast functions for printing integer primitives to an io::Write

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/itoa
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Fast functions for printing integer primitives to an io::Write.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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

%package     -n %{name}+i128-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+i128-devel %{_description}

This package contains library source intended for building other packages
which use "i128" feature of "%{crate}" crate.

%files       -n %{name}+i128-devel
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
* Fri Jun 19 2020 Josh Stone <jistone@redhat.com> - 0.4.6-1
- Update to 0.4.6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Josh Stone <jistone@redhat.com> - 0.4.5-1
- Update to 0.4.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 23:18:31 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.4-3
- Regenerate

* Sun Jun 09 10:13:08 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.4-2
- Regenerate

* Thu May 02 08:37:44 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.3-3
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.3-2
- Run tests in infrastructure

* Tue Sep 11 2018 Josh Stone <jistone@redhat.com> - 0.4.3-1
- Update to 0.4.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Mon Mar 26 2018 Josh Stone <jistone@redhat.com> - 0.4.1-1
- Update to 0.4.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.4-2
- Rebuild for rust-packaging v5

* Sat Nov 04 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.4-1
- Update to 0.3.4

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-2
- Port to use rust-packaging

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-1
- Initial package
