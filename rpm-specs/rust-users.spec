# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate users

Name:           rust-%{crate}
Version:        0.10.0
Release:        2%{?dist}
Summary:        Library for accessing Unix users and groups

# Upstream license specification: MIT
# https://github.com/ogham/rust-users/pull/37
License:        MIT
URL:            https://crates.io/crates/users
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library for accessing Unix users and groups.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+cache-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cache-devel %{_description}

This package contains library source intended for building other packages
which use "cache" feature of "%{crate}" crate.

%files       -n %{name}+cache-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+log-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+log-devel %{_description}

This package contains library source intended for building other packages
which use "log" feature of "%{crate}" crate.

%files       -n %{name}+log-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+logging-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+logging-devel %{_description}

This package contains library source intended for building other packages
which use "logging" feature of "%{crate}" crate.

%files       -n %{name}+logging-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+mock-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mock-devel %{_description}

This package contains library source intended for building other packages
which use "mock" feature of "%{crate}" crate.

%files       -n %{name}+mock-devel
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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 11:29:29 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 22:03:57 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.1-3
- Regenerate

* Sun Jun 09 21:43:48 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.1-2
- Regenerate

* Thu Apr 25 16:30:58 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.9.1-1
- Update to 0.9.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-3
- Adapt to new packaging

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Sun Mar 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-2
- Rebuild for rust-packaging v5

* Sat Nov 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-1
- Initial package
