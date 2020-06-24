%global pypi_name django-annoying

Name:           python-%{pypi_name}
Version:        0.9.0
Release:        14%{?dist}
Summary:        Eliminate annoying things in the Django framework

License:        BSD
URL:            https://github.com/skorokithakis/django-annoying
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
Django-annoying is a django application that tries to
eliminate annoying things in the Django framework.

%package -n python3-%{pypi_name}
Summary:        Annoying things elimination in the Django framework

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-django

Obsoletes:      python2-%{pypi_name} < 0.9.0-5
Obsoletes:      python-%{pypi_name} < 0.9.0-5

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Django-annoying is a django application that tries to
eliminate annoying things in the Django framework.
This package provides Python 3 build of %{pypi_name}.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc PKG-INFO
%{python3_sitelib}/annoying/
%{python3_sitelib}/*.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-5
- Removed Python 2 subpackage for https://fedoraproject.org/wiki/Changes/Django20

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-2
- Rebuild for Python 3.6

* Sat Aug 6 2016 Jan Beran <jberan@redhat.com> - 0.9.0-1
- update to version 0.9.0
- url and source update
- modernized specfile with Python 3 packaging

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-10.20120609hga0de8b
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-9.20120609hga0de8b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-8.20120609hga0de8b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-7.20120609hga0de8b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 30 2013 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.7.6-6.20120609hga0de8b
- Insufficient or ancient Obsoletes removed

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-5.20120609hga0de8b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-4.20120609hga0de8b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jun 09 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.7.6-3.20120609hga0de8b
- Cloned for latest source and added License file

* Sat Mar 24 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.7.6-2
- Renamed Package to python-djange-annoying

* Tue Aug 16 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.7.6-1
- Initial RPM release
