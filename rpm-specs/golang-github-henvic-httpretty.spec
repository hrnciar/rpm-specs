# Generated by go2rpm 1
%bcond_without check

# https://github.com/henvic/httpretty
%global goipath         github.com/henvic/httpretty
Version:                0.0.5

%gometa

%global common_description %{expand:
Package httpretty prints the HTTP requests you make with Go pretty on your
terminal.}

%global golicenses      LICENSE.md
%global godocs          example README.md CONTRIBUTING.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Prints the HTTP requests you make with Go pretty on your terminal

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
* Tue Apr 14 12:07:19 EDT 2020 Jared K. Smith <jsmith@fedoraproject.org> - 0.0.5-1
- Initial package

