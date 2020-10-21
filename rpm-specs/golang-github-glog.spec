# Generated by go2rpm
%bcond_without check

# https://github.com/golang/glog
%global goipath         github.com/golang/glog
%global commit          23def4e6c14b4da8ac2ed8007337bc5eb5007998

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-golang-glog-devel < 0-0.24
}

%global common_description %{expand:
This is an efficient pure Go implementation of leveled logs in the
manner of the open source C++ package.

By binding methods to booleans it is possible to use the log package
without paying the expense of evaluating the arguments to the log.
Through the -vmodule flag, the package also provides fine-grained
control over logging at the file level.}

%global golicenses      LICENSE
%global godocs          README

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Version:        0
Release:        0.29%{?dist}
Summary:        Leveled execution logs for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
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
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.25.20181110git23def4e
- Add Obsoletes for old name

* Tue Apr 23 09:19:20 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.24.20181110git23def4e
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.git23def4e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.22.20181110git23def4e
- Bump to commit 23def4e6c14b4da8ac2ed8007337bc5eb5007998

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.21.gitfca8c88
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.gitfca8c88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 10 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.19.gitfca8c88
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.18.20150801gitfca8c88
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.gitfca8c88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.gitfca8c88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.gitfca8c88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.gitfca8c88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.gitfca8c88
- Polish the spec file
  related: #1249052

* Thu Sep 15 2016 jchaloup <jchaloup@redhat.com> - 0-0.12.gitfca8c88
- Enable devel and unit-test packages for epel7
  related: #1249052

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.gitfca8c88
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Apr 18 2016 jchaloup <jchaloup@redhat.com> - 0-0.10.gitfca8c88
- Bump to upstream fca8c8854093a154ff1eb580aae10276ad6b1b5f
  related: #1249052

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.git44145f0
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git44145f0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.7.git44145f0
- Update to spec-2.1
  related: #1249052

* Fri Jul 31 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.git44145f0
- Update spec file to spec-2.0
  resolves: #1249052

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git44145f0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 09 2014 jchaloup <jchaloup@redhat.com> - 0-0.4.git44145f0
- Bump to upstream 44145f04b68cf362d9c4df2182967c2275eaefed
  resolves: #1161627
- Choose the correct architecture

* Mon Sep 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.2.gitd1c4472
- BR golang
- include check

* Tue Aug 05 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.0.1.gitd1c4472b
- First package for Fedora
