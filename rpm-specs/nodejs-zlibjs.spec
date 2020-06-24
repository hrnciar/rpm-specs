%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%if 0%{?fedora} || 0%{?rhel} >= 7
%global installdir  %{_jsdir}/zlib
%else
%global installdir  %{_datadir}/javascript/zlib
%endif

Name:            nodejs-zlibjs
Version:         0.3.1
Release:         1%{?dist}
Summary:         JavaScript library reimplementing compression, made available for Node.js

License:         MIT
URL:             https://github.com/imaya/zlib.js
Source0:         http://registry.npmjs.org/zlibjs/-/zlibjs-%{version}.tgz

BuildArch:       noarch
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:   nodejs-packaging

%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:   web-assets-devel
Requires:        web-assets-filesystem
%endif

%if 0%{?enable_tests}
BuildRequires:   npm(buster)
%endif

Requires:        js-zlib = %{version}

%description
This module allows zlib.js to be used by other Node.js modules.

zlib.js is ZLIB(RFC1950), DEFLATE(RFC1951), GZIP(RFC1952), and
PKZIP implementation in JavaScript. This library can be used to
perform compression and decompression in the browser.

%prep
%setup -q -n package
# Remove bundled and pre-built files.
rm -rf bin/* vendor/

%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/zlibjs
cp -pr package.json \
    %{buildroot}%{nodejs_sitelib}/zlibjs

# link to file provided by js-zlib package
mkdir -p %{buildroot}%{nodejs_sitelib}/zlibjs/bin
ln -sf %{installdir}/node-zlib.js \
    %{buildroot}%{nodejs_sitelib}/zlibjs/bin/node-zlib.js

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/buster-test
%endif

%files
%license LICENSE
%doc ChangeLog.md README.md README.en.md
%{nodejs_sitelib}/zlibjs

%changelog
* Mon Jun 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-1
- Update to latest upstream release 0.3.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 17 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.0-1
- initial package
