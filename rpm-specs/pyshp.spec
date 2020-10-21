Name:           pyshp
Version:        2.1.2
Release:        1%{?dist}
Summary:        Pure Python read/write support for ESRI Shapefile format
License:        MIT
URL:            https://github.com/GeospatialPython/pyshp
Source0:        https://github.com/GeospatialPython/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildArch:      noarch

%package -n python3-%{name}
Summary:        Pure Python 3 read/write support for ESRI Shapefile format

%description
Pure Python read/write support for ESRI Shapefile format

%description -n python3-%{name}
Pure Python 3 read/write support for ESRI Shapefile format

%prep
%setup -q

# Change line endings, otherwise doctest fails
# Remaining tests should only fail due to missing test data
sed -i 's/.$//' changelog.txt

# Delete the egg info to certainly ship the generated
rm -rf pyshp.egg-info


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --skip-build --root %{buildroot}


%check
%{__python3} shapefile.py


%files -n python3-%{name}
%doc README.md changelog.txt LICENSE.TXT
%{python3_sitelib}/shapefile.py*
%{python3_sitelib}/%{name}-%{version}-py*.egg-info
%{python3_sitelib}/__pycache__/shapefile*


%changelog
* Fri Sep 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.1.2-1
- 2.1.2

* Thu Sep 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.1.1-1
- 2.1.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Volker Fröhlich <volker27@gmx.at> - 2.1.0-1
- New upstream release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 04 2018 Volker Fröhlich <volker27@gmx.at> - 2.0.1-1
- New upstream release
- Drop python2 sub-package

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.12-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.12-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 25 2017 Volker Fröhlich <volker27@gmx.at> - 1.2.12-1
- New upstream release

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.11-3
- Python 2 binary package renamed to python2-pyshp
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 30 2017 Volker Fröhlich <volker27@gmx.at> - 1.2.11-1
- New upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.10-2
- Rebuild for Python 3.6

* Sun Sep 25 2016 Volker Fröhlich <volker27@gmx.at> - 1.2.10-1
- New upstream release

* Tue Aug 30 2016 Volker Fröhlich <volker27@gmx.at> - 1.2.5-2
- Add LICENSE.TXT to cp

* Mon Aug 29 2016 Volker Fröhlich <volker27@gmx.at> - 1.2.5-1
- New upstream release
- Add license file, change README extension

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Jun 22 2015 Volker Fröhlich <volker27@gmx.at> - 1.2.3-1
- New upstream release
- Modernize the process of constructing a Python 3 sub-package
- Ship README and changelog with both packages
- Update homepage and source URL

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon May 12 2014 Volker Fröhlich <volker27@gmx.at> - 1.2.1-1
- New upstream release
- Properly check on Python 3 builds

* Thu Jan 23 2014 Volker Fröhlich <volker27@gmx.at> - 1.2.0-2
- Disable Python 3 builds for EPEL7 until Python 3 is available there

* Sun Oct 06 2013 Volker Fröhlich <volker27@gmx.at> - 1.2.0-1
- New upstream release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.1.4-5
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 19 2012 Volker Fröhlich <volker27@gmx.at> - 1.1.4-3
- Move BR python3-devel in conditional block

* Fri May 18 2012 Volker Fröhlich <volker27@gmx.at> - 1.1.4-2
- Run doctests
- Delete the original egg-info

* Sun Apr 22 2012 Volker Fröhlich <volker27@gmx.at> - 1.1.4-1
- Initial package for Fedora
