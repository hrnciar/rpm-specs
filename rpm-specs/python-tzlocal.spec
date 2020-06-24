%global srcname tzlocal
%global sum A Python module that tries to figure out what your local timezone is

Name:           python-tzlocal
Version:        2.0.0
Release:        2%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/regebro/tzlocal
# pypi/pythonhosted tarballs don't respect symlinks which are used in the test
Source0:        https://github.com/regebro/tzlocal/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-pytz
BuildRequires:  python3-setuptools


%description
This Python module returns a tzinfo object with the local timezone information. 
It requires pytz, and returns pytz tzinfo objects.  This module attempts to fix 
a glaring hole in pytz, that there is no way to get the local timezone 
information, unless you know the zoneinfo name.


%package -n python3-%{srcname}
Summary:        %{sum}
License:        MIT
Requires:       python3-pytz
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This Python module returns a tzinfo object with the local timezone information. 
It requires pytz, and returns pytz tzinfo objects.  This module attempts to fix 
a glaring hole in pytz, that there is no way to get the local timezone 
information, unless you know the zoneinfo name.


%prep
%autosetup -n %{srcname}-%{version}

rm -rf *.egg-info


%build
%py3_build


%install
%py3_install
# Don't install unit tests and test_data
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/test_data


%check
%{__python3} setup.py test


%files -n python3-%{srcname}
%doc README.rst CHANGES.txt
%license LICENSE.txt
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py3.?.egg-info


%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-2
- Rebuilt for Python 3.9

* Fri May 01 2020 Piotr Popieluch <piotr1212@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 16 2018 Piotr Popieluch <piotr1212@gmail.com> - 1.5.1-5
- Remove Python 2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Piotr Popieluch <piotr1212@gmail.com> - 1.5.1-1
- Update to 1.5.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3-2
- Rebuild for Python 3.6

* Wed Nov 09 2016 piotr1212@gmail.com - 1.3-1
- Update to upstream 1.3
- Update specfile to latest python packaging guidelines

* Wed Nov 09 2016 piotr1212@gmail.com - 1.2-6
- Move python3-pytz requires to python3 subpackage (RHBZ#1393397)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Nov 06 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.2-2
- Rebuilt for python 3.5

* Fri Jul 03 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.2-1
- Update to 1.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 22 2014 Piotr Popieluch <piotr1212@gmail.com> - 1.1.2-4
- added epel support

* Tue Oct 28 2014 Piotr Popieluch <piotr1212@gmail.com> - 1.1.2-3
- fixed python3-tzlocal %%summary to match python-tzlocal

* Sat Oct 25 2014 Piotr Popieluch <piotr1212@gmail.com> - 1.1.2-2
- deleted group tag
- added license to python3 module
- rewritten summary
- wrapped description
- added rm -rf *.egg-info to %%prep
- added comments to the rm commands in %%install section

* Fri Oct 24 2014 Piotr Popieluch <piotr1212@gmail.com> - 1.1.2-1
- Initial package
