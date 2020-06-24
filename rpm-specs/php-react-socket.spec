#
# Fedora spec file for php-react-socket
#
# Copyright (c) 2017-2019 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     reactphp
%global github_name      socket
%global github_version   1.3.0
%global github_commit    10f0629ec83ea0fa22597f348623f554227e3ca0

%global composer_vendor  react
%global composer_project socket

# "php": ">=5.3.0"
%global php_min_ver 5.3.0
# "clue/block-react": "^1.2"
%global clue_block_react_min_ver 1.2
%global clue_block_react_max_ver 2.0
# "evenement/evenement": "^3.0 || ^2.0 || ^1.0"
%global evenement_min_ver 1.0
%global evenement_max_ver 4.0
# "react/dns": "^1.0 || ^0.4.13"
%global react_dns_min_ver 0.4.13
%global react_dns_max_ver 2.0
# "react/event-loop": "^1.0 || ^0.5 || ^0.4 || ^0.3.5"
%global react_event_loop_min_ver 0.3.5
%global react_event_loop_max_ver 2.0
# "react/promise": "^2.6.0 || ^1.2.1"
%global react_promise_min_ver 1.2.1
%global react_promise_max_ver 3.0
# "react/promise-timer": "^1.4.0"
%global react_promise_timer_min_ver 1.4.0
%global react_promise_timer_max_ver 2.0
# "react/stream": "^1.1"
%global react_stream_min_ver 1.1
%global react_stream_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       2%{?github_release}%{?dist}
Summary:       Async, streaming plaintext TCP/IP and secure TLS socket server

License:       MIT
URL:           https://reactphp.org/socket/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

# Improve test suite to exclude TLS 1.3 tests on PHP 7.3
# https://github.com/reactphp/socket/commit/198690e6b736d3501cf272fa9e4ed59f3ee08a34
# https://github.com/reactphp/socket/commit/198690e6b736d3501cf272fa9e4ed59f3ee08a34.patch
Patch0:        %{name}.198690e.patch

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit6
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(clue/block-react) >= %{clue_block_react_min_ver} with php-composer(clue/block-react) < %{clue_block_react_max_ver})
BuildRequires: (php-composer(evenement/evenement) >= %{evenement_min_ver} with php-composer(evenement/evenement) < %{evenement_max_ver})
BuildRequires: (php-composer(react/dns) >= %{react_dns_min_ver} with php-composer(react/dns) < %{react_dns_max_ver})
BuildRequires: (php-composer(react/event-loop) >= %{react_event_loop_min_ver} with php-composer(react/event-loop) < %{react_event_loop_max_ver})
BuildRequires: (php-composer(react/promise) >= %{react_promise_min_ver} with php-composer(react/promise) < %{react_promise_max_ver})
BuildRequires: (php-composer(react/promise-timer) >= %{react_promise_timer_min_ver} with php-composer(react/promise-timer) < %{react_promise_timer_max_ver})
BuildRequires: (php-composer(react/stream) >= %{react_stream_min_ver} with php-composer(react/stream) < %{react_stream_max_ver})
%else
BuildRequires: php-composer(clue/block-react) <  %{clue_block_react_max_ver}
BuildRequires: php-composer(clue/block-react) >= %{clue_block_react_min_ver}
BuildRequires: php-composer(evenement/evenement) <  %{evenement_max_ver}
BuildRequires: php-composer(evenement/evenement) >= %{evenement_min_ver}
BuildRequires: php-composer(react/dns) >= %{react_dns_min_ver}
BuildRequires: php-composer(react/dns) <  %{react_dns_max_ver}
BuildRequires: php-composer(react/event-loop) <  %{react_event_loop_max_ver}
BuildRequires: php-composer(react/event-loop) >= %{react_event_loop_min_ver}
BuildRequires: php-composer(react/promise) <  %{react_promise_max_ver}
BuildRequires: php-composer(react/promise) >= %{react_promise_min_ver}
BuildRequires: php-composer(react/promise-timer) >= %{react_promise_timer_min_ver}
BuildRequires: php-composer(react/promise-timer) <  %{react_promise_timer_max_ver}
BuildRequires: php-composer(react/stream) <  %{react_stream_max_ver}
BuildRequires: php-composer(react/stream) >= %{react_stream_min_ver}
%endif
## phpcompatinfo (computed from version 1.3.0)
BuildRequires: php-filter
BuildRequires: php-openssl
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-sockets
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(evenement/evenement) >= %{evenement_min_ver} with php-composer(evenement/evenement) < %{evenement_max_ver})
Requires:      (php-composer(react/dns) >= %{react_dns_min_ver} with php-composer(react/dns) < %{react_dns_max_ver})
Requires:      (php-composer(react/event-loop) >= %{react_event_loop_min_ver} with php-composer(react/event-loop) < %{react_event_loop_max_ver})
Requires:      (php-composer(react/promise) >= %{react_promise_min_ver} with php-composer(react/promise) < %{react_promise_max_ver})
Requires:      (php-composer(react/promise-timer) >= %{react_promise_timer_min_ver} with php-composer(react/promise-timer) < %{react_promise_timer_max_ver})
Requires:      (php-composer(react/stream) >= %{react_stream_min_ver} with php-composer(react/stream) < %{react_stream_max_ver})
%else
Requires:      php-composer(evenement/evenement) <  %{evenement_max_ver}
Requires:      php-composer(evenement/evenement) >= %{evenement_min_ver}
Requires:      php-composer(react/event-loop) <  %{react_event_loop_max_ver}
Requires:      php-composer(react/event-loop) >= %{react_event_loop_min_ver}
Requires:      php-composer(react/dns) <  %{react_dns_max_ver}
Requires:      php-composer(react/dns) >= %{react_dns_min_ver}
Requires:      php-composer(react/promise) <  %{react_promise_max_ver}
Requires:      php-composer(react/promise) >= %{react_promise_min_ver}
Requires:      php-composer(react/promise-timer) >= %{react_promise_timer_min_ver}
Requires:      php-composer(react/promise-timer) <  %{react_promise_timer_max_ver}
Requires:      php-composer(react/stream) <  %{react_stream_max_ver}
Requires:      php-composer(react/stream) >= %{react_stream_min_ver}
%endif
# phpcompatinfo (computed from version 1.3.0)
Requires:      php-filter
Requires:      php-pcre
Requires:      php-sockets
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Packages have been merged (not provided as class names are different)
Obsoletes:     php-react-socket-client < 0.5

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Async, streaming plaintext TCP/IP and secure TLS socket server for React PHP.

The socket component provides a more usable interface for a socket-layer server
based on the EventLoop and Stream components.

Autoloader: %{phpdir}/React/Socket/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

# Improve test suite to exclude TLS 1.3 tests on PHP 7.3
%patch0 -p1


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('React\\Socket\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Evenement/autoload.php',
    '%{phpdir}/React/Dns/autoload.php',
    '%{phpdir}/React/EventLoop/autoload.php',
    '%{phpdir}/React/Promise/autoload.php',
    '%{phpdir}/React/Promise/Timer/autoload.php',
    '%{phpdir}/React/Stream/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/React
cp -rp src %{buildroot}%{phpdir}/React/Socket


%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/React/Socket/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('React\\Tests\\Socket\\\\', __DIR__.'/tests');

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Clue/React/Block/autoload.php',
));
BOOTSTRAP

: Skip test requiring network access
rm -f tests/IntegrationTest.php

: Skip "Class "React\Dns\Resolver\Resolver" is declared "final" and cannot be mocked" warnings
: Why is PHPUnit 6 failing the test run for this even if convertWarningsToExceptions="false"?
rm -f tests/DnsConnectorTest.php
sed \
    -e 's/function testConnectorUsesGivenResolverInstance/function SKIP_testConnectorUsesGivenResolverInstance/' \
    -e 's/function testConnectorUsesResolvedHostnameIfDnsIsUsed/function SKIP_testConnectorUsesResolvedHostnameIfDnsIsUsed/' \
    -i tests/ConnectorTest.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit6)
for PHP_EXEC in "" %{?rhel:php54 php55} php70 php71 php72 php73 php74; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/React/Socket


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Shawn Iwinski <shawn@iwin.ski> - 1.3.0-1
- Update to 1.3.0 (RHBZ #1600308)
- Use PHPUnit 6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Remi Collet <remi@remirepo.net> - 0.8.12-3
- obsolete php-react-socket-client (merged)

* Tue Jul  3 2018 Remi Collet <remi@remirepo.net> - 0.8.12-2
- add missing dependency on react/dns

* Mon Jul 02 2018 Shawn Iwinski <shawn@iwin.ski> - 0.8.12-1
- Update to 0.8.12 (RHBZ #1422067)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8
- Add composer.json to repo

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.6-1
- Update to 0.4.6 (RHBZ #1416802)

* Tue Jan 24 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.5-2
- Restrict evenement/evenement and react/promise dependencies to one major version
- Minor update to SCL tests (only php54 and php55 if rhel)

* Tue Jan 17 2017 Shawn Iwinski <shawn@iwin.ski> - 0.4.5-1
- Initial package
