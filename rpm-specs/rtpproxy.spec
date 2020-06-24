Name:		rtpproxy
Version:	2.0.0
Release:	14%{?dist}
Summary:	A symmetric RTP proxy
License:        BSD
URL:		http://www.rtpproxy.org
VCS:		scm:git:https://github.com/sippy/rtpproxy.git
Source0:	https://github.com/sippy/rtpproxy/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		rtpproxy-0001-Remove-more-autogenerated-stuff.patch
Patch2:		rtpproxy-0002-Fedora-related-fix-for-docbook-path.patch
Patch3:		rtpproxy-0003-Updated-SysV-init-script-for-legacy-systems.patch
Patch4:		rtpproxy-0004-Fix-build-with-the-bcg729-1.0.2.patch

BuildRequires:	systemd-devel
# For /usr/lib/rpm/macros.d/macros.systemd
BuildRequires:  systemd
BuildRequires:	gsm-devel
BuildRequires:	libxslt
BuildRequires:	docbook-style-xsl
BuildRequires:	bcg729-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires(pre):	/usr/sbin/useradd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
This is symmetric RTP proxy designed to be used in conjunction with
the SIP Express Router (SER) or any other SIP proxy capable of
rewriting SDP bodies in SIP messages that it processes.


%prep
%autosetup -p1


%build
autoreconf -ivf
%configure --enable-systemd
make %{?_smp_mflags}
make rtpproxy.8


%install
make install DESTDIR=%{buildroot}
install -D -p -m 0644 rpm/%{name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}
# install systemd files
install -D -m 0644 -p rpm/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 -p rpm/%{name}.socket %{buildroot}%{_unitdir}/%{name}.socket
install -D -m 0644 -p rpm/%{name}.tmpfiles.conf %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_localstatedir}/run/%{name}
install -d %{buildroot}%{_localstatedir}/lib/%{name}


%pre
getent passwd %{name} >/dev/null || \
/usr/sbin/useradd -r -c "RTPProxy service"  -d %{_localstatedir}/lib/%{name} -s /sbin/nologin %{name} 2>/dev/null || :


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%files
%doc AUTHORS README.md README.remote
%license LICENSE
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket
%{_tmpfilesdir}/%{name}.conf
%dir %attr(0755, rtpproxy, rtpproxy) %{_localstatedir}/run/%{name}
%exclude %{_bindir}/rtpproxy_debug
%{_bindir}/rtpproxy
%{_bindir}/makeann
%{_mandir}/man8/rtpproxy.8*
%dir %attr(0750, rtpproxy, rtpproxy) %{_localstatedir}/lib/%{name}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.0.0-10
- Add support for bcg729 library (g.729 codec)
- Drop support for pre-EL7 distributives

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.0.0-6
- Missing *.socket file added

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 20 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.0.0-3
- Add BR: systemd (Fix F23FTBFS, RHBZ#1239882).

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 10 2015 Peter Lemenkov <lemenkov@gmail.com> - 2.0.0-1
- Ver. 2.0.0 Final
- Temporarily exclude debug utility

* Wed Nov 12 2014 Peter Lemenkov <lemenkov@gmail.com> - 2.0-0.1.RC1
- Ver. 2.0-RC1
- Better systemd support
- Removed support for EL5

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-16.git2121113
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-15.git2121113
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 03 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-14.git2121113
- Fixed FTBFS in F20+

* Sat Aug 31 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-13.git2121113
- Spec-file cleanups
- Added systemd-macros where necessary

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-12.git2121113
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-11.git2121113
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-10.git2121113
- Revert systemd macros

* Tue Jan 22 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-9.git2121113
- Latest git snapshot

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-7
- Fixed systemd installation

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 23 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-5
- Works with systemd

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 1.2.1-3
- Rebuilt for gcc bug 634757

* Sun Sep 19 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-2
- Allow group users to write to controlling UNIX-socket (rhbz #626863)

* Sun Nov  1 2009 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-1
- Ver. 1.2.1
- Brand new init-script

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 27 2009 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-1
- Ver. 1.2.0

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.4.beta.200901120
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 Peter Lemenkov <lemenkov@gmail.com> - 1.2-0.3.beta.200901120
- Snapshot 1.2.beta.200901120
- Added sysconfig file

* Mon Oct  6 2008 Peter Lemenkov <lemenkov@gmail.com> - 1.2-0.2.alpha.200807211
- Added missing BuildRequires
- Added init-script

* Wed Aug 13 2008 Peter Lemenkov <lemenkov@gmail.com> - 1.2-0.1.alpha.200807211
- Snapshot 1.2.alpha.200807211

* Wed Jun 18 2008 Peter Lemenkov <lemenkov@gmail.com> - 1.1-1
- Stable ver. 1.1

* Fri May 16 2008 Peter Lemenkov <lemenkov@gmail.com> - 1.1-0.3.beta.200804031
- Snapshot 20080403.1

* Sat Mar 29 2008 Peter Lemenkov <lemenkov@gmail.com> - 1.1-0.2.beta.20080226
- Snapshot 20080226
- Drop upstreamed patch

* Fri Feb 15 2008 Peter Lemenkov <lemenkov@gmail.com> - 1.1-0.1.beta.20071218
- Ver. 1.1.beta.20071218 (we need it because openser-1.3.0 works only with it)

* Mon Feb  4 2008 Peter Lemenkov <lemenkov@gmail.com> - 1.0-1
- Ver. 1.0

* Wed Nov 22 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.3-1
- First version for Fedora Extras

