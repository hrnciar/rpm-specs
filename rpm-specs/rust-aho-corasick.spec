# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate aho-corasick

Name:           rust-%{crate}
Version:        0.7.13
Release:        2%{?dist}
Summary:        Fast multiple substring searching

# Upstream license specification: Unlicense/MIT
License:        Unlicense or MIT
URL:            https://crates.io/crates/aho-corasick
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Fast multiple substring searching.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license UNLICENSE LICENSE-MIT COPYING
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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Josh Stone <jistone@redhat.com> - 0.7.13-1
- Update to 0.7.13

* Tue Mar 10 2020 Josh Stone <jistone@redhat.com> - 0.7.10-1
- Update to 0.7.10

* Thu Feb 27 2020 Josh Stone <jistone@redhat.com> - 0.7.9-1
- Update to 0.7.9

* Thu Feb 06 2020 Josh Stone <jistone@redhat.com> - 0.7.8-1
- Update to 0.7.8

* Thu Jan 30 2020 Josh Stone <jistone@redhat.com> - 0.7.7-1
- Update to 0.7.7

* Sun Aug 04 06:57:02 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.6-1
- Update to 0.7.6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 06 11:24:53 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.4-1
- Update to 0.7.4

* Thu Jun 20 11:37:44 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.3-3
- Regenerate

* Sat Jun 08 23:40:01 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.3-2
- Regenerate

* Wed Apr 03 2019 Josh Stone <jistone@redhat.com> - 0.7.3-1
- Update to 0.7.3

* Sat Feb 16 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.10-1
- Update to 0.6.10

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Josh Stone <jistone@redhat.com> - 0.6.9-1
- Update to 0.6.9

* Sat Oct 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.8-2
- Adapt to new packaging

* Thu Aug 30 2018 Josh Stone <jistone@redhat.com> - 0.6.8-1
- Update to 0.6.8

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.6-3
- Rebuild to trigger tests

* Sat Jul 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.6-2
- Run tests in infrastructure

* Fri Jul 13 2018 Josh Stone <jistone@redhat.com> - 0.6.6-1
- Update to 0.6.6

* Thu Jun 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.5-1
- Update to 0.6.5

* Thu Jun 14 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.4-5
- Bump docopt to 1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.4-3
- Rebuild for rust-packaging v5

* Mon Jan 01 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.4-2
- Bump quickcheck to 0.6
- Bump rand to 0.4

* Thu Nov 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.4-1
- Update to 0.6.4

* Wed Nov 29 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.3-5
- Bump quickcheck to 0.5

* Fri Nov 10 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.3-4
- Exclude more unneeded files

* Wed Nov 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.3-3
- Bump memchr to 2

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.3-2
- Port to use rust-packaging

* Thu Mar 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.3-1
- Update to 0.6.3

* Sat Mar 11 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.2-3
- Rename with rust prefix
- Don't ship useless binary

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.2-2
- Use rich dependencies

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.2-1
- Initial package
