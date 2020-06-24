# Generated by go2rpm
%bcond_without check

# https://github.com/simonferquel/yaml
%global goipath         github.com/simonferquel/yaml
%global commit          69d7a9804db8b5ff0515d2689ad34b6e55065fa9

%gometa

%global common_description %{expand:
YAML support for the Go language.}

%global golicenses      LICENSE LICENSE.libyaml NOTICE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        YAML support for the Go language

# Upstream license specification: Apache-2.0 and MIT
License:        ASL 2.0 and MIT
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

* Thu Jul 04 02:01:10 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190705git69d7a98
- Initial package
