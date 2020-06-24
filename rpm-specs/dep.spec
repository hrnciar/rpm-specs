# Generated by go2rpm 1
%bcond_without check

# https://github.com/golang/dep
%global goipath         github.com/golang/dep
Version:                0.5.4

%gometa

%global goname          dep

%global common_description %{expand:
Go dependency management tool.}

%global golicenses      LICENSE PATENTS
%global godocs          docs AUTHORS CHANGELOG.md CODE_OF_CONDUCT.md\\\
                        CONTRIBUTING.md CONTRIBUTORS MAINTAINERS.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go dependency management tool

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/armon/go-radix)
BuildRequires:  golang(github.com/boltdb/bolt)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/jmank88/nuts)
BuildRequires:  golang(github.com/Masterminds/semver)
BuildRequires:  golang(github.com/Masterminds/vcs)
BuildRequires:  golang(github.com/nightlyone/lockfile)
BuildRequires:  golang(github.com/pelletier/go-toml)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/sdboyer/constext)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(gopkg.in/yaml.v2)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
for cmd in gps; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
# Needs internet access
%gocheck -d . -d cmd/dep -d gps -t internal/importers
%endif

%files
%license LICENSE PATENTS
%doc docs AUTHORS CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS
%doc MAINTAINERS.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 07 17:46:09 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.4-1
- Release 0.5.4 (#1677955)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.1-1
- Release 0.5.1

* Tue Mar 05 2019 Jan Chaloupka <jchaloup@redhat.com> - 0.4.1-8
- Set dep version during build time through -X flag
  resolves: #1667484

* Sun Feb 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.1-7
- Remove unnecessary commit hash in version
- Backport linter fix

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6.git37d9ea0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0.4.1-5
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.4.1-4
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 11 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.4.1-2
- Obsolete godep
  resolves: #1552568

* Tue Mar 20 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.4.1-1
- First package for Fedora
  resolves: #1559388
