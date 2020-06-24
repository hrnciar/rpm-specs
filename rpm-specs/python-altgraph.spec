%global srcname altgraph

Name:           python-%{srcname}
Version:        0.17
Release:        2%{?dist}
Summary:        Python graph (network) package

License:        MIT
URL:            https://altgraph.readthedocs.io/
Source0:        %{pypi_source}
BuildArch:      noarch

%description
altgraph is a fork of graphlib: a graph (network) package for constructing
graphs, BFS, and DFS traversals, topological sort, shortest paths, etc. with
graphviz output.

%package -n python3-%{srcname}
Summary:  %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

Requires:       graphviz
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
altgraph is a fork of graphlib: a graph (network) package for constructing
graphs, BFS, and DFS traversals, topological sort, shortest paths, etc. with
graphviz output.

%package -n %{name}-doc
Summary:        The %{name} documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-theme-alabaster

%description -n %{name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 doc/ html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v altgraph_tests

%files -n python3-%{srcname}
%doc PKG-INFO README.rst doc/_build/html/ altgraph_tests/
%license LICENSE
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}*.egg-info/

%files -n %{name}-doc
%doc html
%license LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.17-2
- Rebuilt for Python 3.9

* Thu Mar 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.17-1
- Add doc subpackage
- Upgrade to latest upstream release 0.17 (rhbz#1792939)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.16.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 31 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.16.1-1
- Upgrade to latest upstream release 0.16.1
- Update BR (rhbz#1636263)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12-20
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.12-17
- Subpackage python2-altgraph has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12-15
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.12-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.12-10
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 06 2016 Dominika Krejci <dkrejci@redhat.com> - 0.12-8
- add Python 3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 03 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.12-5
- Update to new upstream version 0.12

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.10.1-5
- Replace the python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 10 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.1-1
- README issue fixed
- Updated to new upstream version 0.10.1

* Sat Nov 10 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.10-1
- Updated to new upstream version 0.10

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Apr 03 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.9-1
- Added new README file and docs
- Updated URL and macros
- Updated to new upstream version 0.9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 28 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.7-3
- Changed define to global 

* Sat Apr 18 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.7-2
- Removed ./
- Reworked doc part

* Sat Apr 11 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.7-1
- Initial spec for Fedora

