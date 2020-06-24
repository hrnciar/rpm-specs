# Generated by go2rpm
%bcond_without check

# https://github.com/google/gopacket
%global goipath         github.com/google/gopacket
Version:                1.1.17

%gometa

%global godevelheader %{expand:
Requires:       libpcap-devel}

%global common_description %{expand:
Package Gopacket provides packet decoding for the Go language.}

%global golicenses      LICENSE
%global godocs          examples AUTHORS CONTRIBUTING.md README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Provides packet processing capabilities for Go

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/bpf)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  libpcap-devel

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck -d pfring
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 18:02:09 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.17-1
- Release 1.1.17

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 mskalick@redhat.com - 1.1.15-1
- Use version and fix issues from package review

* Mon Nov 26 2018 mskalick@redhat.com - 0-0.1.20181126gitec90f6c
- First package for Fedora
