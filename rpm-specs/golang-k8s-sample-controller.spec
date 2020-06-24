# Generated by go2rpm
%bcond_without check

# https://github.com/kubernetes/sample-controller
%global goipath         k8s.io/sample-controller
%global forgeurl        https://github.com/kubernetes/sample-controller
Version:                1.15.0
%global tag             kubernetes-1.15.0
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
This package implements a simple controller for watching Foo resources as
defined with a CustomResourceDefinition (CRD).}

%global golicenses      LICENSE
%global godocs          docs CONTRIBUTING.md code-of-conduct.md README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Simple controller for watching Foo resources

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(k8s.io/api/apps/v1)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/labels)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer)
BuildRequires:  golang(k8s.io/apimachinery/pkg/types)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/wait)
BuildRequires:  golang(k8s.io/apimachinery/pkg/watch)
BuildRequires:  golang(k8s.io/client-go/discovery)
BuildRequires:  golang(k8s.io/client-go/discovery/fake)
BuildRequires:  golang(k8s.io/client-go/informers)
BuildRequires:  golang(k8s.io/client-go/informers/apps/v1)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/kubernetes/scheme)
BuildRequires:  golang(k8s.io/client-go/kubernetes/typed/core/v1)
BuildRequires:  golang(k8s.io/client-go/listers/apps/v1)
BuildRequires:  golang(k8s.io/client-go/rest)
BuildRequires:  golang(k8s.io/client-go/testing)
BuildRequires:  golang(k8s.io/client-go/tools/cache)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd)
BuildRequires:  golang(k8s.io/client-go/tools/record)
BuildRequires:  golang(k8s.io/client-go/util/flowcontrol)
BuildRequires:  golang(k8s.io/client-go/util/workqueue)
BuildRequires:  golang(k8s.io/klog)

%if %{with check}
# Tests
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/diff)
BuildRequires:  golang(k8s.io/client-go/kubernetes/fake)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/sample-controller %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc docs CONTRIBUTING.md code-of-conduct.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 07 14:26:05 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.15.0-1
- Release 1.15.0

* Mon May 20 17:19:33 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.13.7-1.beta.0
- Initial package
