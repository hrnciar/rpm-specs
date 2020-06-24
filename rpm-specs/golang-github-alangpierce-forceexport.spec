# Generated by go2rpm 1
%ifnarch s390x
%bcond_without check
%endif

# https://github.com/alangpierce/go-forceexport
%global goipath         github.com/alangpierce/go-forceexport
%global commit          8f1d6941cd755b975763ddb1f836561edddac2b8

%gometa

%global common_description %{expand:
Go-forceexport is a golang package that allows access to any module-level
function, even ones that are not exported. You give it the string name of a
function , like "time.now", and gives you a function value that calls that
function. More generally, it can be used to achieve something like reflection on
top-level functions, whereas the reflect package only lets you access methods by
name.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Access unexported functions from other packages

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# Minor syntax errors in test
Patch0:         https://patch-diff.githubusercontent.com/raw/alangpierce/go-forceexport/pull/3.patch#/0001-Minor-syntax-errors-in-test.patch
# Fixes the edge case
Patch1:         https://patch-diff.githubusercontent.com/raw/alangpierce/go-forceexport/pull/4.patch#/0001-Fixes-the-edge-case.patch

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1
%patch1 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Mar 04 17:20:04 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20200304git8f1d694
- Initial package