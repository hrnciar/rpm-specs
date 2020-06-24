# Generated by go2rpm
%bcond_with check
%bcond_without bootstrap

# https://github.com/docker/swarmkit
%global goipath         github.com/docker/swarmkit
Version:                1.12.0
%global commit          ebe39a32e3ed4c3a3783a02c11cccf388818694c

%gometa

%global common_description %{expand:
SwarmKit is a toolkit for orchestrating distributed systems at any scale. It
includes primitives for node discovery, raft-based consensus, task scheduling
and more.

Its main benefits are:
 - Distributed: SwarmKit uses the Raft Consensus Algorithm in order to
   coordinate and does not rely on a single point of failure to perform
   decisions.
 - Secure: Node communication and membership within a Swarm are secure out of
   the box. SwarmKit uses mutual TLS for node authentication, role authorization
   and transport encryption, automating both certificate issuance and rotation.
 - Simple: SwarmKit is operationally simple and minimizes infrastructure
   dependencies. It does not need an external database to operate.}

%global golicenses      LICENSE
%global godocs          BUILDING.md CONTRIBUTING.md README.md

Name:           %{goname}
Release:        7%{?dist}
Summary:        Toolkit for orchestrating distributed systems at any scale

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
# Convert BasicKeyRequest to KeyRequest to use cloudflare/cfssl 1.4.1
Patch0:         0001-Convert-BasicKeyRequest-to-KeyRequest-to-use-cloudfl.patch

BuildRequires:  golang(code.cloudfoundry.org/clock)
BuildRequires:  golang(code.cloudfoundry.org/clock/fakeclock)
BuildRequires:  golang(github.com/cloudflare/cfssl/api)
BuildRequires:  golang(github.com/cloudflare/cfssl/config)
BuildRequires:  golang(github.com/cloudflare/cfssl/csr)
BuildRequires:  golang(github.com/cloudflare/cfssl/errors)
BuildRequires:  golang(github.com/cloudflare/cfssl/helpers)
BuildRequires:  golang(github.com/cloudflare/cfssl/helpers/derhelpers)
BuildRequires:  golang(github.com/cloudflare/cfssl/initca)
BuildRequires:  golang(github.com/cloudflare/cfssl/log)
BuildRequires:  golang(github.com/cloudflare/cfssl/signer)
BuildRequires:  golang(github.com/cloudflare/cfssl/signer/local)
BuildRequires:  golang(github.com/docker/distribution/reference)
BuildRequires:  golang(github.com/docker/docker/api/types)
BuildRequires:  golang(github.com/docker/docker/api/types/container)
BuildRequires:  golang(github.com/docker/docker/api/types/events)
BuildRequires:  golang(github.com/docker/docker/api/types/filters)
BuildRequires:  golang(github.com/docker/docker/api/types/mount)
BuildRequires:  golang(github.com/docker/docker/api/types/network)
BuildRequires:  golang(github.com/docker/docker/api/types/volume)
BuildRequires:  golang(github.com/docker/docker/client)
BuildRequires:  golang(github.com/docker/docker/pkg/plugingetter)
BuildRequires:  golang(github.com/docker/docker/pkg/signal)
BuildRequires:  golang(github.com/docker/go-connections/nat)
BuildRequires:  golang(github.com/docker/go-events)
BuildRequires:  golang(github.com/docker/go-metrics)
BuildRequires:  golang(github.com/docker/go-units)
BuildRequires:  golang(github.com/docker/libnetwork/datastore)
BuildRequires:  golang(github.com/docker/libnetwork/driverapi)
BuildRequires:  golang(github.com/docker/libnetwork/drivers/bridge/brmanager)
BuildRequires:  golang(github.com/docker/libnetwork/drivers/host)
BuildRequires:  golang(github.com/docker/libnetwork/drivers/ipvlan/ivmanager)
BuildRequires:  golang(github.com/docker/libnetwork/drivers/macvlan/mvmanager)
BuildRequires:  golang(github.com/docker/libnetwork/drivers/overlay/overlayutils)
BuildRequires:  golang(github.com/docker/libnetwork/drivers/overlay/ovmanager)
BuildRequires:  golang(github.com/docker/libnetwork/drivers/remote)
BuildRequires:  golang(github.com/docker/libnetwork/drvregistry)
BuildRequires:  golang(github.com/docker/libnetwork/idm)
BuildRequires:  golang(github.com/docker/libnetwork/ipamapi)
BuildRequires:  golang(github.com/docker/libnetwork/ipams/builtin)
BuildRequires:  golang(github.com/docker/libnetwork/ipams/null)
BuildRequires:  golang(github.com/docker/libnetwork/ipams/remote)
BuildRequires:  golang(github.com/docker/libnetwork/ipamutils)
BuildRequires:  golang(github.com/docker/libnetwork/netlabel)
BuildRequires:  golang(github.com/dustin/go-humanize)
BuildRequires:  golang(github.com/fernet/fernet-go)
BuildRequires:  golang(github.com/gogo/protobuf/gogoproto)
BuildRequires:  golang(github.com/gogo/protobuf/plugin/testgen)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/protoc-gen-gogo/descriptor)
BuildRequires:  golang(github.com/gogo/protobuf/protoc-gen-gogo/generator)
BuildRequires:  golang(github.com/gogo/protobuf/sortkeys)
BuildRequires:  golang(github.com/gogo/protobuf/types)
BuildRequires:  golang(github.com/gogo/protobuf/vanity)
BuildRequires:  golang(github.com/gogo/protobuf/vanity/command)
BuildRequires:  golang(github.com/grpc-ecosystem/go-grpc-prometheus)
BuildRequires:  golang(github.com/hashicorp/go-memdb)
BuildRequires:  golang(github.com/opencontainers/go-digest)
BuildRequires:  golang(github.com/phayes/permbits)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/rcrowley/go-metrics)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(go.etcd.io/bbolt)
BuildRequires:  golang(go.etcd.io/etcd/pkg/fileutil)
BuildRequires:  golang(go.etcd.io/etcd/pkg/idutil)
BuildRequires:  golang(go.etcd.io/etcd/raft)
BuildRequires:  golang(go.etcd.io/etcd/raft/raftpb)
# BuildRequires:  golang(go.etcd.io/etcd/etcdserver/api/snap)
BuildRequires:  golang(go.etcd.io/etcd/wal)
BuildRequires:  golang(go.etcd.io/etcd/wal/walpb)
BuildRequires:  golang(golang.org/x/crypto/nacl/secretbox)
BuildRequires:  golang(golang.org/x/crypto/pbkdf2)
BuildRequires:  golang(golang.org/x/net/context/ctxhttp)
BuildRequires:  golang(golang.org/x/time/rate)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/credentials)
BuildRequires:  golang(google.golang.org/grpc/grpclog)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/peer)
BuildRequires:  golang(google.golang.org/grpc/status)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/docker/docker/pkg/plugins)
BuildRequires:  golang(github.com/docker/libnetwork/discoverapi)
BuildRequires:  golang(github.com/docker/libnetwork/types)
BuildRequires:  golang(github.com/gogo/protobuf/jsonpb)
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/gomega)
BuildRequires:  golang(github.com/onsi/gomega/types)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1
sed -i "s|github.com/coreos/etcd|go.etcd.io/etcd|" $(find . -name "*.go")
sed -i "s|go.etcd.io/etcd/snap|go.etcd.io/etcd/etcdserver/api/snap|" $(find . -name "*.go")

%if %{without bootstrap}
%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%endif

%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%endif

%if %{with check}
%check
%gocheck -d agent/exec/dockerapi -d agent -d template -d node -d integration -d ca
%endif

%if %{without bootstrap}
%files
%license LICENSE
%doc BUILDING.md CONTRIBUTING.md README.md
%{_bindir}/*
%endif

%gopkgfiles

%changelog
* Sat Apr 04 23:57:20 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.12.0-7.20200404gitebe39a3
- Bump to commit ebe39a32e3ed4c3a3783a02c11cccf388818694c

* Wed Feb 12 19:39:17 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.12.0-6.20200130git49e3561
- Move go.etcd.io/etcd/snap to go.etcd.io/etcd/etcdserver/api/snap

* Thu Jan 30 19:40:00 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.12.0-5.20200130git49e3561
- Bump to commit 49e35619b18200845c9365c1e953440c28868002

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 06 16:17:25 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.12.0-2.20190706git7c0bd0e
- Bump to commit 7c0bd0e0c09e07956085a48877fdec3a2f798e69

* Sun May 05 17:29:54 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.12.0-1.20190628git36866a9
- Initial package
