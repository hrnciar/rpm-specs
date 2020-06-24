# Generated by go2rpm
%bcond_without check

# https://github.com/go-martini/martini
%global goipath         github.com/go-martini/martini
Version:                1.0
%global commit          22fa46961aabd2665cf3f1343b146d20028f5071

%gometa

%global common_description %{expand:
Martini is a powerful package for quickly writing modular web
applications/services in Golang.}

%global golicenses      LICENSE
%global godocs          README.md translations/*.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Classy web framework for go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/codegangsta/inject)

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 23:17:21 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0-1.20190415git22fa469
- Initial package