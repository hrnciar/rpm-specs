# Use devtoolset 8
%if 0%{?rhel} && 0%{?rhel} == 7
%global dts devtoolset-8-
%endif

Name:           avogadro2
Version:        1.93.0
Release:        4%{?dist}
Summary:        Advanced molecular editor
License:        BSD
URL:            http://avogadro.openmolecules.net/
Source0:        https://github.com/OpenChemistry/avogadroapp/archive/%{version}/avogadroapp-%{version}.tar.gz
Source1:        %{name}.appdata.xml

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif
BuildRequires:  cmake3
BuildRequires:  chrpath, desktop-file-utils
BuildRequires:  avogadro2-libs-devel >= %{version}
BuildRequires:  molequeue-devel, spglib-devel
BuildRequires:  %{?dts}gcc, %{?dts}gcc-c++, doxygen
BuildRequires:  eigen3-devel, hdf5-devel, glew-devel
BuildRequires:  qt5-qtbase-devel, qt5-qttools-devel
%if 0%{?fedora}
BuildRequires:  libappstream-glib
%endif

Requires: python%{python3_pkgversion}
Requires: openbabel%{?_isa}
Requires: avogadro2-libs%{?_isa} >= %{version}

%description
Avogadro is an advanced molecular editor designed for cross-platform use in
computational chemistry, molecular modeling, bioinformatics, materials science,
and related areas. It offers flexible rendering and a powerful plugin
architecture. The code in this repository is a rewrite of Avogadro with source
code split across a libraries repository and an application repository. Core
features and goals of the Avogadro project:

* Open source distributed under the liberal 3-clause BSD license
* Cross platform with nightly builds on Linux, Mac OS X and Windows
* Intuitive interface designed to be useful to whole community
* Fast and efficient embracing the latest technologies
* Extensible, making extensive use of a plugin architecture
* Flexible supporting a range of chemical data formats and packages

%prep
%autosetup -n avogadroapp-%{version}

%build
mkdir build && pushd build
%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%endif
export LDFLAGS="%{__global_ldflags} -Wl,--as-needed"
export CFLAGS="%{optflags} -I%{_includedir}/%{name}"
export CXXFLAGS="%{optflags} -I%{_includedir}/%{name}"
%cmake3 -DCMAKE_BUILD_TYPE:STRING=Release \
 -Wno-dev \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
 -DENABLE_RPATH:BOOL=ON \
 -DENABLE_TESTING:BOOL=OFF \
 -DAvogadroLibs_DIR:PATH=%{_libdir} \
 -DBUILD_DOCUMENTATION:BOOL=ON ..
%make_build

%install
%make_install -C build
rm -rf %{buildroot}%{_datadir}/doc

chrpath -d %{buildroot}%{_bindir}/%{name}

desktop-file-edit --set-key=Exec --set-value='env LD_LIBRARY_PATH=%{_libdir}/%{name} %{name} %f' \
 --set-key=Icon --set-value=%{_datadir}/icons/%{name}/avogadro2_128.png \
 %{buildroot}%{_datadir}/applications/%{name}.desktop

mkdir -p %{buildroot}%{_datadir}/icons/%{name}
cp -a avogadro/icons/* %{buildroot}%{_datadir}/icons/%{name}/

%if 0%{?fedora}
## Install appdata file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}/
%endif

%if 0%{?rhel}
%post
/bin/touch --no-create %{_datadir}/icons/%{name} &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/%{name} &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :
%endif

%check
%if 0%{?fedora}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/*.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/%{name}/

%changelog
* Sat Feb 29 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.93.0-4
- New rebuild

* Fri Feb 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.93.0-3
- Add avogadro2-libs runtime dependency

* Fri Feb 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.93.0-2
- New rebuild

* Sun Feb 09 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.93.0-1
- Release 1.93.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.91.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.91.0-5
- Rebuild for spglib-1.14.1
- Use devtools-8 on EPEL7
- Use CMake3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.91.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 1.91.0-3
- Rebuild for hdf5 1.10.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.91.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 24 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.91.0-1
- Release 1.91.0

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.90.0-14.20180713git74e1ede
- Rebuilt for glew 2.1.0

* Sun Jul 15 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-13.20180713git74e1ede
- Update to commit #74e1ede

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-10
- Rebuild for moloqueue-0.9.0
- Rebuild for GCC-8

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.90.0-9
- Remove obsolete scriptlets

* Thu Dec 21 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-8
- Appdata file moved into metainfo data directory

* Thu Dec 14 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-7
- Rebuild for spglib-1.10.2

* Fri Sep 08 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-6
- Require OpenBabel (bz#1489749)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-3
- Modified for epel7 builds

* Tue Apr 25 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-2
- Add appdata file

* Sat Mar 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-1
- Initial package
