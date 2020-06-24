# trick rpmlint into ignoring the lib path for tmpfiles.d
%global _mylib lib
%global _tmpfilesdir %{_prefix}/%{_mylib}

Name:           sidc
Version:        1.8
Release:        19%{?dist}
Summary:        A VLF signal monitor for recording sudden ionospheric disturbances

License:        GPLv2
URL:            http://github.com/sorki/sidc
Source0:        https://github.com/sorki/sidc/archive/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  fftw-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  systemd-units
Requires:       fftw
Requires:       alsa-utils
Requires(pre):  shadow-utils

%description
sidc is a simple C program to monitor and record VLF signal
for sudden ionospheric disturbance detection.

%prep
%setup -q -n sidc-%{version}

%build
autoconf
%configure
make %{?_smp_mflags}

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_localstatedir}/lib/sidc
install -d %{buildroot}%{_localstatedir}/log/sidc
install -d -m 0755 %{buildroot}/run/sidc/

make DESTDIR=%{buildroot} install

install -Dm 644 sidc.service %{buildroot}%{_unitdir}/sidc.service
install -Dm 644 sidc.sysconf %{buildroot}%{_sysconfdir}/sysconfig/sidc
install -Dm 644 sidc.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/sidc
install -Dm 644 sidc.tmpfiles %{buildroot}%{_tmpfilesdir}/tmpfiles.d/sidc.conf

%files
%doc README.rst
%doc AUTHORS
%doc LICENSE
%{_bindir}/sidc
%config(noreplace) %{_sysconfdir}/sidc.conf
%config(noreplace) %{_sysconfdir}/sysconfig/sidc
%config(noreplace) %{_sysconfdir}/logrotate.d/sidc
%{_unitdir}/sidc.service
%dir %attr(-, sidc, sidc) %{_localstatedir}/lib/sidc
%dir %attr(-, sidc, sidc) %{_localstatedir}/log/sidc
%dir %attr(-, sidc, sidc) /run/sidc/
%{_tmpfilesdir}/tmpfiles.d/sidc.conf

%pre
getent group sidc >/dev/null || groupadd -r sidc
getent passwd sidc >/dev/null || \
useradd -r -g sidc -d %{_localstatedir}/lib/sidc -s /sbin/nologin \
        -c "sidc daemon" -G audio sidc
exit 0

%post
%systemd_post sidc.service

%preun
%systemd_preun sidc.service

%postun
%systemd_postun_with_restart sidc.service

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 22 2016 Richard Marko <rmarko@base48.cz> - 1.8-11
- Fix setup

* Tue Nov 22 2016 Richard Marko <rmarko@base48.cz> - 1.8-10
- Re-add source file under correct filename

* Tue Nov 22 2016 Richard Marko <rmarko@base48.cz> - 1.8-9
- Fix source URL

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 22 2012 Lukáš Nykrýn <lnykryn@redhat.com> - 1.8-2
- Scriptlets replaced with new systemd macros (#850409)

* Mon Jul 23 2012 Richard Marko <rmarko@redhat.com> - 1.8-1
- Version bump, use tmpfiles.d
* Mon Jul 23 2012 Richard Marko <rmarko@redhat.com> - 1.7-2
- Replaced define macro with global
* Sat Jul 21 2012 Richard Marko <rmarko@redhat.com> - 1.7-1
- Version bump, adding logrotate and sysconfig config files
* Fri Jul 20 2012 Richard Marko <rmarko@redhat.com> - 1.6-1
- Version bump, fixed attr issue
* Fri Jul 20 2012 Richard Marko <rmarko@redhat.com> - 1.5-1
- Version bump, systemd compatible now
* Thu Jul 19 2012 Richard Marko <rmarko@redhat.com> - 1.4-1
- Version bump
* Mon Jul 16 2012 Richard Marko <rmarko@redhat.com> - 1.3-1
- Update
* Wed Jun 29 2009 Marek Mahut <mmahut@fedoraproject.org> - 1.0-1
- Initial packaging attempt
