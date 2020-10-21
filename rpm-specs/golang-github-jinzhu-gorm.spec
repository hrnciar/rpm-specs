# Generated by go2rpm
%bcond_without check

# https://github.com/jinzhu/gorm
%global goipath         github.com/jinzhu/gorm
Version:                1.9.15

%gometa

%global common_description %{expand:
The fantastic ORM library for Golang, aims to be developer friendly.}

%global golicenses      License
%global godocs          README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Release:        1%{?dist}
Summary:        The fantastic ORM library for Golang, aims to be developer friendly

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/denisenkom/go-mssqldb)
BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/jinzhu/inflection)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/lib/pq/hstore)
BuildRequires:  golang(github.com/mattn/go-sqlite3)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/erikstmartin/go-testdb)
BuildRequires:  golang(github.com/jinzhu/now)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jul 28 14:38:33 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.9.15-1
- Update to 1.9.15

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 18:48:35 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.9.8-1
- Release 1.9.8

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git82d726b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.13.git82d726b
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git82d726b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.git82d726b
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.20150721git82d726b
- Autogenerate some parts using the new macros

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.git82d726b
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git82d726b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git82d726b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git82d726b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git82d726b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git82d726b
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git82d726b
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git82d726b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git82d726b
- First package for Fedora
  resolves: #1270050
