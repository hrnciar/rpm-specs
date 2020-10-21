# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate gdk-pixbuf-sys

Name:           rust-%{crate}
Version:        0.10.0
Release:        2%{?dist}
Summary:        FFI bindings to libgdk_pixbuf-2.0

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/gdk-pixbuf-sys
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
FFI bindings to libgdk_pixbuf-2.0.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gdk-pixbuf-2.0) >= 2.30

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dox-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dox-devel %{_description}

This package contains library source intended for building other packages
which use "dox" feature of "%{crate}" crate.

%files       -n %{name}+dox-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v2_32-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gdk-pixbuf-2.0) >= 2.32

%description -n %{name}+v2_32-devel %{_description}

This package contains library source intended for building other packages
which use "v2_32" feature of "%{crate}" crate.

%files       -n %{name}+v2_32-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v2_36-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gdk-pixbuf-2.0) >= 2.36

%description -n %{name}+v2_36-devel %{_description}

This package contains library source intended for building other packages
which use "v2_36" feature of "%{crate}" crate.

%files       -n %{name}+v2_36-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v2_36_8-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gdk-pixbuf-2.0) >= 2.36.8

%description -n %{name}+v2_36_8-devel %{_description}

This package contains library source intended for building other packages
which use "v2_36_8" feature of "%{crate}" crate.

%files       -n %{name}+v2_36_8-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v2_40-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gdk-pixbuf-2.0) >= 2.40

%description -n %{name}+v2_40-devel %{_description}

This package contains library source intended for building other packages
which use "v2_40" feature of "%{crate}" crate.

%files       -n %{name}+v2_40-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(gdk-pixbuf-2.0) >= 2.30'

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

* Thu Jul 09 2020 Josh Stone <jistone@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.9.1-2
- Fix new subpackage requirements.

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.9.1-1
- Update to 0.9.1

* Tue Dec 10 2019 Josh Stone <jistone@redhat.com> - 0.9.0-1
- Update to 0.9.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 14:20:38 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Tue Feb 12 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-2
- Rebuild for rust-packaging v5

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Initial package
