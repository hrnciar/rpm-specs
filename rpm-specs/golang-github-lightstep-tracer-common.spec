# Generated by go2rpm
%bcond_without check

# https://github.com/lightstep/lightstep-tracer-common
%global goipath         github.com/lightstep/lightstep-tracer-common
Version:                1.0.3

%gometa

%global common_description %{expand:
Files shared by most or all of the LightStep tracer implementations.}

Name:           %{goname}
Release:        3%{?dist}
Summary:        Files shared by most or all of the LightStep tracer implementations

# https://github.com/lightstep/lightstep-tracer-common/issues/28
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/types)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(google.golang.org/genproto/googleapis/api/annotations)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/internal/transport)

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 23:34:01 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.3-1
- Initial package
