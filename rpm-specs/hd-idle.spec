Name:           hd-idle
Version:        1.05
Release:        9%{?dist}
Summary:        Spin down idle [USB] hard disks

License:        GPLv2
URL:            http://hd-idle.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
Source1:        hd-idle.service
Source2:        hd-idle.logrotate

BuildRequires:  gcc
BuildRequires:  systemd
Requires:       logrotate
%{?systemd_requires}

%description
hd-idle is a utility program for spinning-down external disks after a period
of idle time. Since most external IDE disk enclosures don't support setting
the IDE idle timer, a program like hd-idle is required to spin down idle disks
automatically.

A word of caution: hard disks don't like spinning up too often. Laptop disks
are more robust in this respect than desktop disks but if you set your disks
to spin down after a few seconds you may damage the disk over time due to the
stress the spin-up causes on the spindle motor and bearings. It seems that
manufacturers recommend a minimum idle time of 3-5 minutes, the default in
hd-idle is 10 minutes.

One more word of caution: hd-idle will spin down any disk accessible via the
SCSI layer (USB, IEEE1394, ...) but it will not work with real SCSI disks
because they don't spin up automatically. Thus it's not called scsi-idle and
I don't recommend using it on a real SCSI system unless you have a kernel
patch that automatically starts the SCSI disks after receiving a sense buffer
indicating the disk has been stopped. Without such a patch, real SCSI disks
won't start again and you can as well pull the plug.


%prep
%setup -q -n %{name}
sed -i 's/install -D -g root -o root/install -D/' Makefile


%build
export CFLAGS="%{optflags}"
%make_build


%install
%make_install
# Remove executable bit from manual page
find "%{buildroot}%{_mandir}" -executable -type f -exec chmod -x {} \;

install -d -m 755 %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
install -d %{buildroot}%{_sysconfdir}/sysconfig
echo 'HD_IDLE_OPTS="-i 1200 -l /var/log/hd-idle/hd-idle.log"' > \
     %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -d -m 755 %{buildroot}%{_localstatedir}/log/%{name}
install -d -m 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%{_sbindir}/*
%{_mandir}/man1/%{name}.1*
%{_unitdir}/*
%config(noreplace) %{_sysconfdir}/logrotate.d/*
%config(noreplace) %{_sysconfdir}/sysconfig/*
%dir %{_localstatedir}/log/%{name}
%license LICENSE
%doc README



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Samuel Rakitničan <samuel.rakitnican@gmail.com> 1.05-4
- Add requirement on logrotate and systemd
- Remove executable bit from manual page
- Use macro for systemd with correct post/preun/postun Requires tags

* Wed Aug 02 2017 Samuel Rakitničan <samuel.rakitnican@gmail.com> 1.05-3
- Use %%{optflags} macro

* Wed Aug 02 2017 Samuel Rakitničan <samuel.rakitnican@gmail.com> 1.05-2
- Use macros for building and installing
- Add gcc build requirement

* Sun Feb 26 2017 Samuel Rakitničan <samuel.rakitnican@gmail.com> 1.05-1
- Initialize
