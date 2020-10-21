# Generated by rust2rpm 13
# * Tests do not work out-of-tree
%bcond_with check
%global debug_package %{nil}

%global crate futures-util

Name:           rust-%{crate}
Version:        0.3.6
Release:        1%{?dist}
Summary:        Common utilities and extension traits for the futures-rs library

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/futures-util
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Common utilities and extension traits for the futures-rs library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages
which use "alloc" feature of "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+async-await-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-await-devel %{_description}

This package contains library source intended for building other packages
which use "async-await" feature of "%{crate}" crate.

%files       -n %{name}+async-await-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+async-await-macro-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-await-macro-devel %{_description}

This package contains library source intended for building other packages
which use "async-await-macro" feature of "%{crate}" crate.

%files       -n %{name}+async-await-macro-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+bilock-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bilock-devel %{_description}

This package contains library source intended for building other packages
which use "bilock" feature of "%{crate}" crate.

%files       -n %{name}+bilock-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+cfg-target-has-atomic-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cfg-target-has-atomic-devel %{_description}

This package contains library source intended for building other packages
which use "cfg-target-has-atomic" feature of "%{crate}" crate.

%files       -n %{name}+cfg-target-has-atomic-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+channel-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+channel-devel %{_description}

This package contains library source intended for building other packages
which use "channel" feature of "%{crate}" crate.

%files       -n %{name}+channel-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+compat-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compat-devel %{_description}

This package contains library source intended for building other packages
which use "compat" feature of "%{crate}" crate.

%files       -n %{name}+compat-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-channel-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-channel-devel %{_description}

This package contains library source intended for building other packages
which use "futures-channel" feature of "%{crate}" crate.

%files       -n %{name}+futures-channel-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-io-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-io-devel %{_description}

This package contains library source intended for building other packages
which use "futures-io" feature of "%{crate}" crate.

%files       -n %{name}+futures-io-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-macro-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-macro-devel %{_description}

This package contains library source intended for building other packages
which use "futures-macro" feature of "%{crate}" crate.

%files       -n %{name}+futures-macro-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-sink-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-sink-devel %{_description}

This package contains library source intended for building other packages
which use "futures-sink" feature of "%{crate}" crate.

%files       -n %{name}+futures-sink-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures_01-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures_01-devel %{_description}

This package contains library source intended for building other packages
which use "futures_01" feature of "%{crate}" crate.

%files       -n %{name}+futures_01-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+io-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+io-devel %{_description}

This package contains library source intended for building other packages
which use "io" feature of "%{crate}" crate.

%files       -n %{name}+io-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+io-compat-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+io-compat-devel %{_description}

This package contains library source intended for building other packages
which use "io-compat" feature of "%{crate}" crate.

%files       -n %{name}+io-compat-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+memchr-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+memchr-devel %{_description}

This package contains library source intended for building other packages
which use "memchr" feature of "%{crate}" crate.

%files       -n %{name}+memchr-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+proc-macro-hack-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+proc-macro-hack-devel %{_description}

This package contains library source intended for building other packages
which use "proc-macro-hack" feature of "%{crate}" crate.

%files       -n %{name}+proc-macro-hack-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+proc-macro-nested-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+proc-macro-nested-devel %{_description}

This package contains library source intended for building other packages
which use "proc-macro-nested" feature of "%{crate}" crate.

%files       -n %{name}+proc-macro-nested-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+read-initializer-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+read-initializer-devel %{_description}

This package contains library source intended for building other packages
which use "read-initializer" feature of "%{crate}" crate.

%files       -n %{name}+read-initializer-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+sink-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sink-devel %{_description}

This package contains library source intended for building other packages
which use "sink" feature of "%{crate}" crate.

%files       -n %{name}+sink-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+slab-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+slab-devel %{_description}

This package contains library source intended for building other packages
which use "slab" feature of "%{crate}" crate.

%files       -n %{name}+slab-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-io-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-io-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-io" feature of "%{crate}" crate.

%files       -n %{name}+tokio-io-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages
which use "unstable" feature of "%{crate}" crate.

%files       -n %{name}+unstable-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+write-all-vectored-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+write-all-vectored-devel %{_description}

This package contains library source intended for building other packages
which use "write-all-vectored" feature of "%{crate}" crate.

%files       -n %{name}+write-all-vectored-devel
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
* Wed Oct 07 2020 Fabio Valentini <decathorpe@gmail.com> - 0.3.6-1
- Update to version 0.3.6.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 09 2020 Josh Stone <jistone@redhat.com> - 0.3.5-1
- Update to 0.3.5

* Tue Feb 18 10:52:47 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.3.4-2
- Regenerate

* Mon Feb 10 2020 Josh Stone <jistone@redhat.com> - 0.3.4-1
- Update to 0.3.4

* Thu Feb 06 2020 Josh Stone <jistone@redhat.com> - 0.3.3-1
- Update to 0.3.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 19:08:21 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-2
- Regenerate

* Fri Dec 13 22:50:30 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.1-1
- Initial package
