# Generated by go2rpm 1
# The tests are communitating with a thrid-party system
%bcond_with check

# https://github.com/go-resty/resty
%global goipath         github.com/go-resty/resty
Version:                2.2.0

%gometa

%global common_description %{expand:
Simple HTTP and REST client library for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Simple HTTP and REST client library

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/publicsuffix)

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
* Sun Mar 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.0-2
- Add comment about tests
- Remove file (rhbz#1816642)

* Tue Mar 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.0-1
- Initial package for Fedora

