# Generated by go2rpm 1
%bcond_without check

# https://github.com/bettercap/readline
%global goipath         github.com/bettercap/readline
Version:                1.4
%global commit          9cec905dd29109b64e6752507fba73474c2efd46

%gometa

%global common_description %{expand:
Readline is a pure go (golang) implementation for GNU-Readline kind library.}

%global golicenses      LICENSE
%global godocs          example doc README.md CHANGELOG.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Pure go implementation for GNU-Readline kind library

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/chzyer/readline)
BuildRequires:  golang(github.com/nbutton23/zxcvbn-go)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/chzyer/test)
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
* Sat Apr 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4-1.20200404git9cec905
- Initial package

