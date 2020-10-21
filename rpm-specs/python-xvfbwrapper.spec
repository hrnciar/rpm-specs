
%global pypi_name xvfbwrapper

Name:           python-%{pypi_name}
Version:        0.2.9
Release:        12%{?dist}
Summary:        run headless display inside X virtual framebuffer (Xvfb)

License:        MIT
URL:            https://github.com/cgoldberg/xvfbwrapper
Source0:        https://files.pythonhosted.org/packages/source/x/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%global _description\
Python wrapper for running a display inside X virtual framebuffer (Xvfb)

%description %_description


%package -n python3-%{pypi_name}
Summary:        run headless display inside X virtual framebuffer (Xvfb)

BuildRequires: python3-devel
BuildRequires: python3-mock
BuildRequires: python3-nose
BuildRequires: xorg-x11-server-Xvfb

%description -n python3-%{pypi_name}
Python wrapper for running a display inside X virtual framebuffer (Xvfb)

%prep
%autosetup -n %{pypi_name}-%{version}


# remove shebang
sed -i '1{\@^#!/usr/bin/env python@d}' xvfbwrapper.py




%build

%py3_build

%install

%py3_install

%check
export DISPLAY=:0.0


nosetests-%{python3_version}

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}.py*
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.9-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.9-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.9-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.9-5
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Jul 23 2018 Matthias Runge <mrunge@redhat.com> - 0.2.9-4
- modernize spec
- fix ftbfs (rhbz#1606005)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.9-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Matthias Runge <mrunge@redhat.com> - 0.2.9-1
- update to 0.2.9-1

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.4-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.4-8
- Python 2 binary package renamed to python2-xvfbwrapper
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-5
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Jul 21 2015 Matthias Runge <mrunge@redhat.com> - 0.2.4-2
- add py3 subpackage (rhbz#1244817)

* Mon Jul 20 2015 Matthias Runge <mrunge@redhat.com> - 0.2.4-1
- Initial package.
