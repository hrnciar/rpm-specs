Name:       reprepro
Version:    5.1.1
Release:    9%{?dist}
Summary:    Tool to handle local repositories of Debian packages
# filecntl.c, md5.c, md5.h are Public Domain
# dpkgversions.c is GPLv2+
# docs/sftp.py is MIT
# Rest is GPLv2
License:    GPLv2 and GPLv2+ and MIT
URL:        http://mirrorer.alioth.debian.org/
# We use the Ubuntu URL here because upstream has not posted the latest release
# to alioth, and it's not clear if they will ever do so.
Source0:    https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{version}.orig.tar.gz
BuildRequires:  gcc
%if 0%{?el6}
BuildRequires: db4-devel
%else
BuildRequires: libdb-devel
%endif
BuildRequires: zlib-devel
BuildRequires: gpgme-devel
BuildRequires: bzip2-devel
BuildRequires: libarchive-devel
BuildRequires: xz-devel

%description
reprepro is a tool to manage a repository of Debian packages (.deb).  It
stores files either being injected manually or downloaded from some other
repository (partially) mirrored into one pool/ hierarchy.  Managed packages
and files are stored in a Berkeley DB, so no database server is needed.
Checking signatures of mirrored repositories and creating signatures of the
generated Package indexes is supported.

%prep
%setup -q

# files in docs should not have executable permissions
find docs -type f -exec chmod -x {} +

# Remove py3 shebang since RHEL 7 does not provide /usr/bin/python3.
for f in docs/outstore.py docs/outsftphook.py; do
  sed -i -e 's|#!/usr/bin/python3|#!/usr/bin/python|' $f
done

%build
%configure
make %{?_smp_mflags}

%install
%make_install

pushd docs

# Shell completion files
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv reprepro.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/reprepro
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
mv reprepro.zsh_completion %{buildroot}%{_datadir}/zsh/site-functions/_reprepro

rm Makefile{,.am,.in} changestool.1 rredtool.1 reprepro.1

# Note: Upstream sources contain tests/test.sh, but Fedora lacks some
# dependencies to run this.

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc docs/ AUTHORS README NEWS
%{_mandir}/man1/changestool.1*
%{_mandir}/man1/reprepro.1*
%{_mandir}/man1/rredtool.1*
%{_bindir}/changestool
%{_bindir}/reprepro
%{_bindir}/rredtool
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/reprepro
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_reprepro


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 17 2017 Ken Dreyer <ktdreyer@ktdreyer.com> - 5.1.1-1
- Update to latest upstream release (rhbz#1411068)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.17.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 4.17.0-5
- Rebuild for gpgme 1.18

* Wed Jun 29 2016 Ken Dreyer <ktdreyer@ktdreyer.com> - 4.17.0-4
- add el6 support

* Sat Feb 20 2016 Ken Dreyer <ktdreyer@ktdreyer.com> - 4.17.0-3
- Remove execute bit from docs files (rhbz#1305737)

* Wed Feb 17 2016 Ken Dreyer <ktdreyer@ktdreyer.com> - 4.17.0-2
- Mark COPYING as %%license (rhbz#1305737)
- Install bash and zsh completion files to usable locations (rhbz#1305737)
- Remove unneeded files from /docs/ (rhbz#1305737)
- Comment regarding the use of Source0 upstream URL (rhbz#1305737)
- Comment regarding test suite (rhbz#1305737)

* Tue Feb 09 2016 Ken Dreyer <ktdreyer@ktdreyer.com> - 4.17.0-1
- Update to latest upstream release
- Use latest Source0 URL
- Fix License tag (rhbz#1170529)
- Remove execute bit from docs/sftp.py (rhbz#1170529)
- Remove trailing whitespace
- Drop implicit requirement on /usr/bin/python3 (for el7 compat)
- Wrap description at 80 characters

* Thu Dec 04 2014 Igor Gnatenko <ignatenko@mirantis.com> - 4.16.0-1
- Rebase to latest version
- spec cleanup

* Wed Oct 31 2012 Sebastien Caps <sebastien.caps@guardis.com> - 4.12.3-6
- Fixed ifs blocks for fedora/rhel based on G Swift comments

* Wed Oct 31 2012 Sebastien Caps <sebastien.caps@guardis.com> - 4.12.3-5
- Feedback on openssl patch, patched sha256 error for fc18

* Sun Oct 21 2012 Sebastien Caps <sebastien.caps@guardis.com> - 4.12.3-4
- Fix build dependencies usage on el6
- Switch to openssl md5 and sha because of sha256 errors on fc18

* Wed Aug 29 2012 Sebastien Caps <sebastien.caps@guardis.com> - 4.12.3-3
- Switch from db4-devel db.h to libdb-devel for fc18.

* Tue Aug 14 2012 Sebastien Caps <sebastien.caps@guardis.com> - 4.12.3-2
- Fix some spec file issue.

* Mon Jul 9 2012 Sebastien Caps <sebastien.caps@guardis.com> - 4.12.3-1
- Initial spec.
