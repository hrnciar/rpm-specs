# Generated by go2rpm
%bcond_without check

# https://github.com/census-ecosystem/opencensus-go-exporter-ocagent
%global goipath         contrib.go.opencensus.io/exporter/ocagent
%global forgeurl        https://github.com/census-ecosystem/opencensus-go-exporter-ocagent
Version:                0.6.0

%gometa

%global common_description %{expand:
This repository contains the Go implementation of the OpenCensus Agent
(OC-Agent) Exporter. OC-Agent is a daemon process running in a VM that can
retrieve spans/stats/metrics from OpenCensus Library, export them to other
backends and possibly push configurations back to Library. See more details
on OC-Agent Readme.

Note: This is an experimental repository and is likely to get
backwards-incompatible changes. Ultimately we may want to move the OC-Agent Go
Exporter to OpenCensus Go core library.}

%global golicenses      LICENSE
%global godocs          example CONTRIBUTING.md README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        OpenCensus Go exporters for OpenCensus Agent
# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/census-instrumentation/opencensus-proto/gen-go/agent/common/v1)
BuildRequires:  golang(github.com/census-instrumentation/opencensus-proto/gen-go/agent/metrics/v1)
BuildRequires:  golang(github.com/census-instrumentation/opencensus-proto/gen-go/agent/trace/v1)
BuildRequires:  golang(github.com/census-instrumentation/opencensus-proto/gen-go/metrics/v1)
BuildRequires:  golang(github.com/census-instrumentation/opencensus-proto/gen-go/resource/v1)
BuildRequires:  golang(github.com/census-instrumentation/opencensus-proto/gen-go/trace/v1)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires:  golang(go.opencensus.io)
BuildRequires:  golang(go.opencensus.io/plugin/ocgrpc)
BuildRequires:  golang(go.opencensus.io/resource)
BuildRequires:  golang(go.opencensus.io/stats)
BuildRequires:  golang(go.opencensus.io/stats/view)
BuildRequires:  golang(go.opencensus.io/tag)
BuildRequires:  golang(go.opencensus.io/trace)
BuildRequires:  golang(go.opencensus.io/trace/tracestate)
BuildRequires:  golang(go.opencensus.io/zpages)
BuildRequires:  golang(google.golang.org/api/support/bundler)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/credentials)
BuildRequires:  golang(google.golang.org/grpc/metadata)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 28 18:24:46 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.0-2
- Update to 0.6.0 (#1742113)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 18:47:05 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.0-1
- Release 0.5.0

* Thu Apr 11 23:50:43 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.12-1
- Release 0.4.12 (#1698212)

* Sat Apr 06 19:46:03 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.11-1
- Release 0.4.11 (#1696869)

* Tue Apr 02 17:24:03 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.10-1
- Release 0.4.10 (#1694918)

* Mon Mar 25 20:22:34 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.9-1
- First package for Fedora
