# Generated by go2rpm
%bcond_without check

# https://github.com/nats-io/nuid
%global goipath         github.com/nats-io/nuid
Version:                1.0.1

%gometa

%global common_description %{expand:
A highly performant unique identifier generator.}

%global golicenses      LICENSE
%global godocs          GOVERNANCE.md MAINTAINERS.md README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Highly performant unique identifier generator

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 00:52:01 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-1
- Initial package
