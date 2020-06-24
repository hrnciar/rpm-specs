# Generated by go2rpm
%bcond_without check

# https://github.com/bradfitz/iter
%global goipath         github.com/bradfitz/iter
%global commit          33e6a9893b0c090a6ba5a4227a98c4145c61d09a

%gometa

%global common_description %{expand:
Package Iter provides a syntactically different way to iterate over integers.}

%global golicenses      LICENSE
%global godocs          README.txt

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Range over integers [0,n)

# Upstream license specification: BSD-3-Clause
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
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 23:29:00 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20190307git33e6a98
- Update to new macros

* Thu Mar 07 2019 Robert-André Mauchin - 0-0.1.20190307git33e6a98
- First package for Fedora
