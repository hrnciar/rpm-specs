# %%global pkg_suffix -1

Name:    testssl
Version: 3.0.2
Release: 1%{?dist}

Summary: Testing TLS/SSL encryption
License: GPLv2
URL:     https://testssl.sh/
Source0: https://github.com/drwetter/%{name}.sh/archive/%{version}%{?pkg_suffix}.tar.gz#/%{name}-%{version}%{?pkg_suffix}.tar.gz

BuildArch: noarch

BuildRequires: coreutils
BuildRequires: sed

Requires: bash
# dig, host, nslookup
Requires: bind-utils
# /etc/pki/tls
Requires: ca-certificates
Requires: coreutils
Requires: gawk
# locale
Requires: glibc-common
Requires: grep
Requires: hostname
# tput
Requires: ncurses
Requires: openssl >= 1
# ps
Requires: procps-ng
Requires: sed
# hexdump, kill
Requires: util-linux

%description
testssl.sh is a free command line tool which checks a server's service on any
port for the support of TLS/SSL ciphers, protocols as well as recent
cryptographic flaws and more.

%prep
%autosetup -n %{name}.sh-%{version}%{?pkg_suffix}
sed --in-place '1s#^\#!/usr/bin/env bash$#\#!/bin/bash#' %{name}.sh etc/client-simulation.txt
sed --in-place 's#^TESTSSL_INSTALL_DIR=.*$#TESTSSL_INSTALL_DIR="%{_datadir}/%{name}"#' %{name}.sh
sed --in-place 's#^CA_BUNDLES_PATH=.*$#CA_BUNDLES_PATH="/etc/pki/tls"#' %{name}.sh
sed --in-place '0,/.SH "COPYRIGHT"/s#testssl\\.sh#testssl#g' doc/%{name}.1

%build

%install
install -D --preserve-timestamps %{name}.sh %{buildroot}%{_bindir}/%{name}

for file in ca_hashes.txt cipher-mapping.txt client-simulation.txt common-primes.txt tls_data.txt README.md
do
        install -D --preserve-timestamps --mode=0644 etc/${file} %{buildroot}%{_datadir}/%{name}/etc/${file}
done

install -d %{buildroot}%{_mandir}/man1
install -m 644 doc/%{name}.1 %{buildroot}%{_mandir}/man1/

%files
%doc CHANGELOG.md Readme.md
%license LICENSE
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/testssl.1*

%changelog
* Sat May 09 2020 Christian Krause <chkr@fedoraproject.org> - 3.0.2-1
- Updated to 3.0.2 (BZ #1750167)
- Updated installed documentation files
- Added provided man page (adjusted to Fedora's script name "testssl")

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 25 2017 Michael Kuhn <suraia@fedoraproject.org> - 2.9.5-1
- Update to 2.9.5

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 13 2017 Michael Kuhn <suraia@fedoraproject.org> - 2.8-1
- Update to 2.8

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-0.2.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Michael Kuhn <suraia@fedoraproject.org> - 2.8-0.1.rc3
- Update to 2.8rc3.

* Wed Feb 24 2016 Michael Kuhn <suraia@fedoraproject.org> - 2.6-3
- Add BuildRequires for coreutils.
- Fix shebang.
- Install openssl-rfc.mappping.html.

* Tue Feb 23 2016 Michael Kuhn <suraia@fedoraproject.org> - 2.6-2
- Require OpenSSL >= 1.
- Add Requires for miscellaneous utilities.
- Install mapping-rfc.txt.

* Thu Feb 18 2016 Michael Kuhn <suraia@fedoraproject.org> - 2.6-1
- Initial package.
