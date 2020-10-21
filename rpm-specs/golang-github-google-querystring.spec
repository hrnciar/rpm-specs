# Generated by go2rpm
%bcond_without check

# https://github.com/google/go-querystring
%global goipath         github.com/google/go-querystring
Version:                1.0.0

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-google-go-querystring-devel < 1.0.0-3
}

%global common_description %{expand:
Go-querystring is Go library for encoding structs into URL query parameters.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        7%{?dist}
Summary:        Go library for encoding structs into url query parameters

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock
# Use proper '%v' format for logging structs
# https://github.com/google/go-querystring/commit/992e8021cf787c100d55520d5c906e01536c0a19
Patch0:         https://github.com/google/go-querystring/commit/992e8021cf787c100d55520d5c906e01536c0a19.patch#/0001-use-proper-v-format-for-logging-structs.patch

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1
cp %{S:1} %{S:2} .

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-4
- Add Obsoletes for old name

* Mon Apr 29 21:10:06 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-3
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Update to release 1.0.0

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.14.20141109git547ef5a
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git547ef5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.git547ef5a
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.20141109git547ef5a
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git547ef5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git547ef5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git547ef5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git547ef5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git547ef5a
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git547ef5a
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git547ef5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git547ef5a
- Update to spec-2.1
  related: #1249072

* Fri Jul 31 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git547ef5a
- Update spec file to spec-2.0
  resolves: #1249072

* Thu Apr 16 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git547ef5a
- First package for Fedora
  resolves: #1214913
