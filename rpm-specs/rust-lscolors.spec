# Generated by rust2rpm 13
%bcond_without check

%global crate lscolors

Name:           rust-%{crate}
Version:        0.7.1
Release:        1%{?dist}
Summary:        Colorize paths using the LS_COLORS environment variable

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/lscolors
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Colorize paths using the LS_COLORS environment variable.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE-APACHE LICENSE-MIT
%doc README.md
%{_bindir}/lscolors
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
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

%package     -n %{name}+ansi_term-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ansi_term-devel %{_description}

This package contains library source intended for building other packages
which use "ansi_term" feature of "%{crate}" crate.

%files       -n %{name}+ansi_term-devel
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
* Fri Jun 19 2020 Josh Stone <jistone@redhat.com> - 0.7.1-1
- Update to 0.7.1

* Thu Apr 16 11:47:54 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 21 13:10:53 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 21:20:42 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-3
- Regenerate

* Sun Jun 09 19:56:47 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-2
- Regenerate

* Thu Apr 25 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.0-1
- Initial package