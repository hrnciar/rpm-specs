# Generated by go2rpm 1
%bcond_without check

# https://github.com/creack/goselect
%global goipath         github.com/creack/goselect
Version:                0.1.1

%gometa

%global common_description %{expand:
Select(2) implementation in Go.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Select(2) implementation in Go

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Nov 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.1-1
- Update to latest version

* Fri Oct 18 06:42:59 EDT 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.0-1
- Initial package
