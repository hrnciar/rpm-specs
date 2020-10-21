# Generated by go2rpm
%bcond_without check

# https://github.com/hashicorp/hcl
%global goipath         github.com/hashicorp/hcl
Version:                1.0.0

%gometa

%global common_description %{expand:
HCL (HashiCorp Configuration Language) is a configuration language built by
HashiCorp. The goal of HCL is to build a structured configuration language that
is both human and machine friendly for use with command-line tools, but
specifically targeted towards DevOps tools, servers, etc.

HCL is also fully JSON compatible. That is, JSON can be used as completely valid
input to a system expecting HCL. This helps makes systems interoperable with
other systems.

HCL is heavily inspired by libucl, nginx configuration, and others similar.}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles glide.lock glide.yaml ${testfiles[@]}

Name:           %{goname}
Release:        7%{?dist}
Summary:        Hashicorp configuration language

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock
# https://github.com/hashicorp/hcl/pull/267
Patch0:         https://patch-diff.githubusercontent.com/raw/hashicorp/hcl/pull/267.patch#/0001-Fixes-some-tests-descriptions.patch

%if %{with check}
# Tests
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1
cp %{S:1} %{S:2} .

%install
mapfile -t testfiles <<< $(find $(find . -iname 'test-fixtures' -type d) -type f)
%gopkginstall

# Remove in F33
# Remove erroneous glide.lock folder
%pretrans devel -p <lua>
path = "%{gopath}/src/%{goipath}/glide.lock"
st = posix.stat(path)
if st and st.type == "directory" then
  os.remove(path)
end

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 23:27:17 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-3
- Update to new macros

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-2
- Fix broken test data packaging
- Fix packaging of glide.lock

* Tue Feb 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to first tagged version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.gitef8133d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.18.gitef8133d
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.gitef8133d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.16.gitef8133d
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.20161116gitef8133d
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.gitef8133d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.gitef8133d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.gitef8133d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitef8133d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.gitef8133d
- Bump to upstream ef8133da8cda503718a74741312bf50821e6de79
  related: #1250468

* Thu Jan 12 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.git2deb1d1
- Polish the spec file
  related: #1250468

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git2deb1d1
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git2deb1d1
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git2deb1d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 jchaloup <jchaloup@redhat.com> - 0-0.5.git2deb1d1
- Copy missing directories with test data and run removed tests
  related: #1250468

* Wed Jan 06 2016 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.4.git2deb1d1
- Bump to upstream 2deb1d1db27ed473f38fe65a16044572b9ff9d30
  Removed deleted tests
  related: #1250468

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git513e04c
- Update to spec-2.1
  related: #1250468

* Wed Aug 05 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.git513e04c
- Update spec file to spec-2.0
  resolves: #1250468

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git513e04c
- First package for Fedora
  resolves: #1212059

