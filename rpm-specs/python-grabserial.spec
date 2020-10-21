%global realname grabserial

Name: python-grabserial
Version: 2.0.2
Release: 3%{?dist}
Summary: Reads a serial port and writes data to standard output

License: GPLv2
URL: http://elinux.org/Grabserial
Source0: https://github.com/tbird20d/grabserial/archive/v%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-setuptools
BuildRequires: python3-devel

%global _description\
Grabserial reads a serial port and writes the data to standard output.The main\
purpose of this tool is to collect messages written to the serial console from\
a target board running Linux, and save the messages on a host machine.

%description %_description

%package -n python3-grabserial
Summary: %summary
Requires: python3-pyserial
%{?python_provide:%python_provide python3-grabserial}

%description -n python3-grabserial %_description

%prep
%setup -qn %{realname}-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

%files -n python3-grabserial
%doc README.md
%license LICENSE
%{_bindir}/grabserial
%{python3_sitelib}/*.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-2
- Rebuilt for Python 3.9

* Fri Feb 28 2020 Sinny Kumari <sinnykumari@fedoraproject.org> - 2.0.2-1
- rhbz#1800907: update to upstream release 2.0.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Sinny Kumari <sinnykumari@fedoraproject.org> - 1.9.9-1
- rhbz#1738113: Build python3-grabserial and drop python2-grabserial sub-package
- Update to upstream version v1.9.9

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.9.3-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.3-3
- Python 2 binary package renamed to python2-grabserial
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Sinny Kumari <sinnykumari@fedoraproject.org> - 1.9.3-1
- Rebase to upstream version 1.9.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Sinny Kumari <ksinny@gmail.com> - 1.8.1-1
- Packaging 1.8.1 version

* Sun Apr 12 2015 Sinny Kumari <ksinny@gmail.com> - 1.7.1-2
- Correcting License to GPLv2+
- Cosmetic change in file section

* Sun Mar 15 2015 Sinny Kumari <ksinny@gmail.com> - 1.7.1-1
- Initial Fedora packaging of grabserial
