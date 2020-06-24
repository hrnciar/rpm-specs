# Generated by go2rpm
%bcond_without check

# https://github.com/cloudfoundry/bytefmt
%global goipath         code.cloudfoundry.org/bytefmt
%global forgeurl        https://github.com/cloudfoundry/bytefmt
%global commit          854d396b647c90b5a45646f9dcc2c9cd08ea8d51

%gometa

%global common_description %{expand:
Human readable byte formatter.}

%global golicenses      LICENSE NOTICE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Human readable byte formatter

# Upstream license specification: Apache-2.0
License:        ASL 2.0
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
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 28 17:53:37 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20191228git854d396
- Bump to commit 854d396b647c90b5a45646f9dcc2c9cd08ea8d51

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 00:12:35 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190623git2aa6f33
- Initial package
