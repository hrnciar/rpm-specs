%bcond_without check

# https://github.com/google/gvisor
%global goipath         gvisor.dev/gvisor
%global forgeurl        https://github.com/google/gvisor
Version:                20200211.0
# taken from the "go" branch (as bazel is not available in fedora)
%global commit          384ed132b902ead9aae62430382d38ae9afdb95d

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

BuildRequires:  golang(github.com/cenkalti/backoff)
BuildRequires:  golang(github.com/gofrs/flock)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/ptypes)
BuildRequires:  golang(github.com/google/btree)
BuildRequires:  golang(github.com/google/subcommands)
BuildRequires:  golang(github.com/kr/pty)
BuildRequires:  golang(github.com/opencontainers/runtime-spec/specs-go)
BuildRequires:  golang(github.com/syndtr/gocapability/capability)
BuildRequires:  golang(github.com/vishvananda/netlink)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/time/rate)

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
* Tue Mar 03 2020 Marc-André Lureau <marcandre.lureau@redhat.com> - 20200211.0-1.20200220git384ed13
- Initial package - rhbz#1804288
