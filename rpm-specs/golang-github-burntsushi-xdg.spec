# Generated by go2rpm 1
%bcond_without check

# https://github.com/BurntSushi/xdg
%global goipath         github.com/BurntSushi/xdg
%global commit          e80d3446fea190e21fbd294569844f066e47ccfc

%gometa

%global common_description %{expand:
A Go package for reading config and data files according to the XDG Base
Directory specification.}

%global golicenses      COPYING
%global godocs          README

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Reader for the XDG Base Directory specification

License:        Public Domain

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200429gite80d344
- Initial package

