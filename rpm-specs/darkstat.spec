Name:          darkstat
Summary:       Network traffic analyzer
Version:       3.0.719
Release:       10%{?dist}
License:       GPLv2
URL:           http://unix4lyfe.org/darkstat/
Source:        http://unix4lyfe.org/%{name}/%{name}-%{version}.tar.bz2
# My own systemd files
Source1:       %{name}.service
Source2:       %{name}.sysconfig
BuildRequires:  gcc
BuildRequires: libpcap-devel, zlib-devel

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
BuildRequires:    systemd

%description
darkstat is a network traffic analyzer. It's basically a packet sniffer
which runs as a background process on a cable/DSL router and gathers
all sorts of useless but interesting statistics.

%prep
%setup -q

%build
%configure --disable-silent-rules
make %{?_smp_mflags}

%install
make install DESTDIR="%{buildroot}"

install -Dp -m 0644 %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service
install -Dp -m 0644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}

%pre
getent passwd %{name} >/dev/null || useradd -r -s /sbin/nologin -c "Network traffic analyzer" %{name}
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc AUTHORS COPYING* LICENSE NEWS README *.txt
%{_mandir}/man8/darkstat.8*
%attr(755,-,-) %{_sbindir}/darkstat
%attr(0600,%{name},root) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}.service

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.719-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Pavel Alexeev <Pahan@Hubbitus.info> - 3.0.719-1
- Update to upstream version 3.0.719.
- Lib exit should be fixed (https://unix4lyfe.org/gitweb/darkstat/commitdiff/dbd25d7f8f06770f46fe9f3d460385e699439186).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.718-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.718-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.718-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 3.0.718-3
- Add --disable-silent-rules to configure call.

* Thu Apr 24 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 3.0.718-2
- Do not mark man as %%doc.
- Add systemd stuff.
- Provide separate user for service.

* Fri Mar 14 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 3.0.718-1
- Imported from http://pkgs.repoforge.org/darkstat/darkstat-3.0.717-1.rf.src.rpm and rework to prepare for Fedora.
- Update to 3.0.718.
- Cleanup.
- Update URLs.
- Remove INSTALL file from docs (install-file-in-docs rpmlint warning).
- darkstat.x86_64: E: missing-call-to-setgroups /usr/sbin/darkstat, darkstat.x86_64: E: incorrect-fsf-address /usr/share/doc/darkstat/COPYING.GPL issues mailed to author.
- Add BR zlib-devel