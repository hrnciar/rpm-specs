# Generated by go2rpm
%bcond_without check

# https://github.com/containerd/typeurl
%global goipath         github.com/containerd/typeurl
%global commit          2a93cfde8c20b23de8eb84a5adbc234ddf7a9e8d

%gometa

%global common_description %{expand:
A Go package for managing the registration, marshaling, and unmarshaling of
encoded types.

This package helps when types are sent over a GRPC API and marshaled as a
protobuf.Any.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Go package for managing marshaled types to protobuf.Any

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/types)
BuildRequires:  golang(github.com/pkg/errors)

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
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 17:30:31 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190626git2a93cfd
- Initial package