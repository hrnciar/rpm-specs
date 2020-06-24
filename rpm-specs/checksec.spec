# Testsuite needs root-privileges.
%bcond_with     testsuite


Name:           checksec
Version:        2.2.2
Release:        1%{?dist}
Summary:        Tool to check system for binary-hardening

License:        BSD
URL:            https://github.com/slimm609/%{name}.sh
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

%if %{with testsuite}
BuildRequires:  binutils
BuildRequires:  file
BuildRequires:  findutils
BuildRequires:  gawk
BuildRequires:  libxml2
BuildRequires:  openssl
BuildRequires:  procps-ng
%if 0%{?fedora} || 0%{?rhel} >= 6
BuildRequires:  %{_bindir}/jsonlint
%endif
%endif

Requires:       binutils
Requires:       file
Requires:       findutils
Requires:       gawk
Requires:       which

%description
Modern Linux distributions offer some mitigation techniques to make it harder
to exploit software vulnerabilities reliably. Mitigations such as RELRO,
NoExecute (NX), Stack Canaries, Address Space Layout Randomization (ASLR) and
Position Independent Executables (PIE) have made reliably exploiting any
vulnerabilities that do exist far more challenging. The checksec script is
designed to test what *standard* Linux OS and PaX (http://pax.grsecurity.net/)
security features are being used.

As of version 1.3 the script also lists the status of various Linux kernel
protection mechanisms.

%{name} can check binary-files and running processes for hardening features.


%prep
%autosetup -n %{name}.sh-%{version} -p 1

# Fix shebang.
sed -i 's~^#!/usr/bin/env bash~#!/bin/bash~' checksec

# Disable --update command.
sed -i 's/pkg_release=false/pkg_release=true/' checksec


%build
# noop


%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
install -pm 0755 %{name} %{buildroot}%{_bindir}
install -pm 0644 extras/man/%{name}.1 %{buildroot}%{_mandir}/man1


%if %{with testsuite}
%check
pushd tests
./xml-checks.sh || exit 2
%if 0%{?fedora} || 0%{?rhel} >= 6
./json-checks.sh || exit 2
%endif
popd
%endif


%files
%license LICENSE.txt
%doc ChangeLog README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Fri May 29 2020 Björn Esser <besser82@fedoraproject.org> - 2.2.2-1
- Release 2.2.2 (BZ#1840807)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Robin Lee <cheeselee@fedoraproject.org> - 2.1.0-1
- Release 2.1.0 (BZ#1742252)
- Use 'sed' instead of a patch to disable --update command

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 05 2019 Björn Esser <besser82@fedoraproject.org> - 1.11.1-1
- Update to 1.11.1 (BZ#1693841)
- Section of man-page was moved to man1
- Add patch to disable --update command
- Add patch to fix shebang
- De-tabbify spec file

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 27 2018 Robin Lee <cheeselee@fedoraproject.org> - 1.8.0-2
- Fix Linux 4.18 compitability (BZ#1632412)

* Sun Sep 23 2018 Robin Lee <cheeselee@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0 (BZ#1485319)

* Thu Aug 02 2018 Dan Horák <dan[at]danny.cz - 1.7.4-8
- which is Required

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 08 2017 Troy Dawson <tdawson@redhat.com> - 1.7.4-5
- Cleanup spec file conditionals

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 02 2016 Björn Esser <fedora@besser82.io> - 1.7.4-2
- Add manpage a Source1

* Sun Oct 02 2016 Björn Esser <fedora@besser82.io> - 1.7.4-1
- Update to forked version (rhbz 1240391)
- Added missing runtime-dependency on gawk (rhbz 1380950)

* Sun Oct 02 2016 Björn Esser <fedora@besser82.io> - 1.5-7
- Added missing runtime-dependencies (rhbz 1380950)
- Small improvements to spec-file
- Clean trailing whitespaces

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Björn Esser <bjoern.esser@gmail.com> - 1.5-2
- added stuff for el5-build

* Tue Jun 11 2013 Björn Esser <bjoern.esser@gmail.com> - 1.5-1
- Initial rpm release
