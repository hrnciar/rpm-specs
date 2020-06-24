%bcond_without check

%global goipath         github.com/go-test/deep
Version:                1.0.3

%gometa

%global common_description %{expand:
Golang deep variable equality test that returns human-readable differences.}

%global golicenses      LICENSE
%global godocs          README.md CHANGES.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Golang deep variable equality test
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description %{common_description}

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 01 2019 Carl George <carl@george.computer> - 1.0.3-1
- Initial package rhbz#1747843
