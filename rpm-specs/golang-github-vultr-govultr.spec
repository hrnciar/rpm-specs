%bcond_without check

%global goipath         github.com/vultr/govultr
Version:                0.1.4

%gometa

%global common_description %{expand:
The official Vultr Go client - GoVultr allows you to interact with the Vultr V1
API.}

%global golicenses      LICENSE
%global godocs          README.md CHANGELOG.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Vultr Go API client
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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Carl George <carl@george.computer> - 0.1.4-1
- Initial package rhbz#1747623
