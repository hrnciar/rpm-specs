# Using just the commit date as the version, upstream has not cut a release
# in ten years so they're unlikely to start now...
#global snapdate 20170830
#global snapver %{snapdate}git

Name:		can-utils
Version:	2020.02.04
Release:	2%{?snapdate:.%{snapdate}}%{?dist}
Summary:	SocketCAN user space utilities and tools

# most utilities are dual-licensed but some are GPLv2 only
License:	GPLv2 and (GPLv2 or BSD)
URL:		https://github.com/linux-can/can-utils
# Upstream does not provide release-tarballs
#Source0:       %{name}-%{snapver}.tar.gz
Source0:	https://github.com/linux-can/can-utils/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Use this to extract new snapshots from upstream git repo
Source1:	can-snapshot.sh

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gcc
BuildRequires:	glibc-devel

%description
CAN is a message-based network protocol designed for vehicles originally
created by Robert Bosch GmbH. SocketCAN is a set of open source CAN
drivers and a networking stack contributed by Volkswagen Research to
the Linux kernel.

This package contains some user space utilities for Linux SocketCAN subsystem.

%prep
#%setup -q -n %{name}-%{snapver}
%setup -q
# Correct includes
for file in canlogserver cansniffer isotpdump isotpperf slcanpty isotpdump isotpsniffer; do
    sed -i -e 's|#include <sys/socket.h>|#include <linux/sockios.h>|' ${file}.c
done

%build
autoreconf -vif

export CFLAGS="%{optflags} -fno-strict-aliasing"

%configure --disable-silent-rules
make %{?_smp_mflags}

# Extract the dual license from one of the sources
head -39 asc2log.c | tail -37 | cut -c4- > COPYING

%install
%make_install

%files
%license COPYING
%doc README.md
%{_bindir}/asc2log
%{_bindir}/bcmserver
%{_bindir}/can-calc-bit-timing
%{_bindir}/canbusload
%{_bindir}/candump
%{_bindir}/canfdtest
%{_bindir}/cangen
%{_bindir}/cangw
%{_bindir}/canlogserver
%{_bindir}/canplayer
%{_bindir}/cansend
%{_bindir}/cansniffer
%{_bindir}/isotpdump
%{_bindir}/isotpperf
%{_bindir}/isotprecv
%{_bindir}/isotpsend
%{_bindir}/isotpserver
%{_bindir}/isotpsniffer
%{_bindir}/isotptun
%{_bindir}/jacd
%{_bindir}/jcat
%{_bindir}/jspy
%{_bindir}/jsr
%{_bindir}/log2asc
%{_bindir}/log2long
%{_bindir}/slcan_attach
%{_bindir}/slcand
%{_bindir}/slcanpty
%{_bindir}/testj1939

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.02.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.02.04-1
- Update to 2020.02.04

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.02.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.02.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.02.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.02.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2018.02.0-1
- Upstream 2018.02.0 release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170830git-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 24 2017 Panu Matilainen <pmatilai@redhat.com> - 20170830git-1
- New snapshot from upstream
- Package README.md file now that it has somewhat meaningful content

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20160229git-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20160229git-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20160229git-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 14 2016 Panu Matilainen <pmatilai@redhat.com> - 20160229git-1
- Initial packaging
