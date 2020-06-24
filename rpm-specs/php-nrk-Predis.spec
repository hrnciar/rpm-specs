# remirepo/fedora spec file for php-nrk-Predis
#
# Copyright (c) 2013-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear: %global __pear %{_bindir}/pear}
%global pear_name    Predis
%global pear_channel pear.nrk.io

%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7
%global with_tests   0%{!?_without_tests:1}
%else
%global with_tests   0%{?_with_tests:1}
%endif

Name:           php-nrk-Predis
Version:        1.1.1
Release:        9%{?dist}
Summary:        PHP client library for Redis

License:        MIT
URL:            http://%{pear_channel}
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

# https://github.com/nrk/predis/pull/393
Patch0:         %{name}-pr393.patch
# https://github.com/nrk/predis/pull/486
Patch1:         %{name}-pr486.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.9
BuildRequires:  php-pear(PEAR)
BuildRequires:  php-channel(%{pear_channel})
%if %{with_tests}
BuildRequires:  php-phpunit-PHPUnit
BuildRequires:  redis > 2.8
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.3.9
Requires:       php-reflection
Requires:       php-curl
Requires:       php-filter
Requires:       php-pcre
Requires:       php-session
Requires:       php-sockets
Requires:       php-spl
Requires:       php-pear(PEAR)
Requires:       php-channel(%{pear_channel})

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(predis/predis) = %{version}


%description
Flexible and feature-complete PHP client library for Redis.


%prep
%setup -q -c

cd %{pear_name}-%{version}
%patch0 -p1
%patch1 -p1
sed -e '/test/s/md5sum="[^"]*"//' ../package.xml >%{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}

# Relocate PATH so test suite can be run from install dir
sed -e 's:tests/::' \
    %{buildroot}%{pear_testdir}/%{pear_name}/phpunit.xml.dist \
  > %{buildroot}%{pear_testdir}/%{pear_name}/phpunit.xml


%check
%if %{with_tests}
: Launch redis server
port=6379
pidfile=$PWD/redis.pid
mkdir -p data
redis-server                   \
    --bind      127.0.0.1      \
    --port      $port          \
    --daemonize yes            \
    --logfile   $PWD/redis.log \
    --dir       $PWD/data      \
    --pidfile   $pidfile

: Run the installed test Suite against the installed library
pushd %{buildroot}%{pear_testdir}/%{pear_name}

ret=0
php -d memory_limit=1G %{_bindir}/phpunit \
    --include-path=%{buildroot}%{pear_phpdir} \
    --verbose || ret=1
popd

: Cleanup
if [ -f $pidfile ]; then
   kill $(cat $pidfile)
fi

exit $ret
%else
: Test disabled
%endif


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/%{pear_name}
%{pear_testdir}/%{pear_name}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Remi Collet <remi@remirepo.net> - 1.1.1-5
- fix FTBFS from Koschei with patch from
  https://github.com/nrk/predis/pull/486

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 17 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-2
- fix bootstraping to redis server for test suite
- add patch for PHP 7.1
- open https://github.com/nrk/predis/pull/393

* Fri Jun 17 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Tue Jun 07 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Tue May 31 2016 Remi Collet <remi@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Remi Collet <remi@fedoraproject.org> - 1.0.3-2
- fix FTBFS detected by Koschei since redis 3.0.6
  open https://github.com/nrk/predis/pull/296

* Fri Jul 31 2015 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Thu Jul 30 2015 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 02 2015 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Fri Nov 07 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- (re)enable test suite with redis 2.8.x
- add upstream patch for test suite on 32bits

* Mon Nov 03 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0
- upstream patch for tests
- open https://github.com/nrk/predis/issues/220 - failed tests
  on slow / 32bits computer

* Wed Jul 16 2014 Remi Collet <remi@fedoraproject.org> - 0.8.6-1
- Update to 0.8.6
- provides php-composer(predis/predis)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 16 2014 Remi Collet <remi@fedoraproject.org> - 0.8.5-1
- Update to 0.8.5 (stable)
- don't run tests (need latest redis server)

* Sun Jul 28 2013 Remi Collet <remi@fedoraproject.org> - 0.8.4-1
- Update to 0.8.4

* Wed Jul  3 2013 Remi Collet <remi@fedoraproject.org> - 0.8.3-2
- fixed sources, https://github.com/nrk/predis/issues/125

* Wed Jun  5 2013 Remi Collet <remi@fedoraproject.org> - 0.8.3-1
- initial package
