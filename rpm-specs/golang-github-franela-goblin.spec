# Generated by go2rpm
%bcond_without check

# https://github.com/franela/goblin
%global goipath         github.com/franela/goblin
Version:                0.0.2
%global tag             0.0.2

%gometa

%global common_description %{expand:
A Mocha like BDD testing framework written in Go that requires no additional
dependencies. Requires no extensive documentation nor complicated steps to get
it running.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Minimal and beautiful Go testing framework

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 23:37:49 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.2-1
- Initial package
