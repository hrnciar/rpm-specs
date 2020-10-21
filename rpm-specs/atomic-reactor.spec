%global owner projectatomic
%global project atomic-reactor

%global commit f46b2c4264888d2e4deb1839496c6f67cd775985
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global dock_obsolete_vr 1.3.7-2

Name:           %{project}
Version:        1.6.47
Release:        4%{?dist}

Summary:        Improved builder for Docker images
License:        BSD
URL:            https://github.com/%{owner}/%{project}
Source0:        https://github.com/%{owner}/%{project}/archive/%{commit}/%{project}-%{commit}.tar.gz

# jsonschema version is pinned in requirement.txt to the rhel/centos 7 version
# we want to use the latest from Fedora repos.
Patch0:         atomic-reactor-jsonschema-version.patch

# Fedora uses a local buildroot image
Patch1:		atomic-reactor-local-buildroot.patch

BuildArch:      noarch
Requires:       python3-atomic-reactor = %{version}-%{release}
Requires:       git >= 1.7.10

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?with_check}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-capturelog
BuildRequires:  python3-dockerfile-parse >= 0.0.5
BuildRequires:  python3-docker
BuildRequires:  python3-flexmock >= 0.10.2
BuildRequires:  python3-six
BuildRequires:  python3-osbs-client >= 0.45
BuildRequires:  python3-responses
BuildRequires:  python3-jsonschema
BuildRequires:  python3-PyYAML
BuildRequires:  python3-mock
BuildRequires:  python3-docker-squash >= 1.0.0-0.3
%endif # with_check

Provides:       dock = %{version}-%{release}
Obsoletes:      dock < %{dock_obsolete_vr}

%description
Simple Python tool with command line interface for building Docker
images. It contains a lot of helpful functions which you would
probably implement if you started hooking Docker into your
infrastructure.


%package -n python3-atomic-reactor
Summary:        Python 3 Atomic Reactor library
Requires:       python3-docker
Requires:       python3-requests
Requires:       python3-setuptools
Requires:       python3-dockerfile-parse >= 0.0.5
Requires:       python3-docker-squash >= 1.0.0-0.3
Requires:       python3-jsonschema
Requires:       python3-PyYAML
Provides:       python3-dock = %{version}-%{release}
Obsoletes:      python3-dock < %{dock_obsolete_vr}
%{?python_provide:%python_provide python3-atomic-reactor}

%description -n python3-atomic-reactor
Simple Python 3 library for building Docker images. It contains
a lot of helpful functions which you would probably implement if
you started hooking Docker into your infrastructure.


%package -n python3-atomic-reactor-koji
Summary:        Koji plugin for Atomic Reactor
Requires:       python3-atomic-reactor = %{version}-%{release}
Requires:       koji
Provides:       python3-dock-koji = %{version}-%{release}
Obsoletes:      python3-dock-koji < %{dock_obsolete_vr}
%{?python_provide:%python_provide python3-atomic-reactor-koji}

%description -n python3-atomic-reactor-koji
Koji plugin for Atomic Reactor


%package -n python3-atomic-reactor-metadata
Summary:        Plugin for submitting metadata to OSBS
Requires:       python3-atomic-reactor = %{version}-%{release}
Requires:       osbs
Provides:       python3-dock-metadata = %{version}-%{release}
Obsoletes:      python3-dock-metadata < %{dock_obsolete_vr}
%{?python_provide:%python_provide python3-atomic-reactor-metadata}

%description -n python3-atomic-reactor-metadata
Plugin for submitting metadata to OSBS

%package -n python3-atomic-reactor-rebuilds
Summary:        Plugins for automated rebuilds
Requires:       python3-atomic-reactor = %{version}-%{release}
Requires:       osbs >= 0.15
%{?python_provide:%python_provide python3-atomic-reactor-rebuilds}

%description -n python3-atomic-reactor-rebuilds
Plugins for automated rebuilds


%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%py3_build

%install
%py3_install

# ship reactor in form of tarball so it can be installed within build image
cp -a %{sources} %{buildroot}/%{_datadir}/%{name}/atomic-reactor.tar.gz

mkdir -p %{buildroot}%{_mandir}/man1
cp -a docs/manpage/atomic-reactor.1 %{buildroot}%{_mandir}/man1/


%if 0%{?with_check}
%check
%{__python3} -m pytest -vv tests
%endif # with_check


%files
%doc README.md
%license LICENSE
%{_bindir}/atomic-reactor
%{_mandir}/man1/atomic-reactor.1*


%files -n python3-atomic-reactor
%doc README.md
%doc docs/*.md
%license LICENSE
%dir %{python3_sitelib}/atomic_reactor
%dir %{python3_sitelib}/atomic_reactor/__pycache__
%{python3_sitelib}/atomic_reactor/*.*
%{python3_sitelib}/atomic_reactor/cli
%{python3_sitelib}/atomic_reactor/plugins
%{python3_sitelib}/atomic_reactor/schemas
%{python3_sitelib}/atomic_reactor/__pycache__/*.py*
%exclude %{python3_sitelib}/atomic_reactor/koji_util.py
%exclude %{python3_sitelib}/atomic_reactor/plugins/exit_koji_promote.py
%exclude %{python3_sitelib}/atomic_reactor/plugins/exit_koji_import.py
%exclude %{python3_sitelib}/atomic_reactor/plugins/exit_sendmail.py
%exclude %{python3_sitelib}/atomic_reactor/plugins/exit_store_metadata_in_osv3.py
%exclude %{python3_sitelib}/atomic_reactor/plugins/post_import_image.py
%exclude %{python3_sitelib}/atomic_reactor/plugins/pre_add_filesystem.py
%exclude %{python3_sitelib}/atomic_reactor/plugins/pre_bump_release.py
%exclude %{python3_sitelib}/atomic_reactor/plugins/pre_check_and_set_rebuild.py
%exclude %{python3_sitelib}/atomic_reactor/plugins/pre_koji.py
%exclude %{python3_sitelib}/atomic_reactor/plugins/pre_koji_parent.py
%exclude %{python3_sitelib}/atomic_reactor/plugins/pre_inject_parent_image.py
%exclude %{python3_sitelib}/atomic_reactor/plugins/__pycache__/exit_koji_promote*.py*
%exclude %{python3_sitelib}/atomic_reactor/plugins/__pycache__/exit_koji_import*.py*
%exclude %{python3_sitelib}/atomic_reactor/plugins/__pycache__/exit_sendmail*.py*
%exclude %{python3_sitelib}/atomic_reactor/plugins/__pycache__/exit_store_metadata_in_osv3*.py*
%exclude %{python3_sitelib}/atomic_reactor/plugins/__pycache__/post_import_image*.py*
%exclude %{python3_sitelib}/atomic_reactor/plugins/__pycache__/pre_bump_release*.py*
%exclude %{python3_sitelib}/atomic_reactor/plugins/__pycache__/pre_add_filesystem*.py*
%exclude %{python3_sitelib}/atomic_reactor/plugins/__pycache__/pre_check_and_set_rebuild*.py*
%exclude %{python3_sitelib}/atomic_reactor/plugins/__pycache__/pre_koji*.py*
%exclude %{python3_sitelib}/atomic_reactor/plugins/__pycache__/pre_koji_parent*.py*
%exclude %{python3_sitelib}/atomic_reactor/plugins/__pycache__/pre_inject_parent_image.py*
%exclude %{python3_sitelib}/integration-tests

%{python3_sitelib}/atomic_reactor-%{version}-py3.*.egg-info
%dir %{_datadir}/%{name}
# ship reactor in form of tarball so it can be installed within build image
%{_datadir}/%{name}/atomic-reactor.tar.gz
# dockerfiles for build images
# there is also a script which starts docker in privileged container
# (is not executable, because it's meant to be used within provileged containers, not on a host system)
%{_datadir}/%{name}/images


%files -n python3-atomic-reactor-koji
%{python3_sitelib}/atomic_reactor/koji_util.py
%{python3_sitelib}/atomic_reactor/__pycache__/koji_util*.py*
%{python3_sitelib}/atomic_reactor/plugins/pre_add_filesystem.py
%{python3_sitelib}/atomic_reactor/plugins/pre_bump_release.py
%{python3_sitelib}/atomic_reactor/plugins/pre_koji.py
%{python3_sitelib}/atomic_reactor/plugins/pre_koji_parent.py
%{python3_sitelib}/atomic_reactor/plugins/pre_inject_parent_image.py
%{python3_sitelib}/atomic_reactor/plugins/exit_koji_promote.py
%{python3_sitelib}/atomic_reactor/plugins/exit_koji_import.py
%{python3_sitelib}/atomic_reactor/plugins/__pycache__/pre_add_filesystem*.py*
%{python3_sitelib}/atomic_reactor/plugins/__pycache__/pre_bump_release*.py*
%{python3_sitelib}/atomic_reactor/plugins/__pycache__/pre_koji*.py*
%{python3_sitelib}/atomic_reactor/plugins/__pycache__/pre_koji_parent*.py*
%{python3_sitelib}/atomic_reactor/plugins/__pycache__/pre_inject_parent_image*.py*
%{python3_sitelib}/atomic_reactor/plugins/__pycache__/exit_koji_promote*.py*
%{python3_sitelib}/atomic_reactor/plugins/__pycache__/exit_koji_import*.py*


%files -n python3-atomic-reactor-metadata
%{python3_sitelib}/atomic_reactor/plugins/exit_store_metadata_in_osv3.py
%{python3_sitelib}/atomic_reactor/plugins/__pycache__/exit_store_metadata_in_osv3*.py*

%files -n python3-atomic-reactor-rebuilds
%{python3_sitelib}/atomic_reactor/plugins/exit_sendmail.py
%{python3_sitelib}/atomic_reactor/plugins/post_import_image.py
%{python3_sitelib}/atomic_reactor/plugins/pre_check_and_set_rebuild.py
%{python3_sitelib}/atomic_reactor/plugins/__pycache__/exit_sendmail*.py*
%{python3_sitelib}/atomic_reactor/plugins/__pycache__/post_import_image*.py*
%{python3_sitelib}/atomic_reactor/plugins/__pycache__/pre_check_and_set_rebuild*.py*


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.47-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.47-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Clement Verna <cverna@fedoraproject.org> - 1.6.47-1
- Update to latest upstream

* Tue Dec 10 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.6.44-7
- rebuilt

* Tue Dec 10 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.6.44-6
- rebuilt

* Tue Dec 10 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.6.44-5
- rebuilt

* Wed Nov 13 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.6.44-4
- rebuilt

* Wed Nov 13 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.6.44-3
- rebuilt

* Wed Nov 13 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.6.44-2
- rebuilt

* Wed Oct 16 2019 Clement Verna <cverna@fedoraproject.org> - 1.6.44
- Update to latest Upstream

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.36.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.36.1-5
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.36.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.36.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 04 2018 Clement Verna <cverna@fedoraproject.org> - 1.6.36.1-2
- Add Fedora specific patch

* Mon Dec 03 2018 Clement Verna <cverna@fedoraproject.org> - 1.6.36.1-1
- Update to latest upstream

* Thu Oct 04 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.34-2
- Drop python2 subpackages (#1627391)

* Wed Oct  3 2018 Owen Taylor <otaylor@redhat.com> - 1.6.34-1
- Update to 1.6.34
- Add patches to get module information from Koji rather than the PDC,
  and handle returns from newer versions of ODCS.

* Fri Aug 03 2018 Clement Verna <cverna@fedoraproject.org> - 1.6.33-3
- Modify the requirements.txt patch to use docker instead of docker-py

* Tue Jul 31 2018 Clement Verna <cverna@fedoraproject.org> - 1.6.33-2
- Add patch to manage jsonschema version

* Mon Jul 30 2018 Clement Verna <cverna@fedoraproject.org> - 1.6.33-1
- New upstream release
- Drop patches
- Drop stop_autorebuild_if_disabled plugin

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Clement Verna <cverna@fedoraproject.org> - 1.6.31-3
- Adding patch fo docker-py compatibility

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.31-2
- Rebuilt for Python 3.7

* Tue May 15 2018 Clement Verna <cverna@fedoraproject.org> - 1.6.31-1
- Update to latest upstream

* Mon Feb 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.6.29-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 01 2018 Clement Verna <cverna@fedoraproject.orf> - 1.6.29-2
- Added patch to fix unit test on multi arch
- Build Requires osbs-client version 0.45 for unit test

* Thu Jan 18 2018 Clement Verna <cverna@fedoraproject.org> - 1.6.29-1
- Update to latest upstream

* Wed Nov 8 2017 Vadim Rutkovsky <vrutkovs@fedoraproject.org> - 1.6.28-1
- Update to latest upstream

* Tue Oct 03 2017 Adam Miller <maxamillion@fedoraproject.org> - 1.6.25.1-3
- Patch to fix unicode handling of krb+koji arguments in koji_util

* Tue Oct 03 2017 Adam Miller <maxamillion@fedoraproject.org> - 1.6.25.1-2
- patch requirements to use fedora's docker-py 2.x resource distribution name
- Fix tests on non-x86_64 arches

* Tue Aug 22 2017 Adam Miller <maxamillion@fedoraproject.org> - 1.6.25.1-1
- Update to latest upstream

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.6.23.2-3
- Python 2 binary package renamed to python2-atomic-reactor
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Fri Jun 09 2017 Adam Miller <maxamillion@fedoraproject.org> - 1.6.23.2-1
- Update to latest upstream

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.6.19-5
- Rebuild for Python 3.6

* Tue Dec 06 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.6.19-4
- Remove pycurl patch, it's for osbs-client and added to this package by mistake

* Tue Dec 06 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.6.19-3
- Patch to fix pycurl ssl issue by switching to python-requests (BZ#1401622)

* Tue Dec 06 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.6.19-2
- Patch to fix koji krb5 atomic-reactor plugin auth

* Tue Dec 06 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.6.19-1
- Update to latest upstream release

* Tue Nov 15 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.6.17-3
- Revert patch to not env_replace in add_labels_in_df plugin

* Mon Nov 14 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.6.17-2
- Patch to not env_replace in add_labels_in_df plugin

* Thu Oct 13 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.6.17-1
- Update to latest upstream: 1.6.17

* Tue Sep 20 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.6.16-1
- Update to latest upstream: 1.6.16

* Tue Sep 06 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.6.15-1
- Update to latest upstream: 1.6.15

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.13-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 08 2016 Tim Waugh <twaugh@redhat.com> - 1.6.13-1
- 1.6.13 release

* Mon Jul 4 2016 Vadim Rutkovsky <vrutkovs@redhat.com> - 1.6.12-1
- 1.6.12 release

* Fri Jun 24 2016 Vadim Rutkovsky <vrutkovs@redhat.com> - 1.6.11-1
- 1.6.11 release

* Thu Jun 09 2016 Tim Waugh <twaugh@redhat.com>
- Move the bump_release plugin to the koji subpackage since it uses Koji.

* Wed Jun 08 2016 Martin Milata <mmilata@redhat.com> - 1.6.10-1
- 1.6.10 release

* Thu May 26 2016 Martin Milata <mmilata@redhat.com> - 1.6.9-1
- 1.6.9 release

* Mon May 23 2016 Martin Milata <mmilata@redhat.com> - 1.6.8-1
- New pre_add_filesystem plugin. (Tim Waugh <twaugh@redhat.com>)
- New koji_util module in koji package. (Tim Waugh <twaugh@redhat.com>)
- 1.6.8 release

* Fri Apr 22 2016 Martin Milata <mmilata@redhat.com> - 1.6.7-1
- 1.6.7 release

* Tue Apr 12 2016 Martin Milata <mmilata@redhat.com> - 1.6.6-1
- 1.6.6 release

* Mon Apr 11 2016 Martin Milata <mmilata@redhat.com> - 1.6.5-1
- Move koji_promote plugin to koji package now that it is used in the
  main workflow. (Tim Waugh <twaugh@redhat.com>)
- 1.6.5 release

* Thu Apr 07 2016 Martin Milata <mmilata@redhat.com> - 1.6.4-1
- 1.6.4 release

* Thu Feb 04 2016 Martin Milata <mmilata@redhat.com> - 1.6.3-1
- 1.6.3 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Martin Milata <mmilata@redhat.com> - 1.6.2-1
- 1.6.2 release
- BuildRequires python-flexmock >= 0.10.2 due to
  https://github.com/bkabrda/flexmock/issues/6

* Fri Jan 15 2016 Martin Milata <mmilata@redhat.com> - 1.6.1-1
- 1.6.1 release
- turned off unit tests for now because some of them use network
- use py_build & py_install macros (Jiri Popelka <jpopelka@redhat.com>)
- use python_provide macro (Jiri Popelka <jpopelka@redhat.com>)
- ship executables per packaging guidelines (Jiri Popelka <jpopelka@redhat.com>)
- %%check section (Jiri Popelka <jpopelka@redhat.com>)
- add requirements on python{,3}-docker-scripts (Slavek Kabrda <bkabrda@redhat.com>)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 19 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.6.0-1
- 1.6.0 release

* Tue Sep 08 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.5.1-1
- 1.5.1 release

* Fri Sep 04 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.5.0-1
- 1.5.0 release

* Tue Jul 28 2015 bkabrda <bkabrda@redhat.com> - 1.4.0-2
- fix issues found during Fedora re-review (rhbz#1246702)

* Thu Jul 16 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.4.0-1
- new upstream release 1.4.0

* Tue Jun 30 2015 Jiri Popelka <jpopelka@redhat.com> - 1.3.7-3
- define macros for RHEL-6

* Mon Jun 22 2015 Slavek Kabrda <bkabrda@redhat.com> - 1.3.7-2
- rename to atomic-reactor

* Mon Jun 22 2015 Martin Milata <mmilata@redhat.com> - 1.3.7-1
- new upstream release 1.3.7

* Wed Jun 17 2015 Jiri Popelka <jpopelka@redhat.com> - 1.3.6-2
- update hash

* Wed Jun 17 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.3.6-1
- new upstream release 1.3.6

* Tue Jun 16 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.3.5-1
- new upstream release 1.3.5

* Fri Jun 12 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.3.4-1
- new upstream release 1.3.4

* Wed Jun 10 2015 Jiri Popelka <jpopelka@redhat.com> - 1.3.3-2
- BuildRequires:  python-docker-py

* Wed Jun 10 2015 Jiri Popelka <jpopelka@redhat.com> - 1.3.3-1
- new upstream release 1.3.3

* Mon Jun 01 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.3.2-1
- new upstream release 1.3.2

* Wed May 27 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.3.1-1
- new upstream release 1.3.1

* Mon May 25 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.3.0-1
- new upstream release 1.3.0

* Tue May 19 2015 Jiri Popelka <jpopelka@redhat.com> - 1.2.1-3
- fix el7 build

* Tue May 19 2015 Jiri Popelka <jpopelka@redhat.com> - 1.2.1-2
- rebuilt

* Tue May 19 2015 Martin Milata <mmilata@redhat.com> - 1.2.1-1
- new upstream release 1.2.1

* Thu May 14 2015 Jiri Popelka <jpopelka@redhat.com> - 1.2.0-4
- enable Python 3 build

* Thu May 07 2015 Slavek Kabrda <bkabrda@redhat.com> - 1.2.0-3
- Introduce python-dock subpackage
- Rename dock-{koji,metadata} to python-dock-{koji,metadata}
- move /usr/bin/dock to /usr/bin/dock2, /usr/bin/dock is now a symlink

* Tue May 05 2015 Jiri Popelka <jpopelka@redhat.com> - 1.2.0-2
- require python[3]-setuptools

* Tue Apr 21 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.2.0-1
- new upstream release 1.2.0

* Tue Apr 07 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.1.3-1
- new upstream release 1.1.3

* Thu Apr 02 2015 Martin Milata <mmilata@redhat.com> - 1.1.2-1
- new upstream release 1.1.2

* Thu Mar 19 2015 Jiri Popelka <jpopelka@redhat.com> - 1.1.1-2
- separate executable for python 3

* Tue Mar 17 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.1.1-1
- new upstream release 1.1.1

* Fri Feb 20 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.1.0-1
- new upstream release 1.1.0

* Wed Feb 11 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.0.0-2
- spec: fix python 3 packaging
- fix license in %%files
- comment on weird stuff (dock.tar.gz, docker.sh)

* Thu Feb 05 2015 Tomas Tomecek <ttomecek@redhat.com> - 1.0.0-1
- initial 1.0.0 upstream release

* Wed Feb 04 2015 Tomas Tomecek <ttomecek@redhat.com> 1.0.0.b-1
- new upstream release: beta

* Mon Dec 01 2014 Tomas Tomecek <ttomecek@redhat.com> 1.0.0.a-1
- complete rewrite (ttomecek@redhat.com)
- Use inspect_image() instead of get_image() when checking for existence (#4).
  (twaugh@redhat.com)

* Mon Nov 10 2014 Tomas Tomecek <ttomecek@redhat.com> 0.0.2-1
- more friendly error msg when build img doesnt exist (ttomecek@redhat.com)
- implement postbuild plugin system; do rpm -qa plugin (ttomecek@redhat.com)
- core, logs: wait for container to finish and then gather output
  (ttomecek@redhat.com)
- core, df copying: df was not copied when path wasn't provided
  (ttomecek@redhat.com)
- store dockerfile in results dir (ttomecek@redhat.com)

* Mon Nov 03 2014 Jakub Dorňák <jdornak@redhat.com> 0.0.1-1
- new package built with tito

* Sun Nov  2 2014 Jakub Dorňák <jdornak@redhat.com> - 0.0.1-1
- Initial package
