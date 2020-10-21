# Generated by rust2rpm 12
%bcond_without check
%global debug_package %{nil}

%global crate term

Name:           rust-%{crate}
Version:        0.6.1
Release:        4%{?dist}
Summary:        Terminal formatting library

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/term
Source:         %{crates_source}
# Initial patched metadata
# * No windows
Patch0:         term-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Terminal formatting library.}

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
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 03:09:16 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.1-1
- Update to 0.6.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 12:55:07 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.2-2
- Update dirs to 2.0.1

* Thu Mar 28 23:33:27 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2

* Thu Mar 14 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-7
- Adapt to new packaging

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-5
- Exclude CI files

* Sat Nov 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.1-4
- Adapt to new packaging

* Tue Sep 18 2018 Josh Stone <jistone@redhat.com> - 0.5.1-3
- Fix env::home_dir deprecation

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.6-4
- Rebuild for rust-packaging v5

* Sat Oct 21 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.6-3
- Rebuild to get dependency on cargo

* Sat Sep 23 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.6-2
- Exclude unneeded files

* Sun Jun 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.6-1
- Update to 0.4.6

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.5-2
- Port to use rust-packaging

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.5-1
- Initial package
