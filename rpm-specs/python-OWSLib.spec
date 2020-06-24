# Works with either ElementTree or python-lxml
%global modname OWSLib

Name:           python-%{modname}
Version:        0.20.0
Release:        1%{?dist}
Summary:        Client library for OGC web services
License:        BSD
URL:            https://geopython.github.io/OWSLib
Source0:        https://files.pythonhosted.org/packages/source/O/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description\
Package for client programming with Open Geospatial Consortium (OGC) web\
service (hence OWS) interface standards, and their related content models.

%description %_description

%package -n python3-OWSLib
Summary:        Client library for OGC web services

Requires:       python3-dateutil
Requires:       python3-pyproj
Requires:       python3-pytz
Requires:       python3-requests

%description -n python3-OWSLib
Package for client programming with Open Geospatial Consortium (OGC) web
service (hence OWS) interface standards, and their related content models.

%prep
%setup -q -n %{modname}-%{version}
rm -rf %{modname}.egg-info

find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'


%build
%py3_build


%install
%py3_install


%files -n python3-OWSLib
%doc README.rst CHANGES.rst AUTHORS.rst
# TODO: Add LICENSE on the next release after 0.17.0
%{python3_sitelib}/owslib
%{python3_sitelib}/%{modname}-%{version}-py*.egg-info

%changelog
* Fri Jun 05 2020 Volker Fröhlich <volker27@gmx.at> - 0.20.0-1
- New upstream release

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.19.1-2
- Rebuilt for Python 3.9

* Sun Feb 02 2020 Volker Fröhlich <volker27@gmx.at> - 0.19.1-1
- New upstream release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Volker Fröhlich <volker27@gmx.at> - 0.19.0-1
- New upstream release

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Volker Fröhlich <volker27@gmx.at> - 0.18.0-1
- New upstream release

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 0.17.0-3
- Subpackage python2-owslib has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Volker Fröhlich <volker27@gmx.at> - 0.17.0-1
- New upstream release
- Update names of documentation files

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.16.0-4
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.16.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 22 2017 Volker Fröhlich <volker27@gmx.at> - 0.16.0-1
- New upstream release

* Thu Sep 14 2017 Volker Fröhlich <volker27@gmx.at> - 0.15.0-1
- New upstream release

* Tue Aug 29 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.14.0-5
- Add Provides for the old name

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.14.0-4
- Python 2 binary package renamed to python2-owslib
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Volker Fröhlich <volker27@gmx.at> - 0.14.0-1
- New upstream release

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-2
- Rebuild for Python 3.6

* Sun Sep 25 2016 Volker Fröhlich <volker27@gmx.at> - 0.13.0-1
- New upstream release

* Tue Sep 13 2016 Volker Fröhlich <volker27@gmx.at> - 0.12.0-1
- New upstream release
- Update URL and Source

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 16 2016 Volker Fröhlich <volker27@gmx.at> - 0.11.2-1
- New upstream release

* Sat May 14 2016 Volker Fröhlich <volker27@gmx.at> - 0.11.1-1
- New upstream release

* Fri Apr  1 2016 Volker Fröhlich <volker27@gmx.at> - 0.11.0-1
- New upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Volker Fröhlich <volker27@gmx.at> - 0.10.3-1
- New upstream release

* Sun Nov 22 2015 Volker Fröhlich <volker27@gmx.at> - 0.10.1-1
- New upstream release

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Nov 11 2015 Volker Fröhlich <volker27@gmx.at> - 0.10.0-1
- New upstream release

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Sep 25 2015 Volker Fröhlich <volker27@gmx.at> - 0.9.2-1
- New upstream release

* Sun Sep  6 2015 Volker Fröhlich <volker27@gmx.at> - 0.9.1-2
- Add pyproj dependency

* Sun Sep  6 2015 Volker Fröhlich <volker27@gmx.at> - 0.9.1-1
- New upstream release

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 13 2015 Volker Fröhlich <volker27@gmx.at> - 0.9.0-1
- New upstream release
- Add Python 3 sub-package

* Sat Feb 14 2015 Volker Fröhlich <volker27@gmx.at> - 0.8.13-1
- New upstream release

* Tue Dec 23 2014 Volker Fröhlich <volker27@gmx.at> - 0.8.12-1
- New upstream release

* Wed Dec 17 2014 Volker Fröhlich <volker27@gmx.at> - 0.8.11-1
- New upstream release

* Mon Oct 13 2014 Volker Fröhlich <volker27@gmx.at> - 0.8.10-1
- New upstream release

* Wed Sep 24 2014 Volker Fröhlich <volker27@gmx.at> - 0.8.9-1
- New upstream release

* Mon Jul  7 2014 Volker Fröhlich <volker27@gmx.at> - 0.8.8-1
- New upstream release

* Wed Jul  2 2014 Volker Fröhlich <volker27@gmx.at> - 0.8.7-3
- Changed package summary

* Tue Jul  1 2014 Volker Fröhlich <volker27@gmx.at> - 0.8.7-2
- Correct BR python-setuptools-devel to python-setuptools

* Mon Jun 30 2014 Volker Fröhlich <volker27@gmx.at> - 0.8.7-1
- Initial package for Fedora
