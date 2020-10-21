%global pypi_name django_compressor
Name:           python-django-compressor
Version:        2.4
Release:        1%{?dist}
Summary:        Compresses linked and inline JavaScript or CSS into single cached files

License:        MIT
URL:            http://pypi.python.org/pypi/django_compressor/%{version}
Source0:        https://github.com/django-compressor/django-compressor/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

%global _description\
Django Compressor combines and compresses linked and inline Javascript\
or CSS in a Django templates into cacheable static files by using the\
``compress`` template tag.  HTML in between\
``{% compress js/css %}`` and ``{% endcompress %}`` is\
parsed and searched for CSS or JS. These styles and scripts are subsequently\
processed with optional, configurable compilers and filters.

%description %_description

%package -n python3-django-compressor
Summary:     Compresses linked and inline JavaScript or CSS into single cached files
Requires:    python3-versiontools
Requires:    python3-django-appconf
Requires:    python3-django
Requires:    python3-rjsmin
Requires:    python3-rcssmin

BuildRequires: python3-devel
BuildRequires: python3-setuptools

# Added in f28 cycle.
Obsoletes: python2-django-compressor < 2.1-6
Obsoletes: python-django-compressor < 2.1-6

%description -n python3-django-compressor
Django Compressor combines and compresses linked and inline Javascript
or CSS in a Django templates into cacheable static files by using the
``compress`` template tag.  HTML in between
``{% compress js/css %}`` and ``{% endcompress %}`` is
parsed and searched for CSS or JS. These styles and scripts are subsequently
processed with optional, configurable compilers and filters.



%prep
%autosetup -n django-compressor-%{version}

%build
%py3_build

%install
%py3_install



%files -n python3-django-compressor
%doc README.rst
%license LICENSE
%{python3_sitelib}/compressor
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Sep 09 2020 Yatin Karel <ykarel@redhat.com> - 2.4-1
- Update to 2.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Matthias Runge <mrunge@redhat.com> - 2.2-1
- update to 2.2

* Fri Jan 26 2018 Matthias Runge <mrunge@redhat.com> - 2.1-6
- Drop python2 package for https://fedoraproject.org/wiki/Changes/Django20

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1-5
- Python 2 binary package renamed to python2-django-compressor
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1-2
- Rebuild for Python 3.6

* Thu Aug 11 2016 Matthias Runge <mrunge@redhat.com> - 2.1-1
- update to 2.1 (rhbz#1365700)
- modernize spec

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 26 2016 Matthias Runge <mrunge@redhat.com> - 2.0-1
- update to 2.0 (rhbz#1296716)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 20 2015 Matthias Runge <mrunge@redhat.com> - 1.6-1
- update to 1.6 (rhbz#1283807)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Aug 27 2015 Matthias Runge <mrunge@redhat.com> - 1.5-2
- add python3 subpackage

* Wed Aug 26 2015 Matthias Runge <mrunge@redhat.com> - 1.5-1
- update to 1.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Matthias Runge <mrunge@redhat.com> - 1.4-3
- make compress command work on django-1.8

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Matthias Runge <mrunge@redhat.com> - 1.4-1
- update to 1.4 (rhbz#1100732)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 Matthias Runge <mrunge@redhat.com> - 1.3-1
- update to python-django-compressor-1.3 (rhbz#923735)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 24 2012 Matthias Runge <mrunge@redhat.com> - 1.2-3
- add requirement Django/python-django

* Fri Sep 14 2012 Matthias Runge <mrunge@redhat.com> - 1.2-2
- add requirement python-versiontools

* Tue Sep 11 2012 Matthias Runge <mrunge@redhat.com> - 1.2-1
- Initial package.
