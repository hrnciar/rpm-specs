# Generated by go2rpm
%bcond_without check

# https://github.com/sendgrid/sendgrid-go
%global goipath         github.com/sendgrid/sendgrid-go
Version:                3.4.1
%global commit          df2105ec04e32aff6b9e9a2fd1ca8e5c16a836c5

%gometa

%global common_description %{expand:
This library allows you to quickly and easily use the SendGrid Web API v3 via
Go.}

%global golicenses      LICENSE.txt
%global godocs          examples CHANGELOG.md CODE_OF_CONDUCT.md\\\
                        CONTRIBUTING.md README.md TROUBLESHOOTING.md USAGE.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Official SendGrid Led, Community Driven Golang API Library

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# Fix Sprintf format for p.To, p.CC and p.BCC
Patch0:         0001-Fix-Sprintf-format-for-p.To-p.CC-and-p.BCC.patch

BuildRequires:  golang(github.com/sendgrid/rest)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
# .: needs network
%gocheck -d .
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 19:12:05 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.4.1-1.20190703gitdf2105e
- Initial package