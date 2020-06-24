# Generated by go2rpm
# https://github.com/szferi/gomdb/issues/40
%bcond_with check

# https://github.com/armon/gomdb
%global goipath         github.com/armon/gomdb
%global commit          75f545a47e8956a9f84de7d95fafb003dc916831

%gometa

%global godevelheader %{expand:
Requires:       pkgconfig(lmdb)}

%global common_description %{expand:
Go wrapper for OpenLDAP Lightning Memory-Mapped Database (LMDB).}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Version:        0
Release:        0.20%{?dist}
Summary:        Go wrapper for LMDB: OpenLDAP Lightning Memory-Mapped Database

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml
Patch0:         use-system-lmdb.patch

BuildRequires:  pkgconfig(lmdb)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1
cp %{S:1} %{S:2} .

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 13:15:54 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.18.20181112git75f545a
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.git75f545a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.17.20181112git75f545a
- Bump to commit 75f545a47e8956a9f84de7d95fafb003dc916831

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.15.git.git151f2e0
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git.git151f2e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.git.git151f2e0
- Update to spec 3.0
  Upload glide.lock and glide.yaml

* Mon Feb 26 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.20150106git151f2e0
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git151f2e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git151f2e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git151f2e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git151f2e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git151f2e0
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git151f2e0
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git151f2e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git151f2e0
- Update to spec-2.1
  related: #1248536

* Thu Jul 30 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.3.git151f2e0
- Update of spec file to spec-2.0
  resolves: #1248536

* Sat Jun 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git151f2e0
- Add missing runtime dependency on lmdb-devel
  related: #1212046

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git151f2e0
- First package for Fedora
  resolves: #1212046
