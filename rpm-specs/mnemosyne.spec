%{!?qt5_qtwebengine_arches:%global qt5_qtwebengine_arches %{ix86} x86_64 %{arm} aarch64 mips mipsel mips64el}

%bcond_without check

Name:		mnemosyne
Summary:	Flash-card learning tool
Version:	2.6.1
Release:	6%{?dist}
URL:		https://www.mnemosyne-proj.org/
Source0:	https://downloads.sourceforge.net/sourceforge/mnemosyne-proj/Mnemosyne-%{version}.tar.gz
# contains missing tests and LICENSE files from upstream repo
Source1:        Mnemosyne-tests-%{version}.tar.xz
# run this script to obtain the above tarball
Source10:       mnemosyne-mktarball.sh
Patch0:		mnemosyne-desktop.patch
License:	AGPLv3

BuildArch:	noarch
# no python3-qt5-webengine on power64
ExclusiveArch:	noarch %{qt5_qtwebengine_arches}
BuildRequires:	desktop-file-utils
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%if %{with check}
# unpackaged https://pypi.python.org/pypi/Cheroot
#BuildRequires: python3-cheroot
BuildRequires:	python3-cherrypy
BuildRequires:	python3-nose
BuildRequires:	python3-qt5
BuildRequires:	texlive-collection-latexrecommended
BuildRequires:	texlive-dvipng
%endif
Requires:	hicolor-icon-theme
Requires:	python3-qt5-webkit
Requires:	python3-qt5-webengine
Requires:	python3-matplotlib-qt5
Requires:	python3-cherrypy
Requires:	python3-webob
Requires:	python3-pillow
Requires:       python3-pyopengl

%description
Mnemosyne resembles a traditional flash-card program but with an
important twist: it uses a sophisticated algorithm to schedule the best
time for a card to come up for review.

Optional dependencies:
* latex: enables entering formulas using latex syntax.

%prep
%setup -q -n Mnemosyne-%{version} -a 1
%patch0 -p1 -b .d
rm -r Mnemosyne.egg-info
# requires unpackaged Cheroot python module
rm tests/test_sync.py
cp -p mnemosyne/LICENSE LICENSE.mnemosyne
cp -p openSM2sync/LICENSE LICENSE.openSM2sync

%build
%py3_build

%install
%py3_install

install -d %{buildroot}%{_datadir}/applications
desktop-file-install --vendor="" \
	--dir=%{buildroot}%{_datadir}/applications \
	%{name}.desktop

install -d %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps
pushd %{buildroot}/%{_datadir}/icons
mv %{name}.png hicolor/128x128/apps/%{name}.png
popd

%find_lang %{name}

%if %{with check}
%check
# tests fail if run in parallel
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m nose tests
%endif

%files -f %{name}.lang
%doc ChangeLog README
%license LICENSE LICENSE.mnemosyne LICENSE.openSM2sync
%{_bindir}/%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/Mnemosyne-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/openSM2sync
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-6
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Dominik Mierzejewski <rpm@greysector.net> 2.6.1-1
- update to 2.6.1 (#1613593)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.6-2
- Rebuilt for Python 3.7

* Tue Mar 06 2018 Dominik Mierzejewski <rpm@greysector.net> 2.6-1
- update to 2.6 (#1524747)
- add missing pyopengl dependency to fix crash (#1546829)
- include tests and license texts from upstream repo
- switch to HTTPS URL

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.5-3
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Dominik Mierzejewski <rpm@greysector.net> 2.5-1
- update to 2.5 (#1465009)

* Tue Jun 27 2017 Dominik Mierzejewski <rpm@greysector.net> 2.4.1-2
- make sure qt5_qtwebengine_arches macro is defined

* Wed Jun 21 2017 Dominik Mierzejewski <rpm@greysector.net> 2.4.1-1
- update to 2.4.1
- use ExclusiveArch to restrict availability to qt5_qtwebengine_arches
- use https for Source0:
- use name macro consistently
- tighten file list using python3_version macro
- force rebuild of egg-info

* Wed Mar 22 2017 Jiri Popelka <jpopelka@redhat.com> - 2.4-4
- no python3-qt5-webengine on power64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 2.4-2
- Rebuild for Python 3.6

* Tue Dec 06 2016 Jiri Popelka <jpopelka@redhat.com> - 2.4-1
- 2.4: Python3 & PyQt5

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 03 2016 Jiri Popelka <jpopelka@redhat.com> - 2.3.6-1
- 2.3.6

* Fri Apr 08 2016 Jiri Popelka <jpopelka@redhat.com> - 2.3.5-4
- #1219556 has been fixed

* Wed Mar 02 2016 Rex Dieter <rdieter@fedoraproject.org> 2.3.5-3
- Requires: PyQt4-webkit

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Jiri Popelka <jpopelka@redhat.com> - 2.3.5-1
- 2.3.5

* Tue Oct 06 2015 Jiri Popelka <jpopelka@redhat.com> - 2.3.4-1
- 2.3.4

* Wed Sep 30 2015 Jiri Popelka <jpopelka@redhat.com> - 2.3.3-4
- Requires: python-matplotlib-qt5 due to bug #1219556

* Tue Aug 11 2015 Jiri Popelka <jpopelka@redhat.com> - 2.3.3-3
- %%py2_build && %%py2_install

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Jiri Popelka <jpopelka@redhat.com> - 2.3.3-1
- 2.3.3

* Wed Feb 25 2015 Jiri Popelka <jpopelka@redhat.com> - 2.3.2-1
- 2.3.2

* Thu Jun 19 2014 Jiri Popelka <jpopelka@redhat.com> - 2.3.1-1
- 2.3.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 03 2014 Jiri Popelka <jpopelka@redhat.com> - 2.3-1
- 2.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 15 2013 Jiri Popelka <jpopelka@redhat.com> - 2.2.1-1
- updated to 2.2.1 (no LICENSE file ?)

* Mon Jan 28 2013 Jiri Popelka <jpopelka@redhat.com> - 2.2-3.a
- python-matplotlib moved qt4 backend to -qt4 subpackage (#903760)

* Fri Jan 25 2013 Jiri Popelka <jpopelka@redhat.com> - 2.2-2.a
- updated to 2.2a

* Wed Dec 05 2012 Jiri Popelka <jpopelka@redhat.com> - 2.2-1
- updated to 2.2

* Thu Sep 13 2012 Jiri Popelka <jpopelka@redhat.com> - 2.1-1
- updated to 2.1

* Thu Aug 02 2012 Jiri Popelka <jpopelka@redhat.com> - 2.0.1-1
- updated to 2.0.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 18 2012 Jiri Popelka <jpopelka@redhat.com> - 2.0-1
- updated to 2.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 17 2010 Jiri Popelka <jpopelka@redhat.com> - 1.2.2-3
- requires Python Imaging Library (PIL) (bug #654291)

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 07 2010 Dominik Mierzejewski <rpm@greysector.net> 1.2.2-1
- updated to 1.2.2
- upstream changelog: http://www.mnemosyne-proj.org/news.php

* Wed Aug 26 2009 Dominik Mierzejewski <rpm@greysector.net> 1.2.1-1
- updated to 1.2.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3.r1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2.r1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 Dominik Mierzejewski <rpm@greysector.net> 1.2-1.r1
- updated to 1.2-r1, fixes https://bugs.launchpad.net/mnemosyne-proj/+bug/252152

* Tue Nov 11 2008 Dominik Mierzejewski <rpm@greysector.net> 1.1.1-3.r1
- fixed .desktop file comment to conform to GNOME HIG
- removed a redundant python setup.py install call
- moved the .desktop file category addition to the patch
- added missing hicolor-icon-theme-requires

* Fri Oct 03 2008 Dominik Mierzejewski <rpm@greysector.net> 1.1.1-2.r1
- updated to 1.1.1-r1
- dropped separate icon (fixed upstream)

* Thu Sep 11 2008 Dominik Mierzejewski <rpm@greysector.net> 1.1.1-1
- initial package
- include fixed icon from 1.1
