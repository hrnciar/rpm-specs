# Generated by go2rpm
%bcond_without check

# https://github.com/knz/strtime
%global goipath         github.com/knz/strtime
%global commit          be999391ffa90a7880271a65d53f760fc1cf0151

%gometa

%global common_description %{expand:
Strftime and strptime are functions found in nearly all C library
implementations but with slightly different behaviors on each platform.

To provide identical behavior on all platforms where Go is supported, this
strtime package provides two functions Strftime and Strptime which can be used
in lieu of the platform's native C implementation.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Stable strptime / strftime for Go

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/pkg/errors)

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
* Tue Jul 28 19:50:04 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20200728gitbe99939
- Bump to commit be999391ffa90a7880271a65d53f760fc1cf0151

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 22:49:49 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190701gitaf2256e
- Initial package
