Name:           pyhoca-cli
Version:        0.6.1.2
Release:        4%{?dist}
Summary:        Command line X2Go client written in Python

License:        AGPLv3+
URL:            http://www.x2go.org/
Source0:        http://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-setproctitle
Requires:       python%{python3_pkgversion}-x2go

%description
X2Go is a server based computing environment with:
   - session resuming
   - low bandwidth support
   - LDAP support
   - client side mass storage mounting support
   - client side printing support
   - audio support
   - authentication by smartcard and USB stick

PyHoca-CLI provides a simple and flexible command line client
written in Python that allows you to control X2Go client sessions
on desktops and thin clients.


%prep
%autosetup -p1


%build
# Fix shebang of pyhoca-cli executable.
pathfix.py -i %{__python3} -pn %{name}
%py3_build


%install
%py3_install
mkdir -p %{buildroot}/%{_bindir}/
cp -p %{name} %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_mandir}/
cp -rp man/* %{buildroot}/%{_mandir}/


%files
%license COPYING
%doc README TODO
%{_bindir}/%{name}
%{python3_sitelib}/PyHoca_CLI-*
%{python3_sitelib}/pyhoca/
%{_mandir}/man1/%{name}.1*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.1.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Orion Poplawski <orion@nwra.com> - 0.6.1.2-1
- Update to 0.6.1.2

* Sun Nov 24 2019 Orion Poplawski <orion@nwra.com> - 0.6.1.1-1
- Update to 0.6.1.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 14 2018 Orion Poplawski <orion@nwra.com> - 0.6.0.1-1
- Update to 0.6.0.1

* Wed Sep 19 2018 Orion Poplawski <orion@nwra.com> - 0.6.0.0-1
- Update to 0.6.0.0, requires python 3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0.4-6
- Rebuilt for Python 3.7

* Mon Apr 16 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 0.5.0.4-5
- Fix shebangs to avoid depending on Python 2 for Fedora 28+

* Fri Apr 13 2018 Orion Poplawski <orion@nwra.com> - 0.5.0.4-4
- Switch to python 3 for Fedora 28+

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.0.4-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Orion Poplawski <orion@nwra.com> - 0.5.0.4-1
- Update to 0.5.0.4

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0.3-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.3-1
- Update to 0.5.0.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.2-1
- Update to 0.5.0.2

* Mon Oct 20 2014 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.1-1
- Update to 0.5.0.1

* Mon Oct 20 2014 Orion Poplawski <orion@cora.nwra.com> - 0.5.0.0-1
- Update to 0.5.0.0

* Fri Aug 22 2014 Orion Poplawski <orion@cora.nwra.com> - 0.4.0.2-3
- Drop notify-python requires

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 8 2014 Orion Poplawski <orion@cora.nwra.com> - 0.4.0.2-1
- Update to 0.4.0.2

* Fri Aug 30 2013 Orion Poplawski <orion@cora.nwra.com> - 0.4.0.1-2
- Change tabs to spaces

* Thu Aug 1 2013 Orion Poplawski <orion@cora.nwra.com> - 0.4.0.1-1
- Update to 0.4.0.1

* Tue Dec 18 2012 Orion Poplawski <orion@cora.nwra.com> - 0.2.1.0-1
- Initial Fedora release
