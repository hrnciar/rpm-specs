# Generated by go2rpm 1
# There is an issue with some tests
%bcond_with check

# https://github.com/reconquest/barely
%global goipath         github.com/reconquest/barely
%global commit          0f12e3bb2e13b4cdba2a41b604187163a861e087

%gometa

%global common_description %{expand:
Simple and extensible status bar to pretty display of Golang program's
progress.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Status bar to pretty display of Golang program's progress

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/reconquest/loreley)
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200527git0f12e3b
- Initial package for Fedora
