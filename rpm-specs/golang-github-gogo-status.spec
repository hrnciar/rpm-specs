# Generated by go2rpm 1
%bcond_without check

# https://github.com/gogo/status
%global goipath         github.com/gogo/status
Version:                1.1.0

%gometa

%global common_description %{expand:
GRPC-like status package for use with GoGo Protobuf types.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        GRPC-like status package for use with GoGo Protobuf types

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gogo/googleapis/google/rpc)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/types)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/any)
BuildRequires:  golang(google.golang.org/genproto/googleapis/rpc/status)
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
* Wed Aug 12 18:03:50 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-1
- Initial package
