# Generated by go2rpm
%bcond_without check

# https://github.com/peterbourgon/diskv
%global goipath         github.com/peterbourgon/diskv
Version:                3.0.0

%gometa

%global common_description %{expand:
Diskv (disk-vee) is a simple, persistent key-value store written in the Go
language. It starts with an incredibly simple API for storing arbitrary data
on a filesystem by key, and builds several layers of performance-enhancing
abstraction on top. The end result is a conceptually simple, but highly
performant, disk-backed storage system.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Disk-backed key-value store

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/google/btree)

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 17:03:42 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.0-1
- Release 3.0.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.1-1
- First package for Fedora