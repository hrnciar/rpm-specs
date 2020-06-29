%{?mingw_package_header}

%global pkgname jinja2

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       2.11.2
Release:       2%{?dist}
BuildArch:     noarch

License:       BSD
URL:           https://palletsprojects.com/p/jinja/
Source0:       https://github.com/pallets/jinja/archive/%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-setuptools

BuildRequires: mingw64-filesystem >= 95
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


%prep
%autosetup -p1 -n jinja-%{version}


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
%license LICENSE.rst
%{mingw32_python3_sitearch}/%{pkgname}
%{mingw32_python3_sitearch}/Jinja2-%{version}-py*.egg-info

%files -n mingw64-python3-%{pkgname}
%license LICENSE.rst
%{mingw64_python3_sitearch}/%{pkgname}
%{mingw64_python3_sitearch}/Jinja2-%{version}-py*.egg-info


%changelog
* Sun May 31 2020 Sandro Mani <manisandro@gmail.com> - 2.11.2-2
- Rebuild (python-3.9)

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 2.11.2-1
- Update to 2.11.2

* Wed Oct 30 2019 Sandro Mani <manisandro@gmail.com> - 2.10.3-1
- Update to 2.10.3
- Switch to python3

* Wed Sep 06 2017 Sandro Mani <manisandro@gmail.com> - 2.9.6-1
- Initial package
