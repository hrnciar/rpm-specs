# Fedora/remirepo spec file for glpi
#
# Copyright (c) 2007-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit  7fbee4f15b37c98f6f2078bd10634ef02b5edc25
%global gh_short   %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date    20160923
%global gh_owner   glpi-project
%global gh_project glpi

# System policy includes GLPI rules
%global useselinux 0

# nginx 1.6 with nginx-filesystem
%global with_nginx     1
# httpd 2.4 with httpd-filesystem
%global with_httpd     1

%global with_tests  0%{!?_without_tests:1}


Name:           %{gh_project}
%global upstream_version 9.4.6
#global upstream_prever  RC2
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        1%{?dist}
Summary:        Free IT asset management software
Summary(fr):    Gestion Libre de Parc Informatique

License:        GPLv2+ and GPLv3+ and MIT
URL:            http://www.glpi-project.org/
# Upstream sources (not the github auto-generated archive)
Source0:        https://github.com/%{gh_owner}/%{name}/archive/%{gh_commit}/%{name}-%{upstream_version}%{?upstream_prever:-%{upstream_prever}}-%{gh_short}.tar.gz

Source1:        %{name}-httpd.conf
Source2:        %{name}-downstream.php
Source12:       %{name}-downstream-test.php
Source3:        %{name}-logrotate
Source4:        %{name}-nginx.conf
Source5:        %{name}-fedora-autoloader.php
# Temporary minify script, waiting for consolidation/robo
Source6:        %{name}-minify.php
# Override PHP configuration for php-fpm
Source7:        %{name}-user.ini

# allow to install in /usr/bin
Patch0:         %{name}-bin.patch

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  php-cli
%if %{with_tests}
BuildRequires:  mariadb-server >= 10
# Missing in mariadb
BuildRequires:  hostname
BuildRequires:  php-mysqli
BuildRequires:  php-xmlrpc
# PHP libs
BuildRequires:  php-htmLawed
BuildRequires: (php-composer(iamcal/lib_autolink)             >= 1.7    with php-composer(iamcal/lib_autolink)             < 2)
BuildRequires: (php-composer(phpmailer/phpmailer)             >= 6.0    with php-composer(phpmailer/phpmailer)             < 7)
BuildRequires: (php-composer(sabre/vobject)                   >= 4.1    with php-composer(sabre/vobject)                   < 5)
BuildRequires: (php-composer(simplepie/simplepie)             >= 1.5    with php-composer(simplepie/simplepie)             < 2)
BuildRequires: (php-composer(tecnickcom/tcpdf)                >= 6.2.16 with php-composer(tecnickcom/tcpdf)                < 7)
BuildRequires: (php-composer(sebastian/diff)                  >= 1.4    with php-composer(sebastian/diff)                  < 4)
BuildRequires: (php-autoloader(zendframework/zend-cache)      >= 2.8    with php-autoloader(zendframework/zend-cache)      < 3)
BuildRequires: (php-autoloader(zendframework/zend-i18n)       >= 2.8    with php-autoloader(zendframework/zend-i18n)       < 3)
BuildRequires: (php-autoloader(zendframework/zend-serializer) >= 2.8    with php-autoloader(zendframework/zend-serializer) < 3)
BuildRequires: (php-composer(michelf/php-markdown)            >= 1.6    with php-composer(michelf/php-markdown)            < 2)
BuildRequires: (php-composer(true/punycode)                   >= 2.1    with php-composer(true/punycode)                   < 3)
BuildRequires: (php-composer(paragonie/random_compat)         >= 2.0    with php-composer(paragonie/random_compat)         < 3)
BuildRequires: (php-composer(monolog/monolog)                 >= 1.23   with php-composer(monolog/monolog)                 < 2)
BuildRequires: (php-composer(elvanto/litemoji)                >= 1.4    with php-composer(elvanto/litemoji)                < 3)
BuildRequires: (php-composer(symfony/console)                 >= 3.4    with php-composer(symfony/console)                 < 4)
BuildRequires: (php-composer(leafo/scssphp)                   >= 0.7.7  with php-composer(leafo/scssphp)                   < 1)
# requires-dev
BuildRequires: (php-composer(guzzlehttp/guzzle)               >= 6      with php-composer(guzzlehttp/guzzle)               < 7)
BuildRequires: (php-composer(atoum/atoum)                     >= 3.3    with php-composer(atoum/atoum)                     < 4)
BuildRequires: (php-composer(mikey179/vfsStream)              >= 1.6    with php-composer(mikey179/vfsStream)              < 2)
%endif
# To minimize assets
BuildRequires: (php-composer(natxet/CssMin)                   >= 3.0   with php-composer(natxet/CssMin)                 < 4)
BuildRequires: (php-composer(patchwork/jsqueeze)              >= 2.0   with php-composer(patchwork/jsqueeze)            < 3)
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)

%if %{with_nginx}
Requires:       nginx-filesystem
%endif
%if %{with_httpd}
Requires:       httpd-filesystem
%endif
%if %{with_httpd} || %{with_nginx}
Requires:       webserver
Requires:       php(httpd)
%else
Requires:       httpd, mod_php
%endif
Requires:       php(language) >= 5.6
Requires:       php-reflection
Requires:       php-simplexml
Requires:       php-ctype
Requires:       php-curl
Requires:       php-date
Requires:       php-fileinfo
Requires:       php-filter
Requires:       php-gd
Requires:       php-json
Requires:       php-mbstring
Requires:       php-mysqli
Requires:       php-pcre
Requires:       php-session
Requires:       php-spl
Requires:       php-xml
Requires:       php-zlib
Requires:       php-htmLawed
Requires:      (php-composer(iamcal/lib_autolink)             >= 1.7    with php-composer(iamcal/lib_autolink)             < 2)
Requires:      (php-composer(phpmailer/phpmailer)             >= 6.0    with php-composer(phpmailer/phpmailer)             < 7)
Requires:      (php-composer(sabre/vobject)                   >= 4.1    with php-composer(sabre/vobject)                   < 5)
Requires:      (php-composer(simplepie/simplepie)             >= 1.5    with php-composer(simplepie/simplepie)             < 2)
Requires:      (php-composer(tecnickcom/tcpdf)                >= 6.2.16 with php-composer(tecnickcom/tcpdf)                < 7)
Requires:      (php-composer(sebastian/diff)                  >= 1.4    with php-composer(sebastian/diff)                  < 4)
Requires:      (php-autoloader(zendframework/zend-cache)      >= 2.8    with php-autoloader(zendframework/zend-cache)      < 3)
Requires:      (php-autoloader(zendframework/zend-i18n)       >= 2.8    with php-autoloader(zendframework/zend-i18n)       < 3)
Requires:      (php-autoloader(zendframework/zend-serializer) >= 2.8    with php-autoloader(zendframework/zend-serializer) < 3)
Requires:      (php-composer(michelf/php-markdown)            >= 1.6    with php-composer(michelf/php-markdown)            < 2)
Requires:      (php-composer(true/punycode)                   >= 2.1    with php-composer(true/punycode)                   < 3)
Requires:      (php-composer(paragonie/random_compat)         >= 2.0    with php-composer(paragonie/random_compat)         < 3)
Requires:      (php-composer(monolog/monolog)                 >= 1.23   with php-composer(monolog/monolog)                 < 2)
Requires:      (php-composer(elvanto/litemoji)                >= 1.4    with php-composer(elvanto/litemoji)                < 3)
Requires:      (php-composer(symfony/console)                 >= 3.4    with php-composer(symfony/console)                 < 4)
Requires:      (php-composer(leafo/scssphp)                   >= 0.7.7  with php-composer(leafo/scssphp)                   < 1)
Requires:       gnu-free-sans-fonts
Provides:       bundled(js-chartist-js) = 0.10.1
Provides:       bundled(js-chartist-plugin-legend) = 0.6.0
Provides:       bundled(js-chartist-plugin-tooltip) = 0.0.17
Provides:       bundled(js-fuzzy)
Provides:       bundled(js-jquery)
Provides:       bundled(js-gridstack)
Provides:       bundled(js-leaflet-control-osm-geocoder)
Provides:       bundled(prism)
Provides:       bundled(tiny_mce) = 4.7.13
# Autoloader
Requires:       php-composer(fedora/autoloader)

Requires:         %{_sysconfdir}/logrotate.d
Requires(postun): %{_bindir}/systemctl
Requires(post):   %{_bindir}/systemctl
%if %{useselinux}
Requires(post):   /sbin/restorecon
Requires(post):   /usr/sbin/semanage
Requires(postun): /usr/sbin/semanage
%endif
Requires:         crontabs
# Optional
Recommends:       php-exif
Recommends:       php-imap
Recommends:       php-ldap
Recommends:       php-xmlrpc
Recommends:       php-apcu
Recommends:       php-opcache
Recommends:       php-selinux


%description
GLPI is the Information Resource-Manager with an additional Administration-
Interface. You can use it to build up a database with an inventory for your 
company (computer, software, printers...). It has enhanced functions to make
the daily life for the administrators easier, like a job-tracking-system with
mail-notification and methods to build a database with basic information 
about your network-topology.


%description -l fr
GLPI est une application libre, distribuée sous licence GPL destinée à la
gestion de parc informatique et de helpdesk.

GLPI est composé d’un ensemble de services web écrits en PHP qui permettent
de recenser et de gérer l’intégralité des composantes matérielles ou 
logicielles d’un parc informatique, et ainsi d’optimiser le travail des
techniciens grâce à une maintenance plus cohérente.


%prep
%setup -q -n %{name}-%{gh_commit}
%patch0 -p1 -b .rpm

grep %{upstream_version} inc/define.php

find . -name \*.orig -exec rm {} \; -print

# Drop bundled Flash files
find lib -name \*.swf -exec rm {} \; -print

# Use system lib
rm -r lib/htmlawed
rm    lib/FreeSans.ttf
: bundled JS libraries
ls lib

cp  %{SOURCE2}  inc/downstream.php
cp  %{SOURCE6}  tools/minify.php
cp  %{SOURCE7}  install/.user.ini

mkdir vendor
sed -e "s,##DATADIR##,%{_datadir}," \
    %{SOURCE5} > vendor/autoload.php

mv lib/tiny_mce/lib/license.txt                   LICENSE.tiny_mce
mv lib/chartist-js-0.10.1/LICENSE-MIT             LICENSE.chartist-js
mv lib/chartist-plugin-legend-0.6.0/LICENSE       LICENSE.chartist-plugin-legend
mv lib/chartist-plugin-tooltip-0.0.17/LICENSE     LICENSE.chartist-plugin-tooltip
mv lib/gridstack/LICENSE                          LICENSE.gridstack
mv lib/jqueryplugins/spectrum-colorpicker/LICENSE LICENSE.jqueryplugins.spectrum-colorpicker
mv lib/jqueryplugins/fullcalendar/LICENSE.txt     LICENSE.jqueryplugins.fullcalendar
mv lib/jqueryplugins/jstree/LICENSE-MIT           LICENSE.jqueryplugins.jstree
mv lib/fuzzy/LICENSE-MIT                          LICENSE.fuzzy
mv lib/leaflet/plugins/leaflet-control-osm-geocoder/LICENSE LICENSE.leaflet-control-osm-geocoder

rm scripts/glpi_cron_*.sh

sed -i -e 's/\r//' LICENSE.tiny_mce

cat >cron <<EOF
# GLPI core
# Run cron to execute task even when no user connected
* * * * * apache %{_bindir}/php %{_datadir}/%{name}/front/cron.php
EOF


%build
: Minify CSS and JS files
php tools/minify.php

: Regenerate the locales
for po in locales/*.po
do
   msgfmt $po -o $(dirname $po)/$(basename $po .po).mo
done


%install
# ===== application =====
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -a COPYING.txt *.php apirest.md %{buildroot}/%{_datadir}/%{name}/

for i in ajax css front inc install js lib locales pics plugins scripts sound vendor
do   cp -ar $i %{buildroot}/%{_datadir}/%{name}/$i
done

find %{buildroot}/%{_datadir}/%{name} -type f -exec chmod 644 {} \; 

# ===== apache =====
install -Dpm 0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/httpd/conf.d/glpi.conf

# ===== Nginx =====
%if %{with_nginx}
install -Dpm 0644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/nginx/default.d/glpi.conf
%endif

# ===== config =====
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
touch %{buildroot}%{_sysconfdir}/%{name}/config_db.php
touch %{buildroot}%{_sysconfdir}/%{name}/local_define.php

# ===== files =====
mkdir -p %{buildroot}/%{_localstatedir}/lib/%{name}
cp -ar files %{buildroot}/%{_localstatedir}/lib/%{name}/files

# ===== log =====
mkdir -p %{buildroot}%{_localstatedir}/log
mv %{buildroot}/%{_localstatedir}/lib/%{name}/files/_log %{buildroot}%{_localstatedir}/log/%{name}

install -Dpm 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# ====== Cron =====
install -Dpm 0644 cron %{buildroot}%{_sysconfdir}/cron.d/%{name}

# ====== Command =====
install -Dpm 0755 bin/console %{buildroot}%{_bindir}/%{name}-console

# cleanup
find %{buildroot} -name remove.txt -exec rm -f {} \; -print

# Directories not in apache space
rm -f %{buildroot}%{_localstatedir}/lib/%{name}/files/.htaccess
# Proctection in /etc/httpd/conf.d/glpi.conf
rm -f %{buildroot}%{_datadir}/%{name}/install/mysql/.htaccess
rm -f %{buildroot}%{_datadir}/%{name}/locales/.htaccess
rm -f %{buildroot}%{_datadir}/%{name}/scripts/.htaccess


# Lang
for i in %{buildroot}%{_datadir}/%{name}/locales/*
do
  lang=$(basename $i)
  echo "%lang(${lang:0:2}) %{_datadir}/%{name}/locales/${lang}"
done >%{name}.lang


%check
%if %{with_tests}
RET=0
: Hack for vendor
sed -e '/Development dependencies/s:^://:' -i tests/bootstrap.php
rm composer.lock

: Add developement dependecies
cat << 'EOF' | tee -a vendor/autoload.php
\Fedora\Autoloader\Dependencies::required([
    //        "guzzlehttp/guzzle": "^6.0"
    "$vendor/GuzzleHttp6/autoload.php",
    "$vendor/org/bovigo/vfs/autoload.php",
]);
EOF

: No internet on the builder
export GLPI_SKIP_ONLINE=1

: Running a PHP server
export GLPI_URI=http://127.0.0.1:8089
php -S 127.0.0.1:8089 tests/router.php &>web.log &
PHPPID=$!

: Running a MariaDB server
MYSQL_TEST_HOST=127.0.0.1
MYSQL_TEST_PORT=3308
MYSQL_TEST_SOCKET=$PWD/mysql.sock
MYSQL_PID_FILE=$PWD/mysql.pid
%if 0%{?fedora} >= 32
MYSQL_USER=mockbuild
%else
MYSQL_USER=root
%endif

rm -rf data
mkdir  data
: Create the Database
%{_bindir}/mysql_install_db \
   --force \
   --log-error=$PWD/mysql.log \
   --datadir=$PWD/data

: Launch the Server
%{_libexecdir}/mysqld \
   --socket=$MYSQL_TEST_SOCKET \
   --log-error=$PWD/mysql.log \
   --pid-file=$MYSQL_PID_FILE \
   --port=$MYSQL_TEST_PORT \
   --datadir=$PWD/data &

n=15
while [ $n -gt 0 ]; do
  RESPONSE=$(%{_bindir}/mysqladmin --no-defaults --socket="$MYSQL_TEST_SOCKET" --user=$MYSQL_USER ping 2>&1 || :)
  if [ "$RESPONSE" == "mysqld is alive" ]; then
    break
  fi
  n=$(expr $n - 1)
  sleep 1
done

: Set tests configuration
cp %{SOURCE12} inc/downstream.php

: Run upstream test suite
bin/console.rpm glpi:database:install --config-dir=./tests --no-interaction  --db-port=$MYSQL_TEST_SOCKET --db-name=glpitest --db-user=$MYSQL_USER --force || RET=1

: Ignore test which raise memory issue
rm tests/functionnal/Search.php

ATOUM="%{_bindir}/atoum --debug --use-dot-report --bootstrap-file tests/bootstrap.php --no-code-coverage --max-children-number 1"
$ATOUM -d tests/units       || RET=1
$ATOUM -d tests/functionnal || RET=1
$ATOUM -d tests/web         || RET=1

: Cleanup
if [ -s $MYSQL_PID_FILE ]; then
  kill $(cat $MYSQL_PID_FILE)
fi
kill $PHPPID || :

exit $RET
%else
: Test disabled
%endif


%post
%if %{useselinux}
(
# New File context
semanage fcontext -a -s system_u -t httpd_sys_rw_content_t -r s0 "%{_sysconfdir}/%{name}(/.*)?"
semanage fcontext -a -s system_u -t httpd_var_lib_t        -r s0 "%{_localstatedir}/lib/%{name}(/.*)?"
semanage fcontext -a -s system_u -t httpd_sys_content_t    -r s0 "%{_datadir}/%{name}(/.*)?"
semanage fcontext -a -s system_u -t httpd_log_t            -r s0 "%{_localstatedir}/log/%{name}(/.*)?"
# files created by app
restorecon -R %{_sysconfdir}/%{name}
restorecon -R %{_datadir}/%{name}
restorecon -R %{_localstatedir}/lib/%{name}
restorecon -R %{_localstatedir}/log/%{name}
) &>/dev/null
%endif
%{_bindir}/systemctl condrestart httpd > /dev/null 2>&1 || :


%postun
%if %{useselinux}
if [ "$1" -eq "0" ]; then
    # Remove the File Context
    (
    semanage fcontext -d "%{_sysconfdir}/%{name}(/.*)?"
    semanage fcontext -d "%{_datadir}/%{name}(/.*)?"
    semanage fcontext -d "%{_localstatedir}/log/%{name}(/.*)?"
    semanage fcontext -d "%{_localstatedir}/lib/%{name}(/.*)?"
    ) &>/dev/null
fi
%endif
%{_bindir}/systemctl condrestart httpd > /dev/null 2>&1 || :


%files -f %{name}.lang
%license LICENSE.*
%doc *.txt *.md

%attr(2770,root,apache) %dir %{_sysconfdir}/%{name}
%ghost %config(noreplace,missingok) %{_sysconfdir}/%{name}/config_db.php
%ghost %config(noreplace,missingok) %{_sysconfdir}/%{name}/local_define.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/glpi.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%if %{with_nginx}
%config(noreplace) %{_sysconfdir}/nginx/default.d/glpi.conf
%endif

# This folder can contain private information (sessions, docs, ...)
%dir %_localstatedir/lib/%{name}
%attr(2770,root,apache) %{_localstatedir}/lib/%{name}/files

%{_bindir}/%{name}-console

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.php
%{_datadir}/%{name}/apirest.md
# License file required by installation process
%{_datadir}/%{name}/COPYING.txt
%{_datadir}/%{name}/ajax
%{_datadir}/%{name}/css
%{_datadir}/%{name}/front
%{_datadir}/%{name}/inc
%{_datadir}/%{name}/install
%{_datadir}/%{name}/js
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/pics
%{_datadir}/%{name}/plugins
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/sound
%{_datadir}/%{name}/vendor
%attr(2770,root,apache) %dir %{_localstatedir}/log/%{name}
%dir %{_datadir}/%{name}/locales


%changelog
* Tue May 05 2020 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 9.4.6-1
- update to 9.4.6
- drop patches applied upstream

* Mon Feb 10 2020 Remi Collet <remi@remirepo.net> - 9.4.5-3
- switch test suite on UDS using patch from
  https://github.com/glpi-project/glpi/pull/6921
  fix FTBFS with mariadb 10.4 #1799419

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Remi Collet <remi@remirepo.net> - 9.4.5-2
- add upstream patches for PHP 7.4
- re-enable test suite

* Wed Dec 18 2019 Remi Collet <remi@remirepo.net> - 9.4.5-1
- update to 9.4.5
- disable test suite with PHP 7.4

* Tue Sep 24 2019 Remi Collet <remi@remirepo.net> - 9.4.4-1
- update to 9.4.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Remi Collet <remi@remirepo.net> - 9.4.3-2
- allow elvanto/litemoji 2.0
  see https://github.com/glpi-project/glpi/pull/6141
  and https://github.com/glpi-project/glpi/pull/6147

* Thu Jun 20 2019 Remi Collet <remi@remirepo.net> - 9.4.3-1
- update to 9.4.3

* Thu Apr 11 2019 Remi Collet <remi@remirepo.net> - 9.4.2-1
- update to 9.4.2

* Fri Mar 15 2019 Remi Collet <remi@remirepo.net> - 9.4.1.1-1
- update to 9.4.1.1

* Thu Mar 14 2019 Remi Collet <remi@remirepo.net> - 9.4.1-1
- update to 9.4.1

* Mon Feb 11 2019 Remi Collet <remi@remirepo.net> - 9.4.0-1
- update to 9.4.0
- add dependency on symfony/console 3.4
- add dependency on leafo/scssphp 0.7.7
- add build dependency on mikey179/vfsStream 1.6
- drop dependency on fontawesome-fonts
- add weak dependency on selinux extension

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Remi Collet <remi@remirepo.net> - 9.3.3-1
- update to 9.3.3

* Tue Nov  6 2018 Remi Collet <remi@remirepo.net> - 9.3.2-3
- add missing dependency on elvanto/litemoji

* Mon Nov  5 2018 Remi Collet <remi@remirepo.net> - 9.3.2-1
- update to 9.3.2
- version 9.3.2 conflicts with glpi-fusioninventory < 1:9.3+1.2
  see https://github.com/glpi-project/glpi/issues/4837

* Wed Sep 12 2018 Remi Collet <remi@remirepo.net> - 9.3.1-1
- update to 9.3.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Remi Collet <remi@remirepo.net> - 9.3.0-2
- update to 9.3.0 GA
- improve configuration to simply multi-glpi installation
- add dependency on zend-console
- drop dependency on jasig/phpcas
- raise dependency on phpmailer/phpmailer 6.0
- raise dependency on zendframework 2.8
- allow sebastian/diff 2.0 and 3.0
- add dependency on monolog/monolog
- add upstream patch to fix SQL injection CVE-2018-13049

* Tue Jul  3 2018 Remi Collet <remi@remirepo.net> - 9.2.4-2
- add upstream patch to fix SQL injection CVE-2018-13049

* Thu Jun 21 2018 Remi Collet <remi@remirepo.net> - 9.2.4-1
- update to 9.2.4

* Wed Jun 20 2018 Remi Collet <remi@remirepo.net> - 9.2.3-3
- drop dependency on initscripts #1592356
- use range dependencies on F27+

* Fri Apr 27 2018 Remi Collet <remi@remirepo.net> - 9.2.3-1
- update to 9.2.3
- add dependency on sebastian/diff 1.4

* Thu Mar  1 2018 Remi Collet <remi@remirepo.net> - 9.2.2-1
- update to 9.2.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Remi Collet <remi@remirepo.net> - 9.2.1-6
- add upstream patch to allow upgrade from 9.1.7.1

* Fri Nov 24 2017 Remi Collet <remi@remirepo.net> - 9.2.1-5
- switch to fedora/autoloader

* Fri Nov 17 2017 Remi Collet <remi@remirepo.net> - 9.2.1-3
- properly override PHP configuration for install page

* Thu Nov 16 2017 Remi Collet <remi@remirepo.net> - 9.2.1-2
- update to 9.2.1
- add dependency on zendframework/zend-serializer

* Thu Sep 28 2017 Remi Collet <remi@remirepo.net> - 9.2-1
- update to 9.2
- drop dependency on zetacomponents/graph
- raise dependency on zend-cache, zend-i18n 2.7
- raise dependency on sabre/vobject 4.1
- add dependency on paragonie/random_compat
- switch from phpunit to atoum for test suite

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Johan Cwiklinski <johan AT x-tnd DOT be> - 9.1.6-1
- update to 9.1.6

* Thu Jul 13 2017 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 9.1.5-1
- update to 9.1.5

* Wed Jun 14 2017 Remi Collet <remi@remirepo.net> - 9.1.4-1
- update to 9.1.4

* Fri Apr 28 2017 Remi Collet <remi@remirepo.net> - 9.1.3-1
- update to 9.1.3
- use phpunit6 on F26+
- raise dependency on simplepie/simplepie 1.5

* Tue Feb 21 2017 Remi Collet <remi@fedoraproject.org> - 9.1.2-3
- fix autoloader to allow sabre/vobject version 4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Johan Cwiklinski <jcwiklinski AT teclib DOT com> - 9.1.2-1
- update to 9.1.2
- add missing hostname BR from MariaDB package

* Mon Jan  9 2017 Remi Collet <remi@fedoraproject.org> - 9.1.1-3
- use new tcpdf classmap autoloader

* Tue Nov 15 2016 Remi Collet <remi@fedoraproject.org> - 9.1.1-2
- update to 9.1.1
- drop runtime dependency on guzzlehttp/guzzle

* Wed Sep 28 2016 Remi Collet <remi@fedoraproject.org> - 9.1-2
- missing API documentation

* Mon Sep 26 2016 Remi Collet <remi@fedoraproject.org> - 9.1-1
- update to 9.1
  https://github.com/glpi-project/glpi/milestone/2?closed=1
- add patch to ensure correct autolading
  open https://github.com/glpi-project/glpi/pull/1056
- add patch to ensure test suite use local server
  open https://github.com/glpi-project/glpi/pull/1058

* Fri Sep 23 2016 Johan Cwiklinski <jcwiklinski@teclib.com> - 9.1-0.1.20160922gitf4143e3
- First pre-build for 9.1 series
- Drop upstream patches
- Add unit tests

* Wed Jul 27 2016 Remi Collet <remi@fedoraproject.org> - 0.90.5-1
- update to 0.90.5
  https://github.com/glpi-project/glpi/issues?q=milestone:0.90.5

* Sat Jul 23 2016 Remi Collet <remi@fedoraproject.org> - 0.90.4-2
- fix regression in document form, adding upstream patch

* Tue Jul 19 2016 Remi Collet <remi@fedoraproject.org> - 0.90.4-1
- update to 0.90.4
  https://github.com/glpi-project/glpi/issues?q=milestone:0.90.4

* Wed Jun 22 2016 Remi Collet <remi@fedoraproject.org> - 0.90.3-2
- add upstream patch, drop dependency on zend-version

* Tue Apr 12 2016 Remi Collet <remi@fedoraproject.org> - 0.90.3-1
- update to 0.90.3
  https://github.com/glpi-project/glpi/issues?q=milestone:0.90.3

* Tue Apr  5 2016 Remi Collet <remi@fedoraproject.org> - 0.90.2-2
- fix logrotate configuration for recent version

* Fri Apr  1 2016 Remi Collet <remi@fedoraproject.org> - 0.90.2-1
- update to 0.90.2
- add weak dependency on APCu (recommended)

* Thu Feb 18 2016 Remi Collet <remi@fedoraproject.org> - 0.90.1-3
- fix Zend autoloader (to allow ZF 2.5)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 27 2015 Remi Collet <remi@fedoraproject.org> - 0.90.1-1
- update to 0.90.1

* Thu Oct  8 2015 Remi Collet <remi@fedoraproject.org> - 0.90-1
- update to 0.90

* Wed Sep 16 2015 Remi Collet <remi@fedoraproject.org> - 0.85.5-1
- update to 0.85.5
  https://github.com/glpi-project/glpi/issues?q=milestone:0.85.5
- use system ircmaxell/password-compat
- switch from eZ component to Zeta component

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.85.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May  4 2015 Remi Collet <remi@fedoraproject.org> - 0.85.4-1
- update to 0.85.4
  https://forge.indepnet.net/versions/1136

* Fri Apr 17 2015 Remi Collet <remi@fedoraproject.org> - 0.85.3-1
- update to 0.85.3
  https://forge.indepnet.net/versions/1118

* Fri Feb 27 2015 Remi Collet <remi@fedoraproject.org> - 0.85.2-2
- add security fix https://forge.indepnet.net/issues/5218
- add fix for temporary directory relocation

* Wed Jan 21 2015 Remi Collet <remi@fedoraproject.org> - 0.85.2-1
- update to 0.85.2
  https://forge.indepnet.net/versions/1110

* Mon Dec 22 2014 Remi Collet <remi@fedoraproject.org> - 0.85.1-1
- update to 0.85.1
  0.85   https://forge.indepnet.net/versions/539
  0.85.1 https://forge.indepnet.net/versions/1071
- drop dependency on pear/Cache_Lite
- add dependency on php-tcpdf
- increase system cron frequency and limit

* Mon Dec 22 2014 Remi Collet <remi@fedoraproject.org> - 0.84.8-3
- fix SQL Injection CVE-2014-9258

* Fri Nov  7 2014 Remi Collet <remi@fedoraproject.org> - 0.84.8-2
- use httpd_var_lib_t selinux context for /var/lib/glpi
- don't rely on system selinux policy in EPEL-7
- fix apache configuration when mod_php not enabled

* Fri Oct 17 2014 Remi Collet <remi@fedoraproject.org> - 0.84.8-1
- update to 0.84.8
  https://forge.indepnet.net/versions/1072

* Sun Oct  5 2014 Remi Collet <remi@fedoraproject.org> - 0.84.7-2
- provide nginx configuration (Fedora >= 21)
- rely on system SELinux policy (Fedora >= 20, EPEL-7)

* Fri Jul 11 2014 Remi Collet <remi@fedoraproject.org> - 0.84.7-1
- update to 0.84.7
  https://forge.indepnet.net/versions/1068

* Wed Jun 18 2014 Remi Collet <remi@fedoraproject.org> - 0.84.6-1
- update to 0.84.6
  https://forge.indepnet.net/versions/1028

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.84.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 26 2014 Remi Collet <remi@fedoraproject.org> - 0.84.5-1
- update to 0.84.5
  https://forge.indepnet.net/projects/glpi/versions/1011

* Wed Jan 22 2014 Remi Collet <remi@fedoraproject.org> - 0.84.4-1
- update to 0.84.4
  https://forge.indepnet.net/projects/glpi/versions/993

* Tue Jan 21 2014 Remi Collet <remi@fedoraproject.org> - 0.84.3-2
- fix SELinux context #1032995
  use httpd_sys_rw_content_t instead of httpd_sys_script_rw_t

* Sun Nov  3 2013 Remi Collet <remi@fedoraproject.org> - 0.84.3-1
- update to 0.84.3
  https://forge.indepnet.net/projects/glpi/versions/973

* Wed Oct  2 2013 Remi Collet <remi@fedoraproject.org> - 0.84.2-1
- update to 0.84.2
- add upstream patch for Zend autoload
- use system ZendFramework2 and SimplePie

* Thu Sep 12 2013 Remi Collet <remi@fedoraproject.org> - 0.83.9.1-4
- restrict access for install to local for security

* Fri Aug 23 2013 Remi Collet <remi@fedoraproject.org> - 0.83.9.1-3
- drop bundled Flash files files, #1000251

* Sat Jul 27 2013 Jóhann B. Guðmundsson <johannbg@fedoraproject.org> - 0.83.9.1-2
- Add a missing requirement on crontabs to spec file

* Tue Jun 25 2013 Remi Collet <remi@fedoraproject.org> - 0.83.9.1-1
- version 0.83.91 released (security)
  https://forge.indepnet.net/versions/show/928

* Thu Jun 20 2013 Remi Collet <remi@fedoraproject.org> - 0.83.9-1
- version 0.83.9 released (security and bugfix)
  https://forge.indepnet.net/projects/glpi/versions/915

* Tue Apr  2 2013 Remi Collet <remi@fedoraproject.org> - 0.83.8-1
- version 0.83.8 released (bugfix)
  https://forge.indepnet.net/projects/glpi/versions/866

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.83.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec  4 2012 Remi Collet <remi@fedoraproject.org> - 0.83.7-1
- version 0.83.7 released (bugfix)
  https://forge.indepnet.net/projects/glpi/versions/843

* Tue Oct 16 2012 Remi Collet <remi@fedoraproject.org> - 0.83.6-1
- version 0.83.6 released (bugfix)
  https://forge.indepnet.net/projects/glpi/versions/841

* Tue Oct  9 2012 Remi Collet <remi@fedoraproject.org> - 0.83.5-1
- version 0.83.5 released (bugfix)
  https://forge.indepnet.net/projects/glpi/versions/800

* Fri Jul 27 2012 Remi Collet <remi@fedoraproject.org> - 0.83.4-1
- version 0.83.4 released (bugfix)
  https://forge.indepnet.net/projects/glpi/versions/777

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.83.3.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 Remi Collet <remi@fedoraproject.org> - 0.83.3.1-1
- version 0.83.3 released (bugfix + security)
  https://forge.indepnet.net/projects/glpi/versions/771
- new dependency on htmLawed

* Thu May 31 2012 Remi Collet <remi@fedoraproject.org> - 0.83.2-1
- version 0.83.2 released
  https://forge.indepnet.net/projects/glpi/versions/750

* Thu Apr 19 2012 Remi Collet <remi@fedoraproject.org> - 0.83.1-2
- fix cron patch

* Wed Apr 18 2012 Remi Collet <remi@fedoraproject.org> - 0.83.1-1
- version 0.83.1 released
  0.83.1 https://forge.indepnet.net/projects/glpi/versions/696
  0.83   https://forge.indepnet.net/projects/glpi/versions/538
- adapt config for httpd 2.4

* Thu Feb 09 2012 Remi Collet <remi@fedoraproject.org> - 0.80.7-1
- version 0.80.7 released (security)
  https://forge.indepnet.net/projects/glpi/versions/685

* Thu Jan 05 2012 Remi Collet <remi@fedoraproject.org> - 0.80.6.1-1
- version 0.80.61 released (bugfix)
  https://forge.indepnet.net/projects/glpi/versions/677

* Thu Jan 05 2012 Remi Collet <remi@fedoraproject.org> - 0.80.6-1
- version 0.80.6 released (bugfix)
  https://forge.indepnet.net/projects/glpi/versions/657
- add patch for https://forge.indepnet.net/issues/3299

* Wed Nov 30 2011 Remi Collet <remi@fedoraproject.org> - 0.80.5-1
- version 0.80.5 released (bugfix)
  0.80.5 https://forge.indepnet.net/projects/glpi/versions/643
  0.80.4 https://forge.indepnet.net/projects/glpi/versions/632
  0.80.3 https://forge.indepnet.net/projects/glpi/versions/621
  0.80.2 https://forge.indepnet.net/projects/glpi/versions/605
  0.80.1 https://forge.indepnet.net/projects/glpi/versions/575
  0.80   https://forge.indepnet.net/projects/glpi/versions/466
- increase cron run frequency (3 tasks each 3 minutes)

* Sun Jul 24 2011 Remi Collet <Fedora@FamilleCollet.com> - 0.78.5-3.svn14966
- use system EZC only if available (not in EL-5)

* Fri Jul 22 2011 Remi Collet <Fedora@FamilleCollet.com> - 0.78.5-2.svn14966
- bug and security fix from SVN.

* Sat Jun 11 2011 Remi Collet <Fedora@FamilleCollet.com> - 0.78.5-1
- version 0.78.5 released

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72.4-4.svn11497
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May 20 2010 Remi Collet <Fedora@FamilleCollet.com> - 0.72.4-3.svn11497
- use system phpCAS instead of bundled copy
- minor bug fixes from SVN

* Mon Mar 22 2010 Remi Collet <Fedora@FamilleCollet.com> - 0.72.4-2.svn11035
- update embedded phpCAS to 1.1.0RC7 (security fix - #575906)

* Tue Mar  2 2010 Remi Collet <Fedora@FamilleCollet.com> - 0.72.4-1
- update to 0.72.4

* Tue Oct 27 2009 Remi Collet <Fedora@FamilleCollet.com> - 0.72.3-1
- update to 0.72.3

* Wed Sep 09 2009 Remi Collet <Fedora@FamilleCollet.com> - 0.72.2.1-1
- update to 0.72.21

* Tue Aug 18 2009 Remi Collet <Fedora@FamilleCollet.com> - 0.72.1-1.svn8743
- update to 0.72.1 svn revision 8743
- use system PHPMailer
- now requires php > 5

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 02 2009 Remi Collet <Fedora@FamilleCollet.com> - 0.71.6-1
- update to 0.71.6 (Bugfix Release)

* Fri May 22 2009 Remi Collet <Fedora@FamilleCollet.com> - 0.71.5-4
- post 0.71.5 patches (7910=>8321)

* Sun Apr 26 2009 Remi Collet <Fedora@FamilleCollet.com> - 0.71.5-3
- post 0.71.5 patches (7910=>8236)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Remi Collet <Fedora@FamilleCollet.com> - 0.71.5-1
- update to 0.71.5 (Fix regression in 0.71.4)

* Mon Jan 26 2009 Remi Collet <Fedora@FamilleCollet.com> - 0.71.4-1
- update to 0.71.4 (Security Release)

* Sun Nov 30 2008 Remi Collet <Fedora@FamilleCollet.com> - 0.71.3-1
- update to 0.71.3 (bugfix release)

* Sun Sep 28 2008 Remi Collet <Fedora@FamilleCollet.com> - 0.71.2-1.el4.1
- Fix MySQL 4.1 compatibility issue

* Mon Sep 15 2008 Remi Collet <Fedora@FamilleCollet.com> - 0.71.2-1
- update to 0.71.2 bugfix

* Sat Aug 09 2008 Remi Collet <Fedora@FamilleCollet.com> - 0.71.1-2
- fix SElinux bug on install test (glpi-check.patch)
- add create option on logrotate conf

* Fri Aug 01 2008 Remi Collet <Fedora@FamilleCollet.com> - 0.71.1-1
- update to 0.71.1 bugfix
- use system cron
- increase memory_limit / max_execution_time for upgrade

* Fri Jul 11 2008 Remi Collet <Fedora@FamilleCollet.com> - 0.71-1
- update to 0.71 stable
- fix bug #452353 (selinux)

* Fri Apr 25 2008 Remi Collet <Fedora@FamilleCollet.com> - 0.70.2-3
- remplace module policy by simple semanage (#442706)

* Mon Jan 28 2008 Remi Collet <Fedora@FamilleCollet.com> - 0.70.2-2
- rebuild (fix sources tarball)

* Sun Jan 27 2008 Remi Collet <Fedora@FamilleCollet.com> - 0.70.2-1
- bugfixes update 

* Tue Jan 15 2008 Remi Collet <Fedora@FamilleCollet.com> - 0.70.1a-1
- update 

* Sun Jan 13 2008 Remi Collet <Fedora@FamilleCollet.com> - 0.70.1-2
- fix typo in lang files

* Sun Jan 13 2008 Remi Collet <Fedora@FamilleCollet.com> - 0.70.1-1
- update to 0.70.1 (0.70 + bugfixes)

* Thu Jan 03 2008 Remi Collet <Fedora@FamilleCollet.com> - 0.70-4
- Changeset 6226 + 6228
- disable SELinux in EL-5

* Sat Dec 29 2007 Remi Collet <Fedora@FamilleCollet.com> - 0.70-3
- Changeset 6191 + 6194 + 6196

* Fri Dec 28 2007 Remi Collet <Fedora@FamilleCollet.com> - 0.70-2
- Changeset 6190

* Fri Dec 21 2007 Remi Collet <Fedora@FamilleCollet.com> - 0.70-1
- 0.70 final

* Fri Nov 16 2007 Remi Collet <Fedora@FamilleCollet.com> - 0.70-0.4.rc3
- Release Candidate 3

* Thu Nov 01 2007 Remi Collet <Fedora@FamilleCollet.com> - 0.70-0.3.rc2
- correct source

* Thu Nov 01 2007 Remi Collet <Fedora@FamilleCollet.com> - 0.70-0.2.rc2
- Release Candidate 2

* Mon Oct 08 2007 Remi Collet <Fedora@FamilleCollet.com> - 0.70-0.2.rc1
- From review #322781 : fix Source0 and macros
- Requires php-domxml for EL4

* Sun Sep 30 2007 Remi Collet <Fedora@FamilleCollet.com> - 0.70-0.1.rc1
- GLPI Version 0.7-RC1
- initial SPEC for Fedora Review

* Thu May 03 2007 Remi Collet <RPMS@FamilleCollet.com> - 0.70-0.beta.20070503
- initial RPM

