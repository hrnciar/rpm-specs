%global commit b3337dd90b4725052d62d816f0aa433fd467a9d2
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}

Name:           casync
Version:        2
Release:        12%{?commit:.git%{shortcommit}}%{?dist}
Summary:        Content Addressable Data Synchronizer

License:        LGPLv2+
URL:            https://github.com/systemd/casync
%if %{defined commit}
Source0:        https://github.com/keszybz/casync/archive/%{?commit}/casync-%{shortcommit}.tar.gz
%else
Source0:        https://github.com/systemd/casync/archive/v%{version}/%{name}-%{version}.tar.gz
%endif

Patch0001:      0001-Copy-FOREACH_STRING-fix-from-systemd.patch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(liblzma) >= 5.1.0
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libcurl) >= 7.32.0
BuildRequires:  pkgconfig(fuse) >= 2.6
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  libacl-devel
# for rpm macros
BuildRequires:  systemd
# for tests
BuildRequires:  rsync
# for the man page
BuildRequires:  python3-sphinx

%description
casync provides a way to efficiently transfer files which change over
time over the internet. It will split a given set into a git-inspired
content-addressable set of smaller compressed chunks, which can then
be conveniently transferred using HTTP. On the receiving side those
chunks will be uncompressed and merged together to recreate the
original data. When the original data is modified, only the new chunks
have to be transferred during an update.

%prep
%autosetup -p1 %{?commit:-n %{name}-%{commit}}

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%files
%license LICENSE.LGPL2.1
%doc README.md TODO
%_bindir/casync
%dir %_prefix/lib/casync
%dir %_prefix/lib/casync/protocols
%_prefix/lib/casync/protocols/casync-ftp
%_prefix/lib/casync/protocols/casync-http
%_prefix/lib/casync/protocols/casync-https
%_prefix/lib/casync/protocols/casync-sftp
%_mandir/man1/casync.1*
%_udevrulesdir/75-casync.rules

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2-12.gitb3337dd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2-11.gitb3337dd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2-10.gitb3337dd
- Update to snapshot version: the biggest feature addition are:
  * the gc verb
  * support for .caexclude files
  * support for quota project IDs
  Otherwise, this is mostly a lot of bugfixes.
- Fix compilation (#1676286)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2-7
- Fix FTBFS by running proper checks

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2-5
- Rebuild for openssl 1.1

* Fri Sep 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2-4
- Backport fix for setting chunk-size

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 2-2
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2-1
- Update to latest version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-5.gitcc63fcd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1-4.git
- Pull in fixes for failures on non-amd64 arches

* Tue Jun 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1-1
- Initial packaging
