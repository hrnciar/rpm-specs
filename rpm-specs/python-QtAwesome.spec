%global pypi_name QtAwesome
%global simple_name qtawesome

Name:		python-%{pypi_name}
Version:	0.7.3
Release:	1%{?dist}

Summary:	FontAwesome icons in PyQt and PySide applications
License:	MIT and OFL
URL:		https://github.com/spyder-ide/%{simple_name}

Source0:	%pypi_source

BuildArch:	noarch

BuildRequires:	python3-setuptools
BuildRequires:	python3-devel

#provides font files
#./qtawesome/fonts/fontawesome-webfont.ttf
Provides:	bundled(elusiveicons-fonts) = 001.000
#./qtawesome/fonts/elusiveicons-webfont.ttf
Provides:	bundled(fontawesome-fonts) = 4.4.1

%description
QtAwesome enables iconic fonts such as Font Awesome and Elusive.

It is a port to Python - PyQt / PySide of the QtAwesome C++ library by 
Rick Blommers.

%package -n     python3-%{pypi_name}
Summary:	FontAwesome icons in PyQt and PySide applications
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:	python3-QtPy
Requires:	python3-six

%description -n python3-%{pypi_name}

QtAwesome enables iconic fonts such as Font Awesome and Elusive.

It is a port to Python - PyQt / PySide of the QtAwesome C++ library by 
Rick Blommers.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name} 
%license LICENSE.txt
%doc README.md
%{_bindir}/qta-browser
%{python3_sitelib}/qtawesome
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Sep 22 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.3-1
- Update to 0.7.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-2
- Rebuilt for Python 3.9

* Thu May 07 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.2-1
- Update to 0.7.2
- Use pypi_source macro in specfile

* Sat May 02 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Mon Feb 17 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.7-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 09 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.7-1
- Update to 0.5.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.4-7
- Drop python2 package

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.4-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 16 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-6
- Rebuild for Python 3.6

* Sun Oct 02 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.3.3-5
- Fixed typo on dependency

* Thu Sep 29 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.3.3-4
- Added license tag
- Added doc file 
- Added provides

* Thu Sep 29 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.3.3-3
- Fix source url

* Thu Sep 29 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.3.3-2
- Fix license file installation

* Thu Aug 11 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.3.3-1
- Initial package.
