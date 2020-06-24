Name:			beacon
Version:		0.5
Release:		20%{?dist}
Summary:		WYSIWYG editor for docbook xml

License:		GPLv3+
URL:			http://fedoraproject.org/wiki/DocBook_Editor
Source0:		%{name}-%{version}.tar.gz
Source1:		httpd-beacon.conf
BuildArch:		noarch
Requires:		php, httpd, php-xml, mysql-server, mysql, php-mysql

%description
Beacon is an XSLT based plug-able WYSIWYG editor for DocBook xml. It
is intended to serve as an easy to use tool which will attract new
contributors who would otherwise be discouraged by the steep learning
curve involved with DocBook and will also provide a convenient
alternative to those who are old-timers. More information is available
at https://fedoraproject.org/wiki/DocBook_Editor_Documentation and
https://fedoraproject.org/wiki/DocBook_Editor_Feature.

%prep
%setup -q

cp %{SOURCE1} httpd-beacon.conf

%build
# Empty build

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr sysconfdir=$RPM_BUILD_ROOT/etc/

#mkdir -p $RPM_BUILD_ROOT/%{_datadir}/beacon
#cp -rp beacon php $RPM_BUILD_ROOT/%{_datadir}/beacon/
#mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/
#cp -p  httpd-beacon.conf $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/


%files
%doc docs/* LICENSE README TODO
%{_datadir}/beacon/*
%attr(0700,apache,apache)

%config(noreplace) %{_sysconfdir}/httpd/conf.d/httpd-beacon.conf
%config(noreplace) %{_datadir}/beacon/php/settings.php


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec  5 2012 Remi Collet <rcollet@redhat.com> - 0.5-8
- fix configuration file for httpd 2.4, #871377

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jun 18 2011 P J P <pj.pandit@yahoo.co.in> 0.5-5
- Updated source to include upstream bug fixes.
- included httpd-beacon.conf into the source tarball.

* Tue May 10 2011 Satya Komaragiri <satyak@fedoraproject.org> 0.5-4
- Added dependency on php-mysql.
- Made mysql login as default.
- Handled file names with spaces.

* Wed Aug 24 2009 Satya Komaragiri <satyak@fedoraproject.org> 0.5-3
- Improved description.
- Reverted back to requiring httpd.

* Wed Aug 24 2009 Satya Komaragiri <satyak@fedoraproject.org> 0.5-2
- Changed requires to webserver from httpd
- Added beacon/php/settings.php to the config section.
- Removed /var/tmp as we are using mysql now.
- Added more documentation and moved README.fedora inside the tarball.

* Wed Aug 12 2009 Satya Komaragiri <satyak@fedoraproject.org> 0.5-1
- Initial version
