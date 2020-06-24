# Generated by go2rpm
%bcond_without check

# https://github.com/docker/go-metrics
%global goipath         github.com/docker/go-metrics
%global commit          b84716841b82eab644a0c64fc8b42d480e49add5

%gometa

%global common_description %{expand:
This package is small wrapper around the prometheus Go client to help enforce
convention and best practices for metrics collection in Docker projects.}

%global golicenses      LICENSE LICENSE.docs NOTICE
%global godocs          CONTRIBUTING.md README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Metrics collection in Docker projects

# Upstream license specification: CC-BY-SA-4.0 and Apache-2.0
License:        CC-BY-SA and ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 03 18:56:57 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190627gitb847168
- Initial package