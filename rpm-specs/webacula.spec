Name:          webacula
Version:       5.0.3
Release:       16%{?dist}
Summary:       Web interface of a Bacula backup system
Summary(ru):   Веб интерфейс для Bacula backup system

License:    GPLv3+
URL:        http://webacula.sourceforge.net/
Source0:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildArch:  noarch

Requires: webserver
Requires: bacula-console >= 5.0
Requires: php-ZendFramework >= 1.8.3
Requires: php >= 5.2.4
Requires: php-pdo
Requires: php-json
Requires: php-pcre
Requires: php-gd
Requires: php-xml

%description
Webacula - Web Bacula - web interface of a Bacula backup system.
Supports the run Job, restore all files or selected files,
restore the most recent backup for a client,
restore backup for a client before a specified time,
mount/umount Storages, show scheduled, running and terminated Jobs and more.
Supported languages: English, French, German, Italian,
Portuguese Brazil, Russian.

%description -l ru
Webacula - Web Bacula - веб интерфейс для Bacula backup system.
Поддерживает запуск Заданий, восстановление всех или выбранных файлов,
восстановление самого свежего бэкапа для клиента,
восстановление бэкапа для клиента сделанного перед указанным временем,
монтирование/размонтирование Хранилищ, показ запланированных, 
выполняющихся и завершенных Заданий и прочее.
Поддерживаемые языки: английский, французский, немецкий, итальянский,
бразильский португальский, русский.


%prep
%setup -q
rm -f ./application/.htaccess
rm -f ./html/test_mod_rewrite/.htaccess
rm -f ./html/.htaccess
rm -f ./install/.htaccess
rm -f ./languages/.htaccess
rm -f ./application/.htaccess
rm -f ./docs/.htaccess



%build


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/application
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/html
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/languages
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/library
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/install

cp ./application/config.ini  $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/config.ini
rm -f ./application/config.ini
ln -s %{_sysconfdir}/%{name}/config.ini  $RPM_BUILD_ROOT%{_datadir}/%{name}/application/config.ini 

cp ./install/webacula.conf  $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/webacula.conf
rm -f ./install/webacula.conf

install -p -m 755 ./install/webacula_clean_tmp_files.sh \
   $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/webacula_clean_tmp_files.sh
rm -f ./install/webacula_clean_tmp_files.sh

cp -pr ./application $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr ./html        $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr ./languages   $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr ./library     $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr ./install     $RPM_BUILD_ROOT%{_datadir}/%{name}



%files
%doc 4CONTRIBUTORS 4CONTRIBUTORS.ru AUTHORS COPYING README UPDATE ChangeLog
%doc docs/
%{_datadir}/%{name}/application
%{_datadir}/%{name}/html
%{_datadir}/%{name}/library
%{_datadir}/%{name}/install
%{_sysconfdir}/cron.daily/webacula_clean_tmp_files.sh
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/languages
%config(noreplace) %{_sysconfdir}/httpd/conf.d/webacula.conf
%config(noreplace) %{_sysconfdir}/%{name}/config.ini
%lang(de) %{_datadir}/%{name}/languages/de
%lang(en) %{_datadir}/%{name}/languages/en
%lang(fr) %{_datadir}/%{name}/languages/fr
%lang(pt) %{_datadir}/%{name}/languages/pt
%lang(ru) %{_datadir}/%{name}/languages/ru
%lang(it) %{_datadir}/%{name}/languages/it
%lang(es) %{_datadir}/%{name}/languages/es



%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Yuri Timofeev <tim4dev@gmail.com> 5.0.3-1
- Version 5.0.3

* Tue Aug 10 2010 Yuri Timofeev <tim4dev@gmail.com> 5.0.2-1
- Version 5.0.2

* Thu May 12 2010 Yuri Timofeev <tim4dev@gmail.com> 5.0.1-1
- Version 5.0.1

* Thu Feb 20 2010 Yuri Timofeev <tim4dev@gmail.com> 5.0-1
- Version 5.0

* Tue Feb 16 2010 Yuri Timofeev <tim4dev@gmail.com> 3.5-1
- Version 3.5

* Wed Dec 9 2009 Yuri Timofeev <tim4dev@gmail.com> 3.4.1-1
- Version 3.4.1

* Fri Oct 16 2009 Yuri Timofeev <tim4dev@gmail.com> 3.4-1
- Version 3.4

* Tue Oct 13 2009 Yuri Timofeev <tim4dev@gmail.com> 3.3-6
- Fix #526855.

* Tue Oct 13 2009 Yuri Timofeev <tim4dev@gmail.com> 3.3-5
- Fix #526855. Remove Zend Framework from source.

* Tue Oct 13 2009 Yuri Timofeev <tim4dev@gmail.com> 3.3-4
- Fix #526855

* Mon Oct 12 2009 Yuri Timofeev <tim4dev@gmail.com> 3.3-3
- Fix #526855

* Sat Oct 10 2009 Yuri Timofeev <tim4dev@gmail.com> 3.3-2
- Fix #526855 "Review Request"

* Thu Oct 08 2009 Yuri Timofeev <tim4dev@gmail.com> 3.3-1
- Initial Spec file creation for Fedora
