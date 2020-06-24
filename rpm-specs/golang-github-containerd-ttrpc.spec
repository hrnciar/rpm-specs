# Generated by go2rpm
%bcond_without check

# https://github.com/containerd/ttrpc
%global goipath         github.com/containerd/ttrpc
%global commit          0be804eadb152bc3b3c20c5edc314c4633833398

%gometa

%global common_description %{expand:
GRPC for low-memory environments.

The existing grpc-go project requires a lot of memory overhead for importing
packages and at runtime. While this is great for many services with low density
requirements, this can be a problem when running a large number of services on a
single machine or on a machine with a small amount of memory.

Using the same GRPC definitions, this project reduces the binary size and
protocol overhead required. We do this by eliding the net/http, net/http2 and
grpc package used by grpc replacing it with a lightweight framing protocol. The
result are smaller binaries that use less resident memory with the same ease of
use as GRPC.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        GRPC for low-memory environments

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gogo/protobuf/gogoproto)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/protoc-gen-gogo/descriptor)
BuildRequires:  golang(github.com/gogo/protobuf/protoc-gen-gogo/generator)
BuildRequires:  golang(github.com/gogo/protobuf/types)
BuildRequires:  golang(github.com/gogo/protobuf/vanity)
BuildRequires:  golang(github.com/gogo/protobuf/vanity/command)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(google.golang.org/genproto/googleapis/rpc/status)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/status)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/prometheus/procfs)
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
%doc example README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Fri Feb 07 05:02:22 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20200207git0be804e
- Bump to commit 0be804eadb152bc3b3c20c5edc314c4633833398

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 17:22:26 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190626git699c4e4
- Initial package
