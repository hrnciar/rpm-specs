
Name:       marble-subsurface
Summary:    Marble Subsurface branch
Version:    4.6.2
Release:    9%{?dist}

License:    LGPLv2+
URL:        http://git.subsurface-divelog.org/index.cgi?p=marble.git
Source0:    http://subsurface-divelog.org/downloads/marble-subsurface-branch-%{version}.tgz

BuildRequires: extra-cmake-modules
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qtwebkit-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qttools-devel

%description
A modified version of marble for Subsurface.

%package -n libssrfmarblewidget
Summary:       A modified version of libmarblewidget for Subsurface
# try to share, else we can keep private copy of data too -- rex
Requires:      marble-widget-data
%description -n libssrfmarblewidget
%{summary}.

%package -n libssrfmarblewidget-devel
Summary: Development files for libssrfmarblewidget
Conflicts: marble-widget-devel
Conflicts: marble-widget-qt5-devel
Requires: libssrfmarblewidget%{?_isa} = %{version}-%{release}
%description -n libssrfmarblewidget-devel
%{summary}.


%prep
%autosetup -n marble-subsurface-branch-%{version}

# skip data (for now), try to share marble-widget-data
sed -i -e 's|add_subdirectory(data)|#add_subdirectory(data)|g' CMakeLists.txt


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake} .. \
  -DBUILD_MARBLE_APPS:BOOL=OFF \
  -DBUILD_MARBLE_TESTS:BOOL=OFF \
  -DBUILD_TESTING:BOOL=OFF \
  -DMARBLE_DATA_PATH:PATH="%{_datadir}/marble/data" \
  -DQT5BUILD:BOOL=ON \
  -DQTONLY:BOOL=ON \
  -DWITH_DESIGNER_PLUGIN:BOOL=OFF
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

## unpackaged files
rm -rfv %{buildroot}%{_datadir}/appdata/
rm -rfv %{buildroot}%{_datadir}/marble/data/
rm -rfv %{buildroot}%{_libdir}/libastro*
rm -rfv %{buildroot}%{_includedir}/astro/


%ldconfig_scriptlets -n libssrfmarblewidget

%files -n libssrfmarblewidget
%doc CREDITS BUGS
%license LICENSE.GPL-3 LICENSE.txt
%{_libdir}/libssrfmarblewidget.so.*

%files -n libssrfmarblewidget-devel
%{_datadir}/marble/cmake/FindMarble.cmake
%{_includedir}/marble/
%{_libdir}/libssrfmarblewidget.so


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Feb 21 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.6.2-1
- 4.6.2

* Tue Feb 07 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.6.0-1
- 4.6.0

* Wed Nov 11 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 4.5.2-1
- Update to 4.5.2

* Wed Nov 04 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 4.5.1-1
- Update to 4.5.1

* Wed Sep 02 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.21.3-1
- Initial packaging effort for Fedora

