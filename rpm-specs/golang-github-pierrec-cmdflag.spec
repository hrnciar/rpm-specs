# Generated by go2rpm 1
%bcond_without check

# https://github.com/pierrec/cmdflag
%global goipath         github.com/pierrec/cmdflag
Version:                0.0.2

%gometa

%global common_description %{expand:
Building on top of the excellent flag package from the standard library, cmdflag
adds a simple way of specifying nested commands. Its intent is to blend with the
usage of flag by keeping its idioms and simply augment it with commands.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Augment the flag package with commands

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/xo/dburl)

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 15:49:19 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.2-1
- Initial package
