# Generated by go2rpm
%bcond_without check

# https://github.com/ianlancetaylor/cgosymbolizer
%global goipath         github.com/ianlancetaylor/cgosymbolizer
%global commit          f5072df9c550dc687157e5d7efb50825cdf8f0eb

%gometa

%global common_description %{expand:
A Go package that can be used to convert cgo function pointers into useful
backtrace information.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Experimental symbolizer for cgo backtraces

License:        BSD
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

* Wed May 15 19:02:31 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190701gitf5072df
- Initial package