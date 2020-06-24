%global modname kajiki

Name:               python-kajiki
Version:            0.8.2
Release:            2%{?dist}
Summary:            Really fast well-formed xml templates

License:            MIT
URL:                https://pypi.io/project/Kajiki
Source0:            %pypi_source Kajiki

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-babel
BuildRequires:      python3-nine
BuildRequires:      python3-pytz
BuildRequires:      python3-nose


%description
Are you tired of the slow performance of Genshi? But you still long for the
assurance that your output is well-formed that you miss from all those
other templating engines? Do you wish you had Jinja's blocks with Genshi's
syntax? Then look  no further, Kajiki is for you! Kajiki quickly compiles
Genshi-like syntax to *real python bytecode* that renders with blazing-fast
speed! Don't delay! Pick up your copy of Kajiki today!

%package -n python3-kajiki
Summary:            Really fast well-formed xml templates
%{?python_provide:%python_provide python3-kajiki}

Requires:           python3-babel
Requires:           python3-nine
Requires:           python3-pytz

%description -n python3-kajiki
Are you tired of the slow performance of Genshi? But you still long for the
assurance that your output is well-formed that you miss from all those
other templating engines? Do you wish you had Jinja's blocks with Genshi's
syntax? Then look  no further, Kajiki is for you! Kajiki quickly compiles
Genshi-like syntax to *real python bytecode* that renders with blazing-fast
speed! Don't delay! Pick up your copy of Kajiki today!

%prep
%autosetup -n Kajiki-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-kajiki
%doc README.rst LICENSE.rst CHANGES.rst PKG-INFO
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/Kajiki-%{version}-*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-2
- Rebuilt for Python 3.9

* Mon May 25 2020 Nils Philippsen <nils@redhat.com> - 0.8.2-1
- version 0.8.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-4
- Subpackage python2-kajiki has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Kevin Fenzi <kevin@scrye.com> - 0.8.0-1
- Update to 0.8.0. Fixes bug #1716377

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7.2
- Update to 0.7.2
- Add missing BR on python-nose to run the tests

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.1-2
- Fix creation of python2- subpackage

* Fri Sep 15 2017 Kevin Fenzi <kevin@scrye.com> - 0.7.1-1
- Update to 0.7.1. Fixes bug #1465427

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 27 2017 Kevin Fenzi <kevin@scrye.com> - 0.6.3-1
- Update to 0.6.3. Fixes bug #1455539

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 27 2016 Kevin Fenzi <kevin@scrye.com> - 0.6.1-1
- Update to 0.6.1. Fixes bug #1400145

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 15 2016 Ralph Bean <rbean@redhat.com> - 0.5.5-1
- new version

* Thu Jun 09 2016 Ralph Bean <rbean@redhat.com> - 0.5.4-1
- new version

* Tue Jun 07 2016 Kevin Fenzi <kevin@scrye.com> - 0.5.4-1
- Update to 0.5.4. Fixes bug #1342848

* Mon Apr 04 2016 Ralph Bean <rbean@redhat.com> - 0.5.3-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Ralph Bean <rbean@redhat.com> - 0.5.2-2
- Add python3 subpackage and modernize python macros.

* Wed Oct 14 2015 Ralph Bean <rbean@redhat.com> - 0.5.2-1
- new version

* Wed Sep 16 2015 Ralph Bean <rbean@redhat.com> - 0.5.1-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 12 2015 Ralph Bean <rbean@redhat.com> - 0.4.4-3
- Add req on python-nine.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 12 2014 Ralph Bean <rbean@redhat.com> - 0.4.4-1
- Latest upstream.
- Disabled tests now that they require python-nine which hasn't yet been
  packaged for Fedora.

* Tue Oct 08 2013 Ralph Bean <rbean@redhat.com> - 0.3.5-4
- Added dep on pytz.

* Tue Oct 08 2013 Ralph Bean <rbean@redhat.com> - 0.3.5-3
- Update dep from babel to python-babel.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Ralph Bean <rbean@redhat.com> - 0.3.5-1
- initial package for Fedora
