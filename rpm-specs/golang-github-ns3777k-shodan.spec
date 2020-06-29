# Generated by go2rpm 1
%bcond_without check

# https://github.com/ns3777k/go-shodan/shodan
%global goipath         github.com/ns3777k/go-shodan/shodan
Version:                4.2.0

%gometa

%global common_description %{expand:
A Shodan client written in Go.}

Name:           %{goname}
Release:        1%{?dist}
Summary:        Shodan API client

License:        MIT

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/google/go-querystring/query)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

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
* Mon Apr 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.2.0-1
- Initial package

