# Generated by go2rpm 1
%bcond_without check

# https://github.com/aaronjanse/pty
%global goipath         github.com/aaronjanse/pty
Version:                1.1.14

%gometa

%global common_description %{expand:
Pty is a Go package for using unix pseudo-terminals.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go package for using unix pseudo-terminals

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
* Sun Sep 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.14-1
- Initial package for Fedora