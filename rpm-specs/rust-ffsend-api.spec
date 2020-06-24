# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate ffsend-api

Name:           rust-%{crate}
Version:        0.6.0
Release:        1%{?dist}
Summary:        Fully featured Firefox Send API client

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/ffsend-api
Source:         %{crates_source}
# Initial patched metadata
# * OpenSSL by default
Patch0:         ffsend-api-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Fully featured Firefox Send API client.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
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

%package     -n %{name}+crypto-openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crypto-openssl-devel %{_description}

This package contains library source intended for building other packages
which use "crypto-openssl" feature of "%{crate}" crate.

%files       -n %{name}+crypto-openssl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+crypto-ring-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crypto-ring-devel %{_description}

This package contains library source intended for building other packages
which use "crypto-ring" feature of "%{crate}" crate.

%files       -n %{name}+crypto-ring-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+openssl-devel %{_description}

This package contains library source intended for building other packages
which use "openssl" feature of "%{crate}" crate.

%files       -n %{name}+openssl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ring-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ring-devel %{_description}

This package contains library source intended for building other packages
which use "ring" feature of "%{crate}" crate.

%files       -n %{name}+ring-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+send2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+send2-devel %{_description}

This package contains library source intended for building other packages
which use "send2" feature of "%{crate}" crate.

%files       -n %{name}+send2-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+send3-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+send3-devel %{_description}

This package contains library source intended for building other packages
which use "send3" feature of "%{crate}" crate.

%files       -n %{name}+send3-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+websocket-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+websocket-devel %{_description}

This package contains library source intended for building other packages
which use "websocket" feature of "%{crate}" crate.

%files       -n %{name}+websocket-devel
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
* Sun May 17 18:45:57 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Wed Apr 29 2020 Josh Stone <jistone@redhat.com> - 0.5.1-1
- Update to 0.5.1

* Wed Mar 04 2020 Josh Stone <jistone@redhat.com> - 0.5.0-2
- Bump to hkdf 0.8

* Sun Feb 16 09:08:51 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 05 15:30:21 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4

* Thu Dec 05 14:35:26 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 13:06:05 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-3
- Regenerate

* Fri Apr 19 09:20:28 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-2
- Update version-compare to 0.0.8

* Fri Apr 05 17:23:05 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Wed Mar 20 2019 Josh Stone <jistone@redhat.com> - 0.3.0-1
- Update to 0.3.0

* Wed Mar 13 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3-1
- Initial package
