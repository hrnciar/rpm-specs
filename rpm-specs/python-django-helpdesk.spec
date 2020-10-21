%global pypi_name django-helpdesk

%global desc %{expand: \
Django-helpdesk This is a Django-powered helpdesk ticket tracker, designed to
plug into an existing Django website and provide you with internal (or,
perhaps, external) helpdesk management.}

Name:           python-%{pypi_name}
Version:        0.2.22
Release:        2%{?dist}
Summary:        Django-powered ticket tracker for your helpdesk

License:        BSD
URL:            https://github.com/django-helpdesk/django-helpdesk
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%{?python_enable_dependency_generator}

BuildRequires:	python3-devel
BuildRequires:	python3dist(beautifulsoup4)
BuildRequires:	python3dist(django)
BuildRequires:	python3dist(lxml)
BuildRequires:	python3dist(pytz)
BuildRequires:	python3dist(pytz)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(simplejson)
BuildRequires:	python3dist(six)
BuildRequires:	python3dist(mock)
BuildRequires:	python3dist(pbr)
BuildRequires:	python3dist(coverage)
BuildRequires:	python3dist(pycodestyle)
BuildRequires:	python3dist(pysocks)

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:	python3dist(beautifulsoup4)
Requires:	python3dist(django)
Requires:	python3dist(lxml)
Requires:	python3dist(pytz)
Requires:	python3dist(pytz)
Requires:	python3dist(setuptools)
Requires:	python3dist(simplejson)
Requires:	python3dist(six)
Requires:	python3dist(pbr)
Requires:	python3dist(coverage)
Requires:	python3dist(pycodestyle)
Requires:	python3dist(pysocks)
Requires:	python3dist(mock)

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

for lib in $(find . -type f -name "*.py"); do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%build
%py3_build

%install
%py3_install

%find_lang django
%files -n python3-%{pypi_name} -f django.lang
%license LICENSE LICENSE.3RDPARTY helpdesk/static/helpdesk/vendor/datatables/extensions/AutoFill/License.txt helpdesk/static/helpdesk/vendor/datatables/extensions/Buttons/License.txt helpdesk/static/helpdesk/vendor/datatables/extensions/ColReorder/License.txt helpdesk/static/helpdesk/vendor/datatables/extensions/FixedColumns/License.txt helpdesk/static/helpdesk/vendor/datatables/extensions/FixedHeader/License.txt helpdesk/static/helpdesk/vendor/datatables/extensions/KeyTable/License.txt helpdesk/static/helpdesk/vendor/datatables/extensions/Responsive/License.txt helpdesk/static/helpdesk/vendor/datatables/extensions/RowGroup/License.txt helpdesk/static/helpdesk/vendor/datatables/extensions/RowReorder/License.txt helpdesk/static/helpdesk/vendor/datatables/extensions/Scroller/License.txt helpdesk/static/helpdesk/vendor/datatables/extensions/Select/License.txt helpdesk/static/helpdesk/vendor/datatables/license.txt helpdesk/static/helpdesk/vendor/flot/LICENSE.txt helpdesk/static/helpdesk/vendor/jquery-ui/LICENSE.txt
%doc README.rst demo/README.rst helpdesk/static/helpdesk/vendor/datatables/Readme.md helpdesk/static/helpdesk/vendor/datatables/extensions/AutoFill/Readme.md helpdesk/static/helpdesk/vendor/datatables/extensions/Buttons/Readme.md helpdesk/static/helpdesk/vendor/datatables/extensions/ColReorder/Readme.md helpdesk/static/helpdesk/vendor/datatables/extensions/FixedColumns/Readme.md helpdesk/static/helpdesk/vendor/datatables/extensions/FixedHeader/Readme.md helpdesk/static/helpdesk/vendor/datatables/extensions/KeyTable/Readme.md helpdesk/static/helpdesk/vendor/datatables/extensions/Responsive/Readme.md helpdesk/static/helpdesk/vendor/datatables/extensions/RowGroup/Readme.md helpdesk/static/helpdesk/vendor/datatables/extensions/RowReorder/Readme.md helpdesk/static/helpdesk/vendor/datatables/extensions/Scroller/Readme.md helpdesk/static/helpdesk/vendor/datatables/extensions/Select/Readme.md helpdesk/static/helpdesk/vendor/flot/README.md helpdesk/static/helpdesk/vendor/morrisjs/README.md
%{python3_sitelib}/helpdesk
%exclude %{python3_sitelib}/helpdesk/locale
%{python3_sitelib}/django_helpdesk-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Aug 08 2020 Luis Bazan <lbazan@fedoraproject.org> - 0.2.22-2
- Fix typo changelog

* Sat Aug 08 2020 Luis Bazan <lbazan@fedoraproject.org> - 0.2.22-1
- New upstream version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.21-2
- Rebuilt for Python 3.9

* Tue Apr 21 2020 Luis Bazan <lbazan@fedoraproject.org> - 0.2.21-1
- New upstream version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 27 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.2.19-1
- New upstream version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.16-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.16-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.2.16-1
- New upstream version

* Tue Apr 23 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.2.15-3
- Fix lang locale

* Thu Mar 21 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.2.15-2
- New upstream version

* Sat Feb 16 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.2.14-1
- New Upstream version

* Mon Feb 11 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.2.13-1
- New Upstream version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.2.12-1
- New Upstream version

* Tue Dec 11 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.2.10-2
- Fix spec

* Mon Sep 03 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.2.10-1
- New upstream version

* Wed Jul 25 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.2.9-1
- New upstream version
- Fixes a javascript bug where the date formatting was incorrect

* Fri Jul 13 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.2.8-1
- New upstream version

* Wed Apr 18 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.2.7-1
- new upstream version
- change to use python3

* Tue Nov 21 2017 Luis Bazan <lbazan@fedoraproject.org> - 0.2.1-1
- new upstream version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.18-2
- Rebuild for Python 3.6

* Wed Nov 9 2016 Jan Beran <jberan@redhat.com> - 0.1.18-1
- update to patched version 0.1.18
- source update
- modernized specfile with Python 3 packaging

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 22 2014 Luis Bazan <lbazan@fedoraproject.org> - 0.1.12-4
- clean spec

* Fri Sep 19 2014 Luis Bazan <lbazan@fedoraproject.org> - 0.1.12-3
- rebuild simplejson

* Fri Sep 19 2014 Luis Bazan <lbazan@fedoraproject.org> - 0.1.12-2
- add python-simplejson 

* Sat Aug 09 2014 Luis Bazan <lbazan@fedoraproject.org> - 0.1.12-1
- New Upstream version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Luis Bazan <lbazan@fedoraproject.org> - 0.1.11-1
- New Upstream version
- remove some lines no more necessary

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 Matthias Runge <mrunge@redhat.com> - 0.1.8-4
- requires/buildrequires python-django14

* Wed Mar 27 2013 Luis Bazan <lbazan@fedoraproject.org> - 0.1.8-3
- add python macro 

* Mon Feb 18 2013 Luis Bazan <lbazan@fedoraproject.org> - 0.1.8-2
- Add pytz

* Fri Feb 15 2013 Luis Bazan <lbazan@fedoraproject.org> - 0.1.8-1
- New Upstream Version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 28 2012 Luis Bazan <lbazan@fedoraproject.org> - 0.1.7b-3
- Fix BZ 858025 comment 3
 
* Wed Sep 26 2012 Luis Bazan <lbazan@fedoraproject.org> - 0.1.7b-2
- Fix BZ 858025 comment 2

* Mon Sep 17 2012 Luis Bazan <lbazan@fedoraproject.org> - 0.1.7b-1
- Initial Import
