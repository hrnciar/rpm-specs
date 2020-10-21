%global bashcompdir     %(pkg-config --variable=completionsdir bash-completion 2>/dev/null)
%global bashcomproot    %(dirname %{bashcompdir} 2>/dev/null)
%{?python_enable_dependency_generator}

#%%global commit 17779cf31a712c4142e8e95a408db73ca17cb778
#%%global commit_short %(c=%{commit}; echo ${c:0:7})

# Relax the percentage of code lines that need to be covered by tests a
# little. For whatever reason, running the tests while building an RPM package
# often seems to cover fewer LOCs than tests run in the upstream CI pipeline.
%global cov_fail_under 90

Name:           bodhi
Version:        5.2.2
Release:        4%{?dist}
#Release:        0.beta.1.%{commit_short}%{?dist}
BuildArch:      noarch

License:        GPLv2+
Summary:        A modular framework that facilitates publishing software updates
URL:            https://github.com/fedora-infra/bodhi
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
#Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

# Python 3.9 compatibility
Patch1:         %{url}/commit/b75af1bc.patch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: %{py3_dist alembic}
BuildRequires: %{py3_dist arrow}
BuildRequires: %{py3_dist backoff}
BuildRequires: %{py3_dist bleach}
BuildRequires: %{py3_dist celery}
BuildRequires: %{py3_dist click}
BuildRequires: %{py3_dist colander}
BuildRequires: %{py3_dist cornice_sphinx} >= 0.3
BuildRequires: %{py3_dist cornice} >= 3.1
BuildRequires: %{py3_dist dogpile.cache}
BuildRequires: %{py3_dist fedora_messaging}
BuildRequires: %{py3_dist feedgen}
BuildRequires: %{py3_dist iniparse}
BuildRequires: %{py3_dist jinja2}
BuildRequires: %{py3_dist markdown}
BuildRequires: %{py3_dist psycopg2}
BuildRequires: %{py3_dist mock}
BuildRequires: %{py3_dist pylibravatar}
BuildRequires: %{py3_dist pyramid-fas-openid}
BuildRequires: %{py3_dist pyramid-mako}
BuildRequires: %{py3_dist pyramid}
BuildRequires: %{py3_dist pytest-cov}
BuildRequires: %{py3_dist pytest}
BuildRequires: %{py3_dist python-bugzilla}
BuildRequires: %{py3_dist python-fedora}
BuildRequires: %{py3_dist pyyaml}
BuildRequires: %{py3_dist responses}
BuildRequires: %{py3_dist simplemediawiki}
BuildRequires: %{py3_dist sphinx}
BuildRequires: %{py3_dist sqlalchemy}
BuildRequires: %{py3_dist sqlalchemy_schemadisplay}
BuildRequires: %{py3_dist twisted}
BuildRequires: %{py3_dist webtest}
BuildRequires: pkgconfig(bash-completion)
BuildRequires: dnf
BuildRequires: pungi >= 4.1.20
BuildRequires: python3-createrepo_c
BuildRequires: python3-dnf
BuildRequires: python3-koji
BuildRequires: python3-librepo


%description
Bodhi is a web application that facilitates the process of publishing
updates for a software distribution.

A modular piece of the Fedora Infrastructure stack
* Utilizes the Koji Buildsystem for tracking packages.
* Creates RPM and module update repositories using Pungi, which composes a repository based
  on tagged builds in Koji.
* Manages container and Flatpak updates using skopeo or bodhi-skopeo-lite (included with the
  bodhi-server package).
* Manages RPM, container, module, and Flatpak content.


%package client
Summary: Bodhi Client

Requires: python3-bodhi-client == %{version}-%{release}


%description client
Client tools for interacting with bodhi.


%package composer
Summary: Bodhi composer backend

Requires: %{py3_dist jinja2}
Requires: bodhi-server == %{version}-%{release}
Requires: pungi >= 4.1.20
Requires: python3-createrepo_c
Requires: skopeo


%description composer
The Bodhi composer is the component that publishes Bodhi artifacts to
repositories.


%package docs
Summary: Bodhi documentation

Requires: filesystem


%description docs
Bodhi documentation.


%package -n python3-bodhi
Summary: Common files shared by bodhi-client and bodhi-server

%{?python_provide:%python_provide python3-bodhi}


%description -n python3-bodhi
Common files shared by bodhi-client and bodhi-server.


%package -n python3-bodhi-client
Summary: REST API bindings for Python.

Requires: /usr/bin/koji
Requires: python3-bodhi == %{version}-%{release}
Requires: python3-dnf
Requires: python3-koji

%{?python_provide:%python_provide python3-bodhi-client}


%description -n python3-bodhi-client
REST API bindings for Python.


%package -n python3-bodhi-messages
Summary: Python convenience package for interacting with Bodhi messages

Requires: python3-bodhi == %{version}-%{release}

%{?python_provide:%python_provide python3-bodhi-messages}


%description -n python3-bodhi-messages
Python convenience package for interacting with Bodhi messages.


%package server
Summary: A modular framework that facilitates publishing software updates

Requires: python3-bodhi-client == %{version}-%{release}
Requires: python3-bodhi-messages == %{version}-%{release}
Requires: fedora-messaging
Requires: git
Requires: httpd
Requires: intltool
Requires: python3-koji
Requires: python3-librepo
Requires: python3-mod_wsgi

Provides:  bundled(aajohan-comfortaa-fonts)
Provides:  bundled(abattis-cantarell-fonts)
Provides:  bundled(bootstrap) = 3.0.1
Provides:  bundled(bootstrap) = 3.0.2
Provides:  bundled(bootstrap) = 3.1.1
Provides:  bundled(chrissimpkins-hack-fonts)
Provides:  bundled(fedora-bootstrap) = 1.0.1
Provides:  bundled(fontawesome-fonts-web) = 4.4.0
Provides:  bundled(js-chart)
Provides:  bundled(js-excanvas)
Provides:  bundled(js-jquery) = 1.10.2
Provides:  bundled(js-jquery) = 2.0.3
Provides:  bundled(js-messenger)
Provides:  bundled(js-moment)
Provides:  bundled(js-typeahead.js) = 1.1.1
Provides:  bundled(nodejs-flot)
Provides:  bundled(open-sans-fonts)
Provides:  bundled(xstatic-bootstrap-datepicker-common)


%description server
Bodhi is a modular framework that facilitates the process of publishing
updates for a software distribution.


%prep
%autosetup -p1 -n bodhi-%{version}
#%%autosetup -p1 -n bodhi-%{commit}

# Kill some dev deps
sed -i '/pyramid_debugtoolbar/d' setup.py
sed -i '/pyramid_debugtoolbar/d' devel/development.ini.example

# The unit tests needs a development.ini
mv devel/development.ini.example development.ini


%build
%py3_build

export PYTHONPATH=`pwd`
make %{?_smp_mflags} -C docs html
make %{?_smp_mflags} -C docs man


%install
%py3_install

%{__mkdir_p} %{buildroot}/var/lib/bodhi
%{__mkdir_p} %{buildroot}/var/cache/bodhi
%{__mkdir_p} %{buildroot}%{_sysconfdir}/httpd/conf.d
%{__mkdir_p} %{buildroot}%{_sysconfdir}/bodhi
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}
%{__mkdir_p} -m 0755 %{buildroot}/%{_localstatedir}/log/bodhi

install -Dpm 0755 bodhi-complete.sh %{buildroot}%{bashcompdir}/%{name}
install -m 644 apache/%{name}.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
sed -i -s 's/BODHI_VERSION/%{version}/g' %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
install -m 640 production.ini %{buildroot}%{_sysconfdir}/%{name}/production.ini
install -m 640 alembic.ini %{buildroot}%{_sysconfdir}/%{name}/alembic.ini
install apache/%{name}.wsgi %{buildroot}%{_datadir}/%{name}/%{name}.wsgi

install -d %{buildroot}%{_mandir}/man1
install -pm0644 docs/_build/man/*.1 %{buildroot}%{_mandir}/man1/


%check
# The tests need bodhi to be installed to pass. Let's build a venv so we can install bodhi
# there.
%{__python3} -m venv --system-site-packages --without-pip .test-venv

.test-venv/bin/python3 setup.py develop
.test-venv/bin/python3 /usr/bin/py.test-3 --cov-fail-under=%{cov_fail_under} -v bodhi/tests


%pre server
%{_sbindir}/groupadd -r %{name} &>/dev/null || :
%{_sbindir}/useradd  -r -s /sbin/nologin -d %{_datadir}/%{name} -M \
                     -c 'Bodhi Server' -g %{name} %{name} &>/dev/null || :


%files client
%license COPYING
%doc README.rst
%{bashcomproot}
%{_bindir}/bodhi
%{_mandir}/man1/bodhi.1*


%files composer
%license COPYING
%doc README.rst
%{python3_sitelib}/%{name}/server/tasks/composer.py
# The __pycache__ folder itself is owned by bodhi-server.
%{python3_sitelib}/%{name}/server/tasks/__pycache__/composer.*
%{python3_sitelib}/%{name}/server/metadata.py
%{python3_sitelib}/%{name}/server/__pycache__/metadata.*


%files docs
%license COPYING
%doc docs/_build/html/ README.rst


%files -n python3-bodhi
%license COPYING
%doc README.rst
%dir %{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}/__init__.py
%{python3_sitelib}/%{name}/__pycache__
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info


%files -n python3-bodhi-client
%license COPYING
%doc README.rst
%{python3_sitelib}/%{name}/client
%{python3_sitelib}/%{name}_client-%{version}-py%{python3_version}.egg-info


%files -n python3-bodhi-messages
%license COPYING
%doc README.rst
%{python3_sitelib}/%{name}/messages
%{python3_sitelib}/%{name}_messages-%{version}-py%{python3_version}.egg-info


%files server
%license COPYING
%doc README.rst
%{_bindir}/bodhi-approve-testing
%{_bindir}/bodhi-check-policies
%{_bindir}/bodhi-clean-old-composes
%{_bindir}/bodhi-expire-overrides
%{_bindir}/bodhi-push
%{_bindir}/bodhi-sar
%{_bindir}/bodhi-shell
%{_bindir}/bodhi-skopeo-lite
%{_bindir}/bodhi-untag-branched
%{_bindir}/initialize_bodhi_db
%config(noreplace) %{_sysconfdir}/bodhi/alembic.ini
%config(noreplace) %{_sysconfdir}/httpd/conf.d/bodhi.conf
%dir %{_sysconfdir}/bodhi/
%{python3_sitelib}/%{name}/server
%{python3_sitelib}/%{name}_server-%{version}-py%{python3_version}.egg-info
%{_mandir}/man1/bodhi-*.1*
%{_mandir}/man1/initialize_bodhi_db.1*
%attr(-,bodhi,root) %{_datadir}/%{name}
%attr(-,bodhi,bodhi) %config(noreplace) %{_sysconfdir}/bodhi/*
%attr(0775,bodhi,bodhi) %{_localstatedir}/cache/bodhi
# These excluded files are in the bodhi-consumers package so don't include them here.
%exclude %{python3_sitelib}/%{name}/server/tasks/composer.py
%exclude %{python3_sitelib}/%{name}/server/tasks/__pycache__/composer.*
%exclude %{python3_sitelib}/%{name}/server/metadata.py
%exclude %{python3_sitelib}/%{name}/server/__pycache__/metadata.*


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 5.2.2-2
- Rebuilt for Python 3.9

* Wed Mar 25 2020 Clément Verna <cverna@fedoraproject.org> - 5.2.2-1
- Update to 5.2.2
  https://github.com/fedora-infra/bodhi/releases/tag/5.2.2

* Mon Mar 23 2020 Clément Verna <cverna@fedoraproject.org> - 5.2.1-1
- Update to 5.2.1
  https://github.com/fedora-infra/bodhi/releases/tag/5.2.1

* Thu Mar 19 2020 Clément Verna <cverna@fedoraproject.org> - 5.2.0-1
- Update to 5.2.0
  https://github.com/fedora-infra/bodhi/releases/tag/5.2.0

* Thu Jan 30 2020 Nils Philippsen <nils@redhat.com> - 5.1.1-1
- Update to 5.1.1.
  https://github.com/fedora-infra/bodhi/releases/tag/5.1.1

* Tue Jan 28 2020 Nils Philippsen <nils@redhat.com> - 5.1.0-3
- remove obsolete patch which caused the build to fail
- relax test coverage requirements

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Aurelien Bompard <abompard@fedoraproject.org> - 5.1.0-1
- Update to 5.1.0. https://github.com/fedora-infra/bodhi/releases/tag/5.1.0

* Thu Nov 28 2019 Aurelien Bompard <abompard@fedoraproject.org> - 5.0.0-3
- Hotfix for a crash in the push script.

* Thu Nov 28 2019 Aurelien Bompard <abompard@fedoraproject.org> - 5.0.0-2
- Hotfix with commit 5da6aaaf.

* Thu Nov 07 2019 Aurelien Bompard <abompard@fedoraproject.org> - 5.0.0-1
- Update to 5.0.0. https://github.com/fedora-infra/bodhi/releases/tag/5.0.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 25 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-5
- Enable the documentation

* Tue Aug 20 2019 Aurelien Bompard <abompard@fedoraproject.org> - 4.1.1-1
- Update to 4.1.1. https://github.com/fedora-infra/bodhi/releases/tag/4.1.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Aurelien Bompard <abompard@fedoraproject.org> - 4.1.0-3
- Fix build on Rawhide

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Aurelien Bompard <abompard@fedoraproject.org> - 4.1.0-1
- Update to 4.1.0. https://github.com/fedora-infra/bodhi/releases/tag/4.1.0

* Mon Jun 17 2019 Adam Williamson <awilliam@redhat.com> - 4.0.2-2
- Backport fix for 'updates download' with multiple packages (#3324)

* Mon Jun 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.0.2-1
- Update to 4.0.2 (#1715576).
- https://github.com/fedora-infra/bodhi/releases/tag/4.0.2

* Thu May 30 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.0.2-1
- Update to 4.0.2 (#1715576).
- https://github.com/fedora-infra/bodhi/releases/tag/4.0.2

* Wed May 29 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.0.1-1
- Update to 4.0.1.
- https://github.com/fedora-infra/bodhi/releases/tag/4.0.1

* Thu May 23 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.0.0-1
- Update to 4.0.0.
- https://github.com/fedora-infra/bodhi/releases/tag/4.0.0

* Fri Apr 12 2019 Aurelien Bompard <abompard@fedoraproject.org> - 3.14.0-1
- Update to 3.14.0.
- https://github.com/fedora-infra/bodhi/releases/tag/3.14.0

* Thu Feb 28 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.13.3-1
- Update to 3.13.3.
- https://github.com/fedora-infra/bodhi/releases/tag/3.13.3

* Tue Feb 19 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.13.2-1
- Update to 3.13.2.
- https://github.com/fedora-infra/bodhi/releases/tag/3.13.2

* Mon Feb 18 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.13.1-1
- Update to 3.13.1.
- https://github.com/fedora-infra/bodhi/releases/tag/3.13.1

* Fri Feb 15 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.13.0-1
- Update to 3.13.0.
- https://github.com/fedora-infra/bodhi/releases/tag/3.13.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-103
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.12.0-102
- Enable dependency generator

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 3.12.0-101
- Drop Python 2 subpackage (#1631858)

* Mon Dec 17 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.12.0-100
- Upgrade to 3.12.0.
- https://github.com/fedora-infra/bodhi/releases/tag/3.12.0

* Wed Dec 05 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.11.3-100
- Update to 3.11.3.
- https://github.com/fedora-infra/bodhi/releases/tag/3.11.3

* Mon Dec 03 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.11.2-100
- Update to 3.11.2.
- https://github.com/fedora-infra/bodhi/releases/tag/3.11.2

* Tue Nov 27 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.11.1-100
- Update to 3.11.1.

* Fri Nov 16 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.11.0-3
- Bump the release to 3 so that f29-infra has a newer version than f29.

* Fri Nov 16 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.11.0-1
- Update to 3.11.0.
- Switch bodhi-server to use Python 3 (#1631858).

* Mon Oct 15 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.10.1-2
- Backport some patches for compatibility with click-7.0.0.

* Tue Oct 09 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.10.1-1
- Update to 3.10.1.
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-10-1

* Wed Sep 19 2018 Todd Zullinger <tmz@pobox.com> - 3.10.0-2
- Use recommended directory for bash-completion file

* Mon Sep 17 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.10.0-1
- Update to 3.10.0.
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-10-0

* Wed Aug 22 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.9.0-1
- Update to 3.9.0.
- Fix FTBFS (#1603504).
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-9-0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.8.1-2
- Rebuilt for Python 3.7

* Tue Jun 12 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.8.1-1
- Update to 3.8.1.
- Fix a Python 3.7 FTBFS (#1589990).
- https://github.com/fedora-infra/bodhi/releases/tag/3.8.1

* Wed May 16 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0 (#1582628).
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-8-0

* Tue May 08 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.7.0-1
- Update to 3.7.0.
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-7-0

* Mon Apr 23 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1 (#1570947).
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-6-1
- bodhi-server no longer provides the composer (masher.py). It is now provided
  by a separate bodhi-composer subpackage.

* Mon Mar 26 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.6.0-1
- Update to 3.6.0 (#1567959).
- https://bodhi.stg.fedoraproject.org/docs/user/release_notes.html#v3-6-0
- The CLI now uses Python 3 (#1024795).
- bodhi-client no longer contains the Python bindings - they were split out
  into new python2-bodhi-client and python3-bodhi-client subpackages.

* Mon Mar 26 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.5.2-1
- Update to 3.5.2 (#1560680).
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-5-2

* Wed Mar 21 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.5.1-1
- Update to 3.5.1.
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-5-1

* Tue Feb 27 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.5.0-1
- Update to 3.5.0.
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-5-0

* Mon Feb 26 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0.
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-4-0

* Fri Feb 16 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.3.0-1
- Update to 3.3.0.
- https://bodhi.fedoraproject.org/docs/user/release_notes.html#v3-3-0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0.
- Use the fancy new py2_dist macro for dependencies.
- Fix a FTBFS (#1530245).
- Drop the moveshelf patch because it causes tests to fail.

* Fri Jan 05 2018 Patrick Uiterwijk <patrick@puiterwijk.org> - 3.1.0-3
- Apply patch to move the shelves
