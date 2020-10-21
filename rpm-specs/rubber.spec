Name: rubber
Version: 1.5.1
Release: 5%{?dist}
Summary: An automated system for building LaTeX documents

License: GPL+

URL: https://launchpad.net/%{name}
Source0: https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel texinfo-tex
Requires: tex(latex)

%description
This is a building system for LaTeX documents. It is based on a routine that
runs just as many compilations as necessary. The module system provides a
great flexibility that virtually allows support for any package with no user
intervention, as well as pre- and post-processing of the document. The
standard modules currently provide support for bibtex, dvips, dvipdfm, pdftex,
makeindex. A good number of standard packages are supported, including
graphics/graphicx (with automatic conversion between various formats and
Metapost compilation).

%prep
%setup -q
for file in doc/man-fr/*; do
  iconv -f ISO88591 -t utf8 $file -o $file
done

%build
%{py3_build}

%install
%{py3_install}
mkdir -p %{buildroot}/%{_infodir}
mkdir -p %{buildroot}/%{_mandir}
mv %{buildroot}/usr/info/ %{buildroot}/%{_infodir}
mv %{buildroot}/usr/man/* %{buildroot}/%{_mandir}

%files
%doc COPYING NEWS README
%{_bindir}/*
%{_defaultdocdir}/%{name}/*
%{_infodir}/*
%{python3_sitelib}/*
%{_mandir}/man1/*.gz
%{_mandir}/fr/man1/*.gz

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1, supports python 3, fixes bz #1738178, #1745467

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 1.4-9
- Use python2 macros
- Remove macros for install-info

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.4-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 20 2015 Dennis Chen <barracks510@gmail.com> - 1.4-1
- Updated to version 1.4 of rubber.

* Tue Nov 24 2015 Dennis Chen <barracks510@gmail.com> - 1.3-1
- Updated to latest version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1-16
- Fix wrong Source0 URL

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 15 2013 Patrick C. F. Ernzer <rubber.spec@pcfe.net> - 1.1-14
- incorporating patch from https://live.gnome.org/Gedit/LaTeXPlugin/FAQ

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1-12
- Rubber is hosted in launchpad
- Removing /usr/share/rubber/modules/etex.rub fixes bz #880568

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Dec 28 2009 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1-7
- Adding virtual dependency on latex (bz #550792)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1-5
- Patch to remove a Deprecation Warning in Python 2.6 (bz #506053)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.1-3
- Rebuild for Python 2.6

* Wed Sep 17 2008 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1-2
- ***

* Wed Sep 17 2008 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1-1
- Initial specfile

