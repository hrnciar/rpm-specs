# Generated by go2rpm 1
%bcond_without check

# https://github.com/census-ecosystem/opencensus-go-exporter-aws
%global goipath         contrib.go.opencensus.io/exporter/aws
%global forgeurl        https://github.com/census-ecosystem/opencensus-go-exporter-aws
%global commit          c50fb1bd7f2166f05435d6965cbcdda1abc19092

%gometa

%global common_description %{expand:
OpenCensus Go exporters for AWS (XRay only for now).}

%global golicenses      LICENSE
%global godocs          examples AUTHORS CONTRIBUTING.md README.md

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        OpenCensus Go exporters for AWS

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/aws/aws-sdk-go/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/xray)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/xray/xrayiface)
BuildRequires:  golang(go.opencensus.io/plugin/ochttp)
BuildRequires:  golang(go.opencensus.io/trace)
BuildRequires:  golang(go.opencensus.io/trace/propagation)

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
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 19:28:41 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190917gitc50fb1b
- Initial package
