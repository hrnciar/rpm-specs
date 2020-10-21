Summary: Transparent and scalable SSL/TLS interception
Name: sslsplit
Version: 0.5.5
Release: 4%{?dist}
License: BSD
Url: http://www.roe.ch/SSLsplit
Source: http://mirror.roe.ch/rel/sslsplit/sslsplit-%{version}.tar.bz2
Buildrequires: libevent-devel, openssl-devel, check-devel gcc
Buildrequires: libpcap-devel libnet-devel
Requires: iptables, iproute

%description
SSLsplit is a tool for man-in-the-middle attacks against SSL/TLS encrypted
network connections. Connections are transparently intercepted through a
network address translation engine and redirected to SSLsplit. SSLsplit
terminates SSL/TLS and initiates a new SSL/TLS connection to the original
destination address, while logging all data transmitted. SSLsplit is
intended to be useful for network forensics and penetration testing.

It uses Linux netfilter REDIRECT and TPROXY

%prep
%setup -q

%build
# work around some odd build system option passing
export CFLAGS="%{optflags}"
export DEBUG_CFLAGS="%{optflags}"
make %{?_smp_mflags}

%check
# Requires a network connection
# make test

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1/
cp -a %{name} %{buildroot}%{_bindir}
cp -a %{name}.1  %{buildroot}%{_mandir}/man1/

%files
%attr(0755,root,root) %{_bindir}/%{name}
%doc *.md
%{_mandir}/*/*

%changelog
* Tue Sep 29 20:45:00 CEST 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.5-4
- Rebuilt for libevent 2.1.12

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Paul Wouters <pwouters@redhat.com> - 0.5.5-1
- Resolves: rhbz#1534305 sslsplit-0.5.5 is available
- Enables ecc test

* Thu Aug 22 2019 Paul Wouters <pwouters@redhat.com> - 0.5.4-1
- Resolves: rhbz#1744466 Please update it to 0.5.4

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Patrick Uiterwijk <patrick@puiterwijk.org> - 0.5.2-1
- Rebase to 0.5.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 29 2016 Paul Wouters <pwouters@redhat.com> - 0.5.0-1
- Updated to 0.5.0 (rhbz#1202176)
- Include all *.md files as documentation
- Updated upstream source link

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 29 2014 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.4.8-1
- Rebase to upstream 0.4.8

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 0.4.5-1
- Rebase to upstream 0.4.5
- Switched to usage of Github download links

* Mon Jul 30 2012 Paul Wouters <pwouters@redhat.com> - 0.4.4-4
- Disable make test, as it requires a network connection

* Sat Jul 28 2012 Paul Wouters <pwouters@redhat.com> - 0.4.4-3
- Fix permission of binary to 755

* Fri Jul 27 2012 Paul Wouters <pwouters@redhat.com> - 0.4.4-2
- Fix missing buildrequire for check-devel
- Run make check
- No need to compress man pages
- No mixing of macro styles

* Mon May 28 2012 Paul Wouters <pwouters@redhat.com> - 0.4.4-1
- Initial package
