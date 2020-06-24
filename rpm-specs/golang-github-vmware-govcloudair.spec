# Generated by go2rpm
%bcond_without check

# https://github.com/vmware/govcloudair
%global goipath         github.com/vmware/govcloudair
Version:                0.0.2
%global commit          daf883c2f1db1a1b08e3dc15b2a9f98c877a8d46

%gometa

%global common_description %{expand:
This package provides the govcloudair package which offers an interface to the
vCloud Air 5.6 and 5.7 API and vCloud Director 5.5 API.

It serves as a foundation for a project currently in development, there are
plans to make it a general purpose API in the future. The govcloudair package is
used by the Terraform provider for vCloud Director.

The API is currently under heavy development, its coverage is extremely limited
at the moment.

The bindings now support both Subscription and On-demand accounts and vCloud
Director 5.5.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        4%{?dist}
Summary:        VCloud Air API bindings for Golang

License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
# https://github.com/vmware/govcloudair/pull/41
Patch0:         0001-Fix-formatting-of-Fatalf-messages.patch

%if %{with check}
# Tests
BuildRequires:  golang(gopkg.in/check.v1)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 16:43:05 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.2-2.20190604gitdaf883c
- Update to new macros

* Sat Apr 06 14:54:31 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.2-1.20190406gitdaf883c
- Bump to commit daf883c2f1db1a1b08e3dc15b2a9f98c877a8d46 (#1695291)
- Update to new Go packaging

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git0d7be90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git0d7be90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git0d7be90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git0d7be90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git0d7be90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git0d7be90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git0d7be90
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git0d7be90
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git0d7be90
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 29 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git0d7be90
- Update of spec file to spec-2.0
  resolves: #1248147

* Thu Apr 16 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git0d7be90
- First package for Fedora
  resolves: #1214885
