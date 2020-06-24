# Generated by go2rpm 1
%bcond_without check

# https://github.com/mattn/go-ieproxy
%global goipath         github.com/mattn/go-ieproxy
%global commit          6dee0af9227d0863f1508ce7937af3396d6605c1

%gometa

%global common_description %{expand:
Go package to detect the proxy settings on Windows platform.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Detect the proxy settings on Windows platform

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 11:35:54 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190729git6dee0af
- Initial package
