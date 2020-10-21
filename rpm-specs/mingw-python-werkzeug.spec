%{?mingw_package_header}

%global pkgname werkzeug

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       1.0.1
Release:       4%{?dist}
BuildArch:     noarch

# Code is BSD, bundled fonts are OFL
License:       BSD and OFL
URL:           https://palletsprojects.com/p/werkzeug/
Source0:       https://github.com/pallets/werkzeug/archive/%{version}/%{pkgname}-%{version}.tar.gz

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
%autosetup -p1 -n %{pkgname}-%{version}


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
%license LICENSE.rst src/werkzeug/debug/shared/FONT_LICENSE
%{mingw32_python3_sitearch}/%{pkgname}
%{mingw32_python3_sitearch}/Werkzeug-%{version}-py*.egg-info

%files -n mingw64-python3-%{pkgname}
%license LICENSE.rst src/werkzeug/debug/shared/FONT_LICENSE
%{mingw64_python3_sitearch}/%{pkgname}
%{mingw64_python3_sitearch}/Werkzeug-%{version}-py*.egg-info


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Sandro Mani <manisandro@gmail.com> - 1.0.1-3
- Be more specific in %%files
- Add FONT_LICENSE to %%license
- Add OFL to License

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 1.0.1-2
- Rebuild (python-3.9)

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Wed Oct 30 2019 Sandro Mani <manisandro@gmail.com> - 0.16.0-1
- Update to 0.16.0
- Switch to python3

* Wed Sep 06 2017 Sandro Mani <manisandro@gmail.com> - 0.11.10-1
- Initial package
