%bcond_without check

%global goipath         github.com/mmcloughlin/geohash
Version:                0.9.0

%gometa

%global common_description %{expand:
Go geohash library offering encoding and decoding for string and integer
geohashes.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Golang geohash library
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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 28 2019 Carl George <carl@george.computer> - 0.9.0-1
- Initial package rhbz#1746215
