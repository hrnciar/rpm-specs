%global srcname iptools

Name:           python-%{srcname}
Version:        0.7.0
Release:        2%{?dist}
Summary:        A few useful functions and objects for manipulating IP addresses in python

License:        BSD
URL:            https://github.com/bd808/%{name}
Source0:        https://github.com/bd808/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-setuptools

%global _description\
A few useful functions and objects for manipulating IPv4 and IPv6 addresses\
in python. The project was inspired by a desire to be able to use CIDR address\
notation to designate INTERNAL_IPS in a Django project's settings file.\

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        A few useful functions and objects for manipulating IP addresses in python 3

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%setup -q
find -name .gitignore -delete


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test

 
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc AUTHORS CHANGES docs README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/


%changelog
* Thu Aug 27 2020 Orion Poplawski <orion@nwra.com> - 0.7.0-2
- Use %%license
- Explicit python files
- EPEL compatibility

* Fri Aug 21 2020 Orion Poplawski <orion@nwra.com> - 0.7.0-1
- Update to 0.7.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-15
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.1-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6.1-12
- Python 2 binary package renamed to python2-iptools
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 02 2014 Orion Poplawski <orion@cora.nwra.com> - 0.6.1-3
- Rebuild for Python 3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Orion Poplawski <orion@cora.nwra.com> - 0.6.1-1
- Update to 0.6.1

* Fri Apr 19 2013 Orion Poplawski <orion@cora.nwra.com> - 0.6.0-4
- Remove install dir rm in %%install

* Fri Apr 19 2013 Orion Poplawski <orion@cora.nwra.com> - 0.6.0-3
- Cleanup macros

* Sun Apr 7 2013 Orion Poplawski <orion@cora.nwra.com> - 0.6.0-2
- Add BR python-setuptools
- Add %%check

* Sat Apr 6 2013 Orion Poplawski <orion@cora.nwra.com> - 0.6.0-1
- Initial Fedora package
