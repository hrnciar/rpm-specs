# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate termcolor

Name:           rust-%{crate}
Version:        1.1.0
Release:        2%{?dist}
Summary:        Simple cross platform library for writing colored text to a terminal

# Upstream license specification: Unlicense OR MIT
License:        Unlicense or MIT
URL:            https://crates.io/crates/termcolor
Source:         %{crates_source}
# Initial patched metadata
# * No windows
Patch0:         termcolor-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Simple cross platform library for writing colored text to a terminal.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license COPYING UNLICENSE LICENSE-MIT
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 1.1.0-1
- Update to 1.1.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 09:38:57 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.5-3
- Regenerate

* Sun Jun 09 11:12:29 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.5-2
- Regenerate

* Tue Jun 04 2019 Josh Stone <jistone@redhat.com> - 1.0.5-1
- Update to 1.0.5

* Sun Mar 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.4-4
- Adapt to new packaging

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.4-2
- Adapt to new packaging

* Mon Sep 17 2018 Josh Stone <jistone@redhat.com> - 1.0.4-1
- Update to 1.0.4

* Fri Sep 07 2018 Josh Stone <jistone@redhat.com> - 1.0.3-1
- Update to 1.0.3

* Sun Jul 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Thu Jul 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Josh Stone <jistone@redhat.com> - 0.3.6-1
- Update to 0.3.6

* Wed Feb 21 2018 Josh Stone <jistone@redhat.com> - 0.3.5-1
- Update to 0.3.5

* Mon Feb 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.4-1
- Update to 0.3.4

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.3-3
- Rebuild for rust-packaging v5

* Sat Oct 21 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.3-2
- Rebuild to get dependency on cargo

* Fri Sep 22 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.3-1
- Update to 0.3.3

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-2
- Port to use rust-packaging

* Wed Mar 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Wed Mar 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-1
- Initial package
