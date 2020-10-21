%global commit0 c98f06d942970cdf35dd66ab46840f7d6d567b60
%global date0   20190728
%global scommit %(c=%{commit0}; echo ${c:0:7} )

Name:           ocproxy
Version:        1.60
Release:        3.%{date0}git%{scommit}%{?dist}
Summary:        OpenConnect Proxy

# BSD for both ocproxy and bundled lwip
License:        BSD
URL:            https://github.com/cernekee/%{name}
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{name}-%{scommit}.tar.gz
# PR#11 rebased:
# use latest lwip sources, fix gcc warnings
# drop useless files copied accidently from lwip project
Patch0:         %{name}-1.60-with-lwip-2.1.2.patch

BuildRequires:  automake make gcc
BuildRequires:  libevent-devel

Provides:       bundled(lwip) = 2.1.2
Requires:       openconnect

%description
OCProxy is a user-level SOCKS and port forwarding proxy for OpenConnect based
on lwIP. When using ocproxy, OpenConnect only handles network activity that 
the user specifically asks to proxy, so the VPN interface no longer "hijacks" 
all network traffic on the host.

%prep
%autosetup -p1 -n%{name}-%{commit0}
./autogen.sh


%build
%configure --enable-vpnns
%make_build


%install
%make_install


%files
%license LICENSE
%doc %{_docdir}/%{name}/
%{_bindir}/%{name}
%{_bindir}/vpnns
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/vpnns.1*



%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-3.20190728gitc98f06d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-2.20190728gitc98f06d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Raphael Groner <projects.rg@smart.ms> - 1.60-1.20190728gitc98f06d
- initial
- use latest lwip sources, pull request #11
