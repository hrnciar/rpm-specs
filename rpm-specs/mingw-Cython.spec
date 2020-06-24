%{?mingw_package_header}

%global pkgname Cython

Name:          mingw-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       0.29.19
Release:       1%{?dist}
BuildArch:     noarch

License:       ASL 2.0
URL:           http://www.cython.org
Source:        https://github.com/cython/cython/archive/%{version}/cython-%{version}.tar.gz


BuildRequires: mingw32-filesystem >= 102
BuildRequires: mingw32-gcc
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-setuptools

BuildRequires: mingw64-filesystem >= 102
BuildRequires: mingw64-gcc
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-setuptools


%description
MinGW Windows Python %{pkgname} library.


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
%autosetup -p1 -n cython-%{version}


%build
%{mingw32_python3} setup.py build -b build_py3_mingw32
%{mingw64_python3} setup.py build -b build_py3_mingw64



%install
ln -s build_py3_mingw32 build
%{mingw32_python3} setup.py install -O1 --skip-build --root=%{buildroot}
rm build

ln -s build_py3_mingw64 build
%{mingw64_python3} setup.py install -O1 --skip-build  --root=%{buildroot}
rm build

# Exclude debug files from the main files (note: the debug files are only created after %%install, so we can't search for them directly)
find %{buildroot}%{mingw32_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw32-%{pkgname}.debugfiles
find %{buildroot}%{mingw64_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw64-%{pkgname}.debugfiles


%files -n mingw32-python3-%{pkgname} -f mingw32-%{pkgname}.debugfiles
%license LICENSE.txt
%{mingw32_bindir}/cygdb
%{mingw32_bindir}/cython
%{mingw32_bindir}/cythonize
%{mingw32_python3_sitearch}/*

%files -n mingw64-python3-%{pkgname} -f mingw64-%{pkgname}.debugfiles
%license LICENSE.txt
%{mingw64_bindir}/cygdb
%{mingw64_bindir}/cython
%{mingw64_bindir}/cythonize
%{mingw64_python3_sitearch}/*


%changelog
* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 0.29.19-1
- Update to 0.29.19

* Thu Mar 26 2020 Sandro Mani <manisandro@gmail.com> - 0.29.16-1
- Update to 0.29.16

* Wed Feb 12 2020 Sandro Mani <manisandro@gmail.com> - 0.29.15-1
- Update to 0.29.15

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Sandro Mani <manisandro@gmail.com> - 0.29.14-1
- Update to 0.29.14

* Fri Sep 27 2019 Sandro Mani <manisandro@gmail.com> - 0.29.13-3
- Rebuild (python 3.8)

* Mon Aug 05 2019 Sandro Mani <manisandro@gmail.com> - 0.29.13-2
- Drop python2 build

* Mon Jul 29 2019 Sandro Mani <manisandro@gmail.com> - 0.29.13-1
- Update to 0.29.13

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Sandro Mani <manisandro@gmail.com> - 0.29.12-1
- Update to 0.29.12

* Tue Jul 02 2019 Sandro Mani <manisandro@gmail.com> - 0.29.11-1
- Update to 0.29.11

* Mon Jun 03 2019 Sandro Mani <manisandro@gmail.com> - 0.29.10-1
- Update to 0.29.10

* Mon May 13 2019 Sandro Mani <manisandro@gmail.com> - 0.29.7-1
- Update to 0.29.7

* Wed May 01 2019 Sandro Mani <manisandro@gmail.com> - 0.29.6-2
- Add python3 subpackages

* Mon Mar 11 2019 Sandro Mani <manisandro@gmail.com> - 0.29.6-1
- Update to 0.29.6

* Sun Feb 10 2019 Sandro Mani <manisandro@gmail.com> - 0.29.5-1
- Update to 0.29.5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Sandro Mani <manisandro@gmail.com> - 0.29.3-1
- Update to 0.29.3

* Mon Dec 10 2018 Sandro Mani <manisandro@gmail.com> - 0.29.1-1
- Update to 0.29.1

* Sat Aug 11 2018 Sandro Mani <manisandro@gmail.com> - 0.28.5-1
- Update to 0.28.5

* Sun Jul 15 2018 Sandro Mani <manisandro@gmail.com> - 0.28.4-1
- Update to 0.28.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Sandro Mani <manisandro@gmail.com> - 0.28.1-1
- Update to 0.28.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 06 2017 Sandro Mani <manisandro@gmail.com> - 0.27.3-1
- Update to 0.27.3

* Mon Oct 02 2017 Sandro Mani <manisandro@gmail.com> - 0.27.1-1
- Update to 0.27.1

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 0.25.2-2
- Rebuild for mingw-filesystem

* Thu Aug 31 2017 Sandro Mani <manisandro@gmail.com> - 0.25.2-1
- Initial package
