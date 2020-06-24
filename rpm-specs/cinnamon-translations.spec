%global _trans_version 2018.12.11


Name:           cinnamon-translations
Version:        4.6.1
Release:        1%{?dist}
Summary:        Translations for Cinnamon and Nemo

License:        GPLv2+
URL:            https://github.com/linuxmint/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        http://packages.linuxmint.com/pool/main/m/mint-translations/mint-translations_%{_trans_version}.tar.xz
BuildRequires:  gettext

BuildArch:      noarch

%description
Translations for Cinnamon, Nemo and Mintlocale.


%prep
%autosetup -a 1 -p 1


%build
%{make_build}
%{make_build} -C mint-translations


%install
# install mint translations for mintlocale
%{_bindir}/find mint-translations -not -name 'mintlocale.mo' -type f -delete
%{_bindir}/find . -name 'cinnamon-bluetooth.mo' -type f -delete
%{__cp} -pr mint-translations/%{_datadir}/linuxmint/locale .%{_datadir}
%{__cp} -pr .%{_prefix} %{buildroot}

%find_lang cinnamon
%find_lang mintlocale
%find_lang nemo
%find_lang nemo-extensions
%find_lang cinnamon-control-center
%find_lang cinnamon-screensaver
%find_lang cinnamon-session
%find_lang cinnamon-settings-daemon

%files -f cinnamon.lang -f mintlocale.lang -f nemo.lang -f nemo-extensions.lang -f cinnamon-control-center.lang -f cinnamon-screensaver.lang -f cinnamon-session.lang -f cinnamon-settings-daemon.lang
%license COPYING


%changelog
* Wed Jun 17 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.1-1
- Update to 4.6.1 release

* Tue May 12 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.0-1
- Update to 4.6.0 release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Leigh Scott <leigh123linux@googlemail.com> - 4.4.2-1
- Update to 4.4.2 release

* Wed Dec 11 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.1-1
- Update to 4.4.1 release

* Tue Nov 26 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.0-1
- Update to 4.4.0 release

* Wed Jul 31 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.2-1
- Update to 4.2.2 release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.1-1
- Update to 4.2.1 release

* Fri Jun 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.0-1
- Update to 4.2.0 release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.2-1
- Update to 4.0.2 release

* Wed Nov 28 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.1-1
- Update to 4.0.1 release

* Sat Nov 03 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.0-1
- Update to 4.0.0 release

* Thu Aug 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.2-1
- Update to 3.8.2 release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 22 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.1-2
- Updated translations for mintlocale

* Tue May 22 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.1-1
- Update to 3.8.1 release

* Fri Apr 20 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.0-1
- Update to 3.8.0 release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 12 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.6.2-1
- update to 3.6.2 release

* Tue Oct 24 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.6.0-1
- update to 3.6.0 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.2-1
- update to 3.4.2 release

* Sun May 07 2017 Björn Esser <besser82@fedoraproject.org> - 3.4.1-2
- Updated translations for mintlocale

* Sun May 07 2017 Björn Esser <besser82@fedoraproject.org> - 3.4.1-1
- update to 3.4.1 release

* Thu May 04 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-1
- update to 3.4.0 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 leigh scott <leigh123linux@googlemail.com> - 3.2.2-1
- update to 3.2.2 release

* Mon Nov 28 2016 leigh scott <leigh123linux@googlemail.com> - 3.2.1-1
- update to 3.2.1 release

* Thu Nov 10 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.2.0-1
- update to 3.2.0 release

* Sun Jun 26 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.3-1
- update to 3.0.3 release

* Tue May 24 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.2-1
- update to 3.0.2 release

* Tue May 24 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.1-1
- update to 3.0.1 release

* Mon Apr 25 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-1
- update to 3.0.0 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 09 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.8.1-2
- rebuilt

* Mon Nov 09 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.8.1-1
- update to 2.8.1 release

* Thu Oct 22 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.8.0-1
- update to 2.8.0 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.2-1
- update to 2.6.2 release

* Thu May 21 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.1-1
- update to 2.6.1 release

* Wed May 20 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.0-1
- update to 2.6.0 release

* Fri Apr 03 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.4.4-1
- update to 2.4.5

* Sun Nov 23 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.2-1
- update to 2.4.2

* Wed Nov 12 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.1-1
- update to 2.4.1

* Sat Nov 08 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.0-2
- fix locale path

* Fri Oct 31 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.0-1
- update to 2.4.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.3-2
- move mintlocale translations

* Tue May 27 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.3-1
- update to 2.2.3
- add mintlocale translations

* Tue May 20 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.2-1
- update to 2.2.2

* Wed May 07 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.1-1
- update to 2.2.1

* Mon Apr 14 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.0-1
- update to 2.2.0

* Sun Nov 10 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.2-1
- update to 2.0.2

* Thu Oct 17 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.1-2
- co-own cinnamon locale directories
- remove requires cinnamon

* Wed Oct 09 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.1-1
- update to 2.0.1

* Wed Oct 02 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.0-1
- update to 2.0.0

* Sun Sep 15 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.2-0.4.git6091a38
- update to latest git

* Sat Aug 24 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.2-0.3.git444eac5
- add cinnamon-control-center files

* Fri Aug 23 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.2-0.2.git9c15ee5
- update to latest git

* Fri Aug 23 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.9.2-0.1.git28b56a7
- Initial build

