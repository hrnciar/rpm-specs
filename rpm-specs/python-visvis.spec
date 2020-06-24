%global srcname visvis
Name:             python-%{srcname}
Version:          1.12.3
Release:          2%{?dist}
Summary:          Python library for visualization of 1D to 4D data in an object oriented way
License:          BSD
URL:              https://github.com/almarklein/%{srcname}
Source0:          %{url}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildArch:        noarch

%global _description\
Visvis is a pure Python library for visualization of 1D to 4D data in an\
object oriented way. Essentially, visvis is an object oriented layer of\
Python on top of OpenGl, thereby combining the power of OpenGl with the\
usability of Python. A Matlab/Matplotlib-like interface in the form of a\
set of functions allows easy creation of objects (e.g. plot(), imshow(),\
volshow(), surf()).

%description
%{_description}

%package -n python3-%{srcname}
Summary:          %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:    python3-devel, python3-setuptools
Requires:         python3-numpy, python3-pyopengl
Recommends:       python3-PyQt4, python3-wxpython4
Recommends:       python3-gobject

%description -n python3-%{srcname}
%{_description}

%prep
%setup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license license.txt
%doc README.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.12.3-2
- Rebuilt for Python 3.9

* Mon Apr  6 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1.12.3-1
- New version
  Resolves: rhbz#1821247

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov  7 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1.11.2-5
- Dropped Python 2 support
  Resolves: rhbz#1769828

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1.11.2-1
- New version
  Resolves: rhbz#1693484

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 1.11.1-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Jun 15 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.11.1-3
- Simplified source URL

* Fri Jun 15 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.11.1-2
- Simplified the spec

* Thu Jun  7 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.11.1-1
- Initial release
