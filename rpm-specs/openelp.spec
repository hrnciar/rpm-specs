Name:           openelp
Version:        0.8.0
Release:        5%{?dist}
Summary:        Open Source EchoLink Proxy

License:        BSD
URL:            https://github.com/cottsay/%{name}
Source0:        https://github.com/cottsay/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  doxygen
BuildRequires:  firewalld-filesystem
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  systemd
Requires(pre):  shadow-utils
Requires(post): firewalld-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
OpenELP is an open source EchoLink proxy for Linux and Windows. It aims to be
efficient and maintain a small footprint, while still implementing all of the
features present in the official EchoLink proxy.

OpenELP also has the ability to bind to multiple network interfaces which are
routed to unique external IP addresses, and therefore is capable of accepting
connections from multiple clients simultaneously.


%package devel
Summary:        Development files for OpenELP
Requires:       %{name}%{?isa} = %{version}-%{release}

%description devel
This package contains headers and other development files for building software
which utilizes OpenELP, and Open Source EchoLink Proxy.


%prep
%autosetup -p1

# Remove bundled md5, use OpenSSL instead
rm src/md5.c


%build
%cmake3 \
  -DOPENELP_USE_OPENSSL:BOOL=ON \
  %{nil}

%cmake_build --target all doc


%install
%cmake_install

# Run the service under a specific user
sed -i '/^\[Service\]$/a User=openelp' %{buildroot}%{_unitdir}/%{name}.service

# Extract the command line options to sysconfig
install -d %{buildroot}%{_sysconfdir}/sysconfig
grep ^ExecStart= %{buildroot}%{_unitdir}/%{name}.service | \
  sed 's|.*openelpd *\(.*\) %{_sysconfdir}/ELProxy.conf|\1|' | \
  sed 's|\(.*\)|# Options for openelpd\nOPTIONS="\1"|' > %{buildroot}%{_sysconfdir}/sysconfig/openelpd
sed -i '/^\[Service\]$/a EnvironmentFile=-%{_sysconfdir}/sysconfig/openelpd' %{buildroot}%{_unitdir}/%{name}.service
sed -i 's|\(ExecStart=.*openelpd\).*|\1 \$OPTIONS %{_sysconfdir}/ELProxy.conf|' %{buildroot}%{_unitdir}/%{name}.service

# Manually install the firewalld service
install -m0644 -p -D doc/%{name}.xml %{buildroot}%{_prefix}/lib/firewalld/services/%{name}.xml


%check
%ctest


%pre
getent group openelp >/dev/null || groupadd -r openelp
getent passwd openelp >/dev/null || \
    useradd -r -g openelp -d / -s /sbin/nologin \
    -c "EchoLink Proxy" openelp

%post
%{?ldconfig}
%firewalld_reload
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%{?ldconfig}
%systemd_postun_with_restart %{name}.service


%files
%license LICENSE
%doc AUTHORS README.md TODO.md
%{_bindir}/%{name}d
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/openelpd.1.*
%{_prefix}/lib/firewalld/services/%{name}.xml
%attr(0640, openelp, root) %config(noreplace) %{_sysconfdir}/ELProxy.conf
%config(noreplace) %{_sysconfdir}/sysconfig/openelpd
%{_unitdir}/%{name}.service

%files devel
%doc %{_vpath_builddir}/doc/html
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so


%changelog
* Mon Aug 03 2020 Scott K Logan <logans@cottsay.net> - 0.8.0-5
- Resolve build issues due to CMake out-of-source build changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Scott K Logan <logans@cottsay.net> - 0.8.0-2
- Use macros for ldconfig and firewalld scriptlets
- Specifically remove bundled md5 implementation

* Thu Jun 18 2020 Scott K Logan <logans@cottsay.net> - 0.8.0-1
- Update to 0.8.0
- Add firewalld service
- Adjust ELProxy.conf permissions because it contains a password

* Sun Jun 07 2020 Scott K Logan <logans@cottsay.net> - 0.7.2-1
- Initial package (rhbz#1844794)
