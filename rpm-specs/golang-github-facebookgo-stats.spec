# Generated by go2rpm
%bcond_without check

# https://github.com/facebookgo/stats
%global goipath         github.com/facebookgo/stats
%global commit          1b76add642e42c6ffba7211ad7b3939ce654526e

%gometa

%global common_description %{expand:
Package Stats defines a lightweight interface for collecting statistics. It
doesn't provide an implementation, just the shared interface.}

%global golicenses      license
%global godocs          readme.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Lightweight interface for collecting statistics

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 00:04:05 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190627git1b76add
- Initial package
