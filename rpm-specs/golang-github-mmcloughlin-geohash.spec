%bcond_without check

# https://github.com/mmcloughlin/geohash
%global goipath         github.com/mmcloughlin/geohash
Version:                0.10.0

%gometa

%global common_description %{expand:
Go geohash library offering encoding and decoding for string and integer
geohashes.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
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
* Wed Jul 29 23:08:09 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.10.0-1
- Update to 0.10.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 28 2019 Carl George <carl@george.computer> - 0.9.0-1
- Initial package rhbz#1746215
