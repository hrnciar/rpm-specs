# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate encoding_rs

Name:           rust-%{crate}
Version:        0.8.24
Release:        1%{?dist}
Summary:        Gecko-oriented implementation of the Encoding Standard

# Upstream license specification: Apache-2.0 OR MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/encoding_rs
Source:         %{crates_source}
# Initial patched metadata
# * Drop unneeded script, https://github.com/hsivonen/encoding_rs/pull/38
Patch0:         encoding_rs-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Gecko-oriented implementation of the Encoding Standard.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license COPYRIGHT LICENSE-MIT LICENSE-APACHE
%doc README.md CONTRIBUTING.md Ideas.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+fast-big5-hanzi-encode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fast-big5-hanzi-encode-devel %{_description}

This package contains library source intended for building other packages
which use "fast-big5-hanzi-encode" feature of "%{crate}" crate.

%files       -n %{name}+fast-big5-hanzi-encode-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+fast-gb-hanzi-encode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fast-gb-hanzi-encode-devel %{_description}

This package contains library source intended for building other packages
which use "fast-gb-hanzi-encode" feature of "%{crate}" crate.

%files       -n %{name}+fast-gb-hanzi-encode-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+fast-hangul-encode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fast-hangul-encode-devel %{_description}

This package contains library source intended for building other packages
which use "fast-hangul-encode" feature of "%{crate}" crate.

%files       -n %{name}+fast-hangul-encode-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+fast-hanja-encode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fast-hanja-encode-devel %{_description}

This package contains library source intended for building other packages
which use "fast-hanja-encode" feature of "%{crate}" crate.

%files       -n %{name}+fast-hanja-encode-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+fast-kanji-encode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fast-kanji-encode-devel %{_description}

This package contains library source intended for building other packages
which use "fast-kanji-encode" feature of "%{crate}" crate.

%files       -n %{name}+fast-kanji-encode-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+fast-legacy-encode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fast-legacy-encode-devel %{_description}

This package contains library source intended for building other packages
which use "fast-legacy-encode" feature of "%{crate}" crate.

%files       -n %{name}+fast-legacy-encode-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+less-slow-big5-hanzi-encode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+less-slow-big5-hanzi-encode-devel %{_description}

This package contains library source intended for building other packages
which use "less-slow-big5-hanzi-encode" feature of "%{crate}" crate.

%files       -n %{name}+less-slow-big5-hanzi-encode-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+less-slow-gb-hanzi-encode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+less-slow-gb-hanzi-encode-devel %{_description}

This package contains library source intended for building other packages
which use "less-slow-gb-hanzi-encode" feature of "%{crate}" crate.

%files       -n %{name}+less-slow-gb-hanzi-encode-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+less-slow-kanji-encode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+less-slow-kanji-encode-devel %{_description}

This package contains library source intended for building other packages
which use "less-slow-kanji-encode" feature of "%{crate}" crate.

%files       -n %{name}+less-slow-kanji-encode-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+packed_simd-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+packed_simd-devel %{_description}

This package contains library source intended for building other packages
which use "packed_simd" feature of "%{crate}" crate.

%files       -n %{name}+packed_simd-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+simd-accel-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+simd-accel-devel %{_description}

This package contains library source intended for building other packages
which use "simd-accel" feature of "%{crate}" crate.

%files       -n %{name}+simd-accel-devel
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
* Wed Aug 26 2020 Josh Stone <jistone@redhat.com> - 0.8.24-1
- Update to 0.8.24

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.23-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 13 2020 Josh Stone <jistone@redhat.com> - 0.8.23-1
- Update to 0.8.23

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 27 08:29:54 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.22-1
- Update to 0.8.22

* Mon Sep 16 14:01:50 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.20-1
- Update to 0.8.20

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 11:41:19 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.17-4
- Regenerate

* Sun Jun 09 00:05:11 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.17-3
- Regenerate

* Sun Mar 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.17-2
- Do not pull optional dependencies

* Wed Feb 27 2019 Josh Stone <jistone@redhat.com> - 0.8.17-1
- Update to 0.8.17

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.16-1
- Update to 0.8.16

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Josh Stone <jistone@redhat.com> - 0.8.15-1
- Update to 0.8.15

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.8.14-1
- Update to 0.8.14

* Thu Nov 29 2018 Josh Stone <jistone@redhat.com> - 0.8.13-1
- Update to 0.8.13

* Sun Nov 18 2018 Josh Stone <jistone@redhat.com> - 0.8.12-1
- Update to 0.8.12

* Fri Nov 16 2018 Josh Stone <jistone@redhat.com> - 0.8.11-1
- Update to 0.8.11

* Sun Oct 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.10-2
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.10-1
- Update to 0.8.10

* Thu Oct 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.9-1
- Update to 0.8.9

* Mon Oct 01 2018 Josh Stone <jistone@redhat.com> - 0.8.8-1
- Update to 0.8.8

* Thu Sep 27 2018 Josh Stone <jistone@redhat.com> - 0.8.7-1
- Update to 0.8.7

* Mon Aug 13 2018 Josh Stone <jistone@redhat.com> - 0.8.6-1
- Update to 0.8.6

* Fri Aug 10 2018 Josh Stone <jistone@redhat.com> - 0.8.5-1
- Update to 0.8.5

* Sun Jul 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.4-1
- Update to 0.8.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.2-1
- Update to 0.7.2

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-2
- Rebuild for rust-packaging v5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.11-1
- Update to 0.6.11

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-2
- Port to use rust-packaging

* Wed Mar 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Initial package
