# Generated by go2rpm
%bcond_without check

# https://github.com/justinas/alice
%global goipath         github.com/justinas/alice
%global commit          03f45bd4b7dad4734bc4620e46a35789349abb20

%gometa

%global common_description %{expand:
Alice provides a convenient way to chain your HTTP middleware functions and the
app handler.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        Painless middleware chaining for Go

License:        MIT
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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 17:51:26 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20171023git03f45bd
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20171023git03f45bd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20171023git03f45bd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Kaushal <kshlmster@gmail.com> - 0-0.1.20171023git03f45bd
- First package for Fedora