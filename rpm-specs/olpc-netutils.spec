Name:           olpc-netutils
Version:        0.8.2
Release:        17%{?dist}
Summary:        OLPC network utilities

License:        GPLv2+
URL:            http://wiki.laptop.org/go/Olpc-netutils
Source0:        http://dev.laptop.org/~martin/%{name}/%{name}-%{version}.tar.bz2
Patch0:         olpc-netutils-python3.patch

BuildArch:      noarch
ExclusiveArch:  %{ix86} %{arm}

Requires:       bash
Requires:       python3-dbus

Requires:       coreutils
Requires:       procps
Requires:       util-linux

Requires:       net-tools
Requires:       wireless-tools
Requires:       avahi-tools

Requires:       iputils
Requires:       iptables
Requires:       dnsmasq
Requires:       tcpdump

Requires:       olpc-utils >= 1.3.1

%description
olpc-netutils is a GPL-licensed collection of scripts for logging network
status information on OLPC XOs.

%prep
%autosetup -p1

%build
sed -i 's/python/python3/' usr/bin/sugar-xos
sed -i 's/python/python3/' usr/bin/olpc-mpp

make -f Makefile.build %{?_smp_mflags}


%install
make -f Makefile.build install DESTDIR=$RPM_BUILD_ROOT


%files
%doc COPYING README AUTHORS
%{_bindir}/*


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.2-16
- Initial move to python3

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-15
- Don't require just "python" as that is Python 3 since Fedora 31
- Update the dependency on dbus-python to python2-dbus

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.2-8
- Adjust arches

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.8.2-1
- New 0.8.2 release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 20 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.8.1-1
- New 0.8.1 release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov  9 2009 Daniel Drake <dsd@laptop.org> - 0.8-1
- new release for F11 thanks to Martin Langhoff:
- olpc-mesh: bail out of msh0 does not exist
- olpc-sugar: remove wrong 'Total' line, support dev/test usage
- sugar-xos: added support for direct dbus socket
- connections: read available network interfaces at startup
- netstatus: fix to work on F11 images
- Pull in tcpdump for olpc-netcapture.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 17 2008 Peter Robinson <pbrobinson@gmail.com> - 0.7-2
- Rebuild for Fedora 10 rebase

* Fri Sep 12 2008 Michael Stone <michael@laptop.org> - 0.7-1
- Michael Stone (1):
    Capture disk and process status.

* Fri Sep 12 2008 Michael Stone <michael@laptop.org> - 0.6-2
- Michael Stone (1):
    Pull in tcpdump for olpc-netcapture.

* Fri Sep 12 2008 Michael Stone <michael@laptop.org> - 0.6-1
- Michael Stone (1):
    Dirty hack to make sugar-telepathies work on XOs.

* Fri Sep 12 2008 Michael Stone <michael@laptop.org> - 0.5-1
- Guillaume Desmottes (2):
    Print the quantity of buddies we see.
    Use /tmp/olpc-session-bus if available; otherwise, read the sugar-xos command-line.
- Michael Stone (2):
    Cosmetic fixups to whitespace, comments, and the specfile.
    Makefile improvements.

* Fri Aug 08 2008 Michael Stone <michael@laptop.org> - 0.4-1
- Robin Norwood (1):
    rh#457142: Preserve timestamps when installing files.
- Michael Stone (1):
    Remove disttags from ChangeLog entries.

* Wed Jul 09 2008 Michael Stone <michael@laptop.org> - 0.3-1
- Install dnsmasq for olpc-mpp.

* Wed Jul 02 2008 Michael Stone <michael@laptop.org> - 0.2-1
- Initial release of this spec.
