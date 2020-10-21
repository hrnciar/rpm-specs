%bcond_without check
%global __cargo_skip_build 0
%global __cargo_is_lib() false

# mbed-crypto-provider, pkcs11-provider, tpm-provider, all-providers
%global __cargo_parse_opts --features=tpm-provider,mbed-crypto-provider

%global custom_cargo_build /usr/bin/env PROTOC=%{_bindir}/protoc PROTOC_INCLUDe=%{_includedir} CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 %{_bindir}/cargo build %{_smp_mflags} -Z avoid-dev-deps --release
%global custom_cargo_test /usr/bin/env PROTOC=%{_bindir}/protoc PROTOC_INCLUDe=%{_includedir} CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 %{_bindir}/cargo test %{_smp_mflags} -Z avoid-dev-deps --release --no-fail-fast

Name:          parsec
Version:       0.5.0
Release:       1%{?dist}
Summary:       The PARSEC daemon

License:       ASL 2.0
URL:           https://github.com/parallaxsecond/parsec
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:       parsec.service
Source2:       config.toml
Source3:       parsec.tmpfile.conf

ExclusiveArch: %{rust_arches}
# rhbz 1869980
ExcludeArch:   s390x %{power64}

BuildRequires: protobuf-compiler
BuildRequires: rust-packaging
BuildRequires: systemd
Requires: tpm2-tss >= 3.0.0-3
Requires(pre): shadow-utils
Requires(pre): tpm2-tss >= 3.0.0-3
%{?systemd_requires}

%description
PARSEC is the Platform AbstRaction for SECurity, an open-source initiative to
provide a common API to hardware security and cryptographic services in a
platform-agnostic way. This abstraction layer keeps workloads decoupled from
physical platform details, enabling cloud-native delivery flows within the data
center and at the edge.

%prep
%autosetup -p1
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%custom_cargo_build --features=tpm-provider,mbed-crypto-provider

%install
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%cargo_install

install -D -p -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/parsec.service
install -D -p -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/parsec/config.toml
install -D -p -m0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/parsec.conf
install -d -m0755 %{buildroot}%{_localstatedir}/lib/parsec
install -d -m0755 %{buildroot}%{_libexecdir}
mv %{buildroot}%{_bindir}/parsec %{buildroot}%{_libexecdir}/

%if %{with check}
%check
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%custom_cargo_test -- -- --skip real_ --skip loop_ --skip travis_
%endif

%pre
getent group parsec >/dev/null || groupadd -r parsec
# For PARSEC consumers
getent group parsec-clients >/dev/null || groupadd -r parsec-clients
getent passwd parsec >/dev/null || \
    useradd -r -g parsec -G tss -G parsec-clients -d /var/lib/parsec -s /sbin/nologin \
    -c "PARSEC service" parsec
exit 0

%post
%systemd_post parsec.service

%preun
%systemd_preun parsec.service

%postun
%systemd_postun_with_restart parsec.service

%files
%license LICENSE
%doc README.md config.toml
%attr(0750,parsec,parsec) %dir %{_sysconfdir}/parsec/
%attr(0750,parsec,parsec) %dir %{_localstatedir}/lib/parsec/
%config(noreplace) %{_sysconfdir}/parsec/config.toml
%{_libexecdir}/parsec
%{_tmpfilesdir}/parsec.conf
%{_unitdir}/parsec.service

%changelog
* Fri Oct 02 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Thu Sep 17 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.4.0-5
- Enable the MBed provider

* Thu Sep 17 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.4.0-4
- User fixess, service file fixes, include default config

* Wed Sep 16 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.4.0-3
- Minor fixes

* Wed Sep 16 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.4.0-2
- Add service user creation, enable TPM2 provider, other fixes

* Tue Sep 01 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.4.0-1
- Initial package
