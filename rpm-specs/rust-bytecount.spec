# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate bytecount

Name:           rust-%{crate}
Version:        0.6.0
Release:        2%{?dist}
Summary:        Count occurrences of a given byte, or the number of UTF-8 code points, in a byte slice, fast

# Upstream license specification: Apache-2.0/MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/bytecount
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Count occurrences of a given byte, or the number of UTF-8 code points, in a
byte slice, fast.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE.Apache2 LICENSE.MIT
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

%package     -n %{name}+generic-simd-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+generic-simd-devel %{_description}

This package contains library source intended for building other packages
which use "generic-simd" feature of "%{crate}" crate.

%files       -n %{name}+generic-simd-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+html_report-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+html_report-devel %{_description}

This package contains library source intended for building other packages
which use "html_report" feature of "%{crate}" crate.

%files       -n %{name}+html_report-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+packed_simd-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+packed_simd-devel %{_description}

This package contains library source intended for building other packages
which use "packed_simd" feature of "%{crate}" crate.

%files       -n %{name}+packed_simd-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+runtime-dispatch-simd-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+runtime-dispatch-simd-devel %{_description}

This package contains library source intended for building other packages
which use "runtime-dispatch-simd" feature of "%{crate}" crate.

%files       -n %{name}+runtime-dispatch-simd-devel
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 17:35:02 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.0-1
- Update to 0.6.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 16:53:52 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-4
- Regenerate

* Sun Jun 09 12:26:22 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-3
- Fix skip_build

* Sat Jun 08 23:49:59 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-2
- Regenerate

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-2
- Adapt to new packaging

* Fri Aug 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Tue Jan 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-4
- Rebuild for rust-packaging v5

* Sun Dec 31 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-3
- Bump rand to 0.4
- Bump quickcheck to 0.6

* Sat Dec 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-2
- Bump quickcheck to 0.5

* Fri Nov 10 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Fri Jul 21 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7

* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.6-3
- Relax quickcheck version

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.6-2
- Port to use rust-packaging

* Sat Feb 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.6-1
- Initial package