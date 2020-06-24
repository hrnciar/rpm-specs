# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

Name:           sugar-visualmatch
Version:        49
Release:        13%{?dist}
Summary:        A visual matching game

# namingalert.py is licensed as LGPLv2+
# sprites.py is licensed under the MIT license
# other files are licensed as GPLv3+
License:        GPLv3+ and LGPLv2+ and MIT
URL:            http://wiki.sugarlabs.org/go/Activities/VisualMatch
Source0:        http://download.sugarlabs.org/sources/honey/Visualmatch/VisualMatch-%{version}.tar.bz2

BuildRequires:	gettext
BuildRequires:	gobject-introspection-devel
BuildRequires:	python2-devel
BuildRequires:	sugar-toolkit-gtk3-devel
BuildArch:	noarch
Requires:	sugar

%description
The object is to find sets of three cards where each attribute—color,
shape, number of elements, and shading—either match on all three cards
or are different on all three cards. The current version doesn't yet
support sharing with multiple players or saving to the Journal, but it
can be played by a single player.


%prep
%setup -q -n VisualMatch-%{version}

sed -i 's/python/python2/' *.py

%build
python2 ./setup.py build


%install
python2 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
chmod 0644 $RPM_BUILD_ROOT/%{sugaractivitydir}/VisualMatch.activity/gencards.py
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

%find_lang org.sugarlabs.VisualMatchActivity


%files -f org.sugarlabs.VisualMatchActivity.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/VisualMatch.activity/


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 49-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 49-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 49-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 49-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Kalpa Welivitigoda <callkalpa@gmail.com> - 49-9
- Fix FTBFS (#1556475)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 49-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 49-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 49-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 49-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 26 2013 Peter Robinson <pbrobinson@fedoraproject.org> 49-1
- Release 49

* Sat Jan 26 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 47-1
- New 47 release

* Sun Oct 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> 45-1
- New 45 release

* Sat Oct 13 2012 Peter Robinson <pbrobinson@fedoraproject.org> 43-1
- New 43 release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 30 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 38-1
- New 38 release

* Sat Apr 21 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 37-1
- New 37 release

* Fri Apr 20 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 36-1
- New 36 release

* Wed Feb 29 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 35-1
- New 35 release

* Sun Jan 08 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 34-1
- New 34 release

* Tue Dec 20 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 33-1
- New 33 release

* Fri Nov 18 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 32-1
- New 32 release

* Sun Oct  2 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 30-1
- New 30 release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 27-1
- New 27 release

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 23-2
- recompiling .py files against Python 2.7 (rhbz#623391)

* Thu Jul 08 2010 Sebastian Dziallas <sebastian@when.com> - 23-1
- new upstream release

* Sat Feb 27 2010 Sebastian Dziallas <sebastian@when.com> - 21-1
- new upstream release

* Mon Feb 15 2010 Sebastian Dziallas <sebastian@when.com> - 20-3
- make sure to grab locale files now

* Mon Feb 15 2010 Sebastian Dziallas <sebastian@when.com> - 20-2
- add gettext build requirement

* Mon Feb 15 2010 Sebastian Dziallas <sebastian@when.com> - 20-1
- new upstream release

* Tue Jan 12 2010 Sebastian Dziallas <sebastian@when.com> - 17-1
- new upstream release
- switch to GPLv3+

* Tue Dec 29 2009 Sebastian Dziallas <sebastian@when.com> - 13-1
- new upstream release
- fix license tag

* Sun Dec 06 2009 Sebastian Dziallas <sebastian@when.com> - 8-1
- initial packaging