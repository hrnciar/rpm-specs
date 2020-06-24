# Generated by rust2rpm 15
%bcond_without check
%global debug_package %{nil}

%global crate serde_derive

Name:           rust-%{crate}
Version:        1.0.113
Release:        1%{?dist}
Summary:        Macros 1.1 implementation of #[derive(Serialize, Deserialize)]

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/serde_derive
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Macros 1.1 implementation of #[derive(Serialize, Deserialize)].}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md crates-io.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+deserialize_in_place-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deserialize_in_place-devel %{_description}

This package contains library source intended for building other packages
which use "deserialize_in_place" feature of "%{crate}" crate.

%files       -n %{name}+deserialize_in_place-devel
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
* Fri Jun 19 2020 Josh Stone <jistone@redhat.com> - 1.0.113-1
- Update to 1.0.113

* Sun May 31 10:23:40 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.111-1
- Update to 1.0.111

* Sun May 10 14:21:45 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.110-1
- Update to 1.0.110

* Fri May 08 2020 Josh Stone <jistone@redhat.com> - 1.0.107-1
- Update to 1.0.107

* Sat Apr 04 2020 Josh Stone <jistone@redhat.com> - 1.0.106-1
- Update to 1.0.106

* Wed Mar 18 2020 Josh Stone <jistone@redhat.com> - 1.0.105-1
- Update to 1.0.105

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.104-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Josh Stone <jistone@redhat.com> - 1.0.104-1
- Update to 1.0.104

* Thu Nov 28 13:52:41 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.103-1
- Update to 1.0.103

* Tue Nov 19 09:40:55 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.102-1
- Update to 1.0.102

* Sat Sep 21 08:59:57 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.101-1
- Update to 1.0.101

* Sun Sep 08 15:48:58 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.100-1
- Update to 1.0.100

* Mon Aug 26 05:30:12 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.99-1
- Update to 1.0.99

* Sun Jul 28 21:27:58 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.98-1
- Update to 1.0.98

* Sun Jul 28 18:27:51 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.97-1
- Update to 1.0.97

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 12:00:48 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.94-1
- Update to 1.0.94

* Mon Jun 24 21:36:36 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.93-1
- Update to 1.0.93

* Thu Jun 20 11:47:02 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.92-3
- Regenerate

* Sun Jun 09 11:18:58 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.92-2
- Regenerate

* Fri May 31 2019 Josh Stone <jistone@redhat.com> - 1.0.92-1
- Update to 1.0.92

* Tue May 07 14:44:34 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.91-1
- Update to 1.0.91

* Wed Apr 03 2019 Josh Stone <jistone@redhat.com> - 1.0.90-1
- Update to 1.0.90

* Fri Mar 01 2019 Josh Stone <jistone@redhat.com> - 1.0.89-1
- Update to 1.0.89

* Tue Feb 19 2019 Josh Stone <jistone@redhat.com> - 1.0.88-1
- Update to 1.0.88

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.87-1
- Update to 1.0.87

* Sun Feb 03 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.86-1
- Update to 1.0.86

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.85-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.85-1
- Update to 1.0.85

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 1.0.84-1
- Update to 1.0.84

* Wed Dec 12 2018 Josh Stone <jistone@redhat.com> - 1.0.82-1
- Update to 1.0.82

* Mon Dec 10 2018 Josh Stone <jistone@redhat.com> - 1.0.81-1
- Update to 1.0.81

* Fri Oct 26 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.80-2
- Adapt to new packaging

* Mon Oct 15 2018 Josh Stone <jistone@redhat.com> - 1.0.80-1
- Update to 1.0.80

* Mon Sep 17 2018 Josh Stone <jistone@redhat.com> - 1.0.79-1
- Update to 1.0.79

* Tue Sep 11 2018 Josh Stone <jistone@redhat.com> - 1.0.78-1
- Update to 1.0.78

* Sat Sep 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.77-1
- Update to 1.0.77

* Sat Sep 08 2018 Josh Stone <jistone@redhat.com> - 1.0.76-1
- Update to 1.0.76

* Wed Aug 08 2018 Josh Stone <jistone@redhat.com> - 1.0.71-1
- Update to 1.0.71

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.70-5
- Rebuild to trigger tests

* Sat Jul 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.70-4
- Rebuild to trigger tests

* Sat Jul 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.70-3
- Run tests in infrastructure

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Josh Stone <jistone@redhat.com> - 1.0.70-1
- Update to 1.0.70

* Tue Jul 03 2018 Josh Stone <jistone@redhat.com> - 1.0.69-1
- Update to 1.0.69

* Fri Jun 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.68-1
- Update to 1.0.68

* Wed Jun 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.67-1
- Update to 1.0.67

* Thu Jun 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.66-1
- Update to 1.0.66

* Sun May 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.58-1
- Update to 1.0.58

* Sat May 19 2018 Josh Stone <jistone@redhat.com> - 1.0.56-1
- Update to 1.0.56

* Mon May 14 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.55-1
- Update to 1.0.55

* Sat May 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.54-1
- Update to 1.0.54

* Thu May 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.52-1
- Update to 1.0.52

* Wed May 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.51-1
- Update to 1.0.51

* Tue May 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.50-1
- Update to 1.0.50

* Mon May 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.47-1
- Update to 1.0.47

* Mon May 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.46-1
- Update to 1.0.46

* Wed May 02 2018 Josh Stone <jistone@redhat.com> - 1.0.45-1
- Update to 1.0.45

* Tue Apr 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.43-1
- Update to 1.0.43

* Sun Apr 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.42-1
- Update to 1.0.42

* Fri Apr 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.41-1
- Update to 1.0.41

* Tue Apr 17 2018 Josh Stone <jistone@redhat.com> - 1.0.39-1
- Update to 1.0.39

* Wed Mar 28 2018 Josh Stone <jistone@redhat.com> - 1.0.36-1
- Update to 1.0.36

* Mon Mar 26 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.35-1
- Update to 1.0.35

* Thu Mar 22 2018 Josh Stone <jistone@redhat.com> - 1.0.34-1
- Update to 1.0.34

* Sat Mar 17 2018 Josh Stone <jistone@redhat.com> - 1.0.33-1
- Update to 1.0.33

* Wed Mar 14 2018 Josh Stone <jistone@redhat.com> - 1.0.32-1
- Update to 1.0.32

* Tue Mar 13 2018 Josh Stone <jistone@redhat.com> - 1.0.30-1
- Update to 1.0.30

* Fri Mar 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.29-1
- Update to 1.0.29

* Thu Mar 08 2018 Josh Stone <jistone@redhat.com> - 1.0.28-1
- Update to 1.0.28

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.27-2
- Rebuild for rust-packaging v5

* Sun Dec 31 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.27-1
- Update to 1.0.27

* Sun Dec 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.25-1
- Update to 1.0.25

* Wed Dec 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.24-1
- Update to 1.0.24

* Thu Nov 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.23-1
- Update to 1.0.23

* Fri Nov 17 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.21-1
- Update to 1.0.21

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.20-1
- Update to 1.0.20

* Wed Nov 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.19-1
- Update to 1.0.19

* Sat Jul 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.9-1
- Update to 1.0.9

* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.12-2
- Port to use rust-packaging

* Thu Mar 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.12-1
- Update to 0.9.12

* Mon Mar 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.11-1
- Update to 0.9.11

* Wed Mar 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.10-1
- Update to 0.9.10

* Sat Feb 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.9-1
- Update to 0.9.9

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.8-1
- Update to 0.9.8

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.7-2
- Use rich dependencies

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.7-1
- Initial package
