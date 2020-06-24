%global	timestamp	20190902
%global	svnversion	275
Name:           impressive
Version:        0.13.0
Release:        0.3.%{timestamp}svn%{svnversion}%{?dist}
Summary:        A program that displays presentation slides

License:        GPLv2
URL:            http://impressive.sourceforge.net/
#Source0:        http://downloads.sourceforge.net/%{name}/Impressive-%{version}.tar.gz
# svn export -r %{svnversion} http://svn.emphy.de/impressive/branches/python3/impressive Impressive-%{version}
# make -C Impressive-%{version} release
# mv Impressive-%{version}_releases/Impressive-%{version}-WIP.tar.gz Impressive-%{version}-WIP-%{timestamp}svn%{svnversion}
Source0:        %{name}/Impressive-%{version}-WIP-%{timestamp}svn%{svnversion}.tar.gz
# Wrapper script for making sure hardware acceleration is available
Source1:        %{name}.sh

BuildArch:      noarch
BuildRequires:  python3-devel
# The following requires are not picked up by rpm:
# - imported modules (required):
Requires:       python3-imaging
Requires:       python3-pygame
Requires:       opengl-games-utils
# - external tools for displaying and parsing pdf (required):
Requires:       mupdf
# - external tool for acting on links (strongly recommended):
Requires:       xdg-utils
# - font for on screen display (recommended):
Requires:       dejavu-sans-fonts


%description
Impressive is a program that displays presentation slides. But unlike 
OpenOffice.org Impress or other similar applications, it does so with 
style. 

Smooth alpha-blended slide transitions are provided for the sake 
of eye candy, but in addition to this, Impressive offers some unique tools 
that are really useful for presentations.


%prep
%autosetup -n Impressive-%{version}-WIP -p1
sed -ie '1s#/usr/bin/env python#/usr/bin/python3#' impressive.py

%build
sed -e "s|@PYTHON_SITELIB@|%{python3_sitelib}|" %{SOURCE1} > impressive.sh
# This package doesn't build anything, just copy files under build root.


%install
rm -rf %{buildroot}
install -D -p -m 755 impressive.py %{buildroot}%{python3_sitelib}/impressive.py
install -D -p -m 644 impressive.1 %{buildroot}%{_mandir}/man1/impressive.1
install -D -p -m 755 impressive.sh %{buildroot}%{_bindir}/impressive



%files
%doc changelog.txt demo.pdf impressive.html license.txt
%{_bindir}/impressive
%{python3_sitelib}/impressive.py
%{python3_sitelib}/__pycache__/*
%{_mandir}/man1/impressive.1*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-0.3.20190902svn275
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-0.2.20190902svn275
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Michael J Gruber <mjg@fedoraproject.org> - 0.13.0-0.1.20190902svn275
- build from upstream python3 branch
- previous py3k patches have been upstreamed

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-12
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Michael J Gruber <mjg@fedoraproject.org> - 0.12.0-11
- patch version v0.11.1-74-gc504a64

* Sun Aug 18 2019 Michael J Gruber <mjg@fedoraproject.org> - 0.12.0-10
- port current svn version to python3 (coordinated with upstream, release pending)
- patch version v0.11.1-74-g0223cd9
- fixes bug 1731634

* Fri Jul 26 2019 Michael J Gruber <mjg@fedoraproject.org> - 0.12.0-9
- remove obsolete comment

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 22 2018 Michael J Gruber <mjg@fedoraproject.org> - 0.12.0-6
- rebuild for python2-pygame dependency update

* Fri Jul 13 2018 Michael J Gruber <mjg@fedoraproject.org> - 0.12.0-5
- adjust to py2 packaging guidelines

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.12.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Feb 06 2018 Michael J Gruber <mjg@fedoraproject.org> - 0.12.0-2
- remove obsolete dependency

* Tue Feb 06 2018 Michael J Gruber <mjg@fedoraproject.org> - 0.12.0-1
- upstream bugfix and feature release

* Mon Feb 05 2018 Michael J Gruber <mjg@fedoraproject.org> - 0.11.3-1
- upstream bugfix release

* Sat Jan 06 2018 Michael J Gruber <mjg@fedoraproject.org> - 0.11.2-4
- use correct shebang

* Thu Jan 04 2018 Michael J Gruber <mjg@fedoraproject.org> - 0.11.2-3
- depend on Py2 packages explicitely

* Tue Dec 26 2017 Michael J Gruber <mjg@fedoraproject.org> - 0.11.2-2
- follow upstream re-tagging

* Tue Dec 19 2017 Michael J Gruber <mjg@fedoraproject.org> - 0.11.2-1
- sync with upstream

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 21 2015 Michael J Gruber <mjg@fedoraproject.org> - 0.11.1-2
- adjust to current mudraw option syntax
- use mutool for info parsing

* Sat Nov 21 2015 Michael J Gruber <mjg@fedoraproject.org> - 0.11.1-1
- sync with upstream
- fix changelog typos

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 11 2014 Michael J Gruber <mjg@fedoraproject.org> - 0.10.4-3
- temporarily remove R pdftk

* Thu Jan 02 2014 Michael J Gruber <mjg@fedoraproject.org> - 0.10.4-2
- upate requires as recommended by upstream

* Thu Jan 02 2014 Michael J Gruber <mjg@fedoraproject.org> - 0.10.4-1
- sync with upstream
- drop pillow compatibility patch (upstreamed)
- drop backported PDF parser fix (upstreamed)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Michael J Gruber <mjg@fedoraproject.org> - 0.10.3-10
- pillow compatibility (bug 895270, patch by Toshio Ernie Kuratomi)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Michael J Gruber <mjg@fedoraproject.org> - 0.10.3-7
- backport PDF parser fix

* Mon May 02 2011 Michael J Gruber <mjg@fedoraproject.org> - 0.10.3-6
- EPEL has no pdftk (recommended but optional requirement)

* Fri Mar 11 2011 Michael J Gruber <mjg@fedoraproject.org> - 0.10.3-5
- Clarify explicit requires.
- Add pdftk as requirement.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 05 2010 Michael J Gruber <mjg@fedoraproject.org> - 0.10.3-3
- spec file cleanup.

* Sun Dec 05 2010 Michael J Gruber <mjg@fedoraproject.org> - 0.10.3-2
- Make summary less flashy.
- Install main program in sitelib.
- BR python-devel.

* Fri Dec 03 2010 Michael J Gruber <mjg@fedoraproject.org> - 0.10.3-1
- Sync with upstream.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Allisson Azevedo <allisson@gmail.com> 0.10.2-6
- Added provides keyjnote.

* Mon Feb 16 2009 Allisson Azevedo <allisson@gmail.com> 0.10.2-5
- Obsolete keyjnote.

* Mon Feb 16 2009 Allisson Azevedo <allisson@gmail.com> 0.10.2-4
- Fix requires for dejavu fonts.

* Thu Feb 12 2009 Allisson Azevedo <allisson@gmail.com> 0.10.2-3
- Added OpenGL wrapper.
- Fix requires for dejavu fonts.

* Thu Feb 12 2009 Allisson Azevedo <allisson@gmail.com> 0.10.2-2
- Changed license.
- Added dejavu-fonts to requires.
- Added build section.

* Mon Feb  9 2009 Allisson Azevedo <allisson@gmail.com> 0.10.2-1
- Initial RPM release
