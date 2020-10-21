# Run tests in check section
%bcond_without check

# https://github.com/Masterminds/glide
%global goipath         github.com/Masterminds/glide
Version:                0.13.2

%gometa

%global common_description %{expand:
Glide is a tool for managing the vendor directory within a Go package. This
feature, first introduced in Go 1.5, allows each package to have a vendor
directory containing dependent packages for the project. These vendor packages
can be installed by a tool (e.g. glide), similar to go get or they can be
vendored and distributed with the package.}

%global golicenses      LICENSE
%global godocs          docs CHANGELOG.md README.md

Name:           glide
Release:        6%{?dist}
Summary:        Package Management for Golang

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# From https://github.com/mattfarina/glide-hash/blob/master/main.go
Patch0:         Add-glide-hash.patch

# glide.go
BuildRequires:  golang(github.com/codegangsta/cli)

# Remaining dependencies not included in main packages
BuildRequires:  golang(github.com/Masterminds/semver) < 2.0.0
BuildRequires:  golang(github.com/Masterminds/vcs)
BuildRequires:  golang(github.com/mitchellh/go-homedir)
BuildRequires:  golang(gopkg.in/yaml.v2)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%build
%gobuild -o %{gobuilddir}/bin/glide %{goipath}
%gobuild -o %{gobuilddir}/bin/glide-hash %{goipath}/glide-hash

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
# Disabled tests need vendoring
%check
%gocheck -d dependency -d path -d util
%endif

%files
%license LICENSE
%doc docs CHANGELOG.md README.md
%{_bindir}/glide
%{_bindir}/glide-hash

%gopkgfiles

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.13.2-2
- Update to latest Go macros
- Enable some tests

* Wed Apr 03 00:52:40 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.13.2-1
- Release 0.13.2 (#1694353)

* Sun Feb 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.13.1-6
- Fix broken version specification

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org>
- 0.13.1-4
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.13.1-3
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 13 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.13.1-1
- Update to v0.13.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-0.5.git8032c28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-0.4.git8032c28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-0.3.git8032c28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-0.2.git8032c28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.git8032c28
- First package for Fedora
  resolves: #1373623
