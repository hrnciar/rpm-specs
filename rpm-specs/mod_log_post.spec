# /usr/sbin/apxs with httpd < 2.4 and defined as /usr/bin/apxs with httpd >= 2.4
%{!?_httpd_apxs:       %{expand: %%global _httpd_apxs       %%{_sbindir}/apxs}}
%{!?_httpd_mmn:        %{expand: %%global _httpd_mmn        %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}

Summary:	Module for the Apache web server to log all HTTP POST messages
Summary(de):	Modul für den Apache Webserver zur Protokollierung von HTTP POST
Name:		mod_log_post
Version:	0.1.0
Release:	21%{?dist}
License:	GPLv2 with exceptions
URL:		http://ftp.robert-scheck.de/linux/%{name}/
Source:		http://ftp.robert-scheck.de/linux/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:	httpd-devel >= 2.0.39
Requires:	httpd-mmn = %{_httpd_mmn}
Patch0:        mod_log_post-0.1.0-httpd24.patch

%description
mod_log_post can be used for logging all HTTP POST messages. The module
is based on mod_security but in difference it never returns any error
messages to the visitors of your websites. Logging of POST data can be
very useful for debugging purposes or analyses. As the module is loaded
and run after the SSL decryption, it even can log POST data transmitted
before via SSL to the Apache web server.

%description -l de
mod_log_post kann verwendet werden, um POST von HTTP zu protokollieren.
Das Modul basiert auf mod_security, im Unterschied dazu jedoch liefert
es niemals eine Fehlermeldung an den Besucher einer Webseite aus. Das
Protokollieren von POST-Daten kann bei der Fehlersuche bzw. Analyse sehr
hilfreich sein. Nachdem das Modul nach der SSL-Entschlüsselung geladen
und ausgeführt wird, kann es auch POST-Daten mitschreiben, die mittels
SSL an den Apache Webserver übermittelt worden sind.

%prep
%setup -q
%patch0 -p1 -b .httpd24

%build
%configure --with-apxs=%{_httpd_apxs}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
# Adapt for 2.4-style module configuration
mkdir -p $RPM_BUILD_ROOT%{_httpd_modconfdir}
sed -n /^LoadModule/p $RPM_BUILD_ROOT%{_httpd_confdir}/log_post.conf \
    >> $RPM_BUILD_ROOT%{_httpd_modconfdir}/10-log_post.conf
sed -i /^LoadModule/d $RPM_BUILD_ROOT%{_httpd_confdir}/log_post.conf
%endif

%files
%doc ChangeLog COPYING LICENSING_EXCEPTION README
%{_libdir}/httpd/modules/%{name}.so
%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
%config(noreplace) %{_httpd_modconfdir}/10-log_post.conf
%endif
%config(noreplace) %{_httpd_confdir}/log_post.conf

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Joe Orton <jorton@redhat.com> - 0.1.0-9
- fix _httpd_mmn expansion in absence of httpd-devel

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Joe Orton <jorton@redhat.com> - 0.1.0-5
- update for httpd 2.4 (patch by Jan Kaluza, #809714)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Robert Scheck <robert@fedoraproject.org> 0.1.0-1
- Upgrade to 0.1.0
- Initial spec file for Fedora and Red Hat Enterprise Linux
