Name:    twa
Version: 1.9.3
Release: 1%{?dist}
Summary: Tiny web auditor with strong opinions
License: MIT

URL:     https://github.com/trailofbits/twa
Source0: %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: sed

Requires: bash >= 4.0.0
Requires: curl
Requires: gawk
Requires: jq
Requires: nc
Requires: %{_bindir}/dig

Recommends: testssl


%description
%{name} is a website auditing tool that can be used to detect
HTTPS issues, missing security headers, information-leaking headers,
and other potential security headers.


%prep
%setup -q

# Fix shebang
sed -e 's|^#!/usr/bin/env bash$|#!%{_bindir}/bash|' -i twa

# Remove the bash version check
sed -e '/Expected GNU Bash 4.0 or later/d' -i twa

# Remove the "ensure dependency is installed" checks
sed -e '/^ensure installed .*/d' -i twa


%build
# Nothing to do here - this is a shell script


%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 -p twa    %{buildroot}%{_bindir}/
install -m 755 -p tscore %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 644 -p twa.1 %{buildroot}%{_mandir}/man1/


%files
%license LICENSE
%doc README.md
%{_bindir}/twa
%{_bindir}/tscore
%{_mandir}/man1/twa.*


%changelog
* Sun May 31 2020 Artur Iwicki <fedora@svgames.pl> - 1.9.3-1
- Update to latest upstream release

* Wed Apr 29 2020 Artur Iwicki <fedora@svgames.pl> - 1.9.2-1
- Update to latest upstream release
- Add a weak dependency on testssl

* Fri Apr 24 2020 Artur Iwicki <fedora@svgames.pl> - 1.9.1-1
- Update to latest upstream release

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 Artur Iwicki <fedora@svgames.pl> - 1.8.0-2
- Add missing dependency on /usr/bin/dig

* Sun Feb 17 2019 Artur Iwicki <fedora@svgames.pl> - 1.8.0-1
- Update to latest upstream release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Artur Iwicki <fedora@svgames.pl> - 1.7.1-1
- Update to latest upstream version

* Tue Nov 06 2018 Artur Iwicki <fedora@svgames.pl> - 1.6.2-1
- Update to latest upstream version

* Sat Oct 20 2018 Artur Iwicki <fedora@svgames.pl> - 1.6.0-1
- Update to latest upstream version
- Update upstream URL (repo owner change)

* Sat Oct 06 2018 Artur Iwicki <fedora@svgames.pl> - 1.5.1-1
- Update to latest upstream version

* Tue Sep 18 2018 Artur Iwicki <fedora@svgames.pl> - 1.3.1-1
- Update to latest upstream version
- Use "install -p" (preserve file timestamps)

* Sun Sep 16 2018 Artur Iwicki <fedora@svgames.pl> - 1.2.0-1
- Initial packaging
