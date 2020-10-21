# Generated by go2rpm 1
%bcond_without check

# https://github.com/piprate/json-gold
%global goipath         github.com/piprate/json-gold
Version:                0.3.0

%gometa

%global common_description %{expand:
A JSON-LD processor for Go.}

%global golicenses      LICENSE
%global godocs          examples CONTRIBUTORS.md README.md CHANGELOG.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        JSON-LD processor

License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/pquerna/cachecontrol)

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- Initial package

