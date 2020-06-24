# Generated by go2rpm
%bcond_without check

# https://github.com/Masterminds/semver
%global goipath         github.com/Masterminds/semver
Version:                1.4.2
%global commit          059deebd1619b9ae33232c797f7ab0e8d6c6fd69

%gometa

# Remove in F33
%global godevelheader %{expand:
Obsoletes:      golang-github-Masterminds-semver-devel < 1.4.2-2
}

%global goname          golang-github-masterminds-semver-1
%global godevelname     golang-github-masterminds-semver-1-devel

%global common_description %{expand:
The Semver package provides the ability to work with Semantic Versions in Go.
Specifically it provides the ability to:

 - Parse semantic versions
 - Sort semantic versions
 - Check if a semantic version fits within a set of constraints
 - Optionally work with a v prefix}

%global golicenses      LICENSE.txt
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Work with Semantic Versions in Go

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.2-3.20190604git059deeb
- Add Obsoletes for old name

* Tue Jun 04 16:07:38 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.2-2.20190604git059deeb
- Bump to commit 059deebd1619b9ae33232c797f7ab0e8d6c6fd69

* Wed Apr 03 01:23:25 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.2-1
- Release 1.4.2
