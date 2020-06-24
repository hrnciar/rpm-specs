Name:           rpkg
Version:        1.60
Release:        4%{?dist}

Summary:        Python library for interacting with rpm+git
License:        GPLv2+ and LGPLv2
URL:            https://pagure.io/rpkg
BuildArch:      noarch
Source0:        https://pagure.io/releases/rpkg/%{name}-%{version}.tar.gz

# Fix for bug 1579367
# Due to https://pagure.io/koji/issue/912, python[23]-koji package does not
# have egginfo.
# rpm-py-installer is required as a proxy to install RPM python binding
# library, so rpm is the actual requirement that must be present in the
# requires.txt. But, rpkg has to work in all active Fedora and EPEL releases,
# and there is only old rpm-python package in EL6 and 7, so just simply to
# remove rpm-py-installer for now.
Patch0:         remove-koji-and-rpm-py-installer-from-requires.patch
Patch1:         0001-Repair-downloading-sources-into-external-directory.patch
Patch2:         0002-Repair-compatible-formatting-for-Python-2.6.patch
Patch3:		0003-Switch-from-krb_login-to-gssapi_login.patch

%if 0%{?fedora} || 0%{?rhel} > 7
# Disable python2 build by default
%global with_python2 0
# Enable python3 build by default
%global with_python3 1
%else
%global with_python2 1
%global with_python3 0
# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python2_sitelib: %global python2_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?__python2: %global __python2 %{__python}}
%endif

%description
Python library for interacting with rpm+git


%if 0%{?with_python2}
%package -n python2-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{name}}

BuildRequires:  python2-devel

# We br these things for man page generation due to imports
BuildRequires:  rpmlint
BuildRequires:  python2-koji >= 1.17
BuildRequires:  python2-cccolutils
BuildRequires:  PyYAML

%if 0%{?rhel}
BuildRequires:  GitPython
BuildRequires:  python-pycurl
BuildRequires:  python-requests
BuildRequires:  python-six >= 1.9.0
%else
BuildRequires:  python2-GitPython
BuildRequires:  python2-pycurl
BuildRequires:  python2-requests
BuildRequires:  python2-six >= 1.9.0
BuildRequires:  python2-openidc-client
BuildRequires:  python2-libmodulemd
%endif

%if 0%{?rhel} && 0%{?rhel} < 7
BuildRequires:  python-argparse
BuildRequires:  python-mock
BuildRequires:  python-nose
BuildRequires:  python-setuptools
BuildRequires:  python-unittest2
%else
BuildRequires:  python2-mock
BuildRequires:  python2-nose
BuildRequires:  python2-setuptools
%endif

Requires:       mock
Requires:       redhat-rpm-config
Requires:       rpm-build
Requires:       rpmlint

Requires:       python2-cccolutils
Requires:       python2-koji >= 1.17
Requires:       PyYAML

%if 0%{?rhel}
Requires:       GitPython >= 0.2.0
Requires:       python-pycurl
Requires:       python-requests
Requires:       python-six >= 1.9.0
Requires:       rpm-python
%else
Requires:       python2-GitPython
Requires:       python2-rpm
Requires:       python2-pycurl
Requires:       python2-six >= 1.9.0
Requires:       python2-libmodulemd
%endif

%if 0%{?rhel} && 0%{?rhel} < 7
Requires:       python-argparse
%endif

Requires:       %{name}-common = %{version}-%{release}

Conflicts:      fedpkg < 1.26

# Backward compatibility with capability pyrpkg
Provides: pyrpkg = %{version}-%{release}
# All old versions before 1.49-1 should not be used anymore
Obsoletes: pyrpkg < 1.49-2


%description -n python2-%{name}
A python library for managing RPM package sources in a git repository.
%endif
# end of python2 section


%if 0%{?with_python3}
%package -n python3-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{name}}
# Obsolete python2-rpkg (remove after Fedora29)
%if 0%{?with_python2} == 0
Obsoletes:      python2-rpkg < %{version}-%{release}
%endif

BuildRequires:  python3-devel
BuildRequires:  python3-GitPython
BuildRequires:  python3-koji >= 1.17
%if 0%{?rhel} > 7
BuildRequires:  python3-gobject-base
BuildRequires:  libmodulemd
%else
BuildRequires:  python3-libmodulemd
%endif
BuildRequires:  python3-cccolutils
BuildRequires:  python3-openidc-client
BuildRequires:  python3-mock
BuildRequires:  python3-pycurl
BuildRequires:  python3-six >= 1.9.0
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-PyYAML
BuildRequires:  rpmlint

Requires:       mock
Requires:       redhat-rpm-config
Requires:       rpm-build
Requires:       rpmlint

Requires:       python3-GitPython >= 0.2.0
Requires:       python3-cccolutils
Requires:       python3-koji >= 1.17
%if 0%{?rhel} > 7
Requires:       python3-gobject-base
Requires:       libmodulemd
%else
Requires:       python3-libmodulemd
%endif
Requires:       python3-rpm
Requires:       python3-pycurl
Requires:       python3-six >= 1.9.0
Requires:       python3-PyYAML

Requires:       %{name}-common = %{version}-%{release}

Conflicts:      fedpkg < 1.26

%description -n python3-%{name}
A python library for managing RPM package sources in a git repository.
%endif
# end of python3 section


%package common
Summary:        Common files for %{name}

# Files were moved from python2-rpkg in that version
Conflicts:      python2-rpkg < 1.52-2
Conflicts:      pyrpkg < 1.52-2

%description common
Common files for python2-%{name} and python3-%{name}.


%prep
%autosetup -p1

# Removes section from setup.py that is relevant only for pip and
# is not compatible with in RHEL-6 tools
sed -i -n '/extras_require/,/}/!p' setup.py

%build
%if 0%{?with_python2}
%{__python2} setup.py build
%endif

%if 0%{?with_python3}
%py3_build
%endif


%install
%if 0%{?with_python2}
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%endif

%if 0%{?with_python3}
%py3_install
%endif


# Create configuration directory to holding downstream clients config files
# that are built on top of rpkg
%{__install} -d $RPM_BUILD_ROOT%{_sysconfdir}/rpkg

example_cli_dir=$RPM_BUILD_ROOT%{_datadir}/%{name}/examples/cli
%{__install} -d $example_cli_dir

# Install example CLI to rpkg own data directory
%{__install} -d ${example_cli_dir}%{_bindir}
%{__install} -d ${example_cli_dir}%{_sysconfdir}/bash_completion.d
%{__install} -d ${example_cli_dir}%{_sysconfdir}/rpkg

%{__install} -p -m 0644 bin/rpkg ${example_cli_dir}%{_bindir}
%{__install} -p -m 0644 etc/bash_completion.d/rpkg.bash ${example_cli_dir}%{_sysconfdir}/bash_completion.d
%{__install} -p -m 0644 etc/rpkg/rpkg.conf ${example_cli_dir}%{_sysconfdir}/rpkg


%check
# cannot use python2 -m nose on EPEL 6 (Python 2.6)
%if 0%{?with_python2}
nosetests tests
%endif

%if 0%{?with_python3}
%{__python3} -m nose tests
%endif


%if 0%{?with_python2}
%files -n python2-%{name}
%doc README.rst CHANGELOG.rst
%if 0%{?rhel} && 0%{?rhel} < 7
%doc COPYING COPYING-koji LGPL
%else
%license COPYING COPYING-koji LGPL
%endif
# For noarch packages: sitelib
%{python2_sitelib}/pyrpkg
%{python2_sitelib}/%{name}-%{version}-py*.egg-info
%endif

%if 0%{?with_python3}
%files -n python3-%{name}
%doc README.rst CHANGELOG.rst
%license COPYING COPYING-koji LGPL
%{python3_sitelib}/pyrpkg
%{python3_sitelib}/%{name}-%{version}-py*.egg-info
%endif

%files common
%{_datadir}/%{name}
%{_sysconfdir}/rpkg


%changelog
* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.60-4
- Rebuilt for Python 3.9

* Tue May 19 2020 Ondřej Nosek <onosek@redhat.com> - 1.60-3
- Patch: Switch from krb_login to gssapi_login

* Mon May 11 2020 Ondřej Nosek <onosek@redhat.com> - 1.60-2
- Releasing the epel8 version

* Fri Mar 20 2020 Ondřej Nosek <onosek@redhat.com> - 1.60-1
- More transparent check of retired package (onosek)
- Run newer version of sphinx-build tool (onosek)
- Lookaside cache upload is not based on an extension - #484 (onosek)
- container-build: additional warning when using --release (mlangsdo)
- allow compose-id with repo-url for container_build (rcerven)
- Clone config customization for namespaces - 231 (onosek)
- Repair Jenkins tests (onosek)
- (new-)sources should fail with git tracked files - 241 (onosek)
- Handle new cachito dependency replacement argument (athoscr)
- module-build optional key help - 280 (onosek)
- Modify watch-cancel message (sgallagh)
- Create stats for module builds in 'init' state (csomh)
- RPM 4.15 changed header returns from type 'bytes' to 'string'. Handle either
  by converting to 'string' if necessary. (mmathesi)
- Don't expect module build tasks to have "rpms" (mulaieva)
- Propagate module_hotfixes to getMockConfig - rhbz#1780228 (lsedlar)
- Add check for wrong repo name format during clone - 353 (onosek)
- Simplify methods for getting namespace giturl (onosek)
- Use a single thread pool while watching module builds (csomh)
- Also capture stderr in logfile (orion)
- Line up descriptions for better code readability (onosek)
- Isolated container-build should allow arches override (rcerven)
- container-build: add --koji-parent-build argument (kdreyer)
- tests: add container-build --isolated test (kdreyer)
- container-build: add --isolated argument (kdreyer)
- Pass skip_build option to buildContainer (rcerven)
- Reuse koji_cli.lib.unique_path (cqi)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.59-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Ondřej Nosek <onosek@redhat.com> - 1.59-5
- Some patches:
- Propagate module_hotfixes to getMockConfig
- Don't expect module build tasks to have "rpms"
- RPM 4.15 changed header - type conversion
- Create stats for module builds in 'init' state

* Tue Dec 03 2019 Ondřej Nosek <onosek@redhat.com> - 1.59-4
- Patch: limited thread pool for watching module builds

* Thu Nov 14 2019 Ondřej Nosek <onosek@redhat.com> - 1.59-3
- Backport: Isolated container-build should allow arches override

* Fri Oct 25 2019 Ondrej Nosek <onosek@redhat.com> - 1.59-2
- Backport: container-build: add --isolated and --koji-parent-build arguments
- Backport: Pass skip_build option to buildContainer
- Backport: Reuse koji_cli.lib.unique_path

* Mon Sep 16 2019 Ondřej Nosek <onosek@redhat.com> - 1.59-1
- Add argument to skip build option for container-build (rcerven)
- Sorting imports (onosek)
- Ignore error when adding exclude patterns - 1733862 (onosek)
- Path to lookaside repo fix (onosek)
- Add commands for interacting with Koji side-tag plugin - 329 (lsedlar)
- Do not delete files related to gating on import (onosek)
- Support integer values in the optional module-build arguments (mprahl)
- container-build: add --build-release argument (kdreyer)
- Allow some arguments for container-build together (onosek)
- git-changelog: Fix running on Python 3 - 3 (onosek)
- Port to libmodulemd 2 API (lsedlar)
- Module-overview allows filtering by owner - 325 (onosek)
- Different import --offline command behavior - #445 (onosek)
- Show nvr in container-build (onosek)
- Custom handler for koji watch_tasks (onosek)
- Unittests for clone command (onosek)
- Fix clone --branches - rhbz#1707223 (tmz)
- Make gitbuildhash work for windows builds (lsedlar)

* Mon Sep 16 2019 Ondřej Nosek <onosek@redhat.com> - 1.58-10
- Update koji dependency

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.58-9
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Ondřej Nosek <onosek@redhat.com> - 1.58-8
- Obsoletes python2-rpkg after upgrade to Fedora30

* Wed Jul 31 2019 Stephen Gallagher <sgallagh@redhat.com> - 1.58-7
- Fix libmodulemd requirements

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.58-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Ondřej Nosek <onosek@redhat.com> - 1.58-5
- Now again, libmodulemd is required instead of python3-libmodulemd because
  it was causing troubles with upgrades.

* Mon Jun 10 2019 Ondřej Nosek <onosek@redhat.com> - 1.58-4
- Modify required version of koji package

* Mon May 27 2019 Ondřej Nosek <onosek@redhat.com> - 1.58-3
- Backport: Custom handler for koji watch_tasks
- Backport: Show nvr in container-build
- Backport: Different import --offline command behavior

* Thu May 09 2019 Ondrej Nosek <onosek@redhat.com> - 1.58-2
- Backport: fixed 'clone --branch' command

* Mon Apr 29 2019 Ondřej Nosek <onosek@redhat.com> - 1.58-1
- Ignore files in a cloned repository - #355 (onosek)
- Handle data from python RPM binding as UTF-8 string (zebob.m)
- srpm_import: be compatible with rhbz#1693751 (praiskup)
- Pass --enable-network to mock - 314 (onosek)
- Enhance 'module-overview' sub-command to show scratch status of modules.
  (mmathesi)
- Remove the ability to parse a module's branch automatically to determine the
  base module stream override (mprahl)
- Improvements for scratch module builds (mmathesi)
- Updates to support scratch module builds (mmathesi)
- Refactor fake Koji credential handling from TestBuildPackage class into new
  FakeKojiCreds class so it can be shared with TestModulesCli class. (mmathesi)
- Make Koji upload methods more generic so they can be reused. (mmathesi)
- Allow passing --offline and -r to mbs-manager build_module_locally. (jkaluza)
- Depth param for clone - tuning (onosek)
- Depth param for clone - #363 (onosek)
- Pass --disablerepo and --enablerepo to mock - 313 (onosek)
- Import srpm without uploading sources - rhbz#1175262 (onosek)
- Ignore any specified profile when finding the Flatpak build target (otaylor)
- Show module build links in output from command module-build (cqi)
- Add 'retire' command supporting both packages and modules (mmathesi)
- Fix "push --force" (tim)
- Container-build returns its status to command-line - #415 (onosek)
- Upload .crate files to lookaside cache - 312 (onosek)
- Restrict version of PyYAML on Python 2.6 (lsedlar)
- Simplify srpm method (onosek)
- Permit setting arbitrary rpm macros during build (riehecky)
- Add the ability to configure multiple regex expressions for
  base_module_stream_regex_from_branch (mprahl)
- Do not require PyGObject in setup.py - rhbz#1679365 (onosek)
- Fixing failing Jenkins tests (onosek)
- Unify update-docs script with fedpkg version (onosek)
- README: add links (onosek)
- Watch multiple module builds (cqi)
- Added update-docs script (onosek)

* Thu Apr 25 2019 Ondřej Nosek <onosek@redhat.com> - 1.57-9
- yet another compat fix with RPM after rhbz#1693751

* Fri Apr 19 2019 Pavel Raiskup <praiskup@redhat.com> - 1.57-8
- compat fix with RPM after rhbz#1693751

* Wed Mar 20 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.57-7
- Backport patch for uploading *.crate into lookaside

* Thu Feb 07 2019 Ondřej Nosek <onosek@redhat.com> - 1.57-6
- Revert previous change.
  Now python-gobject-base & libmodulemd are removed from epel7 and RHEL7

* Tue Feb 05 2019 Ondřej Nosek <onosek@redhat.com> - 1.57-5
- python-gobject-base & libmodulemd also for epel7 and RHEL7

* Mon Feb 04 2019 Lubomír Sedlář <lsedlar@redhat.com> - 1.57-4
- Disable Py2 package on F30+

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.57-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Ondřej Nosek <onosek@redhat.com> - 1.57-2
- Merge changes of the .spec files for Fedora and RHEL

* Thu Dec 13 2018 Ondřej Nosek <onosek@redhat.com> - 1.57-1
- Use idna 2.7 for Python 2.6 (lsedlar)
- Imports are sorted (onosek)
- libmodulemd is missing on el7 - #402 (onosek)
- Initialize bash autocompletion (onosek)
- Set configuration in case of "clone --branches" as well (tim)
- Fix fake spec file for clog tests (cqi)
- Move argparse fix from fedpkg - #398 (onosek)
- Send source mtime to dist-git - 220 (lsedlar)
- Fix tests for mock package manager (lsedlar)
- Specify package manager for mock-config (lsedlar)
- Add contributing guide (onosek)
- Validate the module build optional argument when parsing the argument
  (mprahl)
- Add config options to parse the base module (e.g. platform) stream from the
  dist-git branch and apply a buildrequire override (mprahl)
- Add the ability to pass in buildrequire and require overrides on a module
  build (mprahl)
- Raise an error if the module build command receives optional arguments that
  conflict (mprahl)
- Silence Python3 SafeConfigParser warnings (mmathesi)
- Allow to pass posargs to tox from make (cqi)
- Specify dependent packages in one place (cqi)
- Don't registry flatpak-build command on Python-2.6 (otaylor)
- Add flatpak-build subcommand (otaylor)
- Don't pass the MBS API URL around as a parameter (otaylor)
- TestContainerBuildWithKoji: tear down the mock appropriately (otaylor)
- Refine test runner for py26 (cqi)

* Thu Nov 15 2018 Ondřej Nosek <onosek@redhat.com> - 1.56-4
- Allow build for RHEL-8  (onosek)

* Wed Nov 14 2018 Ondřej Nosek <onosek@redhat.com> - 1.56-3
- No mock warning (onosek)

* Fri Sep  7 2018 Owen Taylor <otaylor@redhat.com> - 1.56-2
- Add patch from upstream pull-request to add a flatpak-build subcommand
- Add PyYAML dependencies so that the spec file at least builds on epel6/epel7

* Tue Aug 21 2018 Chenxiong Qi <cqi@redhat.com> - 1.56-1
- Validate greenwave policy early in Commands.build (cqi)
- Refine error message for failure gating.yaml validation (cqi)
- explain mbs-manager exception handling (nils)
- test for missing mbs-manager with errno set (nils)
- catch errno == ENOENT if mbs-manager is missing (nils)
- add missing method docstring (nils)
- Show full error from MBS (lsedlar)
- Fix tests for greenwave policy validation (cqi)
- Add testenv for building docs (cqi)
- New option --buildrootdir - rhbz#1583822 (cqi)
- Add --shell option to mockbuild - rhbz#1438685 (cqi)
- Validate gating.yaml file for Greenwave gating (gnaponie)
- Update README (cqi)
- Reduce the number of repo creation for tests (cqi)
- Fix flake8 error (cqi)
- Drop rpm-py-installer from requires - #357 (cqi)
- Allow _run_command to capture and return output to stdout or stderr (cqi)
- Claim Python 3.7 in README and package classifiers (cqi)
- Fix a bad test teardown (otaylor)
- Refactor build command (cqi)
- Remove rpmfluff package (cqi)
- Set PYCURL_SSL_LIBRARY directly for installing pycurl (cqi)
- Add py37 testenv (cqi)

* Thu Jul 26 2018 Chenxiong Qi <cqi@redhat.com> - 1.55-2
- Remove dependency python-rpmfluff

* Mon Jul 23 2018 Chenxiong Qi <cqi@redhat.com> - 1.55-1
- Fix installing pycurl for running tests (cqi)
- Replace extra module_name with repo_name (cqi)
- Replace name module with repo in tests/fixtures/rpkg*.conf (cqi)
- Add --fail-fast functionality - #331 (tibbs)
- Fix fake spec for build in rawhide (cqi)
- Avoid to upload a file with different checksum - #204 (cqi)
- Give more information when sources has invalid content - #227 (cqi)
- Reserve README.md while import srpm - #149 (cqi)
- Set to repo_name property when --name is specified (cqi)
- Do not restrict argparse version (cqi)
- Check old format args only if there is clone config (cqi)
- Fix typo and reword option help and deprecation message (cqi)
- Massive replacement of module (cqi)
- Deprecate module_name inside rpkg internal (cqi)
- Add new option --name and --namespace - #301 (cqi)
- Man generator indent workaround (onosek)
- Fixing imports in unittests (onosek)
- Minor fixes to doc build (cqi)
- Fix mistakes during rebase (cqi)
- Run document generator script in Py3 explictly (cqi)
- Remove warning of nonexisting source/_static/ during doc build (cqi)
- Do not generate document for sample rpkg app (cqi)
- Exclude subcommand which does not have help (cqi)
- Ensure to clean files for generating HTML documents (cqi)
- Fix rebase error: add module_build_watch back (cqi)
- Fix MANIFEST.in to list files for building doc (cqi)
- Rename generate_man_pages.py (cqi)
- Generate HTML document and manpage for sample rpkg (cqi)
- Simplify doc Makefile (cqi)
- Generate commands HTML and man pages (cqi)
- Update existing docstrings (cqi)
- Generate documents by sphinx - #50 (cqi)
- README: new code should be py3 compatible (ktdreyer)
- Provide base_module to clone_config templates - #326 (tmz)
- Refactor man generator to be reusable (puiterwijk)
- Make sure gitcred doesn't land in man (puiterwijk)
- Don't inject the credential helper to push if OIDC is unconfigured
  (puiterwijk)
- Add docblocks to gitcred methods and don't quit if OpenIDC is unconfigured
  (puiterwijk)
- Also inject the credential helper with rpkg push (puiterwijk)
- Create a "gitcred" command that functions as an OIDC git-credential helper
  (puiterwijk)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.54-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.54-3
- Rebuilt for Python 3.7

* Mon May 21 2018 Chenxiong Qi <cqi@redhat.com> - 1.54-2
- Remove koji and rpm-py-installer Python package requires
- Fix argparse version for el6

* Fri May 11 2018 Chenxiong Qi <cqi@redhat.com> - 1.54-1
- Pass the -s/--set-default-stream to mbs-manager for module local builds.
  (jkaluza)
- Write mock config correctly when run in Py 3 (cqi)
- Add --with and --without options to 'local' - rhbz#1533416 (tmz)
- Add a test for 3f93433 (cqi)
- Raise error if rpm command returns non-zero (cqi)
- Use getpass.getuser() instead of pwd.getpwuid(os.getuid())[0] (jpopelka)
- Allow setting custom MBS config file and config section in rpkg.conf.
  (jkaluza)
- Remove py35 testenv (cqi)
- Ignore .env and tags (cqi)
- Remove question mark from giturl (cqi)
- Added custom ArgumentParser (supports allow_abbrev) (jkucera)
- Grab the correct first line in case of rpm output (zebob.m)

* Mon Apr 16 2018 Chenxiong Qi <cqi@redhat.com> - 1.53-2
- Require python2-koji 1.15 as the minimum version
- Refine BuildRequires

* Tue Apr 10 2018 Chenxiong Qi <cqi@redhat.com> - 1.53-1
- Use NSVs and not build IDs with module-build-local --add-local-build (mprahl)
- Fix docstring of test_module_build_local_with_skiptests (mprahl)
- Add long_description to package (cqi)
- Support local module builds when there are uncommitted changes (mprahl)
- Fix clarifying error that occurs when mbs-manager is not installed (mprahl)
- Add support for Module Stream Expansion (MBS API v2) (mprahl)
- Show errors when a module build fails (mprahl)
- Move full download url construction to separate method (frostyx)
- Fix compose related params for container-build (lucarval)
- Avoid calling /usr/bin/python in tests (miro)
- Change default rpmlint configuration file (athoscr)
- Use koji.grab_session_options() rather than opencoding it (cfergeau)

* Mon Mar 05 2018 Miro Hrončok <mhroncok@redhat.com> - 1.52-2
- Introduce python3 subpackage

* Thu Feb 22 2018 Chenxiong Qi <cqi@redhat.com> - 1.52-1
- Mock ThreadPool in test_module_overview (cqi)
- Drop rpmfluff in test (cqi)
- Fix hardcoded directory name in test (lsedlar)
- Improve testenv for py26 (cqi)
- Run tests with old GitPython in py26 testenv (cqi)
- Compile pycurl with openssl after F27 (cqi)
- Ignore .egg/ from git (cqi)
- Add py26 to testenv (cqi)
- Install koji from PyPI (cqi)
- Make compose-id and repo-url to take one or more values (csomh)
- Let git ignore more directories (cqi)
- Exclude pyc and __pycache__ globally in sdist (cqi)
- Handle nonexisting mbs-manager (cqi)
- Add dependent packages for Python 2.6 in setup.py (cqi)
- Updated module cli API (mcurlej)
- Declare Python versions rpkg can work with - #278 (cqi)
- Fix flake8 errors (cqi)
- Fix tests that do not work with Python 3 (cqi)
- Fix tests: not impact by dict.items call (cqi)
- Add py36 to testenv - #274 (cqi)
- Run tox to run tests and check code styles - #276 (cqi)
- Use flake8 3.5.0 (cqi)
- Add files under requirements/ to sdist package (cqi)
- Install Koji shared library via setuptools (cqi)
- Set install and tests requires in setup.py (cqi)
- Split pypi requirements and refine versions (cqi)
- Change type of compose id from string to int (bfontecc)
- Install RPM Python binding from PyPI (cqi)
- Fix test test_lint_each_file_once (cqi)
- Add compose-id and signing-intent arguments (bfontecc)
- Use env's python (lucarval)
- Use progress callback and TaskWatcher from koji_cli.lib (cqi)
- Get buildhash from git+https:// url (lsedlar)
- lint: Avoid checking rpm's multiple times (tmz)
- Fix giturl as well by calling construct_build_url (cqi)
- Fix construct anongiturl for chain-build (cqi)
- Fix mock openidc_client (cqi)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Chenxiong Qi <cqi@redhat.com> - 1.51-3
- Backport: Add compose-id and signing-intent arguments
- Backport: Change type of compose id from string to int

* Wed Nov 08 2017 Chenxiong Qi <cqi@redhat.com> - 1.51-2
- Backport: Fix construct anongiturl for chain-build
- Backport: Fix giturl as well by calling construct_build_url

* Fri Oct 20 2017 Chenxiong Qi <cqi@redhat.com> - 1.51-1
- Ignore TestModulesCli if openidc-client is unavailable (cqi)
- Port mbs-build to rpkg (mprahl)
- Add .vscode to .gitignore (mprahl)
- Fix TestPatch.test_rediff in order to run with old version of mock (cqi)
- Allow to specify alternative Copr config file - #184 (cqi)
- Tests for patch command (cqi)
- More Tests for mockbuild command (cqi)
- More tests for getting spec file (cqi)
- Tests for container-build-setup command (cqi)
- Test for container-build to use custom config (cqi)
- Suppress output from git command within setUp (cqi)
- Skip test if rpmfluff is not available (lsedlar)
- Allow to override build URL (cqi)
- Test for mock-config command (cqi)
- Tests for copr-build command (cqi)
- Fix arch-override for container-build (lucarval)
- Remove unsupported osbs for container-build (lucarval)
- cli: add --arches support for koji_cointainerbuild (mlangsdo)
- Strip refs/heads/ from branch only once (lsedlar)
- Don't install bin and config files (cqi)
- Fix kojiprofile selection in cliClient.container_build_koji (cqi)
- Avoid branch detection for 'rpkg sources' (praiskup)
- Fix encoding in new command (cqi)
- Minor wording improvement in help (pgier)
- Fix indentation (pviktori)
- Add --with and --without options to mockbuild (pviktori)

* Thu Aug 31 2017 Chenxiong Qi <cqi@redhat.com> - 1.50-2
- Backport: Fix kojiprofile selection in cliClient.container_build_koji (cqi)

* Thu Aug 10 2017 Chenxiong Qi <cqi@redhat.com> - 1.50-1
- Fix PEP8 error (cqi)
- Spelling fixes (ville.skytta)
- Reword help and description of new-sources and upload commands - rhbz#1248737
  (cqi)
- Set autorebuild enabled by default (bfontecc)
- Add commands to whitelist_externals (cqi)
- Declare Python 3 versions to support in setup.py (cqi)
- Replace unicode with six.text_type (cqi)
- Run tests in both Python 2 and 3 with tox (cqi)
- Make tests and covered code compatible with Py3 (cqi)
- Add requirements files (cqi)
- Do not build srpm in test (cqi)
- Do not actually run git-diff in tests (cqi)
- Remove deprecated modules used in koji (cqi)
- Non-zero exit when rpmbuild fails in local command (cqi)
- Report deprecation of config via logger (lsedlar)
- Print --dist deprecation warning explicitly (lsedlar)
- utils: Avoid DeprecationWarning for messages for users (lsedlar)
- Supply namespace to lookaside (if enabled) (lsedlar)
- Support reading koji config from profile - #187 (cqi)
- Remove kitchen (cqi)
- Fix string format (cqi)
- Recommend --release instead of --dist in mockbuild --help (tmz)
- Allow overriding container build target by downstream (lsedlar)
- Add a separate property for namespace (lsedlar)
- Allow container builds from any namespace (maxamillion)
- Make osbs support optional (cqi)
- make osbs dependency optional (pavlix)
- Allow explicit namespaces with slashes (lsedlar)
- Do not hang indefinitely when lookaside cache server stops sending data
  (jkaluza)
- Make --module-name work with namespaces - #216 (lsedlar)
- Include README.rst in dist package (cqi)
- More document in README - #189 (cqi)
- Make new command be able to print unicode - #205 (cqi)
- Allow to specify custom info to a dummy commit (cqi)
- Load module name correctly even if push url ends in slash - #192 (cqi)
- Replace fedorahosted.org with pagure.io - #202 (cqi)
- Fix rpm command to get changelog from SPEC - rhbz#1412224 (cqi)
- Rewrite tests to avoid running rpmbuild and rpmlint (cqi)
- Use fake value to make Command in test (cqi)
- Python 3.6 invalid escape sequence deprecation fixes (ville.skytta)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Chenxiong Qi <cqi@redhat.com> - 1.49-6
- Rename koji to python2-koji

* Thu Jun 29 2017 Lubomír Sedlář <lsedlar@redhat.com> - 1.49-5
- Allow using namespace in --module-name attribute

* Thu Jun 22 2017 Chenxiong Qi <cqi@redhat.com> - 1.49-4
- Remove python-osbs-client

* Fri Jun 16 2017 Chenxiong Qi <cqi@redhat.com> - 1.49-3
- Backport to make osbs optional

* Mon Mar 27 2017 Chenxiong Qi <cqi@redhat.com> - 1.49-2
- Rebuilt to rename pyrpkg to python2-rpkg

* Wed Feb 22 2017 Chenxiong Qi <cqi@redhat.com> - 1.49-1
- More upload PyCURL fixes for EL 7 (merlin)
- Move tag inheritance check into a separate method (cqi)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 1 2017 Lubomír Sedlář <lsedlar@redhat.com> - 1.48-2
- Backport patch to move tag inheritance check to separate method

* Thu Dec 22 2016 Chenxiong Qi <cqi@redhat.com> - 1.48-1
- Better message when fail to authenticate via Kerberos - #180 (cqi)

* Mon Dec 19 2016 Chenxiong Qi <cqi@redhat.com> - 1.47-7
- Refactor Commands._srpmdetails (cqi)

* Thu Dec 15 2016 Chenxiong Qi <cqi@redhat.com> - 1.47-6
- Add missing import koji.ssl.SSLCommon - BZ#1404102 (cqi)
- Fix upload with old PyCURL - BZ#1241059 (lsedlar)

* Mon Dec 12 2016 Lubomír Sedlář <lsedlar@redhat.com> - 1.47-5
- Fix default value for krb_rdns options

* Mon Dec 12 2016 Lubomír Sedlář <lsedlar@redhat.com> - 1.47-4
- Add krb_rdns koji config

* Thu Dec 08 2016 Lubomír Sedlář <lsedlar@redhat.com> - 1.47-3
- Conflict with too old fedpkg

* Wed Dec 07 2016 Chenxiong Qi <cqi@redhat.com> - 1.47-2
- Fix test that fails on a Koji ARM builder

* Fri Dec 02 2016 Chenxiong Qi <cqi@redhat.com> - 1.47-1
- New upstream release 1.47

* Tue Oct 25 2016 Lubomír Sedlář <lsedlar@redhat.com> - 1.46-5
- Allow using gssapi for lookaside caches

* Tue Sep 06 2016 Lubomír Sedlář <lsedlar@redhat.com> - 1.46-4
- Update dependencies for python-argparse and python-hashlib

* Thu Aug 25 2016 Chenxiong Qi <cqi@redhat.com> - 1.46-3
- python-six-1.9.0 is the minimum version rpkg depends

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.46-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 15 2016 Chenxiong Qi <cqi@redhat.com> - 1.46-1
- Warning untracked patches when push (cqi)
- handle correct spec path when push from outside the repo (cqi)
- Remove support for BuildContainer release task opt (lucarval)

* Mon Jun 27 2016 Chenxiong Qi <cqi@redhat.com> - 1.45-2
- Depend on python-six to be compatible with Python 3

* Mon Jun 27 2016 Chenxiong Qi <cqi@redhat.com> - 1.45-1
- add missing git-config in the git repo for testing (cqi)
- Don't print download/upload progress outside of TTY (lsedlar)
- Merge #58 `Rebase of #28 with conflict resolved` (cqi)
- Get correct login without TTY (vgologuz)
- Merge #63 `More Python 3 compatibility fixes` (lubomir.sedlar)
- fix broken when non-ASCII in path (cqi)
- More Python 3 compatibility fixes (ville.skytta)
- Fix push called without argument (lsedlar)
- Use logging.warning instead of deprecated logging.warn (ville.skytta)
- Use assertEqual instead of deprecated assertEquals (ville.skytta)
- Spelling fixes (ville.skytta)
- Add missing dependencies to setup.py (ville.skytta)
- Add tests for cloning with a namespace (lsedlar)
- Fix cloning with -B and namespaced module (lsedlar)
- Adjust figuring out the path of the git repo cloned (pingou)
- Only clone into the bare_dir if no target was specified (pingou)
- Add to the CLI the possibility to specify a target folder for the clone
  (pingou)
- Add unit-tests for cloning into a specified directory (pingou)
- Let rpkg support cloning into a specified directory (pingou)
- Python 3 fixes (ville.skytta)
- rewrite test_commands.setup_module using git (cqi)
- Merge #40 `push: check for missing patches` (lubomir.sedlar)

* Thu Jun 02 2016 Lubomír Sedlář <lsedlar@redhat.com> - 1.44-1
- Log container-build task results (lucarval)
- Add support for BuildContainer release task opt (lucarval)
- handle exception from getTaskInfo correctly (cqi)
- fix failure of test_load_spec_where_path_contains_space on RHEL (cqi)
- allow space appearing in path to cloned repo (cqi)
- fix docstring of Commands.compile (cqi)
- Make 'Failed to get ns_module_name from Git url or pushurl' message a warning
  (issue #42) (orion)
- pyrpkg: use git remote get-url --push (mathstuf)

* Wed Mar 23 2016 Lubomír Sedlář <lubomir.sedlar@gmail.com> - 1.43-1
- Print warning when using old git configuration (lsedlar)
- Add rpms namespace for checkouts without namespace (lsedlar)

* Wed Mar 16 2016 Lubomír Sedlář <lubomir.sedlar@gmail.com> - 1.42-1
- Fix problems with namespacing (maxamillion)

* Mon Mar 14 2016 Lubomír Sedlář <lubomir.sedlar@gmail.com> - 1.41-2
- Depend on python-osbs directly to avoid python3

* Mon Mar 14 2016 Lubomír Sedlář <lubomir.sedlar@gmail.com> - 1.41-1
- Update upstream URL (lsedlar)
- Fixes based on lsedlar's feedback (maxamillion)
- add distgit namespacing for non-rpm content (docker, xdg-app, etc) (maxamillion)
- Container-build: dont't allow to build with unpushed changes (araszka)
- Suggest --dist option when can't get OS ver from branch (araszka)
- fix: print all tags without filter (araszka)
- Fix lookaside upload when --path is specified (araszka)
- Lookaside: encoding repo name to UTF-8 (araszka)
- Fix errors on Python 2.6 (lsedlar)
- Add test and docstring to byte offset convertor (araszka)
- Decode .spec file with UTF-8 (araszka)
- 1271741 - add copr command (Recommends: copr-cli) (msuchy)
- Suggest --target option when unknown target (araszka)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 23 2015 Pavol Babincak <pbabinca@redhat.com> - 1.40-1
- don't use assertRaises (ttomecek)
- refactor test_clone: set clone config in the same test file (pbabinca)
- Fix clone test to not use constructor to set clone_config (pbabinca)
- Fix test clone test (pbabinca)
- Make use of clone_config attribute backwards compatible (pbabinca)

* Thu Oct 22 2015 Pavol Babincak <pbabinca@redhat.com> - 1.39-1
- Replace deprecated BaseException.message with str(BaseException) (pbabinca)
- Don't print exception message during check repo tests (pbabinca)
- Add support for setting post-clone git config (ville.skytta)

* Wed Oct 21 2015 Pavol Babincak <pbabinca@redhat.com> - 1.38-1
- Fix parse error (pbabinca)

* Wed Oct 21 2015 Pavol Babincak <pbabinca@redhat.com> - 1.37-1
- Add support for --nocheck (orion)
- container-build: check repo (ttomecek)
- move repo checking to a method (ttomecek)
- Add 'oxt' and 'xpi' extensions to UPLOADEXTS (dsilakov)
- Switch-branch: give more info about error (araszka)
- Recognize binary files with .oxt and .xpi extensions (dsilakov)
- Container-build: add --nowait option (araszka)
- bash autocompletion: support for command container-build-config (pbabinca)
- Implement getter for autorebuild value, use 'true' and 'false' for values
  (bkabrda)
- Add a command and option to change container build setup (bkabrda)
- Edit tests for python2.6 - EL6 (araszka)
- tests: Don't use assertNotIn (araszka)
- tests: Don't use assertRaises as context manager (araszka)
- tests: Don't use check_output (araszka)
- Typo in import --help descriptions (araszka)
- change the url for rpkg (dennis)

* Wed Jul 15 2015 Pavol Babincak <pbabinca@redhat.com> - 1.36-1
- container-build: support yum repos with --build-with=koji (pbabinca)
- container-build: move --scratch option to koji group (pbabinca)
- Print task info for container-build (pbabinca)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Dennis Gilmore <dennis@ausil.us> - 1.35-2
- pyrpkg Requires python-osbs

* Tue May 26 2015 Pavol Babincak <pbabinca@redhat.com> - 1.35-1
- Test for scratch opt in the actual argument of container_build_koji
  (pbabinca)
- Move the GitIgnore class to its own module (bochecha)
- Modernize the gitignore-handling code (bochecha)
- gitignore: Properly handle adding matching lines (bochecha)
- Refactor: remove unnecessary code (pbabinca)
- Move custom UnknownTargetError to errors module (pbabinca)
- New command: container-build (jluza)
- lookaside: Take over file uploads (bochecha)
- Remove unnecessary log message (bochecha)
- Stop making source files read-only (bochecha)
- Drop some useless comments (bochecha)
- Only report we're uploading when we actually are (bochecha)
- lookaside: Check if a file already was uploaded (bochecha)
- lookaside: Allow client-side and custom CA certificates (bochecha)
- lookaside: Be more flexible when building the download URL (bochecha)
- lookaside: Use the hashtype for the URL interpolation (bochecha)
- lookaside: Add a progress callback (bochecha)
- lookaside: Handle downloading of source files (bochecha)
- lookaside: Move handling of file verification (bochecha)
- lookaside: Move handling of file hashing (bochecha)
- utils: Add a new warn_deprecated helper (bochecha)
- Add a new lookaside module (bochecha)
- Add a new utils module (bochecha)
- Properly set the logger (bochecha)
- Move our custom errors to their own module (bochecha)
- Don't assume MD5 for the lookaside cache (bochecha)
- Remove dead code (bochecha)
- Use the proper exception syntax (bochecha)

* Thu Apr 16 2015 Pavol Babincak <pbabinca@redhat.com> - 1.34-1
- tests: Don't use assertIsNone (bochecha)
- tests: Don't use assertRaises as a context manager (bochecha)
- Add long --verbose option to -v, new --debug and -d option (pbabinca)

* Mon Apr 13 2015 Pavol Babincak <pbabinca@redhat.com> - 1.33-1
- New mockbuild options: --no-clean --no-cleanup-after (jskarvad)
- Catch ssl auth problems and print more helpful messages (pbabinca)
- New exception - rpkgAuthError to allow clients detect auth problems
  (pbabinca)

* Mon Mar 23 2015 Pavol Babincak <pbabinca@redhat.com> - 1.32-1
- tests: Properly open/close the file (bochecha)
- sources: Support writing in either the old or new format (bochecha)
- sources: Reindent code (bochecha)

* Fri Mar 06 2015 Pavol Babincak <pbabinca@redhat.com> - 1.31-1
- Refactor: remove unused imports from test_sources (pbabinca)
- Don't do several times the same thing (bochecha)
- sources: Forbid mixing hash types (bochecha)
- sources: Move to the new file format (bochecha)
- Rewrite the sources module (bochecha)

* Wed Dec 03 2014 Pavol Babincak <pbabinca@redhat.com> - 1.30-2
- Use %%{__python} instead of %%{__python2} as it might be not defined

* Wed Oct 08 2014 Pavol Babincak <pbabinca@redhat.com> - 1.30-1
- add python-nose as BuildRequires as run tests in check section (pbabinca)
- pass extra data to the Commands object via properties instead of __init__()
  (mikeb)
- clean up Koji login, and properly support password auth (mikeb)
- add --runas option (mikeb)
- run os.path.expanduser on the kojiconfig attribute in case the path is in the
  user's home directory (bstinson)
- Override GIT_EDITOR in tests (pbabinca)
- Massive Flake8 fix (bochecha)
- Fix some more Flake8 issues (bochecha)
- Fix some flake8 issues (bochecha)
- Simplify some code (bochecha)
- Fix typo (bochecha)
- tests: Ensure functioning of Commands.list_tag (bochecha)
- list_tags: Stop executing a command (bochecha)
- list_tags: Fix the docstring (bochecha)
- delete_tag: Stop executing a command (bochecha)
- tests: Ensure functioning of Commands.delete_tag (bochecha)
- add_tag: Run the tag command in the right directory (bochecha)
- tests: Ensure proper functioning of Commands.add_tag (bochecha)
- tests: Factor out some code (bochecha)
- tests: Ensure functioning of Commands.clone (bochecha)
- gitignore: Make sure each line ends with a \n (bochecha)
- gitignore: We're not modified any more after we wrote to disk (bochecha)
- tests: Ensure proper functioning of GitIgnore (bochecha)
- tests: Use nose (bochecha)
- Remove unused import (bochecha)
- Some more PEP8 (bochecha)
- Add classifiers to setup.py (pbabinca)
- Add new sources file parser even with unit tests (pbabinca)
- If source file doesn't exist continue without downloading files (pbabinca)
- Reformat setup.py to be compliant with PEP 8 (pbabinca)

* Tue Sep 30 2014 Pavol Babincak <pbabinca@redhat.com> - 1.28-1
- Compare fuller remote branch name with local branch before build

* Fri Sep 26 2014 Pavol Babincak <pbabinca@redhat.com> - 1.27-1
- Explicitly define pyrpkg's client name for man pages (pbabinca)
- Refactor mock results dir to property (pbabinca)
- Add skip-diffs option for import_srpms (lars)
- Properly remove possible .py when creating man pages (lars)
- Process srpm imports to empty repositories more explicitly (pbabinca)
- Make UPLOADEXTS a class variable that can be extended (lars)
- Introduce self.default_branch_remote for fresh clones (pbabinca)
- On self.path change reset properties which could used old value (pbabinca)
- Remove empty entry from git ls-files to not confuse following code (pbabinca)
- Remove file names during srpm import in more extensible way (pbabinca)
- Fix issue causing all current local builds via fedpkg to use md5 rather than
  sha256 (spot)
- License replaced with official GPL 2.0 license from gnu.org (pbabinca)
- Allow "rpkg commit -s" (pjones)

* Tue Jul 29 2014 Pavol Babincak <pbabinca@redhat.com> - 1.26-1
- rpkg doesn't have a python module so use pyrpkg instead (pbabinca)

* Tue Jul 29 2014 Pavol Babincak <pbabinca@redhat.com> - 1.25-1
- 1.25 release (pbabinca)
- Note to do_imports() doc. (pbabinca)
- Change default option for switch-branch from --no-fetch to --fetch (pbabinca)
- Allow default name of the library to be set by subclasses (pbabinca)
- Use name attribute of cliClient to get configuration (pbabinca)
- Make setup.py executable (pbabinca)
- Use direct git call for fetches (pbabinca)
- Print reason for failed switch-branch (pbabinca)
- Match whole branch with remote name when switching branch (pbabinca)
- Refactor: deduplicate remote & branch_merge (pbabinca)
- De-hardcode 'origin' as the remote name (bochecha)
- Fallback the remote on 'origin' (bochecha)

* Mon Jun 09 2014 Pavol Babincak <pbabinca@redhat.com> - 1.24-1
- 1.24 release (pbabinca)
- Work around signed srpms (Till Maas)
- Properly raise the error (bochecha)
- Ability to skip NVR construction altogether for builds (pbabinca)
- If we failed to parse NVRE from rpm output use better error message
  (pbabinca)
- If command to get NVRE printed anything to stderr log that command (pbabinca)
- Refactor: correctly split string on multi lines (pbabinca)
- Use nvr_check as an optional argument for build (pbabinca)
- 1.23 release (pbabinca)
- Use module_name setter instead of constructor parameter (pbabinca)
- Set pushurl & branch_remote by default (pbabinca)
- 1.22 release (pbabinca)
- Define module name from command line, git url and lastly from spec (pbabinca)
- Revert "Define module name from command line, git url and lastly from spec"
  (pbabinca)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 24 2014 Pavol Babincak <pbabinca@redhat.com> - 1.21-1
- Refactor: split strings on multi lines without spaces from indentation
  (pbabinca)
- Refactor: remove spaces at the end of lines (pbabinca)
- Define module name from command line, git url and lastly from spec (pbabinca)
- Option to skip NVR existence check in build system before build (pbabinca)
- Add an 'epoch' property to pyrpkg.Commands (bochecha)
- Fetch remotes before switch-branch by default (pbabinca)
- Protect rhpkg's --arches argument (pbabinca)

* Tue Feb 18 2014 Dennis Gilmore <dennis@ausil.us> - 1.20-1
- read krbservice from the koji config file (dennis)
- We can assume that rpkg is installed if the (ville.skytta)
- clog: Don't require empty line between changelog entries. (ville.skytta)
- Spelling fixes. (ville.skytta)
- expand %%{name} and %%{verion} macros when checking for unused_patches check
  for .patch and .diff files as patches (dennis)
- clean up some language ambiguities (dennis)
- clog: Support %%changelog tag written in non-lowercase. (ville.skytta)
- add spkg as a binary file extention rhbz#972903 (dennis)
- Fixed version to 1.19 (pbabinca)
- Don't track spec file here (pbabinca)
- 1.20 (pbabinca)
- Mock config temp dir in the form $(target)-$(localarch).$(mktemp)mockconfig
  (pbabinca)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 08 2013 Pavol Babincak <pbabinca@redhat.com> - 1.19-1
- Generate mock-config for mockbuild if needed (rhbz#856928) (pbabinca)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 10 2012 Robert Scheck <robert@fedoraproject.org> - 1.18-3
- Require %%{version}-%%{release} rather %%{name}-%%{version}

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Jesse Keating <jkeating@redhat.com> - 1.18-1
- Use rpmdefines when querying for package name

* Mon Apr 09 2012 Jesse Keating <jkeating@redhat.com> - 1.17-1
- Don't assume master branch for chain builds (jkeating)

* Mon Mar 26 2012 Jesse Keating <jkeating@redhat.com> - 1.16-1
- Only read from .koji/config (jkeating)

* Wed Mar 21 2012 Jesse Keating <jkeating@redhat.com> - 1.15-1
- Fix branch push warning (jkeating)
- Handle CVS based builds when getting build hash (jkeating)

* Mon Mar 12 2012 Jesse Keating <jkeating@redhat.com> - 1.14-1
- Warn if the checked out branch cannot be pushed (jkeating)
- Warn if commit or tag fails and we don't push (#21) (jkeating)
- Honor ~/.koji/config (rhbz#785776) (jkeating)
- Update help output for switch-branch (rhbz#741742) (jkeating)

* Thu Mar 01 2012 Jesse Keating <jkeating@redhat.com> - 1.13-1
- Return proper exit code from builds (#20) (jkeating)
- Fix md5 option in the build parser (jkeating)
- More completion fixes (jkeating)
- Add mock-config and mockbuild completion (jkeating)
- Simplify test for rpkg availability. (ville.skytta)
- Fix ~/... path completion. (ville.skytta (jkeating)
- Add a --raw option to clog (#15) (jkeating)
- Make things quiet when possible (jkeating)
- Fix up figuring out srpm hash type (jkeating)
- Allow defining an alternative builddir (jkeating)
- Conflict with older fedpkg (jkeating)
- Attempt to automatically set the md5 flag (jkeating)
- Use -C not -c for config.  (#752411) (jkeating)
- Don't check gpg sigs when importing srpms (ticket #16) (jkeating)
- Enable md5 option in mockbuild (twaugh) (jkeating)

* Tue Jan 24 2012 Jesse Keating <jkeating@redhat.com> - 1.12-1
- Fix mock-config (ticket #13) (jkeating)
- Make md5 a common build argument (jkeating)
- Move arches to be a common build argument (ticket #3) (jkeating)
- Find remote branch to track better (jkeating)

* Fri Jan 13 2012 Jesse Keating <jkeating@redhat.com> - 1.11-1
- Change clog output to be more git-like (sochotnicky)
- Fix mockconfig property (bochecha)
- Use only new-style classes everywhere. (bochecha)
- Testing for access before opening a file is unsafe (bochecha)
- Add a gitbuildhash command (jkeating)
- Always make sure you have a absolute path (aj) (jkeating)
- don't try to import brew, just do koji (jkeating)

* Mon Nov 21 2011 Jesse Keating <jkeating@redhat.com> - 1.10-1
- Use -C for --config shortcut (jkeating)
- Don't leave a directory on failure (#754082) (jkeating)
- Fix chain build (#754189) (jkeating)
- Don't hardcode brew here (jkeating)

* Mon Nov 07 2011 Jesse Keating <jkeating@redhat.com> - 1.9-1
- Don't upload if there is nothing to upload. (jkeating)
- --branch option for import is not supported yet (jkeating)
- Add epilog about mock-config generation (jkeating)
- Don't assume we can create a folder named after the module. (bochecha)
- Fix passing the optional mock root to mockbuild (bochecha)
- Add missing registration for mockbuild target (bochecha)
- Make the clean target work with --path. (bochecha)
- Fix typo in a comment. (bochecha)
- Fix syntax error in main script. (bochecha)
- Fix typo. (bochecha)

* Fri Oct 28 2011 Jesse Keating <jkeating@redhat.com> - 1.8-1
- Get more detailed error output from lookaside (jkeating)
- Move the curl call out to it's own function (jkeating)
- Hide build_common from help/usage (jkeating)
- Fix the help command (jkeating)

* Tue Oct 25 2011 Jesse Keating <jkeating@redhat.com> - 1.7-1
- Support a manually specified mock root (jkeating)
- Add a mock-config subcommand (jkeating)
- Fix a traceback on error. (jkeating)
- Remove debugging code (jkeating)
- More git api updates (jkeating)
- Add topurl as a koji config and property (jkeating)
- Add a mockconfig property (jkeating)
- Turn the latest commit into a property (jkeating)

* Tue Sep 20 2011 Jesse Keating <jkeating@redhat.com> - 1.6-1
- Allow name property to load by itself (jkeating)

* Mon Sep 19 2011 Jesse Keating <jkeating@redhat.com> - 1.5-1
- Fix tag listing (#717528) (jkeating)
- Revamp n-v-r property loading (#721389) (jkeating)
- Don't use os.getlogin (jkeating)
- Code style changes (jkeating)
- Allow fedpkg lint to be configurable and to check spec file. (pingou)
- Handle non-scratch srpm builds better (jkeating)

* Wed Aug 17 2011 Jesse Keating <jkeating@redhat.com> - 1.4-1
- Be more generic when no spec file is found (jkeating)
- Hint about use of git status when dirty (jkeating)
- Don't use print when we can log.info it (jkeating)
- Don't exit from a library (jkeating)
- Do the rpm query in our module path (jkeating)
- Use git's native ability to checkout a branch (jkeating)
- Use keyword arg with clone (jkeating)
- Allow the on-demand generation of an srpm (jkeating)
- Fix up exit codes (jkeating)

* Mon Aug 01 2011 Jesse Keating <jkeating@redhat.com> - 1.3-1
- Fix a debug string (jkeating)
- Set the right property (jkeating)
- Make sure we have a default hashtype (jkeating)
- Use underscore for the dist tag (jkeating)
- Fix the kojiweburl property (jkeating)

* Wed Jul 20 2011 Jesse Keating <jkeating@redhat.com> - 1.2-1
- Fill out the krb_creds function (jkeating)
- Fix the log message (jkeating)
- site_setup is no longer needed (jkeating)
- Remove some rhtisms (jkeating)
- Wire up the patch command in client code (jkeating)
- Add a patch command (jkeating)

* Fri Jun 17 2011 Jesse Keating <jkeating@redhat.com> - 1.1-2
- Use version macro in files

* Fri Jun 17 2011 Jesse Keating <jkeating@redhat.com> - 1.1-1
- New tarball release with correct license files

* Fri Jun 17 2011 Jesse Keating <jkeating@redhat.com> - 1.0-2
- Fix up things found in review

* Tue Jun 14 2011 Jesse Keating <jkeating@redhat.com> - 1.0-1
- Initial package
