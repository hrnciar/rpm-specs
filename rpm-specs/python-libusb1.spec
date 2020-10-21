%global srcname libusb1

Name:           python-%{srcname}
Version:        1.8
Release:        2%{?dist}
Summary:        Pure-python wrapper for libusb-1.0

License:        LGPLv2+
URL:            https://github.com/vpelletier/python-libusb1
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  libusb-devel

%description
Pure-python wrapper for libusb-1.0.

Supports all transfer types, both in synchronous and asynchronous mode.

%package -n python3-%{srcname}
Requires:       libusb1
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Pure-python wrapper for libusb-1.0.

Supports all transfer types, both in synchronous and asynchronous mode.


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info
rm -rf __pycache__

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license COPYING COPYING.LESSER
%doc README.rst PKG-INFO
%pycached %{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/usb1/
%{python3_sitelib}/%{srcname}-*.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jonny Heggheim <hegjon@gmail.com> - 1.8-1
- Updated to 1.8

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.4-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.4-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.4-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 16 2018 Jonny Heggheim <hegjon@gmail.com> - 1.6.4-4
- Removed Python2 sub-package

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.4-2
- Rebuilt for Python 3.7

* Tue Mar 20 2018 Jonny Heggheim <hegjon@gmail.com> - 1.6.4-1
- Inital version
