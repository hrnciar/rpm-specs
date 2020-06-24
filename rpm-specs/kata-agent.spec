%global have_go_rpm_macros 0
%if (0%{?fedora} && 0%{?fedora >= 31})
    %global have_go_rpm_macros 1
%endif

# Debug stripping is disabled, because this package is not run
# on the host but inside an appliance VM, so shipping debuginfo
# packages is not intuitive. Maybe there's some clever way to
# deal with this though...
%global with_debug 0

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%if ! 0%{?gobuild:1}
# gobuild not available on RHEL. Definition lifted from Fedora33 podman.spec and tested on RHEL-8.2
%global gobuild(o:) GO111MODULE=off go build -buildmode pie -compiler gc -tags="rpm_crashtraceback ${BUILDTAGS:-}" -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '-Wl,-z,relro -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld '" -a -v -x %{?**};
%endif

%global domain          github.com
%global org             kata-containers
%global repo            agent
%global download        %{domain}/%{org}/%{repo}
%global importname      %{download}

# Release candidate version tracking
# global rcver rc0
%if 0%{?rcver:1}
%global rcrel .%{rcver}
%global rcstr -%{rcver}
%endif

%global katalibexecdir          %{_libexecdir}/kata-containers
%global kataagentdir            %{katalibexecdir}/agent
%global katalocalstatecachedir  %{_localstatedir}/cache/kata-containers


Version: 1.11.0
Name: kata-agent
Release: 1%{?rcrel}%{?dist}
License: ASL 2.0
Summary: Kata guest agent
URL: https://%{download}
Source0: https://%{download}/archive/%{version}%{?rcstr}/%{repo}-%{version}%{?rcstr}.tar.gz

# kata-agent doesn't build on arm32 or i686
ExcludeArch: %{arm}
ExcludeArch: %{ix86}


%if 0%{?have_go_rpm_macros}
BuildRequires: go-rpm-macros
%else
BuildRequires: compiler(go-compiler)
BuildRequires: golang
%endif
BuildRequires: git
BuildRequires: make


# Bundled kata-agent pieces
Provides: bundled(golang(github.com/checkpoint-restore/go-criu)) = v3.11
Provides: bundled(golang(github.com/cilium/ebpf)) = 4032b1d8aae306b7bb94a2a11002932caf88c644
Provides: bundled(golang(github.com/codahale/hdrhistogram)) = 3a0bb77429bd3a61596f5e8a3172445844342120
Provides: bundled(golang(github.com/containerd/console)) = 2748ece16665b45a47f884001d5831ec79703880
Provides: bundled(golang(github.com/coreos/go-systemd)) = v15
Provides: bundled(golang(github.com/cyphar/filepath-securejoin)) = v0.2.1
Provides: bundled(golang(github.com/davecgh/go-spew)) = v1.1.0
Provides: bundled(golang(github.com/docker/docker)) = v1.13.1
Provides: bundled(golang(github.com/docker/go-units)) = v0.3.2
Provides: bundled(golang(github.com/godbus/dbus)) = v4.1.0
Provides: bundled(golang(github.com/gogo/protobuf)) = 4cbf7e384e768b4e01799441fdf2a706a5635ae7
Provides: bundled(golang(github.com/golang/protobuf)) = 1e59b77b52bf8e4b449a57e6f79f21226d571845
Provides: bundled(golang(github.com/grpc-ecosystem/grpc-opentracing)) = 8e809c8a86450a29b90dcc9efbf062d0fe6d9746
Provides: bundled(golang(github.com/hashicorp/yamux)) = cc6d2ea263b2471faabce371255777a365bf8306
Provides: bundled(golang(github.com/konsorten/go-windows-terminal-sequences)) = v1.0.2
Provides: bundled(golang(github.com/mdlayher/vsock)) = 7b7533a7ca4eba7dd23dab2de70e25ca6eecf7e2
Provides: bundled(golang(github.com/mrunalp/fileutils)) = 7d4729fb36185a7c1719923406c9d40e54fb93c7
Provides: bundled(golang(github.com/opencontainers/runc)) = 2fc03cc11c775b7a8b2e48d7ee447cb9bef32ad0
Provides: bundled(golang(github.com/opencontainers/runtime-spec)) = a1b50f621a48ad13f8f696a162f684a241307db0
Provides: bundled(golang(github.com/opencontainers/selinux)) = v1.2.2
Provides: bundled(golang(github.com/opentracing/opentracing-go)) = v1.0.2
Provides: bundled(golang(github.com/pkg/errors)) = v0.9.1
Provides: bundled(golang(github.com/pmezard/go-difflib)) = v1.0.0
Provides: bundled(golang(github.com/seccomp/libseccomp-golang)) = v0.9.1
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.4.2
Provides: bundled(golang(github.com/stretchr/testify)) = 87b1dfb5b2fa649f52695dd9eae19abe404a4308
Provides: bundled(golang(github.com/syndtr/gocapability)) = d98352740cb2c55f81556b63d4a1ec64c5a319c2
Provides: bundled(golang(github.com/uber/jaeger-client-go)) = v2.15.0
Provides: bundled(golang(github.com/uber/jaeger-lib)) = v1.5.0
Provides: bundled(golang(github.com/vishvananda/netlink)) = 2cbcf73e3dcdaa63941d0ec4008e69c089434756
Provides: bundled(golang(github.com/vishvananda/netns)) = be1fbeda19366dea804f00efff2dd73a1642fdcc
Provides: bundled(golang(golang.org/x/net)) = a8b9294777976932365dabb6640cf1468d95c70f
Provides: bundled(golang(golang.org/x/sys)) = b016eb3dc98ea7f69ed55e8216b87187067ae621
Provides: bundled(golang(golang.org/x/text)) = 57961680700a5336d15015c8c50686ca5ba362a4
Provides: bundled(golang(google.golang.org/genproto)) = 7f0da29060c682909f650ad8ed4e515bd74fa12a
Provides: bundled(golang(google.golang.org/grpc)) = d11072e7ca9811b1100b80ca0269ac831f06d024


%description
Kata guest agent. This is not used on the host, it is copied into
the kata guest image via kata-osbuilder scripts.


%prep
%autosetup -Sgit -n agent-%{version}%{?rcstr}


%build
mkdir go
mv vendor go/src
mkdir -p go/src/%{domain}/%{org}
ln -s $(pwd)/../%{repo}-%{version}%{?rcstr} go/src/%{importname}
cd go/src/%{importname}

export GOPATH="$(pwd)/go"
LDFLAGS="-linkmode=external -X main.version=%{version}%{?rcstr}"
%gobuild -o kata-agent

# Make generated service files
%make_build DESTDIR=%{buildroot}%{kataagentdir}

# Ensure kata-agent is newer than generated .service files, or
# 'make install' triggers a rebuild
touch kata-agent


%install
# Install the whole kata agent rooted in /usr/libexec
# The whole tree is copied into the appliance
%make_install DESTDIR=%{buildroot}%{kataagentdir}


%files
%license LICENSE
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%dir %{katalibexecdir}
%dir %{kataagentdir}
%{kataagentdir}/*


%changelog
* Fri May 08 2020 Cole Robinson <crobinso@redhat.com> - 1.11.0-1
- Update to version 1.11.0

* Mon Apr 20 2020 Cole Robinson <aintdiscole@gmail.com> - 1.11.0-0.2.rc0
- Update to 1.11.0-rc0

* Tue Mar 24 2020 Cole Robinson <crobinso@redhat.com> - 1.11.0-0.1.alpha1
- Initial split of kata-agent out from kata-osbuilder
