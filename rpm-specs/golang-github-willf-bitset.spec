# Generated by go2rpm
%bcond_without check

# https://github.com/willf/bitset
%global goipath         github.com/willf/bitset
Version:                1.1.11

%gometa

%global common_description %{expand:
Package bitset implements bitsets, a mapping between non-negative integers and
boolean values. It should be more efficient than map[uint] bool.

It provides methods for setting, clearing, flipping, and testing individual
integers.

But it also provides set intersection, union, difference, complement, and
symmetric operations, as well as tests to check whether any, all, or no bits are
set, and querying a bitset's current length and number of positive bits.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go package implementing bitsets

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
* Wed Aug 12 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.11-1
- Update to latest version (#1868189)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 23:40:28 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.10-2
- Update to new macros

* Tue Feb 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.10-1
- Update to latest version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.1.9-2
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Wed Oct 10 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.9-1
- Update to latest version

* Wed Aug 15 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.4-2
- rebuilt

* Sun Aug 12 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.4-1
- First package for Fedora
