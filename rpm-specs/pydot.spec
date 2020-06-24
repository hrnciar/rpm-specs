%global common_desc								\
An interface for creating both directed and non directed graphs from Python.	\
Currently all attributes implemented in the Dot language are supported (up	\
to Graphviz 2.16).								\
										\
Output can be inlined in Postscript into interactive scientific environments	\
like TeXmacs, or output in any of the format's supported by the Graphviz	\
tools dot, neato, twopi.

Name:		pydot
Version:	1.4.1
Release:	3%{?dist}
Summary:	Python interface to Graphviz's Dot language

License:	MIT
URL:		https://github.com/erocarrera/pydot
Source0:	https://github.com/erocarrera/pydot/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch

%description
%{common_desc}

%package -n python3-%{name}
Summary:	Python3 interface to Graphviz's Dot language

BuildRequires:	python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(chardet)
BuildRequires:  python3dist(nose)
BuildRequires:	python3dist(pyparsing)
BuildRequires:	python3dist(setuptools)
BuildRequires:	graphviz
Requires:	graphviz

Provides:	%{name} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
%{common_desc}

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%check
EXCLUDE_ARG=""
EXCLUDE_ARG="$EXCLUDE_ARG -e test_graph_with_shapefiles -e test_graphviz_regression_tests -e test_my_regression_tests"
PYTHONPATH=%{buildroot}%{python3_sitelib} nosetests-%{python3_version} -v test/pydot_unittest.py $EXCLUDE_ARG

%files -n python3-%{name}
%doc ChangeLog README.md
%license LICENSE
%{python3_sitelib}/dot_parser.*
%{python3_sitelib}/pydot.*
%{python3_sitelib}/__pycache__/dot_parser.*
%{python3_sitelib}/__pycache__/pydot.*
%{python3_sitelib}/pydot-%{version}-py%{python3_version}.egg-info/

%changelog
* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 26 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.1-1
- Update check section
- Update to latest upstream release 1.4.1 

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.4-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.4-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.4-5
- Enable python dependency generator

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.4-4
- Subpackage python2-pydot has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Oct 15 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.2.4-3
- Bring the Python 2 subpackage back (#1637711).

* Mon Oct  1 2018 Tom Callaway <spot@fedoraproject.org> - 1.2.4-2
- just py3

* Wed Sep 12 2018 Jerry James <loganjerry@gmail.com> - 1.2.4-1
- update to 1.2.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.28-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.28-18
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.28-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.28-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.28-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.28-14
- Rebuild for Python 3.6

* Mon Oct 17 2016 Björn Esser <fedora@besser82.io> - 1.0.28-13
- Drop obsolete stuff
- Move %%description to a common macro
- Add conditionals to build on epel
- Clean trailing whitespaces

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.28-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Apr 15 2016 Tom Callaway <spot@fedoraproject.org> - 1.0.28-11
- use debian's python3 fix (tested against bz1312815)

* Fri Apr  8 2016 Tom Callaway <spot@fedoraproject.org> - 1.0.28-10
- properly obsolete old "pydot" packages (bz1323980)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Tom Callaway <spot@fedoraproject.org> - 1.0.28-8
- python 3 support

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec  9 2013 Tom Callaway <spot@fedoraproject.org> - 1.0.28-5
- fix for pyparsing2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar  2 2012 Tom Callaway <spot@fedoraproject.org> - 1.0.28-1
- update to 1.0.28

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 11 2011 Tom Callaway <spot@fedoraproject.org> - 1.0.25-2
- apply fix for pebl relating to catching AttributeError, thanks to Thomas Spura

* Thu Apr 21 2011 Tom Callaway <spot@fedoraproject.org> - 1.0.25-1
- update to 1.0.25

* Thu Mar  3 2011 Tom Callaway <spot@fedoraproject.org> - 1.0.23-1
- update to 1.0.23

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan  4 2011 Tom Callaway <spot@fedoraproject.org> - 1.0.4-1
- update to 1.0.4

* Wed Nov  3 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.3-1
- update to 1.0.3

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 31 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.2-6
- somehow, the egg info didn't make it into the rebuild...

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul  6 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.2-4
- fix pydot crash with accented character (bugzilla 481540)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.2-2
- Rebuild for Python 2.6

* Fri Sep 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.2-1
- update to 1.0.2

* Thu Dec 14 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.9.10-5
- Rebuild for new Python
- Add BR: python-devel

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.10-4
- bump for fc6

* Thu Oct  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.10-3
- We really do need pyparsing as a BR

* Thu Oct  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.10-2
- change BR to R for graphviz, pyparsing

* Sat Sep 17 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.10-1
- initial package for Fedora Extras
