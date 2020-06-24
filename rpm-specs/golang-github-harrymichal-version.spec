%bcond_without check

# https://github.com/HarryMichal/go-version
%global goipath         github.com/HarryMichal/go-version
Version:                1.0.1

%gometa

%global common_description %{expand:
Version normalizer and comparison library for Go}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Version normalizer and comparison library for Go

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
* Sat Jun 20 2020 Ondřej Míchal <harrymichal@seznam.cz> - 1.0.1-1
- Update to version 1.0.1

* Wed May 27 2020 Harry Míchal <harrymichal@seznam.cz> - 1.0.0-1
- Add 1.0.0 release

