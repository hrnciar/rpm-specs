%bcond_without check

# https://github.com/go-test/deep
%global goipath         github.com/go-test/deep
Version:                1.0.7

%gometa

%global common_description %{expand:
Golang deep variable equality test that returns human-readable differences.}

%global golicenses      LICENSE
%global godocs          README.md CHANGES.md

Name:           %{goname}
Release:        1%{?dist}
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
* Mon Aug 03 15:37:19 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.7-1
- Update to 1.0.7

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 01 2019 Carl George <carl@george.computer> - 1.0.3-1
- Initial package rhbz#1747843
