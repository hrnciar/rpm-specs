%global modname gearbox

Name:               python-gearbox
Version:            0.1.1
Release:            19%{?dist}
Summary:            Command line toolkit born as a PasteScript replacement for TurboGears2

License:            MIT
URL:                http://pypi.python.org/pypi/gearbox
Source0:            http://pypi.python.org/packages/source/g/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools

%global _description\
gearbox is a paster command replacement for TurboGears2. It has been\
created during the process of providing Python3 support to the TurboGears2\
web framework, while still being backward compatible with the existing\
TurboGears projects.\


%description %_description

%package -n python3-gearbox
Summary:            Command line toolkit born as a PasteScript replacement for TurboGears2

Requires:           python3-prettytable
Requires:           python3-cliff
Requires:           python3-tempita
Requires:           python3-paste-deploy

%description -n python3-gearbox
gearbox is a paster command replacement for TurboGears2. It has been
created during the process of providing Python3 support to the TurboGears2
web framework, while still being backward compatible with the existing
TurboGears projects.

%prep
%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}

%files -n python3-gearbox
%doc README.rst
%{_bindir}/gearbox
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-19
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Kevin Fenzi <kevin@scrye.com> - 0.1.1-14
- Drop python2 subpackages. 

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-12
- Use the py2 version of the macros

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.1-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.1-7
- Python 2 binary package renamed to python2-gearbox
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Jan Beran <jberan@redhat.com> - 0.1.1-5
- Fix of missing Python 3 version executables

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Mar 07 2016 Ralph Bean <rbean@redhat.com> - 0.1.1-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Ralph Bean <rbean@redhat.com> - 0.0.11-1
- new version

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Oct 13 2015 Ralph Bean <rbean@redhat.com> - 0.0.9-1
- new version

* Wed Sep 16 2015 Ralph Bean <rbean@redhat.com> - 0.0.8-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jul 21 2014 Ralph Bean <rbean@redhat.com> - 0.0.6-1
- Latest upstream.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Feb 12 2014 Ralph Bean <rbean@redhat.com> - 0.0.5-1
- Latest upstream.

* Wed Jan 22 2014 Ralph Bean <rbean@redhat.com> - 0.0.4-1
- Latest upstream.
- Reenabled python3 subpackage.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-0.3.a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 12 2013 Ralph Bean <rbean@redhat.com> - 0.0.1-0.2.a
- Disabled python3 subpackage for rawhide due to broken python3-cliff.
- Moved python3 Requires inside the python3-gearbox subpackage.

* Wed Apr 03 2013 Luke Macken <lmacken@redhat.com> 0.0.1-0.1.a
- Initial package for Fedora

