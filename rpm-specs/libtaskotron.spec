Name:           libtaskotron
# NOTE: if you update version, *make sure* to also update `libtaskotron/__init__.py`
Version:        0.10.4
Release:        2%{?dist}
Summary:        Taskotron Support Library

License:        GPLv3
URL:            https://pagure.io/taskotron/libtaskotron
Source0:        https://qa.fedoraproject.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
Libtaskotron is a support library for running taskotron tasks.

%package -n python3-libtaskotron
Summary:        libtaskotron python3 libraries

Obsoletes:      python2-libtaskotron <= %{version}-%{release}

Requires:       ansible
Requires:       createrepo_c
Requires:       dnf
Requires:       python3-bodhi-client
Requires:       python3-hawkey
Requires:       python3-jinja2
Requires:       python3-koji
Requires:       python3-munch
Requires:       python3-progressbar
Requires:       python3-pyyaml
Requires:       python3-requests
Requires:       python3-resultsdb_api
Requires:       python3-rpm
Requires:       python3-setuptools
Requires:       python3-xunitparser
# used by 'synchronize' task in ansible
Requires:       rsync

BuildRequires:  python3-bodhi-client
BuildRequires:  python3-devel
BuildRequires:  python3-hawkey
BuildRequires:  python3-koji
BuildRequires:  python3-mock
BuildRequires:  python3-munch
BuildRequires:  python3-progressbar
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pyyaml
BuildRequires:  python3-requests
BuildRequires:  python3-resultsdb_api
BuildRequires:  python3-rpmfluff
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-testcloud
BuildRequires:  python3-xunitparser

%description -n python3-libtaskotron
Libtaskotron libraries built for Python 3.

%pre -n python3-libtaskotron
getent group taskotron >/dev/null || groupadd taskotron


# ****** taskotron-runner ******

%package -n taskotron-runner
Summary:        runtask binary used to execute tasks

Provides: libtaskotron = %{version}-%{release}
Provides: libtaskotron-core = %{version}-%{release}
Provides: libtaskotron-fedora = %{version}-%{release}
Provides: libtaskotron-disposable = %{version}-%{release}
Provides: libtaskotron-config = %{version}-%{release}
Obsoletes: libtaskotron < 0.9.2-1
Obsoletes: libtaskotron-core < 0.9.2-1
Obsoletes: libtaskotron-fedora < 0.9.2-1
Obsoletes: libtaskotron-disposable < 0.9.2-1
Obsoletes: libtaskotron-config < 0.9.2-1

BuildRequires:  ansible
BuildRequires:  grep
# used by 'synchronize' task in ansible
BuildRequires:  rsync
BuildRequires:  sed

Requires:       python3-libtaskotron = %{version}-%{release}
Requires:       python3-testcloud

%description -n taskotron-runner
libtaskotron's runtask binary which is used to execute taskotron tasks.


# *************************************

%prep
%setup -q

%build
# testing needs to occur here instead of %%check section, because we need to
# patch config files after testing is done, but before py[co] files are built
# (so that they match the source files)
%{__python3} setup.py test

# adjust data path in config
sed -i "/_data_dir/s#_data_dir = '../data'#_data_dir = '%{_datarootdir}/libtaskotron'#" libtaskotron/config_defaults.py
grep -Fq  "_data_dir = '%{_datarootdir}/libtaskotron'" libtaskotron/config_defaults.py

# build files
%py3_build

%install
%py3_install

# configuration files
mkdir -p %{buildroot}%{_sysconfdir}/taskotron/
install -m 0644 conf/taskotron.yaml.example %{buildroot}%{_sysconfdir}/taskotron/taskotron.yaml
install -m 0644 conf/namespaces.yaml.example %{buildroot}%{_sysconfdir}/taskotron/namespaces.yaml
install -m 0644 conf/yumrepoinfo.conf.example %{buildroot}%{_sysconfdir}/taskotron/yumrepoinfo.conf

# log dir
install -d %{buildroot}/%{_localstatedir}/log/taskotron

# tmp dir
install -d %{buildroot}/%{_tmppath}/taskotron

# artifacts dir
install -d %{buildroot}/%{_sharedstatedir}/taskotron/artifacts

# cache dir
install -d %{buildroot}/%{_localstatedir}/cache/taskotron

# images dir
install -d %{buildroot}/%{_sharedstatedir}/taskotron/images

# data files
mkdir -p %{buildroot}%{_datarootdir}/libtaskotron
cp -a data/* %{buildroot}%{_datarootdir}/libtaskotron

%files -n taskotron-runner
%{_bindir}/runtask
%doc README.rst
%license LICENSE

%files -n python3-libtaskotron
%{_bindir}/taskotron_result

%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.egg-info

%dir %{_sysconfdir}/taskotron
%config(noreplace) %{_sysconfdir}/taskotron/namespaces.yaml
%config(noreplace) %{_sysconfdir}/taskotron/taskotron.yaml
%config %{_sysconfdir}/taskotron/yumrepoinfo.conf

%{_datarootdir}/libtaskotron
%dir %attr(0775, root, taskotron) %{_sharedstatedir}/taskotron
%dir %attr(2775, root, taskotron) %{_localstatedir}/cache/taskotron
%dir %attr(2775, root, taskotron) %{_localstatedir}/log/taskotron
%dir %attr(2775, root, taskotron) %{_sharedstatedir}/taskotron/artifacts
%dir %attr(2775, root, taskotron) %{_sharedstatedir}/taskotron/images
%dir %attr(2775, root, taskotron) %{_tmppath}/taskotron

%doc README.rst
%license LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.4-2
- Rebuilt for Python 3.9

* Wed Feb 12 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.10.4-1
- yumrepoinfo: F32 is Branched

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.10.3-1
- yumrepoinfo: F31 is stable, F29 is EOL
- Drop Python 2 Support from spec

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-2
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.10.2-1
- yumrepoinfo: Fedora 31 is branched now

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.10.1-1
- yumrepoinfo: Fedora 30 is stable now

* Wed May 22 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.10.0-1
- Reland "update to new bodhi library"
- tests: execute just on Python 3 by default
- ansible: update python requirements to work on F30
- executor: force ansible to use python3
- yumrepoinfo.conf: Fedora 28 is EOL

* Wed Apr 24 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.8-1
- distgit_directive: download from pagure instead of cgit

* Wed Feb 20 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.7-1
- yumrepoinfo: Fedora 30 has been branched
- docs: allow CRASHED outcome

* Fri Feb 15 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.6-1
- Build scripts: Use Fedora 29 chroot
- ansible.cfg: configure ssh connection retry

* Fri Feb 08 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.5-1
- Drop dependency on python3-configparser
- Support both progressbar and progressbar2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-3
- Support python3-progressbar2 (hotfix, rawhide dist-git only)

* Tue Dec 04 2018 Kamil Páral <kparal@redhat.com> - 0.9.4-1
- revert to old bodhi library
- fix group creation during rpm install

* Tue Dec 04 2018 Kamil Páral <kparal@redhat.com> - 0.9.3-2
- add 'pre' section to libraries, the generic one is not executed for them

* Sun Dec 02 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.3-1
- yumrepoinfo.conf: Fedora 27 is EOL
- spec: replace python-fedora with python-bodhi-client
- requirements: unify libtaskotron sections

* Tue Nov 20 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.2-3
- Obsolete python2-libtaskotron in Fedora >= 30
- Require python-bodhi-client instead of python-fedora

* Fri Nov 16 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.2-2
- Drop support for Fedora 27
- Don't build python2-libtaskotron on Fedora >= 30

* Thu Nov 01 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.2-1
- New packaging scheme
- Build the library both for Python 2 and Python 3
- Binaries will use Python 3 by default
- runtask is now in taskotron-runner, which obsoletes libtaskotron-disposable

* Tue Oct 30 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.1-1
- Fedora 29 GA

* Tue Aug 21 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.9.0-1
- Python 3.7 fixes
- Use F28 in example files
- New BR: python2/3-testcloud
- Add Branched F29 to yumrepoinfo
- remove support for executing distgit (vanilla STI) tests
- switch createrepo for createrepo_c
- config: add minion_repos_ignore_errors (bool) option

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.8.0-1
- spec: use python2 macros explicitly, fix python deps
- runner: retry installing required packages
- executor: add friendly error when results.yml is missing
- Enable grabbing secrets from Vault server
- file_utils: fix presence of status code errno for failed http requests
- spec: adjust testcloud requirement
- file_utils: retry 5xx errors when downloading files
- yumrepoinfo: F26 is EOL
- runner: retry network errors when adding minion repos
- doit: update dodo.py to work with Python 3

* Mon May 28 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.7.0-1
- koji_utils: consider debugsource packages as debuginfo
- fix: reintroduce --no-destroy
- executor: fix running as root
- fix: docs variables handling
- Minion env matching extended with taskotron_match_* vars
- Python 3 support for tests
- create file indicating that results were reported

* Thu May 03 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.6.1-1
- yumrepoinfo: retry on socket errors
- yumrepoinfo: mark F28 as stable

* Wed Apr 04 2018 Kamil Páral <kparal@redhat.com> - 0.6.0-1
- distgit_directive: use correct branch name for Rawhide
- allow to specify COPR repos in minion_repos
- spawn new vm for each test*.yml
- save output of 'rpm -qa' to artifacts dir
- yumrepoinfo: Fix F28 updates URL
- distgit_directive: add param ignore_missing
- exit with non-zero code when some playbook crashes
- retry VM spawning when it fails

* Tue Mar 06 2018 Kamil Páral <kparal@redhat.com> - 0.5.1-1
- yumrepoinfo.conf: fix updates repo url for F28+

* Thu Mar 1 2018 Kamil Páral <kparal@redhat.com> - 0.5.0-1
- Support Standard Test Interface (Ansible-based) tasks
  (removes support for previous task format)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.25-4
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Kamil Páral <kparal@redhat.com> - 0.4.25-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3 and
  https://src.fedoraproject.org/rpms/libtaskotron/pull-request/1)

* Thu Nov 23 2017 Kamil Páral <kparal@redhat.com> - 0.4.25-1
- update yumrepoinfo
- update to latest testcloud API
- add `pull_request` item type

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Kamil Páral <kparal@redhat.com> - 0.4.24-1
- do not use --cacheonly for dnf operations

* Wed Jul 12 2017 Kamil Páral <kparal@redhat.com> - 0.4.23-1
- fix python2-koji dep on F27+
- fix broken test suite

* Wed Jul 12 2017 Kamil Páral <kparal@redhat.com> - 0.4.22-1
- mark Fedora 26 as stable in yumrepoinfo
- remove check for installed packages because it was problematic

* Fri Jun 30 2017 Kamil Páral <kparal@redhat.com> - 0.4.21-1
- documentation improvements
- DNF_REPO item type removed
- default task artifact now points to artifacts root dir instead of task log
- fix rpm deps handling via dnf on Fedora 26 (but only support package names
  and filepaths as deps in task formulas)

* Tue Apr 4 2017 Martin Krizek <mkrizek@fedoraproject.org> - 0.4.20-1
- Add module_build item type (D1184)
- taskformula: replace vars in dictionary keys (D1176)
- koji_directive: always create target_dir (D1175)
- koji_directive: don't crash when latest stable build doesn't exist (D1174)
- argparse: change --arch to be a single value instead of a string (D1171)
- yumrepoinfo: specify all primary and alternate arches (D1172)

* Fri Mar 24 2017 Tim Flink <tflink@fedoraproject.org> - 0.4.19-4
- bumping revision to test package-specific testing again

* Fri Mar 17 2017 Tim Flink <tflink@fedoraproject.org> - 0.4.19-3
- bumping revision to test package-specific testing again

* Fri Mar 17 2017 Tim Flink <tflink@fedoraproject.org> - 0.4.19-2
- bumping revision to test package-specific testing

* Fri Mar 17 2017 Tim Flink <tflink@fedoraproject.org> - 0.4.19-1
- updating yumrepoinfo for F26
- improved support for secondary architectures

* Thu Mar 16 2017 Tim Flink <tflink@fedoraproject.org> - 0.4.18-3
- bumping revision to test package-specific testing

* Fri Feb 17 2017 Kamil Páral <kparal@redhat.com> - 0.4.18-4
- require koji >= 1.10.0 because of T910

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 10 2017 Kamil Páral <kparal@redhat.com> - 0.4.18-3
- add python-pytest-cov builddep because the test suite now needs it,
  and python-rpmfluff because we're missing it

* Thu Feb 09 2017 Kamil Páral <kparal@redhat.com> - 0.4.18-2
- require python-resultsdb_api >= 2.0.0

* Wed Jan 11 2017 Martin Krizek <mkrizek@fedoraproject.org> - 0.4.18-1
- distgit directive improvements (D1055, D1069)
- yumrepoinfo.conf updates (D1057, D1074)
- koji_utils: use supported arches when downloading build logs (D1076)

* Thu Nov 3 2016 Tim Flink <tflink@fedoraproject.org> - 0.4.17-1
- add support for resultsdb 2.0 (D1019)
- add armhfp as a primary arch (D1040)

* Wed Aug 17 2016 Martin Krizek <mkrizek@fedoraproject.org> - 0.4.16-1
- symlink testcloud images instead of copying
- copy dir to minion via tarball
- yumrepoinfo.conf: Fedora 25 has been branched

* Thu Jul 28 2016 Martin Krizek <mkrizek@fedoraproject.org> - 0.4.15-1
- Allow resultsdb_directive to read from file
- create_report_directive: allow input from file
- bash to shell directive
- yumrepoinfo.conf: F22 is now EOL
- various fixes and improvements

* Tue Jul 12 2016 Martin Krizek <mkrizek@fedoraproject.org> - 0.4.14-1
- add xunit directive
- docker testing documentation
- taskotron_result tool
- various fixes and improvements

* Fri May 27 2016 Martin Krizek <mkrizek@fedoraproject.org> - 0.4.13-3
- fix download URL for Source0
- fix conf files permissions

* Thu May 26 2016 Martin Krizek <mkrizek@fedoraproject.org> - 0.4.13-2
- remove not needed custom python_sitelib macro

* Thu May 26 2016 Martin Krizek <mkrizek@fedoraproject.org> - 0.4.13-1
- add distgit docs
- fix progressbar
- koji: allow to exclude arches
- remote_exec: update to latest packages even when cache is outdated

* Tue May 10 2016 Martin Krizek <mkrizek@fedoraproject.org> - 0.4.12-2
- remove global write permissions of libtaskotron directories and change group ownership
  to the taskotron group

* Mon May 9 2016 Martin Krizek <mkrizek@fedoraproject.org> - 0.4.12-1
- bash directive
- allow using a dot to access attributes of a variable in formula
- various fixes

* Mon Apr 18 2016 Martin Krizek <mkrizek@fedoraproject.org> - 0.4.11-1
- add result namespace whitelist
- various fixes and small improvements

* Tue Mar 15 2016 Martin Krizek <mkrizek@fedoraproject.org> - 0.4.10-3
- add python-configparser as dep
- install namespaces.yaml

* Mon Mar 14 2016 Martin Krizek <mkrizek@fedoraproject.org> - 0.4.10-2
- add report_templates directory

* Thu Mar 03 2016 Martin Krizek <mkrizek@fedoraproject.org> - 0.4.10-1
- various performance fixes in disposable clients

* Sun Feb 07 2016 Tim Flink <tflink@fedoraproject.org> - 0.4.9-1
- add report directive (D735)
- restructure docs (D734)

* Thu Jan 28 2016 Martin Krizek <mkrizek@redhat.com> - 0.4.8-2
- Add jinja2 as a dep

* Mon Jan 25 2016 Tim Flink <tflink@fedoraproject.org> - 0.4.8-1
- Documentation updates (D726, D725)

* Wed Jan 20 2016 Tim Flink <tflink@fedoraproject.org> - 0.4.7-1
- changed filename structure for disposable images (D696)
- fixed crash when a check does not provide result (D723)
- Lots of documentation fixes and updates

* Wed Dec 9 2015 Martin Krizek <mkrizek@redhat.com> - 0.4.6-1
- urlgrabber replaced with requests (D668)
- Make minion repos configurable (D682)
- Copy all config files on a minion (D662)
- Fix module import error masking missing modules (D659)

* Fri Nov 20 2015 Martin Krizek <mkrizek@redhat.com> - 0.4.5-2
- Require the exact same version of subpackages
- Remove unused deps

* Thu Nov 19 2015 Martin Krizek <mkrizek@redhat.com> - 0.4.5-1
- Do not fail when copying a task from cwd (D656)
- We need -core not -disposable on disposable clients (D652)
- Don't require -disposable in -core (D652)

* Thu Nov 12 2015 Martin Krizek <mkrizek@redhat.com> - 0.4.4-1
- add %%files for libtaskotron meta-package so it's actually built
- make imageurl configurable
- change package install commands to work with new subpackage structure

* Thu Nov 12 2015 Tim Flink <tflink@fedoraproject.org> - 0.4.3-1
- break libtaskotron up into subpackages (D616)

* Tue Nov 3 2015 Martin Krizek <mkrizek@redhat.com> - 0.4.2-1
- setup.py: fix entry point
- check if packages are installed before installing them
- taskotron.yaml.example: fix typo

* Tue Nov 3 2015 Martin Krizek <mkrizek@redhat.com> - 0.4.1-1
- Save tmp files into /tmpdir/$username (D632)
- find latest image using filename convention (D618)
- yumrepoinfo.conf: Fedora 23 has been released (D633)

* Wed Oct 14 2015 Martin Krizek <mkrizek@redhat.com> - 0.4.0-1
- merge disposable branch to add option to execute the task in a throwaway client

* Wed Sep 02 2015 Josef Skladanka <jskaladan@fedoraproject.org> - 0.3.24-1
- remove pytap, bayeux and yamlish dependencies

* Fri Aug 28 2015 Tim Flink <tflink@fedoraproject.org> - 0.3.23-1
- only submit bodhi comments on failure (D542)

* Wed Aug 26 2015 Tim Flink <tflink@fedoraproject.org> - 0.3.22-1
- Re-enabling bodhi comment directive (D527)
- Include artifacts dir at end of run (D533)

* Wed Aug 19 2015 Tim Flink <tflink@fedoraproject.org> - 0.3.21-1
- Fixing bad initialization of bodhi_utils (D514)
- Removing default value of None for fas_password (D511)

* Tue Aug 18 2015 Tim Flink <tflink@fedoraproject.org> - 0.3.20-1
- Fixing tests to not try network connecitons (T574)

* Tue Aug 18 2015 Tim Flink <tflink@fedoraproject.org> - 0.3.19-1
- Fixes to make libtaskotron mostly compatible with bodhi2 (T558)

* Wed Jul 15 2015 Tim Flink <tflink@fedoraproject.org> - 0.3.17-1
- several minor fixes and enhancements, see git log for more information

* Wed Jul 8 2015 Martin Krizek <mkrizek@redhat.com> - 0.3.16-1
- 0.3.16 release. See git log for more information

* Wed May 13 2015 Kamil Paral <kparal@redhat.com> - 0.3.15-2
- synchronize package versions between spec file and requirements.txt (D337)

* Mon Apr 20 2015 Tim Flink <tflink@fedoraproject.org> - 0.3.15-1
- Do not report ABORTED runs to bodhi (T467)

* Mon Apr 20 2015 Tim Flink <tflink@fedoraproject.org> - 0.3.14-1
- Removing logrotate in production (D339)
- Adding status to bodhi operations and removing excess queries (D344)

* Tue Apr 7 2015 Kamil Paral <kparal@redhat.com> - 0.3.13-2
- Require python-setuptools, otherwise runtask fails to execute. See T449.

* Tue Mar 31 2015 Martin Krizek <mkrizek@redhat.com> - 0.3.13-1
- Add support for execdb
- Various fixes

* Wed Feb 25 2015 Martin Krizek <mkrizek@redhat.com> - 0.3.12-1
- Add support for task artifacts

* Thu Feb 12 2015 Tim Flink <tflink@fedoraproject.org> - 0.3.11-1
- Adding 'compose' item type (T381)
- Fix issue with mash when no RPMs downloaded (T351)

* Wed Oct 22 2014 Tim Flink <tflink@fedoraproject.org> - 0.3.10-1
- Fix for i386 unit tests (T361)
- Small documentation fixes

* Fri Oct 17 2014 Martin Krizek <mkrizek@redhat.com> - 0.3.9-1
- Improve logging messages
- Update documentation

* Thu Oct 9 2014 Tim Flink <tflink@fedoraproject.org> - 0.3.8-1
- Adding bodhi query retries for read-only operations (T338)
- several small bugfixes and typo corrections

* Fri Aug 22 2014 Tim Flink <tflink@fedoraproject.org> - 0.3.7-1
- Adding mash as a BR for functional tests
- removing all as an option for runtask

* Fri Aug 22 2014 Martin Krizek <mkrizek@redhat.com> - 0.3.6-1
- Releasing libtaskotron 0.3.6

* Tue Jul 08 2014 Martin Krizek <mkrizek@fedoraproject.org> - 0.3.3-2
- Add /var/log/taskotron directory

* Mon Jun 30 2014 Tim Flink <tflink@fedoraproject.org> - 0.3.3-1
- Changed distibution license to gpl3
- New user-facing docs

* Mon Jun 23 2014 Tim Flink <tflink@fedoraproject.org> - 0.3.2-1
- Gracefully handle missing rpms in build. Fixes T251.

* Mon Jun 23 2014 Tim Flink <tflink@fedoraproject.org> - 0.3.1-1
- Better support for depcheck in koji_utils and mash_directive
- Added ability for check name to be specified in TAP13 output

* Mon Jun 16 2014 Tim Flink <tflink@fedoraproject.org> - 0.3.0-1
- Added sphinx to requirements.txt

* Fri Jun 13 2014 Tim Flink <tflink@fedoraproject.org> - 0.2.1-1
- documentation improvements, added LICENSE file
- better support for depcheck, srpm downloading
- improved logging configuration

* Wed May 28 2014 Tim Flink <tflink@fedoraproject.org> - 0.1.1-1
- adding libtaskotron-config as requires for libtaskotron
- changing variable syntax to $var and ${var}
- add yumrepoinfo directive, other bugfixes

* Fri May 16 2014 Tim Flink <tflink@fedoraproject.org> - 0.1.0-1
- Releasing libtaskotron 0.1

* Fri May 09 2014 Tim Flink <tflink@fedoraproject.org> - 0.0.11-4
- Disabling %%check so that the code can be used while the tests are fixed

* Tue May 06 2014 Kamil Páral <kparal@redhat.com> - 0.0.11-3
- Add a minimum version to python-hawkey. Older versions have a different API.

* Tue Apr 29 2014 Tim Flink <tflink@fedoraproject.org> - 0.0.11-2
- moved config files to libtaskotron-config subpackage

* Tue Apr 29 2014 Tim Flink <tflink@fedoraproject.org> - 0.0.11-1
- changed config files to be noreplace
- updated config file source paths

* Tue Apr 29 2014 Tim Flink <tflink@fedoraproject.org> - 0.0.10-1
- yumrepo fix for upgradepath, output fix for readability

* Fri Apr 25 2014 Tim Flink <tflink@fedoraproject.org> - 0.0.9-1
- koji_utils fix for upgradepath

* Fri Apr 25 2014 Tim Flink <tflink@fedoraproject.org> - 0.0.8-1
- Updating to latest upstream version
- Fixing resultsdb integration, adding some rpm and koji utility methods

* Wed Apr 16 2014 Tim Flink <tflink@fedoraproject.org> - 0.0.7-2
- Fixing some urls and other small packaging changes

* Tue Apr 15 2014 Tim Flink <tflink@fedoraproject.org> - 0.0.7-1
- Updating to latest upstream
- Change to more generic CLI arguments to match reporting and work better with buildbot

* Mon Apr 14 2014 Tim Flink <tflink@fedoraproject.org> - 0.0.6-2
- Initial package for libtaskotron
