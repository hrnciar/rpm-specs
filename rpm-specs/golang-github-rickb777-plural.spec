# Generated by go2rpm 1
%bcond_without check

# https://github.com/rickb777/plural
%global goipath         github.com/rickb777/plural
Version:                1.2.2

%gometa

%global common_description %{expand:
Simple Go API for pluralisation.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple Go API for pluralisation

# Upstream license specification: BSD-3-Clause
License:        BSD
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
* Thu Oct  8 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Sun Sep 20 23:08:32 CST 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.2.1-1
- Initial package

