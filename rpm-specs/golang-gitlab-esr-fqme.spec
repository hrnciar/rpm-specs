# Generated by go2rpm
%bcond_without check

# https://gitlab.com/esr/fqme
%global goipath         gitlab.com/esr/fqme
%global forgeurl        https://gitlab.com/esr/fqme

Version:                0.1.0
%global tag             v%{version}

%gometa

%global common_description %{expand:
Fqme is Fully Qualified Me, a Go module that mines configuration files to
discover your full name and email address.}

%global golicenses      LICENSE
%global godocs          README.adoc

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go module that mines configuration files to discover full name and email address

License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep
rm -rf demo

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Thu Jun 18 2020 Denis Fateyev <denis@fateyev.com> - 0.1.0-1
- Initial Fedora RPM package
