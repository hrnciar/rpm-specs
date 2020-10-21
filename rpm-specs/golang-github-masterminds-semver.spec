# Generated by go2rpm
%bcond_without check

# https://github.com/Masterminds/semver
%global goipath         github.com/Masterminds/semver
Version:                3.1.0

%gometa

%global goaltipaths     github.com/Masterminds/semver/v3

%global common_description %{expand:
The semver package provides the ability to work with Semantic Versions in Go.
Specifically it provides the ability to:

 - Parse semantic versions
 - Sort semantic versions
 - Check if a semantic version fits within a set of constraints
 - Optionally work with a v prefix}

%global golicenses      LICENSE.txt
%global godocs          CHANGELOG.md README.md

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        1%{?dist}
Summary:        Work with semantic versions in Go

License:        MIT
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
* Wed Jul 29 19:11:03 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.1.0-1
- Update to 3.1.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 23:46:22 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.3-1
- Update to 3.0.3

* Tue Dec 03 22:39:13 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.0-0.6.20190807git3c92f33
- Add Conflicts with v1 (#1766884)

* Wed Aug 07 18:03:01 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.0-0.5.20190807git3c92f33
- Pre-release 2.0.0, bump to commit 3c92f33da7a84de8314f3ff82e5f919b89fd1492

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.0-0.3.20190425git353fa92
- Add Obsoletes for old name

* Thu Apr 25 15:53:37 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.0-0.2.20190425git353fa92
- Pre-release 2.0.0, bump to commit 353fa929e66ea3d8adcc58cd040e12d65c47264e

* Tue Mar 19 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.0-0.1.20190319git3c92f33
- Pre-release 2.0.0, bump to commit 3c92f33da7a84de8314f3ff82e5f919b89fd1492

* Tue Mar 19 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.2-1
- Release 1.4.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-0.10.git8d04313
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org>  - 1.1.1-0.9.git8d04313
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-0.8.git8d04313
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.1.1-0.7.git8d04313
- Upload glide files

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.1.1-0.6.20160630git8d04313
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-0.5.git8d04313
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-0.4.git8d04313
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-0.3.git8d04313
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-0.2.git8d04313
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.git8d04313
- First package for Fedora
  resolves: #1373551
