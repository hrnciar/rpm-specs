# Generated by go2rpm
%bcond_without check

# https://github.com/kr/pretty
%global goipath         github.com/kr/pretty
Version:                0.2.1

%gometa

%global common_description %{expand:
Package pretty provides pretty-printing for go values. This is useful during
debugging, to avoid wrapping long output lines in the terminal.}

%global golicenses      License
%global godocs          Readme

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        1%{?dist}
Summary:        Pretty printing for go values

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/kr/text)

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
* Sun Aug 23 12:35:10 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.1-1
- Update to 0.2.1

* Tue Jul 28 20:23:58 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Update to 0.2.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 23:30:56 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-3
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1
- Release 0.1.0

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.19.20140811gitf31442d
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.gitf31442d variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.17.20140811gitf31442d
- Upload glide files

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.16.20140811gitf31442d
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.gitf31442d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Troy Dawson <tdawson@redhat.com> - 0-0.14.gitf31442d
- Cleanup spec file conditionals

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.gitf31442d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.gitf31442d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitf31442d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.gitf31442d
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.gitf31442d
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitf31442d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.7.gitf31442d
- Update to spec-2.1
  related: #1248169

* Mon Aug 17 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.gitf31442d
- Update sources and .gitiginore files
  related: #1248169

* Wed Jul 29 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.gitf31442d
- Update of spec file to spec-2.0
  resolves: #1248169

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.gitf31442d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 20 2014 jchaloup <jchaloup@redhat.com> - 0-0.3.git5feda8d
- Bump to f31442d60e51465c69811e2107ae978868dbea5c
- Choose the correct architecture

* Mon Sep 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.git
- don't redefine gopath
- preserve timestamps

* Wed Aug 06 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.1.git5feda8d
- First package for Fedora.

