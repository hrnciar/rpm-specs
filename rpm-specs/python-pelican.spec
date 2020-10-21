%global pypi_name pelican
Name:           python-%{pypi_name}
Version:        4.2.0
Release:        2%{?dist}
Summary:        A tool to generate a static blog from reStructuredText or Markdown input files

License:        AGPLv3
URL:            http://getpelican.com
Source0:        https://github.com/getpelican/pelican/archive/%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
Pelican is a static site generator, written in Python_.

* Write your weblog entries directly with your editor of choice (vim!)
  in reStructuredText_ or Markdown_
* Includes a simple CLI tool to ...

%package -n python3-%{pypi_name}
Summary:        A tool to generate a static blog from reStructuredText or Markdown input files
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Obsoletes:      python-%{pypi_name} < 3.7.1-4
Obsoletes:      python2-%{pypi_name} < 3.7.1-4
Conflicts:      python2-%{pypi_name} < 3.7.1-4
Provides:       %{pypi_name} == %{version}-%{release}

BuildRequires:  python3-devel
BuildRequires:  python3-blinker
BuildRequires:  python3-sphinx
BuildRequires:  python3-unidecode

BuildRequires:  python3-mock
BuildRequires:  python3-markdown
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-lxml
BuildRequires:  python3-six
BuildRequires:  python3-pytz
BuildRequires:  python3-jinja2
BuildRequires:  python3-django
BuildRequires:  python3-dateutil

Requires:  python3-blinker
Requires:  python3-six
Requires:  python3-unidecode
Requires:  python3-jinja2
Requires:  python3-pytz
Requires:  python3-pygments
Requires:  python3-docutils
Requires:  python3-django
Requires:  python3-markdown
Requires:  python3-feedparser
Requires:  python3-dateutil


%description -n python3-%{pypi_name}
Pelican is a static site generator, written in Python_.

* Write your weblog entries directly with your editor of choice (vim!)
  in reStructuredText_ or Markdown_
* Includes a simple CLI tool to ...


%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# make file not zero length to silence rpmlint
echo " " > pelican/themes/simple/templates/tag.html

# remove bangpath #!/usr/bin/env from files
sed -i '1d' pelican/tools/pelican_import.py
sed -i '1d' pelican/tools/pelican_quickstart.py
sed -i '1d' pelican/tools/pelican_themes.py
sed -i '1d' pelican/tools/templates/pelicanconf.py.jinja2
sed -i '1d' pelican/tools/templates/publishconf.py.jinja2

# substitute feedgenerator with it's original django
sed -i 's|feedgenerator|django.utils.feedgenerator|' pelican/writers.py
sed -i "s|'feedgenerator >= 1.9', ||" setup.py
sed -i "s|'pytz >= 0a'|'pytz'|" setup.py

%build
%py3_build

# build docs
PYTHONPATH=.:$PYTHONPATH sphinx-build-3 docs html

# remove leftovers from sphinxbuild
rm html/_downloads/*/theme-basic.zip html/_static/theme-basic.zip
rm -rf html/.doctrees html/.buildinfo


%install
%py3_install

# backwards compatibility helpers
ln -s ./pelican %{buildroot}/%{_bindir}/pelican-3
ln -s ./pelican-import %{buildroot}/%{_bindir}/pelican-import-3
ln -s ./pelican-quickstart %{buildroot}/%{_bindir}/pelican-quickstart-3
ln -s ./pelican-themes %{buildroot}/%{_bindir}/pelican-themes-3



%check
# disable tests for now. they are a bit unstable due comparing
# html attributes via diff. Failed several times, when attributes
# were ordered differently!
# nosetests-3 -sv --with-coverage --cover-package=pelican pelican

%files -n python3-%{pypi_name}
%doc html README.rst
%license LICENSE

%{_bindir}/pelican
%{_bindir}/pelican-import
%{_bindir}/pelican-quickstart
%{_bindir}/pelican-themes

%{_bindir}/pelican-3
%{_bindir}/pelican-import-3
%{_bindir}/pelican-quickstart-3
%{_bindir}/pelican-themes-3

%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*-py%{python3_version}.egg-info


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 4.2.0-1
- 4.2.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Gwyn Ciesla <limburgher@gmail.com> - 4.0.1-1
- 4.0.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.7.1-7
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Matthias Runge <mrunge@redhat.com> - 3.7.1-6
- fix python2/python3 bangpath issue (rhbz#1546755)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 12 2017 Miro Hrončok <mhroncok@redhat.com> - 3.7.1-4
- Remove the python2 subpackage (rhbz#1487848)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Matěj Cepl <mcepl@redhat.com> - 3.7.1-2
- Make build working even on EPEL7

* Thu Feb 23 2017 Matthias Runge <mrunge@redhat.com> - 3.7.1-1
- update to 3.7.1 (rhbz#1426053)

* Wed Feb 08 2017 Matthias Runge <mrunge@redhat.com> - 3.7.0-2
- remove python requirements to feedgenerator (rhbz#1379149)

* Tue Jan 03 2017 Matthias Runge <mrunge@redhat.com> - 3.7.0-1
- update to 3.7.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.6.3-7
- Rebuild for Python 3.6

* Wed Aug 03 2016 Matthias Runge <mrunge@redhat.com> - 3.6.3-6
- rename python3 executables (rhbz#1362516)
- modernize spec file

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.3-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Matthias Runge <mrunge@redhat.com> - 3.6.3-3
- properly provide python2-pelican (rhbz#1282229)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5


* Wed Nov 04 2015 Matthias Runge <mrunge@redhat.com> - 3.6.3-1
- update to 3.6.3

* Mon Jun 22 2015 Matthias Runge <mrunge@redhat.com> - 3.6.0-1
- update to 3.6.0
- add python3 support (rhbz#1227982)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Matthias Runge <mrunge@redhat.com> - 3.5.0-3
- change requirements for pytz

* Mon Mar 23 2015 Matthias Runge <mrunge@redhat.com> - 3.5.0-2
- add runtime requirement python-dateutil(rhbz#1204791)

* Tue Mar 10 2015 Matthias Runge <mrunge@redhat.com> - 3.5.0-1
- update to 3.5.0 (rhbz#1200030)

* Mon Sep 01 2014 Matthias Runge <mrunge@redhat.com> - 3.4.0-1
- update to 3.4.0
- add requires: python-feedparser (rhbz#1135665)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 21 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.3.0-4
- add Requires: python-markdown

* Wed Feb 05 2014 Matthias Rugne <mrunge@redhat.com> - 3.3.0-3
- use __python2 instead of __python
- use a tarball from github, as it significantly differs from pypi
- add tests
- build docs


* Sat Jan 25 2014 Matthias Runge <mrunge@redhat.com> - 3.3-1
- Initial package.
