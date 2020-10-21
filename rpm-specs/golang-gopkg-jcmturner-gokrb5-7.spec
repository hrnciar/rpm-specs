# Generated by go2rpm 1
%bcond_without check

# https://github.com/jcmturner/gokrb5
%global goipath         gopkg.in/jcmturner/gokrb5.v7
%global forgeurl        https://github.com/jcmturner/gokrb5
Version:                7.5.0

%gometa


%global goipathsex0     gopkg.in/jcmturner/gokrb5.v7/v8

%global common_description %{expand:
Pure Go Kerberos library for clients and services.}

%global golicenses      LICENSE
%global godocs          examples CONTRIBUTING.md README.md USAGE.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Pure Go Kerberos library for clients and services

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/hashicorp/go-uuid)
BuildRequires:  golang(github.com/jcmturner/gofork/encoding/asn1)
BuildRequires:  golang(github.com/jcmturner/gofork/x/crypto/pbkdf2)
BuildRequires:  golang(golang.org/x/crypto/md4)
BuildRequires:  golang(golang.org/x/crypto/pbkdf2)
BuildRequires:  golang(gopkg.in/jcmturner/aescts.v1)
BuildRequires:  golang(gopkg.in/jcmturner/dnsutils.v1)
BuildRequires:  golang(gopkg.in/jcmturner/goidentity.v3)
BuildRequires:  golang(gopkg.in/jcmturner/rpc.v1/mstypes)
BuildRequires:  golang(gopkg.in/jcmturner/rpc.v1/ndr)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
rm -rf v8/

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Sun Aug 02 18:16:50 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 7.5.0-1
- Initial package