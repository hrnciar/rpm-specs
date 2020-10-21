# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate openssl-sys

Name:           rust-%{crate}
Version:        0.9.58
Release:        2%{?dist}
Summary:        FFI bindings to OpenSSL

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/openssl-sys
Source:         %{crates_source}
# Initial patched metadata
# * No windows
Patch0:         openssl-sys-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
FFI bindings to OpenSSL.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(openssl) >= 1.0.1

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT
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

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(openssl) >= 1.0.1'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Josh Stone <jistone@redhat.com> - 0.9.58-1
- Update to 0.9.58

* Tue May 26 2020 Josh Stone <jistone@redhat.com> - 0.9.57-1
- Update to 0.9.57

* Fri May 08 2020 Josh Stone <jistone@redhat.com> - 0.9.56-1
- Update to 0.9.56

* Wed Apr 08 2020 Josh Stone <jistone@redhat.com> - 0.9.55-1
- Update to 0.9.55

* Thu Jan 30 2020 Josh Stone <jistone@redhat.com> - 0.9.54-1
- Update to 0.9.54

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.9.53-2
- Bump to autocfg 1

* Sat Nov 23 2019 Josh Stone <jistone@redhat.com> - 0.9.53-1
- Update to 0.9.53

* Tue Nov 19 2019 Josh Stone <jistone@redhat.com> - 0.9.52-1
- Update to 0.9.52

* Sat Sep 21 13:14:23 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.49-1
- Update to 0.9.49

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 12:25:59 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.47-2
- Regenerate

* Fri May 31 2019 Josh Stone <jistone@redhat.com> - 0.9.47-1
- Update to 0.9.47

* Thu May 09 2019 Josh Stone <jistone@redhat.com> - 0.9.46-1
- Update to 0.9.46

* Thu May 02 2019 Josh Stone <jistone@redhat.com> - 0.9.44-1
- Update to 0.9.44

* Fri Mar 22 2019 Josh Stone <jistone@redhat.com> - 0.9.43-1
- Update to 0.9.43

* Thu Mar 14 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.42-2
- Adapt to new packaging

* Fri Mar 01 2019 Josh Stone <jistone@redhat.com> - 0.9.42-1
- Update to 0.9.42

* Fri Feb 22 2019 Josh Stone <jistone@redhat.com> - 0.9.41-1
- Update to 0.9.41

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.9.40-1
- Update to 0.9.40

* Sat Nov 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.39-2
- Adapt to new packaging

* Mon Oct 22 2018 Josh Stone <jistone@redhat.com> - 0.9.39-1
- Update to 0.9.39

* Mon Sep 17 2018 Josh Stone <jistone@redhat.com> - 0.9.36-1
- Update to 0.9.36

* Tue Aug 07 2018 Josh Stone <jistone@redhat.com> - 0.9.35-1
- Update to 0.9.35

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.33-1
- Update to 0.9.33

* Tue Jun 05 2018 Josh Stone <jistone@redhat.com> - 0.9.32-1
- Update to 0.9.32

* Tue May 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.31-1
- Update to 0.9.31

* Wed May 02 2018 Josh Stone <jistone@redhat.com> - 0.9.30-1
- Update to 0.9.30

* Fri Apr 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.28-1
- Update to 0.9.28

* Thu Mar 01 2018 Josh Stone <jistone@redhat.com> - 0.9.27-1
- Update to 0.9.27

* Mon Feb 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.26-1
- Update to 0.9.26

* Thu Feb 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.25-1
- Update to 0.9.25

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.24-1
- Update to 0.9.24

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.23-2
- Rebuild for rust-packaging v5

* Wed Dec 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.23-1
- Update to 0.9.23

* Thu Nov 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.22-1
- Update to 0.9.22

* Sun Nov 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.21-1
- Update to 0.9.21

* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.14-1
- Update to 0.9.14

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.10-2
- Port to use rust-packaging

* Mon Apr 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.10-1
- Update to 0.9.10

* Wed Mar 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.9-1
- Update to 0.9.9

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.7-2
- Rebuild

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.7-1
- Initial package
