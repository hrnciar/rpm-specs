# Generated by go2rpm
%bcond_without check

# https://github.com/ghemawat/stream
%global goipath         github.com/ghemawat/stream
%global commit          696b145b53b9611fe9c9f189122f990171e391a0

%gometa

%global common_description %{expand:
Package stream provides filters that can be chained together in a manner
similar to Unix pipelines.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Filters that can be chained together similar to Unix pipelines

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 21:17:06 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190701git696b145
- Initial package