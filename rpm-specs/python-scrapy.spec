%global pypi_name Scrapy
%global pkg_name scrapy
Name:		python-scrapy
Version:	1.5.1
Release:	9%{?dist}
Summary:	A high-level Python Screen Scraping framework

License:	BSD
URL:		http://scrapy.org
Source0:	https://files.pythonhosted.org/packages/source/S/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:	noarch


%description
Scrapy is a fast high-level screen scraping and web crawling 
framework, used to crawl websites and extract structured data 
from their pages. It can be used for a wide range of purposes,
from data mining to monitoring and automated testing.


%package -n python3-%{pkg_name}
Summary:	%{summary}

BuildRequires:	python3-devel
BuildRequires:	python3-sphinx
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	python3-cssselect
BuildRequires:	python3-lxml
BuildRequires:	python3-twisted
BuildRequires:	python3-w3lib
BuildRequires:	python3-queuelib
Requires:	python3-pyOpenSSL
Requires:	python3-twisted
Requires:	python3-lxml
Requires:	python3-w3lib
Requires:	python3-queuelib
Requires:	python3-zope-interface
Requires:	python3-cssselect
Requires:	python3-pydispatcher
Requires:	python3-parsel

%{?python_provide:%python_provide python3-%{pkg_name}}


%description -n python3-%{pkg_name}
Scrapy is a fast high-level screen scraping and web crawling 
framework, used to crawl websites and extract structured data 
from their pages. It can be used for a wide range of purposes,
from data mining to monitoring and automated testing.



%package doc
Summary:	Documentation for %{name}

%description doc
Scrapy is a fast high-level screen scraping and web crawling 
framework, used to crawl websites and extract structured data 
from their pages. It can be used for a wide range of purposes,
from data mining to monitoring and automated testing.
This package contains the documentation for %{name}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build
PYTHONPATH=$(pwd) make -C docs html
rm -f docs/build/html/.buildinfo

%install
%py3_install

%check
#Tests disabled (needs network connection)
# PYTHONPATH=$(pwd) 
# pushd bin
# ./runtests.sh
# popd
 

%files -n python3-%{pkg_name}
%license LICENSE
%doc AUTHORS PKG-INFO
%{python3_sitelib}/scrapy
%{python3_sitelib}/Scrapy-*.egg-info
%{_bindir}/scrapy

%files doc
%doc docs/build/html

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 25 2018 Eduardo Echeverria  <echevemaster@gmail.com> - 1.5.1-2
- Remove python2-scrapy as part of this process https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 13 2018 Eduardo Echeverria  <echevemaster@gmail.com> - 1.5.1-1
- Update to 1.5.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Update to 1.5.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-2
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.5.0-1
- Rebuilt for new upstream release 1.5.0, fixes rhbz #1431310
- Fixes rhbz #1478686 and rhbz #1507308

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Jan Beran <jberan@redhat.com> - 1.3.2-1
- Update to the latest upstream version
- Provides python 3 subpackage

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 1 2015 Eduardo Echeverria  <echevemaster@gmail.com> - 1.0.3-1
- Update to the latest upstream version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 5 2014 Eduardo Echeverria  <echevemaster@gmail.com> - 0.24.4-1
- Update to the latest upstream version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 19 2014 Eduardo Echeverria  <echevemaster@gmail.com> - 0.22.0-1
- Update to the latest upstream version

* Sun Jan 19 2014 Eduardo Echeverria  <echevemaster@gmail.com> - 0.20.2-1
- Initial packaging
