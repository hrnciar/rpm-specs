# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

%{!?python3_sitelib: %define python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global __python %{__python3}

Name:		gaupol
Version:	1.4
Release:	9%{?dist}
Summary:	Subtitle editor

License:	GPLv3+
URL:		http://otsaloma.io/gaupol/
Source0:	https://github.com/otsaloma/gaupol/archive/%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	desktop-file-utils, gettext, doxygen, intltool
BuildRequires:	python3-setuptools
Requires:	python3-enchant, python3-chardet
Requires:	aeidon >= 1.4

%description
Editor for text-based subtitle files. It supports multiple subtitle file
formats and provides means of correcting texts and timing subtitles to match
video. The user interface is designed with attention to batch processing of
multiple documents and convenience of translating.

%package -n aeidon
Summary: Package for reading, writing and manipulating text-based subtitle files

%description -n aeidon
This is a Python package for reading, writing and manipulating
text-based subtitle files. It is separate from the gaupol package,
which provides a subtitle editor application with a GTK+ user
interface.

%prep
%setup -q

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%find_lang %{name}
desktop-file-install					\
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications		\
--add-category AudioVideoEditing			\
$RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS.md COPYING README.md NEWS.md
%{_bindir}/gaupol
%{python3_sitelib}/gaupol*
%{_datadir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*/*/apps/%{name}.*
%{_mandir}/man1/gaupol.1*

%files -n aeidon
%doc AUTHORS.md COPYING README.aeidon.md NEWS.md
%{python3_sitelib}/aeidon

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4-9
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4-2
- Rebuilt for Python 3.7

* Fri Jun 22 2018 Lucian Langa <lucilanga@gnome.eu.org> - 1.4-1
- metainfo files installed into 'metainfo', not 'appdata'
- new upstream release

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-7
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0-3
- Rebuild for Python 3.6

* Tue Nov 22 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.0-2
- upped minimum aeidon version requirement

* Tue Nov 22 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.0-1
- misc cleanups
- new upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.25-3
- Attempt to fix FTBFS by adding BR: python3-devel

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Richard Hughes <rhughes@redhat.com> - 0.25-1
- New upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 07 2011 Lucian Langa <cooly@gnome.eu.org> - 0.19.2-1
- new upstream release

* Mon Sep 26 2011 cooly@gnome.eu.org - 0.19.1-1
- new upstream release

* Sun Jul 31 2011 Lucian Langa <cooly@gnome.eu.org> - 0.19-1
- new upstream release

* Sat Jun 18 2011 Lucian Langa <cooly@gnome.eu.org> - 0.18-1
- new upstream release

* Sun Apr 24 2011 Lucian Langa <cooly@gnome.eu.org> - 0.17.2-1
- drop version from supackage (to match main version)
- new upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 18 2010 Lucian Langa <cooly@gnome.eu.org> - 0.17.1-1
- new upstream release

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jul 08 2010 Lucian Langa <cooly@gnome.eu.org> - 0.17-1
- new supackage aeidon the subtitle engine
- new upstream release

* Fri Apr 02 2010 Lucian Langa <cooly@gnome.eu.org> - 0.15.1-1
- update to 0.15.1

* Sun Sep 27 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.15-5
- Update desktop file according to F-12 FedoraStudio feature

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.15-4
- Use bzipped upstream tarball.

* Sun Aug 02 2009 Lucian Langa <cooly@gnome.eu.org> - 0.15-3
- do not remove required file (b.g.o #590537)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 18 2009 Lucian Langa <cooly@gnome.eu.org> - 0.15-1
- add python-chardet as requirement
- new upstream release

* Mon Apr 13 2009 Lucian Langa <cooly@gnome.eu.org> - 0.14-1
- fix Source url
- new upstream release

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Lucian Langa <cooly@gnome.eu.org> - 0.13.1-1
- initial package


