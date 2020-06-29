%{?mingw_package_header}

%global pkgname requests

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       2.23.0
Release:       3%{?dist}
BuildArch:     noarch

License:       ASL 2.0
URL:           https://requests.readthedocs.io/
Source0:       https://github.com/psf/requests/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-setuptools

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-setuptools


%description
MinGW Windows Python %{pkgname}.


%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname}
Requires:      mingw32-python3-certifi

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python3 %{pkgname}.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname}
Requires:      mingw64-python3-certifi

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python3 %{pkgname}.


%prep
%autosetup -p1 -n %{pkgname}-%{version}

# Strip env shebang in nonexecutable file
sed -i '/#!\/usr\/.*python/d' requests/certs.py


%build
%{mingw32_python3} setup.py build -b build_mingw32
%{mingw64_python3} setup.py build -b build_mingw64


%install
ln -s build_mingw32 build
%{mingw32_python3} setup.py install -O1 --skip-build --root=%{buildroot}
rm build

ln -s build_mingw64 build
%{mingw64_python3} setup.py install -O1 --skip-build  --root=%{buildroot}
rm build


%files -n mingw32-python3-%{pkgname}
%license LICENSE
%{mingw32_python3_sitearch}/%{pkgname}
%{mingw32_python3_sitearch}/%{pkgname}-%{version}-py*.egg-info


%files -n mingw64-python3-%{pkgname}
%license LICENSE
%{mingw64_python3_sitearch}/%{pkgname}
%{mingw64_python3_sitearch}/%{pkgname}-%{version}-py*.egg-info


%changelog
* Thu Jun 25 2020 Sandro Mani <manisandro@gmail.com> - 2.23.0-3
- Be more specific in %%files
- Fix license
- Strip env shebang in nonexecutable file

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 2.23.0-2
- Rebuild (python-3.9)

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 2.23.0-1
- Update to 2.23.0

* Fri Dec 06 2019 Sandro Mani <manisandro@gmail.com> - 2.22.0-1
- Initial package
