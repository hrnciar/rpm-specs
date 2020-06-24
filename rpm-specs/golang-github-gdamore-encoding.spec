# Generated by go2rpm
%bcond_without check

# https://github.com/gdamore/encoding
%global goipath         github.com/gdamore/encoding
Version:                1.0.0

%gometa
%global common_description %{expand:
Package encoding provides a number of encodings that are missing from the
standard Go encoding package.

We hope that we can contribute these to the standard Go library someday. It
turns out that some of these are useful for dealing with I/O streams coming
from non-UTF friendly sources.

The UTF8 Encoder is also useful for situations where valid UTF-8 might be
carried in streams that contain non-valid UTF; in particular I use it for
helping me cope with terminals that embed escape sequences in otherwise valid
UTF-8.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Various character map encodings missing from golang.org/x/net/encoding

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/text/encoding)
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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 14:28:51 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-3
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to first tagged release

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.5.gitb23993c
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitb23993c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.3.20180607gitb23993c
- Re-template against More Go Packaging guidelines

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20151215gitb23993c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20151215gitb23993c
- Add commit date to revision

* Fri Aug 18 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.gitb23993c
- Initial package for Fedora