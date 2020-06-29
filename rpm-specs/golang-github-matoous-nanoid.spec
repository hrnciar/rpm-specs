# Generated by go2rpm 1
%bcond_without check

# https://github.com/matoous/go-nanoid
%global goipath         github.com/matoous/go-nanoid
Version:                1.4.1

%gometa

%global common_description %{expand:
Go implementation of ai's nanoid.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go implementation of ai's nanoid

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
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.1-1
- Update to latest upstream release 1.4.1

* Fri May 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Initial package
