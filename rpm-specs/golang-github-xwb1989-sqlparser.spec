# Generated by go2rpm 1
%bcond_without check

# https://github.com/xwb1989/sqlparser
%global goipath         github.com/xwb1989/sqlparser
%global commit          120387863bf27d04bc07db8015110a6e96d0146c

%gometa

%global common_description %{expand:
SQL Parser implemented in Go.}

%global golicenses      LICENSE.md
%global godocs          CONTRIBUTORS.md README.md

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        SQL Parser implemented in Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 21:39:46 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20200703git1203878
- Initial package
