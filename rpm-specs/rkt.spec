# Generated by go2rpm
%bcond_without check
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(github.com/containernetworking/cni.*\\)$

# Unsupported arches
%ifnarch armv7hl ppc64le s390x
%bcond_without binary
%endif

# https://github.com/rkt/rkt
%global goipath         github.com/rkt/rkt
Version:                1.30.0
%global commit          0c8765619cae3391a9ffa12c8dbd12ba7a475eb8

%gometa

%global goaltipaths     github.com/coreos/rkt

%global common_description %{expand:
Rkt (pronounced like a "rocket") is a CLI for running application containers on
Linux. rkt is designed to be secure, composable, and standards-based.}

%global golicenses      LICENSE pkg/acl/LICENSE.MIT\\\
                        store/imagestore/LICENSE.BSD
%global godocs          CHANGELOG.md CODE-OF-CONDUCT.md CONTRIBUTING.md\\\
                        README.md ROADMAP.md Documentation

%global gosupfiles      "${vendor[@]}"

Name:           rkt
Release:        3%{?dist}
Summary:        Pod-native container engine for Linux

# Upstream license specification: Apache-2.0 and BSD-3-Clause and MIT
# Main library: ASL 2.0
# pkg/acl: MIT
# store/imagestore: BSD
License:        ASL 2.0 and BSD and MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bc
BuildRequires:  git-core
BuildRequires:  glibc-static
BuildRequires:  golang >= 1.6
BuildRequires:  gperf
BuildRequires:  gnupg
BuildRequires:  intltool
BuildRequires:  libacl-devel
BuildRequires:  libcap-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  libmount-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  trousers-devel
BuildRequires:  perl-Config-Tiny
BuildRequires:  squashfs-tools
BuildRequires:  systemd-devel
BuildRequires:  systemd >= 222
BuildRequires:  golang(github.com/appc/docker2aci/lib)
BuildRequires:  golang(github.com/appc/docker2aci/lib/common)
BuildRequires:  golang(github.com/appc/goaci/proj2aci)
BuildRequires:  golang(github.com/appc/spec/aci)
BuildRequires:  golang(github.com/appc/spec/discovery)
BuildRequires:  golang(github.com/appc/spec/pkg/acirenderer)
BuildRequires:  golang(github.com/appc/spec/pkg/device)
BuildRequires:  golang(github.com/appc/spec/pkg/tarheader)
BuildRequires:  golang(github.com/appc/spec/schema)
BuildRequires:  golang(github.com/appc/spec/schema/lastditch)
BuildRequires:  golang(github.com/appc/spec/schema/types)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/client/metadata)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/request)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/signer/v4)
# Use bundled ones until upstream updates
# BuildRequires:  golang(github.com/containernetworking/cni/pkg/invoke)
# BuildRequires:  golang(github.com/containernetworking/cni/pkg/types)
# BuildRequires:  golang(github.com/containernetworking/plugins/pkg/ip)
# BuildRequires:  golang(github.com/containernetworking/plugins/pkg/ns)
# BuildRequires:  golang(github.com/containernetworking/plugins/pkg/utils)
# BuildRequires:  golang(github.com/containernetworking/plugins/pkg/utils/sysctl)
BuildRequires:  golang(github.com/coreos/gexpect)
BuildRequires:  golang(github.com/coreos/go-iptables/iptables)
BuildRequires:  golang(github.com/coreos/go-systemd/activation)
BuildRequires:  golang(github.com/coreos/go-systemd/daemon)
BuildRequires:  golang(github.com/coreos/go-systemd/unit)
BuildRequires:  golang(github.com/coreos/go-systemd/util)
BuildRequires:  golang(github.com/coreos/go-tspi/tpmclient)
BuildRequires:  golang(github.com/coreos/ioprogress)
BuildRequires:  golang(github.com/coreos/pkg/dlopen)
BuildRequires:  golang(github.com/d2g/dhcp4)
BuildRequires:  golang(github.com/d2g/dhcp4client)
BuildRequires:  golang(github.com/dustin/go-humanize)
BuildRequires:  golang(github.com/godbus/dbus)
BuildRequires:  golang(github.com/godbus/dbus/introspect)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/gorilla/mux)
BuildRequires:  golang(github.com/hashicorp/errwrap)
BuildRequires:  golang(github.com/hashicorp/golang-lru)
BuildRequires:  golang(github.com/hydrogen18/stoppableListener)
BuildRequires:  golang(github.com/jonboulle/clockwork)
BuildRequires:  golang(github.com/kballard/go-shellquote)
BuildRequires:  golang(github.com/kr/pty)
BuildRequires:  golang(github.com/opencontainers/selinux/go-selinux/label)
BuildRequires:  golang(github.com/pborman/uuid)
BuildRequires:  golang(github.com/peterbourgon/diskv)
BuildRequires:  golang(github.com/PuerkitoBio/purell)
BuildRequires:  golang(github.com/shirou/gopsutil/load)
BuildRequires:  golang(github.com/shirou/gopsutil/process)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/syndtr/gocapability/capability)
BuildRequires:  golang(github.com/vishvananda/netlink)
BuildRequires:  golang(golang.org/x/crypto/openpgp)
BuildRequires:  golang(golang.org/x/crypto/openpgp/errors)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(modernc.org/ql/driver)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/kr/pretty)
%endif

%{?systemd_requires}
Requires(pre):  shadow-utils
Requires:       iptables
Requires:       systemd-container

%description
%{common_description}

%gopkg

%prep
%goprep -k

# Keep mandatory vendor only
mkdir tmp
cp -R --parents vendor/github.com/appc/spec/actool tmp
cp -R --parents vendor/github.com/containernetworking/cni tmp
rm -rf vendor
mv tmp/vendor vendor

# Upgrade import paths
find . -name "*.go" -exec sed -i "s|github.com/cznic/ql|modernc.org/ql|" "{}" +;
find . -name "*.go" -exec sed -i "s|github.com/aws/aws-sdk-go/private/signer/v4|github.com/aws/aws-sdk-go/aws/signer/v4|" "{}" +;
sed -i "s|activation.Listeners(true)|activation.Listeners()|" vendor/github.com/containernetworking/cni/plugins/ipam/dhcp/daemon.go
sed -i "s|v4.Sign|v4.SignSDKRequest|" rkt/config/auth.go

# Unbundle
sed -i "s|GOPATH := \$(GOPATH_TO_CREATE)|GOPATH := \"%{?gopath}:%{gobuilddir}:%{_builddir}\"|" makelib/variables.mk
ln -s %{_builddir}/%{name}-%{commit} %{_builddir}/src

%if %{with binary}
%build
./autogen.sh
export GOPATH=%{?gopath}
# ./configure flags: https://github.com/coreos/rkt/blob/master/Documentation/build-configure.md
%configure --with-stage1-flavors=host,fly                                     \
           --with-stage1-flavors-version-override=%{version}-%{release}       \
           --with-stage1-default-images-directory=%{_libexecdir}/%{name}      \
           --with-stage1-default-location=%{_libexecdir}/%{name}/stage1-host.aci
%make_build all bash-completion
%endif

%install
mapfile -t vendor <<< $(find vendor -type f)
%gopkginstall

%if %{with binary}
# install binaries
install -dp %{buildroot}{%{_bindir},%{_libexecdir}/%{name},%{_unitdir}}
install -dp %{buildroot}%{_sharedstatedir}/%{name}

install -pm755 build-%{name}-%{version}+git/target/bin/%{name} %{buildroot}%{_bindir}
install -pm755 dist/scripts/setup-data-dir.sh %{buildroot}%{_bindir}/%{name}-setup-data-dir.sh
install -pm644 build-%{name}-%{version}+git/target/bin/stage1-*.aci %{buildroot}%{_libexecdir}/%{name}

# install bash completion
install -dp %{buildroot}%{_datadir}/bash-completion/completions
install -pm644 dist/bash_completion/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}

# install metadata unitfiles
install -pm644 dist/init/systemd/%{name}-gc.timer %{buildroot}%{_unitdir}
install -pm644 dist/init/systemd/%{name}-gc.service %{buildroot}%{_unitdir}
install -pm644 dist/init/systemd/%{name}-metadata.socket %{buildroot}%{_unitdir}
install -pm644 dist/init/systemd/%{name}-metadata.service %{buildroot}%{_unitdir}

install -dp %{buildroot}%{_prefix}/lib/tmpfiles.d
install -pm644 dist/init/systemd/tmpfiles.d/%{name}.conf %{buildroot}%{_prefix}/lib/tmpfiles.d

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
exit 0

%post
%{_bindir}/systemd-tmpfiles --create %{_prefix}/lib/tmpfiles.d/%{name}.conf
%systemd_post %{name}-metadata.service

%preun
%systemd_preun %{name}-metadata.service

%postun
%systemd_postun_with_restart %{name}-metadata.service
%endif

%if %{with check}
%check
%gocheck -d tests -d pkg/pod -d pkg/tar -d rkt -d rkt/image -d store/db -d store/imagestore -d store/treestore
%endif

%if %{with binary}
%files
%license LICENSE pkg/acl/LICENSE.MIT store/imagestore/LICENSE.BSD
%doc CHANGELOG.md CODE-OF-CONDUCT.md CONTRIBUTING.md
%doc README.md ROADMAP.md Documentation
%{_bindir}/%{name}
%{_bindir}/%{name}-setup-data-dir.sh
%{_libexecdir}/%{name}/stage1-*.aci
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
%{_prefix}/lib/tmpfiles.d/%{name}.conf
%{_sharedstatedir}/%{name}
%{_unitdir}/%{name}*
%endif

%gopkgfiles

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 14:03:50 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.30.0-1.20190512git0c87656
- Release 1.30.0, commit 0c8765619cae3391a9ffa12c8dbd12ba7a475eb8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-6.gitd2d35e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-5.gitd2d35e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-4.gitd2d35e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-3.gitd2d35e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-2.gitd2d35e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 13 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.25.0-1.gitd2d35e0
- built @coreos/master commit d2d35e0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-3.git34ff175
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 22 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.23.0-2.git34ff175
- set default stage1 image dir to /usr/libexec/rkt
- built commit 34ff175

* Sat Jan 21 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.23.0-1.git34ff175
- bump to v1.23.0
- built commit 34ff175

* Sat Jan 14 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.22.0-1.git81602c6
- Resolves: #1412106 - bump to v1.22.0
- built commit 81602c6

* Mon Jan 09 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.21.0-2.git6b3852f
- create dir structure using rkt.conf file

* Wed Dec 14 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.21.0-1.git6b3852f
- Resolves: #1403520 - bump to v1.21.0
- built commit#6b3852f

* Tue Nov 29 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.20.0-1.gitd9d6ad8
- Resolves: #1394076 - bump to v1.20.0
- built commit d9d6ad8

* Sat Oct 29 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.18.0-1.gite22f5f8
- Resolves: #1385271 - bump to v1.18.0
- built commit#e22f5f8

* Fri Sep 30 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.16.0-1.gitc5e67a2
- Resolves: #1376622 - bump to v1.16.0
- built commit c5e67a2

* Mon Sep 26 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.15.0-2.git53825ed
- built commit 53825ed

* Fri Sep 16 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.15.0-1.gitcf0aa2e
- Resolves: #1376622 - bump to v1.15.0
- built commit cf0aa2e

* Mon Sep 12 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.14.0-4.git05b8bd9
- built commit 05b8bd9
- correct dep name - systemd-container

* Sat Sep 10 2016 Dennis Gilmore <dennis@ausil.us> - 1.14.0-3.git70b5545
- enable 32 bit arm and x86

* Sat Sep 10 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.14.0-2.git70b5545
- built commit 70b5545
- require iptables and systemd-containers at runtime
- From: Kushal Das <mail@kushaldas.in>

* Thu Sep 01 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.14.0-1.git0d72cd8
- Resolves: #1370817 - bump to v1.14.0
- built commit 0d72cd8

* Wed Aug 31 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.13.0-1.git65894a7
- bump to v1.13.0
- built commit 65894a7

* Sat Aug 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.12.0-2.git826ebf7
- Build on aarch64

* Sat Aug 13 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.12.0-1.git826ebf7
- Resolves: #1365245 - bump to v1.12.0
- Resolves: #1366811 - include "fly" stage1 flavor
- built commit#826ebf7

* Mon Jul 25 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.11.0-1.git1ec4c60
- built commit 1ec4c60

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-5.gite61deb2
- https://fedoraproject.org/wiki/Changes/golang1.7

* Tue Jul 19 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.10.0-4.gite61deb2
- built commit e61deb2

* Sun Jul 17 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.10.0-3.gitb3a9e95
- built commit b3a9e95

* Thu Jul 14 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.10.0-2.gite76b2fa
- built commit e76b2fa

* Fri Jul 08 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.10.0-1.gite73846f
- built commit e73846f

* Sat Jun 25 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.9.1-1.git1cbbf03
- built commit 1cbbf03

* Mon Jun 13 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.8.0-1.git7ebc0e7
- built commit 7ebc0e7

* Fri Jun 03 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.7.0-1.git09c4760
- Resolves: #1341436 - update to 1.7.0
- built commit 09c4760
- br: systemd-devel for /usr/include/systemd/sd-journal.h

* Thu May 26 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.6.0-5.git26e62f5
- built commit#26e62f5

* Tue May 24 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.6.0-4.git8f74d28
- built commit#8f74d28

* Sat May 21 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.6.0-3.git3386b89
- built commit 3386b89

* Thu May 19 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.6.0-2.gitde05a39
- built commit#de05a39

* Sat May 14 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.6.0-1.git7740f9d
- Resolves: #1336072 - bump to v1.6.0
- built commit 7740f9d

* Fri May 06 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.5.1-1.git38b4462
- Resolves: #1327805 - bump to v1.5.1
- built commit 38b4462

* Sat Apr 02 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.3.0-1.gitb6a73a7
- Resolves: rhbz#1323388 - bump to v1.3.0
- built commit#b6a73a7

* Wed Mar 30 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.2.1-2.gitadc2bbd
- built commit#adc2bbd

* Fri Mar 25 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.2.1-1.gite568957
- built commit#e568957

* Fri Mar 18 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-10.gitff0813b
- built commit#ff0813b

* Mon Mar 14 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-9.git990029c
- built commit#990029c

* Fri Mar 11 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-8.git0aacba3
- built commit#0aacba3

* Wed Mar 09 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-7.git7b07bf2
- built commit#7b07bf2

* Mon Mar 07 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-6.gite2c3011
- built commit#e2c3011

* Sun Mar 06 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-5.git63522c3
- built commit#63522c3

* Fri Mar 04 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-4.git63522c3
- built commit#63522c3

* Wed Mar 02 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-3.git5a19dc6
- built commit#5a19dc6

* Wed Mar 02 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-2.git5a19dc6
- built commit#5a19dc6

* Fri Feb 26 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-1.gitdebc46e
- built commit#debc46e

* Thu Feb 25 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-13.gitd4db664
- built commit#d4db664

* Wed Feb 24 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-12.git07235a7
- built commit#07235a7

* Tue Feb 23 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-11.git9003f4a
- do not remove /var/lib/rkt on uninstall

* Tue Feb 23 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-10.git9003f4a
- built commit#9003f4a

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9.gitd842d09
- https://fedoraproject.org/wiki/Changes/golang1.6

* Mon Feb 22 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-8.gitd842d09
- built commit#d842d09

* Thu Feb 18 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-7.gitd2b211d
- built commit#d2b211d

* Thu Feb 18 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-6.gitd2b211d
- built commit#d2b211d

* Sun Feb 14 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-5.gitf529cc2
- built commit#f529cc2

* Fri Feb 05 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-4.git6ce1d5f
- built commit#6ce1d5f

* Thu Feb 04 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-3.git6146a78
- built commit#6146a78

* Thu Feb 04 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-2.git6146a78
- built commit#6146a78

* Thu Feb 04 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-1.git6146a78
- built commit#6146a78

* Wed Feb 03 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.16.0-6.git5a8ee7d
- built commit#5a8ee7d

* Mon Feb 01 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.16.0-5.gite542f81
- built commit#e542f81

* Wed Jan 27 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.16.0-4.git646746d
- built commit#646746d

* Mon Jan 25 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.16.0-3.git6ad1d4a
- built commit#6ad1d4a

* Sun Jan 24 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.16.0-2.gitf37aae6
- built commit#f37aae6

* Fri Jan 22 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.16.0-1.git43e4d22
- Resolves: rhbz#1300874 - bump to v0.16.0
- built commit#43e4d22

* Thu Jan 14 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.15.0-4.git5988b72
- install bash completion

* Thu Jan 14 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.15.0-3.git5988b72
- built commit#5988b72
- Alban Crequy <alban.crequy@gmail.com> provided fixes for configure flags
and dir paths installed

* Sun Jan 10 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.15.0-2.git7575500
- built commit#7575500

* Mon Aug 03 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.7.0-3.git6dae5d5
- built rkt commit#6dae5d5

* Mon Aug 03 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.7.0-2.git6dae5d5
- built rkt commit#6dae5d5

* Sun Jul 19 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.7.0-1
- New version: 0.7.0, built rkt         commit#c5e8cd5

* Wed Jun 17 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.6.1-1
- New version: 0.6.1, built rkt         commit#30cb88c

* Wed Jun 10 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.6-5.git06bf23b
- built rkt commit#06bf23b

* Sun Jun 07 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.6-4.git7bf926e
- built rkt commit#7bf926e

* Tue Jun 02 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.6-3.git25b862d
- built rkt commit#25b862d

* Fri May 29 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.6-2.gited97885
- built rkt commit#ed97885

* Thu May 28 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.6-1
- New version: 0.5.6, built rkt         commit#139af2b

* Wed May 27 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.5-7.git5e95eac
- built rkt commit#5e95eac

* Sun May 24 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.5-6.gite5be761
- built rkt commit#e5be761

* Mon May 11 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.5-5.git724e49e
- built rkt commit#724e49e

* Mon May 11 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.5-4.git724e49e
- built rkt commit#724e49e

* Fri May 08 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.5-3.gitd61a4c5
- built rkt commit#d61a4c5

* Mon May 04 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.5-2.gitb1190d9
- built rkt commit#b1190d9

* Mon May 04 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.5-1
- New version: 0.5.5, built rkt         commit#b1190d9

* Wed Apr 29 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.4-3.git40ecb47
- built rkt commit#40ecb47

* Wed Apr 29 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.4-2.git%{d_shortcommit}
- built rkt commit#40ecb47

* Thu Apr 23 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-16.gita506a39
- built rkt commit#a506a39

* Tue Apr 21 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-15.git73e6e1e
- built rkt commit#73e6e1e

* Mon Apr 13 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-14.git7bcbe3f
- built rkt commit#7bcbe3f

* Sun Apr 12 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-13.git7bcbe3f
- built rkt commit#7bcbe3f

* Wed Apr 08 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-12.git96d0cc0
- built rkt commit#96d0cc0

* Tue Apr 07 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-11.gitfd44be4
- built rkt commit#fd44be4

* Sun Apr 05 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-10.gitb9bfa72
- built rkt commit#b9bfa72

* Sat Apr 04 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-9.gitb9bfa72
- built rkt commit#b9bfa72

* Fri Apr 03 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-8.gitae78000
- built rkt commit#ae78000

* Fri Apr 03 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-7.gitae78000
- built rkt commit#ae78000

* Fri Apr 03 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-6.gitae78000
- built rkt commit#ae78000

* Fri Apr 03 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-5.gitae78000
- built rkt commit#ae78000

* Fri Apr 03 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-4.gitae78000
- built rkt commit#ae78000

* Fri Apr 03 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-3.gitae78000
- built rkt commit#ae78000

* Thu Apr 02 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-2.gita72ad99
- install stage1.aci and metadata socket file

* Thu Apr 02 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-1.gita72ad99
- update to 0.5.3+git

* Sat Mar 28 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.1-2.git9d66f8c
- use github.com/lsm5/rkt branch systemd-vendored which includes a checked
out systemd v215 tree instead of git cloning it
- should allow building the rpm in a mock/koji environment

* Fri Mar 27 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.1-1.git58bd354
- update to latest upstream master

* Mon Feb 02 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.2.0-1.git29d53af
- use latest master commit
- mkrootfs uses fedora docker base image from koji
via Václav Pavlin <vpavlin@redhat.com>

* Tue Dec 02 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1.0-1.git553023e
- Initial package
- install init in libexec/rkt/stage1
https://github.com/coreos/rkt/issues/173
thanks Jonathan Boulle <jonathan.boulle@coreos.com>
and Tom Prince <tom.prince@ualberta.net>