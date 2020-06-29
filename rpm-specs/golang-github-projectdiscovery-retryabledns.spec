# Generated by go2rpm 1
%bcond_without check

# https://github.com/projectdiscovery/retryabledns
%global goipath         github.com/projectdiscovery/retryabledns
Version:                1.0.4

%gometa

%global common_description %{expand:
Retryable DNS client in Go.}

# Fixed but not released yet: https://github.com/projectdiscovery/retryabledns/issues/8
#%%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Retryable DNS client

License:        MIT

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/miekg/dns)

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
* Sun May 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.4-1
- Initial package
