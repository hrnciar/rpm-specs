# Generated by go2rpm 1
%bcond_with check

# https://github.com/nats-io/stan.go
%global goipath         github.com/nats-io/stan.go
Version:                0.6.0

%gometa

%global goaltipaths     github.com/nats-io/go-nats-streaming

%global common_description %{expand:
NATS Streaming is an extremely performant, lightweight reliable streaming
platform powered by NATS.}

%global golicenses      LICENSE
%global godocs          examples CODE-OF-CONDUCT.md GOVERNANCE.md\\\
                        MAINTAINERS.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Performant, lightweight reliable streaming platform

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gogo/protobuf/gogoproto)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/nats-io/nats.go)
BuildRequires:  golang(github.com/nats-io/nats.go/bench)
BuildRequires:  golang(github.com/nats-io/nuid)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/nats-io/nats-server/test)
BuildRequires:  golang(github.com/nats-io/nats-streaming-server/server)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
sed -i "s|github.com/nats-io/nats-server/v2|github.com/nats-io/nats-server|" $(find . -type f -name "*.go")

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Sat Feb 01 21:27:01 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.0-1
- Initial package