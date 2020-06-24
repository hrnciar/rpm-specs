# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

Name:           sugar-view-slides
Version:        8
Release:        22%{?dist}
Summary:        Image serie viewer for Sugar

License:        GPLv3+
URL:            http://wiki.laptop.org/go/View_Slides
Source0:        http://download.sugarlabs.org/sources/honey/ViewSlides/ViewSlides-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  python2
BuildRequires:  sugar-toolkit
BuildRequires:  gettext

Requires:       sugar
Requires:       sugar-toolkit
Requires:       python2-pygame


%description
The View Slides activity is meant to allow the XO laptop to read
view the contents of a Zip file containing images named sequentially.
Project Gutenberg has a few books as raw scanned images, and this can
be a useful format for picture books, comic books, magazine articles,
photo essays, etc.

The interface to View Slides is similar to the core Read activity,
which should not be surprising as the toolbar code was adapted from
Read's toolbar. You can use the up and down arrows or the game
controller to move from page to page.


%prep
%setup -q -n ViewSlides-%{version}
chmod +x xopower.py

sed -i 's/python/python2/' *.py

%build
python2 setup.py build


%install
python2 setup.py install --prefix=%{buildroot}/%{_prefix}
%find_lang org.laptop.ViewSlidesActivity


%files -f org.laptop.ViewSlidesActivity.lang
%doc NEWS
%{sugaractivitydir}/ViewSlides.activity/


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 8-18
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 8-12
- Add Requires sugar-toolkit

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 8-5
- recompiling .py files against Python 2.7 (rhbz#623390)

* Wed Mar 17 2010 Fabian Affolter <fabian@bernewireless.net> - 8-4
- Added gettext as a BR

* Mon Mar 15 2010 Fabian Affolter <fabian@bernewireless.net> - 8-3
- Minor layout changes

* Sat Aug 01 2009 Fabian Affolter <fabian@bernewireless.net> - 8-2
- Added pygame as a requirement (as mentioned in #508441) 

* Wed Jun 24 2009 Fabian Affolter <fabian@bernewireless.net> - 8-1
- Updated to new upstream version 7
- Added translation support
- Removed all the vcs checkout stuff 

* Thu Jan 29 2009 Fabian Affolter <fabian@bernewireless.net> - 0-1.20090129
- Initial package for Fedora
