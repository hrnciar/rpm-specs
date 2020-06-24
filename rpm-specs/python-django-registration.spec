%global pypi_name django-registration
%global summary A user-registration application for Django

Name:           python-%{pypi_name}
Version:        2.1.2
Release:        14%{?dist}
Summary:        %{summary}

License:        BSD
URL:            https://github.com/ubernostrum/django-registration/
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
This is a fairly simple user-registration application for Django,
designed to make allowing user sign ups as painless as possible. It
requires a functional installation of Django 1.8 or newer, but has no
other dependencies.

%package doc
Summary:        %{summary} - documentation

%description doc
This is a fairly simple user-registration application for Django,
designed to make allowing user sign ups as painless as possible. It
requires a functional installation of Django 1.8 or newer, but has no
other dependencies.
This package provides documentation of %{pypi_name}.

%package -n python3-%{pypi_name}
Summary:        %{summary} - Python 3 version

BuildRequires:  python3-devel
Requires:       python3-django

Obsoletes:      python-%{pypi_name} < 2.1.2-5
Obsoletes:      python2-%{pypi_name} < 2.1.2-5

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This is a fairly simple user-registration application for Django,
designed to make allowing user sign ups as painless as possible. It
requires a functional installation of Django 1.8 or newer, but has no
other dependencies.
This package provides Python 3 build of %{pypi_name}.


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

#Language files; not under /usr/share, need to be handled manually
(cd %{buildroot} && find .%{python3_sitelib} -name 'django*.[mp]o') |
    %{__sed} -e 's|^.||' | %{__sed} -e \
    's:\(.*/locale/\)\([^/_]\+\)\(.*\.[mp]o$\):%lang(\2) \1\2\3:' \
  >> python3-%{pypi_name}.lang


%files doc
%license LICENSE
%doc AUTHORS PKG-INFO README.rst docs/*

%files -f python3-%{pypi_name}.lang -n python3-%{pypi_name}
%license LICENSE
%{python3_sitelib}/*.egg-info
%dir %{python3_sitelib}/registration
%{python3_sitelib}/registration/management
%{python3_sitelib}/registration/backends
%{python3_sitelib}/registration/migrations
%{python3_sitelib}/registration/__pycache__
%{python3_sitelib}/registration/tests
%{python3_sitelib}/registration/*.py*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.2-5
- Remove Python 2 subpackage for https://fedoraproject.org/wiki/Changes/Django20

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-2
- Rebuild for Python 3.6

* Wed Aug 17 2016 Jan Beran <jberan@redhat.com> - 2.1.2-1
- update to version 2.1.2
- url and source update
- modernized specfile with Python 3 packaging

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 10 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 0.8-5
- correct django-registration obs_ver

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 25 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.8-1
- New version

* Sat Mar 24 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.7-5
- Made minor changes according to review

* Fri Mar 23 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.7-4
- Renamed package to python-django-registration

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 06 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.7-2
- Take over the package

* Mon Sep 28 2009 Michel Salim <salimma@fedoraproject.org> - 0.7-1
- Initial package

