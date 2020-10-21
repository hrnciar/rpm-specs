Name:		php-voms-admin
%define shortname pva
Version:	0.7.0
Release:	9%{?dist}
Summary:	Web based interface to control VOMS parameters written in PHP

License:	ASL 2.0
URL:		http://grid.org.ua/development/pva/
#		The source was created from a svn checkout
#		svn export http://svn.nordugrid.org/repos/nordugrid/contrib/pva/tags/pva-0.7.0 php-voms-admin-0.7.0
#		tar -z -c -f php-voms-admin-0.7.0.tar.gz php-voms-admin-0.7.0
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

Requires:	httpd
Requires:	php
Requires:	php-mysqli
Requires:	php-PHPMailer
Requires:	php-soap
Requires:	php-gd
Requires:	mysql >= 5.0.0
Provides:	%{shortname} = %{version}-%{release}

%if %{?fedora}%{!?fedora:0} >= 23 || %{?rhel}%{!?rhel:0} >= 8
Requires(post):		policycoreutils-python-utils
Requires(postun):	policycoreutils-python-utils
%else
%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 6
Requires(post):		policycoreutils-python
Requires(postun):	policycoreutils-python
%endif
%endif

%description
PHP VOMS-Admin (PVA) originally implemented the same functions as the
traditional JAVA-based VOMS-Admin (v.2.0.18) interface for Apache
Tomcat. It was designed to be more flexible and stable, provide easy
scalability and minimize resource usage. PVA is fully compatible with
the vomsd mysql backend.

%prep
%setup -q

# Remove bundled PHPMailer
rm modules/class.phpmailer.php modules/class.smtp.php
sed 's!//REDHAT_PHPMAILER//!!' -i modules/miscmail.php

%build
# Nothing to build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_datadir}/%{shortname}/conf
mkdir -p %{buildroot}%{_sysconfdir}/%{shortname}/vomses
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
mkdir -p %{buildroot}%{_localstatedir}/www/%{shortname}/mail-copies
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man5

sed '/^ADDVOCONF=/s!=.*!=%{_sysconfdir}/%{shortname}/addvo.conf!' \
    addvo > %{buildroot}%{_sbindir}/pva-addvo
chmod 755 %{buildroot}%{_sbindir}/pva-addvo

install -p -m 755 pva-dbschema-update %{buildroot}%{_sbindir}

install -p -m 644 index.php rpc.php \
    VOMSACL.php \
    VOMSAdmin.php \
    VOMSAttributes.php \
    VOMSCompatibility.php \
    VOMSCompatibility2.php \
    VOMSRegistration.php \
    APIv2.php \
    %{buildroot}%{_datadir}/%{shortname}

for dir in interfaces js kcaptcha lang modules pics styles wsdl rest ; do
    cp -pr ${dir} %{buildroot}%{_datadir}/%{shortname}
done

sed -e 's!%%SYSCONFDIR%%!%{_sysconfdir}!g' \
    -e 's!%%LIBDIR%%!%{_libdir}!g' \
    addvo.conf > %{buildroot}%{_sysconfdir}/%{shortname}/addvo.conf

sed -e 's!%%INSTALLROOT%%!%{_datadir}/%{shortname}!g' \
    -e '/\$mail_filecopies_path=/s!".*"!"%{_localstatedir}/www/%{shortname}/mail-copies"!' \
    conf/config.inc > %{buildroot}%{_sysconfdir}/%{shortname}/%{shortname}-config

install -p -m 640 conf/vomses/external \
    %{buildroot}%{_sysconfdir}/%{shortname}/vomses

install -p -m 640 conf/vomses/vogroups \
    %{buildroot}%{_sysconfdir}/%{shortname}/vomses

sed 's!%%DATADIR%%!%{_datadir}!g' \
    %{shortname}.conf > %{buildroot}%{_sysconfdir}/httpd/conf.d/%{shortname}.conf

ln -s %{_sysconfdir}/%{shortname}/%{shortname}-config \
    %{buildroot}%{_datadir}/%{shortname}/conf/config.inc
ln -s %{_sysconfdir}/%{shortname}/vomses \
    %{buildroot}%{_datadir}/%{shortname}/conf

install -p -m 644 pva-addvo.1 %{buildroot}%{_mandir}/man1/
install -p -m 644 pva-dbschema-update.1 %{buildroot}%{_mandir}/man1/
install -p -m 644 addvo.conf.5 %{buildroot}%{_mandir}/man5/
install -p -m 644 pva-config.5 %{buildroot}%{_mandir}/man5/

%post
%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 6
semanage fcontext -a -t httpd_sys_rw_content_t \
"%{_localstatedir}/www/%{shortname}/mail-copies(/.*)?" 2>/dev/null || :
restorecon -R %{_localstatedir}/www/%{shortname}/mail-copies 2>/dev/null || :
%endif

# update DB schema for served VOs
for voconf in $( find %{_sysconfdir}/%{shortname}/vomses -name '*.conf' ); do
    eval $( php -r "require(\"$voconf\"); 
	printf(\"DBHOST='%%s'\\nDBNAME='%%s'\\nDBUSER='%%s'\\nDBPASSWD='%%s'\\n\", \$dbhost, \$dbname, \$dbuser, \$dbpasswd);"
    )
    %{_sbindir}/pva-dbschema-update -h "${DBHOST}" -d "${DBNAME}" -u "${DBUSER}" -p "${DBPASSWD}"
    if [ $? -ne 0 ]; then
	echo "Database schema update for VO specified in config file '${voconf}' finished with errors."
    fi
done

%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 6
%postun
if [ $1 -eq 0 ]; then
  semanage fcontext -d -t httpd_sys_rw_content_t \
  "%{_localstatedir}/www/%{shortname}/mail-copies(/.*)?" 2>/dev/null || :
  [ -d %{_localstatedir}/www/%{shortname}/mail-copies ] && \
  restorecon -R %{_localstatedir}/www/%{shortname}/mail-copies 2>/dev/null || :
fi
%endif

%{!?_licensedir: %global license %%doc}

%files
%{_sbindir}/pva-addvo
%{_sbindir}/pva-dbschema-update
%{_mandir}/man1/pva-addvo.1*
%{_mandir}/man1/pva-dbschema-update.1*
%{_mandir}/man5/addvo.conf.5*
%{_mandir}/man5/pva-config.5*
%{_datadir}/%{shortname}
%dir %{_localstatedir}/www/%{shortname}
%attr(-,apache,apache) %{_localstatedir}/www/%{shortname}/mail-copies
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{shortname}.conf
%dir %{_sysconfdir}/%{shortname}
%dir %{_sysconfdir}/%{shortname}/vomses
%attr(640,root,root) %config(noreplace) %{_sysconfdir}/%{shortname}/addvo.conf
%attr(640,apache,apache) %config(noreplace) %{_sysconfdir}/%{shortname}/pva-config
%attr(640,apache,apache) %config(noreplace) %{_sysconfdir}/%{shortname}/vomses/external
%attr(640,apache,apache) %config(noreplace) %{_sysconfdir}/%{shortname}/vomses/vogroups
%doc AUTHORS CHANGELOG NOTES README README.transactions README.Fedora
%license LICENSE

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 11 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.7.0-1
- Update to released version 0.7.0
- Change Requires php-mysql to php-mysqli

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 26 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6.7-6
- Adapt to new policycoreutils packaging

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6.7-1
- Update to released version 0.6.7

* Fri Oct 26 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6.5-2
- Minor fixes to post installation script
- Add missing package dependencies

* Tue Oct 23 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6.5-1
- Update to released version 0.6.5

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 28 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6-1
- Update to released version 0.6

* Fri Jun 17 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.5.1-2
- Add file context handling scriptlets

* Wed Jun 08 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.5.1-1
- Update to released version 0.5.1

* Sun May 15 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.5-1
- Update to released version 0.5

* Fri Jun 11 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.5-0.svn18160
- Initial package
