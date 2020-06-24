# Generated by go2rpm
# Needs a redis-server
%bcond_with check

# https://github.com/gomodule/redigo
%global goipath         github.com/gomodule/redigo
Version:                1.7.0

%gometa

%global goaltipaths     github.com/garyburd/redigo

%global common_description %{expand:
Redigo is a Go client for the Redis database.

Features:
 - A Print-like API with support for all Redis commands.
 - Pipelining, including pipelined transactions.
 - Publish/Subscribe.
 - Connection pooling.
 - Script helper type with optimistic use of EVALSHA.
 - Helper functions for working with command replies.}

%gometa

%global golicenses      LICENSE
%global godocs          README.markdown

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
# Upstream yanked 2.0
Epoch:          1
Release:        5%{?dist}
Summary:        Go client for redis

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 00:17:08 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1:1.7.0-3
- Release 1.7.0

* Thu Nov 01 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.0-1
- Release 2.0.0

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.15.git3e4727f
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git3e4727f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.git3e4727f
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.20150520git3e4727f
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git3e4727f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git3e4727f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git3e4727f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git3e4727f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git3e4727f
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git3e4727f
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git3e4727f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git3e4727f
- Update to spec-2.1
  resolves: #1248994

* Fri Jul 31 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git3e4727f
- Update spec file to spec-2.0
  resolves: #1248994

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git3e4727f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git3e4727f
- First package for Fedora
  resolves: #1228795
