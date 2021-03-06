%global srcname hypothesis

Name:           python-%{srcname}
Version:        5.29.4
Release:        1%{?dist}
Summary:        Library for property based testing

License:        MPLv2.0
URL:            https://github.com/HypothesisWorks/hypothesis-python
Source0:        %{url}/archive/%{srcname}-python-%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

# Needs pytest and others, but hypothesis is built sooner than pytest when bootstrapping
%bcond_without tests
%bcond_without doc

%if %{with doc}
# Manpage
BuildRequires:  %{_bindir}/sphinx-build
BuildRequires:  python%{python3_pkgversion}-sphinx-hoverxref
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme
%endif

%global _description \
Hypothesis is a library for testing your Python code against a much\
larger range of examples than you would ever want to write by\
hand. It’s based on the Haskell library, Quickcheck, and is designed\
to integrate seamlessly into your existing Python unit testing work\
flow.

%description %{_description}

%package     -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Obsoletes:      platform-python-%{srcname} < %{version}-%{release}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python3dist(attrs) >= 19.2.0
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(sortedcontainers)
%if %{with tests}
#BuildRequires:  python3dist(django)
#BuildRequires:  python3dist(dpcontracts)
#BuildRequires:  python3dist(lark)
BuildRequires:  black
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pexpect)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(typing-extensions)
%endif
Requires:       python%{python3_version}dist(sortedcontainers)
Suggests:       python%{python3_version}dist(pytz) >= 2014.1
Suggests:       python%{python3_version}dist(numpy) >= 1.9.0
Suggests:       python%{python3_version}dist(pytest) >= 3.0

%description -n python%{python3_pkgversion}-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{srcname}-python-%{version}/%{srcname}-python -p2
# disable Sphinx extensions that require Internet access
sed -i -e '/sphinx.ext.intersphinx/d' docs/conf.py

# remove tests we cannot run
rm -r tests/lark tests/dpcontracts # missing deps

%build
%py3_build
%if %{with doc}
PYTHONPATH=src READTHEDOCS=True sphinx-build -b man docs docs/_build/man
%endif

%install
%py3_install
%if %{with doc}
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man1 docs/_build/man/hypothesis.1
%endif

%if %{with tests}
%check
PATH=%{buildroot}%{_bindir}:$PATH PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-3 -v -n auto -k "not test_healthcheck_traceback_is_hidden"
%endif

%files -n python%{python3_pkgversion}-%{srcname}
%license ../LICENSE.txt
%doc README.rst
%{_bindir}/hypothesis
%{python3_sitelib}/hypothesis-*.egg-info
%{python3_sitelib}/hypothesis/
%if %{with doc}
%{_mandir}/man1/hypothesis.1*
%endif

%changelog
* Fri Aug 28 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.29.4-1
- Update to 5.29.4

* Fri Aug 28 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.29.3-1
- Update to 5.29.3

* Tue Aug 25 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.29.0-1
- Update to 5.29.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.20.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.20.3-1
- Update to 5.20.3

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.15.1-3
- Rebuilt for Python 3.9

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 5.15.1-2
- Bootstrap for Python 3.9

* Thu May 21 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.15.1-1
- Update to 5.15.1
- Upstream now verifies against Python 3.9 pre-releases in CI

* Sat May 16 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.14.0-1
- Update to 5.14.0

* Wed May 13 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.13.1-1
- Update to 5.13.1
- Python 3.9 fix now upstreamed

* Tue May 12 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.13.0-1
- Update to 5.13.0
- Fix NamedTuple detection on Python 3.9

* Mon May 11 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.12.0-1
- Update to 5.12.0

* Wed May  6 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.10.5-1
- Update to 5.10.5

* Sat Apr 25 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.10.4-1
- Update to 5.10.4

* Wed Apr 22 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.10.3-1
- Update to 5.10.3

* Sun Apr 12 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.8.2-1
- Update to 5.8.2

* Tue Apr  7 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.8.0-2
- Manually add requirement on sortedcontainers

* Tue Apr  7 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.8.0-1
- Update to 5.8.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.23.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Miro Hrončok <mhroncok@redhat.com> - 4.23.8-6
- Drop python2-hypothesis

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.23.8-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.23.8-4
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 4.23.8-3
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.23.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Miro Hrončok <mhroncok@redhat.com> - 4.23.8-1
- Update to 4.23.8 (#1711096)

* Thu May 09 2019 Miro Hrončok <mhroncok@redhat.com> - 4.23.4-1
- Update to 4.23.4 (#1609770)

* Sat Mar 09 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.9.0-1
- Update to 4.9.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.66.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.66.11-1
- Update to 3.66.11

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.66.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.66.0-1
- Update to 3.66.0

* Sat Jul 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.56.7-1
- Update to 3.56.7

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 3.49.0-2
- Rebuilt for Python 3.7

* Mon Mar 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.49.0-1
- Update to 3.49.0

* Mon Mar 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.47.0-1
- Update to 3.47.0

* Sun Feb 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.44.24-4
- Pick up automatic dependency from generator

* Sat Feb 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.44.24-3
- Add missing dependency on enum34

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.44.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.44.24-1
- Update to 3.44.24

* Sat Jan 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.44.18-1
- Update to 3.44.18

* Mon Jan 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.44.17-1
- Update to 3.44.17

* Sun Jan 14 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.44.16-1
- Update to 3.44.16

* Tue Jan 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.44.14-1
- Update to 3.44.14

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.44.12-1
- Update to 3.44.12

* Sun Dec 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.44.4-1
- Update to 3.44.4

* Wed Dec 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.42.2-1
- Update to 3.42.2

* Thu Nov 23 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.38.4-1
- Update to 3.38.4

* Sun Nov 19 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.38.0-1
- Update to 3.38.0

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.37.0-1
- Update to 3.37.0

* Sun Nov 12 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.36.1-1
- Update to 3.36.1

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.36.0-2
- Use better Obsoletes for platform-python

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.36.0-1
- Update to 3.36.0

* Mon Nov 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.34.1-1
- Update to 3.34.1

* Sat Nov 04 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.34.0-1
- Update to 3.34.0

* Thu Nov 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.33.1-1
- Update to 3.33.1

* Thu Aug 24 2017 Miro Hrončok <mhroncok@redhat.com> - 3.12.0-4
- Rebuilt for rhbz#1484607

* Thu Aug 10 2017 Tomas Orsava <torsava@redhat.com> - 3.12.0-3
- Added the platform-python subpackage

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.12.0-1
- Update to 3.12.0
- Reenable docs in EPEL7

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 3.4.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun May 29 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0
- Version the explicit Provides

* Wed May 04 2016 Nathaniel McCallum <npmccallum@redhat.com> - 3.1.3-1
- Update to 3.1.3
- Remove unused code
- Remove unused dependencies

* Sun Feb 14 2016 Michel Salim <salimma@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Sep 25 2015 Michel Salim <salimma@fedoraproject.org> - 1.11.2-1
- Update to 1.11.2

* Sun Sep 20 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.11.1-1
- Update to 1.11.1

* Wed Sep  2 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0

* Tue Sep  1 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.6-3
- Re-disable tests for now

* Tue Sep  1 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.6-2
- Disable Python3 tests - need debugging on ARM builders

* Mon Aug 31 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.6-1
- Update to 1.10.6
- Enable tests

* Fri Aug  7 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.0-1
- Update to 1.10

* Wed Jul 29 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Fri Jul 24 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.5-2
- Remove she-bang from tools/mergedbs.py
- Include manpage

* Fri Jul 24 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.5-1
- Update to 1.8.5
- Make Python3 build unconditional

* Thu Jul 23 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.2-1
- Initial package
