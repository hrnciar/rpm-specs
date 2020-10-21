%{?mingw_package_header}

%global pkgname numpy

Name:          mingw-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       1.19.2
Release:       1%{?dist}
BuildArch:     noarch

# Everything is BSD except for class SafeEval in numpy/lib/utils.py which is Python
License:       BSD and Python
URL:           http://www.numpy.org/
Source0:       https://github.com/%{pkgname}/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

# Don't use MSC specific stuff
Patch0:        numpy_mingw.patch


BuildRequires: mingw32-filesystem >= 102
BuildRequires: mingw32-gcc
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-Cython
BuildRequires: mingw32-python3-setuptools

BuildRequires: mingw64-filesystem >= 102
BuildRequires: mingw64-gcc
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-Cython
BuildRequires: mingw64-python3-setuptools


%description
%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname} library

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python3 %{pkgname} library.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname} library

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python3 %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
# Add -fno-asynchronous-unwind-tables to workaround "Error: invalid register for .seh_savexmm"
# See https://stackoverflow.com/questions/43152633/invalid-register-for-seh-savexmm-in-cygwin
CFLAGS="%{mingw32_cflags} -fno-asynchronous-unwind-tables" %{mingw32_python3} setup.py build -b build_py3_mingw32
CFLAGS="%{mingw64_cflags} -fno-asynchronous-unwind-tables" %{mingw64_python3} setup.py build -b build_py3_mingw64


%install
ln -s build_py3_mingw32 build
%{mingw32_python3} setup.py install -O1 --root=%{buildroot} --skip-build
rm build

ln -s build_py3_mingw64 build
%{mingw64_python3} setup.py install -O1 --root=%{buildroot} --skip-build
rm build

# FIXME: These files are not installed for some reason
cp -a build_py3_mingw32/src.mingw-%{mingw32_python3_version}/numpy/core/include/numpy/*.h %{buildroot}%{mingw32_python3_sitearch}/numpy/core/include/numpy/
cp -a build_py3_mingw32/src.mingw-%{mingw32_python3_version}/numpy/core/include/numpy/*.txt %{buildroot}%{mingw32_python3_sitearch}/numpy/core/include/numpy/
cp -a build_py3_mingw64/src.mingw-%{mingw64_python3_version}/numpy/core/include/numpy/*.h %{buildroot}%{mingw64_python3_sitearch}/numpy/core/include/numpy/
cp -a build_py3_mingw64/src.mingw-%{mingw64_python3_version}/numpy/core/include/numpy/*.txt %{buildroot}%{mingw64_python3_sitearch}/numpy/core/include/numpy/

# Symlink includedir
mkdir -p %{buildroot}%{mingw32_includedir}
mkdir -p %{buildroot}%{mingw64_includedir}
ln -s %{mingw32_python3_sitearch}/numpy/core/include/numpy/ %{buildroot}%{mingw32_includedir}/numpy
ln -s %{mingw64_python3_sitearch}/numpy/core/include/numpy/ %{buildroot}%{mingw64_includedir}/numpy

# Exclude debug files from the main files (note: the debug files are only created after %%install, so we can't search for them directly)
find %{buildroot}%{mingw32_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw32-%{pkgname}.debugfiles
find %{buildroot}%{mingw64_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw64-%{pkgname}.debugfiles


%files -n mingw32-python3-%{pkgname} -f mingw32-%{pkgname}.debugfiles
%license LICENSE.txt
%{mingw32_bindir}/f2py
%{mingw32_bindir}/f2py3
%{mingw32_bindir}/f2py%{mingw32_python3_version}
%{mingw32_includedir}/%{pkgname}
%{mingw32_python3_sitearch}/*

%files -n mingw64-python3-%{pkgname} -f mingw64-%{pkgname}.debugfiles
%license LICENSE.txt
%{mingw64_bindir}/f2py
%{mingw64_bindir}/f2py3
%{mingw64_bindir}/f2py%{mingw32_python3_version}
%{mingw64_includedir}/%{pkgname}
%{mingw64_python3_sitearch}/*


%changelog
* Fri Sep 11 2020 Sandro Mani <manisandro@gmail.com> - 1.19.2-1
- Update to 1.19.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Sandro Mani <manisandro@gmail.com> - 1.19.1-1
- Update to 1.19.1

* Tue Jun 23 2020 Sandro Mani <manisandro@gmail.com> - 1.19.0-1
- Update to 1.19.0

* Mon Jun 08 2020 Sandro Mani <manisandro@gmail.com> - 1.18.5-1
- Update to 1.18.5

* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 1.18.4-2
- Rebuild (python-3.9)

* Mon May 04 2020 Sandro Mani <manisandro@gmail.com> - 1.18.4-1
- Update to 1.18.4

* Tue Apr 21 2020 Sandro Mani <manisandro@gmail.com> - 1.18.3-1
- Update to 1.18.3

* Wed Mar 18 2020 Sandro Mani <manisandro@gmail.com> - 1.18.2-1
- Update to 1.18.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Sandro Mani <manisandro@gmail.com> - 1.18.1-1
- Update to 1.18.1

* Mon Dec 30 2019 Sandro Mani <manisandro@gmail.com> - 1.18.0-1
- Update to 1.18.0

* Tue Nov 12 2019 Sandro Mani <manisandro@gmail.com> - 1.17.4-1
- Update to 1.17.4

* Thu Oct 24 2019 Sandro Mani <manisandro@gmail.com> - 1.17.3-2
- Link devel files to include dir
- Add missing headers

* Fri Oct 18 2019 Sandro Mani <manisandro@gmail.com> - 1.17.3-1
- Update to 1.17.3

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.17.2-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Fri Sep 27 2019 Sandro Mani <manisandro@gmail.com> - 1.17.2-1
- Update to 1.17.2

* Fri Aug 02 2019 Sandro Mani <manisandro@gmail.com> - 1.17.0-1
- Update to 1.17.0
- Drop python2 packages

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Sandro Mani <manisandro@gmail.com> - 1.16.4-1
- Update to 1.16.4

* Wed May 01 2019 Sandro Mani <manisandro@gmail.com> - 1.16.3-2
- Add python3 subpackages

* Tue Apr 23 2019 Sandro Mani <manisandro@gmail.com> - 1.16.3-1
- Update to 1.16.3

* Wed Feb 27 2019 Sandro Mani <manisandro@gmail.com> - 1.16.2-1
- Update to 1.16.2

* Mon Feb 04 2019 Sandro Mani <manisandro@gmail.com> - 1.16.1-1
- Update to 1.16.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Sandro Mani <manisandro@gmail.com> - 1.16.0-1
- Update to 1.16.0

* Thu Aug 30 2018 Sandro Mani <manisandro@gmail.com> - 1.15.1-1
- Update to 1.15.1

* Thu Aug 02 2018 Sandro Mani <manisandro@gmail.com> - 1.15.0-1
- Update to 1.15.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Sandro Mani <manisandro@gmail.com> - 1.14.5-1
- Update to 1.14.5

* Wed May 02 2018 Sandro Mani <manisandro@gmail.com> - 1.14.3-1
- Update to 1.14.3

* Tue Mar 13 2018 Sandro Mani <manisandro@gmail.com> - 1.14.2-1
- Update to 1.14.2

* Thu Feb 22 2018 Sandro Mani <manisandro@gmail.com> - 1.14.1-1
- Update to 1.14.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 Sandro Mani <manisandro@gmail.com> - 1.13.3-1
- Update to 1.13.3

* Fri Sep 29 2017 Sandro Mani <manisandro@gmail.com> - 1.13.2-1
- Update to 1.13.2

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 1.13.1-2
- Rebuild for mingw-filesystem

* Sat Sep 02 2017 Sandro Mani <manisandro@gmail.com> - 1.13.1-1
- Initial package
