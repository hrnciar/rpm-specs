# https://github.com/restic/restic
%global goipath         github.com/restic/restic
Version:                0.9.6

%gometa

%global common_description %{expand:
A backup program that is easy, fast, verifiable, secure, efficient and free.

Backup destinations can be:
*Local
*SFTP
*REST Server
*Amazon S3
*Minio Server
*OpenStack Swift
*Backblaze B2
*Microsoft Azure Blob Storage
*Google Cloud Storage
*Other Services via rclone}

%global golicenses    LICENSE


Name:    restic
Release: 3%{?dist}
Summary: Fast, secure, efficient backup program
URL:     %{gourl}
License: BSD
Source0: %{gosource}
Patch0:	 0001-Fix-running-tests-on-a-SELinux-enabled-system.patch

#Restic does not compile for the following archs
ExcludeArch: s390x

BuildRequires: golang(bazil.org/fuse)
BuildRequires: golang(bazil.org/fuse/fs)
BuildRequires: golang(github.com/Azure/azure-sdk-for-go/storage)
BuildRequires: golang(github.com/cenkalti/backoff)
BuildRequires: golang(github.com/elithrar/simple-scrypt)
BuildRequires: golang(github.com/juju/ratelimit)
BuildRequires: golang(github.com/kurin/blazer/b2)
BuildRequires: golang(github.com/mattn/go-isatty)
BuildRequires: golang(github.com/minio/minio-go)
BuildRequires: golang(github.com/minio/minio-go/pkg/credentials)
BuildRequires: golang(github.com/ncw/swift)
BuildRequires: golang(github.com/pkg/errors)
BuildRequires: golang(github.com/pkg/sftp)
BuildRequires: golang(github.com/pkg/xattr)
BuildRequires: golang(github.com/restic/chunker)
BuildRequires: golang(github.com/hashicorp/golang-lru/simplelru)
BuildRequires: golang(golang.org/x/crypto/poly1305)
BuildRequires: golang(golang.org/x/crypto/scrypt)
BuildRequires: golang(golang.org/x/crypto/ssh/terminal)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/context/ctxhttp)
BuildRequires: golang(golang.org/x/net/http2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/sync/errgroup)
BuildRequires: golang(golang.org/x/sys/unix)
BuildRequires: golang(golang.org/x/text/encoding/unicode)
BuildRequires: golang(google.golang.org/api/googleapi)
BuildRequires: golang(google.golang.org/api/storage/v1)
BuildRequires: golang(gopkg.in/tomb.v2)
#for check/testing
BuildRequires: golang(github.com/google/go-cmp/cmp)
#Soft dependency for mounting , ie: fusemount
#Requires: fuse


%description
%{common_description}

#%%gopkg

%prep
%goprep
%patch0 -p1

%build
%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}/cmd/restic


%install
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions
install -p -m 644 doc/man/* %{buildroot}%{_mandir}/man1/
#zsh completion
install -p -m 644 doc/zsh-completion.zsh %{buildroot}%{_datarootdir}/zsh/site-functions/_restic
#Bash completion
install -p -m 644 doc/bash-completion.sh %{buildroot}%{_datarootdir}/bash-completion/completions/restic
install -m 0755 -vd %{buildroot}%{_bindir}
install -p -m 755 %{gobuilddir}/bin/%{name} %{buildroot}%{_bindir}


%check
#Skip tests using fuse due to root requirement
export RESTIC_TEST_FUSE=0
%gocheck


%files
%license LICENSE
%doc GOVERNANCE.md CONTRIBUTING.md CHANGELOG.md README.rst
%{_bindir}/%{name}
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_restic
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/restic
%{_mandir}/man1/restic*.*


%changelog
* Tue Mar 17 2020 Steve Miller (copart) <code@rellims.com> - 0.9.6-3
- Added upstream patch for AccessTime test fix, commit 7cacba0394b1336dfee33e81cb1dc0e87f8ba10f

* Tue Mar 17 2020 Steve Miller (copart) <code@rellims.com> - 0.9.6-2
- Added upstream patch for tests in selinux, commit 2828a9c2b09a7e42ca8ca1c6ac506f87280c158b
- Replaced deprecated gochecks and gobuildroot macros

* Mon Mar 16 2020 Steve Miller (copart) <code@rellims.com> - 0.9.6-1
- Bumped to upstream 0.9.6
  Resolves: #1775745 and #1799976

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Steve Miller (copart) <code@rellims.com> - 0.9.5-1
- Bumped to upstream 0.9.5
  Resolves: #1702384

* Fri Feb 15 2019 Steve Miller (copart) <code@rellims.com> - 0.9.4-1
- Bumped to upstream 0.9.4
- Added new upstream dependency 
  golang(github.com/hashicorp/golang-lru/simplelru)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 3 2018 Steve Miller (copart) <code@rellims.com> - 0.9.3-1
- Bumped to upstream 0.9.3
  Resolves: #1645405 and #1642891
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@xxxxxxxxxxxxxxxxxxxxxxx/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Wed Aug 8 2018 Steve Miller (copart) <code@rellims.com> - 0.9.2-1
- Bumped to upstream 0.9.2

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.9.1-3
- Rebuild with fixed binutils

* Wed Jun 13 2018 Steve Miller (copart) <code@rellims.com> - 0.9.1-2
- First package for Fedora
- Rework using More Go packaging

* Sun Jun 10 2018 Steve Miller (copart) <code@rellims.com> - 0.9.1-1
- Bumped restic version

* Sun May 27 2018 Steve Miller (copart) <code@rellims.com> - 0.9.0-1
- Bumped restic version

* Sun Mar 04 2018 Steve Miller (copart) <code@rellims.com> - 0.8.3-1
- Bumped restic version

* Tue Feb 20 2018 Steve Miller (copart) <code@rellims.com> - 0.8.2-1
- Bumped restic version

* Fri Jan 12 2018 Steve Miller (copart) <code@rellims.com> - 0.8.1-2
- Added man pages
- Added bash completion
- Added zsh completion

* Sun Jan 07 2018 Steve Miller (copart) <code@rellims.com> - 0.8.1-1
- New Version

* Sat Sep 16 2017 Philipp Baum <phil@phib.io> - 0.7.2-1
- New Version

* Sun Aug 27 2017 Philipp Baum <phil@phib.io> - 0.7.1-1
- New Version

* Wed Mar 15 2017 Philipp Baum <phil@phib.io> - 0.5.0-1
- Initial package build
