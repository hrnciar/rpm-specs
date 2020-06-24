# Generated by go2rpm
# Not working, dead upstream
%bcond_with check

# https://github.com/jimstudt/http-authentication
%global goipath         github.com/jimstudt/http-authentication
%global commit          3eca13d6893afd7ecabe15f4445f5d2872a1b012

%gometa

%global common_description %{expand:
Go implementation of RFC 2617 HTTP Authentication: Basic and Digest Access
Authentication.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Go implementation of RFC 2617 HTTP Authentication

License:        MIT
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

* Sat May 18 18:40:42 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190702git3eca13d
- Initial package