Name:           natural-earth-map-data
Version:        4.1.0
Release:        4%{?dist}
Summary:        Free vector and raster map data at 1:10m, 1:50m, and 1:110m scales

License:        Public Domain
URL:            http://www.naturalearthdata.com/
# Repackaged the zip as tar.xz because it saves a significant amount (~100MB).
# See repackage.sh.
#Source0:        http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/physical/110m_physical.zip
Source0:        110m_physical.tar.xz
#Source1:        http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural/110m_cultural.zip
Source1:        110m_cultural.tar.xz
#Source2:        http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/50m/physical/50m_physical.zip
Source2:        50m_physical.tar.xz
#Source3:        http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/50m/cultural/50m_cultural.zip
Source3:        50m_cultural.tar.xz
#Source4:        http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/10m_physical.zip
Source4:        10m_physical.tar.xz
#Source5:        http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/10m_cultural.zip
Source5:        10m_cultural.tar.xz
Source6:        https://github.com/nvkelso/natural-earth-vector/raw/master/LICENSE.md
BuildArch:      noarch

%global _description \
Natural Earth is a public domain map dataset available at 1:10m, 1:50m, and \
1:110 million scales. Featuring tightly integrated vector and raster data, with \
Natural Earth you can make a variety of visually pleasing, well-crafted maps \
with cartography or GIS software.

%description %{_description}


%package        110m
Summary:        Natural Earth map data - 110m resolution

%description    110m %{_description}

This provides data at 1:110m resolution.


%package        50m
Summary:        Natural Earth map data - 50m resolution

%description    50m %{_description}

This provides data at 1:50m resolution.


%package        10m
Summary:        Natural Earth map data - 10m resolution

%description    10m %{_description}

This provides data at 1:10m resolution.


%package        all
Summary:        Natural Earth map data - all resolutions
Requires:       %{name}-110m
Requires:       %{name}-50m
Requires:       %{name}-10m

%description    all %{_description}

This provides data at all resolutions.


%prep
%setup -c -T
# 110m
mkdir -p 110m/physical
tar -C 110m/physical -xf %SOURCE0
mkdir -p 110m/cultural
tar -C 110m/cultural -xf %SOURCE1
# 50m
mkdir -p 50m/physical
tar -C 50m/physical -xf %SOURCE2
mkdir -p 50m/cultural
tar -C 50m/cultural -xf %SOURCE3
# 10m
mkdir -p 10m/physical
tar -C 10m/physical -xf %SOURCE4
# One has to be different...
#mkdir -p 10m/cultural
tar -C 10m -xf %SOURCE5
mv 10m/10m_cultural 10m/cultural
mv 10m/{README.md,CHANGELOG,VERSION} 10m/cultural
cp -p %SOURCE6 .


%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_pkgdocdir}
for theme in physical cultural; do
    mkdir -p %{buildroot}%{_datadir}/%{name}/${theme}
    for scale in 110m 50m 10m; do
        chmod -x ${scale}/${theme}/ne_${scale}_*
        cp -a ${scale}/${theme}/ne_${scale}_* %{buildroot}%{_datadir}/%{name}/${theme}
        for docfile in README.md CHANGELOG VERSION; do
            cp -a ${scale}/${theme}/${docfile} %{buildroot}%{_pkgdocdir}/${scale}-${theme}-${docfile}
        done
    done
done


%files 110m
%license LICENSE.md
%dir %{_pkgdocdir}
%{_pkgdocdir}/110m-*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/physical/
%{_datadir}/%{name}/physical/ne_110m_*
%dir %{_datadir}/%{name}/cultural/
%{_datadir}/%{name}/cultural/ne_110m_*


%files 50m
%license LICENSE.md
%dir %{_pkgdocdir}
%{_pkgdocdir}/50m-*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/physical/
%{_datadir}/%{name}/physical/ne_50m_*
%dir %{_datadir}/%{name}/cultural/
%{_datadir}/%{name}/cultural/ne_50m_*


%files 10m
%license LICENSE.md
%dir %{_pkgdocdir}
%{_pkgdocdir}/10m-*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/physical/
%{_datadir}/%{name}/physical/ne_10m_*
%dir %{_datadir}/%{name}/cultural/
%{_datadir}/%{name}/cultural/ne_10m_*


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.1.0-1
- Update to latest version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.0.0-2
- Add license file to package.
- Use more-compressed source files.

* Thu Feb 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.0.0-1
- Initial package
