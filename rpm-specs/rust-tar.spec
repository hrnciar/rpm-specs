# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate tar

Name:           rust-%{crate}
Version:        0.4.30
Release:        1%{?dist}
Summary:        Rust implementation of a TAR file reader and writer

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/tar
Source:         %{crates_source}
# Initial patched metadata
# * No redox
Patch0:         tar-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust implementation of a TAR file reader and writer. This library does not
currently handle compression, but it is abstract over all I/O readers and
writers. Additionally, great lengths are taken to ensure that the entire
contents are never required to be entirely resident in memory all at once.}

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

%package     -n %{name}+xattr-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xattr-devel %{_description}

This package contains library source intended for building other packages
which use "xattr" feature of "%{crate}" crate.

%files       -n %{name}+xattr-devel
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
# Test files are not shipped
%cargo_test -- --doc
%endif

%changelog
* Tue Sep 01 2020 Josh Stone <jistone@redhat.com> - 0.4.30-1
- Update to 0.4.30

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.29-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Josh Stone <jistone@redhat.com> - 0.4.29-1
- Update to 0.4.29

* Fri May 22 2020 Josh Stone <jistone@redhat.com> - 0.4.28-1
- Update to 0.4.28

* Thu May 21 2020 Josh Stone <jistone@redhat.com> - 0.4.27-1
- Update to 0.4.27

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 16:14:23 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.26-2
- Regenerate

* Fri May 31 2019 Josh Stone <jistone@redhat.com> - 0.4.26-1
- Update to 0.4.26

* Sun May 12 11:17:06 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.25-1
- Update to 0.4.25

* Mon Apr 29 20:43:52 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.24-1
- Update to 0.4.24

* Tue Apr 23 19:12:30 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.23-1
- Update to 0.4.23

* Thu Mar 14 2019 Josh Stone <jistone@redhat.com> - 0.4.22-1
- Update to 0.4.22

* Tue Mar 05 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.21-1
- Update to 0.4.21

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Josh Stone <jistone@redhat.com> - 0.4.20-1
- Update to 0.4.20

* Tue Nov 13 2018 Josh Stone <jistone@redhat.com> - 0.4.19-1
- Update to 0.4.19
- Adapt to new packaging

* Fri Sep 28 2018 Josh Stone <jistone@redhat.com> - 0.4.17-1
- Update to 0.4.17

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Josh Stone <jistone@redhat.com> - 0.4.16-1
- Update to 0.4.16

* Wed Apr 25 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.15-1
- Update to 0.4.15

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.14-1
- Update to 0.4.14

* Mon Jul 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.13-1
- Initial package
