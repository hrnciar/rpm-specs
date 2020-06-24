# Generated by go2rpm
%bcond_without check

# https://github.com/mjibson/appstats
%global goipath         github.com/mjibson/appstats
%global commit          0542d5f0e87ea3a8fa4174322b9532f5d04f9fa8

%gometa

%global common_description %{expand:
Package appstats profiles the RPC performance of Google App Engine
applications.}

%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Profile the RPC performance of Google App Engine applications

# Archived, can't add license file.
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(google.golang.org/appengine)
BuildRequires:  golang(google.golang.org/appengine/log)
BuildRequires:  golang(google.golang.org/appengine/memcache)
BuildRequires:  golang(google.golang.org/appengine/user)

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 22:40:50 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190629git0542d5f
- Initial package
