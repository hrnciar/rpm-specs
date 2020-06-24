# Generated by go2rpm
# Tests fail on ppc/aarch64
%ifnarch ppc64le aarch64
%bcond_without check
%endif

# https://github.com/zyedidia/poller
%global goipath         github.com/zyedidia/poller
Version:                2.0.0
%global commit          ab09682913b79f402713d1df1977dedc19eb25ac

%gometa

%global common_description %{expand:
Package Poller is a file-descriptor multiplexer.}

%global golicenses      LICENSE.txt
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Epoll(7)-based file-descriptor multiplexer

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep
find . -name "*.go" -exec sed -i "s|github.com/npat-efault/poller|github.com/zyedidia/poller|" "{}" +;


%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 19:50:34 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.0-1.20180314gitab09682
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20180314gitab09682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.5.20180314gitab09682
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20180314gitab09682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180314gitab09682
- Update with the new Go packaging

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170616gitab09682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170616gitab09682
- First package for Fedora
