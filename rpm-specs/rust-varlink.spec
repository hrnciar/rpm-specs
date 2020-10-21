# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate varlink

Name:           rust-%{crate}
Version:        11.0.0
Release:        2%{?dist}
Summary:        Client and server support for the varlink protocol

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/varlink
Source:         %{crates_source}
# Initial patched metadata
# * No windows deps
Patch0:         varlink-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Client and server support for the varlink protocol.}

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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Josh Stone <jistone@redhat.com> - 11.0.0-1
- Update to 11.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 15:07:31 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 10.0.0-1
- Update to 10.0.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.0.1-1
- Update to 7.0.1

* Sat Feb 16 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.0.0-1
- Update to 7.0.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Josh Stone <jistone@redhat.com> - 5.3.0-1
- Update to 5.3.0

* Wed Dec 12 2018 Josh Stone <jistone@redhat.com> - 5.2.0-1
- Update to 5.2.0

* Mon Dec 10 2018 Josh Stone <jistone@redhat.com> - 5.1.0-1
- Update to 5.1.0

* Mon Nov 26 2018 Josh Stone <jistone@redhat.com> - 5.0.1-1
- Update to 5.0.1

* Sat Nov 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.0.0-2
- Adapt to new packaging

* Sun Sep 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.0.0-1
- Update to 5.0.0

* Thu Aug 09 2018 Josh Stone <jistone@redhat.com> - 3.1.0-1
- Update to 3.1.0

* Sat Aug 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1

* Mon Jul 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Initial package
