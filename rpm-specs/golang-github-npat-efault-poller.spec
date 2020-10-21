# Generated by go2rpm 1
%bcond_without check

# https://github.com/npat-efault/poller
%global goipath         github.com/npat-efault/poller
Version:                2.0.0

%gometa

%global common_description %{expand:
An epoll(7)-based file-descriptor multiplexer.}

%global golicenses      LICENSE.txt
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        An epoll(7)-based file-descriptor multiplexer

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

%ifnarch ppc64le
%if %{with check} 
%check
%gocheck
%endif
%endif

%gopkgfiles

%changelog
* Sun Sep 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.0-1
- Initial package