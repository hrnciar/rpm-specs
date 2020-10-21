%global srcname borgbackup

%if 0%{?fedora} || 0%{?rhel} == 8
  %global bundle_msgpack 1
%else
  %global bundle_msgpack 0
%endif

Name:           %{srcname}
Version:        1.1.14
Release:        1%{?dist}
Summary:        A deduplicating backup program with compression and authenticated encryption

%if %bundle_msgpack
License:        BSD and ASL 2.0 and zlib
%else
License:        BSD and zlib
%endif

URL:            https://borgbackup.readthedocs.org
Source0:        %pypi_source
Source1:        %pypi_source.asc
# upstream publishes only key ids:
#    https://borgbackup.readthedocs.io/en/stable/support.html#verifying-signed-releases
# gpg2 --export --export-options export-minimal "6D5B EF9A DD20 7580 5747 B70F 9F88 FB52 FAF7 B393" > gpgkey-6D5B_EF9A_DD20_7580_5747_B70F_9F88_FB52_FAF7_B393.gpg
Source2:        gpgkey-6D5B_EF9A_DD20_7580_5747_B70F_9F88_FB52_FAF7_B393.gpg

# we don't need the guzzley_sphinx theme for only man page generation
Patch1:         0002-disable-sphinx-man-page-build.patch
# ability not to build bundled msgpack
Patch2:         0003-ability-to-unbundle-msgpack.patch
# https://mail.python.org/pipermail/borgbackup/2020q4/001699.html
Patch3:         borgbackup-strip-llfuse-versions.patch

BuildRequires:  gnupg2
# build
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm
BuildRequires:  python%{python3_pkgversion}-Cython
BuildRequires:  python%{python3_pkgversion}-llfuse >= 1.3.4

%if %bundle_msgpack
Provides:       bundled(python%{python3_pkgversion}-msgpack) = 0.5.6
# requirements for bundled msgpack
BuildRequires:  gcc-c++
%else
BuildRequires:  python%{python3_pkgversion}-msgpack <= 0.5.6
%endif

# test
BuildRequires:  python%{python3_pkgversion}-pytest

# doc
BuildRequires:  python%{python3_pkgversion}-sphinx

# no python deps
BuildRequires:  gcc
BuildRequires:  openssl-devel >= 1.0.0
BuildRequires:  fuse-devel
BuildRequires:  libacl-devel
BuildRequires:  libb2-devel
BuildRequires:  lz4-devel >= 1.7.0
BuildRequires:  libzstd-devel >= 1.3.0

%if ! %bundle_msgpack
Requires:       python%{python3_pkgversion}-msgpack <= 0.5.6
%endif
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-llfuse >= 1.3.4
Requires:       fuse

# xxHash: https://github.com/Cyan4973/xxHash
# license: 2-clause BSD (Fedora: BSD, SPDX: BSD-2-Clause)
# code was stripped a bit to only contain 64-bit functionality
# upstream justification for bundling:
#     https://github.com/borgbackup/borg/pull/2580#issuecomment-305579398
# upstream won't unbundle this for v1.1.x:
#     https://github.com/borgbackup/borg/issues/4592#issuecomment-495951573
# since borgbackup 1.1.11 the code needs at least xxHash >= 0.7.2
Provides:       bundled(xxHash) = 0.7.4

%description
BorgBackup (short: Borg) is a deduplicating backup program. Optionally, it
supports compression and authenticated encryption.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
rm -rf %{srcname}.egg-info

# remove copies of bundled libraries to ensure these don't end up in our
# binaries
rm -rf src/borg/algorithms/{blake2,lz4,zstd}
# remove precompiled Cython code to ensure we always built "from source"
find src/ -name '*.pyx' | sed -e 's/.pyx/.c/g' | xargs rm -f

%if %bundle_msgpack
  # bundled msgpack uses C++ for its generated sources
  find src/ -name '*.pyx' | sed -e 's/.pyx/.cpp/g' | xargs rm -f

  # better name for inclusion in %%license
  cp -a docs/3rd_party/msgpack/COPYING COPYING.msgpack
%else
  rm -rf src/borg/algorithms/msgpack

  # https://bugzilla.redhat.com/show_bug.cgi?id=1630992
  sed -i 's/msgpack-python/msgpack/' setup.py
%endif


%build
%if ! %bundle_msgpack
    export BORG_EXTERNAL_MSGPACK=True
%endif
%py3_build

# MANPAGE GENERATION
# workaround to dump sphinx_rtd_theme dependency - not needed for manpages
export READTHEDOCS=True

# workaround to include borg module for usage generation
export PYTHONPATH=$(pwd)/build/$(ls build/ | grep 'lib.')

make -C docs SPHINXBUILD=sphinx-build-%python3_version man

%install
find . -name *.so -type f -exec chmod 0755 {} \;

%py3_install
install -D -m 0644 docs/_build/man/borg*.1* %{buildroot}%{_mandir}/man1/borg.1

# add shell completions
#%define bash_compdir %(pkg-config --variable=completionsdir bash-completion)
%define bash_compdir %{_prefix}/share/bash-completion/completions
%define zsh_compdir %{_prefix}/share/zsh/site-functions
%define fish_compdir %{_prefix}/share/fish/completions

install -d  %{buildroot}%{bash_compdir}
install -d  %{buildroot}%{zsh_compdir}
install -d  %{buildroot}%{fish_compdir}

install -D -m 0644 scripts/shell_completions/bash/* %{buildroot}%{bash_compdir}
install -D -m 0644 scripts/shell_completions/zsh/* %{buildroot}%{zsh_compdir}
install -D -m 0644 scripts/shell_completions/fish/* %{buildroot}%{fish_compdir}

%check
export PYTHONPATH=$(pwd)/build/$(ls build/ | grep 'lib.')

# workaround to prevent test issues with ascii/utf-8 under rhel 7
%if 0%{?rhel} == 7
export LANG=en_US.UTF-8
%endif

# exclude test_fuse: there is no modprobe in mock for fuse
# test_readonly_mount: needs fuse mount
# exclude benchmark: not relevant for package build
TEST_SELECTOR="not test_fuse and not test_readonly_mount and not benchmark"
%if 0%{?rhel} == 7
# exclude test_dash_open: pytest stub has a bug and is fixed in 3.0.2 (epel7 uses 2.9.2)
TEST_SELECTOR="$TEST_SELECTOR and not test_dash_open"
%endif
py.test-3 -x -vk "$TEST_SELECTOR" $PYTHONPATH/borg/testsuite/*.py

%files
%license LICENSE
%if %bundle_msgpack
  %license COPYING.msgpack
%endif
%doc README.rst PKG-INFO AUTHORS
%doc docs/changes.rst
%{_mandir}/man1/*

%{python3_sitearch}/borg
%{python3_sitearch}/borgbackup-%{version}-py%{python3_version}.egg-info
# - files in %%{python3_sitearch}/borg/algorithms/msgpack are licensed under the ASL
# - %%{python3_sitearch}/borg/algorithms/checksums.*.so contains code licensed
#   under the zlib license
%{_bindir}/borg
%{_bindir}/borgfs
%{_prefix}/share/bash-completion/completions/*
%{_prefix}/share/zsh/site-functions/*
%{_prefix}/share/fish/completions/*


%changelog
* Thu Oct 08 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.14-1
- update to 1.1.14

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.13-1
- update to 1.1.13

* Thu Jun 04 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.11-3
- add patch to prevent sporadic test failures (see F31 rebuild attempts)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.11-2
- Rebuilt for Python 3.9

* Sun Mar 08 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.11-1
- update to 1.1.11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.10-6
- enable GPG source file verification

* Mon Sep 23 2019 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.10-5
- Rebuilt for libb2 0.98.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.10-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.10-2
- declare bundled xxhash correctly and adapt license tag accordingly
- bundle python3-msgpack only when necessary (Fedora 30+)
- fine-grained test exclusion to run as many tests as possible

* Thu May 16 2019 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.10-1
- Upstream Release 1.1.10

* Thu May 09 2019 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.9-3
- bundle msgpack 0.5.6 (rhbz 1669083)

* Sun Mar 10 2019 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.9-2
- drop python2-sphinx dependency

* Sat Mar 09 2019 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.9-1
- Upstream Release 1.1.9

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 29 2018 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.8-1
- Upstream Release 1.1.8

* Sun Sep 23 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.7-2
- Fix entrypoint broken by the msgpack rename (#1630992)

* Mon Sep 03 2018 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.7-1
- Upstream Release 1.1.7
- Rawhide compliant

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-3
- Rebuilt for Python 3.7

* Wed Apr 11 2018 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.5-2
- require python-msgpack >= 0.5.6 (see GH#3753)

* Tue Apr 10 2018 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.5-1
- upstream version 1.1.5 (see upstream changelog)
- require python-msgpack < 0.5.0
- patch0 not needed anymore - fixed upstream

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 1 2018 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.4-2
- add testsuite, needed for selftest

* Mon Jan 1 2018 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.4-1
- upstream version 1.1.4 (see upstream changelog)
- added zstd compression
- removed patch for borg check --repair malfunction
- remove testsuite from package

* Sun Dec 17 2017 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.3-2
- fix borg check --repair malfunction (upstream pull #3444)

* Tue Nov 28 2017 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.3-1
- upstream version 1.1.3
- fixes CVE-2017-15914 (BZ#1517664)

* Tue Nov 07 2017 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.2-1
- upstream version 1.1.2
- added shell completions

* Wed Nov 01 2017 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.1-1
- upstream version 1.1.1

* Mon Oct 09 2017 Benjamin Pereto <bpereto@fedoraproject.org> - 1.1.0-1
- upstream version 1.1.0 (BZ#1499512)
- added missing fuse dependency (BZ#1493434)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.11-3
- removed sphinx_rtd_theme dependency

* Sat Jul 29 2017 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.11-1
- upstream version 1.0.11 (BZ#1473897)
- removed setup.py build_api

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.10-1
- upstream version 1.0.10 (BZ#1421660)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 25 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.9-1
- upstream version 1.0.9 (BZ#1406277)
- fix manifest spoofing vulnerability - see docs for info

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.8-3
- Rebuild for Python 3.6

* Mon Oct 31 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.8-2
- upstream version 1.0.8 (BZ#1389986)

* Sun Aug 21 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.7-1
- security fix with borg serve and restrict-to-path (BZ#1354371)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.6-1
- upstream version 1.0.6 (BZ#1354371)
- update source url (now pointing to files.pythonhosted.org)
- testsuite on XFS is patched upstream

* Fri Jul 01 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0.3-2
- Fix testsuite on XFS (#1331820)

* Sun May 22 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.3-1
- Added requires for setuptools (BZ#1335325)
- upstream version 1.0.3

* Thu Apr 28 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.2-2
- rebuilt

* Thu Apr 28 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.2-2
- Missing dependency python-setuptools

* Sun Apr 17 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.2-1
- added epel7 specific parts
- make manpage generation work with epel7
- upstream version 1.0.2

* Sat Apr 16 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.1-2
- simplified specfile
- removed unneeded dependencies: python3-mock, python3-pytest-cov

* Sun Apr 10 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.1-1
- Upstream version 1.0.1. see changelog

* Thu Apr 07 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.0-2
- Added requires for python3-llfuse (#1324685)
- Added minversion for openssl

* Mon Apr 04 2016 Benjamin Pereto <bpereto@fedoraproject.org> - 1.0.0-1
- Upstream version 1.0.0
- Rewrote build requirements for EPEL7

* Thu Dec 17 2015 Benjamin Pereto <bpereto@fedoraproject.org> - 0.29.0-3
- Specified correct project URL
- Added Buildrequires python3-sphinx_rtd_theme for f23

* Thu Dec 17 2015 Benjamin Pereto <bpereto@fedoraproject.org> - 0.29.0-2
- Cleanup Spec
- Rename package to borgbackup
 
* Mon Dec 14 2015 Benjamin Pereto <bpereto@fedoraproject.org> - 0.29.0-1
- New Upstream Version
- Added manpage from Upstream
- Testsuite now functional without benchmark

* Sat Dec 05 2015 Benjamin Pereto <bpereto@fedoraproject.org> - 0.28.2-6
- Added correct testsuite to check
- Removed unnessesary statements

* Fri Dec 04 2015 Benjamin Pereto <bpereto@fedoraproject.org> - 0.28.2-5
- Renamed Specfile to python3 only and remove pre-built egg-info

* Wed Dec 02 2015 Benjamin Pereto <bpereto@fedoraproject.org> - 0.28.2-4
- Removed double package statement and sum macro

* Tue Dec 01 2015 Benjamin Pereto <bpereto@fedoraproject.org> - 0.28.2-3
- Added dependency python3-msgpack to buildrequires

* Tue Dec 01 2015 Benjamin Pereto <bpereto@fedoraproject.org> - 0.28.2-2
- Added dependency python3-msgpack

* Tue Dec 01 2015 Benjamin Pereto <bpereto@fedoraproject.org> - 0.28.2-1
- Initial Packaging for the BorgBackup Project

