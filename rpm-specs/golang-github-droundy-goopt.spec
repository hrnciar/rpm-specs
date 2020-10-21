%bcond_without check

# https://github.com/droundy/goopt
%global goipath         github.com/droundy/goopt
%global commit          0b8effe182da161d81b011aba271507324ecb7ab

%gometa

%global common_description %{expand:
Getopt-like flags package for Go.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Getopt-like flags package for Go

# Upstream license specification: BSD-2-Clause
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
* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 0-0.4
- Update summary and description for clarity and consistency

* Tue Jul 28 2020 Brandon Perkins <bperkins@redhat.com> - 0-0.3.20200728git0b8effe
- Update to release 3 of git commit 0b8effe (#1811180)
- Enable check stage
- Clean changelog

* Fri Mar 06 2020 Brandon Perkins <bperkins@redhat.com> - 0-0.2.20200304git0b8effe
- Remove build of test-program binary example as this is a devel only package

* Fri Nov 22 2019 Brandon Perkins <bperkins@redhat.com> - 0-0.1.20191122git0b8effe
- Initial package

