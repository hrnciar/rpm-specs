# Generated by go2rpm
%bcond_without check

# https://github.com/russross/blackfriday
%global goipath         gopkg.in/russross/blackfriday.v1
%global forgeurl        https://github.com/russross/blackfriday
Version:                1.5.2

%gometa

# Yes, the version here was incorrect before.
# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-russross-blackfriday-devel < 2.0.1-4
}

%global common_description %{expand:
Blackfriday is a Markdown processor implemented in Go. It is paranoid about its
input (so you can safely feed it user-supplied data), it is fast, it supports
common extensions (tables, smart punctuation substitutions, etc.), and it is
safe for all utf-8 (unicode) input.

HTML output is currently supported, along with Smartypants extensions.}

%global golicenses      LICENSE.txt
%global godocs          README.md

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        4%{?dist}
Summary:        Markdown processor for Go

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.2-2
- Add Obsoletes for old name

* Thu Apr 25 17:35:56 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.5.2-1
- Release 1.5.2

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.5-3
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.5-1
- Update to v1.5
  related: #1222338

* Wed Aug 16 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.2-20
- Bump to upstream 0ba0f2b6ed7c475a92e4df8641825cb7a11d1fa3
  related: #1222338

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.2-17
- Bump to upstream 5f33e7b7878355cd2b7e6b8eefc48a5472c69f70
  related: #1222338

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-15
- https://fedoraproject.org/wiki/Changes/golang1.7

* Tue Mar 22 2016 jchaloup <jchaloup@redhat.com> - 1.2-14
- Bump to upstream 300106c228d52c8941d4b3de6054a6062a86dda3
  related: #1222338

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 1.2-13
- Bump to upstream 8cec3a854e68dba10faabbe31c089abf4a3e57a6
  related: #1222338

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-12
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 24 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.2-10
- Change deps on compiler(go-compiler)
- Update Arches
- Use %%license

* Tue Aug 25 2015 jchaloup <jchaloup@redhat.com> - 1.2-9
- Provide devel package on rhel7
  related: #1222338

* Wed Aug 12 2015 Fridolin Pokorny <fpokorny@redhat.com> - 1.2-8
- Update spec file to spec-2.0
  related: #1222338

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 jchaloup <jchaloup@redhat.com> - 1.2-6
- Add license macro for LICENSE
- Remove runtime dependency on golang.
  resolves: #1222338

* Mon Mar 02 2015 jchaloup <jchaloup@redhat.com> - 1.2-5
- Bump to upstream 77efab57b2f74dd3f9051c79752b2e8995c8b789
  Update spec file to used commit tarball
  related: #1156176

* Wed Feb 25 2015 jchaloup <jchaloup@redhat.com> - 1.2-4
- Add commit and shortcommit global variable
  related: #1156176

* Fri Oct 31 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.2-3
- include fedora/rhel arch conditionals

* Mon Oct 27 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.2-2
- runtime requires go.net/html

* Fri Oct 24 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.2-1
- Resolves: rhbz#1156176 - Initial package
