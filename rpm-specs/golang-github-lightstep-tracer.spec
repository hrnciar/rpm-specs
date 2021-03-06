# Generated by go2rpm
# https://github.com/lightstep/lightstep-tracer-go/issues/217
%ifnarch %{ix86} %{arm} s390x
%bcond_without check
%endif

# https://github.com/lightstep/lightstep-tracer-go
%global goipath         github.com/lightstep/lightstep-tracer-go
Version:                0.20.0

%gometa

%global common_description %{expand:
Package Lightstep implements the LightStep OpenTracing client for Go.}

%global golicenses      LICENSE
%global godocs          examples CHANGELOG.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        LightStep distributed tracing library for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# Go 1.15: https://github.com/lightstep/lightstep-tracer-go/issues/257
Patch0:         0001-Convert-id-to-string-using-strconv.Itoa.patch

BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/types)
BuildRequires:  golang(github.com/lightstep/lightstep-tracer-common/golang/gogo/collectorpb)
BuildRequires:  golang(github.com/lightstep/lightstep-tracer-common/golang/gogo/lightsteppb)
BuildRequires:  golang(github.com/lightstep/lightstep-tracer-common/golang/gogo/metricspb)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/ext)
BuildRequires:  golang(github.com/opentracing/opentracing-go/log)
BuildRequires:  golang(github.com/shirou/gopsutil/cpu)
BuildRequires:  golang(github.com/shirou/gopsutil/mem)
BuildRequires:  golang(github.com/shirou/gopsutil/net)
BuildRequires:  golang(github.com/shirou/gopsutil/process)
BuildRequires:  golang(go.opencensus.io/trace)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/credentials)
BuildRequires:  golang(google.golang.org/grpc/metadata)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/lightstep/lightstep-tracer-common/golang/gogo/collectorpb/collectorpbfakes)
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/gomega)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jul 28 22:32:31 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.20.0-1
- Update to 0.20.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 23:31:21 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.16.0-1
- Initial package
