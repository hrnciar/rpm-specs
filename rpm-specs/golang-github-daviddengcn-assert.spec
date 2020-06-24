# Generated by go2rpm
%bcond_without check

# https://github.com/daviddengcn/go-assert
%global goipath         github.com/daviddengcn/go-assert
%global commit          ba7e68aeeff6e81e6a7699c9e603d342e4b2b919

%gometa

%global common_description %{expand:
Testing utils for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Testing utils for Go

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/daviddengcn/go-algs/ed)
BuildRequires:  golang(github.com/daviddengcn/go-villa)

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
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 21:37:24 EDT 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20190711gitba7e68a
- Initial package