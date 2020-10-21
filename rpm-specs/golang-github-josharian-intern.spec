# Generated by go2rpm 1
%bcond_without check

# https://github.com/josharian/intern
%global goipath         github.com/josharian/intern
Version:                1.0.0

%gometa

%global common_description %{expand:
Intern Go strings.}

%global golicenses      license.md
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Intern Go strings

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
* Wed Jul 29 17:51:45 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Initial package