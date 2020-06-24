%global srcname anyjson
%global sum Wraps the best available JSON implementation

Name:           python-%{srcname}
Version:        0.3.3
Release:        27%{?dist}
Summary:        %{sum}

License:        BSD
URL:            http://pypi.python.org/pypi/anyjson
Source0:        http://pypi.python.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
# Fix Python 3 compatibility
Patch0:         anyjson-python3.patch
# Include ujson, raise priority of cjson and drop the 'deprecation'
# warning (it's about as alive as half the others), drop jsonlib,
# jsonlib2 and django.utils.simplejson (which all appear to be dead
# as doornails)
%if 0%{?fedora} > 25 || 0%{?rhel} > 7
Patch1:         python-anyjson-update-order-ujson.patch
%else
# Just the same, but don't include ujson, as its behaviour pre-2.0
# was very weird and unexpected, it would 'serialize' all sorts of
# unserializable things
Patch1:         python-anyjson-update-order.patch
%endif
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-nose

BuildRequires:  python3-simplejson

%if 0%{?fedora} > 25 || 0%{?rhel} > 7
BuildRequires:  python3-ujson
%endif

%description
Anyjson loads whichever is the fastest JSON module installed and
provides a uniform API regardless of which JSON implementation is used.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-six

%description -n python3-%{srcname}
Anyjson loads whichever is the fastest JSON module installed and
provides a uniform API regardless of which JSON implementation is used.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test
 
%files -n python3-%{srcname}
%doc CHANGELOG README
%license LICENSE
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-27
- Rebuilt for Python 3.9

* Thu May 21 2020 Yatin Karel <ykarel@redhat.com> - 0.3.3-26
- Make anyjson buildable in El8 (#1787123)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-24
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-23
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-21
- Subpackage python2-anyjson has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-18
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.3-17
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Adam Williamson <awilliam@redhat.com> - 0.3.3-14
- Add ujson support (for Fedora > 25, with ujson 2.0+)

* Sat Dec 24 2016 Adam Williamson <awilliam@redhat.com> - 0.3.3-13
- update the Python 3 compatibility patch (fixes build)
- enable tests
- add some more BuildRequires to extend test coverage

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com>
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 14 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.3-11
- Fix FTBFS (rhbz#1307894)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.3-9
- Cleanup

* Wed Nov 04 2015 Matej Stuchlik <mstuchli@redhat.com> - 0.3.3-8
- Rebuilt for Python 3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.3.3-2
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Aug 03 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.3.3-1
- update to 0.3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-3
- Minor py3 fixes

* Sun Jan 29 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 0.3.1-2
- add python3 variant

* Sun Apr 03 2011 Fabian Affolter <fabian@bernewireless.net> - 0.3.1-1
- Updated to new upstream version 0.3.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Fabian Affolter <fabian@bernewireless.net> - 0.3-1
- Updated to new upstream version 0.3

* Sat Jul 31 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jul 03 2010 Fabian Affolter <fabian@bernewireless.net> - 0.2.4-1
- Initial package
