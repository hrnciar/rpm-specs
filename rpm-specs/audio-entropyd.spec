Name:           audio-entropyd
Version:        2.0.3
Release:        19%{?dist}
License:        GPLv2
Summary:        Generate entropy from audio output
URL:            http://www.vanheusden.com/aed/
Source0:        http://www.vanheusden.com/aed/audio-entropyd-%{version}.tgz
Source1:        audio-entropyd.service
Source2:	audio-entropyd.conf
# The upstream for this code is basically dead. 
# stan <gryt@q.com> provided this patch which reworks
# this code significantly, but allows it to actually work
# with pulseaudio. Actually working fork > non-working upstream.
Patch0:		audio-entropyd-2.0.3-pulseaudio-fork.patch
# Fix arg parsing (thanks to stan)
Patch1:		audio-entropyd-2.0.3-fixargs.patch
BuildRequires:  gcc
BuildRequires:	alsa-lib-devel
BuildRequires:  systemd-units
Requires(post): systemd-sysv
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
Audio-entropyd generates entropy-data for the /dev/random device.

%prep
%setup -q
%patch0 -p0 -b .pulseaudio
%patch1 -p1 -b .fixargs

%build
make OPT_FLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
install -m0755 audio-entropyd $RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -m0755 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/audio-entropyd

%post
%systemd_post audio-entropyd.service

%preun
%systemd_preun audio-entropyd.service

%postun
%systemd_postun_with_restart audio-entropyd.service

%triggerun -- audio-entropyd < 2.0.3-1
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply audio-entropyd
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save audio-entropyd >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del httpd >/dev/null 2>&1 || :
/bin/systemctl try-restart audio-entropyd.service >/dev/null 2>&1 || :

%files
%doc COPYING README TODO
%{_unitdir}/audio-entropyd.service
%{_sbindir}/audio-entropyd
%config(noreplace) %{_sysconfdir}/sysconfig/audio-entropyd

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 30 2015 Tom Callaway <spot@fedoraproject.org> - 2.0.3-10
- fix arg parsing (thanks to stan)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr  7 2014 Tom Callaway <spot@fedoraproject.org> - 2.0.3-6
- apply patches to support pulseaudio natively. See: 
  https://bugzilla.redhat.com/show_bug.cgi?id=982660

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 23 2012 Tom Callaway <spot@fedoraproject.org> - 2.0.3-3
- update scriptlets for new systemd macros

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Tom Callaway <spot@fedoraproject.org> 2.0.3-1
- update to 2.0.3
- convert to systemd

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May  5 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.1-1
- upstream took my alsa patch (improved on it too)

* Wed Mar 25 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.5-4
- port from OSS to ALSA

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.5-2
- initscript no longer on by default (bz 441273)

* Sun Sep 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.5-1
- update to 1.0.5
- drop debug patch, upstream fixed the problem in a different manner
- add config file and fix initscript to use it (bz 463904)

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.1-5
- random rawhide appeasement

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.1-4
- add xtra-debug option

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.1-2
- Autorebuild for GCC 4.3

* Tue Feb 19 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.1-1
- update to 1.0.1

* Thu Aug 23 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.0-5
- rebuild for BuildID

* Thu Aug  2 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.0-4
- selinux policy not needed

* Mon Jun 11 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.0-3
- add selinux policy (bugzilla 243453)

* Tue Jun  5 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.0-2
- add condrestart to postun

* Tue May 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.0-1
- initial package for Fedora Extras
