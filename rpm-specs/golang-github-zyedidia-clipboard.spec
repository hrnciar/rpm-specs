# Generated by go2rpm
%bcond_without check

# https://github.com/zyedidia/clipboard
%global goipath         github.com/zyedidia/clipboard
Version:                1.0.3

%gometa

%global common_description %{expand:
Clipboard for golang.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Clipboard for golang

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

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
* Tue Aug 04 23:03:08 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.3-
- Update to 1.0.3

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 19:47:19 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.10.20200718git7c45b86
- Bump to commit 7c45b8673834045ddc6dd553fcb65f3bf4224119

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 17 13:19:04 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.7.20190417gitbd31d74
- Bump to commit bd31d747117d04b4e25b61f73e1ea4faeea3c56a

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git4611e80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.5.git4611e80
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git4611e80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180314git4611e80
- Update with the new Go packaging
- Upstream GIT revision 4611e80

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20161226gitadacf41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20161226gitadacf41
- First package for Fedora
