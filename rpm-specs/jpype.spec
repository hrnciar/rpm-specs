%bcond_with doc

%global srcurl  https://github.com/jpype-project/%{name}
%global sum     Full access for Python programs to Java class libraries

Name:           jpype
Version:        0.7.5
Release:        1%{?dist}
Summary:        %{sum}

# Some files come from JDK (jni_md.h) and Python (capsulethunk.h)
License:        ASL 2.0 and GPLv2 and Python
URL:            http://www.%{name}.org
Source0:        %{srcurl}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++

BuildRequires:  python-rpm-macros

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-mock

BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme
BuildRequires:  python%{python3_pkgversion}-readthedocs-sphinx-ext

BuildRequires:  java-devel ant
# define _jsdir macro
BuildRequires:  web-assets-devel

%global _description \
JPype is an effort to allow python programs full access to\
java class libraries. This is achieved not through\
re-implementing Python, as Jython/JPython has done, but rather \
through interfacing at the native level in both Virtual Machines.

%description
%_description

%package -n python%{python3_pkgversion}-%{name}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}

%description -n python%{python3_pkgversion}-%{name}
%_description

This is the package with support for Python version %{python3_version}.

%package doc
Summary:         Documentation files for %{name}
BuildArch:       noarch
Requires:        js-jquery >= 3

%description doc
%{summary}.


%prep
%autosetup -p1 -n%{name}-%{version}
# sanify line delimiters
find . -name '*.py' -or -name '*.java' -or -name '*.TXT' \
 -or -name '*.sh' -or -name '*.xml' -or -name '*.js' \
 |xargs sed -i "s|\r||g"
# unittest2 is not needed for python3 only
sed -i "s|'unittest2'||" setup.py
sed -i -r "s|(import unittest)2 as unittest|\1|" test/jpypetest/*.py


%build
%py3_build

# generate html documentation
%if %{with doc}
sphinx-build-3 -d doctrees doc html
rm html/.buildinfo
# unbundle jquery, https://fedoraproject.org/wiki/Changes/jQuery
rm -v html/_static/jquery*.js
ln -fs %{_jsdir}/jquery/3/jquery.min.js html/_static/jquery.js
%endif


%install
%py3_install
find %{buildroot} -name '*.so' |xargs chmod 0755


%check
pushd test/%{name}test
# FIXME skip b0rken tests, maybe due to jdk8?
rm test_leak.py test_legacy.py
rm test_module.py test_properties.py
rm test_shutdown.py test_startup.py
rm test_proxy.py
popd
%{__python3} setup.py test
ant -f test/build.xml


%files -n python%{python3_pkgversion}-%{name}
%license LICENSE
%doc AUTHORS.rst README.rst
%{python3_sitearch}/_%{name}.cpython-*.so
%{python3_sitearch}/%{name}/
%{python3_sitearch}/JPype1-%{version}-py%{python3_version}.egg-info/

%files doc
%license LICENSE
%doc examples/
%if %{with doc}
%doc html/
%else
%doc doc/*.rst doc/*.png doc/*.py
%endif


%changelog
* Sat Jun 06 2020 Raphael Groner <raphgro@fedoraproject.org> - 0.7.5-1
- bump to v0.7.5

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-2
- Rebuilt for Python 3.9

* Sat May 02 2020 Raphael Groner <raphgro@fedoraproject.org> - 0.7.4-1
- bump to v0.7.4
- skip generation of documentation with odd python bug
- skip b0rken tests with jdk8
- drop useless comments

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Raphael Groner <projects.rg@smart.ms> - 0.7.1-1
- new version

* Thu Oct 03 2019 Raphael Groner <projects.rg@smart.ms> - 0.7-4
- use unittest instead of unittest2 for python3 only

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-2
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Raphael Groner <projects.rg@smart.ms> - 0.7.0-1
- new version
- new upstream
- drop obsolete patch
- use right python version in BR: sphinx
- drop build conditionals
- adjust execution of tests
- add explicit folder names for sitearch

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Raphael Groner <projects.rg@smart.ms> - 0.6.3-7
- drop deprecated python2, bug #1626632

* Thu Jul 19 2018 Raphael Groner <projects.rg@smart.ms> - 0.6.3-6
- add BuildRequires: gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 Raphael Groner <projects.rg@smart.ms> - 0.6.3-4
- Rebuild for Python 3.7, another try

* Fri Jun 22 2018 Raphael Groner <projects.rg@smart.ms> - 0.6.3-3
- revert back to jquery v3.x because bundled has v3.2.1

* Fri Jun 22 2018 Raphael Groner <projects.rg@smart.ms> - 0.6.3-2
- add BR to define _jsdir macro
- exclude test sources due to inconsistent mtime of pyc file
- use js-jquery2 for compatibility

* Thu Jun 21 2018 Raphael Groner <projects.rg@smart.ms> - 0.6.3-1
- new version
- add patch for upcoming python 3.7
- drop compatibility for retired branches

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-5
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.2-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Aug 16 2017 Raphael Groner <projects.rg@smart.ms> - 0.6.2-2
- revert accidently disabled python2

* Tue Aug 15 2017 Raphael Groner <projects.rg@smart.ms> - 0.6.2-1
- new version
- [epel7] enable python3, disable sphinx due to strange bug

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Sep 10 2015 Raphael Groner <projects.rg@smart.ms> - 0.6.1-1
- new upstream release v0.6.1
- make tests work with python3
- deprecation of jpype-py3
- split subpackages for python2 and 3
- use python build and install macros
- ease html generation
- ship _static documentation files
- unbundle jquery
- ship tests folder as an import option w/o execution bits
- restrict documentation to only some .rst files

* Tue Jul 21 2015 Raphael Groner <projects.rg@smart.ms> - 0.6.0-2
- include patch of proxy argument issue

* Tue Jun 23 2015 Raphael Groner <projects.rg@smart.ms> - 0.6.0-1
- based on originally jpype-py3.spec
- official jpype 0.6.0 with python3
- more documentation in subpackage

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.20150202gitca6fc96
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Raphael Groner <projects.rg@smart.ms> - 0-0.2.20150202gitca6fc96
- add GPLv2 for bundled source files
- remove wrong sitearch macro
- make tests work

* Thu Apr 02 2015 Raphael Groner <projects.rg@smart.ms> - 0-0.1.20150202gitca6fc96
- initial
