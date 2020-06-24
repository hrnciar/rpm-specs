# Generated by go2rpm
# Needs network
%bcond_with check

# https://github.com/revel/revel
%global goipath         github.com/revel/revel
Version:                0.21.0

%gometa

%global common_description %{expand:
A high productivity, full-stack web framework for the Go language.}

%global golicenses      LICENSE
%global godocs          AUTHORS CHANGELOG.md CONTRIBUTING.md README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        High productivity, full-stack web framework for the Go language

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/bradfitz/gomemcache/memcache)
BuildRequires:  golang(github.com/garyburd/redigo/redis)
BuildRequires:  golang(github.com/mattn/go-colorable)
BuildRequires:  golang(github.com/patrickmn/go-cache)
BuildRequires:  golang(github.com/revel/config)
BuildRequires:  golang(github.com/revel/log15)
BuildRequires:  golang(github.com/revel/pathtree)
BuildRequires:  golang(github.com/twinj/uuid)
BuildRequires:  golang(github.com/xeonx/timeago)
BuildRequires:  golang(golang.org/x/net/websocket)
BuildRequires:  golang(gopkg.in/fsnotify/fsnotify.v1)
BuildRequires:  golang(gopkg.in/natefinch/lumberjack.v2)
BuildRequires:  golang(gopkg.in/stack.v0)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 18:41:15 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.21.0-1
- Initial package
