%global modname 2.4.6

Summary: Open source Church presentation and lyrics projection application
Name: OpenLP
Version: 2.4.6
Release: 12%{?dist}
Source0: https://get.openlp.org/%{version}/OpenLP-%{version}.tar.gz
License: GPLv2
BuildArch: noarch

URL: http://openlp.org/

BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-qt5
Requires:       python3-qt5-webkit
Requires:       python3-beautifulsoup4
Requires:       python3-chardet
Requires:       python3-lxml
Requires:       python3-sqlalchemy
Requires:       python3-enchant
Requires:       python3-mako
Requires:       python3-openoffice
Requires:       python3-alembic
Requires:       hicolor-icon-theme
Requires:       libreoffice-graphicfilter
Requires:       libreoffice-impress
Requires:       mupdf

%description
OpenLP is a church presentation software, for lyrics projection software,
used to display slides of Songs, Bible verses, videos, images, and
presentations via LibreOffice using a computer and projector.

%prep
%setup -q

%build
%{__python3} setup.py build

%install
rm -rf %{buildroot}
%{__python3} setup.py install --skip-build -O1 --root %{buildroot}

install -m644 -p -D resources/images/openlp-logo-16x16.png \
   %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/openlp.png
install -m644 -p -D resources/images/openlp-logo-32x32.png \
   %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/openlp.png
install -m644 -p -D resources/images/openlp-logo-48x48.png \
   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/openlp.png
install -m644 -p -D resources/images/openlp-logo.svg \
   %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/openlp.svg

desktop-file-install \
  --dir %{buildroot}/%{_datadir}/applications \
  resources/openlp.desktop

desktop-file-validate %{buildroot}/%{_datadir}/applications/openlp.desktop

mv %{buildroot}%{_bindir}/openlp.py %{buildroot}%{_bindir}/openlp

mkdir -p %{buildroot}%{_datadir}/openlp/i18n/
mv resources/i18n/*.qm %{buildroot}%{_datadir}/openlp/i18n
mkdir -p %{buildroot}%{_datadir}/mime/packages
cp -p resources/openlp.xml %{buildroot}%{_datadir}/mime/packages

%files
%doc copyright.txt LICENSE
%{_bindir}/openlp
%{_datadir}/mime/packages/openlp.xml
%{_datadir}/applications/openlp.desktop
%{_datadir}/icons/hicolor/*/apps/openlp.*
%{_datadir}/openlp
%{python3_sitelib}/openlp/
%{python3_sitelib}/OpenLP-%{modname}*.egg-info


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.6-11
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.6-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.6-8
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.6-4
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 31 2017 Tim Bentley <Tim.Bentley@openlp.org> - 2.4.6-1
- 2.4.6 Release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Tim Bentley <Tim.Bentley@openlp.org> - 2.4.5-1
- 2.4.5 Release

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.4.4-3
- Rebuild for Python 3.6

* Sat Nov 26 2016 Tim Bentley Tim.Bentley@openlp.org - 2.4.4-2
- 2.4.4 Release

* Sat Nov 26 2016 Tim Bentley Tim.Bentley@openlp.org - 2.4.4-1 
- 2.4.4 Release

* Sun Sep 25 2016 Tim Bentley Tim.Bentley@openlp.org - 2.4.3 
- 2.4.3 Release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages


* Sat Jun 25 2016 Tim Bentley Tim.Bentley@openlp.org - 2.4.2-1
- 2.4.2 Release

* Sat Apr 30 2016 Tim Bentley Tim.Bentley@openlp.org - 2.4.1-1
- 2.4.1 Release

* Wed Mar 02 2016 Rex Dieter <rdieter@fedoraproject.org> 2.4-2
- Requires: +python3-qt5-webkit, -phonon

* Sat Feb 13 2016 Tim Bentley Tim.Bentley@openlp.org - 2.4-1
- 2.4 Release

* Sun Feb 07 2016 Tim Bentley Tim.Bentley@openlp.org - 2.3.3-1
- 2.3.3 RC Releaase 

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 10 2016 Tim Bentley Tim.Bentley@openlp.org - 2.3.2-1
- 2.3.2 Beta Release

* Mon Dec 28 2015 Tim Bentley Tim.Bentley@openlp.org - 2.3.1-1
- 2.3.1 Alpha Release

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-1
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Oct 30 2015 Tim Bentley Tim.Bentley@openlp.org - 2.2.1-0
- 2.2.1 Update release

* Sat Oct 17 2015 Tim Bentley Tim.Bentley@openlp.org - 2.2-0
- 2.2 Full Release

* Sun Aug 23 2015 Tim Bentley Tim.Bentley@openlp.org - 2.1.6-2
- 2.1.6 Test  Release 2 

* Sun Aug 23 2015 Tim Bentley Tim.Bentley@openlp.org - 2.1.6-1
- 2.1.6 Test  Release 

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Tim Bentley Tim.Bentley@openlp.org - 2.1.5-1
- 2.1.5 Test  Release 

* Sun Apr 26 2015 Tim Bentley Tim.Bentley@openlp.org - 2.1.4-1
- 2.1.4 Beta 4 Release 

* Sat Feb 21 2015 Tim Bentley Tim.Bentley@openlp.org - 2.1.3-1
- 2.1.3 Beta 3 Release 

* Sat Jan 24 2015 Tim Bentley Tim.Bentley@openlp.org - 2.1.2-1
- 2.1.2 Beta 2 Release

* Mon Nov 24 2014 Tim Bentley Tim.Bentley@openlp.org - 2.1.1-2
- Remove libreoffice-headless

* Sat Nov 1 2014 Tim Bentley Tim.Bentley@openlp.org - 2.1.1
- 2.1.1 Beta Release 

* Sat Sep 27 2014 Rex Dieter <rdieter@fedoraproject.org> 2.0.5-2
- update/optimize icon/mime scriptlets

* Fri Jun 27 2014 Tim Bentley Tim.Bentley@openlp.org - 2.0.5-1
- 2.0.5 final release

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 2 2014 Tim Bentley <timbentley@openlp.org> - 2.0.4-1
- Release 2.0.4

* Sat Sep 14 2013 Tim Bentley <timbentley@openlp.org> - 2.0.3-1
- Release 2.0.3

* Sun Aug 25 2013 Tim Bentley <timbentley@openlp.org> - 2.0.2-2
- Release 2.0.2

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 05 2013 Tim Bentley <timbentley@openlp.org> - 2.0.1-1
- Release 2.0.1

* Sat Dec 1 2012 Tim Bentley <timbentley@openlp.org> - 2.0-1
- Release 2.0

* Sat Sep 15 2012 Tim Bentley <timbentley@openlp.org> - 1.9.12-1
- Release 1.9.12

* Sat Jul 28 2012 Tim Bentley <timbentley@openlp.org> - 1.9.11-1
- Relaese 1.9.11 build

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Tim Bentley <timbentley@openlp.org> - 1.9.10-2
- Import Issues

* Sat Jun 23 2012 Tim Bentley <timbentley@openlp.org> - 1.9.10-1
- Release 1.9.10 build

* Sun Mar 25 2012 Tim Bentley <timbentley@openlp.org> - 1.9.9-1
- Release 1.9.9 build

* Fri Dec 23 2011 Tim Bentley <timbentley@openlp.org> - 1.9.8-1
- Release 1.9.8 build

* Sat Sep 24 2011 Tim Bentley <timbentley@openlp.org> - 1.9.7
- Weekly build

* Sat Jun 25 2011 Tim Bentley <timbentley@openlp.org> - 1.9.6-1
- Release build for beta 2

* Sat Jun 11 2011 Tim Bentley <timbentley@openlp.org> - 1.9.5-5
- Update Build Script

* Tue May 24 2011 Tim Bentley <timbentley@openlp.org> - 1.9.5-4
- Fix Typing error

* Mon May 23 2011 Tim Bentley <timbentley@openlp.org> - 1.9.5-3
- Fix dependancy

* Mon May 23 2011 Tim Bentley <timbentley@openlp.org> - 1.9.5-2
- Fix LibreOffice addition for presentations

* Fri Mar 25 2011 Tim Bentley <timbentley@openlp.org> - 1.9.5-1
- Beta 1 release build

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 8 2011 Tim Bentley <timbentley@openlp.org> - 1.9.4-1
- Alpha 4 release build

* Sat Sep 25 2010 Tim Bentley <timbentley@openlp.org> - 1.9.3-1
- Alpha 3 release build

* Mon Aug 30 2010 Tim Bentley <timbentley@openlp.org> - 1.9.2.1-4
- Update to build 1000

* Sat Aug 28 2010 Tim Bentley <timbentley@openlp.org> - 1.9.2.1-3
- Update to 996 and test build on git

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.9.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jun 26 2010 Tim Bentley <timbentley@openlp.org> 1.9.2.1
- Fix bug with build versions

* Sat Jun 26 2010 Tim Bentley <timbentley@openlp.org> 1.9.2
- New Release - Alpha 2 Release

* Sun Mar 28 2010 Tim Bentley <timbentley@openlp.org> 1.9.1.1
- Initial build version - Alpha 1 Release
