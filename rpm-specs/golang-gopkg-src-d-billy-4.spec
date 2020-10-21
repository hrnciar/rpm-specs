# Generated by go2rpm
%bcond_without check

# https://github.com/src-d/go-billy
%global goipath         gopkg.in/src-d/go-billy.v4
%global forgeurl        https://github.com/src-d/go-billy
Version:                4.3.2

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-gopkg-src-d-billy-4-devel < 4.1.1-5
}

%global common_description %{expand:
The missing interface filesystem abstraction for Go. Billy implements an
interface based on the os standard library, allowing to develop applications
without dependency on the underlying storage. Makes it virtually free to
implement mocks and testing over filesystem operations.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Interface filesystem abstraction for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(gopkg.in/check.v1)

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.3.2-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.3.0-2
- Add Obsoletes for old name

* Sun Apr 28 14:27:24 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 4.3.0-1
- Release 4.3.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 4.1.1-3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 05 2018 Dominik Mierzejewski <dominik@greysector.net> - 4.1.1-1
- update to 4.1.1

* Tue Apr 03 2018 Dominik Mierzejewski <dominik@greysector.net> - 4.1.0-1
- First package for Fedora
