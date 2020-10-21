# Generated by go2rpm
%bcond_without check

# https://github.com/hashicorp/consul-migrate
%global goipath         github.com/hashicorp/consul-migrate
Version:                0.1.0
%global commit          678fb10cdeae25ab309e99e655148f0bf65f9710

%gometa

%global common_description %{expand:
Consul-migrate is a Go package and CLI utility to perform a very specific data
migration for Consul servers nodes. Between Consul versions 0.5.0 and 0.5.1, the
backend for storing Raft data was changed from LMDB to BoltDB. To support
seamless upgrades, this library is embedded in Consul version 0.5.1 to perform
the upgrade automatically.}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Release:        5%{?dist}
Summary:        Consul server data migrator

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/hashicorp/raft)
BuildRequires:  golang(github.com/hashicorp/raft-boltdb)
BuildRequires:  golang(github.com/hashicorp/raft-mdb)

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .

%build
%gobuild -o %{gobuilddir}/bin/consul-migrate %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck -d migrator
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 21:32:31 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1.20190602git678fb10
- Release 0.1.0, commit 678fb10cdeae25ab309e99e655148f0bf65f9710

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.git4977886
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.14.git4977886
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git4977886
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.git4977886
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.20150411git4977886
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git4977886
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git4977886
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git4977886
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git4977886
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git4977886
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git4977886
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git4977886
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git4977886
- Update to spec-2.1
  related: #1250462

* Wed Aug 05 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.git4977886
- Update spec file to spec-2.0
  resolves: #1250462

* Thu Apr 16 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git4977886
- First package for Fedora
  resolves: #1212350
