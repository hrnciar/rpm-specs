# The check need root privilege
%bcond_with check

Name:           nispor
Version:        0.6.1
Release:        2%{?dist}
Summary:        Unified interface for Linux network state querying
License:        ASL 2.0
URL:            https://github.com/nispor/nispor
Source:         https://github.com/nispor/nispor/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
ExclusiveArch:  %{rust_arches}
BuildRequires:  pkg-config
BuildRequires:  python3-devel
BuildRequires:  rust-packaging
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  (crate(serde/default) >= 1.0 with crate(serde/default) < 2.0)
BuildRequires:  (crate(serde_derive/default) >= 1.0 with crate(serde_derive/default) < 2.0)
BuildRequires:  (crate(serde_json/default) >= 1.0 with crate(serde_json/default) < 2.0)
BuildRequires:  (crate(rtnetlink/default) >= 0.5.0 with crate(rtnetlink/default) < 0.6.0)
BuildRequires:  (crate(netlink-packet-route/default) >= 0.5.0 with crate(netlink-packet-route/default) < 0.6.0)
BuildRequires:  (crate(netlink-packet-utils/default) >= 0.3.0 with crate(netlink-packet-utils/default) < 0.4.0)
BuildRequires:  (crate(netlink-sys/default) >= 0.4.0 with crate(netlink-sys/default) < 0.5.0)
BuildRequires:  (crate(tokio/macros) >= 0.2.0 with crate(tokio/macros) < 0.3.0)
BuildRequires:  (crate(tokio/rt-core) >= 0.2.0 with crate(tokio/rt-core) < 0.3.0)
BuildRequires:  (crate(varlink/default) >= 11 with crate(varlink/default) < 12)
BuildRequires:  (crate(libc/default) >= 0.2.74 with crate(libc/default) < 0.3.0)

%description
Unified interface for Linux network state querying.

%package -n     rust-%{name}-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-%{name}-devel

This package contains library source intended for building other packages
which use "%{name}" crate.

%package -n     rust-%{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-%{name}+default-devel

This package contains library source intended for building other packages
which use "%{name}" crate with default feature.

%package -n     python3-%{name}
Summary:        %{summary}
Requires:       nispor = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch:      noarch

%description -n python3-%{name}

This package contains python3 binding of %{name}.

%package        devel
Summary:        %{summary}
Requires:       nispor%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel

This package contains C binding of %{name}.

%prep
%autosetup -n %{name}-%{version_no_tilde} -p1

%cargo_prep
for sub_dir in lib cli clib varlink;do
    pushd src/$sub_dir
    %cargo_prep
    popd
done

# The cargo_prep will create `.cargo/config` which take precedence over
# `.cargo/config.toml` shipped by upstream which fix the SONAME of cdylib.
# To workaround that, merge upstream rustflags into cargo_prep created one.
_FLAGS=`sed -ne 's/rustflags = "\(.\+\)"/\1/p' .cargo/config.toml`
sed -i -e "s/rustflags = \[\(.\+\), \]$/rustflags = [\1, \"$_FLAGS\"]/" \
    .cargo/config

%build
for sub_dir in lib cli clib varlink;do
    pushd src/$sub_dir
    %cargo_build
    popd
done

pushd src/python
%py3_build
popd

%install

pushd src/lib
%cargo_install
popd

env SKIP_PYTHON_INSTALL=1 PREFIX=%{_prefix} LIBDIR=%{_libdir} %make_install

pushd src/python
%py3_install
popd


%if %{with check}
%check
%cargo_test
%endif

%files
%doc AUTHORS CHANGELOG DEVEL.md README.md
%license LICENSE
%{_bindir}/npc
%{_bindir}/npd
%{_libdir}/libnispor.so.*
%{_unitdir}/nispor.socket
%{_unitdir}/nispor.service

%files -n       python3-%{name}
%license LICENSE
%{python3_sitelib}/nispor*

%files devel
%license LICENSE
%{_libdir}/libnispor.so
%{_includedir}/nispor.h

%files -n       rust-%{name}-devel
%license LICENSE
%{cargo_registry}/%{name}-%{version_no_tilde}/

%files -n       rust-%{name}+default-devel
%ghost %{cargo_registry}/%{name}-%{version_no_tilde}/Cargo.toml

%post
%systemd_post nispor.service

%preun
%systemd_preun nispor.service

%postun
%systemd_postun_with_restart nispor.service

%changelog
* Sat Oct 10 2020 Gris Ge <fge@redhat.com> - 0.6.1-2
- Fix incorrect build requirements.

* Sat Oct 10 2020 Gris Ge <fge@redhat.com> - 0.6.1-1
- Upgrade to 0.6.1

* Sun Sep 20 2020 Gris Ge <fge@redhat.com> - 0.5.1-1
- Upgrade to 0.5.1

* Mon Sep 07 2020 Gris Ge <fge@redhat.com> - 0.5.0-2
- Fix the python3-nispor requirement

* Mon Sep 07 2020 Gris Ge <fge@redhat.com> - 0.5.0-1
- Upgrade to 0.5.0

* Wed Aug 26 2020 Gris Ge <fge@redhat.com> - 0.4.0-2
- The mainpackage is not noarch.
- Remove useless-provides.

* Wed Aug 26 2020 Gris Ge <fge@redhat.com> - 0.4.0-1
- Upgrade to 0.4.0

* Mon Aug 17 2020 Gris Ge <fge@redhat.com> - 0.3.0-2
- Fix python linux bridge vlan filter

* Sun Aug 16 2020 Gris Ge <fge@redhat.com> - 0.3.0-1
- Upgrade to 0.3.0

* Thu Jul 09 2020 Gris Ge <fge@redhat.com> - 0.1.1-2
- Include license and documents

* Wed Jul 08 2020 Gris Ge <fge@redhat.com> - 0.1.1-1
- Upgrade to 0.1.1

* Tue Jul 07 14:50:05 CST 2020 Gris Ge <cnfourt@gmail.com> - 0.1.0-1
- Initial package
