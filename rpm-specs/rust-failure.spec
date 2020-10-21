# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate failure

Name:           rust-%{crate}
Version:        0.1.8
Release:        2%{?dist}
Summary:        Experimental error handling abstraction

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/failure
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Experimental error handling abstraction.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md RELEASES.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/
%exclude %{cargo_registry}/%{crate}-%{version_no_tilde}/build-docs.sh

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+backtrace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backtrace-devel %{_description}

This package contains library source intended for building other packages
which use "backtrace" feature of "%{crate}" crate.

%files       -n %{name}+backtrace-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+derive-devel %{_description}

This package contains library source intended for building other packages
which use "derive" feature of "%{crate}" crate.

%files       -n %{name}+derive-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+failure_derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+failure_derive-devel %{_description}

This package contains library source intended for building other packages
which use "failure_derive" feature of "%{crate}" crate.

%files       -n %{name}+failure_derive-devel
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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Josh Stone <cuviper@gmail.com> - 0.1.8-1
- Update to 0.1.8

* Thu Mar 05 2020 Josh Stone <jistone@redhat.com> - 0.1.7-1
- Update to 0.1.7

* Sat Nov 23 2019 Josh Stone <jistone@redhat.com> - 0.1.6-1
- Update to 0.1.6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 12:43:12 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-4
- Regenerate

* Mon Apr 15 20:23:42 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.5-3
- Add patch to fix compilation with Rust 1.34

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.1.5-1
- Update to 0.1.5

* Sat Nov 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.3-2
- Adapt to new packaging

* Mon Oct 22 2018 Josh Stone <jistone@redhat.com> - 0.1.3-1
- Update to 0.1.3

* Sat Aug 04 2018 Josh Stone <jistone@redhat.com> - 0.1.2-1
- Update to 0.1.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-2
- Rebuild for rust-packaging v5

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-1
- Initial package
