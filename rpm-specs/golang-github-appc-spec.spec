# Generated by go2rpm
%bcond_without check

# https://github.com/appc/spec
%global goipath         github.com/appc/spec
Version:                0.8.11

%gometa

%global common_description %{expand:
This package contains schema definitions and tools for the App Container (appc)
specification. These include technical details on how an appc image is
downloaded over a network, cryptographically verified, and executed on a host.
See SPEC.md for details of the specification itself.}

%global golicenses      LICENSE
%global godocs          examples CHANGELOG.md CONTRIBUTING.md GUIDE.md\\\
                        POLICY.md README.md SPEC.md

Name:           %{goname}
Release:        8%{?dist}
Summary:        App Container Specification and Tooling

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/coreos/go-semver/semver)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(go4.org/errorutil)
BuildRequires:  golang(golang.org/x/net/html)
BuildRequires:  golang(golang.org/x/net/html/atom)
BuildRequires:  golang(gopkg.in/inf.v0)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/gofuzz)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in ace actool; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
mv %{gobuilddir}/bin/ace %{gobuilddir}/bin/ace-validator

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc examples CHANGELOG.md CONTRIBUTING.md GUIDE.md POLICY.md README.md SPEC.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 22:11:24 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.11-6
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.11-4
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0.8.11-3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.8.11-1
  Bump to 0.8.11

* Fri Jun 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.5.1-13.git.git37bef67
- Update to spec 3.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-12.git37bef67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-11.git37bef67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-10.git37bef67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-9.git37bef67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-8.git37bef67
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-7.git37bef67
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6.git37bef67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0.5.1-5.git37bef67
- Update to spec-2.1
  related: #1248491

* Thu Jul 30 2015 jchaloup <jchaloup@redhat.com> - 0.5.1-4.git37bef67
- Update of spec file to spec-2.0
  resolves: #1248491

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3.git37bef67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 02 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.1-2.git37bef67
- update to latest upstream master

* Fri Mar 27 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.1-1.gitc8559a2
- update to latest upstream master branch

* Wed Feb 18 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.3.0-2.gitfa6d3af
- only build for x86_64, ace-validator doesn't work for arm

* Wed Feb 18 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.3.0-1.gitfa6d3af
- update to commit fa6d3af86db496053a2d3c907c676fd9ee1118a8

* Tue Feb 03 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.2.0-2.git2fee340
- update to master commit#2fee340
- provide actool and ace-validator in main package
- remove mentions of fedora 19 (EOL)

* Sat Jan 31 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.2.0-1.git202fd7b
- Resolves: rhbz#1174030 - first package upload
- update to master commit#202fd7b

* Mon Dec 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1.1-2
- update metaprovides
- update docs packaged

* Tue Dec 09 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1.1-1
- First package for Fedora
