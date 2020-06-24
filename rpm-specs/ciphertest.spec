Name:           ciphertest
Version:        0.2.2
Release:        8%{?dist}
Summary:        An SSL cipher checker

License:        GPLv3+
URL:            https://github.com/OpenSecurityResearch/ciphertest
Source0:        https://github.com/OpenSecurityResearch/ciphertest/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       gnutls-utils%{?_isa}
Requires:       openssl%{?_isa}
Requires:       bash%{?_isa}

%description
cipherTest.sh is an SSL cipher checker in that it uses gnutls, which has
support for many more configurations than openssl. It tests potentially 
~3,200 different configurations but does some pre-optimization so that
it minimizes "failed" checks.

%prep
%setup -q
find -name '*.sh' | xargs sed -i '1s|^#!/usr/bin/env bash|#!/bin/bash|'

%build
# nothing to build

%install
install -Dp -m 0755 cipherTest.sh %{buildroot}%{_bindir}/ciphertest

%files
%doc LICENSE README
%license COPYING 
%{_bindir}/%{name}

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 14 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.2-1
- Update to latest upstream version 0.2.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 29 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-2
- Fix Source0

* Wed Oct 29 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-1
- Initial package for Fedora
