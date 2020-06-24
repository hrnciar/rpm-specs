%global srcname persistent

Name:           python-%{srcname}
Version:        4.6.4
Release:        2%{?dist}
Summary:        Translucent persistent python objects

License:        ZPLv2.1
URL:            http://www.zodb.org/
Source0:        https://github.com/zopefoundation/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  python3dist(cffi)
BuildRequires:  python3dist(manuel)
BuildRequires:  python3dist(repoze.sphinx.autointerface)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(zope.interface)
BuildRequires:  python3dist(zope.testrunner)

%global common_desc                                                        \
This package contains a generic persistence implementation for Python.  It \
forms the core protocol for making objects interact transparently with a   \
database such as python-ZODB3.

%description
%{common_desc}

%package -n python3-%{srcname}
Summary:        Translucent persistent python objects

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_desc}

%package -n python3-%{srcname}-devel
Summary:        Development files for python3-%{srcname}
Requires:       python3-%{srcname} = %{version}-%{release}
BuildArch:      noarch

%{?python_provide:%python_provide python3-%{srcname}-devel}

%description -n python3-%{srcname}-devel
Header files for building applications that use python3-%{srcname}.

%package -n python3-%{srcname}-doc
Summary:        Documentation for python3-%{srcname}
Requires:       python3-%{srcname} = %{version}-%{release}
BuildArch:      noarch

Provides:       bundled(jquery)
Provides:       bundled(js-underscore)
%{?python_provide:%python_provide python3-%{srcname}-doc}

%description -n python3-%{srcname}-doc
Documentation for python3-%{srcname}.

%prep
%autosetup -p0 -n %{srcname}-%{version}

# Update the sphinx theme name
sed -i "s/'default'/'classic'/" docs/conf.py

# Use local objects.inv for intersphinx
sed -i "s|\('https://docs\.python\.org/': \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" docs/conf.py

%build
export CFLAGS="%{optflags} -fwrapv"
%py3_build

# Build the documentation
PYTHONPATH=$(echo $PWD/build/lib.linux-*) make -C docs html

%install
%py3_install

# Remove unwanted documentation and source files; fix permissions (Python 3)
rm -f docs/_build/html/.buildinfo
rm -f %{buildroot}%{python3_sitearch}/%{srcname}/*.{c,h}
chmod 0755 %{buildroot}%{python3_sitearch}/%{srcname}/*.so

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE.txt
%{python3_sitearch}/%{srcname}*

%files -n python3-%{srcname}-devel
%{_includedir}/python3.*/%{srcname}/

%files -n python3-%{srcname}-doc
%doc docs/_build/html/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.6.4-2
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Jerry James <loganjerry@gmail.com> - 4.6.4-1
- Version 4.6.4
- Drop upstreamed -refs patch

* Thu Mar 19 2020 Jerry James <loganjerry@gmail.com> - 4.6.3-1
- Version 4.6.3
- Drop upstreamed -32bit patch

* Wed Mar 18 2020 Jerry James <loganjerry@gmail.com> - 4.6.2-1
- Version 4.6.2
- Add -refs and -32bit patches
- Build with -fwrapv to fix test failures on 32-bit systems
- Stop shipping _compat.h; BTrees has its own copy

* Thu Mar  5 2020 Jerry James <loganjerry@gmail.com> - 4.6.0-1
- Version 4.6.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov  6 2019 Jerry James <loganjerry@gmail.com> - 4.5.1-1
- Version 4.5.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.5.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.5.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Jerry James <loganjerry@gmail.com> - 4.5.0-1
- New upstream version
- Drop upstreamed -format patch

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Jerry James <loganjerry@gmail.com> - 4.4.3-1
- New upstream version
- Drop the python2 subpackage

* Mon Sep 24 2018 Jerry James <loganjerry@gmail.com> - 4.4.2-1
- New upstream version

* Tue Jul 31 2018 Jerry James <loganjerry@gmail.com> - 4.3.0-1
- New upstream version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.2.4.2-4
- Rebuilt for Python 3.7

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.2.4.2-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 20 2017 Jerry James <loganjerry@gmail.com> - 4.2.4.2-1
- New upstream version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Jerry James <loganjerry@gmail.com> - 4.2.4-1
- New upstream version

* Thu Mar  9 2017 Jerry James <loganjerry@gmail.com> - 4.2.3-1
- New upstream version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Jerry James <loganjerry@gmail.com> - 4.2.2-3
- Install a header file that upstream overlooked

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.2.2-2
- Rebuild for Python 3.6

* Fri Dec  2 2016 Jerry James <loganjerry@gmail.com> - 4.2.2-1
- New upstream version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 27 2016 Jerry James <loganjerry@gmail.com> - 4.2.1-1
- New upstream version

* Sat May  7 2016 Jerry James <loganjerry@gmail.com> - 4.2.0-1
- New upstream version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 4.1.1-3
- Comply with latest python packaging guidelines

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun  5 2015 Jerry James <loganjerry@gmail.com> - 4.1.1-1
- New upstream version

* Sat May 23 2015 Jerry James <loganjerry@gmail.com> - 4.1.0-1
- New upstream version
- Drop upstreamed -timestamp patch

* Tue Apr 14 2015 Jerry James <loganjerry@gmail.com> - 4.0.9-1
- New upstream version

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun  3 2014 Jerry James <loganjerry@gmail.com> - 4.0.8-2
- Conditionalize python 3 build
- Remove %%clean script

* Thu May 29 2014 Jerry James <loganjerry@gmail.com> - 4.0.8-1
- Initial RPM (bz 1102950)
