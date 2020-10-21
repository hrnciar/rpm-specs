# Generated by go2rpm
%bcond_without check

# https://github.com/pkg/errors
%global goipath         github.com/pkg/errors
Version:                0.9.1

%gometa

%global common_description %{expand:
Package Errors provides simple error handling primitives.}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        2%{?dist}
Summary:        Simple error handling primitives

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 22:25:23 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.9.1-1
- Update to 0.9.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 03:38:35 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.1-5
- Update to new macros

* Mon Feb 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.1-4
- Backport patches to fix Go 1.12

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.1-3
- Attach scriptlet to the correct subpackage

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.1-2
- Add scriplet to fixup accidental glide.lock directory

* Sat Feb 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.1-1
- Update to latest version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-0.5.git645ef00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org>
- 0.8.0-0.4
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-0.3.git645ef00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Jan Chaloupka <jchaloup@redhat.com>
- Upload glide files

* Sat Mar 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.8.0-0.1.git645ef00
- It's actually v0.8.0
  resolves: #1504175

* Sat Mar 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.7.1-0.8.git645ef00
- Bump to 645ef00459ed84a119197bfb8d8205042c6df63d

* Sat Mar 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.7.1-0.7.gita887431
- Update to spec 3.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.6.gita887431
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.5.gita887431
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.4.gita887431
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.3.gita887431
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Jan Chaloupka <jchaloup@redhat.com> - 0.7.1-0.2.gita887431
- Extend the default architectures, consolidate with_ macros
  related: #1387115

* Thu Oct 20 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.gita887431
- First package for Fedora
  resolves: #1387115
