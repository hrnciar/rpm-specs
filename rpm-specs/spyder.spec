
%global _description %{expand:
Spyder is a powerful scientific environment written in Python, for Python, and 
designed by and for scientists, engineers and data analysts. It features a 
unique combination of the advanced editing, analysis, debugging and profiling 
functionality of a comprehensive development tool with the data exploration, 
interactive execution, deep inspection and beautiful visualization capabilities 
of an analysis package. Furthermore, Spyder offers built-in integration with 
many popular scientific libraries, including NumPy, SciPy, Pandas, IPython, 
QtConsole, Matplotlib, SymPy, and more, and can be extended further with 
full plugin support.
}

Name:		spyder
Version:	4.1.3
Release:	3%{?dist}
Summary:	Scientific Python Development Environment

Source0:	https://github.com/%{name}-ide/%{name}/archive/v%{version}.tar.gz

License:	MIT
URL:		https://www.spyder-ide.org/
BuildArch:	noarch


%description
%_description

%package -n python3-%{name}
Summary:	%{summary}

%{?python_provide:%python_provide python3-%{name}}

BuildRequires:	python3-devel
BuildRequires:	python3-sphinx
BuildRequires:	python3-setuptools
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib

Requires:	hicolor-icon-theme
Requires:	python3-atomicwrites
Requires:	python3-chardet
Requires:	python3-cloudpickle
Requires:	python3-diff-match-patch
Requires:	python3-intervaltree
Requires:	python3-ipython
Requires:	python3-jedi
Requires:	python3-nbconvert
Requires:	python3-numpydoc
Requires:	python3-paramiko
Requires:	python3-parso
Requires:	python3-pexpect
Requires:	python3-pickleshare
Requires:	python3-psutil
Requires:	python3-pygments
Requires:	python3-pylint
Requires:	python3-language-server
Requires:	python3-pyxdg
Requires:	python3-qdarkstyle
Requires:	python3-qt5
Requires:	python3-qt5-webkit
Requires:	python3-QtAwesome
Requires:	python3-qtconsole
Requires:	python3-QtPy
Requires:	python3-rtree
Requires:	python3-sphinx
Requires:	python3-spyder-kernels
Requires:	python3-watchdog
Requires:	python3-zmq

%description -n python3-%{name}
%_description

%prep
%setup -q -n %{name}-%{version}
sed -i 's/\xe2\x80\x8b//g' scripts/spyder3.appdata.xml

rm -rf PKG-INFO

# Remove DOS line endings
for file in `find -name "*.rst" -o -name "*.py" -o -name "*.css"`; do
	sed "s|\r||g" $file > $file.new && \
	touch -r $file $file.new && \
	mv $file.new $file
done


%build
%py3_build


%install
mkdir -p %{buildroot}%{_datadir}/appdata
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

%py3_install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications scripts/%{name}3.desktop

# install appdata file
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}3.appdata.xml

# cleanup
rm -rf %{buildroot}%{python3_sitelib}/spyderlib/doc/{.buildinfo,.doctrees}
rm -rf %{buildroot}%{python_sitelib}/spyderlib/doc/{.buildinfo,.doctrees}
rm -rf %{buildroot}%{_bindir}/spyder_win_post_install.py

%ldconfig_scriptlets

%files -n python3-%{name}
%{python3_sitelib}/spyder-*.egg-info
%{python3_sitelib}/spyder/
%{_bindir}/%{name}3
%{_metainfodir}/%{name}3.appdata.xml
%{_datadir}/applications/%{name}3.desktop
%{_datadir}/icons/spyder3.png


%changelog
* Tue Jun 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.1.3-3
- Add BR:python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.1.3-2
- Rebuilt for Python 3.9

* Sat May 09 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.1.3-1
- Update to 4.1.3

* Thu May 07 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.1.2-1
- Update to 4.1.2
- Minor spec changes

* Sat Feb 29 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.3.6-5
- Drop pathlib2 as requires

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.3.6-3
- Drop pep8 as requires

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.6-2
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.3.6-1
- Update to 3.3.6

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.3.4-1
- Update to 3.3.4

* Sun Feb 10 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.3.3-1
- Update to 3.3.3

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 02 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.3.2-1
- Update to 3.3.2

* Sun Oct 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.3.1-6
- Fix desktop file installation

* Sun Oct 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.3.1-5
- Drop python2 version

* Mon Oct 15 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.3.1-4
- Drop direct requires on prompt_toolkit (should be pulled through iPython)

* Thu Aug 23 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.3.1-3
- Fix py2 requires

* Sun Aug 12 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.3.1-2
- Fix description
- Drop py3 conditional

* Sat Aug 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.3.1-1
- Update to 3.3.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.3.0-2
- Add requires on python-spyder-kernels

* Sat Jul 07 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.3.0-1
- Update to 3.3.0
- Fix appdata file install location

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.2.8-3
- Rebuilt for Python 3.7

* Fri Mar 23 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.2.8-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Mar 15 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.2.8-1
- Update to 3.2.8

* Sat Mar 03 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.2.7-4
- Add conditional for py2-chardet

* Mon Feb 26 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.2.7-3
- Update to 3.2.7
- use ldconfig-scriptlets
- fix icon installation
- bump release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Mukundan Ragavan <nonamedotc@gmail.com> - 3.2.6-3
- bump release and rebuild

* Thu Jan 18 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.2.6-2
- change requires from py* to py2* subpackages

* Tue Jan 09 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.2.6-1
- Update to 3.2.6

* Thu Jan 04 2018 Lumír Balhar <lbalhar@redhat.com> - 3.2.5-3
- Fix directory ownership

* Wed Dec 27 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.2.5-2
- Add cloudpickle as dependency

* Wed Dec 27 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.2.5-1
- Update to 3.2.5 (bugfix update)

* Sun Nov 12 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.2.4-2
- Add requires for python3-rope

* Fri Oct 20 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.2.4-1
- Update to 3.2.4

* Mon Sep 11 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.2.3-1
- Update to 3.2.3

* Thu Sep 07 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.2.2-1
- Update to 3.2.2

* Sat Sep 02 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.2.1-2
- Fix requires (python- vs python2-)
- Add pycodestyle as requires

* Mon Aug 14 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.2.1-1
- Update to 3.2.1
- Drop the appdata patch in favor of sed fix

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Tomas Hozza <thozza@redhat.com> - 3.1.4-3
- Use RPM macros for building and installing Python2 and Python3 versions of the package
- Provide upgrade path from spyder package (#1469003)

* Thu May 04 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.1.4-2
- Fix requires for python3 subpackage

* Mon Apr 24 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.1.4-1
- Update to 3.1.4
- Install upstream desktop files
- Install appdata file

* Thu Mar 16 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.1.3-2
- Add numpydoc as requires

* Mon Feb 20 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.1.3-1
- Update to 3.1.3

* Thu Jan 26 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.1.2-1
- Update to 3.1.2

* Sun Jan 22 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1

* Wed Jan 18 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.1.0-2
- Update requires completely

* Wed Jan 18 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0

* Tue Jan 03 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.0.2-2
- Add dependencies

* Thu Dec 29 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2

* Tue Sep 20 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.0.0-3.b7
- Update to beta 7

* Sat Sep 03 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.0.0-3.b6
- Update to beta 6

* Thu Aug 11 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.0.0-2.b4
- Fix requires

* Wed Aug 10 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.0.0-1.b4
- Update to 3.0.0 beta 4

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.9-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr 26 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.9-1
- Update to v2.3.9

* Wed Mar 02 2016 Rex Dieter <rdieter@fedoraproject.org> 2.3.8-3
- (unconditionally) Requires: PyQt4-webkit

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.8-1
- Update to 2.3.8

* Thu Nov 12 2015 Kalev Lember <klember@redhat.com> - 2.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Nov 04 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.7-4
- Fix spyder3 desktop file

* Tue Nov 03 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.7-3
- Added EL conditionals for requires

* Mon Nov 02 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.7-2
- Build python3 subpackage

* Tue Oct 06 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.7-1
- Updated to v2.3.7
- Updated source and package URL
- Removed old version patch

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 07 2014 Radek Novacek <rnovacek@redhat.com> 2.2.4-4
- Remove Requires: qtwebkit as its already pulled by PyQt4

* Wed Jul 30 2014 Radek Novacek <rnovacek@redhat.com> 2.2.4-3
- Add Requires: qtwebkit (#1121360)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 25 2013 Tomas Hozza <thozza@redhat.com> 2.2.4-1
- new upstream version 2.2.4 (#1010935)
- Spyder failed to start and ended with EOFError (#1010568)

* Fri Aug 16 2013 Radek Novacek <rnovacek@redhat.com> 2.2.2-1
- Update to 2.2.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 10 2013 Radek Novacek <rnovacek@redhat.com> 2.2.1-1
- Update to 2.2.1

* Mon May 20 2013 Radek Novacek <rnovacek@redhat.com> 2.2.0-1
- Update to 2.2.0
- Spec cleanup
- Add spyder.png pixmap
- Resolves: #958040

* Mon Mar 11 2013 Radek Novacek <rnovacek@redhat.com> 2.1.13-3
- Fix checking PyQt4 version
- Resolves: #919921

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Radek Novacek <rnovacek@redhat.com> 2.1.13-1
- Update to 2.1.13

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 06 2012 Radek Novacek <rnovacek@redhat.com> 2.1.6-3
- Require pyflakes >= 0.5.0
- Resolves: #786836

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan 02 2012 Radek Novacek <rnovacek@redhat.com> 2.1.6-1
- Update to 2.1.6
- Fix crash with ipython 0.12dev
- Resolves: #770161

* Fri Nov 25 2011 Radek Novacek <rnovacek@redhat.com> 2.1.2-1
- Update to 2.1.2

* Mon Nov 07 2011 Radek Novacek <rnovacek@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Thu Jul 14 2011 Radek Novacek <rnovacek@redhat.com> - 2.0.12-1
- Update to 2.0.12

* Sun May 22 2011 Chen Lei <supercyper@163.com> - 2.0.11-1
- Update to 2.0.11

* Sun Dec 19 2010 Chen Lei <supercyper@163.com> - 2.0.5-1
- Update to 2.0.5

* Wed Dec 08 2010 Chen Lei <supercyper@163.com> - 2.0.3-1
- Update to 2.0.3

* Wed Dec 01 2010 Chen Lei <supercyper@163.com> - 2.0.1-1
- Update to 2.0.1

* Tue Nov 30 2010 Chen Lei <supercyper@163.com> - 2.0.0-1
- Update to 2.0.0 final

* Wed Oct 13 2010 Chen Lei <supercyper@163.com> - 2.0.0-0.2.beta5
- Update to 2.0.0beta5

* Wed Sep 15 2010 Chen Lei <supercyper@163.com> - 2.0.0-0.1.beta3
- Initial rpm build
