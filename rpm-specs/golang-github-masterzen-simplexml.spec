# Generated by go2rpm 1
%bcond_without check

# https://github.com/masterzen/simplexml
%global goipath         github.com/masterzen/simplexml
%global commit          31eea30827864c9ab643aa5a0d5b2d4988ec8409

%gometa

%global common_description %{expand:
Go library to generate XML content from a naive DOM.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Go library to generate XML content from a naive DOM

License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
%endif

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
* Mon Apr 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200406git31eea30
- Initial package
