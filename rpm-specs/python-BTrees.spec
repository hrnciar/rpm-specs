%global srcname BTrees

# When bootstrapping a new architecture, there is no python3-ZODB-doc package
# yet, since it requires this package to build.  We only need it for building
# documentation, so use the following procedure:
# 1. Do a bootstrap build of this package.
# 2. Build python-ZODB.
# 3. Do a normal build of this packages.
%bcond_with bootstrap

Name:           python-%{srcname}
Version:        4.7.2
Release:        3%{?dist}
Summary:        Scalable persistent object containers

License:        ZPLv2.1
URL:            http://www.zodb.org/
Source0:        %pypi_source

BuildRequires:  fontawesome-fonts-web
BuildRequires:  font(fontawesome)
BuildRequires:  font(lato)
BuildRequires:  font(robotoslab)
BuildRequires:  fontconfig
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  python3-persistent-devel
BuildRequires:  python3-persistent-doc
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(repoze.sphinx.autointerface)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(transaction)
BuildRequires:  python3dist(zope.interface)
BuildRequires:  python3dist(zope.testrunner)

%if %{without bootstrap}
BuildRequires:  python-ZODB-doc
%endif

%global common_desc %{expand:
This package contains a set of persistent object containers built around
a modified BTree data structure.  The trees are optimized for use inside
ZODB's "optimistic concurrency" paradigm, and include explicit
resolution of conflicts detected by that mechanism.}

%description %{common_desc}

%package -n python3-%{srcname}
Summary:        Scalable persistent object containers

%description -n python3-%{srcname} %{common_desc}

%package        doc
Summary:        Documentation for BTrees
BuildArch:      noarch
Requires:       fontawesome-fonts-web
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)
Provides:       bundled(jquery)
Provides:       bundled(js-underscore)

%description    doc
Documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{version}

# Use local objects.inv for intersphinx
sed -e "s|\('https://docs\.python\.org/3/', \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" \
    -e "s|\('https://persistent\.readthedocs\.io/en/latest/', \)None|\1'%{_docdir}/python3-persistent-doc/objects.inv'|" \
    -i docs/conf.py

%if %{without bootstrap}
sed -e 's|\("https://zodb-docs\.readthedocs\.io/en/latest/", \)None|\1"%{_docdir}/python-ZODB-doc/html/objects.inv"|' \
    -i docs/conf.py
%endif

%build
export CFLAGS="%{optflags} -IBTrees"
%py3_build
PYTHONPATH=$PWD make -C docs html
rst2html --no-datestamp CHANGES.rst CHANGES.html
rst2html --no-datestamp README.rst README.html

# Do not bundle fonts into the documentation
cd docs/_build/html/_static/fonts
for suffix in eot svg ttf woff woff2; do
  rm fontawesome-webfont.$suffix
  ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.$suffix .
done
rm {Lato,RobotoSlab}/*.ttf
ln -s $(fc-match -f "%%{file}" "lato:bold") Lato/lato-bold.ttf
ln -s $(fc-match -f "%%{file}" "lato:bold:italic") Lato/lato-bolditalic.ttf
ln -s $(fc-match -f "%%{file}" "lato:italic") Lato/lato-italic.ttf
ln -s $(fc-match -f "%%{file}" "lato") Lato/lato-regular.ttf
ln -s $(fc-match -f "%%{file}" "robotoslab:bold") RobotoSlab/roboto-slab-v7-bold.ttf
ln -s $(fc-match -f "%%{file}" "robotoslab") RobotoSlab/roboto-slab-v7-regular.ttf
cd -

%install
%py3_install

# Remove unwanted documentation and source files; fix permissions
rm -f docs/_build/html/{.buildinfo,_static/placeholder.txt}
rm -f %{buildroot}%{python3_sitearch}/%{srcname}/*{.c,.h,~}
rm -fr %{buildroot}%{python3_sitearch}/%{srcname}/tests
chmod 0755 %{buildroot}%{python3_sitearch}/%{srcname}/*.so

%check
%{__python3} setup.py test

%files -n       python3-%{srcname}
%doc CHANGES.html README.html
%license COPYRIGHT.txt LICENSE.txt
%{python3_sitearch}/%{srcname}*

%files          doc
%doc docs/_build/html/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.7.2-2
- Rebuilt for Python 3.9

* Wed Apr  8 2020 Jerry James <loganjerry@gmail.com> - 4.7.2-1
- Version 4.7.2

* Sun Mar 22 2020 Jerry James <loganjerry@gmail.com> - 4.7.1-1
- Version 4.7.1
- Use fc-match for a more robust approach to symlinking fonts

* Wed Mar 18 2020 Jerry James <loganjerry@gmail.com> - 4.7.0-1
- Version 4.7.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Jerry James <loganjerry@gmail.com> - 4.6.1-1
- Version 4.6.1
- Add -doc subpackage
- Unbundle fonts from the documentation

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.6.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.6.0-2
- Rebuilt for Python 3.8

* Fri Aug  2 2019 Jerry James <loganjerry@gmail.com> - 4.6.0-1
- New upstream version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Jerry James <loganjerry@gmail.com> - 4.5.1-2
- Drop python2 subpackage

* Thu Aug  9 2018 Jerry James <loganjerry@gmail.com> - 4.5.1-1
- New upstream version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.5.0-2
- Rebuilt for Python 3.7

* Fri Apr 27 2018 Jerry James <loganjerry@gmail.com> - 4.5.0-1
- New upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.4.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Jerry James <loganjerry@gmail.com> - 4.4.1-1
- New upstream version

* Sat Jan 14 2017 Jerry James <loganjerry@gmail.com> - 4.4.0-1
- New upstream version

* Fri Jan  6 2017 Jerry James <loganjerry@gmail.com> - 4.3.2-1
- New upstream version

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.3.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 17 2016 Jerry James <loganjerry@gmail.com> - 4.3.1-1
- New upstream version

* Tue May 10 2016 Jerry James <loganjerry@gmail.com> - 4.3.0-1
- New upstream version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 4.2.0-1
- Update to current python packaging guidelines
- Actually package the documentation we built
- Run all the tests
- Don't ship the tests

* Fri Nov 13 2015 Jerry James <loganjerry@gmail.com> - 4.2.0-1
- New upstream version, fixes python 3.5 build

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun  8 2015 Jerry James <loganjerry@gmail.com> - 4.1.4-1
- New upstream version

* Sat May 23 2015 Jerry James <loganjerry@gmail.com> - 4.1.3-1
- New upstream version

* Tue Apr 14 2015 Jerry James <loganjerry@gmail.com> - 4.1.2-1
- New upstream version

* Mon Jan  5 2015 Jerry James <loganjerry@gmail.com> - 4.1.1-1
- New upstream version
- Drop upstreamed -overflow patch
- Use license macro

* Tue Aug 12 2014 Jerry James <loganjerry@gmail.com> - 4.0.8-2
- Add -overflow patch to fix test failures with 32-bit python 3.4

* Mon Jun  2 2014 Jerry James <loganjerry@gmail.com> - 4.0.8-1
- Initial RPM
