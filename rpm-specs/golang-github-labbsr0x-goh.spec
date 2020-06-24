%bcond_without check

%global goipath         github.com/labbsr0x/goh
%global commit          6360eb50f0262fdd96ed65dfb5df813a52590019

%gometa

%global common_description %{expand:
Utility lib for writing extremely simple webhooks in go, among other things.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Go library for writing simple webhooks
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-cmd/cmd)
BuildRequires:  golang(github.com/go-errors/errors)
BuildRequires:  golang(github.com/sirupsen/logrus)

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Carl George <carl@george.computer> - 0-0.1
- Initial package rhbz#1747626
