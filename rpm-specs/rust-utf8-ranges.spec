# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate utf8-ranges

Name:           rust-%{crate}
Version:        1.0.4
Release:        4%{?dist}
Summary:        Convert ranges of Unicode codepoints to UTF-8 byte ranges

# Upstream license specification: Unlicense/MIT
License:        Unlicense or MIT
URL:            https://crates.io/crates/utf8-ranges
Source:         %{crates_source}
# Initial patched metadata
# - Bump quicheck to 0.9
Patch0:         utf8-ranges-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Convert ranges of Unicode codepoints to UTF-8 byte ranges.
DEPRECATED. Use regex-syntax::utf8 submodule instead.}

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
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 22:20:26 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.4-2
- Bump quicheck to 0.9

* Sun Aug 04 07:21:26 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 11:36:33 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-2
- Regenerate

* Sun Jun 09 17:20:05 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Sun Jun 09 12:27:00 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-4
- Fix skip_build

* Sun Jun 09 10:03:32 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-3
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Josh Stone <jistone@redhat.com> - 1.0.2-1
- Update to 1.0.2

* Sat Oct 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-2
- Adapt to new packaging

* Thu Aug 30 2018 Josh Stone <jistone@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-10
- Rebuild to trigger tests

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-7
- Rebuild for rust-packaging v5

* Mon Jan 01 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-6
- Bump quickcheck to 0.6

* Wed Nov 29 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-5
- Bump quickcheck to 0.5
- Enable tests

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-4
- Exclude unneeded files

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-3
- Port to use rust-packaging

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-2
- Use rich dependencies

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Initial package
