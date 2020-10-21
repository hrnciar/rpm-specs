%global pypi_name markups

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        2%{?dist}
Summary:        A wrapper around various text markups

License:        BSD
URL:            https://github.com/retext-project/pymarkups
Source0:        %{pypi_source Markups}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(markdown)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(python-markdown-math)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(textile)
BuildRequires:  python3dist(sphinx)

%description
This module provides a wrapper around various text markup languages. Available
by default are Markdown, reStructuredText and Textile, but you can easily
add your own markups.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This module provides a wrapper around various text markup languages. Available
by default are Markdown_, reStructuredText_ and Textile_, but you can easily
add your own markups.


%package -n python-%{pypi_name}-doc
Summary:        markups documentation
%description -n python-%{pypi_name}-doc
Documentation for markups


%prep
%autosetup -n Markups-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test -v

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/Markups-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Mon Jul  6 2020 José Matos <jamatos@fedoraproject.org> - 3.0.0-2
- Remove manual Requires (they are autodetected)
- Clean the Description text

* Sun May 03 2020 José Abílio Matos <jamatos@fc.up.pt> - 3.0.0-1
- Update to 3.0.0 for resubmission

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.0-11
- Subpackage python2-markups has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.0-6
- Python 2 binary package renamed to python2-markups
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 13 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 2.0-1
- New upstream version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 23 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 1.0.1-1
- New upstream version

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Sep 26 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.6.3-4
- Yet some more runtime requirements

* Thu Sep 24 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.6.3-3
- Fix runtime requirements

* Tue Sep 22 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.6.3-2
- Add python-docutils as runtime requirement

* Fri Sep 11 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.6.3-1
- New upstream version
- Disable the tests for now

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 31 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 0.5.2-4
- Fix the disttag
- Remove LICENSE from %%doc in the python3 package

* Tue Dec 30 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 0.5.2-3
- Use the %%license macro

* Sat Dec 06 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 0.5.2-2
- Some cleanup due to rpmlint warnings

* Sun Nov 30 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 0.5.2-1
- New upstream version
- Enable both Python 2 and 3

* Sun May 05 2013 Huaren Zhong <huaren.zhong@gmail.com> - 0.2.4
- Rebuild for Fedora
