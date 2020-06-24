# Generated by rust2rpm
%bcond_with check
%global debug_package %{nil}

%global crate env_logger

Name:           rust-%{crate}0.4
Version:        0.4.3
Release:        9%{?dist}
Summary:        Logging implementation for `log` which is configured via environment variable

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/env_logger
Source:         %{crates_source}
# Initial patched metadata
# * Bump regex to 1
Patch0:         env_logger-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(log/default) >= 0.3.0 with crate(log/default) < 0.4.0)
BuildRequires:  (crate(regex/default) >= 1.0.0 with crate(regex/default) < 2.0.0)

%global _description \
A logging implementation for `log` which is configured via an environment\
variable.

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+regex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+regex-devel %{_description}

This package contains library source intended for building other packages
which use "regex" feature of "%{crate}" crate.

%files       -n %{name}+regex-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.3-7
- Adapt to new packaging

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.3-4
- Bump regex to 1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.3-2
- Rebuild for rust-packaging v5

* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.3-1
- Update to 0.4.3

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-2
- Port to use rust-packaging

* Wed Mar 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Sat Feb 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-1
- Initial package