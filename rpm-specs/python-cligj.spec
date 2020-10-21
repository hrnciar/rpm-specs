%global srcname cligj

Name:           python-%{srcname}
Version:        0.6.0
Release:        1%{?dist}
Summary:        Click params for GeoJSON CLI

License:        BSD
URL:            https://github.com/mapbox/cligj
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  (python3dist(click) >= 4 with python3dist(click) < 8)
BuildRequires:  python3dist(pytest)

%description
Common arguments and options for GeoJSON processing commands, using Click.


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
Common arguments and options for GeoJSON processing commands, using Click.


%prep
%autosetup -n %{srcname}-%{version}

# README is executable
chmod -x README.rst


%build
%py3_build


%install
%py3_install


%check
%{pytest}


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Oct 20 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.0-1
- Update to latest version (#1889450)

* Thu Oct 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6~b1-1
- Update to latest beta version
- Fix License to BSD

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.0-1
- Update to latest version
- Compatibility with click 7
- Clean up some old vestiges of Python 2 subpackage

* Fri Sep 21 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-7
- Drop Python 2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 01 2017 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.0-3
- Fix ambiguous Python 2 dependencies declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 13 2017 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-1
- Updated to 0.4.0
- Updated to the new naming scheme

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Jul 27 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.0-1
- Update to latest version, required by python-Fiona

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 19 2015 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-1
- Initial package.
