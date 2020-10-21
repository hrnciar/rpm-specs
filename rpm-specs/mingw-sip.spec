%global win32_dir %{_builddir}/mingw32-%{name}-%{version}-%{release}
%global win64_dir %{_builddir}/mingw64-%{name}-%{version}-%{release}
%global win32_host_dir %{_builddir}/mingw32-host-%{name}-%{version}-%{release}
%global win64_host_dir %{_builddir}/mingw64-host-%{name}-%{version}-%{release}

# Disable debuginfo subpackages and debugsource packages for now to use old logic
%undefine _debugsource_packages
%undefine _debuginfo_subpackages

# Override the __debug_install_post argument as this package
# contains both native as well as cross compiled binaries
%global __debug_install_post %%{mingw_debug_install_post}; %{_rpmconfigdir}/find-debuginfo.sh %{?_missing_build_ids_terminate_build:--strict-build-id} %{?_find_debuginfo_opts} "%{_builddir}/%%{?buildsubdir}" %{nil}

%global pkgname sip
#global pre dev1805261119

Name:           mingw-%{pkgname}
Summary:        MinGW Windows SIP
Version:        4.19.24
Release:        1%{?pre:.%pre}%{?dist}

# sipgen/parser.{c.h} is GPLv3+ with exceptions (bison)
License:        GPLv2 or GPLv3 and (GPLv3+ with exceptions)
Url:            http://www.riverbankcomputing.com/software/sip/intro
Source0:        https://www.riverbankcomputing.com/static/Downloads/sip/%{version}/sip-%{version}%{?pre:.%pre}.tar.gz
Source1:        mingw-win32-g++
Source2:        mingw-win64-g++

# make install should not strip (by default), kills -debuginfo
Patch0:         sip-4.16.3-no_strip.patch
# try not to rpath the world
Patch1:         sip-4.16.3-no_rpath.patch
# Fix some config paths, add -lpythonX.Y to linker flags, fix broken mkdistinfo
Patch2:         sip-4.19-config.patch


BuildRequires:  gcc-c++
BuildRequires:  python3-devel

BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-qt5-qtbase

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-qt5-qtbase


%description
MinGW Windows SIP.

%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Windows SIP - Python 3
Obsoletes:     mingw32-%{pkgname} < 4.19.12-2
Provides:      mingw32-%{pkgname} = %{version}-%{release}
Requires:      mingw32-python3

%description -n mingw32-python3-%{pkgname}
MinGW Windows SIP - Python 3.


%package -n mingw32-python3-pyqt5-%{pkgname}
Summary:       MinGW Windows SIP module for PyQt5 - Python 3
Requires:      mingw32-python3-%{pkgname}

%description -n mingw32-python3-pyqt5-%{pkgname}
MinGW Windows SIP - Python 3.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows SIP
Obsoletes:     mingw64-%{pkgname} < 4.19.12-2
Provides:      mingw64-%{pkgname} = %{version}-%{release}
Requires:      mingw64-python3

%description -n mingw64-python3-%{pkgname}
MinGW Windows SIP - Python 3.


%package -n mingw64-python3-pyqt5-%{pkgname}
Summary:       MinGW Windows SIP module for PyQt5 - Python 3
Requires:      mingw64-python3-%{pkgname}

%description -n mingw64-python3-pyqt5-%{pkgname}
MinGW Windows SIP - Python 3.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}%{?pre:.%pre}
cp -a %{SOURCE1} specs/mingw-win32-g++
cp -a %{SOURCE2} specs/mingw-win64-g++


%build
function genHostConfig() {
    target=$1
    pyver=$2
    cat > ${target}_${pyver}.host.config <<EOF
plat_bin_dir=/usr/$target/bin
plat_py_site_dir=/usr/$target/lib/python$pyver/site-packages
py_inc_dir=/usr/$target/sys-root/mingw/include/python$pyver
py_pylib_dir=/usr/$target/lib
sip_bin_dir=/usr/$target/bin
sip_sip_dir=/usr/$target/sys-root/mingw/share/sip
sip_module_dir=/usr/$target/lib/python$pyver/site-packages
EOF
    echo ${target}_${pyver}.host.config
}

function genTargetConfig() {
    target=$1
    pyver=$2
    cat > ${target}_${pyver}.config <<EOF
plat_bin_dir=/usr/$target/sys-root/mingw/bin
plat_py_site_dir=/usr/$target/sys-root/mingw/lib/python$pyver/site-packages
py_inc_dir=/usr/$target/sys-root/mingw/include/python$pyver
py_pylib_dir=/usr/$target/sys-root/mingw/lib
sip_bin_dir=/usr/$target/sys-root/mingw/bin
sip_sip_dir=/usr/$target/sys-root/mingw/share/sip
sip_module_dir=/usr/$target/sys-root/mingw/lib/python$pyver/site-packages
py_platform=win32-g++
EOF
    echo ${target}_${pyver}.config
}

for module in "" PyQt5; do

moduleargs=""
if [ ! -z $module ]; then
    moduleargs="--sip-module $module.sip --no-tools"
fi

## Python3, host
mkdir build_mingw32_host_py3_$module
pushd build_mingw32_host_py3_$module
py3ver=%{mingw32_python3_version}
%{__python3} ../configure.py --configuration=`genHostConfig %{mingw32_target} $py3ver` \
    -d %{_prefix}/%{mingw32_target}/lib/python$py3ver/site-packages/ $moduleargs \
    CXXFLAGS="%{optflags} -I/usr/include/python${py3ver}" CFLAGS="%{optflags} -I/usr/include/python${py3ver}" LFLAGS="%{?__global_ldflags} -lpython${py3ver}"
%make_build
popd

mkdir build_mingw64_host_py3_$module
pushd build_mingw64_host_py3_$module
py3ver=%{mingw64_python3_version}
%{__python3} ../configure.py --configuration=`genHostConfig %{mingw64_target} $py3ver m` \
    -d %{_prefix}/%{mingw64_target}/lib/python$py3ver/site-packages/ $moduleargs \
    CXXFLAGS="%{optflags} -I/usr/include/python${py3ver}" CFLAGS="%{optflags} -I/usr/include/python${py3ver}" LFLAGS="%{?__global_ldflags} -lpython${py3ver}"
%make_build
popd

## Python3, target
mkdir build_mingw32_py3_$module
pushd build_mingw32_py3_$module
mingw32-python3 ../configure.py --configuration=`genTargetConfig %{mingw32_target} %{mingw32_python3_version}` \
    --use-qmake --no-stubs -p mingw-win32-g++ $moduleargs \
    CXXFLAGS="%{optflags}" CFLAGS="%{optflags}" LFLAGS="%{?__global_ldflags}"
%mingw32_qmake_qt5 sip.pro
%mingw32_make %{?_smp_mflags}
popd

mkdir build_mingw64_py3_$module
pushd build_mingw64_py3_$module
mingw64-python3 ../configure.py --configuration=`genTargetConfig %{mingw64_target} %{mingw64_python3_version}` \
    --use-qmake --no-stubs -p mingw-win64-g++ $moduleargs \
    CXXFLAGS="%{optflags}" CFLAGS="%{optflags}" LFLAGS="%{?__global_ldflags}"
%mingw64_qmake_qt5 sip.pro
%mingw64_make %{?_smp_mflags}
popd

done


%install
for module in "" PyQt5; do

%make_install -C build_mingw32_host_py3_$module
%make_install -C build_mingw64_host_py3_$module
%mingw32_make install INSTALL_ROOT=%{buildroot} -C build_mingw32_py3_$module
%mingw64_make install INSTALL_ROOT=%{buildroot} -C build_mingw64_py3_$module

done


mkdir -p %{buildroot}%{mingw32_datadir}/sip
mkdir -p %{buildroot}%{mingw64_datadir}/sip

mkdir -p %{buildroot}%{_bindir}
ln -s %{_prefix}/%{mingw32_target}/bin/sip %{buildroot}%{_bindir}/mingw32-sip
ln -s %{_prefix}/%{mingw64_target}/bin/sip %{buildroot}%{_bindir}/mingw64-sip

# Exclude debug files from the main files (note: the debug files are only created after %%install, so we can't search for them directly)
find %{buildroot}%{mingw32_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw32-%{pkgname}.debugfiles
find %{buildroot}%{mingw64_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw64-%{pkgname}.debugfiles


%files -n mingw32-python3-%{pkgname} -f mingw32-%{pkgname}.debugfiles
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%{_prefix}/%{mingw32_target}/bin/sip
%{_prefix}/%{mingw32_target}/lib/python%{mingw32_python3_version}/site-packages/*
%exclude %{_prefix}/%{mingw32_target}/lib/python%{mingw32_python3_version}/site-packages/PyQt5*
%{_bindir}/mingw32-sip
%{mingw32_bindir}/sip.exe
%{mingw32_python3_sitearch}/*
%exclude %{mingw32_python3_sitearch}/PyQt5*
%{mingw32_includedir}/python%{mingw32_python3_version}/sip.h
%dir %{mingw32_datadir}/sip

%files -n mingw32-python3-pyqt5-%{pkgname}
%{_prefix}/%{mingw32_target}/lib/python%{mingw32_python3_version}/site-packages/PyQt5*
%{mingw32_python3_sitearch}/PyQt5*

%files -n mingw64-python3-%{pkgname} -f mingw64-%{pkgname}.debugfiles
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%{_prefix}/%{mingw64_target}/bin/sip
%{_prefix}/%{mingw64_target}/lib/python%{mingw32_python3_version}/site-packages/*
%exclude %{_prefix}/%{mingw64_target}/lib/python%{mingw32_python3_version}/site-packages/PyQt5*
%{_bindir}/mingw64-sip
%{mingw64_bindir}/sip.exe
%{mingw64_python3_sitearch}/*
%exclude %{mingw64_python3_sitearch}/PyQt5*
%{mingw64_includedir}/python%{mingw32_python3_version}/sip.h
%dir %{mingw64_datadir}/sip

%files -n mingw64-python3-pyqt5-%{pkgname}
%{_prefix}/%{mingw64_target}/lib/python%{mingw32_python3_version}/site-packages/PyQt5*
%{mingw64_python3_sitearch}/PyQt5*


%changelog
* Tue Aug 18 2020 Sandro Mani <manisandro@gmail.com> - 4.19.24-1
- Update to 4.19.24

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.19.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 09 2020 Sandro Mani <manisandro@gmail.com> - 4.19.23-1
- Update to 4.19.23

* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 4.19.22-2
- Rebuild (python-3.9)

* Wed Apr 08 2020 Sandro Mani <manisandro@gmail.com> - 4.19.22-1
- Update to 4.19.22

* Fri Jan 31 2020 Sandro Mani <manisandro@gmail.com> - 4.19.21-1
- Update to 4.19.21

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.19.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 21 2019 Sandro Mani <manisandro@gmail.com> - 4.19.20-1
- Update to 4.19.20

* Fri Sep 27 2019 Sandro Mani <manisandro@gmail.com> - 4.19.19-1
- Update to 4.19.19

* Fri Sep 27 2019 Sandro Mani <manisandro@gmail.com> - 4.19.18-2
- Rebuild (python 3.8)

* Mon Aug 05 2019 Sandro Mani <manisandro@gmail.com> - 4.19.18-1
- Update to 4.19.18
- Drop python2 build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.19.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 2019 Sandro Mani <manisandro@gmail.com> - 4.19.17-1
- Update to 4.19.17

* Wed May 01 2019 Sandro Mani <manisandro@gmail.com> - 4.19.16-2
- Add python3 subpackages

* Sat Apr 20 2019 Sandro Mani <manisandro@gmail.com> - 4.19.16-1
- Update to 4.19.16

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.19.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Sandro Mani <manisandro@gmail.com> - 4.19.13-2
- Bump

* Thu Oct 04 2018 Sandro Mani <manisandro@gmail.com> - 4.19.13-1
- Update to 4.19.13

* Mon Jul 30 2018 Sandro Mani <manisandro@gmail.com> - 4.19.12-4
- Rename pyqt5 sip subpackage in line with native packages
- Remove PyQt5 __init__.py scripts again

* Mon Jul 30 2018 Sandro Mani <manisandro@gmail.com> - 4.19.12-3
- Add __init__.py to PyQt5 module directories, to make private PyQt5 sip modules importable

* Sun Jul 29 2018 Sandro Mani <manisandro@gmail.com> - 4.19.12-2
- Rename mingw{32,64}-sip to mingw{32,64}-python2-sip
- Add PyQt5 private sip modules (Sigh...)

* Wed Jul 11 2018 Sandro Mani <manisandro@gmail.com> - 4.19.12-1
- Update to 4.19.12

* Fri Jun 01 2018 Sandro Mani <manisandro@gmail.com> - 4.19.9-0.1.dev1805261119
- Update to 4.19.9.dev1805261119

* Wed Mar 07 2018 Sandro Mani <manisandro@gmail.com> - 4.19.8-1
- Update to 4.19.8

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.19.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Sandro Mani <manisandro@gmail.com> - 4.19.7-1
- Update to 4.19.7

* Sat Nov 25 2017 Sandro Mani <manisandro@gmail.com> - 4.19.6-1
- Update to 4.19.6

* Tue Nov 07 2017 Sandro Mani <manisandro@gmail.com> - 4.19.5-1
- Update to 4.19.5

* Sat Nov 04 2017 Sandro Mani <manisandro@gmail.com> - 4.19.4-1
- Update to 4.19.4

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 4.19.3-4
- More robust debug file filtering

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 4.19.3-3
- Rebuild for mingw-filesystem

* Mon Sep 04 2017 Sandro Mani <manisandro@gmail.com> - 4.19.3-2
- Build against Qt5

* Tue Jul 11 2017 Sandro Mani <manisandro@gmail.com> - 4.19.3-1
- Update to 4.19.3

* Tue Apr 25 2017 Sandro Mani <manisandro@gmail.com> - 4.19.2-1
- Update to 4.19.2

* Mon Jan 16 2017 Sandro Mani <manisandro@gmail.com> - 4.19-1
- Update to 4.19.0

* Fri Jan 22 2016 Sandro Mani <manisandro@gmail.com> - 4.17-1
- Update to 4.17.0

* Mon Aug 10 2015 Sandro Mani <manisandro@gmail.com> - 4.16.9-1
- Initial package
