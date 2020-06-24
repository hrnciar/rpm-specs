# Generated by go2rpm 1
%bcond_without check

# https://github.com/weppos/publicsuffix-go
%global goipath         github.com/weppos/publicsuffix-go
Version:                0.5.0

%gometa

%global common_description %{expand:
The package publicsuffix provides a Go domain name parser based on the Public
Suffix List.}

%global golicenses      LICENSE.txt
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Domain name parser for Go based on the Public Suffix List

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/idna)

%if %{with check}
# Tests
BuildRequires:  golang(golang.org/x/net/publicsuffix)
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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 01:22:50 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.0-1
- Initial package
