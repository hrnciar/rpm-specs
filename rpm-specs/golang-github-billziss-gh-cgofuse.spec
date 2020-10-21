# Generated by go2rpm
# Deactivating test: tests depends on fuse being present and fuse.ko being
# loaded but the chroot doesn't allow to insert module.
%bcond_with check

# https://github.com/billziss-gh/cgofuse
%global goipath         github.com/billziss-gh/cgofuse
Version:                1.4.0

%gometa

%global common_description %{expand:
Cgofuse is a cross-platform FUSE library for Go. It is supported on multiple
platforms and can be ported to any platform that has a FUSE implementation. It
has cgo and !cgo ("nocgo") variants depending on the platform.}

%global golicenses      License.txt
%global godocs          examples Changelog.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Cross-platform FUSE library for Go

License:        MIT
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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 13:52:13 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.0-1
- Update to 1.4.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 14:46:35 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-6.20190524gitdd0c76f
- Bump to commit dd0c76f07d34a74e62f4dd700ebe09a44925900c

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-4
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.1.0-3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-1
- Upstream release 1.1.0

* Thu Mar 08 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.4-2
- Update with the new Go packaging

* Thu Dec 07 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.4-1
- Upstream release 1.0.4

* Mon Jul 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-1
- First package for Fedora
