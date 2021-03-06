# Generated by go2rpm
%bcond_without check

# https://github.com/git-lfs/gitobj
%global goipath         github.com/git-lfs/gitobj
Version:                1.4.1

%gometa

%global goaltipaths     github.com/git-lfs/gitobj/v2

%global common_description %{expand:
Package Gitobj reads and writes loose and packed Git objects.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Epoch:          1
Release:        1%{?dist}
Summary:        Read and write Git objects

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

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
* Sun Aug 02 23:33:36 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1:1.4.1-1
- Revert update

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 19:27:03 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.1-1
- Update to latest version

* Sun Aug 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-1
- Update to latest version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 20:22:35 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.0-1
- Release 1.3.0

* Mon Mar 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- Update to latest version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest version

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.0.0-2
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Thu Oct 11 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to first tagged version

* Wed Aug 29 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20180831git5aa0c18
- First package for Fedora
