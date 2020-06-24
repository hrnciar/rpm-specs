%{?mingw_package_header}

%global pkgname setuptools

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       47.1.1
Release:       1%{?dist}
BuildArch:     noarch

License:       MIT
URL:           https://pypi.python.org/pypi/%{pkgname}
Source0:       https://files.pythonhosted.org/packages/source/s/%{pkgname}/%{pkgname}-%{version}.zip

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3


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


%prep
%autosetup -p1 -n %{pkgname}-%{version}

# Remove bundled exes
rm -f setuptools/*.exe

# Strip shebangs on python modules
find setuptools -name \*.py | xargs sed -i -e '1 {/^#!\//d}'


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

find %{buildroot}%{mingw32_python3_sitearch}/ -name '*.exe' | xargs rm -f
find %{buildroot}%{mingw64_python3_sitearch}/ -name '*.exe' | xargs rm -f

# Drop unversioned easy_install
rm -f %{buildroot}%{mingw32_bindir}/easy_install
rm -f %{buildroot}%{mingw64_bindir}/easy_install


%files -n mingw32-python3-%{pkgname}
%license LICENSE
%{mingw32_bindir}/easy_install-%{mingw32_python3_version}
%{mingw32_python3_sitearch}/*

%files -n mingw64-python3-%{pkgname}
%license LICENSE
%{mingw64_bindir}/easy_install-%{mingw64_python3_version}
%{mingw64_python3_sitearch}/*


%changelog
* Fri Jun 12 2020 Sandro Mani <manisandro@gmail.com> - 47.1.1-1
- Update to 47.1.1

* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 46.4.0-2
- Rebuild (python-3.9)

* Mon May 18 2020 Sandro Mani <manisandro@gmail.com> - 46.4.0-1
- Update to 46.4.0

* Thu May 14 2020 Sandro Mani <manisandro@gmail.com> - 46.2.0-1
- Update to 46.2.0

* Thu Apr 02 2020 Sandro Mani <manisandro@gmail.com> - 46.1.2-1
- Update to 46.1.2

* Fri Mar 13 2020 Sandro Mani <manisandro@gmail.com> - 46.0.0-1
- Update to 46.0.0

* Mon Mar 02 2020 Sandro Mani <manisandro@gmail.com> - 45.2.0-1
- Update to 45.2.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 41.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Sandro Mani <manisandro@gmail.com> - 41.6.0-1
- Update to 41.6.0

* Thu Sep 26 2019 Sandro Mani <manisandro@gmail.com> - 41.2.0-1
- Update to 41.2.0

* Mon Aug 05 2019 Sandro Mani <manisandro@gmail.com> - 41.0.1-3
- Drop python2 build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 41.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Sandro Mani <manisandro@gmail.com> - 41.0.1-1
- Update to 41.0.1
- Add python3 subpackages

* Wed Feb 06 2019 Sandro Mani <manisandro@gmail.com> - 40.8.0-1
- Update to 40.8.0

* Tue Feb 05 2019 Sandro Mani <manisandro@gmail.com> - 40.7.3-1
- Update to 40.7.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 40.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Sandro Mani <manisandro@gmail.com> - 40.7.1-1
- Update to 40.7.1

* Tue Sep 25 2018 Sandro Mani <manisandro@gmail.com> - 40.4.3-1
- Update to 40.4.3

* Thu Sep 20 2018 Sandro Mani <manisandro@gmail.com> - 40.4.1-1
- Update to 40.4.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 39.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 28 2018 Sandro Mani <manisandro@gmail.com> - 39.2.0-1
- Update to 39.2.0

* Wed Mar 21 2018 Sandro Mani <manisandro@gmail.com> - 39.0.1-1
- Update to 39.0.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 38.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Sandro Mani <manisandro@gmail.com> - 38.4.0-1
- Update to 38.4.0

* Wed Jan 03 2018 Sandro Mani <manisandro@gmail.com> - 38.2.5-1
- Update to 38.2.5

* Thu Nov 23 2017 Sandro Mani <manisandro@gmail.com> - 37.0.0-1
- Update to 37.0.0

* Tue Sep 05 2017 Sandro Mani <manisandro@gmail.com> - 36.2.0-2
- Remove bundled exes
- Remove shebangs on python modules
- Delete exes underneath site-packages

* Thu Aug 31 2017 Sandro Mani <manisandro@gmail.com> - 36.2.0-1
- Initial package
