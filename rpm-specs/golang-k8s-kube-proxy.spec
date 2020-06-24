# Generated by go2rpm
%bcond_without check

# https://github.com/kubernetes/kube-proxy
%global goipath         k8s.io/kube-proxy
%global forgeurl        https://github.com/kubernetes/kube-proxy
Version:                1.15.0
%global tag             kubernetes-1.15.0
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
Provide a versioned API for configuring kube-proxy.}

%global golicenses      LICENSE
%global godocs          README.md code-of-conduct.md CONTRIBUTING.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Kube-proxy component configs

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  golang(k8s.io/component-base/config/v1alpha1)

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 07 02:00:44 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.15.0-1
- Release 1.15.0

* Mon May 20 14:47:44 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.13.7-1.beta.0
- Initial package
