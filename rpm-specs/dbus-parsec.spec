%bcond_without check
%global __cargo_skip_build 0

%global custom_cargo_build /usr/bin/env PROTOC=%{_bindir}/protoc PROTOC_INCLUDe=%{_includedir} CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 %{_bindir}/cargo build %{_smp_mflags} -Z avoid-dev-deps --release
%global custom_cargo_test /usr/bin/env PROTOC=%{_bindir}/protoc PROTOC_INCLUDe=%{_includedir} CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 %{_bindir}/cargo test %{_smp_mflags} -Z avoid-dev-deps --release --no-fail-fast

# dbus-parsec is supposed to be daemon used through dbus
%global __cargo_is_lib() false

Name:          dbus-parsec
Version:       0.3.0
Release:       2%{?dist}
Summary:       DBus PARSEC interface

License:       EUPL 1.2
URL:           https://github.com/fedora-iot/dbus-parsec
Source:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:        parsec-client-ver-bump.patch
Patch1:        dbus-parsec-service-tweaks.patch

ExclusiveArch: %{rust_arches}
# rhbz 1869980
ExcludeArch:   s390x %{power64}

BuildRequires: NetworkManager-libnm-devel
BuildRequires: protobuf-compiler
BuildRequires: rust-packaging
BuildRequires: systemd dbus-common
Requires: parsec
%{?systemd_requires}

%description
%{summary}.

%prep
%autosetup -p1
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%custom_cargo_build

%install
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%cargo_install

install -D -p -m0644 dbus-parsec.service %{buildroot}%{_unitdir}/dbus-parsec.service
install -D -p -m0644 dbus-parsec.conf %{buildroot}%{_datadir}/dbus-1/system.d/dbus-parsec.conf
install -d -m0755 %{buildroot}%{_localstatedir}/lib/dbus-parsec
install -d -m0755 %{buildroot}%{_libexecdir}
mv %{buildroot}%{_bindir}/dbus-parsec %{buildroot}%{_libexecdir}/

%if %{with check}
%check
%custom_cargo_test -- -- --skip real_ --skip loop_ --skip travis_
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/dbus-parsec-control
%{_datadir}/dbus-1/system.d/dbus-parsec.conf
%{_libexecdir}/dbus-parsec
%{_localstatedir}/lib/dbus-parsec
%{_unitdir}/dbus-parsec.service

%changelog
* Fri Oct 02 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.0-2
- Rebuild for new parsec/parsec-client

* Wed Sep 23 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0
- Support storing WiFi (PSK and WPA-Enterprise) credentials

* Thu Sep 17 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.2.2-3
- Include createcredential.py sample client tool

* Thu Sep 17 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.2.2-2
- Require the parsec service to be running

* Mon Sep 14 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2

* Thu Sep 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.0-1
- Initial release
