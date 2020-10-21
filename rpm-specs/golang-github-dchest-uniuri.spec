# Generated by go2rpm 1
%bcond_without check

# https://github.com/dchest/uniuri
%global goipath         github.com/dchest/uniuri
%global commit          7aecb25e1fe5a22533fab90a637a8f74a9cf7340

%gometa

%global common_description %{expand:
Go package uniuri generates random strings good for use in URIs to identify
unique objects.}

%global golicenses      COPYING
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Go package to generate random strings for use in URIs

License:        CC0
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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 21:09:42 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20200725git7aecb25
- Bump to commit 7aecb25e1fe5a22533fab90a637a8f74a9cf7340

* Fri Feb 07 16:45:41 CET 2020 Andreas Gerstmayr <agerstmayr@redhat.com> - 0-0.1.20200207git8902c56
- Initial package
