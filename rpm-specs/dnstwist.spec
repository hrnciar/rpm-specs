Name: dnstwist
Summary: Domain name permutation engine
License: ASL 2.0

Version: 20200916
Release: 1%{?dist}

URL:     https://github.com/elceef/%{name}/
Source0: %{url}archive/%{version}/%{name}-%{version}.tar.gz

# Remove all "are we on MS Windows?" checks
Patch0: dnstwist--no-win32-check.patch
# Remove all "is this Python import present?" checks
Patch1: dnstwist--modules-always-present.patch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildArch: noarch

Requires: GeoIP-GeoLite-data >= 2016.09
Requires: python3-GeoIP >= 1.3.2
Requires: python3-dns >= 1.14.0
Requires: python3-requests >= 2.20.0
Requires: python3-ssdeep >= 3.1.1
Requires: python3-tld >= 0.9.1
Requires: python3-whois >= 0.7

%{?python_enable_dependency_generator}


%description
See what sort of trouble users can get in trying to type your domain name.
Find similar-looking domains that adversaries can use to attack you.
Detect typosquatters, phishing attacks, fraud and corporate espionage.
Useful as an additional source of targeted threat intelligence.


%prep
%autosetup -p1


%build
# Nothing to do here


%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 -p %{name}.py  %{buildroot}%{_bindir}/%{name}

install -m 755 -d %{buildroot}%{_datadir}/%{name}
cp -a dictionaries/ %{buildroot}%{_datadir}/%{name}/

install -m 755 -d %{buildroot}%{_mandir}/man1/
install -m 644 -p docs/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1


%files
%doc docs/README.md docs/THANKS.md
%license docs/LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*


%changelog
* Fri Sep 18 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20200916-1
- Update to latest upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200707-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Artur Iwicki <fedora@svgames.pl> - 20200707-1
- Update to latest upstream release

* Thu Jun 25 2020 Artur Iwicki <fedora@svgames.pl> - 20200521-2
- Add an explicit BuildRequires on python3-setuptools

* Fri May 22 2020 Artur Iwicki <fedora@svgames.pl> - 20200521-1
- Update to latest upstream release

* Wed Apr 29 2020 Artur Iwicki <fedora@svgames.pl> - 20200429-1
- Update to latest upstream release
- Drop Source101 (man page - merged upstream)

* Sun Mar 22 2020 Artur Iwicki <fedora@svgames.pl> - 20190706-3
- Remove the bundled GeoIP database,
  require the GeoIP-GeoLite-data package instead

* Thu Mar 05 2020 Artur Iwicki <fedora@svgames.pl> - 20190706-2
- Add a man page
- Preserve timestamps during %%install

* Sun Dec 22 2019 Artur Iwicki <fedora@svgames.pl> - 20190706-1
- Initial packaging
