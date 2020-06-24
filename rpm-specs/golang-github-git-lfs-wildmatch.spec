# Generated by go2rpm
%bcond_without check

# https://github.com/git-lfs/wildmatch
%global goipath         github.com/git-lfs/wildmatch
Version:                1.0.4

%gometa

%global common_description %{expand:
Package Wildmatch is a reimplementation of Git's wildmatch.c-style filepath
pattern matching.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Pattern matching language for filepaths compatible with Git

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.4-1
- Update to latest version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 22:20:12 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-3
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.2-1
- Update to latest version

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.0.0-2
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Wed Oct 10 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to first tagged version

* Wed Aug 15 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.3.20180816gitb31c344
- Re-template against More Go Packaging guidelines
- Update to latest commit

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20180219git8a05186
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 03 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20180219git8a05186
- Initial package
