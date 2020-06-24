%global upstream_name blessings


Name:           python-%{upstream_name}
Version:        1.7
Release:        10%{?dist}
Summary:        Python library for terminal coloring, styling, and positioning
License:        MIT
URL:            https://github.com/erikrose/blessings
Source0:        https://files.pythonhosted.org/packages/source/b/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
# https://github.com/erikrose/blessings/issues/25
Patch1:         0001-fix-tests-when-run-without-a-tty-fixes-25.patch
Patch2:         0002-more-fixes-for-tests-without-a-tty.patch
BuildArch:      noarch

%description
Blessings is a thin, practical wrapper around terminal coloring, styling, and 
positioning in Python.

%package -n python3-%{upstream_name}
Summary:        Python 3 library for terminal coloring, styling, and positioning
%{?python_provide:%python_provide python3-%{upstream_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-six
Requires:       python3-six

%description -n python3-%{upstream_name}
Blessings is a thin, practical wrapper around terminal coloring, styling, and 
positioning in Python.

%prep
%setup -q -n %{upstream_name}-%{version}
%patch1 -p1
%patch2 -p1
rm -rf blessings.egg-info

%build
%py3_build

%install
%py3_install

%check
nosetests-3 build/lib

%files -n python3-%{upstream_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/blessings
%{python3_sitelib}/blessings*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7-5
- Subpackage python2-blessings has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7-2
- Rebuilt for Python 3.7

* Tue Jun 26 2018 Dan Callaghan <dcallagh@redhat.com> - 1.7-1
- Upstream release 1.7 (RHBZ#1594040)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5-16
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Dan Callaghan <dcallagh@redhat.com> - 1.5-13
- forgot to add %%python_provide macro

* Fri Jun 23 2017 Dan Callaghan <dcallagh@redhat.com> - 1.5-12
- renamed python-blessings to python2-blessings

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5-10
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 30 2012 Dan Callaghan <dcallagh@redhat.com> - 1.5-1
- initial version
