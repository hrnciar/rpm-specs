# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

Name:           sugar-ruler
Version:        33
Release:        16%{?dist}
Summary:        Simple collection of measurement tools

License:        GPLv3+
URL:            http://wiki.sugarlabs.org/go/Activities/Ruler
Source0:        http://download.sugarlabs.org/sources/honey/Ruler/Ruler-%{version}.tar.bz2

BuildRequires:  python2-devel sugar-toolkit-gtk3 gettext
BuildArch:      noarch
Requires:       sugar >= 0.97.6

%description
Ruler is a simple collection of measurement tools that are displayed 
on the screen. Since the OLPC XO computer has a 200 DPI display, the 
rulers are quite accurate. One other hardware, where the display 
resolution is not known, their is a spinner to let the user set the DPI. 
Ruler saves this value to the Journal, so it need not be set on 
subsequent uses of the Activity.

%prep
%setup -q -n Ruler-%{version}

sed -i 's/python/python2/' *.py

%build
python2 ./setup.py build

%install
python2 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

%find_lang com.laptop.Ruler


%files -f com.laptop.Ruler.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Ruler.activity/


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 33-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 33-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 33-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 33-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 33-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 33-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 33-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 33-9
- Escape macros in %%changelog

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 33-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 33-7
- Fix the bug number in the previous entry of the changelog

* Thu Feb 23 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 33-6
- Remove the generated .desktop file (#1424512)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 33-1
- Release 33

* Sat Dec 14 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 32-1
- Release 32

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 31 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 31-1
- Release 31

* Sun May 26 2013 Peter Robinson <pbrobinson@fedoraproject.org> 29
- Release 29

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 27-1
- new upstream 27 release

* Tue Jan 08 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 25-1
- new upstream 25 release

* Sat Dec 29 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 24-1
- new upstream 24 release

* Fri Nov 02 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 23-2
- changed to require: sugar >= 0.97.6

* Tue Oct 30 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 23-1
- new upstream 23 release

* Sat Oct 27 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 21-1
- new upstream 21 release
- gtk3 port

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 01 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 19-1
- new upstream 19 release

* Mon Jan 16 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 17-1
- new upstream 17 release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 30 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 14-1
- new upstream 14 release

* Mon Oct 10 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 13-1
- new upstream 13 release

* Tue Sep 13 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 12-2
- use of %%{__python} in install

* Sun Sep 11 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 12-1
- removed unsupported languages

* Wed Sep 7 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 11-6
- changed summary and description

* Thu Sep 1 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 11-5
- fixed too long error and fullstop warning in summary
- fixed license error

* Fri Aug 26 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 11-4
- use of %%{__python}

* Fri Aug 26 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 11-3
- word splitting in description fixed

* Fri Aug 26 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 11-2
- removed BuildRoot
- removed "rm -rf $RPM_BUILD_ROOT"
- removed %%clean
- description wrapped at 80 chars
- swapped $RPM_BUILD_ROOT with %%{buildroot}

* Fri Aug 26 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 11-1
- initial packaging
