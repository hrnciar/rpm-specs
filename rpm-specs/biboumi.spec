Name: biboumi
Version: 8.5
Release: 4%{?dist}
Summary: An XMPP gateway that connects to IRC servers

License: zlib
URL: https://lab.louiz.org/louiz/biboumi
Source0: %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: Don-t-download-catch-during-build.patch

BuildRequires: gcc-c++
BuildRequires: cmake >= 3.0
BuildRequires: catch-devel
BuildRequires: libuuid-devel
BuildRequires: expat-devel
BuildRequires: libidn-devel
BuildRequires: systemd-devel
BuildRequires: botan2-devel
BuildRequires: sqlite-devel
BuildRequires: udns-devel
BuildRequires: libpq-devel
BuildRequires: pandoc
BuildRequires: systemd-rpm-macros
%{?systemd_requires}

%description
Biboumi is an XMPP gateway that connects to IRC servers and translates
between the two protocols. It can be used to access IRC channels using any
XMPP client as if these channels were XMPP MUCs.


%prep
%autosetup


%build
%cmake \
    -DCMAKE_BUILD_TYPE=release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DPOLLER=EPOLL \
    -DWITH_BOTAN=1 \
    -DWITH_SYSTEMD=1 \
    -DWITH_LIBIDN=1 \
    -DWITH_SQLITE3=1 \
    -DWITH_POSTGRESQL=1 .
%cmake_build


%install
%cmake_install


%check
ctest -VV %{?_smp_mflags}


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%license COPYING
%doc README.rst doc/*.rst
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_sysconfdir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_unitdir}/%{name}.service
%{_bindir}/%{name}


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.5-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Florent Le Coz <louiz@louiz.org> - 8.5-3
- Use cmake_build/install, see https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds#Migration

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Jeremy Cline <jcline@redhat.com> - 8.5-1
- Update to v8.5

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Jeremy Cline <jcline@redhat.com> - 8.3-2
- Add systemd scriptlets
- Own the /etc/biboumi directory

* Sun Apr 14 2019 Jeremy Cline <jeremy@jcline.org> - 8.3-1
- Initial package
