# Generated by go2rpm
%bcond_without check

# https://github.com/zyedidia/tcell
%global goipath         github.com/zyedidia/tcell
Version:                1.4.10

%gometa

%global common_description %{expand:
Package Tcell provides a cell based view for text terminals, like xterm. It was
inspired by termbox, but differs from termbox in some important ways. It also
adds substantial functionality beyond termbox.}

%global golicenses      LICENSE
%global godocs          AUTHORS README.md TERMINALS.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Alternate terminal package

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gdamore/encoding)
BuildRequires:  golang(github.com/lucasb-eyer/go-colorful)
BuildRequires:  golang(github.com/mattn/go-runewidth)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/text/encoding)
BuildRequires:  golang(golang.org/x/text/encoding/charmap)
BuildRequires:  golang(golang.org/x/text/encoding/japanese)
BuildRequires:  golang(golang.org/x/text/encoding/korean)
BuildRequires:  golang(golang.org/x/text/encoding/simplifiedchinese)
BuildRequires:  golang(golang.org/x/text/encoding/traditionalchinese)
BuildRequires:  golang(golang.org/x/text/transform)

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
* Tue Aug 04 23:13:51 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.10-1
- Update to 1.4.10

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 19:36:44 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.8-1
- Update to 1.4.8 (#1837077)

* Thu Jun 18 19:53:04 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.7-1
- Update to 1.4.7

* Mon Feb 17 18:52:26 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.4-1
- Update to 1.4.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 18:25:43 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.8.20190602git5c58b4e
- Bump to commit

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git208b6e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.6.git208b6e8
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git208b6e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180314git208b6e8
- Fix BuildRequires

* Sat Mar 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180314git208b6e8
- Update with the new Go packaging
- Upstream GIT revision 208b6e8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20171129git869faf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20171129git869faf8
- Upstream GIT revision 869faf8

* Fri Sep 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170919git7095cc1
- First package for Fedora
