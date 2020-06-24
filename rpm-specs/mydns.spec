%define _legacy_common_support 1

Summary: A Database based DNS server
Name: mydns
Version: 1.2.8.32
Release: 8%{?dist}
License: GPLv2+
URL: http://mydns-ng.com/
#URL: http://mydns.bboy.net/  this is the original website, but mydns is no more  maintaned by it's original creator
#because this mydns-ng in sourceforge was created
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: HOWTO
Source2: mydns.service
Source3: %{name}-sysusers.conf

BuildRequires: mariadb-devel
BuildRequires: zlib-devel
BuildRequires: libecpg-devel
BuildRequires: texinfo
BuildRequires: systemd
BuildRequires: gcc

Patch0: mydns_user.patch
# Fix build with MariaDB 10.2
# https://bugzilla.redhat.com/show_bug.cgi?id=1470175
# http://bugs.mydns-ng.com/view.php?id=78
Patch1: mydns-mariadb102.patch

%description
A name server that serves records directly from your database.

%package mysql
Summary: MyDNS compiled with MySQL support
Requires: %{name} = %{version}-%{release}
%{?systemd_requires}

%description mysql
MyDNS compiled with MySQL support

%package pgsql
Summary: MyDNS compiled with PostGreSQL support
Requires: %{name} = %{version}-%{release}
%{?systemd_requires}

%description pgsql
MyDNS compiled with PostGreSQL support

%prep
%autosetup -p1

#install doc about alternatives
install -Dp -m 644 %{SOURCE1} ./HOWTO

%build
#mydns current doesn't support loadable modules, so We need to compile it 2 times and use alternatives, :-(
%configure \
    --without-pgsql \
    --with-mysql \
    --with-mysql-lib=%{_libdir}/mysql \
    --with-mysql-include=%{_includedir}/mysql \
    --with-zlib=%{_libdir} \
    --enable-status \
    --enable-alias

make %{?_smp_mflags}
make install DESTDIR=$(pwd)/mysql

for dir in lib src; do
    ( cd $dir && make clean )
done

%configure \
    --with-pgsql \
    --without-mysql \
    --with-pgsql-lib=%{_libdir} \
    --with-pgsql-include=%{_includedir} \
    --with-zlib=%{_libdir} \
    --enable-status \
    --enable-alias

make %{?_smp_mflags}
make install DESTDIR=$(pwd)/pgsql

%install
install -Dp %SOURCE3 %{buildroot}%{_sysusersdir}/%{name}.conf

#install mysql and pgsql files
for database in mysql pgsql; do
    install -Dp ./$database%{_bindir}/mydnscheck %{buildroot}%{_bindir}/mydnscheck-$database
    install -Dp ./$database%{_bindir}/mydns-conf %{buildroot}%{_bindir}/mydns-conf-$database
    install -Dp ./$database%{_bindir}/mydnsexport %{buildroot}%{_bindir}/mydnsexport-$database
    install -Dp ./$database%{_bindir}/mydnsptrconvert %{buildroot}%{_bindir}/mydnsptrconvert-$database
    install -Dp ./$database%{_bindir}/mydnsimport %{buildroot}%{_bindir}/mydnsimport-$database
    install -Dp ./$database%{_sbindir}/mydns %{buildroot}%{_sbindir}/mydns-$database

    install -d %{buildroot}%{_datadir}/locale
    cp -a ./$database%{_datadir}/locale %{buildroot}%{_datadir}
done

%find_lang %{name}

#main package (all files not linked with mysql or pgsql)
install -Dp -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/mydns.service
install -Dp -m 600 mydns.conf %{buildroot}%{_sysconfdir}/mydns.conf
install -Dp -m 644 contrib/admin.php %{buildroot}%{_datadir}/%{name}/admin.php

install -Dp -m 644 doc/mydns.conf.5 %{buildroot}%{_mandir}/man5/mydns.conf.5
install -Dp -m 644 doc/mydns.8 %{buildroot}%{_mandir}/man8/mydns.8
install -Dp -m 644 doc/mydnscheck.8 %{buildroot}%{_mandir}/man8/mydnscheck.8
install -Dp -m 644 doc/mydnsexport.8 %{buildroot}%{_mandir}/man8/mydnsexport.8
install -Dp -m 644 doc/mydnsimport.8 %{buildroot}%{_mandir}/man8/mydnsimport.8
install -Dp -m 644 doc/mydns-conf.8 %{buildroot}%{_mandir}/man8/mydns-conf.8
install -Dp -m 644 doc/mydns.info %{buildroot}%{_infodir}/mydns.info

%pre
%sysusers_create_inline '%(cat %{SOURCE3})'

%post
%systemd_post mydns.service

%preun
%systemd_preun mydns.service

%postun mysql
%systemd_postun_with_restart mydns.service

%postun pgsql
%systemd_postun_with_restart mydns.service

%post pgsql
%{_sbindir}/alternatives --install %{_sbindir}/mydns MyDNS %{_sbindir}/mydns-pgsql 1 \
    --slave %{_bindir}/mydnscheck mydnscheck %{_bindir}/mydnscheck-pgsql \
    --slave %{_bindir}/mydnsexport mydnsexport %{_bindir}/mydnsexport-pgsql \
    --slave %{_bindir}/mydnsimport mydnsimport %{_bindir}/mydnsimport-pgsql \
    --slave %{_bindir}/mydnsptrconvert mydnsptrconvert %{_bindir}/mydnsptrconvert-pgsql
%systemd_post mydns.service


%post mysql
%{_sbindir}/alternatives --install %{_sbindir}/mydns MyDNS %{_sbindir}/mydns-mysql 2 \
    --slave %{_bindir}/mydnscheck mydnscheck %{_bindir}/mydnscheck-mysql \
    --slave %{_bindir}/mydnsexport mydnsexport %{_bindir}/mydnsexport-mysql \
    --slave %{_bindir}/mydnsimport mydnsimport %{_bindir}/mydnsimport-mysql \
    --slave %{_bindir}/mydnsptrconvert mydnsptrconvert %{_bindir}/mydnsptrconvert-mysql
%systemd_post mydns.service



%preun pgsql
%systemd_preun mydns.service
%{_sbindir}/alternatives -remove MyDNS %{_sbindir}/mydns-pgsql
exit 0


%preun mysql
%systemd_preun mydns.service
%{_sbindir}/alternatives -remove MyDNS %{_sbindir}/mydns-mysql
exit 0

%files -f %{name}.lang
%{_sysusersdir}/%{name}.conf
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_infodir}/mydns.info.*
%doc AUTHORS ChangeLog COPYING NEWS README TODO HOWTO
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/mydns.conf
%{_unitdir}/mydns.service
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/admin.php

%files mysql
%doc QUICKSTART.mysql
%{_bindir}/mydnscheck-mysql
%{_bindir}/mydns-conf-mysql
%{_bindir}/mydnsexport-mysql
%{_bindir}/mydnsptrconvert-mysql
%{_bindir}/mydnsimport-mysql
%{_sbindir}/mydns-mysql

%files pgsql
%doc QUICKSTART.postgres
%{_bindir}/mydnscheck-pgsql
%{_bindir}/mydns-conf-pgsql
%{_bindir}/mydnsexport-pgsql
%{_bindir}/mydnsptrconvert-pgsql
%{_bindir}/mydnsimport-pgsql
%{_sbindir}/mydns-pgsql

%changelog
* Sun Mar 29 2020  Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.2.8.32-8
- fix FTBS rhbz#1799670

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 1.2.8.32-5
- Remove hardcoded gzip suffix from GNU info pages

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.2.8.32-2
- clean up spec file

* Mon Feb 19 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.2.8.32-1
- add gcc into buildrequires
- sync with git code

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8.31-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8.31-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8.31-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Adam Williamson <awilliam@redhat.com> - 1.2.8.31-17
- Rebuild against MariaDB 10.2 with patch from Augusto Caringi

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8.31-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8.31-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8.31-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 03 2015 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.2.8.31-13
- change systemd unit file to start it after mariadb-server

* Thu Feb 26 2015 Matej Cepl <mcepl@redhat.com> - 1.2.8.31-12
- Fix build of the mydns-pgsql so that it actually supports pgsql
  (#985909) Thanks for the patch by Tomasz Sterna.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8.31-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Aug 03 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.2.8.31-10
- BR: systemd for %%{_unitdir} (#1106254)
- systemd-units -> systemd

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8.31-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8.31-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 18 2012 Jon Ciesla <limburgher@gmail.com> - 1.2.8.31-5
- Migrate to systemd, BZ 790047.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 1.2.8.31-3
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 24 2010 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.2.8.31-1
- new version

* Mon Aug 17 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.2.8.27-4
- make mydns start after mysql

* Tue Aug 04 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.2.8.27-3
- fix spec file for rhel

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 25 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.2.8.27-1
- New version 1.2.8.27

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 09 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 1.2.8.25-1
- upgrade to a new version
- various fixes from Comment #21 From  Mamoru Tasaka, bz #476832

* Tue Feb 03 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 1.2.8.23-3
- remove QUICKSTART.mysql from main package, let it alive in -mysql subpackage
- change the way to create user and group
- enforce /etc/mydns.conf permissions

* Mon Feb 02 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 1.2.8.23-2
- add postun requires, simplify HOWTO about alternatives install

* Wed Feb 02 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 1.2.8.23-1
- upgrade to new version, remove init.d patch merged with upstream
- add --enable-status --enable-alias to configure script

* Wed Jan 30 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 1.2.8.22-2
- create separated mydns user and group

* Wed Jan 30 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 1.2.8.22-1
- upgrade to new version
- alot of improviments from bz #476832 Comment #10 From  Mamoru Tasaka

* Wed Jan 27 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 1.2.8.19-3
- fix some rpmlint messages about install-info and chkconfig

* Wed Jan 27 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 1.2.8.19-2
- add installinfo scriptlets

* Wed Jan 27 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 1.2.8.19-1
- upgrade to new version, improve spec files with alternatives

* Wed Jan 23 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 1.2.8.18-1
- create sub-packages for mysql and postgresql
- Rebuild for Fedora 10

* Thu Mar 27 2003 Don Moore <bboy@bboy.net>
- now installs startup scripts

* Fri Jul 12 2002 Don Moore <bboy@bboy.net>
- initial public release
