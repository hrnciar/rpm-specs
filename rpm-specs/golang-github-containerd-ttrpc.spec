# Generated by go2rpm
%bcond_without check

# https://github.com/containerd/ttrpc
%global goipath         github.com/containerd/ttrpc
Version:                1.0.1

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
Release:        2%{?dist}
Summary:        GRPC for low-memory environments

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
# Convert to github.com/golang/protobuf
# https://github.com/containerd/ttrpc/issues/62
Patch0:         0001-Convert-to-github.com-golang-protobuf.patch

BuildRequires:  golang(github.com/golang/protobuf/proto)
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
%patch0 -p1
rm -rf cmd/

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Sun Aug 23 01:04:49 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-2
- Rebuilt for FTBFS

* Sun Aug 09 22:59:10 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 07 05:02:22 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20200207git0be804e
- Bump to commit 0be804eadb152bc3b3c20c5edc314c4633833398

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 17:22:26 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190626git699c4e4
- Initial package
