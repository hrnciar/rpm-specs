# Generated by go2rpm
%bcond_without check

# https://github.com/nkovacs/streamquote
%global goipath         github.com/nkovacs/streamquote
Version:                1.0.0

%gometa

%global common_description %{expand:
This package provides a streaming version of strconv.Quote.

It allows you to quote the data in an io.Reader and write it out to an io.Writer
without having to store the entire input and the entire output in memory.

Its primary use case is go.rice and similar tools, which need to convert lots of
files, some of them quite large, to go strings.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Streaming version of strconv.Quote

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
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 23:32:23 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Initial package
