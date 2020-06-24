Name:		python-libevdev
Version:	0.9
Release:	1%{?dist}
Summary:	Python bindings to the libevdev evdev device wrapper library

License:	MIT
URL:		https://pypi.python.org/pypi/libevdev/
Source0:	https://gitlab.freedesktop.org/libevdev/python-libevdev/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

%description
%{name} provides the Python bindings to the libevdev evdev device
wrapper library. These bindings provide a pythonic API to access evdev
devices and create uinput devices.

%package -n	python3-libevdev
Summary:	Python bindings to the libevdev evdev device wrapper library

BuildRequires:	python3-devel python3-setuptools
Requires:	libevdev

%{?python_provide:%python_provide python3-libevdev}

%description -n	python3-libevdev
%{name} provides the Python bindings to the libevdev evdev device
wrapper library. These bindings provide a pythonic API to access evdev
devices and create uinput devices.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%py3_build


%install
%py3_install


%files -n	python3-libevdev
%license COPYING
%{python3_sitelib}/libevdev/
%{python3_sitelib}/libevdev-%{version}-py*.egg-info

%changelog
* Thu Jun 04 2020 Peter Hutterer <peter.hutterer@redhat.com> 0.9-1
- python-libevdev 0.9

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Peter Hutterer <peter.hutterer@redhat.com> 0.8-1
- python-libevdev 0.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 2019 Peter Hutterer <peter.hutterer@redhat.com> 0.7-1
- python-libevdev 0.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Peter Hutterer <peter.hutterer@redhat.com> 0.6.1-1
- python-libevdev 0.6.1

* Tue Sep 11 2018 Peter Hutterer <peter.hutterer@redhat.com> 0.5-4
- Update URLs for gitlab

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5-2
- Rebuilt for Python 3.7

* Tue Apr 24 2018 Peter Hutterer <peter.hutterer@redhat.com> 0.5-1
- python-libevdev 0.5

* Thu Apr 19 2018 Peter Hutterer <peter.hutterer@redhat.com> 0.4-2
- Fix failure when setting up EV_REP 

* Mon Feb 26 2018 Peter Hutterer <peter.hutterer@redhat.com>- 0.4-1
- initial import (#1549003)

