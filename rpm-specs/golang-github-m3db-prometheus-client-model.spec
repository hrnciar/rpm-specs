# Generated by go2rpm
%bcond_without check

# https://github.com/m3db/prometheus_client_model
%global goipath         github.com/m3db/prometheus_client_model
Version:                0.0.2
%global commit          d3fff8420252ef63bffb96f689d1a85096c97321

%gometa

%global common_description %{expand:
Data model artifacts for Prometheus.}

%global golicenses      LICENSE NOTICE
%global godocs          CONTRIBUTING.md MAINTAINERS.md README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Data model artifacts for Prometheus

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/protobuf/proto)

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
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 15:58:25 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.2-1.20190628gitd3fff84
- Initial package
