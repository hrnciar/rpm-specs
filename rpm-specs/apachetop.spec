Name:           apachetop
Version:        0.19.7
Release:        3%{?dist}
Summary:        A top-like display of Apache logs
License:        BSD
URL:            https://github.com/tessus/apachetop
Source0:        https://github.com/tessus/apachetop/releases/download/%{version}/apachetop-%{version}.tar.gz
Source1:        https://github.com/tessus/apachetop/releases/download/%{version}/apachetop-%{version}.tar.gz.asc
Source2:        gpgkey-8A5570C1BD85D34EADBC386C172380A011EF4944.gpg
BuildRequires:  gnupg2, gcc-c++, ncurses-devel, m4, readline-devel, pcre-devel

%description
ApacheTop watches a logfile generated by Apache (in standard common or
combined logformat, although it doesn't (yet) make use of any of the extra
fields in combined) and generates human-parsable output in realtime.

%prep
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q

%build
%configure --with-logfile=%{_localstatedir}/log/httpd/access_log
%make_build

%install
%make_install

%files 
%license LICENSE
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Robert Scheck <robert@fedoraproject.org> - 0.19.7-1
- Upgrade to 0.19.7

* Tue Jun 25 2019 Robert Scheck <robert@fedoraproject.org> - 0.18.4-1
- Upgrade to 0.18.4

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.6-10
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.15.6-3
- Rebuild for readline 7.x

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jun 21 2015 Robert Scheck <robert@fedoraproject.org> 0.15.6-1
- Upgrade to 0.15.6 (#1230464)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.12.6-16
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 27 2013 Adam Miller <maxamillion@fedoraproject.org> - 0.12.6-12
- Fix BZ 925005 - rerun autoconf to add support for aarch64

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jun 21 2008 Robert Scheck <robert@fedoraproject.org> 0.12.6-5
- Fixed a buffer overflow by wrong MAXPATHLEN define (#446199)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.12.6-4
- Autorebuild for GCC 4.3

* Sat Aug 25 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.12.6-3
- rebuild for BuildID

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 0.12.6-2
- rebuild

* Fri Jun 16 2006 Aurelien Bompard <gauret[AT]free.fr> 0.12.6-1
- Upgrade to 0.12.6 (#194602). Thanks to Robert Scheck.

* Sat Mar 11 2006 Aurelien Bompard <gauret[AT]free.fr> 0.12.5-4
- remove hardcoded requirement on httpd (#184491)

* Tue Feb 21 2006 Aurelien Bompard <gauret[AT]free.fr> 0.12.5-3
- rebuilt for FC5

* Tue Oct 04 2005 Aurelien Bompard <gauret[AT]free.fr> 0.12.5-2
- add patch for CAN-2005-2660

* Sun May 08 2005 Aurelien Bompard <gauret[AT]free.fr> 0.12.5-1%{?dist}
- version 0.12.5
- drop patch (applied upsteam)

* Thu Nov 11 2004 Michael Schwendt <mschwendt[AT]users.sf.net> 0.12-2
- Fix build for FC3/GCC 3.4.

* Sat May 22 2004 Aurelien Bompard <gauret[AT]free.fr> 0:0.12-0.fdr.1
- Initial RPM release.
