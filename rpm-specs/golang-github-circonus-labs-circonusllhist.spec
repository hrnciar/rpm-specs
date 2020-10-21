# Generated by go2rpm
%bcond_without check

# https://github.com/circonus-labs/circonusllhist
%global goipath         github.com/circonus-labs/circonusllhist
Version:                0.1.4

%gometa

%global common_description %{expand:
Package Circllhist provides an implementation of Circonus fixed log-linear
histogram data structure. This allows tracking of histograms in a composable way
such that accurate error can be reasoned about.}

%global golicenses      LICENSE

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go implementation of Circonus log-linear histograms

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 23:58:37 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.4-1
- Update to 0.1.4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 17 16:00:29 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.3-2
- Update to new macros

* Wed Apr 03 20:50:41 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.3-1
- Release 0.1.3 (#1695228)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1
- Release 0.1.0

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.8.20161110git365d370
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git365d370
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.6.20161110git365d370
- Upload glide file

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.5.20161110git365d370
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git365d370
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git365d370
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git365d370
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jan 05 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.git365d370
- First package for Fedora
  resolves: #1410356
