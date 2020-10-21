# Generated by go2rpm
%bcond_without check

# https://github.com/kubernetes/node-api
%global goipath         k8s.io/node-api
%global forgeurl        https://github.com/kubernetes/node-api
Version:                1.17.12
%global tag             kubernetes-1.17.12
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md code-of-conduct.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/labels)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer)
BuildRequires:  golang(k8s.io/apimachinery/pkg/types)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/watch)
BuildRequires:  golang(k8s.io/client-go/discovery)
BuildRequires:  golang(k8s.io/client-go/discovery/fake)
BuildRequires:  golang(k8s.io/client-go/rest)
BuildRequires:  golang(k8s.io/client-go/testing)
BuildRequires:  golang(k8s.io/client-go/tools/cache)
BuildRequires:  golang(k8s.io/client-go/util/flowcontrol)

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
* Wed Sep 30 03:26:38 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.17.12-1
- Update to 1.17.12

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 21:32:01 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.15.0-1
- Initial package
