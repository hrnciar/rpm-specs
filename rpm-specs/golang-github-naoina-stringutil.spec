# Generated by go2rpm
%bcond_without check

# https://github.com/naoina/go-stringutil
%global goipath         github.com/naoina/go-stringutil
Version:                0.1.0

%gometa

%global common_description %{expand:
Faster string utilities implementation for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Faster string utilities implementation for Go

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 20:09:13 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1
- Initial package
