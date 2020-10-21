# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

Name:		sugar-labyrinth
Version:	16
Release:        15%{?dist}
Summary:        A lightweight mind-mapping activity for Sugar

License:        GPLv2+
URL:            http://wiki.sugarlabs.org/go/Activities/Labyrinth
Source0:        http://download.sugarlabs.org/sources/honey/Labyrinth/Labyrinth-%{version}.tar.bz2

BuildRequires:  gettext python2 sugar-toolkit
BuildArch:      noarch
Requires:       sugar
Requires:       sugar-toolkit

%description
A lightweight mind-mapping activity based on an Open Source project called
Labyrinth. It allows creating mind maps from a mixture of text, freehand
drawings, and images from your Journal. There is an infinite sized canvas
for your map that can be panned and zoomed while you work. Maps can be
"Kept to PDF" for uploading to web sites, sharing, and printing by others
who may not be using Sugar. 


%prep
%setup -q -n Labyrinth-%{version}
rm po/aym.po
rm po/cpp.po
rm po/nah.po
rm po/son.po

# remove these shebangs to calm rpmlint down
for Files in src/TextThought.py src/MMapArea.py labyrinthactivity.py src/labyrinth.py; do
  %{__sed} -i.orig -e 1d ${Files}
  touch -r ${Files}.orig ${Files}
  %{__rm} ${Files}.orig
done

sed -i 's/python/python2/' *.py

%build
python2 ./setup.py build


%install
python2 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}

%find_lang org.gnome.Labyrinth

# Remove empty file
rm $RPM_BUILD_ROOT/%{_datadir}/sugar/activities/Labyrinth.activity/port/TODO


%files -f org.gnome.Labyrinth.lang
%license COPYING
%doc AUTHORS NEWS README
%{sugaractivitydir}/Labyrinth.activity/


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16-15
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 16-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 16-4
- Add Requires sugar-toolkit

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 16-1
- New 16 release

* Tue Jun 18 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 15-1
- New 15 release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 14-1
- New 14 release

* Tue Jun 26 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 13-1
- New 13 release

* Fri Mar 16 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 12-1
- New 12 release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@gmail.com> - 11-1
- New 11 release

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 9-2
- recompiling .py files against Python 2.7 (rhbz#623377)

* Mon Mar 24 2010 Sebastian Dziallas <sebastian@when.com> - 9-1
- new upstream release

* Fri Mar 05 2010 Sebastian Dziallas <sebastian@when.com> - 8-1
- initial packaging
