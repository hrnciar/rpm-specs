# Review bug: https://bugzilla.redhat.com/479723

# Defaults
%global gitver      2.25.1
%global cachedir    %{_localstatedir}/cache/%{name}
%global filterdir   %{_libexecdir}/%{name}/filters
%global scriptdir   %{_localstatedir}/www/cgi-bin
%global cgitdata    %{_datadir}/%{name}

# GPG signing key fingerprints
%global gpg_cgit    AB9942E6D4A4CFC3412620A749FC7012A5DE03AE
%global gpg_git     96E07AF25771955980DAD10020D04E5A713660A7

# Disable automatic compilation of *.py files outside of python sitelib,
# the *.py files in cgit are not importable python modules
%global _python_bytecompile_extra 0

# Settings for Fedora and EL > 7
%if 0%{?fedora} || 0%{?rhel} > 7
%global use_perl_interpreter    1
%else
%global use_perl_interpreter    0
%endif

# The highlight package is only available in EL7+ on ppc64le and x86_64
%if 0%{?rhel} >= 7 && ! ( "%{_arch}" == "ppc64le" || "%{_arch}" == "x86_64" )
%bcond_with     highlight
%else
%bcond_without  highlight
%endif

# Older epel lacks httpd-filesystem
%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without  httpd_filesystem
%else
%bcond_with     httpd_filesystem
%endif

Name:           cgit
Version:        1.2.3
Release:        2%{?dist}
Summary:        A fast web interface for git

License:        GPLv2
URL:            https://git.zx2c4.com/cgit/
Source0:        https://git.zx2c4.com/cgit/snapshot/%{name}-%{version}.tar.xz
Source1:        https://www.kernel.org/pub/software/scm/git/git-%{gitver}.tar.xz
Source2:        cgitrc
Source3:        README.SELinux

# Jason A. Donenfeld's key is used to sign cgit releases.
#https://www.zx2c4.com/keys/AB9942E6D4A4CFC3412620A749FC7012A5DE03AE.asc
Source90:       gpgkey-%{gpg_cgit}.asc

# Junio C Hamano's key is used to sign git releases.  It can be found in the
# junio-gpg-pub tag within git.
#
# (Note that the tagged blob in git contains a version of the key with an
# expired signing subkey.  The subkey expiration has been extended on the
# public keyservers, but the blob in git has not been updated.)
#
# https://git.kernel.org/cgit/git/git.git/tag/?h=junio-gpg-pub
# https://git.kernel.org/cgit/git/git.git/blob/?h=junio-gpg-pub&id=7214aea37915ee2c4f6369eb9dea520aec7d855b
# https://src.fedoraproject.org/rpms/git/raw/master/f/gpgkey-junio.asc
Source91:       gpgkey-%{gpg_git}.asc

# Tarball signatures
Source92:        https://git.zx2c4.com/cgit/snapshot/%{name}-%{version}.tar.asc
Source93:        https://www.kernel.org/pub/software/scm/git/git-%{gitver}.tar.sign

# All supported releases use highlight version 3.
Patch0:         cgit-0.9.1-highlightv3.patch

# Security guys might try to repoquery for this.
Provides:       bundled(git) = %gitver

%if %{with highlight}
BuildRequires:  highlight
%endif

BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libcurl-devel
BuildRequires:  openssl-devel
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  zlib-devel

# Test dependencies
BuildRequires:  gettext
BuildRequires:  lzip
%if %{use_perl_interpreter}
BuildRequires:  perl-interpreter
%else
BuildRequires:  perl
%endif
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  strace
BuildRequires:  tidy
BuildRequires:  unzip
BuildRequires:  xz
BuildRequires:  zstd

%if %{with httpd_filesystem}
# httpd-filesystem provides the basic apache directory layout
Requires:       httpd-filesystem
%endif
Requires:       webserver


%description
Cgit is a fast web interface for git.  It uses caching to increase performance.

%prep
# Verify GPG signatures
#
# Create a temp dir for gpg to ensure we don't use any existing keyrings or
# configuration
gpghome="$(mktemp -qd)"
# Both cgit and git sign the uncompressed tarballs.  Uncompress the sources and
# verify them using the respective signing keys
verify_source() {
    local src=$1 key=$2 ext=$3 tar
    tar=${src/%.xz/}
    xz -dc $src > $tar
    gpg2 --dearmor --quiet --batch --yes $key >/dev/null
    gpgv2 --homedir "$gpghome" --quiet --keyring $key.gpg $tar$ext $tar
    rm -f $key.gpg $tar
}
verify_source %{SOURCE0} %{SOURCE90} .asc
verify_source %{SOURCE1} %{SOURCE91} .sign
rm -rf "$gpghome"

# Ensure a blank line follows autosetup, el6 chokes otherwise
# https://bugzilla.redhat.com/1310704
%autosetup -a 1 -p1

# setup the git dir
rm -rf git
mv git-%{gitver} git

# add README.SELinux
cp -p %{SOURCE3} .

# Use the same options for every invocation of 'make'.
# Otherwise it will rebuild in %%install due to flags changes.
cat << \EOF > cgit.conf
V = 1
CFLAGS = %{optflags}
LDFLAGS = %{?__global_ldflags}
CACHE_ROOT = %{cachedir}
CGIT_SCRIPT_PATH = %{scriptdir}
CGIT_SCRIPT_NAME = cgit
CGIT_DATA_PATH = %{cgitdata}
COPYTREE = %{__cp} -rp
docdir = %{docdir}
filterdir = %{filterdir}
prefix = %{_prefix}
EOF

# git build flags
cat << \EOF > git/config.mak
V = 1
CFLAGS = %{optflags}
LDFLAGS = %{?__global_ldflags}
EOF

# remove env shebang's from filter scripts
grep -rl '#!.*/env' filters/ | xargs -r sed -Ei 's@^(.+/)env (.+)$@\1\2@'

# remove execute permissions from contrib file
find contrib -type f | xargs -r chmod -x

# default httpd config
cat > httpd.conf <<EOF
Alias /cgit-data /usr/share/cgit
ScriptAlias /cgit /var/www/cgi-bin/cgit
%if 0%{?fedora} || 0%{?rhel} >= 7
<Directory "/usr/share/cgit">
    Require all granted
</Directory>
%endif
EOF


%build
%make_build all doc-man doc-html

%if %{with highlight}
highlight --print-style --style-outfile=stdout >> cgit.css
%endif


%install
%make_install install install-man
install -d -m0755 %{buildroot}%{_sysconfdir}/httpd/conf.d
install -p -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/cgitrc
install -p -m0644 httpd.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/cgit.conf
install -d -m0755 %{buildroot}%{cachedir}


%check
make test


%files
%doc README* contrib *.html
%license COPYING
%config(noreplace) %{_sysconfdir}/cgitrc
%if ! %{with httpd_filesystem}
# own httpd config dirs on systems without httpd-filesystem
%dir %{_sysconfdir}/httpd
%dir %{_sysconfdir}/httpd/conf.d
%endif
%config(noreplace) %{_sysconfdir}/httpd/conf.d/cgit.conf
%dir %attr(-,apache,root) %{cachedir}
%{cgitdata}
%{filterdir}
# exclude byte-compiled python files (relevant on Fedora < 29 and RHEL < 8)
%exclude %{filterdir}/*.py[co]
%{scriptdir}/*
%{_mandir}/man*/*


%changelog
* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 1.2.3-2
- Fix string quoting for rpm >= 4.16

* Sat Mar 14 2020 Todd Zullinger <tmz@pobox.com> - 1.2.3-1
- update to 1.2.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Todd Zullinger <tmz@pobox.com> - 1.2.2-1
- update to 1.2.2
- adjust highlight requirement conditional for EL-7+

* Fri Aug 02 2019 Todd Zullinger <tmz@pobox.com> - 1.2.1-5
- add missing zlib-devel BuildRequires, fixes FTBFS (#1737005)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Todd Zullinger <tmz@pobox.com> - 1.2.1-2
- use git's default, collision-detecting SHA1 implementation
- verify upstream GPG signatures in %%prep

* Fri Aug 03 2018 Todd Zullinger <tmz@pobox.com> - 1.2.1-1
- Update to 1.2.1, fixes directory traversal vulnerability

* Fri Jul 13 2018 Todd Zullinger <tmz@pobox.com> - 1.2-1
- Update to 1.2
- Include contrib dir in docs
- Update example cgtirc settings

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Todd Zullinger <tmz@pobox.com> - 1.1-11
- disable automatic compilation of *.py files outside of python sitelib
- use %%bcond_(with|without) to toggle highlight
- use %%autosetup macro
- drop crufty curl-devel conditional
- fix parallel make issues in docs
- simplify README.SELinux install
- use %%bcond_(with|without) to handle httpd-filesystem
- avoid libcrypto.so requires
- run test suite in %%check

* Mon Jun 04 2018 Todd Zullinger <tmz@pobox.com>
- make config: drop redundant DESTDIR/INSTALL, add COPYTREE
- remove env shebang's from filter scripts

* Sun Feb 18 2018 Todd Zullinger <tmz@pobox.com> - 1.1-10
- Use https for source URLs
- Remove el5 conditionals
- Use cgit.conf and config.mak for cgit/git build options
- Drop obsolete %%{buildroot} cleanup
- Add gcc and make BuildRequires

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 1.1-7
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Todd Zullinger <tmz@pobox.com> - 1.1-5
- Require webserver on all dists (#1468839)

* Mon Jul 24 2017 Kevin Fenzi <kevin@scrye.com> - 1.1-4
- Fix httpd requirements on epel7. Fixes bug #1468839

* Tue Mar 07 2017 Pavel Raiskup <praiskup@redhat.com> - 1.1-3
- suggest using correct selinux context (rhbz#1429790)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 23 2016 Kevin Fenzi <kevin@scrye.com> - 1.1-1
- Update to 1.1. Fixes bug #1397820

* Mon Sep 19 2016 Pavel Raiskup <praiskup@redhat.com> - 1.0-2
- ensure we inform about git bundling appropriately

* Tue Jun 07 2016 Kevin Fenzi <kevin@scrye.com> - 1.0-1
- Update to 1.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Kevin Fenzi <kevin@scrye.com> - 0.12-1
- Update to 0.12. Fixes bug #1298912
- Fixes CVE-2016-1899 CVE-2016-1900 CVE-2016-1901

* Sat Sep 05 2015 Kevin Fenzi <kevin@scrye.com> 0.11.2-3
- Fix up logic around webserver and httpd.
- On Fedora require webserver and httpd-filesystem
- On EPEL require httpd.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 14 2015 Kevin Fenzi <kevin@scrye.com> 0.11.2-1
- Update to 0.11.2

* Tue Mar 10 2015 Kevin Fenzi <kevin@scrye.com> 0.11.1-1
- Update to 0.11.1

* Mon Feb 16 2015 Kevin Fenzi <kevin@scrye.com> 0.11.0-1
- Update to 0.11.0

* Mon Feb 09 2015 Pavel Raiskup <praiskup@redhat.com> - 0.10.2-5
- require "any" 'webserver' instead of concrete 'httpd' (#1138599)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 08 2014 Pavel Raiskup <praiskup@redhat.com> - 0.10.2-3
- currently epel-7-ppc64 does not have highlight package (#1117261)

* Tue Jul 08 2014 Pavel Raiskup <praiskup@redhat.com> - 0.10.2-2
- install README.SELinux documentation again (#1036123)
- generate cgit.conf for httpd >= 2.4 when needed

* Tue Jul 01 2014 Kevin Fenzi <kevin@scrye.com> 0.10.2-1
- Update to 0.10.2. Fixes bug #1114970

* Wed Jun 11 2014 Kevin Fenzi <kevin@scrye.com> 0.10.1-4
- Add patch to fix raw patch handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.10.1-2
- Include highlight styles in cgit.css

* Thu Feb 27 2014 Kevin Fenzi <kevin@scrye.com> 0.10.1-1
- Update to 0.10.1
- Correctly enable lua filters. 

* Wed Feb 19 2014 Kevin Fenzi <kevin@scrye.com> 0.10-1
- Update to 0.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 27 2013 Todd Zullinger <tmz@pobox.com> - 0.9.2-1
- Update to 0.9.2, fixes CVE-2013-2117

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Kevin Fenzi <kevin@scrye.com> 0.9.1-3
- Fixed ldflags. Fixes bug 878611

* Sat Nov 17 2012 Kevin Fenzi <kevin@scrye.com> 0.9.1-2
- Add patch to use correct version of highlight for all branches except epel5

* Thu Nov 15 2012 Kevin Fenzi <kevin@scrye.com> 0.9.1-1
- Update to 0.9.1
- Fixes bug #870714 - CVE-2012-4548
- Fixes bug #820733 - CVE-2012-4465

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Todd Zullinger <tmz@pobox.com> - 0.9.0.2-2
- Fix potential XSS vulnerability in rename hint

* Thu Jul 21 2011 Todd Zullinger <tmz@pobox.com> - 0.9.0.2-1
- Update to 0.9.0.2

* Sun Mar 06 2011 Todd Zullinger <tmz@pobox.com> - 0.9-1
- Update to 0.9
- Fixes: CVE-2011-1027
  http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2011-1027
- Generate and install man page and html docs
- Use libcurl-devel on RHEL >= 6
- Include example filter scripts
- Update example cgitrc

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 27 2010 Todd Zullinger <tmz@pobox.com> - 0.8.2.1-4
- Appy upstream git patch for CVE-2010-2542 (#618108)

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.8.2.1-3
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 15 2009 Todd Zullinger <tmz@pobox.com> - 0.8.2.1-1
- Update to 0.8.2.1

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 01 2009 Todd Zullinger <tmz@pobox.com> - 0.8.2-1
- Update to 0.8.2
- Drop upstreamed Makefile patch

* Sun Jan 18 2009 Todd Zullinger <tmz@pobox.com> - 0.8.1-2
- Rebuild with new openssl

* Mon Jan 12 2009 Todd Zullinger <tmz@pobox.com> - 0.8.1-1
- Initial package
