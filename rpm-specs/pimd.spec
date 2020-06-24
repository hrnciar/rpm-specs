Name:           pimd
Version:        2.3.2
Release:        13%{?dist}
Summary:        The original PIM-SM multicast routing daemon

License:        BSD
URL:            http://troglobit.com/pimd.html

Source0:        ftp://ftp.troglobit.com/pimd/%{name}-%{version}.tar.gz
Source1:        %{name}.service

# https://fedorahosted.org/fpc/ticket/174
Provides:       bundled(libite) = 1.4.2

BuildRequires:      systemd gcc
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd


%description
pimd is a lightweight, stand-alone PIM-SM/SSM multicast routing daemon
available under the free 3-clause BSD license. This is the restored
original version from University of Southern California, by Ahmed Helmy,
Rusty Eddy and Pavlin Ivanov Radoslavov.


%prep
%setup -q


%build
%configure
export CFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=${RPM_BUILD_ROOT}
rm $RPM_BUILD_ROOT/usr/share/doc/pimd/LICENSE
rm $RPM_BUILD_ROOT/usr/share/doc/pimd/LICENSE.mrouted

# Systemd unit files
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service



%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
%{_sbindir}/pimd
%{_mandir}/man8/*
%license LICENSE LICENSE.mrouted
%doc README.md README-config.md README.config.jp README-debug.md ChangeLog.org
%doc CONTRIBUTING.md CODE-OF-CONDUCT.md INSTALL.md
%doc TODO.org CREDITS FAQ.md AUTHORS
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_unitdir}/%{name}.service


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 John W. Linville <linville@redhat.com> - 2.3.2-10
- Add previously unnecessary BuildRequires for gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 John W. Linville <linville@redhat.com> - 2.3.2-8
- Fix ExecStart path in systemd unit file

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 19 2016 John W. Linville <linville@redhat.com> - 2.3.2-3
- Add BuildRequires and Requires for systemd

* Fri Sep 16 2016 John W. Linville <linville@redhat.com> - 2.3.2-2
- Add systemd unit file

* Wed Sep 07 2016 John W. Linville <linville@redhat.com> - 2.3.2-1
- Initial import
