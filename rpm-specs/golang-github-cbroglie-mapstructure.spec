# Generated by go2rpm
%bcond_without check

# https://github.com/cbroglie/mapstructure
%global goipath         github.com/cbroglie/mapstructure
%global commit          300500ef91c136320994efa1d54bcea36d035f61

%gometa

%global common_description %{expand:
Mapstructure is a Go library for decoding generic map values to structures and
vice versa, while providing helpful error handling.

This library is most useful when decoding values from some data stream (JSON,
Gob, etc.) where you don't quite know the structure of the underlying data until
you read a part of it. You can therefore read a map[string]interface{} and use
this library to decode it into the proper underlying native Go structure.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Go library for decoding generic map values into native Go structures

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 20:50:12 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190702git300500e
- Initial package
