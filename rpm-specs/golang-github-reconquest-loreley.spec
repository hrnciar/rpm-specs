# Generated by go2rpm 1
%bcond_without check

# https://github.com/reconquest/loreley
%global goipath         github.com/reconquest/loreley
%global commit          621c1cd37fd1081c0b81b1923444df2d9d4775ff

%gometa

%global common_description %{expand:
Simple and extensible colorizer for programs' output.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Simple and extensible colorizer for programs' output

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)

%if %{with check}
# Tests
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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.2.20200714git621c1cd
- Update to latest commit (rhbz#1840713)

* Wed May 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200527git9e95b93
- Initial package

