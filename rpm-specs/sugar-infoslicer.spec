# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

Name:           sugar-infoslicer
Version:        25
Release:        10%{?dist}
Summary:        Downloader for articles from Wikipedia
License:        GPLv2+
URL:            http://sugarlabs.org/go/Activities/InfoSlicer
Source0:        https://github.com/sugarlabs/infoslicer/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:	gettext
BuildRequires:	gobject-introspection-devel
BuildRequires:	python2-devel
BuildRequires:	sugar-toolkit-gtk3-devel
Requires:       sugar
Requires:	sugar-toolkit-gtk3

%description
InfoSlicer downloads articles from Wikipedia so that you can create new
documents by dragging and dropping content from the Wikipedia articles.
You can then publish the articles as a mini website.

%prep
%autosetup -n infoslicer-%{version}

sed -i 's/python/python2/' setup.py

%build
python2 ./setup.py build

%install
python2 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true
%find_lang org.sugarlabs.InfoSlicer

%files -f org.sugarlabs.InfoSlicer.lang
%license COPYING
%doc NEWS README examples/
%{sugaractivitydir}/InfoSlicer.activity/


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 25-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 25-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 25-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 22 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 25-1
- Release 25

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 24-1
- Release 24

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 23-1
- Release 23

* Mon Dec 16 2013 Peter Robinson <pbrobinson@fedoraproject.org> 22-1
- Release 22

* Mon Aug 19 2013 Peter Robinson <pbrobinson@fedoraproject.org> 21-1
- Release 21

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Peter Robinson <pbrobinson@fedoraproject.org> 20-1
- Release 20

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> 15-3
- Add patch to remove cjson

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 15-1
- Release 15

* Sun Apr 15 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 14-1
- Release 14

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 31 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 11-1
- Release 11

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 8-2
- bump build

* Tue Nov 16 2010 Fabian Affolter <fabian@bernewireless.net> - 8-1
- Updated to new upstream version 8

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 6-3
- recompiling .py files against Python 2.7 (rhbz#623375)

* Mon Dec 14 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 6-2
- Add buildreq gettext to fix build issues on F-12/rawhide - fixes # 539177

* Fri Nov 20 2009 Fabian Affolter <fabian@bernewireless.net> - 6-1
- Updated to new upstream version 6

* Thu Jul 30 2009 Fabian Affolter <fabian@bernewireless.net> - 5.1-1
- Removed end-of-line fix
- Added support for translations
- Updated to new upstream version 5-1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 25 2009 Fabian Affolter <fabian@bernewireless.net> - 5-1
- Initial package for Fedora
