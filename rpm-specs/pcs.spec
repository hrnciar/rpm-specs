Name: pcs
Version: 0.10.7
Release: 1%{?dist}
# https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses
# GPLv2: pcs
# MIT: ember, handlebars, jquery, jquery-ui
License: GPLv2 and MIT
URL: https://github.com/ClusterLabs/pcs
Summary: Pacemaker Configuration System

%global version_or_commit %{version}
# %%global version_or_commit 67591ed1487cb0aefa181fdfc166c8a66b55d25a
%global pcs_source_name %{name}-%{version_or_commit}

# ui_commit can be determined by hash, tag or branch
%global ui_commit 0.1.3
%global ui_src_name pcs-web-ui-%{ui_commit}

%global pcs_snmp_pkg_name  pcs-snmp

%global pyagentx_version 0.4.pcs.2
%global dacite_version 1.5.1

# bundled libraries for old web-ui
%global ember_version 1.4.0
%global jquery_version 1.9.1
%global jquery_ui_version 1.10.1
%global handlebars_version 1.2.1

# We do not use _libdir macro because upstream is not prepared for it.
# Pcs does not include binaries and thus it should live in /usr/lib. Tornado
# and gems include binaries and thus it should live in /usr/lib64. But the
# path to tornado/gems is hardcoded in pcs sources. Modify hard links in pcs
# sources is not the way since then rpmdiff complains that the same file has
# different content in different architectures.
%global pcs_libdir %{_prefix}/lib
%global bundled_src_dir pcs/bundled
%global pcsd_public_dir pcsd/public

#part after last slash is recognized as filename in look-aside repository
#desired name is achived by trick with hash anchor
Source0: %{url}/archive/%{version_or_commit}/%{pcs_source_name}.tar.gz

Source41: https://github.com/ondrejmular/pyagentx/archive/v%{pyagentx_version}/pyagentx-%{pyagentx_version}.tar.gz
Source44: https://github.com/konradhalas/dacite/archive/v%{dacite_version}/dacite-%{dacite_version}.tar.gz

Source100: https://github.com/idevat/pcs-web-ui/archive/%{ui_commit}/%{ui_src_name}.tar.gz
Source101: https://github.com/idevat/pcs-web-ui/releases/download/%{ui_commit}/pcs-web-ui-node-modules-%{ui_commit}.tar.xz

# Patch0: name.patch

# git for patches
BuildRequires: git
#printf from coreutils is used in makefile
BuildRequires: coreutils
# python for pcs
BuildRequires: python3 >= 3.6
BuildRequires: python3-dateutil >= 2.7.0
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pycurl
BuildRequires: python3-pyparsing
BuildRequires: python3-tornado
# ruby and gems for pcsd
BuildRequires: ruby >= 2.2.0
BuildRequires: ruby-devel
BuildRequires: rubygem-backports
BuildRequires: rubygem-ethon
BuildRequires: rubygem-ffi
BuildRequires: rubygem-io-console
BuildRequires: rubygem-json
BuildRequires: rubygem-open4
BuildRequires: rubygem-rack
BuildRequires: rubygem-rack-protection
BuildRequires: rubygem-rack-test
BuildRequires: rubygem-sinatra
BuildRequires: rubygem-tilt
# ruby libraries for tests
BuildRequires: rubygem-test-unit
# for touching patch files (sanitization function)
BuildRequires: diffstat
# for post, preun and postun macros
BuildRequires: systemd
# for tests
BuildRequires: python3-lxml
BuildRequires: python3-pyOpenSSL
# pcsd fonts and font management tools for creating symlinks to fonts
BuildRequires: fontconfig
BuildRequires: liberation-sans-fonts
BuildRequires: overpass-fonts

# for building web ui
BuildRequires: npm

# python and libraries for pcs, setuptools for pcs entrypoint
Requires: python3 >= 3.6
Requires: python3-dateutil >= 2.7.0
Requires: python3-lxml
Requires: python3-setuptools
Requires: python3-pycurl
Requires: python3-pyparsing
Requires: python3-tornado
# ruby and gems for pcsd
Requires: ruby >= 2.2.0
Requires: rubygem-backports
Requires: rubygem-ethon
Requires: rubygem-ffi
Requires: rubygem-json
Requires: rubygem-open4
Requires: rubygem-rack
Requires: rubygem-rack-protection
Requires: rubygem-rack-test
Requires: rubygem-sinatra
Requires: rubygem-tilt
# ruby and gems for pcsd-ruby
Requires: rubygem-daemons
Requires: rubygem-eventmachine
Requires: rubygem-thin
# for killall
Requires: psmisc
# for working with certificates (validation etc.)
Requires: openssl
Requires: python3-pyOpenSSL
# cluster stack and related packages
Suggests: pacemaker
Requires: (corosync >= 2.99 if pacemaker)
# pcs enables corosync encryption by default so we require libknet1-plugins-all
Requires: (libknet1-plugins-all if corosync)
Requires: pacemaker-cli >= 2.0.0
# for post, preun and postun macros
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# pam is used for authentication inside daemon (python ctypes)
# more details: https://bugzilla.redhat.com/show_bug.cgi?id=1717113
Requires: pam
# pcsd fonts
Requires: liberation-sans-fonts
Requires: overpass-fonts

Provides: bundled(dacite) = %{dacite_version}
Provides: bundled(ember) = %{ember_version}
Provides: bundled(handlebars) = %{handlebars_version}
Provides: bundled(jquery) = %{jquery_version}
Provides: bundled(jquery-ui) = %{jquery_ui_version}

%description
pcs is a corosync and pacemaker configuration tool.  It permits users to
easily view, modify and create pacemaker based clusters.

# pcs-snmp package definition
%package -n %{pcs_snmp_pkg_name}
Summary: Pacemaker cluster SNMP agent
# https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses
# GPLv2: pcs
# BSD-2-Clause: pyagentx
License: GPLv2 and BSD-2-Clause
URL: https://github.com/ClusterLabs/pcs

# tar for unpacking pyagetx source tar ball
BuildRequires: tar

Requires: pcs = %{version}-%{release}
Requires: pacemaker
Requires: net-snmp

Provides: bundled(pyagentx) = %{pyagentx_version}

%description -n %{pcs_snmp_pkg_name}
SNMP agent that provides information about pacemaker cluster to the master agent (snmpd)

%prep
%autosetup -p1 -S git -n %{pcs_source_name}

# -- following is inspired by python-simplejon.el5 --
# Update timestamps on the files touched by a patch, to avoid non-equal
# .pyc/.pyo files across the multilib peers within a build

update_times(){
  # update_times <reference_file> <file_to_touch> ...
  # set the access and modification times of each file_to_touch to the times
  # of reference_file

  # put all args to file_list
  file_list=("$@")
  # first argument is reference_file: so take it and remove from file_list
  reference_file=${file_list[0]}
  unset file_list[0]

  for fname in ${file_list[@]}; do
    touch -r $reference_file $fname
  done
}

update_times_patch(){
  # update_times_patch <patch_file_name>
  # set the access and modification times of each file in patch to the times
  # of patch_file_name

  patch_file_name=$1

  # diffstat
  # -l lists only the filenames. No histogram is generated.
  # -p override the logic that strips common pathnames,
  #    simulating the patch "-p" option. (Strip the smallest prefix containing
  #    num leading slashes from each file name found in the patch file)
  update_times ${patch_file_name} `diffstat -p1 -l ${patch_file_name}`
}

# update_times_patch %%{PATCH0}

# prepare dirs/files necessary for building web ui
# inside SOURCE100 is only directory %%{ui_src_name}
tar -xzf %SOURCE100 -C %{pcsd_public_dir}
tar -xf %SOURCE101 -C %{pcsd_public_dir}/%{ui_src_name}

# 3) dir for python bundles
mkdir -p %{bundled_src_dir}

# 4) sources for pyagentx
tar -xzf %SOURCE41 -C %{bundled_src_dir}
mv %{bundled_src_dir}/pyagentx-%{pyagentx_version} %{bundled_src_dir}/pyagentx
update_times %SOURCE41 `find %{bundled_src_dir}/pyagentx -follow`
cp %{bundled_src_dir}/pyagentx/LICENSE.txt pyagentx_LICENSE.txt
cp %{bundled_src_dir}/pyagentx/CONTRIBUTORS.txt pyagentx_CONTRIBUTORS.txt
cp %{bundled_src_dir}/pyagentx/README.md pyagentx_README.md

# 7) sources for python dacite
tar -xzf %SOURCE44 -C %{bundled_src_dir}
mv %{bundled_src_dir}/dacite-%{dacite_version} %{bundled_src_dir}/dacite
cp %{bundled_src_dir}/dacite/LICENSE dacite_LICENSE
cp %{bundled_src_dir}/dacite/README.md dacite_README.md

%build
%define debug_package %{nil}

%install
rm -rf $RPM_BUILD_ROOT
pwd

# build web ui and put it to pcsd
make -C %{pcsd_public_dir}/%{ui_src_name} build
mv %{pcsd_public_dir}/%{ui_src_name}/build  pcsd/public/ui
rm -r %{pcsd_public_dir}/%{ui_src_name}

# main pcs install
%make_install \
  PREFIX=%{_prefix} \
  SYSTEMD_UNIT_DIR=%{_unitdir} \
  LIB_DIR=%{pcs_libdir} \
  PYTHON=%{__python3} \
  PYTHON_SITELIB=%{python3_sitelib} \
  BASH_COMPLETION_DIR=%{_datadir}/bash-completion/completions \
  BUNDLE_PYAGENTX_SRC_DIR=`readlink -f %{bundled_src_dir}/pyagentx` \
  BUNDLE_DACITE_SRC_DIR=`readlink -f %{bundled_src_dir}/dacite` \
  BUILD_GEMS=false \
  SYSTEMCTL_OVERRIDE=true \
  hdrdir="%{_includedir}" \
  rubyhdrdir="%{_includedir}" \
  includedir="%{_includedir}"

%check
# In the building environment LC_CTYPE is set to C which causes tests to fail
# due to python prints a warning about it to stderr. The following environment
# variable disables the warning.
# On the live system either UTF8 locale is set or the warning is emmited
# which breaks pcs. That is the correct behavior since with wrong locales it
# would be probably broken anyway.
# The main concern here is to make the tests pass.
# See https://fedoraproject.org/wiki/Changes/python3_c.utf-8_locale for details.
export PYTHONCOERCECLOCALE=0

run_all_tests(){
  #run pcs tests

  # disabled tests:
  #
  BUNDLED_LIB_LOCATION=$RPM_BUILD_ROOT%{pcs_libdir}/pcs/bundled/packages \
    %{__python3} pcs_test/suite.py --tier0 -v --vanilla --all-but \
    pcs_test.tier0.daemon.app.test_app_remote.SyncConfigMutualExclusive.test_get_not_locked \
    pcs_test.tier0.daemon.app.test_app_remote.SyncConfigMutualExclusive.test_post_not_locked \

  test_result_python=$?

  #run pcsd tests and remove them
  pcsd_dir=$RPM_BUILD_ROOT%{pcs_libdir}/pcsd
  # GEM_HOME is not needed anymore since all required gems are in fedora
  ruby \
    -I${pcsd_dir} \
    -I${pcsd_dir}/test \
    ${pcsd_dir}/test/test_all_suite.rb
  test_result_ruby=$?

  if [ $test_result_python -ne 0 ]; then
    return $test_result_python
  fi
  return $test_result_ruby
}

remove_all_tests() {
  pcsd_dir=$RPM_BUILD_ROOT%{pcs_libdir}/pcsd
  #remove pcsd tests, we do not distribute them in the rpm
  rm -r -v ${pcsd_dir}/test

  # remove javascript testing files
  rm -r -v ${pcsd_dir}/public/js/dev
}

run_all_tests
remove_all_tests

%posttrans
# Make sure the new version of the daemon is runnning.
# Also, make sure to start pcsd-ruby if it hasn't been started or even
# installed before. This is done by restarting pcsd.service.
%{_bindir}/systemctl daemon-reload
%{_bindir}/systemctl try-restart pcsd.service

%post
%systemd_post pcsd.service
%systemd_post pcsd-ruby.service

%post -n %{pcs_snmp_pkg_name}
%systemd_post pcs_snmp_agent.service

%preun
%systemd_preun pcsd.service
%systemd_preun pcsd-ruby.service

%preun -n %{pcs_snmp_pkg_name}
%systemd_preun pcs_snmp_agent.service

%postun
%systemd_postun_with_restart pcsd.service
%systemd_postun_with_restart pcsd-ruby.service

%postun -n %{pcs_snmp_pkg_name}
%systemd_postun_with_restart pcs_snmp_agent.service

%files
%doc CHANGELOG.md
%doc README.md
%doc dacite_README.md
%license dacite_LICENSE
%license COPYING
%{python3_sitelib}/pcs
%{python3_sitelib}/pcs-%{version}-py3.*.egg-info
%{_sbindir}/pcs
%{_sbindir}/pcsd
%{pcs_libdir}/pcs/pcs_internal
%{pcs_libdir}/pcsd/*
%{pcs_libdir}/pcs/bundled/packages/dacite*
%{_unitdir}/pcsd.service
%{_unitdir}/pcsd-ruby.service
%{_datadir}/bash-completion/completions/pcs
%{_sharedstatedir}/pcsd
%{_sysconfdir}/pam.d/pcsd
%dir %{_var}/log/pcsd
%config(noreplace) %{_sysconfdir}/logrotate.d/pcsd
%config(noreplace) %{_sysconfdir}/sysconfig/pcsd
%ghost %config(noreplace) %attr(0600,root,root) %{_sharedstatedir}/pcsd/cfgsync_ctl
%ghost %config(noreplace) %attr(0600,root,root) %{_sharedstatedir}/pcsd/known-hosts
%ghost %config(noreplace) %attr(0600,root,root) %{_sharedstatedir}/pcsd/pcsd.cookiesecret
%ghost %config(noreplace) %attr(0600,root,root) %{_sharedstatedir}/pcsd/pcsd.crt
%ghost %config(noreplace) %attr(0600,root,root) %{_sharedstatedir}/pcsd/pcsd.key
%ghost %config(noreplace) %attr(0644,root,root) %{_sharedstatedir}/pcsd/pcs_settings.conf
%ghost %config(noreplace) %attr(0644,root,root) %{_sharedstatedir}/pcsd/pcs_users.conf
%{_mandir}/man8/pcs.*
%{_mandir}/man8/pcsd.*
%exclude %{pcs_libdir}/pcsd/*.debian
%exclude %{pcs_libdir}/pcsd/Gemfile
%exclude %{pcs_libdir}/pcsd/Gemfile.lock
%exclude %{pcs_libdir}/pcsd/Makefile
%exclude %{pcs_libdir}/pcsd/pcsd.conf
%exclude %{pcs_libdir}/pcsd/pcsd.service
%exclude %{pcs_libdir}/pcsd/pcsd-ruby.service
%exclude %{pcs_libdir}/pcsd/pcsd.8
%exclude %{pcs_libdir}/pcsd/public/js/dev/*
%exclude %{python3_sitelib}/pcs/bash_completion
%exclude %{python3_sitelib}/pcs/pcs.8
%exclude %{python3_sitelib}/pcs/pcs

%files -n %{pcs_snmp_pkg_name}
%{pcs_libdir}/pcs/pcs_snmp_agent
%{pcs_libdir}/pcs/bundled/packages/pyagentx*
%{_unitdir}/pcs_snmp_agent.service
%{_datadir}/snmp/mibs/PCMK-PCS*-MIB.txt
%{_mandir}/man8/pcs_snmp_agent.*
%config(noreplace) %{_sysconfdir}/sysconfig/pcs_snmp_agent
%doc CHANGELOG.md
%doc pyagentx_CONTRIBUTORS.txt
%doc pyagentx_README.md
%license COPYING
%license pyagentx_LICENSE.txt

%changelog
* Wed Sep 30 2020 Miroslav Lisik <mlisik@redhat.com> - 0.10.7-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- Added dependency on python packages pyparsing and dateutil
- Fixed virtual bundle provides for ember, handelbars, jquery and jquery-ui
- Removed dependency on python3-clufter

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Miroslav Lisik <mlisik@redhat.com> - 0.10.6-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- Updated pcs-web-ui
- Stopped bundling tornado (use distribution package instead)
- Stopped bundling rubygem-tilt (use distribution package instead)
- Removed rubygem bundling
- Removed unneeded BuildRequires: execstack, gcc, gcc-c++
- Excluded some tests for tornado daemon

* Tue Jul 21 2020 Tom Stellard <tstellar@redhat.com> - 0.10.5-8
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Wed Jul 15 2020 Ondrej Mular <omular@redhat.com> - 0.10.5-7
- Use fixed upstream version of dacite with Python 3.9 support
- Split upstream tests in gating into tiers

* Fri Jul 03 2020 Ondrej Mular <omular@redhat.com> - 0.10.5-6
- Use patched version of dacite compatible with Python 3.9
- Resolves: rhbz#1838327

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.5-5
- Rebuilt for Python 3.9

* Thu May 07 2020 Ondrej Mular <omular@redhat.com> - 0.10.5-4
- Rebased to latest upstream sources (see CHANGELOG.md)
- Run only tier0 tests in check section

* Fri Apr 03 2020 Ondrej Mular <omular@redhat.com> - 0.10.5-3
- Enable gating

* Fri Mar 27 2020 Ondrej Mular <omular@redhat.com> - 0.10.5-2
- Remove usage of deprecated module xml.etree.cElementTree
- Resolves: rhbz#1817695

* Wed Mar 18 2020 Miroslav Lisik <mlisik@redhat.com> - 0.10.5-1
- Rebased to latest upstream sources (see CHANGELOG.md)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Miroslav Lisik <mlisik@redhat.com> - 0.10.4-1
- Rebased to latest upstream sources (see CHANGELOG.md)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.3-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 23 2019 Ondrej Mular <omular@redhat.com> - 0.10.3-1
- Rebased to latest upstream sources (see CHANGELOG.md)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Ondrej Mular <omular@redhat.com> - 0.10.2-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- Added pam as required package
- An alternative webUI rebased to latest upstream sources
- Improved configuration files permissions in rpm

* Tue Mar 19 2019 Tomas Jelinek <tojeline@redhat.com> - 0.10.1-4
- Removed unused dependency rubygem-multi_json
- Removed files needed only for building rubygems from the package

* Mon Feb 04 2019 Ivan Devát <idevat@redhat.com> - 0.10.1-3
- Corrected gem install flags

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Ivan Devát <idevat@redhat.com> - 0.10.1-1
- Rebased to latest upstream sources (see CHANGELOG.md)

* Tue Oct 09 2018 Ondrej Mular <omular@redhat.com> - 0.10.0.alpha.6-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- Resolves: rhbz#1618911

* Fri Aug 31 2018 Ivan Devát <idevat@redhat.com> - 0.10.0.alpha.2-3
- Started bundling rubygem-tilt (rubygem-tilt is orphaned in fedora due to rubygem-prawn dependency)
- Enabled passing tests

* Sat Aug 25 2018 Ivan Devát <idevat@redhat.com> - 0.10.0.alpha.2-2
- Fixed error with missing rubygem location during pcsd start
- Resolves: rhbz#1618911

* Thu Aug 02 2018 Ivan Devát <idevat@redhat.com> - 0.10.0.alpha.2-1
- Rebased to latest upstream sources (see CHANGELOG.md)

* Wed Jul 25 2018 Ivan Devát <idevat@redhat.com> - 0.9.164-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.164-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.164-2
- Rebuilt for Python 3.7

* Mon Apr 09 2018 Ondrej Mular <omular@redhat.com> - 0.9.164-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- Fixed: CVE-2018-1086, CVE-2018-1079

* Mon Feb 26 2018 Ivan Devát <idevat@redhat.com> - 0.9.163-2
- Fixed crash when adding a node to a cluster

* Tue Feb 20 2018 Ivan Devát <idevat@redhat.com> - 0.9.163-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- Adapted for Rack 2 and Sinatra 2

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.160-5
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.160-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.9.160-3
- Rebuilt for switch to libxcrypt

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.160-2
- F-28: rebuild for ruby25
- Workaround for gem install option

* Wed Oct 18 2017 Ondrej Mular <omular@redhat.com> - 0.9.160-1
- Rebased to latest upstream sources (see CHANGELOG.md)
- All pcs tests are temporarily disabled because of issues in pacemaker.

* Thu Sep 14 2017 Ondrej Mular <omular@redhat.com> - 0.9.159-4
- Bundle rubygem-rack-protection which is being updated to 2.0.0 in Fedora.
- Removed setuptools patch.
- Disabled debuginfo subpackage.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.159-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.159-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Ondrej Mular <omular@redhat.com> - 0.9.159-1
- Rebased to latest upstream sources (see CHANGELOG.md)

* Tue May 23 2017 Tomas Jelinek <tojeline@redhat.com> - 0.9.156-3
- Fixed python locales issue preventing build-time tests to pass
- Bundle rubygem-tilt which is being retired from Fedora

* Thu Mar 23 2017 Tomas Jelinek <tojeline@redhat.com> - 0.9.156-2
- Fixed Cross-site scripting (XSS) vulnerability in web UI CVE-2017-2661
- Re-added support for clufter as it is now available for Python 3

* Wed Feb 22 2017 Tomas Jelinek <tojeline@redhat.com> - 0.9.156-1
- Rebased to latest upstream sources (see CHANGELOG.md)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.155-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Vít Ondruch <vondruch@redhat.com> - 0.9.155-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Wed Jan 04 2017 Adam Williamson <awilliam@redhat.com> - 0.9.155-1
- Latest release 0.9.155
- Fix tests with Python 3.6 and lxml 3.7
- Package the license as license, not doc
- Use -f param for rm when wiping test directories as they are nested now

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com>
- Rebuild for Python 3.6

* Tue Oct 18 2016 Tomas Jelinek <tojeline@redhat.com> - 0.9.154-2
- Fixed upgrading from pcs-0.9.150

* Thu Sep 22 2016 Tomas Jelinek <tojeline@redhat.com> - 0.9.154-1
- Re-synced to upstream sources
- Spec file cleanup and fixes

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.150-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 11 2016 Tomas Jelinek <tojeline@redhat.com> - 0.9.150-1
- Re-synced to upstream sources
- Make pcs depend on python3
- Spec file cleanup

* Tue Feb 23 2016 Tomas Jelinek <tojeline@redhat.com> - 0.9.149-2
- Fixed rubygems issues which prevented pcsd from starting
- Added missing python-lxml dependency

* Thu Feb 18 2016 Tomas Jelinek <tojeline@redhat.com> - 0.9.149-1
- Re-synced to upstream sources
- Security fix for CVE-2016-0720, CVE-2016-0721
- Fixed rubygems issues which prevented pcsd from starting
- Rubygems built with RELRO
- Spec file cleanup
- Fixed multilib .pyc/.pyo issue

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.144-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Vít Ondruch <vondruch@redhat.com> - 0.9.144-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Fri Sep 18 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.144-1
- Re-synced to upstream sources

* Tue Jun 23 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.141-2
- Added requirement for psmisc for killall

* Tue Jun 23 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.141-1
- Re-synced to upstream sources

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.140-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.140-1
- Re-synced to upstream sources

* Fri May 22 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.139-4
- Fix for CVE-2015-1848, CVE-2015-3983 (sessions not signed)

* Thu Mar 26 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.139-3
- Add BuildRequires: systemd (rhbz#1206253)

* Fri Feb 27 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.139-2
- Reflect clufter inclusion (rhbz#1180723)

* Thu Feb 19 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.139-1
- Re-synced to upstream sources

* Sat Jan 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.115-5
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.115-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.115-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 Tomas Jelinek <tojeline@redhat.com> - 0.9.115-2
- Rebuild to fix ruby dependencies

* Mon Apr 21 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-1
- Re-synced to upstream sources

* Fri Dec 13 2013 Chris Feist <cfeist@redhat.com> - 0.9.102-1
- Re-synced to upstream sources

* Wed Jun 19 2013 Chris Feist <cfeist@redhat.com> - 0.9.48-1
- Rebuild with upstream sources

* Thu Jun 13 2013 Chris Feist <cfeist@redhat.com> - 0.9.44-5
- Added fixes for building rpam with ruby-2.0.0

* Mon Jun 03 2013 Chris Feist <cfeist@redhat.com> - 0.9.44-4
- Rebuild with upstream sources

* Tue May 07 2013 Chris Feist <cfeist@redhat.com> - 0.9.41-2
- Resynced to upstream sources

* Fri Apr 19 2013 Chris Feist <cfeist@redhat.com> - 0.9.39-1
- Fixed gem building
- Re-synced to upstream sources

* Mon Mar 25 2013 Chris Feist <cfeist@rehdat.com> - 0.9.36-4
- Don't try to build gems at all

* Mon Mar 25 2013 Chris Feist <cfeist@rehdat.com> - 0.9.36-3
- Removed all gems from build, will need to find pam package in the future

* Mon Mar 25 2013 Chris Feist <cfeist@redhat.com> - 0.9.36-2
- Removed duplicate libraries already present in fedora

* Mon Mar 18 2013 Chris Feist <cfeist@redhat.com> - 0.9.36-1
- Resynced to latest upstream

* Mon Mar 11 2013 Chris Feist <cfeist@redhat.com> - 0.9.33-1
- Resynched to latest upstream
- pcsd has been moved to /usr/lib to fix /usr/local packaging issues

* Thu Feb 21 2013 Chris Feist <cfeist@redhat.com> - 0.9.32-1
- Resynced to latest version of pcs/pcsd

* Mon Nov 05 2012 Chris Feist <cfeist@redhat.com> - 0.9.27-3
- Build on all archs

* Thu Oct 25 2012 Chris Feist <cfeist@redhat.com> - 0.9.27-2
- Resync to latest version of pcs
- Added pcsd daemon

* Mon Oct 08 2012 Chris Feist <cfeist@redhat.cmo> - 0.9.26-1
- Resync to latest version of pcs

* Thu Sep 20 2012 Chris Feist <cfeist@redhat.cmo> - 0.9.24-1
- Resync to latest version of pcs

* Thu Sep 20 2012 Chris Feist <cfeist@redhat.cmo> - 0.9.23-1
- Resync to latest version of pcs

* Wed Sep 12 2012 Chris Feist <cfeist@redhat.cmo> - 0.9.22-1
- Resync to latest version of pcs

* Thu Sep 06 2012 Chris Feist <cfeist@redhat.cmo> - 0.9.19-1
- Resync to latest version of pcs

* Tue Aug 07 2012 Chris Feist <cfeist@redhat.com> - 0.9.12-1
- Resync to latest version of pcs

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 24 2012 Chris Feist <cfeist@redhat.com> - 0.9.4-1
- Resync to latest version of pcs
- Move cluster creation options to cluster sub command.

* Mon May 07 2012 Chris Feist <cfeist@redhat.com> - 0.9.3.1-1
- Resync to latest version of pcs which includes fixes to work with F17.

* Mon Mar 19 2012 Chris Feist <cfeist@redhat.com> - 0.9.2.4-1
- Resynced to latest version of pcs

* Mon Jan 23 2012 Chris Feist <cfeist@redhat.com> - 0.9.1-1
- Updated BuildRequires and %%doc section for fedora

* Fri Jan 20 2012 Chris Feist <cfeist@redhat.com> - 0.9.0-2
- Updated spec file for fedora specific changes

* Mon Jan 16 2012 Chris Feist <cfeist@redhat.com> - 0.9.0-1
- Initial Build
