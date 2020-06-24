%{?mingw_package_header}

%global pkgname certifi

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       2020.04.05.1
Release:       2%{?dist}
BuildArch:     noarch

License:       MPL2.0
URL:           https://certifi.io/en/latest/
Source0:       https://github.com/certifi/python-certifi/archive/%{version}/%{pkgname}-%{version}.tar.gz

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

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python3 %{pkgname}.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname}

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python3 %{pkgname}.


%prep
%autosetup -p1 -n python-%{pkgname}-%{version}


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
%{mingw32_python3_sitearch}/*

%files -n mingw64-python3-%{pkgname}
%license LICENSE
%{mingw64_python3_sitearch}/*


%changelog
* Sun May 31 2020 Sandro Mani <manisandro@gmail.com> - 2020.04.05.1-2
- Rebuild (python-3.9)

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 2020.04.05.1-1
- Update to 2020.04.05.1

* Mon Dec 16 2019 Sandro Mani <manisandro@gmail.com> - 2019.11.28-1
- Initial package
