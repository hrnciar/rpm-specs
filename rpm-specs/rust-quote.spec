# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate quote

Name:           rust-%{crate}
Version:        1.0.7
Release:        1%{?dist}
Summary:        Quasi-quoting macro quote!(...)

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/quote
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Quasi-quoting macro quote!(...).}

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

%package     -n %{name}+proc-macro-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+proc-macro-devel %{_description}

This package contains library source intended for building other packages
which use "proc-macro" feature of "%{crate}" crate.

%files       -n %{name}+proc-macro-devel
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
* Thu Jun 11 2020 Josh Stone <jistone@redhat.com> - 1.0.7-1
- Update to 1.0.7

* Mon May 18 07:38:37 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6

* Wed May 13 2020 Josh Stone <jistone@redhat.com> - 1.0.5-1
- Update to 1.0.5

* Thu Apr 30 2020 Josh Stone <jistone@redhat.com> - 1.0.4-1
- Update to 1.0.4

* Thu Mar 05 2020 Josh Stone <jistone@redhat.com> - 1.0.3-1
- Update to 1.0.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 18 15:32:52 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Sat Aug 03 14:08:02 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.13-1
- Update to 0.6.13

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 11:32:19 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.12-3
- Regenerate

* Sun Jun 09 10:23:39 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.12-2
- Regenerate

* Wed Apr 10 07:48:32 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.12-1
- Update to 0.6.12

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.11-1
- Update to 0.6.11

* Sat Nov 10 2018 Josh Stone <jistone@redhat.com> - 0.6.10-1
- Update to 0.6.10

* Mon Oct 29 2018 Josh Stone <jistone@redhat.com> - 0.6.9-1
- Update to 0.6.9

* Fri Oct 26 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.8-2
- Adapt to new packaging

* Fri Sep 07 2018 Josh Stone <jistone@redhat.com> - 0.6.8-1
- Update to 0.6.8

* Mon Aug 13 2018 Josh Stone <jistone@redhat.com> - 0.6.6-1
- Update to 0.6.6

* Tue Aug 07 2018 Josh Stone <jistone@redhat.com> - 0.6.5-1
- Update to 0.6.5

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.4-2
- Rebuild to trigger tests

* Mon Jul 23 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.4-1
- Update to 0.6.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.3-1
- Update to 0.6.3

* Sun Apr 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2

* Tue Apr 17 2018 Josh Stone <jistone@redhat.com> - 0.5.1-1
- Update to 0.5.1

* Thu Mar 08 2018 Josh Stone <jistone@redhat.com> - 0.4.2-1
- Update to 0.4.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.15-3
- Rebuild for rust-packaging v5

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.15-2
- Port to use rust-packaging

* Mon Mar 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.15-1
- Update to 0.3.15

* Tue Feb 28 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.14-1
- Update to 0.3.14

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.13-1
- Update to 0.3.13

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.12-1
- Initial package
