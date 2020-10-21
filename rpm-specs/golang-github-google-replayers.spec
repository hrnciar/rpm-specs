# Generated by go2rpm 1
%bcond_without check

# https://github.com/google/go-replayers
%global goipath         github.com/google/go-replayers
Version:                0.1.1
%global commit          bd9e3607ce6aa15c8efa64828ddd4f43fc5ff1fc
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
This package contains two tools for testing network clients by recording real
interactions with servers, then playing back the server responses later. These
record/replay proxies let you run an "integration" test that accesses a backend
and record the interaction. Subsequent runs of the test can replay the server's
responses without actually contacting the server, turning the integration test
into a fast and inexpensive unit test.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md examples

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go Tools for Recording and Replaying RPCs

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/ptypes)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/any)
BuildRequires:  golang(github.com/google/martian/v3)
BuildRequires:  golang(github.com/google/martian/v3/fifo)
BuildRequires:  golang(github.com/google/martian/v3/httpspec)
BuildRequires:  golang(github.com/google/martian/v3/martianhttp)
BuildRequires:  golang(github.com/google/martian/v3/martianlog)
BuildRequires:  golang(github.com/google/martian/v3/mitm)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(google.golang.org/api/option)
BuildRequires:  golang(google.golang.org/api/transport/http)
BuildRequires:  golang(google.golang.org/genproto/googleapis/rpc/status)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/status)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  golang(google.golang.org/grpc/codes)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
sed -i 's|github.com/google/martian|github.com/google/martian/v3|' $(find -iname "*.go" -type f)

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Aug 10 21:09:38 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.1-2
- Update martian import path

* Mon Jul 27 13:24:37 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.1-1
- Update to 0.1.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 22:09:00 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1
- Initial package
