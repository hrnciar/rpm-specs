# Enable Python dependency generation
%{?python_enable_dependency_generator}

# Missing dependencies for tests
%bcond_with check

# Missing dependencies for documentation
%bcond_with docs

Name:           buildbot
Version:        2.5.1
Release:        3%{?dist}

Summary:        Build/test automation system
License:        GPLv2
URL:            https://buildbot.net
Source0:        %{pypi_source buildbot}
Source1:        %{pypi_source buildbot-worker}
Source2:        %{pypi_source buildbot-www}
Source3:        %{pypi_source buildbot-waterfall-view}
Source4:        %{pypi_source buildbot-grid-view}
Source5:        %{pypi_source buildbot-console-view}
# Build-time only component for buildbot
Source6:        %{pypi_source buildbot-pkg}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# For making the build work from source
BuildRequires:  python3dist(setuptools) >= 21.2.1
BuildRequires:  python3dist(twisted) >= 17.9
BuildRequires:  python3dist(jinja2) >= 2.1
BuildRequires:  python3dist(zope.interface) >= 4.1.1
BuildRequires:  python3dist(future)
BuildRequires:  python3dist(sqlalchemy) >= 0.8
BuildRequires:  python3dist(sqlalchemy-migrate) >= 0.9
BuildRequires:  python3dist(python-dateutil) >= 1.5
BuildRequires:  python3dist(txaio) >= 2.2.2
BuildRequires:  python3dist(autobahn) >= 0.16
BuildRequires:  python3dist(pyjwt)
BuildRequires:  python3dist(pyyaml)

BuildRequires:  python3dist(treq)
BuildRequires:  python3dist(boto3)
BuildRequires:  python3dist(mock) >= 2
BuildRequires:  python3dist(lz4)

%if %{with check}
BuildRequires:  bzr
BuildRequires:  cvs
BuildRequires:  git
BuildRequires:  mercurial
BuildRequires:  subversion
BuildRequires:  darcs
%endif

%if %{with docs}
BuildRequires:  python3dist(sphinx) >= 1.4
BuildRequires:  python3dist(sphinxcontrib-blockdiag)
BuildRequires:  python3dist(sphinxcontrib-spelling)
BuildRequires:  python3dist(pyenchant)
BuildRequires:  (python3dist(docutils) >= 0.8 with python3dist(docutils) < 0.13)
BuildRequires:  python3dist(sphinx-jinja)
BuildRequires:  python3dist(towncrier)
%endif

# Turns former package into a metapackage for installing everything
Requires:       %{name}-master = %{version}
Requires:       %{name}-worker = %{version}
Requires:       %{name}-www = %{version}
%if %{with docs}
Requires:       %{name}-doc = %{version}
%else
Obsoletes:      %{name}-doc < %{version}-%{release}
%endif

%description
The BuildBot is a system to automate the compile/test cycle required by
most software projects to validate code changes. By automatically
rebuilding and testing the tree each time something has changed, build
problems are pinpointed quickly, before other developers are
inconvenienced by the failure.

%package master
Summary:        Build/test automation system
Recommends:     %{name}-www = %{version}-%{release}
%if ! %{with docs}
Obsoletes:      %{name}-doc < %{version}-%{release}
%endif

%description master
The BuildBot is a system to automate the compile/test cycle required by
most software projects to validate code changes. By automatically
rebuilding and testing the tree each time something has changed, build
problems are pinpointed quickly, before other developers are
inconvenienced by the failure.

This package contains only the buildmaster implementation.
The buildbot-worker package contains the buildworker.

%package worker
Summary:        Build/test automation system
Obsoletes:      %{name}-slave < 0.9.0
Provides:       %{name}-slave = %{version}-%{release}

%if ! %{with docs}
Obsoletes:      %{name}-doc < %{version}-%{release}
%endif

%description worker
This package contains only the buildworker implementation.
The buildbot-master package contains the buildmaster.

%package www
Summary:        Build/test automation system

# Script to get bundled js
# cat \
# ./www/codeparameter/package.json \
# ./www/console_view/package.json	\
# ./www/base/package.json	\
# ./www/waterfall_view/package.json \
# ./www/data_module/package.json \
# ./www/grid_view/package.json \
# | jq '.dependencies' | sed 's/[{}, ]//g' | sort -u

Provides:        bundled(guanlecoja) = 0.8.0
Provides:        bundled(guanlecoja) = 0.8.3
Provides:        bundled(gulp) = 3.9.0
Provides:        bundled(gulp) = 3.9.1
Provides:        bundled(gulp-shell) = 0.4.1
Provides:        bundled(http-proxy) = 1.11.1
Provides:        bundled(minimist) = 1.1.1
Provides:        bundled(shelljs) = 0.5.3

%description www
Provides web frontend for buildbot.

%if %{with docs}
%package doc
Summary:        Buildbot documentation

%description doc
%{summary}.
%endif

%prep
%setup -q -b0 -b1 -b2 -b3 -b4 -b5 -b6


%build
%py3_build

%if %{with docs}
#TODO create API documentation
pushd docs
make docs.tgz VERSION="%{version}" SPHINXBUILD=sphinx-build-3
popd
%endif

pushd ../%{name}-worker-%{version}
%py3_build
popd

# For buildbot_pkg build-time module to set version correctly
export BUILDBOT_VERSION=%{version}

# So that other modules can use buildbot-pkg import
export PYTHONPATH=%{_builddir}/%{name}-%{version}/build/lib:%{_builddir}/%{name}-pkg-%{version}/build/lib

bbweb_components=(pkg www waterfall-view grid-view console-view)

for bbweb_component in ${bbweb_components[@]}; do
	pushd ../%{name}-${bbweb_component}-%{version}
	sed -e "s/^    setup_requires=.*$//" -i setup.py
	%py3_build
	popd
done

%install
%py3_install

# For buildbot_pkg build-time module to set version correctly
export BUILDBOT_VERSION=%{version}

# So that other modules can use buildbot-pkg import
export PYTHONPATH=%{_builddir}/%{name}-%{version}/build/lib:%{_builddir}/%{name}-pkg-%{version}/build/lib

bbweb_components=(www waterfall-view grid-view console-view)

for bbweb_component in ${bbweb_components[@]}; do
	pushd ../%{name}-${bbweb_component}-%{version}
	%py3_install
	popd
done

install -Dpm0644 -t %{buildroot}%{_mandir}/man1 docs/buildbot.1

%if %{with docs}
mkdir -p %{buildroot}%{_pkgdocdir}
tar xf docs/docs.tgz --strip-components=1 -C %{buildroot}%{_pkgdocdir}
%endif

# install worker files
pushd ../%{name}-worker-%{version}
%py3_install
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 docs/buildbot-worker.1
popd

# Purge windows-only files
rm -vf %{buildroot}%{_bindir}/*windows*

%if %{with check}
%check
trial buildbot.test
%endif

%files
# Empty because metapackage

%files master
%doc CREDITS NEWS UPGRADING
%license COPYING
%{_bindir}/buildbot
%{_mandir}/man1/buildbot.1*
%{python3_sitelib}/buildbot/
%{python3_sitelib}/buildbot-*egg-info/

%files worker
%doc NEWS UPGRADING
%license COPYING
%{_bindir}/buildbot-worker
%{_mandir}/man1/buildbot-worker.1*
%{python3_sitelib}/buildbot_worker/
%{python3_sitelib}/buildbot_worker-*egg-info/

%files www
%license COPYING
%{python3_sitelib}/buildbot_www/
%{python3_sitelib}/buildbot_www-*.egg-info/
%{python3_sitelib}/buildbot_waterfall_view/
%{python3_sitelib}/buildbot_waterfall_view-*egg-info/
%{python3_sitelib}/buildbot_grid_view/
%{python3_sitelib}/buildbot_grid_view-*egg-info/
%{python3_sitelib}/buildbot_console_view/
%{python3_sitelib}/buildbot_console_view-*egg-info/

%if %{with docs}
%files doc
%{_pkgdocdir}/
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.1-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Orion Poplawski <orion@nwra.com> - 2.5.1-1
- Update to 2.5.1 (bz#1776032)

* Tue Oct 22 2019 Neal Gompa <ngompa13@gmail.com> - 2.5.0-1
- Update to 2.5.0 (#1751387)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 25 2019 Neal Gompa <ngompa13@gmail.com> - 2.4.0-1
- Update to 2.4.0 (#1743002)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 14:27:44 CEST 2019 Neal Gompa <ngompa13@gmail.com> - 2.3.1-2
- Add missing changelog entry

* Tue May 28 13:09:59 CEST 2019 František Zatloukal <fzatlouk@redhat.com> - 2.3.1-1
- Update to 2.3.1

* Sat Feb 09 2019 Neal Gompa <ngompa13@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Sat Feb 09 2019 Neal Gompa <ngompa13@gmail.com> - 1.8.1-1
- Update to 1.8.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 22 2018 Neal Gompa <ngompa13@gmail.com> - 1.7.0-1
- Update to 1.7.0

* Tue Dec 11 2018 Neal Gompa <ngompa13@gmail.com> - 1.6.0-2
- Add www subpackage with frontend components

* Wed Dec 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Fri Jul 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 11 2018 Neal Gompa <ngompa13@gmail.com> - 1.1.0-1
- Upgrade to 1.1.0 (#1554094)

* Tue Feb 20 2018 Neal Gompa <ngompa13@gmail.com> - 1.0.0-1
- Rebase to 1.0.0 (#1236345)
- Rename slave subpackage to worker subpackage per upstream rename
- Drop tests and docs as they require several unpackaged dependencies

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.12-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 Gianluca Sforna <giallu@gmail.com> 0.8.12-1
- new upstream release
- drop upstreamed patch

* Fri Aug 21 2015 Gianluca Sforna <giallu@gmail.com> 0.8.10-4
- update deps, twisted is now a monolithic package
- fix #1255739: darcs is available on all arch

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar  5 2015 Gianluca Sforna <giallu@gmail.com> - 0.8.10-2
- add patch from upstream for # 1199283

* Fri Dec 19 2014 Gianluca Sforna <giallu@gmail.com> - 0.8.10-1
- new upstream release
- remove upstreamed patch

* Mon Sep 29 2014 Gianluca Sforna <giallu@gmail.com> - 0.8.9-1
- new upstream release
- use packages from PyPI

* Tue Jun 24 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.8.8-3
- Fix FTBFS due to changes in sphinx and twisted (#1106019)
- Cleanup spec

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 23 2013 Gianluca Sforna <giallu@gmail.com> - 0.8.8-1
- new upstream release

* Mon Aug 05 2013 Gianluca Sforna <giallu@gmail.com> - 0.8.7p1-2
- Install docs to %%{_pkgdocdir} where available.

* Sun Jul 28 2013 Gianluca Sforna <giallu@gmail.com> - 0.8.7p1-1
- New upstream release
- Require python-dateutil

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6p1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6p1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 18 2012 Gianluca Sforna <giallu@gmail.com> - 0.8.6p1-2
- Add missing require for slave subpackage

* Thu Apr 05 2012 Gianluca Sforna <giallu@gmail.com> - 0.8.6p1-1
- New upstream release

* Mon Mar 12 2012 Gianluca Sforna <giallu@gmail.com> - 0.8.6-2
- New upstream release
- Enable tests again
- Don't test deprecated tla
- Correctly populate -slave subpackage (#736875)
- Fix fetching from git > 1.7.7 (#801209)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5p1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 02 2011 Dan Radez <dan@radez.net> - 0.8.5p1-1
- New Upstream Release
- updated make for the docs
- removed the buildbot.info refs added the man page

* Wed Jun 22 2011 Gianluca Sforna <giallu@gmail.com> - 0.8.4p1-2
- Upgrade to 0.8.x
- Add -master and -slave subpackages
- Split html docs in own package

* Mon May 30 2011 Gianluca Sforna <giallu@gmail.com> - 0.7.12-6
- Properly install texinfo files #694199
- Disable tests for now, need to investigate some failures

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 31 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.7.12-4
- Rebuild for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jul 22 2010 Gianluca Sforna <giallu gmail com> - 0.7.12-3
- Remove BR:bazaar (fixes FTBS)

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.7.12-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Feb  7 2010 Gianluca Sforna <giallu gmail com>
- Require python-boto for EC2 support
- Require python-twisted-conch for manhole support
- Silence rpmlint

* Fri Jan 22 2010 Gianluca Sforna <giallu gmail com> - 0.7.12-1
- New upstream release

* Mon Aug 17 2009 Steve 'Ashcrow' Milner <stevem@gnulinux.net> - 0.7.11p3-1
- Update for another XSS vuln from upstream

* Thu Aug 13 2009 Steve 'Ashcrow' Milner <stevem@gnulinux.net> - 0.7.11p2-1
- Update for XSS vuln from upstream

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.11p1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Gianluca Sforna <giallu gmail com> - 0.7.11p1-1
- New upstream release
- Change Source0 URI
- Make tests optional

* Tue Mar  3 2009 Gianluca Sforna <giallu gmail com> - 0.7.10p1-2
- New upstream release
- darcs only avaliable on ix86 platforms

* Thu Feb 26 2009 Gianluca Sforna <giallu gmail com> - 0.7.10-1
- New upstream release
- Drop upstreamed patch
- Add %%check section and needed BR

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.7.7-3
- Rebuild for Python 2.6

* Thu Apr  3 2008 Gianluca Sforna <giallu gmail com> - 0.7.7-2
- Fix upgrade path

* Mon Mar 31 2008 Gianluca Sforna <giallu gmail com> - 0.7.7-1
- new upstream release

* Thu Jan  3 2008 Gianluca Sforna <giallu gmail com> - 0.7.6-2
- pick up new .egg file

* Mon Oct 15 2007 Gianluca Sforna <giallu gmail com> - 0.7.6-1
- new upstream release
- refreshed Patch0
- requires clean up
- License tag update (GPLv2)

* Sat Mar 17 2007 Gianluca Sforna <giallu gmail com>
- Silence rpmlint

* Thu Mar 01 2007 Gianluca Sforna <giallu gmail com> - 0.7.5-1
- new upstream release
- minor spec tweaks
- Removed (unmantained and orphaned) python-cvstoys Require

* Sat Sep 09 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.7.4-2
- cleanup %%files

* Fri Sep 08 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.7.4-1
- Upstream update
- don't ghost pyo files

* Fri Jul 28 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.7.3-3
- move contribs to %%{_datadir}/%%{name}

* Fri Jul 07 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.7.3-2
- fixes for review
- added patch to remove #! where its not needed (shutup rpmlint)

* Fri Jun 02 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.7.3-1
- Inital build for FE
