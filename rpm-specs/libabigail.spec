%global tarball_revision 0
%global tarball_name %{name}-%{version}

Name: libabigail
Version: 1.7
Release: 2%{?dist}
Summary: Set of ABI analysis tools

License: LGPLv3+
URL: https://sourceware.org/libabigail/
Source0: http://mirrors.kernel.org/sourceware/libabigail/%{tarball_name}.tar.gz

BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: elfutils-devel
BuildRequires: libxml2-devel
BuildRequires: doxygen
BuildRequires: python3-sphinx
BuildRequires: texinfo
BuildRequires: dos2unix
BuildRequires: dpkg
BuildRequires: wget
BuildRequires: koji

%description
The libabigail package comprises seven command line utilities:
abidiff, kmidiff, abipkgdiff, abicompat, abidw, and abilint.
The abidiff command line tool compares the ABI of two
ELF shared libraries and emits meaningful textual reports about
changes impacting exported functions, variables and their types.
Simarly, the kmidiff compares the kernel module interface of two Linux
kernels.  abipkgdiff compares the ABIs of ELF binaries contained in
two packages.  abicompat checks if a subsequent version of a shared
library is still compatible with an application that is linked against
it.  abidw emits an XML representation of the ABI of a given ELF
shared library. abilint checks that a given XML representation of the
ABI of a shared library is correct.

Install libabigail if you need to compare the ABI of ELF shared
libraries.

%package devel
Summary: Shared library and header files to write ABI analysis tools
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains a shared library and the associated header files
that are necessary to develop applications that use the C++ Libabigail
library.  The library provides facilities to analyze and compare
application binary interfaces of shared libraries in the ELF format.


%package doc
Summary: Man pages, texinfo files and html manuals of libabigail

%description doc
This package contains documentation for the libabigail tools in the
form of man pages, texinfo documentation and API documentation in html
format.

%if 0%{?fedora}
%package fedora
Summary: Utility to compare the ABI of Fedora packages
BuildRequires: python3-devel
BuildRequires: python3-koji
BuildRequires: python3-mock
BuildRequires: python3-rpm
BuildRequires: python3-pyxdg
#For x-rpm mimetype definition!
BuildRequires: mailcap
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: curl
Requires: koji
Requires: python3 >= 3.6
Requires: python3-koji
Requires: python3-pyxdg
Requires: python3-rpm
#For x-rpm mimetype definition!
Requires: mailcap

%description fedora
This package contains the fedabipkgdiff command line utility, which
interacts with the Fedora Build System over the internet to let the
user compare the ABI of Fedora packages without having to download
them manually.
%endif

%prep
%setup -n %{tarball_name}

%build
%configure --disable-silent-rules --disable-zip-archive --disable-static 
make %{?_smp_mflags}
pushd doc
make html-doc
pushd manuals
make html-doc
make man
make info
popd
popd

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Install man and texinfo files as they are not installed by the
# default 'install' target of the makefile.
make -C doc/manuals install-man-and-info-doc DESTDIR=%{buildroot}
dos2unix doc/manuals/html/_static/jquery.js

%if 0%{?fedora}
# Explicitly use Python 3 as the interpreter
pathfix.py -i %{__python3} -pn %{buildroot}%{_bindir}/fedabipkgdiff
%endif

%check
time make %{?_smp_mflags} check || (cat tests/test-suite.log && exit 2)

if test $? -ne 0; then
  cat tests/tests-suite.log
fi

%ldconfig_scriptlets

%files
%{_bindir}/abicompat
%{_bindir}/abidiff
%{_bindir}/abidw
%{_bindir}/abilint
%{_bindir}/abipkgdiff
%{_bindir}/kmidiff
%{_libdir}/libabigail.so.0
%{_libdir}/libabigail.so.0.0.0
%{_libdir}/libabigail/default.abignore
%doc README AUTHORS ChangeLog
%license COPYING COPYING-LGPLV3 COPYING-GPLV3
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_infodir}/abigail.info*

%files devel
%{_libdir}/libabigail.so
%{_libdir}/pkgconfig/libabigail.pc
%{_includedir}/*
%{_datadir}/aclocal/abigail.m4

%files doc
%license COPYING  COPYING-LGPLV3 COPYING-GPLV3
%doc doc/manuals/html/*

%if 0%{?fedora}
%files fedora
%{_bindir}/fedabipkgdiff
%endif

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 25 2020 Dodji Seketeli <dodji@redhat.com> - 1.7-1
- Update to upstream 1.7

* Mon Feb 17 2020 Sinny Kumari <skumari@fedoraproject.org> - 1.6-4
- Add koji as BuildRequires
- Fixes: RHBZ#1799575

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Dodji Seketeli <dodji@redhat.com> - 1.6-1
- Update to upstream 1.6
- Removed patches that are now upstream
  Support-having-several-debuginfo-search-dirs-for-a-b.patch
  Add-a-fail-no-debug-info-to-abidiff.patch

* Wed Mar 13 2019 Mathieu Bridon <bochecha@daitauha.fr> - 1.5-4
- Remove unnecessary dependencies: python3-unittest2 and wget which
  was referred to twice.
- Better group dependencies: Many dependencies are only required for
  fedabipkgdiff, so let's put them under the right conditional.
- Split fedabipkgdiff to its own subpackage
    This tool is very specific, and only useful to Fedora developers,
    not all developers.  It also has lots of dependencies which aren't
    required by the other tools.  Splitting it to its own specialized
    package makes the main package, with its library and utilities,
    much lighter.

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1.5-4
- Remove obsolete requirements for %%post/%%preun scriptlets

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Dodji Seketeli <dodji@seketeli.org> - 1.5-2
- Apply patches
  Support-having-several-debuginfo-search-dirs-for-a-b.patch and
  Add-a-fail-no-debug-info-to-abidiff.patch

* Thu Oct 25 2018 Dodji Seketeli <dodji@seketeli.org> - 1.5-1
- Update to upstream 1.5

* Wed Jul 25 2018 Nils Philippsen <nils@tiptoe.de> - 1.4-2
- explicitly use Python 3 for fedabipkgdiff

* Fri Jul 13 2018 Dodji Seketeli <dodji@redhat.com> - 1.4-1
- Update to upstream 1.4
- Merge change to build fedabipkgdiff in Fedora only.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3-2
- Rebuilt for Python 3.7

* Wed May 16 2018 Dodji Seketeli <dodji@redhat.com> - 1.3-1
- Update to upstream 1.3
- Use python3 modules

* Mon Mar 19 2018 Dodji Seketeli <dodji@redhat.com> - 1.2-2
- Depend on Koji only on Fedora

* Mon Mar  5 2018 Dodji Seketeli <dodji@redhat.com> - 1.2-1
- Update to upstream 1.2

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1-4
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1-2
- Switch to %%ldconfig_scriptlets

* Thu Jan 25 2018 Dodji Seketeli <dodji@redhat.com> - 1.1-1
- Update to upstream 1.1
- Use python2-sphynx, rpm-python2, python2-rpm rather than
  python-sphinx, rpm-python.

* Wed Nov 22 2017 Dodji Seketeli <dodji@seketeli.org> - 1.0-1
- Add missing %%{dist} to release.

* Tue Nov 7 2017 Dodji Seketeli <dodji@redhat.com> - 1.0-1
- Update to upstream 1.0 tarball
- Adjust tarball_revision and tarball_name macros
- Adjust Release macro
- Remove the koji build require as python2-koji is enough
- Replace the pyxdg build require with the python2-pyxdg one.
- Added missing build and runtime require 'mailcap' to allow
  fedabipkgdiff to detect RPM files
- Update description to account for the new kmidiff tool
- Remove patches that got applied upstream:
  0001-A-suppressed-diff-node-implies-suppressing-all-equiv.patch
  0001-Bug-20927-Segfault-when-HOME-is-not-set.patch
  0001-Fix-aborting-when-reading-.foo-symbols-from-a-ppc64-.patch
- Add kmidiff to the RPM

* Fri Oct 06 2017 Troy Dawson <tdawson@redhat.com> - 1.0-0.13.rc6.4
- Fix rawhide FTBFS - Added Buildrequires python2-koji

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.12.rc6.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.11.rc6.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.10.rc6.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.9.rc6.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec  9 2016 Dodji Seketeli <dodji@redhat.com> - 1.0-0.8.rc6.4
- Fix upstream bug - Fix aborting when reading .foo symbols from a ppc64 binary

* Mon Dec  5 2016 Dodji Seketeli <dodji@redhat.com> - 1.0-0.8.rc6.3
- Fix upstream Bug 20927 - Segfault when abidiff is invoked with $HOME empty
  Apply the upstream patch here.

* Sat Nov 26 2016 Dodji Seketeli <dodji@redhat.com> - 1.0-0.8.rc6.2
- Fix an issue where some suppressed diff nodes are still visible in change reports
  This implies applying upstream patch:
   "[PATCH] A suppressed diff node implies suppressing all equivalent nodes too"

* Wed Nov 23 2016 Dodji Seketeli <dodji@redhat.com> - 1.0-0.8.rc6.1
- Update to upstream 1.0.rc6 tarball
- Add wget as a build and runtime requirement.  It's useful for fedabipkgdiff

* Mon Aug 29 2016 Dodji Seketeli <dodji@seketeli.org> - 1.0-0.8.rc5.5
- Update the package description to mention fedabipkgdiff

* Mon Aug 29 2016 Chenxiong Qi <cqi@redhat.com> - 1.0-0.8.rc5.4
- Add pyxdg, rpm-python, koji and python2 as runtime dependencies

* Tue Jun 28 2016 Dodji Seketeli <dodji@seketeli.org> - 1.0-0.8.rc5.3
- Fix previous change log entry

* Tue Jun 28 2016 Dodji Seketeli <dodji@seketeli.org> - 1.0-0.8.rc5.2
- Add README

* Mon Jun 27 2016 Dodji Seketeli <dodji@seketeli.org> - 1.0-0.8.rc5.1
- Update to upstream 1.0.rc5 tarball
- Add new build requires for new fedabipkgdiff tool:
  python2-devel, rpm-python, python2-mock, koji, pyxdg, python2-unittest2
- Add new %%{_bindir}/fedabipkgdiff binary and
  %%{_libdir}/libabigail/default.abignore configuration file to the set
  of distributed files. 
- Drop patches that were integrated upstream:
  0001-Bug-19961-Distinguish-between-PI-executable-and-shar.patch
  0002-Bug-19964-Cannot-load-function-aliases-on-ppc64.patch


* Mon May  2 2016 Dodji Seketeli <dodji@seketeli.org> - 1.0-0.8.rc4.3%{?dist}
- Add README file

* Mon Apr 25 2016 Dodji Seketeli <dodji@seketeli.org> - 1.0-0.8.rc4.2
- Fix PIE and ppc64 function aliases handling.
  The exact two upstream bugs fixed are:
    Bug 19961 - Distinguish between PI executable and shared library
    Bug 19964 - Cannot load function aliases on ppc64
  The two upstream patches applied are 8944ceb9ef03a4187 and 2529f84ae0e2ca2a

* Sun Apr 17 2016 Dodji Seketeli <dodji@seketeli.org> - 1.0-0.8.rc4.1
- Update to upstream 1.0.rc4
- Remove fix-test-diff-pkg-patch.txt as it was applied upstream.

* Tue Mar  8 2016 Dodji Seketeli <dodji@seketeli.org> - 1.0-0.rc3.2
- Fix test-diff-pkg regression test failure due to a race condition.

* Tue Mar  8 2016 Dodji Seketeli <dodji@seketeli.org> - 1.0-0.rc3.1
- Update to upstream 1.0.rc3
- Add gcc-c++ as BuildRequires
- Measure the time taken by regression tests

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.rc2.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan  7 2016 Dodji Seketeli <dodji@seketeli.org> - 1.0-0.rc2.1
- Update to upstream 1.0.rc2
- This fixes an important regression in the handling of binaries
  which debug info have been compressed with dwz.
- Fix source tarball URL.

* Wed Jan  6 2016 Dodji Seketeli <dodji@seketeli.org> - 1.0-0.rc1.3
- Run make check in // if possible

* Wed Jan  6 2016 Dodji Seketeli <dodji@seketeli.org> - 1.0-0.rc1.2
- Add/Remove info pages to/from info pages database after install/before remove

* Tue Jan  5 2016 Dodji Seketeli <dodji@redhat.com> - 1.0-0.rc1.1
- Ship man/info pages right into the main package, along with the main
  programs.
- Update to upstream release 1.0.rc1
- Significant changes include:
   rhtbz/1283906 - crash in abigail::dwarf_reader::build_reference_type()
   libabigail/19336 - Better handle redundantly qualified reference types
   libabigail/19126 - abidw segv on a dwz compressed version of r300_dri.so
   libabigail/19355 - Libabigail slow on r300_dri.so
   Numerous other bug fixes and cleanups

* Mon Nov 16 2015 Dodji Seketeli <dodji@seketeli.org> - 1.0-0.7.rc0.20151116gitd8bcceb
- Update to upstream release 1.0.rc0
- Take a tarball built using make dist now.
- Update the comments in the spec regarding how the tarball has been generated.
- Do not run autoreconf -i anymore, during the build.

* Wed Sep 9 2015 Dodji Seketeli <dodji@seketeli.org> - 1.0-0.6.20150909git164d17e
- Update to upstream git commit hash 164d17e
  Bug 18791 - libabigail fails to read the output of abidw
  Bug 18818 - abidw aborts on a class with a non-complete base class
  Bug 18828 - Handle force-resolving of multiple declarations-only of the same type
  Bug 18844 - assert failure in abidw at abg-dwarf-reader.cc:6537
  Bug 18894 - Fix representation of enumerators in abixml format
  Bug 18893 - type degradation from dwarf to abixml on libGLU.so
  Bug 18892 - type degradation from DWARF to abixml on libtsan.so
  Bug 18904 - Fix support for C++ rvalue references
  Numerous additional bug fixes
  Added .deb, tarball and directory support to abipkgdiff
  Several improvements to abidw, abidiff and abilint
- Added dpkg build dependency to activate support of .deb archives
- cat tests/test-suite.log when check fails
- Update description to add abipkgdiff

* Mon Jul 27 2015 Sinny Kumari <ksinny@gmail.com> - 1.0-0.5.20150727gitf0d319a
- Update to upstream git commit hash f0d319a. Returns different exit status code
  when abipkgdiff runs and various other bug fixes in libabigail.
- Adjust date, git_revision and Release macros

* Mon Jul 20 2015 Sinny Kumari <ksinny@gmail.com> - 1.0-0.4.20150720gitab1316b
- Update to upstream git commit hash ab1316b. It brings various bug fixes and a
  new abipkgdiff tool to detect abi changes at package level.
- Install abipkgdiff binary in bindir
- Adjust date, git_revision and Release macros

* Thu Jun 25 2015 Dodji Seketeli <dodji@seketeli.org> - 1.0-0.3.20150625git43c06a8
- Update to upstream git commit hash 43c06a8 (pre-release of 1.0).
  This brings lots of bug fixes as well as some improvements in change
  report suppression capabilities in the library and in the abidiff
  tool.
- Tarball name format is now clearer: %%{name}-%%{version}-git-%%{git_revision}
- Add new macro tarball_name for that
- Adjust the Source0, git_revision, date, Release macros
- Adjust the %%setup directive to the fact that the tarball now extracts to
  a directory named %%{name}-%%{version}-git-%%{git_revision}
- Adjust the packaging of the man pages as some of them moved from
  section 7 to section 1.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.2.20150422gita9582d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 22 2015 Sinny Kumari <ksinny@gmail.com> - 1.0-0.1.20150420gita9582d8
- Add COPYING-GPLV3 license file as well
- Remove python-sphinx-latex from BuildRequires
- Package latest source tar with git revision a9582d8

* Sat Jan 24 2015 Sinny Kumari <ksinny@gmail.com> - 1.0-0.3.20150114git63c81f0
- Specify only sub-packgae name instead of giving full package name
- Add info as post and preun Requires for doc sub-package

* Fri Jan 23 2015 Sinny Kumari <ksinny@gmail.com> - 1.0-0.2.20150114git63c81f0
- Add python-sphinx-latex as BuildRequires
- Use license instead of doc macro for license file installation
- Update checkout value

* Sun Jan 18 2015 Sinny Kumari <ksinny@gmail.com> - 1.0-0.1.git.63c81f0
- Initial build of the libabigail package using source code from git
  revision 63c81f0.
