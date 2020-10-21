%global gssapi_version 1.6.5
%global decorator_version 4.4.2
%global enum34_version 1.1.10

Name:           offlineimap
Version:        7.3.3
Release:        3%{?dist}
Summary:        Powerful IMAP/Maildir synchronization and reader support

License:        GPLv2+
URL:            http://www.offlineimap.org/
Source0:        https://github.com/OfflineIMAP/offlineimap/archive/v%{version}.tar.gz
Source1:        gssapi-%{gssapi_version}.tar.gz
Source2:        decorator-%{decorator_version}.tar.gz
Source3:        enum34-%{enum34_version}.tar.gz


Patch0:         disable_rfc6555.patch
Patch1:         offlineimap-bundledgssapi.patch
Patch2:         gssapi.patch

BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  python2-six
BuildRequires:  asciidoc
BuildRequires:  make
BuildRequires:  gzip
BuildRequires:  python3-sphinx
BuildRequires:  python2-setuptools
# for bundled gssapi
BuildRequires: /usr/bin/pathfix.py
BuildRequires:  krb5-devel >= 1.10
BuildRequires:  krb5-libs >= 1.10
BuildREquires:  gcc

Requires: python2-six
Requires: sqlite

%description
OfflineIMAP is a tool to simplify your e-mail reading. With OfflineIMAP,
you can read the same mailbox from multiple computers.  You get a
current copy of your messages on each computer, and changes you make one
place will be visible on all other systems. For instance, you can delete
a message on your home computer, and it will appear deleted on your work
computer as well. OfflineIMAP is also useful if you want to use a mail
reader that does not have IMAP support, has poor IMAP support, or does
not provide disconnected operation.

%prep
%setup -a1
%patch2 -p0

%setup -D -a2

%setup -D -a3

%setup -D
%patch0 -p1
%patch1 -p1


%build

# build bundled gssapi
pushd gssapi-%{gssapi_version}
CFLAGS="%{optflags}" %{__python2} setup.py build
popd

# build bundled decorator
pushd decorator-%{decorator_version}
%{__python2} setup.py build
popd

# build bundled enum
pushd enum34-%{enum34_version}
%{__python2} setup.py build
popd

sed -i "s|FIXME|%{_libdir}/offlineimap|g" offlineimap/imapserver.py
%{py2_build}

# 'make docs' builds the man pages and the api documentation.
make docs SPHINXBUILD='%{__python3} -msphinx'
gzip -c docs/offlineimap.1 > docs/offlineimap.1.gz
gzip -c docs/offlineimapui.7 > docs/offlineimapui.7.gz
chmod a-x docs/offlineimap.1.gz
chmod a-x docs/offlineimapui.7.gz

%install
%{py2_install}

pushd gssapi-%{gssapi_version}
%{__python2} setup.py install --skip-build --root %{buildroot}

# fix permissions on shared objects (mock seems to set them
# to 0775, whereas a normal build gives 0755)
find %{buildroot}%{python2_sitearch}/gssapi -name '*.so' -exec chmod 0755 {} \;
rm -rf %{buildroot}%{python2_sitearch}/gssapi-*
mkdir -p %{buildroot}%{_libdir}/offlineimap
mv %{buildroot}%{python2_sitearch}/gssapi %{buildroot}/%{_libdir}/offlineimap/
popd

pushd decorator-%{decorator_version}
%{__python2} setup.py install --skip-build --root %{buildroot}

mv %{buildroot}%{python2_sitelib}/decorator* %{buildroot}/%{_libdir}/offlineimap/
popd

pushd enum34-%{enum34_version}
%{__python2} setup.py install --skip-build --root %{buildroot}

mv %{buildroot}%{python2_sitelib}/enum* %{buildroot}/%{_libdir}/offlineimap/
popd

#  Fix python shebang in the offlineimap program.
#  The shebang should use 'python2' rather than just 'python'.
#  To learn more about this, look at:
#  https://fedoraproject.org/wiki/Changes/Make_ambiguous_python_shebangs_error.
# -p preserves timestamps
# -n prevents creating ~backup files
# -i specifies the interpreter for the shebang
pathfix.py -pni "%{__python2} %{py2_shbang_opts}" %{buildroot}/%{_bindir}/offlineimap

mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_mandir}/man7
install -p docs/offlineimap.1.gz %{buildroot}/%{_mandir}/man1/
install -p docs/offlineimapui.7.gz %{buildroot}/%{_mandir}/man7/

%check

./offlineimap.py -V

%files
%license COPYING
%doc offlineimap.conf* docs/html/*.html
%{_bindir}/%{name}
%{_libdir}/%{name}
%{python2_sitelib}/%{name}/
%{python2_sitelib}/%{name}-*-py%{python2_version}.egg-info
%{_mandir}/man1/%{name}.1*
%{_mandir}/man7/%{name}ui.7*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 5 2020 sguelton@redhat.com - 7.3.3-2
- Update and fix gssapi dependency

* Tue Apr 14 2020 sguelton@redhat.com - 7.3.3-1
- Update to upstream 7.3.3

* Tue Mar 24 2020 sguelton@redhat.com - 7.3.2-1
- Update to upstream 7.3.2, without rfc6555 support.

* Tue Feb 25 2020 Bill Nottingham <notting@splat.cc> - 7.2.4-6
- add missing python-six requires (#1806933)

* Tue Feb 04 2020 Bill Nottingham <notting@splat.cc> - 7.2.4-5
- bundle gssapi, move to an archful package

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 12 2019 Bill Nottingham <notting@splat.cc> - 7.2.4-3
- fix build for now

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Bill Nottingham <notting@redhat.com> - 7.2.4-1
- Update to upstream 7.2.4
  - Drop patches
- Add upstreamed patch for SNI with TLS

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 18 2018 Dodji Seketeli <dodji@redhat.com> - 7.2.1-2
- Add patch to handle empty token with complete GSSAPI context.
  This patch was committed upstream so it should be available in the
  next upstream release.  It should fix rhbz#1646916.

* Tue Dec  4 2018 Dodji Seketeli <dodji@redhat.com> - 7.2.1-1
- Update to upstream 7.2.1 tarball
  - Drop the patch Port-to-python-gssapi-from-pykerberos.patch
  - Patch the file offlineimap which contains a shebang invocation of
    python, rather than python2. And this is forbidden by the Fedora
    policies and enforced by a script that fails the build
    otherwise. The patching is done using pathfix.py.
  - Use the python-unversioned-command package at build time (which
    has a python command) because the Makefile uses 'python', rather
    than python2.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 04 2018 Till Maas <opensource@till.name> - 7.1.5-4
- Add patch to use gssapi instead of pykerberos (RH #1549312)
- Use %%{version} in URL
- Use %%license
- Remove %%defattr
- Remove Group tag
- remove unnecessary rm/mkdir

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Dodji Seketeli <dodji@seketeli.org> - 7.1.5-2
- Use %%python2_sitelib, not %%python_sitelib

* Wed Jan 17 2018 Dodji Seketeli <dodji@seketeli.org> - 7.1.5-1
- Update to upstream 7.1.5 tarball
  - Update the URL
  - Droped the patch make-docs-target-be-phony.patch
  - Specifically require python2 packages
  - Require sqlite at runtime

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Mar 21 2016 Dodji Seketeli <dodji@seketeli.org> - 6.7.0-1
- Update to upstream 6.7.0 version.
- Update the URL.
- Droped the patch 0001-Update-version-to-reflect-6.5.6.patch.
- Remove comments that had macros in them, making rpm spit out warning
  during the build.
- Add a patch to force "make docs" to build the documentation, even
  though there is a directory named 'docs'.
- Add asciidoc as a build dependency.  This is useful because the new
  manpage generation mecanism introduced by upstream needs it.
- 'make docs' is is the new way to generate the man pages.
- There is now a new offlineimapui.7 man page.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 10 2015 Dodji Seketeli <dodji@seketeli.org> - 6.5.6-2
- Add python-kerberos as runtime dependency

* Sun Jan  4 2015  <dodji@seketeli.org> - 6.5.6-1
- Update to upstream version 6.5.6
- Adjust the packagedirname macro to the normal naming (non git-pre-release) scheme
- Adjust the Source0 macro to the normal naming scheme
- Now that the name of the extracted source director is normal,
  simplify %%setup rule.
- Add the 0001-Update-version-to-reflect-6.5.6.patch to make the
  version of offlineimap as returned by 'offlineimap --version' be
  6.5.6, as opposed to 6.5.5

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec  1 2013 Dodji Seketeli <dodji@seketeli.org> - 6.5.5-1
- Update to upstream version 6.5.5-0

* Tue Sep 24 2013 Dodji Seketeli <dodji@seketeli.org> - 6.5.5-rc3-0-g254e848-1
- Update to pre-release version 6.5.5-rc3-0-g254e848
- Update Release field accordingly.
- Remove reference to the previous patch.  According to upstream that
  issue should be solved by a folderfilter that filters out empty
  directory names.
- Update %%setup directive in %%prep section to reflect the new naming
  scheme of the package source directory name.
- Update html files references.
- Update the *.egg-info file name reference.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 25 2012 Dodji Seketeli <dodji@seketeli.org> - 6.5.2.1-3
- Do away with the (too heavy) use of git to apply patches
- Apply 35bccdc7dfab8 - Avoid trying to synchronize folders that have empty names
  This is from git://github.com/OfflineIMAP/offlineimap, in the 'pu' branch.
  Fixes #835688 - offline fails to sync with 'new' folder in tree created by dovecot

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 14 2012 Christoph Höger <choeger@umpa-net.de> 6.5.2.1-1
- Upgrade to latest stable version
- Fixes #789805

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 16 2011 Christoph Höger <choeger@umpa-net.de> - 6.3.4-1
- Upgrade to latest stable version
- Fixes #708898

* Tue May 10 2011 Christoph Höger <choeger@umpa-net.de> - 6.3.3-1
- Upgrade to latest stable version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Sep 19 2010 Christoph Höger <choeger@cs.tu-berlin.de> - 6.2.0-1
- Update to the last (not latest, last!) released stable version
- This release fixed some bugs by removing IDLE support
- fixes #525824

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 6.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Christoph Höger <choeger@cs.tu-berlin.de> - 6.1.2-1
- Update to latest version
- remove patch -> upstream
- fixes #510036 

* Thu Jul 02 2009 Christoph Höger <choeger@cs.tu-berlin.de> - 6.1.0-1
- Update to latest version
- Add a temporary patch for socket.ssl deprecation

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Christoph Höger <choeger@cs.tu-berlin.de> 6.0.3-1
- Update to latest version
- use own tarball instead of debian ftp

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 6.0.0-2
- Rebuild for Python 2.6

* Wed Jun 18 2008 Till Maas <opensource till name> - 6.0.0-1
- Update to latest release

* Tue Mar 04 2008 Till Maas <opensource till name> - 5.99.7-1
- Update to latest version

* Tue Mar 04 2008 Till Maas <opensource till name> - 5.99.6-1
- Update to latest version

* Mon Jan 07 2008 Till Maas <opensource till name> - 5.99.4-2
- add egg-info to %%files

* Sun Oct 21 2007 Till Maas <opensource till name> - 5.99.4-1
- update to new version

* Tue Sep 04 2007 Till Maas <opensource till name> - 5.99.2-1
- update to new version
- update license Tag
- add unclosed listitem in offlineimap.sgml
- add missing BR: docbook-utils
- build manpage
- remove todo and manual files from %%doc

* Sat Dec 09 2006 Till Maas <opensource till name> - 4.0.16-3
- rebuild for python2.5
- added BR: python-devel, which is needed now

* Mon Dec 04 2006 Till Maas <opensource till name> - 4.0.16-2
- added -p to cp to preserve timestamp of ChangeLog

* Sun Dec 03 2006 Till Maas <opensource till name> - 4.0.16-1
- version bump
- added one more %%{version} to Source0
- added FAQ.html, todo to %%doc
- added debian/changelog as ChangeLog to %%doc

* Sat Dec 02 2006 Till Maas <opensource till name> - 4.0.15-1
- added %%{?dist} tag
- made Source0 a valid URL
- rearranged tag order and changed whitespace
- added -q -n %%name to %%setup
- removed ChangeLog* from %%doc (not in archive)
- added offlineimap.conf* to %%doc
- Use %%{_bindir} and %%{python_sitelib}
- removed directory docs from %%doc
- added BuildArch: noarch
- added manpage

* Tue May 16 2006 Adam Spiers <adam@spiers.net> 4.0.13-3
- Force prefix to /usr

* Mon May 15 2006 Adam Spiers <adam@spiers.net> 4.0.13-2
- Finally get savemessage_searchforheader right?

* Sun May 14 2006 Adam Spiers <adam@spiers.net> 4.0.13-1
- Updated for 4.0.13

* Sat Apr 29 2006 Adam Spiers <offlineimap@adamspiers.org> 4.0.11-2
- Add patch for Groupwise IMAP servers.

* Fri Apr 28 2006 Adam Spiers <offlineimap@adamspiers.org> 4.0.11-1
- Initial build.
