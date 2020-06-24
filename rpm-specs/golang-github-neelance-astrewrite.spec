# Generated by go2rpm
%bcond_without check

# https://github.com/neelance/astrewrite
%global goipath         github.com/neelance/astrewrite
%global commit          99348263ae862cc230986ce88deaddbf7edcc034

%gometa

%global common_description %{expand:
Go tool to write AST.}

%global golicenses      LICENSE

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        Go tool to write AST

# Upstream license specification: BSD-2-Clause
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

* Mon May 27 20:37:58 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180418git9934826
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git9934826
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git9934826
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180418git9934826
- First package for Fedora
