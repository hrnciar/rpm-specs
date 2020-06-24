# vim: syntax=spec

%if 0%{?fedora} || 0%{?rhel} > 7
%global python          /usr/bin/python3
%global python_build    %py3_build
%global python_install  %py3_install
%global python_sitelib  %python3_sitelib
%else
%global python          /usr/bin/python2
%global python_build    %py2_build
%global python_install  %py2_install
%global python_sitelib  %python2_sitelib
%endif

Name: rpkg-util
Version: 2.7
Release: 6%{?dist}
Summary: RPM packaging utility
License: GPLv2+
URL: https://pagure.io/rpkg-util.git

%if 0%{?fedora} || 0%{?rhel} > 6
VCS: git+ssh://git@pagure.io/rpkg-util.git#ecfcf3b21bc2dcd25895a39427693e11be28edc9:
%endif

# Source is created by:
# git clone https://pagure.io/rpkg-util.git
# cd rpkg-util
# git checkout rpkg-util-2.7-1
# ./rpkg spec --sources
Source0: rpkg-util-2.7.tar.gz

BuildArch: noarch

%description
This package contains the rpkg utility. We are putting
the actual 'rpkg' package into a subpackage because there already
exists package https://src.fedoraproject.org/rpms/rpkg. That package,
however, does not actually produce rpkg rpm whereas rpkg-util does.

%package -n rpkg
Summary: RPM packaging utility
BuildArch: noarch

%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires: python3
BuildRequires: python3-setuptools
BuildRequires: python3-devel
BuildRequires: python3-rpkg
BuildRequires: python3-mock
BuildRequires: python3-pytest
BuildRequires: python3-pyparsing
BuildRequires: python3-munch
BuildRequires: python3-rpm-macros

Requires: python3-rpkg
Requires: python3-pyparsing
%else
BuildRequires: python2
BuildRequires: python2-setuptools
BuildRequires: python2-devel
BuildRequires: python2-rpkg
BuildRequires: python2-mock
BuildRequires: python2-pytest
BuildRequires: python2-configparser
BuildRequires: pyparsing
BuildRequires: python-munch
BuildRequires: python2-rpm-macros

Requires: python2-rpkg
Requires: python2-configparser
Requires: pyparsing
%endif

Requires: git

%description -n rpkg
This is an RPM packaging utility based on python-rpkg library.
It works with both DistGit and standard Git repositories and
it handles packed directory content as well as unpacked content.

%prep
%setup -q

%check
FULL=1 PYTHON=%{python} ./run_tests.sh

%build
version=%{version} %python_build
%{python} man/rpkg_man_page.py > rpkg.1

%install
%{python_install}

sed -i '1 s|#.*|#!%{python}|' %{buildroot}%{_bindir}/rpkg

install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 rpkg.1 %{buildroot}%{_mandir}/man1

install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_datarootdir}/bash-completion/completions

cp -a rpkg.conf %{buildroot}%{_sysconfdir}/
cp -a rpkg.bash %{buildroot}%{_datarootdir}/bash-completion/completions/

%files -n rpkg
%{!?_licensedir:%global license %doc}
%license LICENSE
%{python_sitelib}/*

%config(noreplace) %{_sysconfdir}/rpkg.conf
%{_datadir}/bash-completion/completions/rpkg.bash

%{_bindir}/rpkg
%{_mandir}/*/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.7-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 clime <clime@redhat.com> 2.7-1
- remove dependency on python3-configparser

* Wed Sep 26 2018 clime <clime@redhat.com> 2.6-1
- be more specific about auto-packing deprecation
- fix encoding issues on python2 with POSIX locale set
- fix invalid arguments to setopt on EPEL

* Tue Sep 18 2018 clime <clime@redhat.com> 2.5-1
- EPEL6 fixes
- resolve SafeConfigParser deprecation warning
- EPEL fixes, old git + python related issues
- remove unneded format for tag sorting

* Wed Aug 29 2018 clime <clime@redhat.com> 2.4-1
- fix pg#13: print out more information when lookaside cache is missing
- fix verrel command

* Thu Aug 02 2018 clime <clime@redhat.com> 2.3-1
- tar >= 1.28 condition no longer needed as we dropped --exclude-vcs-ignores
- instead of tar --exclude-vcs-ignores, get the exclude list by git check-ignore
- fix rpkg srpm completion
- switch to git_dir_* macros
- fix no tagname given for rpkg tag -d
- fix for new pyrpkg
- improve git_archive logging info
- print help if no command is given
- add comments to the example config file in man pages
- fix name suffixing for git_cwd and git_dir macros on top-level dir
- follow redirects when downloading sources
- add __pycache__ into .gitignore
- zero umask before creating /tmp/rpkg, ad. #4a4311a
- add log info about path being packed into git_pack
- return back python2 support
- create /tmp/rpkg as writeable by all with sticky bit set
- explicitly mention needed version of git and tar in the spec file
- #8 rpkg error when EDITOR="gvim -f"

* Wed May 02 2018 clime <clime@redhat.com> 2.2-1
- python3 migration
- fix pack_sources script for (sym)linked paths
- fix test dependancy on a parent git repo existance

* Fri Apr 27 2018 clime <clime@redhat.com> 2.1-1
- filter GIT_DISCOVERY_ACROSS_FILESYSTEM not set in tests

* Fri Apr 27 2018 clime <clime@redhat.com> 2.0-1
- slight update in man pages
- fix copr build
- arch param renamed to target + fix tests
- allow --with/--without/--arch for srpm generation

* Thu Apr 19 2018 clime <clime@redhat.com> 2.rc2-1
- implement --with/--without for local, install, prep, compile
- add --follow-tags for push
- fix Git protocol Url parsing for ns_module_name
- fix setup.py not to install tests dir

* Mon Apr 16 2018 clime <clime@redhat.com> 2.rc1-1
- set follow to rc1
- limit renderred commits in tag changelog to path
- invert (fix) logic git_changelog's since_tag and until_tag
for non-existentent tags
- move ~/.config/rpkg to ~/.config/rpkg.conf

* Mon Apr 09 2018 clime <clime@redhat.com> 1.0-1
- spec templates basic impl
- basic command set pretty much determined
- project tagging implemented
- examples and man pages
- rename of package wrapper to rpkg-util
- provide features to manage .spec enriched git projects

* Sun Feb 18 2018 clime <clime@redhat.com> 0.14-1
- fix error when redownloading sources
- do not invoke parent's module_name in load_ns_module_name
- fix python builddeps naming

* Mon Dec 04 2017 clime <clime@redhat.com> 0.13-1
- add LICENSE to ignored file regex

* Mon Oct 23 2017 clime <clime@redhat.com> 0.12-1
- respect hashtype from the sources file if any

* Fri Oct 20 2017 clime <clime@redhat.com> 0.11-1
- set default distgit target to src.fedoraproject.org
- fix downloading sources for any-length-namespace
  modules
- make the whole lookaside url template explict in
  the config file
- rename 'rpkg' config section to 'distgit'
- update in command descriptions

* Wed Oct 18 2017 clime <clime@redhat.com> 0.10-1
- possibility to give directory to --spec
- also take --spec in account for rpmdefines

* Mon Oct 16 2017 clime <clime@redhat.com> 0.9-1
- update spec descriptions
- added is-packed subcommand
- try reading ~/.config/rpkg before /etc/rpkg
- add unittests
- for source downloading, try both url formats
  with/without hashtype
- add make-source subcommand
- patch srpm to generate Source0 if unpacked content
- override load_ns_module_name to work with any length
  namespaces
- added --spec for srpm, make-source, and copr-build
- fixed tagging not to include host dist tag
- docs update
- make all config values optional

* Thu Jul 27 2017 clime <clime@redhat.com> 0.8-1
- fix man pages to only include actually provided part of pyrpkg functionality
- add rpkglib to provide functional interface
- change summary of wrapper package

* Wed Jul 26 2017 clime <clime@redhat.com> 0.7-1
- use %%py2_build and %%py2_install macros
- explicitly invoke python2 for doc generation
- remove no longer needed $BUILDROOT removal in %%install clause
- add missing BuildRequires on python-setuptools

* Fri Jul 07 2017 clime <clime@redhat.com> 0.6-1
- fix build error

* Tue Jun 27 2017 clime <clime@redhat.com> 0.5-1
- remove Requires bash-completion

* Tue Jun 27 2017 clime <clime@redhat.com> 0.4-1
- move config file to /etc/rpkg.conf
- add Requires bash-completion

* Tue Jun 27 2017 clime <clime@redhat.com> 0.3-1
- remove some directories from %%files in .spec
- add (for now) short README.md

* Tue Jun 20 2017 clime <clime@redhat.com> 0.2-1
- new rpkg-client package built with tito

* Mon Jun 12 2017 clime <clime@redhat.com> 0.1-1
- Initial version
