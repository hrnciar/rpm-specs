# Generated by go2rpm 1
%bcond_without check

# https://github.com/bketelsen/crypt
%global goipath         github.com/bketelsen/crypt
Version:                0.0.3

%gometa

%global common_description %{expand:
Store and retrieve encrypted configs from etcd or consul.}

%global golicenses      LICENSE
%global godocs          README.md bin/crypt/README.md config/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Store and retrieve encrypted configs from etcd or consul

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(cloud.google.com/go/firestore)
BuildRequires:  golang(github.com/coreos/etcd/client)
BuildRequires:  golang(github.com/hashicorp/consul/api)
BuildRequires:  golang(golang.org/x/crypto/openpgp)
BuildRequires:  golang(google.golang.org/api/iterator)
BuildRequires:  golang(google.golang.org/api/option)
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
* Sat Sep 05 03:01:23 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.3-1
- Initial package
