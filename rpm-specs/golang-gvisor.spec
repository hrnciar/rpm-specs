%bcond_without check

# https://github.com/google/gvisor
%global goipath         gvisor.dev/gvisor
%global forgeurl        https://github.com/google/gvisor
Version:                20200804.0
# taken from the "go" branch (as bazel is not available in fedora)
%global commit          1d6b9c1e7c040f90f7520abed1fe7ea9aac3b85e

%global go_arches       x86_64

%gometa

%global common_description %{expand:
gVisor is an open-source, OCI-compatible sandbox runtime that provides
a virtualized container environment. It runs containers with a new
user-space kernel, delivering a low overhead container security
solution for high-density applications.

gVisor integrates with Docker, containerd and Kubernetes, making it
easier to improve the security isolation of your containers while
still using familiar tooling. Additionally, gVisor supports a variety
of underlying mechanisms for intercepting application calls, allowing
it to run in diverse host environments, including cloud-hosted virtual
machines.}

%global golicenses      LICENSE
%global godocs          README.md AUTHORS

Name:           %{goname}
Release:        1%{?dist}
Summary:        A container sandbox runtime focused on security, efficiency, and ease of use

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/cenkalti/backoff)
BuildRequires:  golang(github.com/containerd/cgroups)
BuildRequires:  golang(github.com/containerd/console)
BuildRequires:  golang(github.com/containerd/containerd/api/events)
BuildRequires:  golang(github.com/containerd/containerd/api/types/task)
BuildRequires:  golang(github.com/containerd/containerd/errdefs)
BuildRequires:  golang(github.com/containerd/containerd/events)
BuildRequires:  golang(github.com/containerd/containerd/log)
BuildRequires:  golang(github.com/containerd/containerd/mount)
BuildRequires:  golang(github.com/containerd/containerd/namespaces)
BuildRequires:  golang(github.com/containerd/containerd/pkg/process)
BuildRequires:  golang(github.com/containerd/containerd/pkg/stdio)
BuildRequires:  golang(github.com/containerd/containerd/runtime)
BuildRequires:  golang(github.com/containerd/containerd/runtime/linux/runctypes)
BuildRequires:  golang(github.com/containerd/containerd/runtime/v1/shim/v1)
BuildRequires:  golang(github.com/containerd/containerd/runtime/v2/shim)
BuildRequires:  golang(github.com/containerd/containerd/runtime/v2/task)
BuildRequires:  golang(github.com/containerd/containerd/sys)
BuildRequires:  golang(github.com/containerd/containerd/sys/reaper)
BuildRequires:  golang(github.com/containerd/fifo)
BuildRequires:  golang(github.com/containerd/go-runc)
BuildRequires:  golang(github.com/containerd/ttrpc)
BuildRequires:  golang(github.com/containerd/typeurl)
BuildRequires:  golang(github.com/gofrs/flock)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/types)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/ptypes)
BuildRequires:  golang(github.com/google/btree)
BuildRequires:  golang(github.com/google/subcommands)
BuildRequires:  golang(github.com/kr/pty)
BuildRequires:  golang(github.com/mohae/deepcopy)
BuildRequires:  golang(github.com/opencontainers/runtime-spec/specs-go)
BuildRequires:  golang(github.com/syndtr/gocapability/capability)
BuildRequires:  golang(github.com/vishvananda/netlink)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/time/rate)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/status)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/runsc %{goipath}/runsc

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Aug 05 23:07:20 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 20200804.0-1.20200805git1d6b9c1
- Update to 20200804.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200211.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200211.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 03 2020 Marc-André Lureau <marcandre.lureau@redhat.com> - 20200211.0-1.20200220git384ed13
- Initial package - rhbz#1804288
