# This package has a circular dependency with pyutil.
# Enable the bootstrap conditional to break the cycle.
%bcond_with bootstrap

Name:           python-zbase32
Version:        1.1.5
Release:        20%{?dist}
Summary:        A base32 encoder/decoder
License:        BSD and LGPLv2
URL:            http://allmydata.org/trac/zbase32
Source0:        http://pypi.python.org/packages/source/z/zbase32/zbase32-%{version}.tar.gz
Patch1:         0001-port-to-Python-3.patch
Patch2:         0002-expect-binary-data-to-be-bytes-not-str.patch
BuildArch:      noarch

%global _description\
An alternate base32 encoder (not RFC 3548 compliant).

%description %_description

%package -n python3-zbase32
Summary: %summary
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with bootstrap}
%{?python_disable_dependency_generator}
%else
BuildRequires:  python3-pyutil
Requires:       python3-pyutil
%endif
%{?python_provide:%python_provide python3-zbase32}

%description -n python3-zbase32 %_description

%prep
%setup -q -n zbase32-%{version}
%patch1 -p1
%patch2 -p1
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" .

%build
%py3_build

%install
%py3_install

chmod 0755 %{buildroot}%{python3_sitelib}/zbase32/test/test_zbase32.py
chmod 0755 %{buildroot}%{python3_sitelib}/zbase32/zbase32.py

%check
%if ! %{with bootstrap}
%{__python3} setup.py test
%endif

%files -n python3-zbase32
%doc README DESIGN TODO
%{python3_sitelib}/zbase32
%{python3_sitelib}/zbase32-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-19
- Rebuilt for Python 3.9

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-18
- Bootstrap for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-13
- Subpackage python2-zbase32 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 27 2018 Dan Callaghan <dcallagh@redhat.com> - 1.1.5-12
- Added Python 3 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.5-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.5-8
- Python 2 binary package renamed to python2-zbase32
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 30 2013 Christopher Meng <rpm@cicku.me> - 1.1.5-1
- Update to 1.1.5

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.1.3-1
- Upstream released new version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 27 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.1.2-7
- pyutil is in. Re-enable tests. Re-add Requires: pyutil

* Tue Jul 27 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.1.2-6
- Also comment out Requires: pyutil

* Tue Jul 27 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.1.2-5
- Disable tests. We need to bootstrap against pyutil

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun 24 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.1.2-3
- Re-diff patch

* Thu Jun 24 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.1.2-2
- Re-add patch

* Thu Jun 24 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.1.2-1
- Upstream released new version

* Sun Feb 21 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.1.1-4
- Require pyutil now it's in

* Tue Feb 09 2010 Ruben Kerkhof <ruben@rubenkerkhof.com 1.1.1-3
- Stop setuptools from looking for setuptools_darcs

* Mon Feb 01 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.1.1-2
- Disable dependency on pyutil until that's approved (#560457)

* Sun Jan 31 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.1.1-1
- Initial import

