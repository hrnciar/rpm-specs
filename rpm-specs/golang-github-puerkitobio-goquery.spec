# Generated by go2rpm
%bcond_without check

# https://github.com/PuerkitoBio/goquery
%global goipath         github.com/PuerkitoBio/goquery
Version:                1.5.1

%gometa

%global common_description %{expand:
Goquery brings a syntax and a set of features similar to jQuery to the Go
language. It is based on Go's net/html package and the CSS Selector library
cascadia. Since the net/html parser returns nodes, and not a full-featured DOM
tree, jQuery's stateful manipulation functions (like height(), css(), detach())
have been left off.}

%global golicenses      LICENSE
%global godocs          doc README.md

Name:           %{goname}
Release:        6%{?dist}
Summary:        Set of features similar to jQuery for the Go language

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
# Go 1.15: https://github.com/PuerkitoBio/goquery/issues/341
Patch0:         0001-Convert-int-to-string-using-fmt.Sprintf.patch

BuildRequires:  golang(github.com/andybalholm/cascadia)
BuildRequires:  golang(golang.org/x/net/html)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 31 23:46:36 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.5.1-1
- Update to 1.5.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.0-2
- Add Obsoletes for old name

* Thu May 16 00:03:34 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.5.0-1
- Release 1.5.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.1.0-1
- First package for Fedora
