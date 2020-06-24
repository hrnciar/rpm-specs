# Generated by go2rpm
%bcond_without check

# https://github.com/eapache/go-xerial-snappy
%global goipath         github.com/eapache/go-xerial-snappy
%global commit          776d5712da21bc4762676d614db1d8a64f4238b0

%gometa

%global common_description %{expand:
Xerial-compatible Snappy framing support for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Xerial-compatible Snappy framing support for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/snappy)

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 18:54:21 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20190408git776d571
- Update to new macros

* Mon Apr 08 19:47:08 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190408git776d571
- First package for Fedora