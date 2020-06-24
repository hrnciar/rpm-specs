Name:           PyMca
Version:        5.5.0
Release:        5%{?dist}
Summary:        X-ray Fluorescence Toolkit
License:        GPLv2+
URL:            http://pymca.sourceforge.net/
%if 0
Original source: http://downloads.sourceforge.net/sourceforge/pymca/pymca%%{version}-src.tgz
However it bundles a copy of the "sift" module which implements a patented algorithm.
The algorithm can be used for non-commercial research purposes ONLY. Per:
http://fedoraproject.org/wiki/Packaging:SourceURL#When_Upstream_uses_Prohibited_Code
we must remove them before uploading:
  ./getsources.sh %{version}
%endif
Source0:        pymca-%{version}-filtered.tar.xz
Source1:        PyMca.desktop
Source2:        edfviewer.desktop
Source3:        elementsinfo.desktop
Source4:        mca2edf.desktop
Source5:        peakidentifier.desktop
Source6:        pymcabatch.desktop
Source7:        pymcapostbatch.desktop
Source8:        pymcaroitool.desktop
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %py3_dist cython
BuildRequires:  %py3_dist numpy
BuildRequires:  python3-PyQt4
BuildRequires:  %py3_dist fisx
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  qhull-devel
BuildRequires:  %py3_dist h5py
Requires:       hicolor-icon-theme
Requires:       %{name}-data = %{version}-%{release}

%description
PyMCA provides a graphical interface for multi-channel analyzer spectra
visualization and analysis. PyMca can display spectra from a file or directly
from SPEC during acquisitions.

%package        data
Summary:        Data files for %{name}
BuildArch:      noarch

%description    data
This package contains photon interaction data/elements data for %{name}.

%prep
%autosetup -p1 -n pymca-%{version}

# Drop bundled qhull.
rm -frv third-party/
# Patch for the craps qhull brings in.
sed -i -e 's|"geom.h"|<geom.h>|'      \
       -e 's|"libqhull.h"|<libqhull.h>|' \
       -e 's|"poly.h"|<poly.h>|'      \
       -e 's|"qset.h"|<qset.h>|'      \
       PyMca5/Object3D/Object3DQhull/Object3DQhull.c

# Fix wrong shebang of pymcapostbatch.
sed -i "s|!python|!%{__python3}|g" PyMca5/scripts/pymcapostbatch

%build
# Need to define manually. Note using pkg-config to export the cflags
# is not identified by the setup.py script as it requires non-blank
# stdin for both CFLAGS/LDFLAGS, so we manually define the CFLAGS.
QHULL_CFLAGS="-I%{_includedir}/libqhull" \
QHULL_LIBS="-lqhull" \
SPECFILE_USE_GNU_SOURCE=1 \
PYMCA_DATA_DIR=/usr/share/PyMca \
PYMCA_DOC_DIR=/usr/share/doc/PyMca \
%py3_build

%install
PYMCA_DATA_DIR=/usr/share/PyMca \
PYMCA_DOC_DIR=/usr/share/doc/PyMca \
%py3_install

# Install desktop file.
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:1}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:2}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:3}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:4}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:5}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:6}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:7}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:8}

# Merge applications into one software center item
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/edfviewer.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="desktop">
  <metadata_license>CC0-1.0</metadata_license>
  <id>edfviewer.desktop</id>
  <metadata>
    <value key="X-Merge-With-Parent">PyMca.desktop</value>
  </metadata>
</component>
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/elementsinfo.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="desktop">
  <metadata_license>CC0-1.0</metadata_license>
  <id>elementsinfo.desktop</id>
  <metadata>
    <value key="X-Merge-With-Parent">PyMca.desktop</value>
  </metadata>
</component>
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/mca2edf.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="desktop">
  <metadata_license>CC0-1.0</metadata_license>
  <id>mca2edf.desktop</id>
  <metadata>
    <value key="X-Merge-With-Parent">PyMca.desktop</value>
  </metadata>
</component>
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/peakidentifier.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="desktop">
  <metadata_license>CC0-1.0</metadata_license>
  <id>peakidentifier.desktop</id>
  <metadata>
    <value key="X-Merge-With-Parent">PyMca.desktop</value>
  </metadata>
</component>
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/pymcabatch.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="desktop">
  <metadata_license>CC0-1.0</metadata_license>
  <id>pymcabatch.desktop</id>
  <metadata>
    <value key="X-Merge-With-Parent">PyMca.desktop</value>
  </metadata>
</component>
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/pymcapostbatch.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="desktop">
  <metadata_license>CC0-1.0</metadata_license>
  <id>pymcapostbatch.desktop</id>
  <metadata>
    <value key="X-Merge-With-Parent">PyMca.desktop</value>
  </metadata>
</component>
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/pymcaroitool.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="desktop">
  <metadata_license>CC0-1.0</metadata_license>
  <id>pymcaroitool.desktop</id>
  <metadata>
    <value key="X-Merge-With-Parent">PyMca.desktop</value>
  </metadata>
</component>
EOF

# Convert to various sizes, via the 256x256 source.
for size in 192x192 128x128 96x96 72x72 64x64 48x48 40x40 36x36 32x32 26x26 24x24 22x22 16x16 ; do
    install -pdm755 \
        %{buildroot}%{_datadir}/icons/hicolor/${size}/apps
    convert -resize ${size} icons/PyMca_256x256.png \
        %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/%{name}.png
done

# Get rid of spurious executable rights.
find %{buildroot}%{python3_sitearch}/PyMca5/ -type f -exec chmod 644 {} +
find %{buildroot}%{python3_sitearch}/PyMca5/ -name *.so -exec chmod 755 {} +

# Get rid of /usr/bin/env in libraries.
find %{buildroot}%{python3_sitearch}/PyMca5 -type f -name '*.py' \
     -exec sed -i '/\/usr\/bin\/env/d' {} + \
     -exec touch -r setup.py {} +

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} \
PYMCA_DATA_DIR=%{buildroot}/usr/share/PyMca \
PYMCA_DOC_DIR=%{buildroot}/usr/share/doc/PyMca \
%{__python3} PyMca5/tests/TestAll.py

%files
%license LICENSE.GPL
%doc changelog.txt README.rst
%{_bindir}/edfviewer
%{_bindir}/elementsinfo
%{_bindir}/mca2edf
%{_bindir}/peakidentifier
%{_bindir}/pymca*
%{_bindir}/rgbcorrelator
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_mandir}/man1/*.1*
%{python3_sitearch}/PyMca5/
%{python3_sitearch}/PyMca5-%{version}-py%{python3_version}.egg-info
%exclude %{_pkgdocdir}

%files data
%{_datadir}/%{name}/
%{_pkgdocdir}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.5.0-5
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 5.5.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.5.0-2
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl>
- Drop dependency on PyQwt, it is not necessary anymore (#1724456)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.4.3-1
- Update to latest version (#1198140)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.7.3-11
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.3-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Apr 29 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.7.3-6
- Rebuild for qhull-2015.2-1.
- Reflect qhull.h/libqhull.h's location having changed.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 4.7.3-3
- Add an AppData file for the software center

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 04 2014 Christopher Meng <rpm@cicku.me> - 4.7.3-1
- Update to 4.7.3

* Wed Jun 18 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 4.5.0-6
- Fix FTBFS with -Werror=format-security (#1105919)
- Cleanup spec

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 24 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.0-1
- Update to 4.5.0.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.1-5.p1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.4.1-4.p1
- Fix binary permissions (BZ #721149).

* Fri Feb 25 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.4.1-3.p1
- Update to 4.4.1p1.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 10 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.4.1-1
- Update to 4.4.1.

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jun 19 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.4.0-1
- Update to 4.4.0.

* Fri Oct 30 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.3.0-4
- Keep time stamps also on binfiles.

* Fri Oct 30 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.3.0-3
- Added BR: python-devel.
- Added desktop file.

* Fri Oct 30 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.3.0-2
- Keep time stamps during sed of libraries.
- Changed BR: python-setuptools-devel to python-setuptools-devel.

* Thu Oct 08 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.3.0-1
- First release.
