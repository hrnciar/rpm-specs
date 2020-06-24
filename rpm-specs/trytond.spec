%global major 4.0

Name:           trytond
Version:        4.0.4
Release:        14%{?dist}
Summary:        Server for the Tryton application framework

License:        GPLv3+
URL:            http://www.tryton.org
Source0:        http://downloads.tryton.org/%{major}/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
Source2:        %{name}_log.conf
Source20:       %{name}.service

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-tools
BuildRequires:  python3-sphinx
BuildRequires:  systemd

Requires:       %{name}-server = %{version}-%{release}
Requires:       python3-lxml
Requires:       python3-relatorio
Requires:       python3-sql
Requires:       python3-pydot
Requires:       python3-dateutil
Requires:       python3-polib
Requires:       python3-werkzeug
Requires:       python3-wrapt
Requires(pre):  shadow-utils
%{?systemd_requires}

Provides:       tryton(kernel) = %{major}


%description
Tryton is a three-tiers high-level general purpose application framework
written in Python and use PostgreSQL as database engine. It is the core base
of an Open Source ERP. It provides modularity, scalability and security.

The core of Tryton (also called Tryton kernel) provides all the necessary
functionalities for a complete application framework: data persistence (i.e
an ORM with extensive modularity), users management (authentication, fine
grained control for data access, handling of concurrent access of resources),
workflow and report engines, web services and internationalisation. Thus
constituting a complete application platform which can be used for any
relevant purpose.


%package openoffice
Summary:        OpenOffice.org support for Tryton Server
Requires:       %{name} = %{version}-%{release}
Requires:       python3-openoffice

%description openoffice
OpenOffice.org support for Tryton Server.


%package mysql
Summary:        MySQL support for Tryton Server
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-server = %{version}-%{release}
Requires:       MySQL-python3

%description mysql
MySQL support for Tryton Server.


%package pgsql
Summary:        PostgreSQL support for Tryton Server
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-server = %{version}-%{release}
Requires:       python3-psycopg2

%description pgsql
PostgreSQL support for Tryton Server.


%package sqlite
Summary:        SQLite support for Tryton Server
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-server = %{version}-%{release}

%description sqlite
SQLite support for Tryton Server.


%prep
%setup -q


%build
%py3_build

# docs
pushd doc
make html
popd


%install
%py3_install

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m 640 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}

mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644 %{SOURCE20} $RPM_BUILD_ROOT%{_unitdir}/

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/{lib,log}/%{name}


%pre
getent group tryton > /dev/null || /usr/sbin/groupadd -r tryton
getent passwd tryton > /dev/null || /usr/sbin/useradd -r -g tryton \
       -d %{_localstatedir}/lib/%{name} -s /sbin/nologin tryton
:

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%doc CHANGELOG COPYRIGHT INSTALL LICENSE README
%doc doc/_build/html
%{_unitdir}/%{name}.service
%attr(0640,tryton,tryton) %config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}_log.conf
%{_bindir}/%{name}
%{_bindir}/%{name}-admin
%{_bindir}/%{name}-cron
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.egg-info/
%exclude %{python3_sitelib}/%{name}/backend/mysql
%exclude %{python3_sitelib}/%{name}/backend/postgresql
%exclude %{python3_sitelib}/%{name}/backend/sqlite
%attr(0750,tryton,tryton) %{_localstatedir}/lib/%{name}
%attr(0750,tryton,tryton) %{_localstatedir}/log/%{name}

%files openoffice

%files mysql
%{python3_sitelib}/%{name}/backend/mysql

%files pgsql
%{python3_sitelib}/%{name}/backend/postgresql

%files sqlite
%{python3_sitelib}/%{name}/backend/sqlite


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.4-14
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.4-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.4-11
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.0.4-7
- Rebuilt for Python 3.7

* Mon Mar 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.0.4-6
- Build docs with Python 3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.0.4-2
- Rebuild for Python 3.6

* Fri Sep 09 2016 Dan Horák <dan@danny.cz> - 4.0.4-1
- new upstream version 4.0.4

* Thu Jul 21 2016 Dan Horák <dan@danny.cz> - 4.0.2-1
- new upstream version 4.0.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Dan Horák <dan@danny.cz> - 2.6.2-1
- new upstream version 2.6.2

* Sat Oct 27 2012 Dan Horák <dan@danny.cz> - 2.6.0-1
- new upstream version 2.6.0

* Tue Sep 11 2012 Dan Horák <dan@danny.cz> - 2.4.2-1
- new upstream version 2.4.2 (CVE-2012-2238)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Dan Horák <dan@danny.cz> - 2.4.1-3
- make pywebdav dependency versioned

* Mon Jun 04 2012 Dan Horák <dan@danny.cz> - 2.4.1-2
- convert from initscript to systemd unit and use the unit file for Fedora >= 17

* Mon Jun 04 2012 Dan Horák <dan@danny.cz> - 2.4.1-1
- new upstream version 2.4.1

* Fri Mar 30 2012 Dan Horák <dan@danny.cz> - 2.2.2-1
- new upstream version 2.2.2 (CVE-2012-0215)

* Mon Mar 05 2012 Dan Horák <dan@danny.cz> - 2.2.1-3
- add missing R:

* Wed Feb  8 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 2.2.1-2
- Remove the python-sqlite2 dep in Fedora as tryton will work with sqlite3 from
  the python stdlib

* Sun Jan 15 2012 Dan Horák <dan@danny.cz> - 2.2.1-1
- new upstream version 2.2.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 23 2011 Dan Horák <dan@danny.cz> - 2.0.2-1
- new upstream version 2.0.2

* Mon Jun 06 2011 Dan Horák <dan@danny.cz> - 2.0.1-1
- new upstream version 2.0.1

* Tue May 03 2011 Dan Horák <dan@danny.cz> - 2.0.0-1
- new upstream version 2.0.0

* Mon Feb 21 2011 Dan Horák <dan[at]danny.cz> 1.8.2-1
- update to upstream version 1.8.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 17 2010 Dan Horák <dan[at]danny.cz> 1.8.1-2
- drop the conflicts between db backends, they can co-exist

* Tue Nov 16 2010 Dan Horák <dan[at]danny.cz> 1.8.1-1.1
- fix the tryton(kernel) Provides:

* Sat Nov 13 2010 Dan Horák <dan[at]danny.cz> 1.8.1-1
- update to upstream version 1.8.1

* Sat Nov 13 2010 Dan Horák <dan[at]danny.cz> 1.6.2-1
- update to upstream version 1.6.2
- do not duplicate the logs on console (#641609)

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jul 15 2010 Dan Horák <dan[at]danny.cz> 1.6.0-3
- build documentation
- add R: python-dateutil

* Wed Jul  7 2010 Dan Horák <dan[at]danny.cz> 1.6.0-2
- fix the tryton(kernel) Provides:

* Wed Jul  7 2010 Dan Horák <dan[at]danny.cz> 1.6.0-1
- update to upstream version 1.6.0
- split the DB support into subpackages

* Thu Apr  1 2010 Dan Horák <dan[at]danny.cz> 1.4.5-1
- update to upstream version 1.4.5

* Fri Feb 19 2010 Dan Horák <dan[at]danny.cz> 1.4.4-1
- update to upstream version 1.4.4

* Thu Dec 10 2009 Dan Horák <dan[at]danny.cz> 1.4.3-1
- update to upstream version 1.4.3

* Sat Nov 28 2009 Dan Horák <dan[at]danny.cz> 1.4.2-1
- update to upstream version 1.4.2

* Wed Oct 21 2009 Dan Horák <dan[at]danny.cz> 1.4.1-1
- update to upstream version 1.4.1

* Mon Aug 31 2009 Dan Horák <dan[at]danny.cz> 1.2.2-1
- update to upstream version 1.2.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Dan Horák <dan[at]danny.cz> 1.2.1-1
- update to upstream version 1.2.1

* Fri May 22 2009 Dan Horák <dan[at]danny.cz> 1.2.0-1
- update to upstream version 1.2.0

* Fri Mar  6 2009 Dan Horák <dan[at]danny.cz> 1.0.3-1
- update to upstream version 1.0.3

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 Dan Horák <dan[at]danny.cz> 1.0.2-2
- add modular support for webdav

* Thu Jan  8 2009 Dan Horák <dan[at]danny.cz> 1.0.2-1
- modularize the openoffice.org support
- update to upstream version 1.0.2

* Tue Dec  2 2008 Dan Horák <dan[at]danny.cz> 1.0.1-2
- add dependency on python-openoffice

* Mon Dec  1 2008 Dan Horák <dan[at]danny.cz> 1.0.1-1
- update to upstream version 1.0.1

* Fri Nov 28 2008 Dan Horák <dan[at]danny.cz> 1.0.0-2
- keep modules in %%python_sitelib after a discussion with upstream, user
  written and non packaged modules will be symlinked there

* Fri Nov 28 2008 Dan Horák <dan[at]danny.cz> 1.0.0-1
- initial Fedora version
