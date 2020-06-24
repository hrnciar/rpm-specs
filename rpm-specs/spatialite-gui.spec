Name:           spatialite-gui
Version:        1.7.1
Release:        23%{?dist}
Summary:        GUI to manage Spatialite databases

License:        GPLv3+
URL:            https://www.gaia-gis.it/fossil/spatialite_gui
Source0:        http://www.gaia-gis.it/gaia-sins/spatialite_gui-%{version}.tar.gz
# Link agains wx aui
Patch1:         %{name}-1.7.0-aui_linking.patch

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  freexl-devel
BuildRequires:  libspatialite-devel
BuildRequires:  libgaiagraphics-devel
BuildRequires:  libxml2-devel
BuildRequires:  compat-wxGTK3-gtk2-devel
BuildRequires:  sqlite-devel
BuildRequires:  geos-devel
BuildRequires:  proj-devel

%description
GUI to manage Spatialite databases.


%prep
%autosetup -p1 -n spatialite_gui-%{version}

# Delete shebang from desktop file
sed -i '1d' gnome_resource/%{name}.desktop


%build
export CFLAGS="%{optflags} -DACCEPT_USE_OF_DEPRECATED_PROJ_API_H"
export LDFLAGS="%{__global_ldflags} -lsqlite3"

%configure
%make_build


%install
%make_install

# Install icon and desktop file
install -Dpm 0644 gnome_resource/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    gnome_resource/%{name}.desktop


%files
%doc AUTHORS
%license COPYING
%{_bindir}/spatialite_gui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
* Tue Apr 14 2020 Sandro Mani <manisandro@gmail.com> - 1.7.1-23
- Fix FTBFS
- Modernize spec
- Drop ExcludeArch

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.7.1-20
- rebuilt (proj)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Volker Fröhlich <volker27@gmx.at> - 1.7.1-17
- Build with compat-wxGTK3-gtk2 instead of wxGTK3
  Regular crashes were reported and this is the author's suggestion.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 03 2017 Volker Froehlich <volker27@gmx.at> - 1.7.1-13
- Rebuild for gtk3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Volker Froehlich <volker27@gmx.at> - 1.7.1-11
- Rebuild for libproj

* Tue Dec 20 2016 Volker Froehlich <volker27@gmx.at> - 1.7.1-10
- Correct linking issues with sqlite3 and wx aui

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.7.1-7
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar 14 2015 Volker Froehlich <volker27@gmx.at> - 1.7.1-6
- Rebuild for proj 4.9.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 25 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.7.1-4
- rebuild (libspatialite)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul  1 2013 Volker Fröhlich <volker27@gmx.at> 1.7.1-1
- New upstream release

* Tue Jun  4 2013 Volker Fröhlich <volker27@gmx.at> 1.7.0-1
- New upstream release
- Drop geos linking patch (solved upstream)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan  6 2013 Volker Fröhlich <volker27@gmx.at> 1.6.0-1
- New upstream release
- Patch missing linking instruction

* Sun Dec  2 2012 Bruno Wolff III <bruno@wolff.to> 1.5.0-5
- Rebuild for libspatialite soname bump

* Fri Aug 10 2012 Volker Fröhlich <volker27@gmx.at> 1.5.0-4
- Exclude ppc

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul  6 2012 Volker Fröhlich <volker27@gmx.at> 1.5.0-2
- Add forgotten BR freexl-devel

* Wed Jan 11 2012 Volker Fröhlich <volker27@gmx.at> 1.5.0-1
- Update for new release
- Update URL and source URL
- Correct license to GPLv3+
- Drop patch for wxwidget (solved)
- Use upstreams desktop file and icon
- Don't modify linker flags anymore (solved)

* Mon Jan  9 2012 Volker Fröhlich <volker27@gmx.at> 1.4.0-3
- Exclude ppc64 architecture

* Sun Jan  8 2012 Volker Fröhlich <volker27@gmx.at> 1.4.0-2
- Remove post and postun sections with useless ldconfig

* Sun Dec  4 2011 Volker Fröhlich <volker27@gmx.at> 1.4.0-1
- Initial packaging 
