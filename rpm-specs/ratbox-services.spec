Name:		ratbox-services
Version:	1.2.4
Release:	7%{?dist}
Summary:	Service package for ircd-ratbox

License:	GPLv2
URL:		https://services.ratbox.org
Source0:	%{url}/download/%{name}-%{version}.tgz
Source1:	ratbox-services.init
Source2:	ratbox-services.conf
Source3:	ratbox-services.logrotate

Patch0:		ratbox-services-1.2.1-dbpath.patch
Patch1:		ratbox-services-1.2.1-oldflex.patch
Patch2:		ratbox-services-1.2.4-crypt-null-pointer-dereference.patch
Patch3:		ratbox-services-1.2.4-gcc10.patch

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gcc
BuildRequires:	libpq-devel
BuildRequires:	mariadb-connector-c-devel
BuildRequires:	pcre-devel
BuildRequires:	perl-generators
BuildRequires:	sqlite-devel

Requires:	MTA
Requires:	ircd-ratbox

Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service

%description
ratbox-services is a services package written mostly from
scratch for use with ircd-ratbox. It is highly configurable,
with nearly all options being set in a config that can be
rehashed rather than set at compile time. It also uses the
SQLite database backend, which works as a database interface
to a normal file, meaning no separate database software must be running.


%package devel
Summary:	Devel package for ircd-ratbox service
Requires:	%{name} = %{version}-%{release}

%description devel
Headers for ratbox-services, service package for ircd-ratbox.


%prep
%autosetup -p 1

cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
sed -e '/perl(definetolength.pl)/d'
EOF

%define __perl_requires %{_builddir}/%{name}-%{version}/%{name}-req
chmod +x %{__perl_requires}


%build
sed 's/-Werror//g' -i configure # usage of -Werror in stable version of software is a bug
export CFLAGS="%{optflags} -fgnu89-inline"
%configure					\
	--bindir=%{_sbindir}			\
	--with-helpdir=%{_datadir}/%{name}	\
	--with-confdir=%{_sysconfdir}		\
	--sysconfdir=%{_sysconfdir}		\
	--with-logdir=%{_var}/log/%{name}	\
	--with-nicklen=32			\
	--with-topiclen=350
#%%make_build
make


%install
%make_install
mkdir -p %{buildroot}%{_var}/lib/%{name}/
install -D -m755 %{SOURCE1} %{buildroot}%{_sysconfdir}/init.d/%{name}
install -D -m640 %{SOURCE2} %{buildroot}%{_sysconfdir}/ratbox-services.conf
install -D -m664 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/ratbox-services
install -D -m655 tools/base/schema-sqlite.txt %{buildroot}%{_datadir}/%{name}/schemas/schema-sqlite.txt
install -D -m655 tools/base/schema-mysql.txt %{buildroot}%{_datadir}/%{name}/schemas/schema-mysql.txt
install -D -m655 tools/base/schema-pgsql.txt %{buildroot}%{_datadir}/%{name}/schemas/schema-pgsql.txt


%post
if [ $1 -eq 0 ]; then
	/sbin/chkconfig --add ratbox-services
fi

if [ ! -e %{_var}/lib/%{name}/%{name}.db ]; then
	/usr/bin/sqlite3 init %{_var}/lib/%{name}/%{name}.db
	/usr/bin/sqlite3 %{_var}/lib/%{name}/%{name}.db < %{_datadir}/%{name}/schemas/schema-sqlite.txt
fi


%preun
if [ $1 -eq 0 ]; then
	/sbin/service ratbox-services stop >/dev/null 2>&1
	/sbin/chkconfig --del ratbox-services
fi


%files
%doc DBMOVE INSTALL* RELEASE_NOTES SVN-Access README doc/*
%license CREDITS LICENSE
%attr(-,root,ircd) %{_sbindir}/%{name}
%{_sbindir}/*.pl
%{_sysconfdir}/init.d/%{name}
%{_datadir}/%{name}
%config(noreplace) %attr(-,root,ircd) %{_sysconfdir}/ratbox-services.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/ratbox-services
%dir %attr(-,ircd,ircd) %{_var}/lib/%{name}
%dir %attr(750,ircd,ircd) %{_var}/log/%{name}
%exclude %{_sysconfdir}/example.conf


%files devel
%{_includedir}/*.h


%changelog
* Thu Mar 05 2020 Than Ngo <than@redhat.com> - 1.2.4-7
- Fixed bz#1799965, FTBFS

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.2.4-3
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Jan 03 2019 Björn Esser <besser82@fedoraproject.org> - 1.2.4-2
- Use sequential make to fix Makefile dependencies

* Thu Jan 03 2019 Björn Esser <besser82@fedoraproject.org> - 1.2.4-1
- Update to 1.2.4
- Fix FTBFS (#1556312, #1606078)
- Use mariadb-connector-c-devel (#1494072)
- Modernize spec-file

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.2.1-18
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.2.1-9
- Perl 5.18 rebuild

* Sat Feb 23 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.2.1-8
- Fix F-19 FTBFS due to old flex parser skeleton code (#914427).
- Build with system PCRE instead of a bundled copy.
- Fix bogus date in %%changelog.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Marek Mahut <mmahut@fedoraproject.org> - 1.2.1-1
- Initial package build
