# Generated by go2rpm
# Needs network
%bcond_with check

# https://github.com/hashicorp/mdns
%global goipath         github.com/hashicorp/mdns
Version:                1.0.3

%gometa

%global common_description %{expand:
Simple mdns client/server library in golang.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Simple mdns client/server library in golang

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/miekg/dns)
BuildRequires:  golang(golang.org/x/net/ipv4)
BuildRequires:  golang(golang.org/x/net/ipv6)

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 20:03:20 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.3-1
- Update to 1.0.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 17:15:20 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-2
- Update to new macros

* Mon Apr 01 17:30:36 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-1
- Release 1.0.1 (#1668783)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20150317git2b439d3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.14.20150317git2b439d3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20150317git2b439d3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.20150317git2b439d3
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git2b439d3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git2b439d3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git2b439d3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git2b439d3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git2b439d3
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git2b439d3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git2b439d3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git2b439d3
- Update to spec-2.1
  related: #1250470

* Mon Aug 10 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git2b439d3
- Update dependencies on go.net
  related: #1250470

* Wed Aug 05 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.git2b439d3
- Update spec file to spec-2.0
  resolves: #1250470

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git2b439d3
- First package for Fedora
  resolves: #1212116

