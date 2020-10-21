# Generated by go2rpm
%bcond_without check

# https://github.com/codahale/hdrhistogram
%global goipath         github.com/codahale/hdrhistogram
%global commit          3a0bb77429bd3a61596f5e8a3172445844342120

%gometa

%global common_description %{expand:
Package Hdrhistogram provides an implementation of Gil Tene's HDR Histogram data
structure. The HDR Histogram allows for fast and accurate analysis of the
extreme ranges of data with non-normal distributions, like latency.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Pure Go implementation of Gil Tene's HDR Histogram

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 15:35:28 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20190318git3a0bb77
- Update to new macros

* Mon Mar 18 2019 Nathan Scott <nathans@redhat.com> - 0-0.1.20190318git3a0bb77
- First package for Fedora
