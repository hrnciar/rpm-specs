# Generated by go2rpm 1
%bcond_without check

# https://github.com/cncf/udpa
%global goipath         github.com/cncf/udpa
Version:                0.0.1

%gometa

%global common_description %{expand:
Universal Data Plane API Working Group (UDPA-WG).}

%global golicenses      LICENSE
%global godocs          DEVELOPER.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Universal Data Plane API Working Group (UDPA-WG)

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/envoyproxy/protoc-gen-validate/validate)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
BuildRequires:  golang(github.com/golang/protobuf/ptypes)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/any)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/duration)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/struct)
BuildRequires:  golang(google.golang.org/grpc)

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
* Thu Sep 03 21:04:31 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1-1
- Initial package
