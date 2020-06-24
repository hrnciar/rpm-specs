# Generated by go2rpm
%bcond_without check

# https://github.com/ianlancetaylor/demangle
%global goipath         github.com/ianlancetaylor/demangle
%global commit          5e5cf60278f657d30daa329dd0e7e893b6b8f027

%gometa

%global common_description %{expand:
A Go package that can be used to demangle C++ symbol names.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        C++ symbol name demangler written in Go

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 12:55:04 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20190423git5e5cf60
- Bump to commit 5e5cf60278f657d30daa329dd0e7e893b6b8f027

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git4883227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git4883227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180417git4883227
- First package for Fedora