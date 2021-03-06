# Generated by go2rpm 1
%bcond_without check

# https://github.com/antchfx/xpath
%global goipath         github.com/antchfx/xpath
Version:                1.1.10

%gometa

%global common_description %{expand:
XPath package for Golang, supported HTML, XML, JSON query.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        XPath package

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 17:27:54 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.10-1
- Update to 1.1.10

* Mon Apr 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.5-1
- Update to latest upstream stream release 1.1.5 (rhbz#1820852)

* Sat Apr 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.4-1
- Initial package
