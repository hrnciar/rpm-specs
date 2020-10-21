# Generated by go2rpm 1
%bcond_without check

# https://github.com/istio/gogo-genproto
%global goipath         istio.io/gogo-genproto
%global forgeurl        https://github.com/istio/gogo-genproto
Version:                1.7.0
%global tag             1.7.0

%gometa

%global common_description %{expand:
Houses generated source code for imported libraries used within Istio.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md SUPPORT.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Houses generated source code for imported libraries used within Istio

# Upstream license specification: BSD-3-Clause and Apache-2.0 and MIT
License:        BSD and ASL 2.0 and MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/protoc-gen-gogo/descriptor)
BuildRequires:  golang(github.com/gogo/protobuf/sortkeys)
BuildRequires:  golang(github.com/gogo/protobuf/types)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/status)

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
* Thu Jul 23 21:50:44 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.7.0-1
- Initial package