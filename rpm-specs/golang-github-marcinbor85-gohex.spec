# Generated by go2rpm
%bcond_without check

# https://github.com/marcinbor85/gohex
%global goipath         github.com/marcinbor85/gohex
%global commit          7a43cd876e46e0f6ddc553f10f91731a78e6e949

%gometa

%global common_description %{expand:
A Go library for parsing Intel HEX files.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Go library for parsing Intel HEX files

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 00:29:28 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20190422git7a43cd8
- Update to new macros

* Mon Apr 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20190422git7a43cd8
- First package for Fedora