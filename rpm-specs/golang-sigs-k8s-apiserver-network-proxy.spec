# Generated by go2rpm 1
%bcond_without check

# https://github.com/kubernetes-sigs/apiserver-network-proxy
%global goipath         sigs.k8s.io/apiserver-network-proxy
%global forgeurl        https://github.com/kubernetes-sigs/apiserver-network-proxy
Version:                0.0.12

%gometa

%global common_description %{expand:
Proto-type and reference implementations for server network proxies.}

%global golicenses      LICENSE
%global godocs          examples CONTRIBUTING.md code-of-conduct.md README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Proto-type and reference implementations for server network proxies

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/mock/gomock)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/connectivity)
BuildRequires:  golang(google.golang.org/grpc/credentials)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(k8s.io/api/authentication/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/wait)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd)
BuildRequires:  golang(k8s.io/klog/v2)

%if %{with check}
# Tests
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/client-go/kubernetes/fake)
BuildRequires:  golang(k8s.io/client-go/kubernetes/typed/authentication/v1/fake)
BuildRequires:  golang(k8s.io/client-go/testing)
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
%gocheck -d konnectivity-client/pkg/client -t pkg
%endif

%gopkgfiles

%changelog
* Tue Sep 29 17:26:10 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.12-1
- Update to 0.0.12

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.10-4
- Do not vendor google.golang.org/grpc

* Tue Jun 16 14:57:42 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.10-3
- Exclude requires

* Mon Jun 15 21:44:25 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.10-2
- Fix vendoring

* Sun Apr 12 23:39:42 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.10-1
- Initial package
