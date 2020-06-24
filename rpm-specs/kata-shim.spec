%if (0%{?fedora} && 0%{?fedora >= 31})
    %define have_go_rpm_macros 1
%else
    %define have_go_rpm_macros 0
%endif

%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%if ! 0%{?gobuild:1}
# %gobuild not available on RHEL. Definition lifted from Fedora33 podman.spec and tested on RHEL-8.2
%define gobuild(o:) GO111MODULE=off go build -buildmode pie -compiler gc -tags="rpm_crashtraceback ${BUILDTAGS:-}" -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '-Wl,-z,relro -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld '" -a -v -x %{?**};
%endif

%global domain          github.com
%global org             kata-containers
%global repo            shim
%global download        %{domain}/%{org}/%{repo}
%global importname      %{download}

# Release candidate version tracking
# global rcver rc0
%if 0%{?rcver:1}
%global rcrel .%{rcver}
%global rcstr -%{rcver}
%endif

Name:      kata-%{repo}
Version:   1.11.0
Release:   1%{?rcrel}%{?dist}
Url:       https://%{download}
Source0:   https://%{download}/archive/%{version}%{?rcstr}/%{repo}-%{version}%{?rcstr}.tar.gz
Summary:   A shim running in the host for teh Kata Containers project
Group:     Development/Tools
License:   ASL 2.0

%if 0%{?have_go_rpm_macros}
BuildRequires: go-rpm-macros
%else
BuildRequires: compiler(go-compiler)
BuildRequires: golang
%endif

Provides: bundled(golang(github.com/Azure/go-ansiterm)) = d6e3b3328b783f23731bc4d058875b0371ff8109
Provides: bundled(golang(github.com/davecgh/go-spew)) = v1.1.0
Provides: bundled(golang(github.com/docker/docker)) = bc183a0062c1283cfc47f42ec78501868629dd2b
Provides: bundled(golang(github.com/gogo/protobuf)) = 342cbe0a04158f6dcb03ca0079991a51a4248c02
Provides: bundled(golang(github.com/golang/protobuf)) = 1e59b77b52bf8e4b449a57e6f79f21226d571845
Provides: bundled(golang(github.com/kata-containers/agent)) = 8f22514ae5790f3b6953cf93692e663fa29469e3
Provides: bundled(golang(github.com/kr/pty)) = v1.1.0
Provides: bundled(golang(github.com/mdlayher/vsock)) = 738c88d6e4cfd60e8124a5344fa10d205fd828b9
Provides: bundled(golang(github.com/moby/moby)) = v1.13.1
Provides: bundled(golang(github.com/opencontainers/runtime-spec)) = 4e3b9264a330d094b0386c3703c5f379119711e8
Provides: bundled(golang(github.com/pmezard/go-difflib)) = v1.0.0
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.0.4
Provides: bundled(golang(github.com/stretchr/testify)) = v1.2.0
Provides: bundled(golang(golang.org/x/crypto)) = 13931e22f9e72ea58bb73048bc752b48c6d4d4ac
Provides: bundled(golang(golang.org/x/net)) = a8b9294777976932365dabb6640cf1468d95c70f
Provides: bundled(golang(golang.org/x/sys)) = 810d7000345868fc619eb81f46307107118f4ae1
Provides: bundled(golang(golang.org/x/text)) = e19ae1496984b1c655b8044a65c0300a3c878dd3
Provides: bundled(golang(google.golang.org/genproto)) = a8101f21cf983e773d0c1133ebc5424792003214
Provides: bundled(golang(google.golang.org/grpc)) = v1.8.0


%description
This project implements a shim called kata-shim for the Kata Containers project.

Kata Containers is an open source project and community working to
build a standard implementation of lightweight Virtual Machines (VMs)
that feel and perform like containers, but provide the workload
isolation and security advantages of VMs.

The shim runs in the host environment, handling standard I/O and
signals on behalf of the container process which runs inside the
virtual machine.

%prep
%autosetup -p1 -n %{repo}-%{version}%{?rcstr}

%build
# Adjust for go build requirements
# Future: Use %gopkginstall
# export GOROOT="$(pwd)/go"
export GOPATH="$(pwd)/go"

mkdir go
mv vendor go/src
mkdir -p go/src/%{domain}/%{org}
ln -s $(pwd)/../%{repo}-%{version}%{?rcstr} go/src/%{importname}
cd go/src/%{importname}

LDFLAGS="-linkmode=external -X main.version=%{version}%{?rcstr}"
%gobuild

%install
install -D shim %{buildroot}%{_libexecdir}/kata-containers/%{name}

%files
%license LICENSE
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%dir %{_libexecdir}/kata-containers
%{_libexecdir}/kata-containers/%{name}


%changelog
* Fri May 08 2020 Cole Robinson <crobinso@redhat.com> - 1.11.0-1
- Update to version 1.11.0

* Mon Apr 20 2020 Cole Robinson <aintdiscole@gmail.com> - 1.11.0-0.1-rc0
- Update to 1.11.0-rc0

* Mon Mar 23 2020 Fabiano Fidêncio <fidencio@redhat.com> - 1.11.0-0.alpha1
- Update to release 1.11.0-alpha1

* Sat Feb 15 2020 Cole Robinson <aintdiscole@gmail.com> - 1.10.0-3
- virtio-fs fixes

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Christophe de Dinechin <dinechin@redhat.com> - 1.10.0-1
- Update to release 1.10.0
  + Some debugging fixing (tracing, PREFIX path)

* Fri Jan 17 2020 Christophe de Dinechin <dinechin@redhat.com> - 1.9.3-1
- Update to release 1.9.3 (no changes upstream)

* Fri Jan 17 2020 Christophe de Dinechin <dinechin@redhat.com> - 1.9.2-1
- Update to release 1.9.2 (no changes upstream)

* Fri Nov 29 2019 Christophe de Dinechin <dinechin@redhat.com> - 1.9.1-1
- Update to release 1.9.1

* Thu Nov 14 2019 Christophe de Dinechin <dinechin@redhat.com> - 1.9.0-1
- Update to release 1.9.0

* Fri Sep 20 2019 Christophe de Dinechin <dinechin@redhat.com> - 1.8.2-1
- Update to 1.8.2 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3.git6346110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2.git6346110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.3.1-6.git58f757d
- use macros where possible

* Wed Nov 21 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.3.1-5.git58f757d
- build with %%gobuild

* Wed Nov 21 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.3.1-4.git58f757d
- build for all supported arches

* Wed Nov 21 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.3.1-3.git58f757d
- no need for make as BR

* Mon Nov 12 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.3.1-2.git58f757d
- bundled Provides

* Sat Nov 10 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.3.1-1.git58f757d
- bump to v1.3.1
- built commit 58f757d

* Thu Jun 14 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-1.git087a537
- first build (ready for Fedora review)
