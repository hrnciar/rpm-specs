%global pkgname line_profiler

Name:           python-%{pkgname}
Version:        2.1
Release:        8%{?dist}
Summary:        Line-by-line profiler for python

License:        BSD and Python
URL:            https://github.com/rkern/line_profiler
Source0:        %{url}/archive/%{version}/%{pkgname}-%{version}.tar.gz

# Support for Python 3.7:
# https://github.com/rkern/line_profiler/issues/129
Patch0:         pep479.patch

BuildRequires:  gcc

%global _description \
line_profiler is a module for doing line-by-line profiling of functions.\
kernprof is a convenient script for running either line_profiler or\
the Python standard library's cProfile or profile modules,\
depending on what is available.

%description %{_description}

%package -n     python3-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3-ipython-console
Requires:       python3-ipython-console
Conflicts:      python2-%{pkgname} < 2.1-2

%description -n python3-%{pkgname} %{_description}

Python 3 version.

%prep
%autosetup -p1 -n %{pkgname}-%{version}
sed -i -e '1{\@^#!/usr/bin/env python@d}' %{pkgname}.py kernprof.py

%build
%py3_build

%install
%py3_install


%check
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -m unittest discover -s tests -v

%files -n python3-%{pkgname}
%license LICENSE.txt LICENSE_Python.txt
%doc README.rst
%{python3_sitearch}/%{pkgname}-*.egg-info/
%{python3_sitearch}/_%{pkgname}.*.so
%{python3_sitearch}/%{pkgname}.py
%{python3_sitearch}/%{pkgname}_py35.py
%{python3_sitearch}/__pycache__/%{pkgname}.*
%{python3_sitearch}/__pycache__/%{pkgname}_py35.*
%{python3_sitearch}/kernprof.py
%{python3_sitearch}/__pycache__/kernprof.*
%{_bindir}/kernprof

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-3
- Drop Python 2 subpackage

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 16 2018 Jackson Isaac <jacksonisaac@fedoraproject.org> - 2.1-1
- Update to 2.1
- Add patch for python 3.7 - Fixes #1605752
- Update file list for python3 package to add new py35 files

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.0-2
- Bump version

* Sun Jan 15 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.0-1
- Update to 2.0
- Modernize spec

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0-10
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Jul 25 2015 Jackson Isaac <jacksonisaac2008@gmail.com> - 1.0-6
- Add Python License. Exclude __pycache__ in py3 file listing.

* Thu Jul 23 2015 Jackson Isaac <jacksonisaac2008@gmail.com> - 1.0-5
- Remove python2_sitelib definition. Remove ghost from files. 
- Add PYTHONPATH for tests. Run tests for files in tests/

* Wed Jul 22 2015 Jackson Isaac <jacksonisaac2008@gmail.com> - 1.0-4
- Rename kernprof binary instead of symlinking.

* Mon Jul 20 2015 Jackson Isaac <jacksonisaac2008@gmail.com> - 1.0-3
- Do not use py3dir as it is unclean. Use chmod instead of attr.

* Wed Jul 15 2015 Jackson Isaac <jacksonisaac2008@gmail.com> - 1.0-2
- Add compiler flags in build. Create py2 and py3 specific packages.
- Add kernprof script in buildroot for both py2 and py3 versions.

* Wed Jul  8 2015 Jackson Isaac - 1.0-1
- Initial version of line_profiler package
