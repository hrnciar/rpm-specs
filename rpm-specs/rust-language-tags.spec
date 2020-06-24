# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate language-tags

Name:           rust-%{crate}
Version:        0.2.2
Release:        8%{?dist}
Summary:        Language tags for Rust

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/language-tags
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Language tags for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+heap_size-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+heap_size-devel %{_description}

This package contains library source intended for building other packages
which use "heap_size" feature of "%{crate}" crate.

%files       -n %{name}+heap_size-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+heapsize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+heapsize-devel %{_description}

This package contains library source intended for building other packages
which use "heapsize" feature of "%{crate}" crate.

%files       -n %{name}+heapsize-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+heapsize_plugin-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+heapsize_plugin-devel %{_description}

This package contains library source intended for building other packages
which use "heapsize_plugin" feature of "%{crate}" crate.

%files       -n %{name}+heapsize_plugin-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
# Treating warnings as errors is bad idea
sed -i -e '/#!\[.*deny(warnings).*\]/d' src/lib.rs
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 16:45:12 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-6
- Regenerate

* Thu Mar 14 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-5
- Adapt to new packaging

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Josh Stone <jistone@redhat.com> - 0.2.2-3
- Adapt to new packaging

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-1
- Initial package
