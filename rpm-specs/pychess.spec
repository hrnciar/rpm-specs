%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

Name:           pychess
Version:        0.12.4
Release:        19%{?dist}
Summary:        Chess game for GNOME

License:        GPLv3
URL:            http://pychess.org
Source0:        https://github.com/pychess/pychess/releases/download/%{version}/%{name}-%{version}.tar.gz
# install data files to gtksourceview2 datadir, since that's
# what Fedora ships
Patch0:         pygtksourceview-2.patch

   
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils, gettext

# gnome-settings-daemon
Requires:       python3-gobject
Requires:       librsvg2
Requires:       gnome-icon-theme
Requires:       python3-gstreamer1
# for editing .pgn files
Requires:       gtksourceview3

%description
PyChess is a GTK+ chess game for Linux. It is designed to at the same time
be easy to use, beautiful to look at, and provide advanced functions for
advanced players.


%prep
%setup -q -n %{name}-%{version}
%patch0
find -type f -exec chmod -x {} ';'

# strip shebang from files not meant to be run
cd lib/pychess
sed -i '1d' System/command.py System/which.py


%build
%py3_build


%install
%py3_install
# Remove Debian specific menu stuff
rm -r $RPM_BUILD_ROOT%{_datadir}/menu

desktop-file-install --delete-original                  \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications   \
        --remove-category Application \
        $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 William Moreno <williamjmorenor@gmail.com> -->
<!--
BugReportURL: https://code.google.com/p/pychess/issues/detail?id=915
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">pychess.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Chess client written entirely in Python</summary>
  <description>
    <p>
    Pychess is a Chess client can start a game using its own engine
    or any other engine installed on the computer is completely written
    in Python from the User Interface to the game engine and can connect
    to play games online with other people.
    </p>
  </description>
  <url type="homepage">http://pychess.org</url>
  <screenshots>
    <screenshot type="default">http://pychess.org/images/feature-1.png</screenshot>
  </screenshots>
</application>
EOF

%find_lang %{name}

%files -f %{name}.lang
%doc README.md AUTHORS ARTISTS DOCUMENTERS TRANSLATORS
%license LICENSE
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%{_bindir}/%{name}
%{_datadir}/pychess
%{_datadir}/gtksourceview-2.0/language-specs/pgn.lang
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/pixmaps/*
%{_mandir}/man?/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.4-19
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.4-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.4-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.4-12
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.4-10
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Iryna Shcherbina <ishcherb@redhat.com> - 0.12.4-7
- Switch to Python 3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.4-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 29 2016 Bruno Wolff III <bruno@wolff.to> - 0.12.4-5
- Without python-gobject, pychess doesn't work properly

* Mon Jun 27 2016 Bruno Wolff III <bruno@wolff.to> - 0.12.4-4
- For now also require gtksourceview3, since it at least checks for it

* Sun Jun 26 2016 Bruno Wolff III <bruno@wolff.to> - 0.12.4-3
- No we should use gtksourceview2, because that's what pygtksourceview does

* Sun Jun 26 2016 Bruno Wolff III <bruno@wolff.to> - 0.12.4-2
- We need gtksourceview3

* Sun Jun 26 2016 Bruno Wolff III <bruno@wolff.to> - 0.12.4-1
- Update to 0.12.4
- Bugfix release. See: https://github.com/pychess/pychess/releases/tag/0.12.4
- Patch is no longer needed.

* Thu Mar 03 2016 Sérgio Basto <sergio@serjux.com> - 0.12.3-1
- Update to pychess-0.12.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.10.1-7
- Add an AppData file for the software center

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Bruno Wolff III <bruno@wolff.to> 0.10.1-4
- Remove vendor prefix from desktop file

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 09 2012 Bruno Wolff III <bruno@wolff.to> 0.10.1-1
- Upstream 0.10.1 release
- Should only be bug fixes since beta2
- At some point the license changed to GPL3

* Sat Oct 29 2011 Bruno Wolff III <bruno@wolff.to> 0.10.1-0.1.beta2
- Pick up a few more bug fixes with the beta2 prerelease.

* Sat Sep 03 2011 Bruno Wolff III <bruno@wolff.to> - 0.10.rev2004-1
- Pickup lots of post 0.10 fixes (hopefully that fix reported bugs)

* Wed May 18 2011 Christopher Aillon <caillon@redhat.com> - 0.10-1
- Update to 0.10

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-0.9.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Michel Salim <salimma@fedoraproject.org> - 0.10-0.8.rc1
- Update to 0.10rc1
- Install PGN language spec in correct location
- Properly update icon cache

* Sun Aug 15 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10-0.7.20100815hg
- update to new version (fixes bug #598062)

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.10-0.6.20100511hg
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed May 12 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10-0.5.20100511hg
- new hg snapshot to fix #591165

* Tue May  4 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10-0.4.20100504hg
- new hg snapshot to get it working again (#577570)

* Sun Feb 14 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10-0.3.20100214svn
- update svnsnapshot to fix some fedora bugs
  (562895,565225,563330)

* Fri Feb  5 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10-0.2.20100203svn
- add R: gnome-python2-rsvg (#551475)

* Wed Feb  3 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.10-0.1.20100203svn
- update to svn snapshot (the rest is currently non working)
- %%global and not %%define
- delete the patches, all upstream or solved upstream differently
- remove R python-sqlite2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.8.2-2
- Rebuild for Python 2.6

* Tue Aug 26 2008 Michel Salim <salimma@fedoraproject.org> - 0.8.2-1
- Update to 0.8.2

* Mon Mar 17 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 0.8-2
- Bump release

* Thu Feb 21 2008 Sindre Pedersen Bjordal <foolish@guezz.net> - 0.8-1
- Final 0.8 release

* Mon Dec  3 2007 Michel Salim <michel.sylvan@gmail.com> - 0.8-0.1.beta2
- Update to 0.8beta2

* Sun Nov 11 2007 Michel Salim <michel.sylvan@gmail.com> - 0.8-0.1.beta1
- Update to 0.8beta1

* Thu Apr 19 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.6.0-1
- Update to 0.6.0 final

* Sun Jan 14 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.6.0-0.3.beta5
- Update description

* Sun Jan 14 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.6.0-0.2.beta5
- Fix permissions
- Fix quiet %%setup

* Sun Jan 14 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.6.0-0.1.beta5
- Initial build
