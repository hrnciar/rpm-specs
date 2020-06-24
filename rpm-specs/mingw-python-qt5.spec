%{?mingw_package_header}

# Disable debuginfo subpackages and debugsource packages for now to use old logic
%undefine _debugsource_packages
%undefine _debuginfo_subpackages

# Override the __debug_install_post argument as this package
# contains both native as well as cross compiled binaries
%global __debug_install_post %%{mingw_debug_install_post}; %{_rpmconfigdir}/find-debuginfo.sh %{?_missing_build_ids_terminate_build:--strict-build-id} %{?_find_debuginfo_opts} "%{_builddir}/%%{?buildsubdir}" %{nil}


%global host_py3_dir %{_builddir}/host-py3-%{name}-%{version}-%{release}
%global win32_py3_dir %{_builddir}/mingw32-py3-%{name}-%{version}-%{release}
%global win64_py3_dir %{_builddir}/mingw64-py3-%{name}-%{version}-%{release}

%global pkgname python-qt5
%global qt_ver 5.14.2

# Workaround "error: create archive failed: cpio: write failed - Cannot allocate memory"
# https://bugzilla.redhat.com/show_bug.cgi?id=1729382
%global _smp_build_nthreads 1
%global _binary_payload w13.zstdio

#define pre dev1805251538

Name:           mingw-%{pkgname}
Summary:        MinGW Windows PyQt5
Version:        5.14.2
Release:        2%{?pre:.%pre}%{?dist}

# GPLv2 exceptions(see GPL_EXCEPTIONS*.txt)
License:        (GPLv3 or GPLv2 with exceptions) and BSD
Url:            http://www.riverbankcomputing.com/software/pyqt/
# Source0:        https://www.riverbankcomputing.com/static/Downloads/PyQt5/%{version}/PyQt5-%{version}%{?pre:.%pre}.tar.gz
Source0:        https://files.pythonhosted.org/packages/4d/81/b9a66a28fb9a7bbeb60e266f06ebc4703e7e42b99e3609bf1b58ddd232b9/PyQt5-%{version}.tar.gz
# Hack in WS_WIN instead of WS_X11 in sip-flags
Patch0:         PyQt5_wswin.patch
# Tweak configure for cross build
Patch1:         PyQt5_configure.patch


BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-pyqt5-sip
BuildRequires:  python3-sip-devel

BuildRequires:  qt5-qtbase-devel >= %{qt_ver}
BuildRequires:  qt5-qtlocation-devel >= %{qt_ver}
BuildRequires:  qt5-qtmultimedia-devel >= %{qt_ver}
BuildRequires:  qt5-qtsensors-devel >= %{qt_ver}
BuildRequires:  qt5-qtserialport-devel >= %{qt_ver}
BuildRequires:  qt5-qtsvg-devel >= %{qt_ver}
BuildRequires:  qt5-qttools-devel >= %{qt_ver}
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qtxmlpatterns-devel >= %{qt_ver}
BuildRequires:  qt5-qtwebchannel-devel >= %{qt_ver}

BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-qt5-qtbase >= %{qt_ver}
BuildRequires:  mingw32-qt5-qtlocation >= %{qt_ver}
BuildRequires:  mingw32-qt5-qtmultimedia >= %{qt_ver}
BuildRequires:  mingw32-qt5-qtsensors >= %{qt_ver}
BuildRequires:  mingw32-qt5-qtserialport >= %{qt_ver}
BuildRequires:  mingw32-qt5-qtsvg >= %{qt_ver}
BuildRequires:  mingw32-qt5-qttools >= %{qt_ver}
BuildRequires:  mingw32-qt5-qtwebkit
BuildRequires:  mingw32-qt5-qtxmlpatterns >= %{qt_ver}
BuildRequires:  mingw32-qt5-qtwebchannel >= %{qt_ver}
BuildRequires:  mingw32-python3-pyqt5-sip

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-qt5-qtbase >= %{qt_ver}
BuildRequires:  mingw64-qt5-qtlocation >= %{qt_ver}
BuildRequires:  mingw64-qt5-qtmultimedia >= %{qt_ver}
BuildRequires:  mingw64-qt5-qtsensors >= %{qt_ver}
BuildRequires:  mingw64-qt5-qtserialport >= %{qt_ver}
BuildRequires:  mingw64-qt5-qtsvg >= %{qt_ver}
BuildRequires:  mingw64-qt5-qttools >= %{qt_ver}
BuildRequires:  mingw64-qt5-qtwebkit
BuildRequires:  mingw64-qt5-qtxmlpatterns >= %{qt_ver}
BuildRequires:  mingw64-python3-pyqt5-sip
BuildRequires:  mingw64-qt5-qtwebchannel >= %{qt_ver}


%description
MinGW Windows PyQt5

%package -n mingw32-python3-qt5
Summary:       MinGW Windows Python3-Qt5
Requires:      qt5-qtbase >= %{qt_ver}
Requires:      sip
Requires:      mingw32-qt5-qtbase >= %{qt_ver}
Requires:      mingw32-qt5-qttools >= %{qt_ver}
Requires:      mingw32-python3-pyqt5-sip

%description -n mingw32-python3-qt5
MinGW Windows Python3-Qt5


%package -n mingw64-python3-qt5
Summary:       MinGW Windows Python3-Qt5
Requires:      qt5-qtbase >= %{qt_ver}
Requires:      sip
Requires:      mingw64-qt5-qtbase >= %{qt_ver}
Requires:      mingw64-qt5-qttools >= %{qt_ver}
Requires:      mingw64-python3-pyqt5-sip

%description -n mingw64-python3-qt5
MinGW Windows Python3-Qt5


%{?mingw_debug_package}


%prep
%setup -q -n PyQt5-%{version}%{?pre:.%pre}

for dir in %{host_py3_dir}; do
rm -rf $dir
cp -a . $dir
pushd $dir
%patch0 -p1
popd
done

for dir in %{win32_py3_dir} %{win64_py3_dir}; do
rm -rf $dir
cp -a . $dir
pushd $dir
%patch1 -p1
popd
done


%build
pushd %{host_py3_dir}
%{__python3} configure.py \
  --assume-shared \
  --confirm-license \
  --qmake=%{_qt5_qmake} \
  --no-qsci-api \
  --verbose
%make_build
popd

pushd %{win32_py3_dir}
mingw32-python3 configure.py \
  --assume-shared \
  --confirm-license \
  --sip=/usr/bin/mingw32-sip \
  --qmake=%{mingw32_qmake_qt5} \
  --no-qsci-api \
  --verbose
%mingw32_make %{?_smp_mflags}
popd

pushd %{win64_py3_dir}
mingw64-python3 configure.py \
  --assume-shared \
  --confirm-license \
  --sip=/usr/bin/mingw64-sip \
  --qmake=%{mingw64_qmake_qt5} \
  --no-qsci-api \
  --verbose
%mingw64_make %{?_smp_mflags}
popd


%install
make install INSTALL_ROOT=%{buildroot} -C %{host_py3_dir}
%mingw32_make install INSTALL_ROOT=%{buildroot} -C %{win32_py3_dir}
%mingw64_make install INSTALL_ROOT=%{buildroot} -C %{win64_py3_dir}

# Ensure so's are executable, else they are ignored by the debuginfo extractor
find %{buildroot} -type f -name '*.so' -exec chmod +x {} \;

# Move native build to host libs
mkdir -p %{buildroot}%{_prefix}/%{mingw32_target}/lib/python%{mingw32_python3_version}/site-packages/
mkdir -p %{buildroot}%{_prefix}/%{mingw64_target}/lib/python%{mingw32_python3_version}/site-packages/
cp -a %{buildroot}%{python3_sitearch}/PyQt5 %{buildroot}%{_prefix}/%{mingw32_target}/lib/python%{mingw32_python3_version}/site-packages/PyQt5
cp -a %{buildroot}%{python3_sitearch}/PyQt5 %{buildroot}%{_prefix}/%{mingw64_target}/lib/python%{mingw32_python3_version}/site-packages/PyQt5

# Remove pylupdate, pyuic and pyrcc shell scripts
rm -f %{buildroot}%{mingw32_bindir}/py{lupdate,rcc,uic}5
rm -f %{buildroot}%{mingw64_bindir}/py{lupdate,rcc,uic}5

# Remove unused stuff
rm -rf %{buildroot}%{_libdir}
rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_datadir}

# Exclude debug files from the main files (note: the debug files are only created after %%install, so we can't search for them directly)
find %{buildroot}%{mingw32_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw32-%{pkgname}.debugfiles
find %{buildroot}%{mingw64_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw64-%{pkgname}.debugfiles


%files -n mingw32-python3-qt5 -f mingw32-%{pkgname}.debugfiles
%license LICENSE
%{_prefix}/%{mingw32_target}/lib/python%{mingw32_python3_version}/site-packages/PyQt5/
%{mingw32_python3_sitearch}/PyQt5/
%{mingw32_python3_sitearch}/PyQt5-%{version}.dist-info/
%{mingw32_libdir}/qt5/plugins/designer/pyqt5.dll
%{mingw32_libdir}/qt5/plugins/PyQt5/
%{mingw32_datadir}/sip/PyQt5


%files -n mingw64-python3-qt5 -f mingw64-%{pkgname}.debugfiles
%license LICENSE
%{_prefix}/%{mingw64_target}/lib/python%{mingw32_python3_version}/site-packages/PyQt5/
%{mingw64_python3_sitearch}/PyQt5/
%{mingw64_python3_sitearch}/PyQt5-%{version}.dist-info/
%{mingw64_libdir}/qt5/plugins/designer/pyqt5.dll
%{mingw64_libdir}/qt5/plugins/PyQt5/
%{mingw64_datadir}/sip/PyQt5


%changelog
* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 5.14.2-2
- Rebuild (python-3.9)

* Sat Apr 11 2020 Sandro Mani <manisandro@gmail.com> - 5.14.2-1
- Update to 5.14.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Sandro Mani <manisandro@gmail.com> - 5.13.2-3
- Rebuild (qt5)

* Thu Dec 12 2019 Sandro Mani <manisandro@gmail.com> - 5.13.2-2
- Rebuild (qt5)

* Tue Nov 05 2019 Sandro Mani <manisandro@gmail.com> - 5.13.2-1
- Update to 5.13.2

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 5.13.1-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Tue Oct 01 2019 Sandro Mani <manisandro@gmail.com> - 5.13.1-1
- Update to 5.13.1

* Fri Sep 27 2019 Sandro Mani <manisandro@gmail.com> - 5.13.0-3
- Rebuild (python 3.8, qt 5.12.5)

* Wed Aug 28 2019 Sandro Mani <manisandro@gmail.com> - 5.13.0-2
- Rebuild (qt5-qtwebkit)

* Mon Aug 05 2019 Sandro Mani <manisandro@gmail.com> - 5.13.0-1
- Update to 5.13.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Sandro Mani <manisandro@gmail.com> - 5.12.3-3
- Actually apply patch

* Fri Jul 19 2019 Sandro Mani <manisandro@gmail.com> - 5.12.3-2
- Backport python2 fix

* Thu Jul 18 2019 Sandro Mani <manisandro@gmail.com> - 5.12.3-1
- Update to 5.12.3

* Tue May 07 2019 Sandro Mani <manisandro@gmail.com> - 5.12.2-1
- Update to 5.12.2

* Wed May 01 2019 Sandro Mani <manisandro@gmail.com> - 5.12.1-2
- Add python3 subpackages

* Sat Apr 20 2019 Sandro Mani <manisandro@gmail.com> - 5.12.1-1
- Update to 5.12.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Sandro Mani <manisandro@gmail.com> - 5.11.3-2
- Rebuild for qt5-5.11.3

* Thu Oct 04 2018 Sandro Mani <manisandro@gmail.com> - 5.11.3-1
- Update to 5.11.3

* Mon Sep 24 2018 Sandro Mani <manisandro@gmail.com> - 5.11.2-5
- Bump qt_ver

* Sun Sep 23 2018 Sandro Mani <manisandro@gmail.com> - 5.11.2-4
- Rebuild for qt5-5.11.2

* Tue Jul 31 2018 Sandro Mani <manisandro@gmail.com> - 5.11.2-3
- Fix incorrect requires

* Sun Jul 29 2018 Sandro Mani <manisandro@gmail.com> - 5.11.2-2
- Require private PyQt5 sip modules

* Fri Jul 20 2018 Sandro Mani <manisandro@gmail.com> - 5.11.2-1
- Update to 5.11.2
- Enable qtserialport bindings

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.2-0.3.dev1805251538
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Sandro Mani <manisandro@gmail.com> - 5.10.2-0.2.dev1805251538
- Rebuild for qt5-5.11.1

* Fri Jun 01 2018 Sandro Mani <manisandro@gmail.com> - 5.10.2-0.1.dev1805251538
- Update to 5.10.2.dev1805251538

* Wed Mar 07 2018 Sandro Mani <manisandro@gmail.com> - 5.10.1-1
- Update to 5.10.1

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.com> - 5.10-5
- Add missing BR: gcc-c++, make

* Sat Feb 17 2018 Sandro Mani <manisandro@gmail.com> - 5.10-4
- Bump qt_ver to 5.10.1

* Fri Feb 16 2018 Sandro Mani <manisandro@gmail.com> - 5.10-3
- Rebuild for qt5-5.10.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Sandro mani <manisandro@gmail.com> - 5.10-1
- Update to 5.10

* Mon Jan 08 2018 Sandro Mani <manisandro@gmail.com> - 5.9.2-3
- Support Qt5 newer than just 5.9.3 (+5.9.4,5.10.0,5.10.1)

* Thu Dec 21 2017 Sandro Mani <manisandro@gmail.com> - 5.9.2-2
- Rebuild for qt5-5.10.0

* Mon Nov 27 2017 Sandro Mani <manisandro@gmail.com> - 5.9.2-1
- Update to 5.9.2

* Sat Nov 04 2017 Sandro Mani <manisandro@gmail.com> - 5.9.1-1
- Update to 5.9.1

* Wed Oct 11 2017 Sandro Mani <manisandro@gmail.com> - 5.9-6
- Also build qtlocation, qtmultimedia and qtsensor bindings

* Wed Oct 11 2017 Jan Grulich <jgrulich@redhat.com> - 5.9-5
- Bump qt_ver to 5.9.2

* Tue Sep 19 2017 Sandro Mani <manisandro@gmail.com> - 5.9-4
- Rebuild (mingw-filesystem)

* Tue Sep 05 2017 Sandro Mani <manisandro@gmail.com> - 5.9-3
- Require mingw{32,64}-qt5-qttools for directory ownership

* Wed Aug 09 2017 Sandro Mani <manisandro@gmail.com> - 5.9-2
- Bump qt_ver to 5.9.1

* Tue Jul 11 2017 Sandro Mani <manisandro@gmail.com> - 5.9-1
- Update to 5.9

* Sat May 06 2017 Sandro Mani <manisandro@gmail.com> - 5.8.2-1
- Initial package
