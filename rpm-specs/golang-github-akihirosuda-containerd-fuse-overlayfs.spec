# Generated by go2rpm 1
%bcond_without check

# https://github.com/AkihiroSuda/containerd-fuse-overlayfs
%global goipath         github.com/AkihiroSuda/containerd-fuse-overlayfs
%global commit          ce3f92bc40ad9f820e0f733758ae5e3df0f120f7

%gometa

%global common_description %{expand:
Fuse-overlayfs plugin for rootless containerd.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Fuse-overlayfs plugin for rootless containerd

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/containerd/containerd/api/services/snapshots/v1)
BuildRequires:  golang(github.com/containerd/containerd/contrib/snapshotservice)
BuildRequires:  golang(github.com/containerd/containerd/log)
BuildRequires:  golang(github.com/containerd/containerd/mount)
BuildRequires:  golang(github.com/containerd/containerd/platforms)
BuildRequires:  golang(github.com/containerd/containerd/plugin)
BuildRequires:  golang(github.com/containerd/containerd/snapshots)
BuildRequires:  golang(github.com/containerd/containerd/snapshots/storage)
BuildRequires:  golang(github.com/containerd/continuity/fs)
BuildRequires:  golang(github.com/coreos/go-systemd/v22/daemon)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(google.golang.org/grpc)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/containerd/containerd/pkg/testutil)
BuildRequires:  golang(github.com/containerd/containerd/snapshots/testsuite)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

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
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Thu Oct 01 11:13:10 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20201001gitce3f92b
- Initial package
