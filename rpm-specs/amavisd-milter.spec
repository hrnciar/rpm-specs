Summary:           Sendmail milter for amavisd-new using the AM.PDP protocol
Name:              amavisd-milter
Version:           1.7.0
Release:           1%{?dist}
License:           BSD
URL:               https://github.com/prehor/amavisd-milter
Source0:           https://github.com/prehor/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:           amavisd-milter.service
Source2:           amavisd-milter.init
Source3:           amavisd-milter.sysconfig
BuildRequires:     gcc
%if 0%{?rhel} > 7 || 0%{?fedora} > 25
BuildRequires:     sendmail-milter-devel >= 8.12.0
%else
BuildRequires:     sendmail-devel >= 8.12.0
%endif
%if 0%{?rhel} > 6 || 0%{?fedora} > 17
BuildRequires:     systemd
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd
%else
Requires(post):    /sbin/chkconfig
Requires(preun):   /sbin/service, /sbin/chkconfig
Requires(postun):  /sbin/service
%endif
Requires:          amavisd-new

%description
The amavisd-milter is a sendmail milter (mail filter) for amavisd-new
2.4.3 (and above) and sendmail 8.13 (and above) which use the new AM.PDP
protocol.

Run 'usermod -a -G amavis postfix' when using Postfix and amavisd-milter
via the unix socket.

%prep
%setup -q

%build
%configure \
%if 0%{?rhel} > 6 || 0%{?fedora} > 14
  --localstatedir=/run/amavisd \
%else
  --localstatedir=%{_localstatedir}/run/amavisd \
%endif
  --with-working-dir=%{_localstatedir}/spool/amavisd/tmp
%make_build

%install
%make_install

# Install systemd unit file or initscript
install -D -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
%if 0%{?rhel} > 6 || 0%{?fedora} > 14
install -D -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
%else
install -D -p -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/%{name}
sed -e 's@/run@%{_localstatedir}/run@g' -i $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
touch -c -r %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
%endif

%post
%if 0%{?rhel} > 6 || 0%{?fedora} > 17
%systemd_post %{name}.service
%else
/sbin/chkconfig --add %{name}
%endif

%preun
%if 0%{?rhel} > 6 || 0%{?fedora} > 17
%systemd_preun %{name}.service
%else
if [ $1 -eq 0 ]; then
  /sbin/service %{name} stop > /dev/null 2>&1 || :
  /sbin/chkconfig --del %{name}
fi
%endif

%postun
%if 0%{?rhel} > 6 || 0%{?fedora} > 17
%systemd_postun_with_restart %{name}.service
%else
if [ $1 -ne 0 ]; then
  /sbin/service %{name} condrestart > /dev/null 2>&1 || :
fi
%endif

%files
%license LICENSE
%doc CHANGES
%{_sbindir}/%{name}
%if 0%{?rhel} > 6 || 0%{?fedora} > 14
%{_unitdir}/%{name}.service
%else
%{_sysconfdir}/rc.d/init.d/%{name}
%endif
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
* Wed Apr 22 2020 Robert Scheck <robert@fedoraproject.org> 1.7.0-1
- Upgrade to 1.7.0 (#1824332)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Robert Scheck <robert@fedoraproject.org> 1.6.1-1
- Upgrade to 1.6.1
- Initial spec file for Fedora and Red Hat Enterprise Linux
