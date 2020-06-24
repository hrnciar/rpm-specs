# Generated by go2rpm 1
%bcond_without check

# https://github.com/andygrunwald/go-gerrit
%global goipath         github.com/andygrunwald/go-gerrit
Version:                0.5.2
%global tag             0.5.2
%global commit          3f5e365ccf57c158d081f41b71847795b8b8a9a8

%gometa

%global common_description %{expand:
Go(lang) client/library for Gerrit Code Review.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go(lang) client/library for Gerrit Code Review

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/google/go-querystring/query)

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
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 28 15:59:19 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.2-1.20191228git3f5e365
- Initial package
