Name:           tortoisehg
Version:        5.4
Release:        2%{?dist}
Summary:        Mercurial GUI command line tool thg
License:        GPLv2
# - few files are however under the more permissive GPLv2+
URL:            https://tortoisehg.bitbucket.io/
Source0:        https://bitbucket.org/tortoisehg/thg/get/%{version}.tar.bz2#/%{name}-%{version}.tar.bz2
Source1:        thg.appdata.xml
BuildArch:      noarch
BuildRequires:  python3-devel, gettext, python3-sphinx, python3-qt5, desktop-file-utils, libappstream-glib
BuildRequires:  mercurial-py3 >= 5.3, mercurial-py3 < 5.5
Requires:       mercurial-py3 >= 5.3, mercurial-py3 < 5.5, python3-iniparse
Requires:       python3-qt5, python3-qscintilla-qt5, python3-pygments
Requires:       python3-gobject-base

%description
This package contains the thg command line tool, which provides a graphical
user interface to the Mercurial distributed revision control system.

%package        nautilus
Summary:        Mercurial GUI plug-in to the Nautilus file manager
Requires:       %{name} = %{version}-%{release}, python3-nautilus

%description    nautilus
This package contains the TortoiseHg Gnome/Nautilus extension, which makes the
Mercurial distributed revision control system available in the file manager
with a graphical interface.

Note that the nautilus extension has been deprecated upstream.

%prep
%autosetup -n tortoisehg-thg-68b8b70539b4 -p 1

# Hack to try to support Mercurial 4.7 until it gets upgraded
#sed -i "s/testedwith = '4.8 4.9'/testedwith = '4.7 4.8 4.9'/" tortoisehg/util/hgversion.py

# Avoid wrong upgrade recommendation caused by (4, 9) < (4, 9, 0)
#sed -i '/curver = (0,0,0)/a\        if len(curver) < 3: curver = curver + (0,)' tortoisehg/hgqt/bugreport.py

# Support Python 3.9 - https://bitbucket.org/tortoisehg/thg/issues/5549/i18n-msgfmtpy-arrayarray-tostring-fails-on
sed -i '/array.array/s/tostring/tobytes/' i18n/msgfmt.py

%build
%py3_build

# override config.py from setup.py build_config()
cat > build/lib/tortoisehg/util/config.py << EOT
bin_path     = "%{_bindir}"
license_path = "%{_licensedir}/tortoisehg/COPYING.txt"
locale_path  = "%{_datadir}/locale"
icon_path    = "%{_datadir}/pixmaps/tortoisehg/icons"
nofork       = True
EOT

(cd doc && make html)
rm doc/build/html/.buildinfo

%install
%py3_install
rm $RPM_BUILD_ROOT/%{python3_sitelib}/hgext3rd/__init__.*
rm $RPM_BUILD_ROOT/%{python3_sitelib}/hgext3rd/__pycache__/__init__.*

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/mercurial/hgrc.d
install -pm0644 contrib/mergetools.rc $RPM_BUILD_ROOT%{_sysconfdir}/mercurial/hgrc.d/thgmergetools.rc

ln -s tortoisehg/icons/scalable/apps/thg.svg $RPM_BUILD_ROOT%{_datadir}/pixmaps/thg_logo.svg
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications contrib/thg.desktop
install -D %{SOURCE1} -pm0644 $RPM_BUILD_ROOT/%{_datadir}/appdata/thg.appdata.xml

%find_lang %{name}

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/thg.appdata.xml

%files -f %{name}.lang
%license COPYING.txt
%doc doc/build/html/
%config(noreplace) %{_sysconfdir}/mercurial/hgrc.d/thgmergetools.rc
%{_bindir}/thg
%{_datadir}/appdata/thg.appdata.xml
%{python3_sitelib}/hgext3rd/thg.py*
%{python3_sitelib}/hgext3rd/__pycache__/thg.*.pyc
%{python3_sitelib}/tortoisehg/
%{python3_sitelib}/tortoisehg-*.egg-info
%{_datadir}/pixmaps/tortoisehg/
%{_datadir}/pixmaps/thg_logo.svg
%{_datadir}/applications/thg.desktop

%files nautilus
%{_datadir}/nautilus-python/extensions/nautilus-thg.py*

%changelog
* Thu Jun 04 2020 Mads Kiilerich <mads@kiilerich.com> - 5.4-2
- Workaround for array.array().tostring() removed in Python 3.9

* Wed Jun 03 2020 Mads Kiilerich <mads@kiilerich.com> - 5.4-1
- tortoisehg 5.4

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.3.2-2
- Rebuilt for Python 3.9

* Fri Apr 10 2020 Mads Kiilerich <mads@kiilerich.com> - 5.3.2-1
- tortoisehg 5.3.2

* Wed Mar 11 2020 Mads Kiilerich <mads@kiilerich.com> - 5.3.1-1
- tortoisehg 5.3.1

* Thu Mar 05 2020 Mads Kiilerich <mads@kiilerich.com> - 5.3-1
- tortoisehg 5.3
- setup.py build will override custom config.py - create it after build
- COPYING.txt is no longer in _pkgdocdir - use _licensedir

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-20191202.00a9f6fd23fe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 01 2019 Mads Kiilerich <mads@kiilerich.com> - 5.1-20191201.00a9f6fd23fe
- early 5.2 snapshot 5.1+229-00a9f6fd23fe
- migrate to py3

* Mon Aug 12 2019 Mads Kiilerich <mads@kiilerich.com> - 5.0.2-2
- tortoisehg 5.0.2 requires Mercurial at build time

* Mon Aug 12 2019 Mads Kiilerich <mads@kiilerich.com> - 5.0.2-1
- tortoisehg 5.0.2
- drop gnome-python2-gconf dependency - it is no longer available in Fedora and
  is not essential (rhbz#1739937)

* Wed Aug 07 2019 Mads Kiilerich <mads@kiilerich.com> - 4.9-4
- Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 07 2019 Mads Kiilerich <mads@kiilerich.com> - 4.9-2
- Use python3-sphinx for building docs - python2-sphinx is no longer available

* Sun Apr 07 2019 Mads Kiilerich <mads@kiilerich.com> - 4.9-1
- tortoisehg 4.9

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Mads Kiilerich <mads@kiilerich.com> - 4.6.1-1
- tortoisehg 4.6.1
- Rename appdata thg.appdata.xml #1570409
- python2-enum34 is also needed for building ... but apparently not at runtime
- Bump all Python references to Python2

* Tue Jul 24 2018 Mads Kiilerich <mads@kiilerich.com> - 4.6-3
- TortoiseHg actually require python-qt5 and python2-qscintilla-qt5 now

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 22 2018 Mads Kiilerich <mads@kiilerich.com> - 4.6-1
- tortoisehg 4.6

* Sun Apr 08 2018 Mads Kiilerich <mads@kiilerich.com> - 4.5.3-1
- tortoisehg 4.5.3

* Sun Mar 11 2018 Mads Kiilerich <mads@kiilerich.com> - 4.5.2-1
- tortoisehg 4.5.2

* Wed Feb 21 2018 Mads Kiilerich <mads@kiilerich.com> - 4.5-1
- tortoisehg 4.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 29 2017 Mads Kiilerich <mads@kiilerich.com> - 4.4.2-2
- Rebuild

* Thu Dec 28 2017 Mads Kiilerich <mads@kiilerich.com> - 4.4.2-1
- tortoisehg 4.4.2

* Sat Jul 29 2017 Mads Kiilerich <mads@kiilerich.com> - 4.2.2-1
- tortoisehg 4.2.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Björn Esser <besser82@fedoraproject.org> - 4.2.1-1
- tortoisehg 4.2.1 (rhbz#917634)
- Update spec file to recent guidelines

* Sun May 07 2017 Mads Kiilerich <mads@kiilerich.com> - 4.2-1
- tortoisehg 4.2

* Wed Apr 05 2017 Mads Kiilerich <mads@kiilerich.com> - 4.1.2-1
- tortoisehg 4.1.2

* Tue Feb 21 2017 Mads Kiilerich <mads@kiilerich.com> - 4.1-1
- tortoisehg 4.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Mads Kiilerich <mads@kiilerich.com> - 4.0.1-1
- tortoisehg 4.0.1

* Sun Jun 05 2016 Mads Kiilerich <mads@kiilerich.com> - 3.8.3-1
- tortoisehg 3.8.3

* Sat Mar 05 2016 Mads Kiilerich <mads@kiilerich.com> - 3.7.2-1
- tortoisehg 3.7.2

* Sun Feb 07 2016 Mads Kiilerich <mads@kiilerich.com> - 3.7.1-1
- tortoisehg 3.7.1

* Sun Feb 07 2016 Mads Kiilerich <mads@kiilerich.com> - 3.6.2-5
- Install tortoisehg.appdata.xml as mode 644 - avoid rmplint 'script-without-shebang'

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 01 2016 Mads Kiilerich <mads@kiilerich.com> - 3.6.2-3
- Fix nautilus plugin - add python-gobject-base as dependency
- Introduce tortoisehg.appdata.xml with appdata info for GNOME Software

* Thu Dec 24 2015 Mads Kiilerich <mads@kiilerich.com> - 3.6.2-2
- support Mercurial 3.6.x in dependencies

* Thu Dec 24 2015 Mads Kiilerich <mads@kiilerich.com> - 3.6.2-1
- tortoisehg 3.6.2

* Tue Nov 10 2015 Mads Kiilerich <mads@kiilerich.com> - 3.6-1
- tortoisehg 3.6

* Fri Sep 11 2015 Mads Kiilerich <mads@kiilerich.com> - 3.5.1-1
- tortoisehg 3.5.1

* Sat Aug 15 2015 Mads Kiilerich <mads@kiilerich.com> - 3.5-2
- support Mercurial 3.5 in dependencies too

* Sun Aug 09 2015 Mads Kiilerich <mads@kiilerich.com> - 3.5-1
- tortoisehg 3.5

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 10 2015 Mads Kiilerich <mads@kiilerich.com> - 3.4-1
- tortoisehg 3.4

* Thu Apr 02 2015 Mads Kiilerich <mads@kiilerich.com> - 3.3.3-1
- tortoisehg 3.3.3

* Mon Mar 16 2015 Mads Kiilerich <mads@kiilerich.com> - 3.3.2-1
- tortoisehg 3.3.2

* Fri Feb 20 2015 Mads Kiilerich <mads@kiilerich.com> - 3.3-3
- actually support Mercurial 3.3 - disable hack

* Wed Feb 18 2015 Mads Kiilerich <mads@kiilerich.com> - 3.3-2
- require Mercurial < 3.4

* Thu Feb 12 2015 Mads Kiilerich <mads@kiilerich.com> - 3.3-1
- tortoisehg 3.3

* Thu Feb 12 2015 Mads Kiilerich <mads@kiilerich.com> - 3.2.4-1
- tortoisehg 3.2.4

* Sun Dec 14 2014 Mads Kiilerich <mads@kiilerich.com> - 3.2.1-1
- tortoisehg 3.2.1

* Sun Sep 07 2014 Mads Kiilerich <mads@kiilerich.com> - 3.1.1-1
- tortoisehg 3.1.1

* Sat Aug 09 2014 Mads Kiilerich <mads@kiilerich.com> - 3.1-1
- tortoisehg 3.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Mads Kiilerich <mads@kiilerich.com> - 3.0-1
- tortoisehg 3.0

* Thu Apr 03 2014 Mads Kiilerich <mads@kiilerich.com> - 2.11.2-1
- tortoisehg 2.11.2

* Wed Mar 05 2014 Mads Kiilerich <mads@kiilerich.com> - 2.11.1-1
- tortoisehg 2.11.1

* Thu Feb 06 2014 Mads Kiilerich <mads@kiilerich.com> - 2.11-1
- tortoisehg 2.11

* Sun Jan 26 2014 Mads Kiilerich <mads@kiilerich.com> - 2.10.2-1
- tortoisehg 2.10.2

* Wed Nov 06 2013 Mads Kiilerich <mads@kiilerich.com> - 2.10-1
- tortoisehg 2.10

* Wed Oct 09 2013 Mads Kiilerich <mads@kiilerich.com> - 2.9.2-1
- tortoisehg 2.9.2

* Mon Sep 09 2013 Mads Kiilerich <mads@kiilerich.com> - 2.9.1-1
- tortoisehg-2.9.1
- .desktop file is now named correctly upstream ... but not in the tar

* Wed Aug 07 2013 Mads Kiilerich <mads@kiilerich.com> - 2.9-2
- use %%{_pkgdocdir} to get the new path to unversioned doc dir (#993947)

* Sun Aug 04 2013 Mads Kiilerich <mads@kiilerich.com> - 2.9-1
- tortoisehg-2.9
- rename desktop file to thg.desktop so it matches WM_CLASS

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 Mads Kiilerich <mads@kiilerich.com> - 2.8-1
- tortoisehg-2.8

* Tue Mar 12 2013 Mads Kiilerich <mads@kiilerich.com> - 2.7.1-2
- support for PyQt-4.10 #920749

* Tue Mar 05 2013 Mads Kiilerich <mads@kiilerich.com> - 2.7.1-1
- tortoisehg-2.7.1

* Mon Feb 04 2013 Mads Kiilerich <mads@kiilerich.com> - 2.7-1
- tortoisehg-2.7

* Fri Jan 04 2013 Mads Kiilerich <mads@kiilerich.com> - 2.6.2-1
- tortoisehg-2.6.2

* Mon Nov 19 2012 Mads Kiilerich <mads@kiilerich.com> - 2.6-1
- tortoisehg-2.6

* Wed Oct 03 2012 Mads Kiilerich <mads@kiilerich.com> - 2.5.1-1
- tortoisehg-2.5.1

* Thu Sep 06 2012 Mads Kiilerich <mads@kiilerich.com> - 2.5-1
- tortoisehg-2.5

* Tue Aug 21 2012 Mads Kiilerich <mads@kiilerich.com> - 2.4.3-1
- tortoisehg-2.4.3

* Sun Aug 19 2012 Mads Kiilerich <mads@kiilerich.com> - 2.4.2-3
- update nautilus-python extension directory
- make the package noarch
- accept mercurial 2.3 while waiting for a new thg release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 08 2012 Mads Kiilerich <mads@kiilerich.com> - 2.4.2-1
- tortoisehg-2.4.2
- fix naming of logo svg

* Sat Jun 09 2012 Mads Kiilerich <mads@kiilerich.com> - 2.4.1-1
- tortoisehg-2.4.1

* Sun May 06 2012 Mads Kiilerich <mads@kiilerich.com> - 2.4-1
- tortoisehg-2.4

* Fri May 04 2012 Mads Kiilerich <mads@kiilerich.com> - 2.3.2-2
- pretend compatibility with Mercurial 2.2.x as well - not just 2.2

* Tue Apr 24 2012 Mads Kiilerich <mads@kiilerich.com> - 2.3.2-1
- tortoisehg-2.3.2

* Sat Mar 10 2012 Mads Kiilerich <mads@kiilerich.com> - 2.3.1-1
- tortoisehg-2.3.1
- remove Mercurial 2.1 hack

* Thu Feb 16 2012 Mads Kiilerich <mads@kiilerich.com> - 2.3-1
- tortoisehg-2.3

* Wed Jan 25 2012 Mads Kiilerich <mads@kiilerich.com> - 2.2.2-3
- actually apply hack to relax version check so it works with mercurial-2.1

* Wed Jan 25 2012 Mads Kiilerich <mads@kiilerich.com> - 2.2.2-2
- bump Mercurial version requirement to accept mercurial-2.1-1.rc1.
  tortoisehg-2.2.2 happens to work with the next version of Mercurial anyway.

* Wed Jan 11 2012 Mads Kiilerich <mads@kiilerich.com> - 2.2.2-1
- tortoisehg-2.2.2

* Thu Dec 22 2011 Mads Kiilerich <mads@kiilerich.com> - 2.2.1-1
- tortoisehg-2.2.1

* Wed Nov 09 2011 Mads Kiilerich <mads@kiilerich.com> - 2.2-1
- tortoisehg-2.2

* Fri Oct 07 2011 Mads Kiilerich <mads@kiilerich.com> - 2.1.4-2
- the real tortoisehg-2.1.4, not just a stupid proxy

* Thu Oct 06 2011 Mads Kiilerich <mads@kiilerich.com> - 2.1.4-1
- tortoisehg-2.1.4

* Sun Aug 28 2011 Mads Kiilerich <mads@kiilerich.com> - 2.1.3-1
- tortoisehg-2.1.3

* Wed Aug 03 2011 Mads Kiilerich <mads@kiilerich.com> - 2.1.2-1
- tortoisehg-2.1.2

* Mon Jul 11 2011 Mads Kiilerich <mads@kiilerich.com> - 2.1.1-1
- tortoisehg-2.1.1
- clarify in requirements that this is intended to work with Mercurial 1.9.x only

* Sun Jul 03 2011 Mads Kiilerich <mads@kiilerich.com> - 2.1-1
- tortoisehg-2.1

* Thu Jun 02 2011 Mads Kiilerich <mads@kiilerich.com> - 2.0.5-1
- tortoisehg-2.0.5

* Mon May 02 2011 Mads Kiilerich <mads@kiilerich.com> - 2.0.4-1
- tortoisehg-2.0.4

* Sat Apr 02 2011 Mads Kiilerich <mads@kiilerich.com> - 2.0.3-1
- tortoisehg-2.0.3

* Thu Mar 10 2011 Mads Kiilerich <mads@kiilerich.com> - 2.0.2-1
- tortoisehg-2.0.2

* Thu Mar 10 2011 Mads Kiilerich <mads@kiilerich.com> - 2.0.1-1
- tortoisehg-2.0.1
- require Mercurial 1.8 or later

* Thu Mar 03 2011 Mads Kiilerich <mads@kiilerich.com> - 2.0-1
- tortoisehg-2.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Mads Kiilerich <mads@kiilerich.com> - 1.9.2.4-1
- tortoisehg-1.9.2+4-cff31955a6fa
- preparing for the qt based TortoiseHg 2.0 in Fedora 15

* Thu Feb 03 2011 Mads Kiilerich <mads@kiilerich.com> - 1.1.9.1-1
- tortoisehg-1.1.9.1

* Wed Feb 02 2011 Mads Kiilerich <mads@kiilerich.com> - 1.1.9-1
- tortoisehg-1.1.9

* Sun Jan 02 2011 Mads Kiilerich <mads@kiilerich.com> - 1.1.8-1
- tortoisehg-1.1.8

* Thu Dec 02 2010 Mads Kiilerich <mads@kiilerich.com> - 1.1.7-1
- tortoisehg-1.1.7

* Tue Nov 16 2010 Mads Kiilerich <mads@kiilerich.com> - 1.1.6.1-1
- tortoisehg-1.1.6.1

* Tue Nov 16 2010 Mads Kiilerich <mads@kiilerich.com> - 1.1.6-1
- tortoisehg-1.1.6

* Sun Nov 07 2010 Mads Kiilerich <mads@kiilerich.com> - 1.1.5-1
- tortoisehg-1.1.5

* Fri Aug 27 2010 Mads Kiilerich <mads@kiilerich.com> - 1.1.3-1
- tortoisehg-1.1.3

* Sun Aug  8 2010 Mads Kiilerich <mads@kiilerich.com> - 1.1.2-1
- tortoisehg-1.1.2

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jul 13 2010 Mads Kiilerich <mads@kiilerich.com> - 1.1.1-1
- tortoisehg-1.1.1 with minor bugfixes
- requires mercurial-1.6

* Fri Jul 02 2010 Mads Kiilerich <mads@kiilerich.com> - 1.1-1
- tortoisehg-1.1
- Still requires Mercurial 1.5 but also works with 1.6

* Wed Jun  2 2010 Mads Kiilerich <mads@kiilerich.com> - 1.0.4-1
- New upstream bugfix release 1.0.4

* Sun May 16 2010 Mads Kiilerich <mads@kiilerich.com> - 1.0.3-1
- New upstream bugfix release 1.0.3
- Drop unused dependency gnome-python2-gtksourceview

* Fri Apr  2 2010 Mads Kiilerich <mads@kiilerich.com> - 1.0.1-1
- New upstream bugfix release 1.0.1

* Sat Mar  6 2010 Mads Kiilerich <mads@kiilerich.com> - 1.0-1
- New upstream release 1.0

* Tue Feb  2 2010 Mads Kiilerich <mads@kiilerich.com> - 0.9.3-1
- New upstream minor release 0.9.3

* Sat Jan  2 2010 Mads Kiilerich <mads@kiilerich.com> - 0.9.2-1
- New upstream bugfix release 0.9.2

* Thu Dec  3 2009 Mads Kiilerich <mads@kiilerich.com> - 0.9.1.1-1
- tortoisehg-0.9.1.1 - a brown paperbag release

* Thu Dec  3 2009 Mads Kiilerich <mads@kiilerich.com> - 0.9.1-1
- tortoisehg-0.9.1

* Wed Nov 18 2009 Mads Kiilerich <mads@kiilerich.com> - 0.9-1
- Update to tortoisehg-0.9

* Mon Nov 16 2009 Mads Kiilerich <mads@kiilerich.com> - 0.9-0.2.hg2525801b8b8d
- New upstream snapshot, pretty close to 0.9
- First koji upload

* Tue Oct 20 2009 Mads Kiilerich <mads@kiilerich.com> - 0.9-0.1.hgdc0d0231f39a
- Address review comments from Mamoru Tasaka
- Rebase to new non-forking upstream version from unreleased stable branch

* Fri Oct 16 2009 Mads Kiilerich <mads@kiilerich.com> 0.9-0.0.hg7d91c4a48d37
- Rebase to snapshot of upstream and adopt new package structure

* Fri Jul 24 2009 Mads Kiilerich <mads@kiilerich.com> 0.8.1-1
- New upstream release where minor fixes has been applied
- Remove workarounds no longer needed

* Mon Jul 20 2009 Mads Kiilerich <mads@kiilerich.com> 0.8-4.6da01818c9ea
- Rebase to snapshot of upstream with
  - Clarified that license is GPLv2
  - .mo files build with gettext
  - Local copy of python-iniparse replaced with dependency

* Mon Jul 6 2009 Mads Kiilerich <mads@kiilerich.com> 0.8-3
- Initial package of tortoisehg 0.8
