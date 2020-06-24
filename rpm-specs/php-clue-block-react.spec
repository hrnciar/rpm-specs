#
# Fedora spec file for php-clue-block-react
#
# Copyright (c) 2017-2019 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     clue
%global github_name      reactphp-block
%global github_version   1.3.1
%global github_commit    2f516b28259c203d67c4c963772dd7e9db652737

%global composer_vendor  clue
%global composer_project block-react

# "php": ">=5.3"
%global php_min_ver 5.3
# "react/event-loop": "^1.0 || ^0.5 || ^0.4 || ^0.3.5"
%global react_event_loop_min_ver 0.3.5
%global react_event_loop_max_ver 2.0
# "react/promise": "^2.7 || ^1.2.1"
%global react_promise_min_ver 1.2.1
%global react_promise_max_ver 3.0
# "react/promise-timer": "^1.5"
%global react_promise_timer_min_ver 1.5
%global react_promise_timer_max_ver 2.0

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       4%{?github_release}%{?dist}
Summary:       Integrate async React PHP components into your blocking environment

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit6
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(react/event-loop) >= %{react_event_loop_min_ver} with php-composer(react/event-loop) < %{react_event_loop_max_ver})
BuildRequires: (php-composer(react/promise-timer) >= %{react_promise_timer_min_ver} with php-composer(react/promise-timer) < %{react_promise_timer_max_ver})
BuildRequires: (php-composer(react/promise) >= %{react_promise_min_ver} with php-composer(react/promise) < %{react_promise_max_ver})
%else
BuildRequires: php-composer(react/event-loop) <  %{react_event_loop_max_ver}
BuildRequires: php-composer(react/event-loop) >= %{react_event_loop_min_ver}
BuildRequires: php-composer(react/promise-timer) <  %{react_promise_timer_max_ver}
BuildRequires: php-composer(react/promise-timer) >= %{react_promise_timer_min_ver}
BuildRequires: php-composer(react/promise) <  %{react_promise_max_ver}
BuildRequires: php-composer(react/promise) >= %{react_promise_min_ver}
%endif
## phpcompatinfo (computed from version 1.3.0)
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(react/event-loop) >= %{react_event_loop_min_ver} with php-composer(react/event-loop) < %{react_event_loop_max_ver})
Requires:      (php-composer(react/promise-timer) >= %{react_promise_timer_min_ver} with php-composer(react/promise-timer) < %{react_promise_timer_max_ver})
Requires:      (php-composer(react/promise) >= %{react_promise_min_ver} with php-composer(react/promise) < %{react_promise_max_ver})
%else
Requires:      php-composer(react/event-loop) <  %{react_event_loop_max_ver}
Requires:      php-composer(react/event-loop) >= %{react_event_loop_min_ver}
Requires:      php-composer(react/promise-timer) <  %{react_promise_timer_max_ver}
Requires:      php-composer(react/promise-timer) >= %{react_promise_timer_min_ver}
Requires:      php-composer(react/promise) <  %{react_promise_max_ver}
Requires:      php-composer(react/promise) >= %{react_promise_min_ver}
%endif
# phpcompatinfo (computed from version 1.3.0)
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Lightweight library that eases integrating async components built for
React PHP [1] in a traditional, blocking environment.

Autoloader: %{phpdir}/Clue/React/Block/autoload.php

[1] http://reactphp.org/


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Dependencies::required(array(
    __DIR__.'/functions_include.php',
    '%{phpdir}/React/EventLoop/autoload.php',
    '%{phpdir}/React/Promise/autoload.php',
    '%{phpdir}/React/Promise/Timer/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/Clue/React
cp -rp src %{buildroot}%{phpdir}/Clue/React/Block


%check
%if %{with_tests}
: Mock Composer autoloader
mkdir vendor
ln -s %{buildroot}%{phpdir}/Clue/React/Block/autoload.php vendor/autoload.php

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit6)
for PHP_EXEC in "" %{?rhel:php54 php55} php70 php71 php72 php73 php74; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose \
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
%dir %{phpdir}/Clue
%dir %{phpdir}/Clue/React
     %{phpdir}/Clue/React/Block


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Shawn Iwinski <shawn@iwin.ski> - 1.3.1-3
- Use PHPUnit 6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Shawn Iwinski <shawn@iwin.ski> - 1.3.1-1
- Update to 1.3.1 (RHBZ #1697987)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Shawn Iwinski <shawn@iwin.ski> - 1.3.0-1
- Update to 1.3.0 (RHBZ #1591266)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8
- Add composer.json to repo

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-2
- Add missing BuildRequires and Requires
- Retrict react/promise dependency to one major version
- Minor update to SCL tests (only php54 and php55 if rhel)

* Tue Jan 17 2017 Shawn Iwinski <shawn@iwin.ski> - 1.1.0-1
- Initial package
