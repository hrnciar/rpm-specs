%global pluginversion 1.0.0
%global owner highperformancecoder

Name:           scidavis
Version:        2.3.0
Release:        1%{?dist}
Summary:        Application for Scientific Data Analysis and Visualization

License:        GPLv3+
URL:            http://scidavis.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Main upstream development repository (master, snapshots, releases not yet in sf)
#Source0:        https://github.com/%%{owner}/%%{name}/archive/master/%%{name}-master.tar.gz
#Source0:        https://github.com/%%{owner}/%%{name}/archive/%%{version}/%%{name}-%%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  desktop-file-utils
BuildRequires:  gsl-devel
BuildRequires:  liborigin-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  muParser-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qwt5-qt5-devel
BuildRequires:  qwtplot3d-qt5-devel
BuildRequires:  python3-sip-devel
BuildRequires:  python3-pyqt5-sip
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-linguist
BuildRequires:  zlib-devel
BuildRequires:  libappstream-glib
# required for the tests, enable when building locally
#BuildRequires:  xorg-x11-server-Xvfb
#BuildRequires:  unittest-cpp-devel
#BuildRequires:  boost-devel

Requires:       python3-qt5
Requires:       hicolor-icon-theme
Requires:       kde-filesystem

Recommends:     python3-%{name}


%description
SciDAVis is a free interactive application aimed at data analysis and
publication-quality plotting. It combines a shallow learning curve and
an intuitive, easy-to-use graphical user interface with powerful
features such as scriptability and extensibility.



%package -n python3-%{name}
BuildRequires:  python3-devel
BuildRequires:  python3-qt5-devel

Summary:        Python 3 bindings for SciDAVis
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}
Obsoletes:      python2-%{name} < 1.23-5


%description -n python3-%{name}
This module provides SciDAVis bindings to the Python3 programming language.



%prep
%setup -q -n %{name}-%{version}
# Development builds
#%%setup -q -n %%{name}-master
# Set the correct python paths
sed -i 's+pythonconfig.path = "$$INSTALLBASE/../etc"+pythonconfig.path = "$$INSTALLBASE/..%{python3_sitearch}/scidavis"+g' config.pri
sed -i 's+pythonutils.path = "$$INSTALLBASE/share/scidavis"+pythonutils.path = "$$INSTALLBASE/..%{python3_sitearch}/scidavis"+g' config.pri


%build
# Set python version to 3
export PYTHON=python3
%if 0%{?__isa_bits} == 64
# Enable testsuite when building locally
#%%qmake_qt4 PRESET=linux_package libsuff="64" CONFIG+=aegis CONFIG+=python
%qmake_qt5 PRESET=linux_package libsuff="64" CONFIG+="python liborigin noassistant"
%else
# Enable testsuite when building locally
#%%qmake_qt4 PRESET=linux_package CONFIG+=aegis CONFIG+=python
%qmake_qt5 PRESET=linux_package CONFIG+="python liborigin noassistant"
%endif
%make_build


%install
make INSTALL_ROOT="%{buildroot}" install
install -pm 644 ChangeLog.md %{buildroot}%{_docdir}/%{name}/

mkdir -p %{buildroot}%{_datadir}/{%{name}/translations,applications,mime/packages,appdata}
cp -p %{name}/translations/*.qm %{buildroot}%{_datadir}/%{name}/translations/

# KDE3 remnant - upstream is aware
rm -rf %{buildroot}%{_datadir}/mimelnk/

# gpl.txt is copied over by the license macro
rm -f %{buildroot}%{_docdir}/%{name}/gpl.txt

# Plugins are unversioned .so files
cd %{buildroot}%{_libdir}/%{name}/plugins
for plugin in `ls *.so`
do
    mv ${plugin}.%{pluginversion} ${plugin}
    rm -f ${plugin}.*
done


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml
# Enable testsuite when building locally
#cd test && xvfb-run -a ./unittests

%files
%license gpl.txt LICENSE license.rtf
%{_mandir}/man1/%{name}.1*
%{_docdir}/%{name}/
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/locolor/*/apps/%{name}.*


%files -n python3-%{name}
%{python3_sitearch}/%{name}/


%changelog
* Mon Jun 15 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0
- Add qwt5-qt5 and all the new BRs
- Drop Qt4 and old deps

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.26-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.26-1
- Update to 1.26

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.25.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 25 2019 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.25.1-1
- New release, fixes for sf bugs #293, #379, #383, #385 and #388

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 1.25-8
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.25-7
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.25-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 12 2019 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.25-4
- Backport fixes for sf bugs #380 and #381
- Merge all post-1.25 bugfixes as the same files are being edited

* Sun Mar 31 2019 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.25-3
- Backport fix for 3D plot colors reverting to black

* Sat Mar 16 2019 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.25-2
- Backport fix for plot colors reverting to black

* Tue Mar 05 2019 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.25-1
- Update to 1.25 (bugfixes, updated translations)

* Sat Mar 02 2019 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.24-1
- Update to 1.24

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 02 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.23.4-3
- Fix for sf#360 - patch by Miquel Garriga

* Thu Nov 22 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.23.4-2
- Build against system liborigin library

* Sun Nov 18 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.23.4-1
- Realign with upstream versioning
- Minor bugfixes
- Remove unneeded patches

* Wed Aug 01 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.23-7.20180705git0ca8811
- Fix an interface crash - patch by Miquel Garriga

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-6.20180705git0ca8811
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.23-5.20180705git0ca8811
- Switch to git snapshot 0ca8811 (multiple fixes)
- Clean up spec file and unneeded patches

* Sun Jul 01 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.23-4
- Switch to python 3.x and python3 dependencies
- Add unit testing dependencies
- Comprehensive fix for python3-related issues - patch by Miquel Garriga

* Wed Jun 27 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.23-3
- Fix font scaling bug #337 - patch by Miquel Garriga

* Thu Jun 07 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.23-2
- Fix a crash caused by Qt color picker - patch by Miquel Garriga
- Explicitly require python2 in script headers

* Mon Jun 04 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.23-1
- Update to 1.23
- Remove unneeded patches

* Sat Mar 10 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.22-6
- Restore upstream intended paste behavior

* Thu Mar 08 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.22-5
- Add patch to speed up pasting of data

* Fri Feb 16 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.22-4
- Add gcc-c++ build dependency

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.22-2
- Remove obsolete scriptlets

* Mon Oct 23 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.22-1
- New version
- Remove obsolete patches and scripts

* Mon Oct 02 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.21-6
- Update appdata.xml file

* Sat Sep 16 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.21-5
- Add code and requirements in order to run the provided tests (in local builds)
- Add kde-filesystem requirement
- Combine licenses to GPLv3+

* Thu Sep 14 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.21-4
- Fix another armv7hl issue - patches by Robert-André Mauchin and Miquel Garriga
- Patch for setting Python paths by Antonio Trande
- Backport patch for https://sourceforge.net/p/scidavis/scidavis-bugs/316/
- Enable all build options (CONFIG+=aegis)
- Include AppData file from next release
- More code cleanup

* Tue Sep 12 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.21-3
- Enable Python scripting
- Remove more redundant code

* Mon Sep 11 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.21-2
- Hold off unbundling until liborigin-3.0.0 official release
- Remove x-sciprj.desktop and /usr/share/mimelnk/application/
- Fix manpage location
- Remove redundant code from the spec file

* Sat Aug 19 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.21-1
- New version

* Tue Aug 01 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.19-2
- Enable ARM builds - patch by Miquel Garriga <gbmiquel.at.gmail.com>
- Clean up spec file

* Thu Jul 20 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.19-1
- New version

* Wed Jun 28 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.18-2.20170628git7c6e07df
- Unbundle liborigin - patch by Miquel Garriga <gbmiquel.at.gmail.com>

* Fri Jun 23 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.18-1
- new version

* Mon Jun 12 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.17-2
- Enabled bundled patched liborigin

* Mon Jun 12 2017 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.17-1
- new version

* Mon Jul 11 2016 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.D13-1
- new version

* Tue Nov 24 2015 Christian Dersch <lupinix@mailbox.org> - 1.D9-1
- new version

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.D8-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.D8-11
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.D8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.D8-9
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.D8-8
- Rebuild for boost 1.57.0

* Fri Jan 02 2015 Christian Dersch <lupinix@fedoraproject.org> - 1.D8-7
- added patch to fix http://sourceforge.net/p/scidavis/svn/1458/

* Sat Dec 20 2014 Christian Dersch <lupinix@fedoraproject.org> - 1.D8-6
- added missing find_lang macro
- adjusted condition for 32/64 bit decision

* Mon Dec 15 2014 Christian Dersch <lupinix@fedoraproject.org> - 1.D8-5
- added ExcludeArch for arm as scidavis doesn't build there

* Mon Dec 15 2014 Christian Dersch <lupinix@fedoraproject.org> - 1.D8-4
- fixed spec
- added post/postun scripts
- removed versioned .so files
- don't package compiled versions of scidavisrc.py config file

* Thu Aug  7 2014 Christian Dersch <lupinix@fedoraproject.org> - 1.D8-3
- fixed spec to be conform with guidelines

* Mon Aug  4 2014 Christian Dersch <lupinix@fedoraproject.org> - 1.D8-2
- fixed BuildRequires

* Mon Aug  4 2014 Christian Dersch <lupinix@fedoraproject.org> - 1.D8-1
- initial spec
- inspired by old scidavis spec http://pkgs.fedoraproject.org/cgit/scidavis.git/tree/scidavis.spec?h=f15
