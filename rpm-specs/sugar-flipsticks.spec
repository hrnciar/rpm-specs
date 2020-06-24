# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

Name:           sugar-flipsticks
Version:        13
Release:        15%{?dist}
Summary:        A keyframe animation activity for Sugar
License:        GPLv2+
URL:            http://wiki.sugarlabs.org/go/Activities/Flip_Sticks

Source0:        http://download.sugarlabs.org/activities/4044/flip_sticks-%{version}.xo
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  sugar-toolkit
BuildRequires:  gettext
Requires:       sugar
Requires:       sugar-toolkit

%description
Flipsticks is a keyframe animation activity that lets you pose and program
a stick figure to walk, run, rotate, twist, tumble and dance. You can save
your animations to the journal and will soon be able to share them via the
mesh. Flipsticks can be used to explore concepts in geometry, computer
programming and animation; it helps develop spatial and analytical thinking
skills. 

%prep
%setup -q -n FlipSticks.activity

sed -i 's/python/python2/' setup.py

%build
python2 ./setup.py build

%install
python2 ./setup.py install --prefix=%{buildroot}/%{_prefix}
%find_lang org.worldwideworkshop.olpc.FlipSticks

%files -f org.worldwideworkshop.olpc.FlipSticks.lang
%license COPYING
%doc AUTHORS NEWS TODO
%{sugaractivitydir}/FlipSticks.activity/

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 13-5
- Add Requires sugar-toolkit

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 13-1
- update to v13

* Thu Mar  8 2012 Tom Callaway <spot@fedoraproject.org> - 12-1
- update to v12

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 18 2011 Fabian Affolter <fabian@bernewireless.net> - 8-3
- Translations added

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 16 2010 Fabian Affolter <fabian@bernewireless.net> - 8-1
- Updated to new upstream version 8

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 2-3
- recompiling .py files against Python 2.7 (rhbz#623370)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 20 2009 Fabian Affolter <fabian@bernewireless.net> - 2-1
- Initial package for Fedora
