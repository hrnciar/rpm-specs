# Generated by go2rpm
%bcond_without check

# https://github.com/xrash/smetrics
%global goipath         github.com/xrash/smetrics
%global commit          a3153f7040e90324c58c6287535e26a0ac5c1cc1

%gometa

%global common_description %{expand:
This library contains implementations of the Levenshtein distance, Jaro-Winkler
and Soundex algorithms written in Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        String metrics library written in Go

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 17:17:57 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20190530gita3153f7
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gita3153f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gita3153f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 0-0.1.gita3153f7
- Initial packaging
