%global srcname cartopy
%global Srcname Cartopy

# Some tests use the network.
%bcond_with network

Name:           python-%{srcname}
Version:        0.18.0
Release:        2%{?dist}
Summary:        Cartographic Python library with Matplotlib visualisations

License:        LGPLv3
URL:            http://scitools.org.uk/cartopy/docs/latest/
Source0:        %pypi_source %{Srcname}
# Set location of Fedora-provided pre-existing data.
Source1:        siteconfig.py
# Might not go upstream in current form.
Patch0004:      0001-Increase-tolerance-for-new-FreeType.patch

BuildRequires:  gcc-c++
BuildRequires:  geos-devel >= 3.3.3
BuildRequires:  proj-devel >= 4.9.0

%global _description \
Cartopy is a Python package designed to make drawing maps for data analysis \
and visualisation easy. It features: \
* object oriented projection definitions \
* point, line, polygon and image transformations between projections \
* integration to expose advanced mapping in matplotlib with a simple and \
  intuitive interface \
* powerful vector data handling by integrating shapefile reading with Shapely \
  capabilities

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython >= 0.15.1
BuildRequires:  python3-six >= 1.3.0
BuildRequires:  python3-numpy >= 1.10
BuildRequires:  python3-shapely >= 1.5.6
BuildRequires:  python3-pyshp >= 1.1.4
# OWS requirements
BuildRequires:  python3-OWSLib >= 0.8.11
BuildRequires:  python3-pillow >= 1.7.8
# Plotting requirements
BuildRequires:  python3-matplotlib >= 1.5.1
BuildRequires:  gdal-python3 >= 1.10.0
BuildRequires:  python3-pillow >= 1.7.8
BuildRequires:  python3-pykdtree >= 1.2.2
BuildRequires:  python3-scipy >= 0.10
# Testing requirements
BuildRequires:  python3-filelock
BuildRequires:  python3-mock >= 1.0.1
BuildRequires:  python3-pytest >= 3.1.0

Requires:       python-%{srcname}-common = %{version}-%{release}
Requires:       python3-setuptools >= 0.7.2
Requires:       python3-six >= 1.3.0
Requires:       python3-numpy >= 1.10
Requires:       python3-shapely >= 1.5.6
Requires:       python3-pyshp >= 1.1.4
# OWS requirements
Recommends:     python3-OWSLib >= 0.8.11
Recommends:     python3-pillow >= 1.7.8
# Plotting requirements
Recommends:     python3-matplotlib >= 1.5.1
Recommends:     gdal-python3 >= 1.10.0
Recommends:     python3-pillow >= 1.7.8
Recommends:     python3-pykdtree >= 1.2.2
Recommends:     python3-scipy >= 0.10

%description -n python3-%{srcname} %{_description}


%package -n     python-%{srcname}-common
Summary:        Data files for %{srcname}
BuildArch:      noarch

BuildRequires:  natural-earth-map-data-110m
BuildRequires:  natural-earth-map-data-50m

Recommends:     natural-earth-map-data-110m
Suggests:       natural-earth-map-data-50m
Suggests:       natural-earth-map-data-10m

%description -n python-%{srcname}-common
Data files for %{srcname}.


%prep
%autosetup -n %{Srcname}-%{version} -p1
cp -a %SOURCE1 lib/cartopy/

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install

mkdir -p %{buildroot}%{_datadir}/cartopy/shapefiles/natural_earth/
for theme in physical cultural; do
    ln -s %{_datadir}/natural-earth-map-data/${theme} \
        %{buildroot}%{_datadir}/cartopy/shapefiles/natural_earth/${theme}
done


%check
%if %{with network}
PYTHONPATH="%{buildroot}%{python3_sitearch}" PYTHONDONTWRITEBYTECODE=1 MPLBACKEND=Agg \
    pytest-3 --doctest-modules --pyargs cartopy
%else
PYTHONPATH="%{buildroot}%{python3_sitearch}" PYTHONDONTWRITEBYTECODE=1 MPLBACKEND=Agg \
    pytest-3 --doctest-modules --pyargs cartopy -m "not network"
%endif


%files -n python-%{srcname}-common
%doc README.md
%license COPYING COPYING.LESSER lib/cartopy/data/LICENSE
%{_datadir}/cartopy/

%files -n python3-%{srcname}
%{python3_sitearch}/cartopy
%{python3_sitearch}/%{Srcname}-%{version}-py*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.18.0-2
- Rebuilt for Python 3.9

* Mon May 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.18.0-1
- Update to latest version

* Fri May 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.18.0~rc1-1
- Update to latest release candidate

* Mon Apr 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.18.0~b2-1
- Update to latest beta

* Mon Feb 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.18.0~b1-1
- Update to latest beta

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.17.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.17.0-5
- Fix build against FreeType 2.10.0

* Tue Feb 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.17.0-4
- Rebuilt for updated Proj

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 06 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.17.0-2
- Remove pytest bytecode

* Sat Nov 17 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.17.0-1
- Update to latest version
- Remove workaround for unpackaged Natural Earth data
- Drop Python 2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.16.0-5
- Add explicit gcc-c++ BR

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.16.0-4
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.16.0-3
- Drop patch for old versions of Matplotlib.
- Use python2- prefix for dependencies.

* Sun Feb 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.16.0-2
- Enable testing with now-packaged Natural Earth data.

* Fri Feb 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.16.0-1
- Initial package.
