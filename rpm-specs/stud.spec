%global stud_githash	0b88039
%global stud_user	stud
%global stud_group	stud
%global stud_homedir	%{_localstatedir}/lib/stud
%global stud_confdir	%{_sysconfdir}/stud
%global stud_datadir	%{_datadir}/stud


Name:		stud
Version:	0.3
Release:	18.20120814git%{?dist}
Summary:	The Scalable TLS Unwrapping Daemon

License:	BSD
URL:		https://github.com/bumptech/stud
Source0:	bumptech-%{name}-%{version}-51-g%{stud_githash}.tar.gz
Source1:	%{name}.service
Source2:	%{name}.cfg
Patch0:		stud-0.3-fix-libev-include-path.patch

BuildRequires:	gcc
BuildRequires:	libev-devel
BuildRequires:	compat-openssl10-devel
BuildRequires:	systemd-units

Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units


%description
stud is a network proxy that terminates TLS/SSL connections and
forwards the unencrypted traffic to some backend. It is designed to
handle tens of thousands of connections efficiently on multicore
machines. stud has very few features -- it is designed to be paired
with an intelligent backend like haproxy or nginx.


%prep
%setup -q -n bumptech-%{name}-%{stud_githash}
%patch0 -p1


%build
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} BINDIR=%{_sbindir}
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/stud.service
%{__install} -p -D -m 0644 %{SOURCE2} %{buildroot}%{stud_confdir}/stud.cfg
%{__install} -d -m 0755 %{buildroot}%{stud_homedir}
%{__install} -d -m 0755 %{buildroot}%{stud_datadir}



%pre
groupadd -r %{stud_group} &>/dev/null ||:
useradd -r -g %{stud_group} -s /sbin/nologin -d %{stud_homedir} %{stud_user} &>/dev/null ||:


%post
%systemd_post stud.service


%preun
%systemd_preun stud.service


%postun
%systemd_postun_with_restart stud.service


%files
%doc LICENSE README.md
%dir %{stud_confdir}
%dir %{stud_datadir}
%config(noreplace) %{stud_confdir}/stud.cfg
%{_unitdir}/stud.service
%{_sbindir}/stud
%{_mandir}/man8/stud.8*
%attr(-,%{stud_user},%{stud_group}) %dir %{stud_homedir}


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-18.20120814git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17.20120814git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-16.20120814git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15.20120814git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Ryan O'Hara <rohara@redhat.com> - 0.3-14.20120814git
- Add BuildRequires gcc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-13.20120814git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12.20120814git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-11.20120814git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 29 2017 Ryan O'Hara <rohara@redhat.com> - 0.3-10.20120814git
- Build using compat-openssl10-devel (#1424476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9.20120814git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8.20120814git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7.20120814git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6.20120814git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-5.20120814git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4.20120814git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 Ryan O'Hara <rohara@redhat.com> - 0.3-3.20120814git
- Use new systemd-rpm macros in stud spec file (#857398).

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2.20120814git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Ryan O'Hara <rohara@redhat.com> - 0.3-1.20120814git
- Initial build.
