# Generated by go2rpm
%bcond_without check

# https://github.com/opentracing-contrib/go-grpc
%global goipath         github.com/opentracing-contrib/go-grpc
%global commit          db30781987df913dc5a2345439c43e1598e33434

%gometa

%global common_description %{expand:
The Otgrpc package makes it easy to add OpenTracing support to gRPC-based
systems in Go.}

%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        OpenTracing support for any gRPC client or server

License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/ext)
BuildRequires:  golang(github.com/opentracing/opentracing-go/log)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/status)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/opentracing/opentracing-go/mocktracer)
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
* Thu Jul 30 18:37:38 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20200730gitdb30781
- Bump to commit db30781987df913dc5a2345439c43e1598e33434

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 08:41:36 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190701git4b5a12d
- Initial package
