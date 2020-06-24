# Generated by go2rpm
%bcond_without check

# https://github.com/rainycape/unidecode
%global goipath         github.com/rainycape/unidecode
%global commit          cb7f23ec59bec0d61b19c56cd88cee3d0cc1870c

%gometa

%global common_description %{expand:
Unicode transliterator in Golang: replaces non-ASCII characters with their
ASCII approximations.}

%global golicenses      LICENSE
%global godocs          README.md table.txt

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Unicode transliterator in Golang

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 17:44:33 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20190315gitcb7f23e
- Update to new macros

* Fri Mar 15 2019 Nathan Scott <nathans@redhat.com> - 0-0.1.20190315gitcb7f23e
- First package for Fedora
