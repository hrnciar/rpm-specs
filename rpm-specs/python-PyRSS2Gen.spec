Name:		python-PyRSS2Gen
Version:	1.1
Release:	25%{?dist}
Summary:	A Python library for generating RSS 2.0 feeds

License:	BSD
URL:		http://www.dalkescientific.com/Python/PyRSS2Gen.html
Source0:	http://www.dalkescientific.com/Python/PyRSS2Gen-%{version}.tar.gz
BuildArch:	noarch
%global _description\
A Python library for generating RSS 2.0 feeds.

%description %_description

%package -n python3-PyRSS2Gen
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
Requires:	python3-feedparser
Summary:	A Python library for generating RSS 2.0 feeds
BuildArch:	noarch
%description -n python3-PyRSS2Gen
A Python3 library for generating RSS 2.0 feeds.



%prep
%setup -qn PyRSS2Gen-%{version}

%build

%install
%{__python3} setup.py install --root %{buildroot}

%check


%files -n python3-PyRSS2Gen
%{python3_sitelib}/PyRSS2Gen-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/PyRSS2Gen.py
%{python3_sitelib}/__pycache__/PyRSS2Gen.cpython-*.pyc
%doc README LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-25
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-23
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-22
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1-19
- Subpackage python2-pyrss2gen has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1-17
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1-15
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1-14
- Python 2 binary package renamed to python2-pyrss2gen
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1-11
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Sep 10 2013 Pete Travis <immanetize@fedoraproject.org> 1.1-4
- Completing python3 subpackaging, so it really does work.

* Fri Sep 06 2013 Pete Travis <immanetize@fedoraproject.org> 1.1-3
- This should build a python3 package, too.

* Thu Aug 22 2013 Pete Travis <immanetize@fedoraproject.org> 1.1-1
- Initial packaging.

* Thu Aug 22 2013 Pete Travis <immanetize@fedoraproject.org> 1.1-2
- Correcting Requires and BuildRequires in spec, build as noarch.
