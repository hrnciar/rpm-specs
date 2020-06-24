# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate crossbeam-deque

Name:           rust-%{crate}
Version:        0.7.3
Release:        1%{?dist}
Summary:        Concurrent work-stealing deque

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/crossbeam-deque
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Concurrent work-stealing deque.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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
* Sun Feb 23 11:23:50 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.7.3-1
- Update to 0.7.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 11:23:59 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.2-1
- Update to 0.7.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 11:50:00 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-2
- Regenerate

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.6.3-1
- Update to 0.6.3

* Sat Dec 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2

* Sun Oct 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.1-2
- Adapt to new packaging

* Sat Sep 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Sat May 05 2018 Josh Stone <jistone@redhat.com> - 0.3.1-1
- Update to 0.3.1

* Thu Mar 22 2018 Josh Stone <jistone@redhat.com> - 0.3.0-2
- Bump crossbeam-utils to 0.3

* Thu Feb 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-1
- Initial package
