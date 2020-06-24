%global commit a93a0a55a24912e113e21f81971dc7248de7f6e2
%global shortcommit a93a0a5

# https://github.com/acobaugh/osrelease
%global goipath         github.com/acobaugh/osrelease
Version:                0.0.0

%gometa

%global common_description %{expand:
Golang package to read and parse /etc/os-release}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang package to read and parse /etc/os-release

License:        BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/osrelease-%{commit}.tar.gz

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%check
%gocheck

%gopkgfiles

%changelog
* Mon Jun 1 2020 Harry Míchal <harrymichal@seznam.cz> - 0.0.1-1
- Add initial release

