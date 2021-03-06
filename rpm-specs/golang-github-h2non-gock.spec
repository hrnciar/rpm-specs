# Generated by go2rpm
%bcond_without check

# https://github.com/h2non/gock
%global goipath         github.com/h2non/gock
Version:                1.0.14

%gometa

%global common_description %{expand:
Versatile HTTP mocking made easy in Go for net/http stdlib package.}

%global golicenses      LICENSE
%global godocs          _examples History.md README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Expressive HTTP traffic mocking and testing made easy in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/h2non/parth)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/nbio/st)
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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 16:40:09 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.14-1
- Initial package
