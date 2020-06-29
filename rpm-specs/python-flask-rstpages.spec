# Created by pyp2rpm-1.1.1
%global pypi_name Flask-RSTPages

%if 0%{?fedora}
%else
# EL doesn't have Python 3
%global with_python3 0
%endif

%if 0%{?rhel} && 0%{?rhel} < 7
%global python2_sitelib %{python_sitelib}
%endif

Name:           python-flask-rstpages
Version:        0.3
Release:        22%{?dist}
Summary:        Adds support for reStructuredText to a Flask application
License:        BSD
URL:            http://flask-rstpages.readthedocs.org/
Source0:        https://pypi.python.org/packages/source/F/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-sphinx

BuildRequires:  python3-devel
BuildRequires:  python3-flask
BuildRequires:  python3-sphinx

%global _description\
Flask-RSTPages adds support for reStructuredText\
to your Flask application.

%description %_description

%package -n     python3-flask-rstpages
Summary:        Adds support for reStructuredText to a Flask application
Requires:       python3-flask
Requires:       python3-pygments
Requires:       python3-docutils

%description -n python3-flask-rstpages
Flask-RSTPages adds support for reStructuredText
to your Flask application.


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# generate html docs
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
# generate html docs
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%build

%{__python3} setup.py build


%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%{__python3} setup.py install --skip-build --root %{buildroot}

%files -n python3-flask-rstpages
%doc html LICENSE
%{python3_sitelib}/flask_rstpages
%{python3_sitelib}/Flask_RSTPages-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3-22
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-20
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-19
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3-16
- Subpackage python2-flask-rstpages has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3-14
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3-11
- Python 2 binary package renamed to python2-flask-rstpages
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 24 2014 Richard Marko <rmarko@fedoraproject.org> - 0.3-3
- Add conditionals for EPEL

* Thu Oct 16 2014 Richard Marko <rmarko@fedoraproject.org> - 0.3-2
- Corrected packaging errors.

* Wed Oct 01 2014 Richard Marko <rmarko@fedoraproject.org> - 0.3-1
- Initial package.
