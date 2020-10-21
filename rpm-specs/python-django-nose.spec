%global pkgname django-nose

Name:           python-django-nose
Version:        1.4.7
Release:        2%{?dist}
Summary:        Django test runner that uses nose

License:        BSD
URL:            https://github.com/jbalogh/django-nose
Source0:        https://files.pythonhosted.org/packages/source/d/%{pkgname}/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools


%global _description\
Django test runner that uses nose.

%description %_description

%package -n python3-%{pkgname}
Summary:        Django test runner that uses nose
Requires:       python3-nose
Requires:       python3-django

%description -n python3-%{pkgname} %_description

%prep
%autosetup -n %{pkgname}-%{version}

%build
%py3_build


%install
%py3_install

# remove testapp
rm -rf %{buildroot}/%{python3_sitelib}/testapp


%files -n python3-%{pkgname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/django_nose
%{python3_sitelib}/django_nose-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Sep 08 2020 Joel Capitao <jcapitao@redhat.com> - 1.4.7-2
- fix hash sum mismatch

* Tue Sep 08 2020 Joel Capitao <jcapitao@redhat.com> - 1.4.7-1
- update to 1.4.7

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.5-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.5-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.5-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.5-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Matthias Runge <mrunge@redhat.com> - 1.4.5-3
- drop Python2 subpackage for https://fedoraproject.org/wiki/Changes/Django20

* Fri Jan 26 2018 Matthias Runge <mrunge@redhat.com> - 1.4.5-2
- fix python2 requires, fix python2-django requires

* Mon Oct 23 2017 Matthias Runge <mrunge@redhat.com> - 1.4.5-1
- update to 1.4.5 (rhbz#1504626)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.3-6
- Python 2 binary package renamed to python2-django-nose
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 21 2016 Matthias Runge <mrunge@redhat.com> - 1.4.3-1
- modernize spec file, provide python3-package (rhbz#1311551)
- update to 1.4.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 04 2015 Matthias Runge <mrunge@redhat.com> - 1.4.1-1
- update to 1.4.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Matthias Runge <mrunge@redhat.com> - 1.3-2
- Convert nose optparse options to argparse

* Fri Feb 27 2015 Matthias Runge <mrunge@redhat.com> - 1.3-1
- update to 1.3
- add patch for Django-1.8 compatibility

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Matthias Runge <mrunge@redhat.com> - 1.2-1
- update to 1.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Matthias Runge <mrunge@matthias-runge.de> - 1.0-3
- update provides for django-nose

* Fri Mar 23 2012 Matthias Runge <mrunge@matthias-runge.de> - 1.0-2
- change requirement from Django to python-django

* Fri Mar 16 2012 Matthias Runge <mrunge@matthias-runge.de> - 1.0-1
- update to 1.0 from upstream
- more explicit %%files-section
- remove bundled egg-info

* Tue Jan 31 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.1.3-1
- initial packaging
