%global commit f82e052f62c5746c2d6ae9667c3ad7315e08acfb
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           ogr2osm
Version:        0.1
Release:        0.8.20200130gitf82e052%{?dist}
Summary:        Convert ogr-readable files like shapefiles into .osm data

License:        MIT
URL:            https://github.com/pnorman/ogr2osm/
Source0:        https://github.com/pnorman/ogr2osm/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
Requires:       python3-gdal

%description
ogr2osm will read any data source that ogr can read and handle reprojection
for you. It takes a python file to translate external data source tags into
OSM tags, allowing you to use complicated logic. If no translation is
specified it will use an identity translation, carrying all tags from the
source to the .osm output.


%prep
%autosetup -n %{name}-%{commit}

# Remove shebang from non executable scripts
sed -i -e '/^#!\//, 1d' *.py


%build
%py3_build


%install
%py3_install 


%files
%{_bindir}/%{name}
%{python3_sitelib}/ogr2osm*
%{python3_sitelib}/geom.py
%{python3_sitelib}/__pycache__/*
%doc README.md


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.8.20200130gitf82e052
- Rebuilt for Python 3.9

* Wed Feb 05 2020 Andrea Musuruane <musuruan@gmail.com> - 0.1-0.7.20200130gitf82e052
- Updated to new upstream snapshot

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.6.20191023git1b9cc00
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Andrea Musuruane <musuruan@gmail.com> - 0.1-0.5.20191023git1b9cc00
- Updated to new upstream snapshot

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.4.20190104git183e226
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.3.20190104git183e226
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.2.20190104git183e226
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr  6 2019 Andrea Musuruane <musuruan@gmail.com> - 0.1-0.1.20190104git183e226
- First release

