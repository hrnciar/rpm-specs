# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

Name:           sugar-measure
Version:        103
Release:        3%{?dist}
Summary:        Measure for Sugar

License:        GPLv3+
URL:            http://wiki.laptop.org/go/Measure
Source0:        https://download.sugarlabs.org/sources/honey/Measure/Measure-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3

Requires:       sugar


%description
A tool on the XO that allows kids to indulge in "learning by doing". 
It provides an interface for the kids to connect  sensors (light, heat,
magnetic field etc) and view their signal.


%prep
%autosetup -n Measure-%{version}

sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build


%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

%find_lang org.laptop.MeasureActivity


%files -f org.laptop.MeasureActivity.lang
%license COPYING
%doc README
%{sugaractivitydir}/Measure.activity/
%{_datadir}/metainfo/*.appdata.xml


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 103-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 103-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

• Mon Feb 17 2020 Peter Robinson <pbrobinson@fedoraproject.org> 103-1
- Release 103

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 102-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 102-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Peter Robinson <pbrobinson@fedoraproject.org> 102-3
- Fix build without python-unversioned-command

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 102-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 102-1
- Release 102

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 101-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 101-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 101-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 101-1
- Release 101

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 13 2015 Kalpa Welivitigoda - 52-1
- Release 52

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 51-3
- Add Requires sugar-toolkit

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 51-1
- Release 51

* Tue Aug 20 2013 Kalpa Welivitigoda <callkalpa@gmail.com> 49-1
- Release 49

* Sun Aug 18 2013 Kalpa Welivitigoda <callkalpa@gmail.com> 48-1
- Release 48

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 04 2013 Kalpa Welivitigoda <callkalpa@gmail.com> 47-1
- Release 47

* Sun Jun 30 2013 Kalpa Welivitigoda <callkalpa@gmail.com> 46-1
- Release 46

* Sun May 26 2013 Peter Robinson <pbrobinson@fedoraproject.org> 45-1
- Release 45

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 15 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 44-1
- New 44 release

* Sun Jul 01 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 42-1
- New 42 release

* Sun Jun 24 2012 Kalpa Welivitigoda <callkalpa@gmail.com>
- New 41 release

* Sun Jun 24 2012 Kalpa Welivitigoda <callkalpa@gmail.com>
- New 40 release

* Sat Jun 23 2012 Kalpa Welivitigoda <callkalpa@gmail.com>
- New 39 release

* Tue Jan 17 2012 Kalpa Welivitigoda <callkalpa@gmail.com>
- New 36 release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 11 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 35-1
- New 35 release

* Sat Oct  1 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 34-1
- New 34 release
- Cleanup spec, add COPYING, update license

* Wed Aug 10 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 33-1
- New 33 release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 32-1
- New 32 release

* Sat Jul 31 2010 Kedar Sovani <kedars@marvell.com> - 31.1
- Update to upstream Measure version 31.

* Tue Jan 19 2010 Kedar Sovani <kedars@marvell.com> - 29-1
- Initial package for Fedora
