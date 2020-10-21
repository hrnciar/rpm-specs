# Generated by go2rpm 1
%bcond_without check

# https://github.com/urfave/cli
%global goipath         github.com/urfave/cli/v2
Version:                2.2.0

%gometa

%global common_description %{expand:
A simple, fast, and fun package for building command line apps in Go.}

%global golicenses      LICENSE
%global godocs          docs/v2 CODE_OF_CONDUCT.md README.md

Name:           %{goname}
Release:        4%{?dist}
Summary:        A simple, fast, and fun package for building command line apps in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}


BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/cpuguy83/go-md2man/v2/md2man)
BuildRequires:  golang(gopkg.in/yaml.v2)

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
* Mon Aug 03 22:09:26 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.0-4
- Fix import path for md2man

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 24 19:50:42 CEST 2020 Andreas Gerstmayr <agerstmayr@redhat.com> - 2.2.0-2
- Patch dependency import path in docs.go to use
  golang-github-cpuguy83-md2man-devel >= 2.0.0 (credits to Fabian Affolter)

* Thu Apr 23 20:13:44 CEST 2020 Andreas Gerstmayr <agerstmayr@redhat.com> - 2.2.0-1
- Initial package

