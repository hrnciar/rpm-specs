# Generated by go2rpm
%bcond_without check

# https://github.com/jpillora/requestlog
%global goipath         github.com/jpillora/requestlog
Version:                1.0.0

%gometa

%global common_description %{expand:
Simple request logging in Go (Golang).}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple request logging

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/andrew-d/go-termutil)
BuildRequires:  golang(github.com/jpillora/ansi)
BuildRequires:  golang(github.com/jpillora/sizestr)
BuildRequires:  golang(github.com/tomasen/realip)

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
* Wed Feb 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Initial package for Fedora