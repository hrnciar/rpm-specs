# remirepo/fedora spec file for php-sensiolabs-security-checker
#
# Copyright (c) 2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    a576c01520d9761901f269c4934ba55448be4a54
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sensiolabs
%global gh_project   security-checker
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_name      %{gh_project}
# PSR-0 namespace
%global ns_vendor    SensioLabs
%global ns_project   Security

Name:           php-%{pk_vendor}-%{pk_name}
Version:        6.0.3
Release:        2%{?dist}
Summary:        A security checker for your composer.lock

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

# Fix autoloader path
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
# For check
BuildRequires:  php(language) >= 7.1.3
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-cli
BuildRequires: (php-composer(symfony/console)     >= 4.3   with php-composer(symfony/console)     < 6)
BuildRequires: (php-composer(symfony/http-client) >= 4.3   with php-composer(symfony/http-client) < 6)
BuildRequires: (php-composer(symfony/mime)        >= 4.3   with php-composer(symfony/mime)        < 6)

# From composer.json, "require": {
#        "php": ">=7.1.3",
#        "symfony/console": "^2.8|^3.4|^4.2|^5.0",
#        "symfony/http-client": "^4.3|^5.0",
#        "symfony/mime": "^4.3|^5.0",
#        "symfony/polyfill-ctype": "^1.11"
Requires:       php(language) >= 7.1.3
Requires:      (php-composer(symfony/console)     >= 4.3   with php-composer(symfony/console)     < 6)
Requires:      (php-composer(symfony/http-client) >= 4.3   with php-composer(symfony/http-client) < 6)
Requires:      (php-composer(symfony/mime)        >= 4.3   with php-composer(symfony/mime)        < 6)

# From phpcompatifo report for 5.0.3
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
The SensioLabs Security Checker is a command line tool that checks if your
application uses dependencies with known security vulnerabilities. It uses
the Security Check Web service and the Security Advisories Database.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch0 -p1 -b .rpm


%build
: Generate a simple autoloader
%{_bindir}/phpab -t fedora -o %{ns_vendor}/%{ns_project}/autoload.php %{ns_vendor}/%{ns_project}

cat << 'EOF' | tee -a %{ns_vendor}/%{ns_project}/autoload.php
\Fedora\Autoloader\Dependencies::required([
    [
        '%{_datadir}/php/Symfony5/Component/Console/autoload.php',
        '%{_datadir}/php/Symfony4/Component/Console/autoload.php',
    ],
    [
        '%{_datadir}/php/Symfony5/Component/HttpClient/autoload.php',
        '%{_datadir}/php/Symfony4/Component/HttpClient/autoload.php',
    ],
    [
        '%{_datadir}/php/Symfony5/Component/Mime/autoload.php',
        '%{_datadir}/php/Symfony4/Component/Mime/autoload.php',
    ],
]);
EOF


%install
mkdir -p            %{buildroot}%{_datadir}/php
cp -pr %{ns_vendor} %{buildroot}%{_datadir}/php/%{ns_vendor}

install -Dpm 755 security-checker %{buildroot}%{_bindir}/%{name}


%check
: Ensure our autoloader is ok.
sed -e 's:%{_datadir}:%{buildroot}%{_datadir}:' security-checker >test
%{_bindir}/php test --version


%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}
%{_bindir}/%{name}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Remi Collet <remi@remirepo.net> - 6.0.3-1
- update to 6.0.3
- raise dependency on PHP 7.1
- raise dependency on Symfony version 4.3 and allow version 5
- drop dependency on composer/ca-bundle

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan  3 2019 Remi Collet <remi@remirepo.net> - 5.0.3-1
- initial package, version 5.0.3
