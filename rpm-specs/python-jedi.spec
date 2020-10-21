# what it's called on pypi
%global srcname jedi
# what it's imported as
%global libname jedi
# name of egg info directory
%global eggname jedi
# package name fragment
%global pkgname jedi

%global common_description %{expand:
Jedi is a static analysis tool for Python that can be used in IDEs/editors. Its
historic focus is autocompletion, but does static analysis for now as well.
Jedi is fast and is very well tested. It understands Python on a deeper level
than all other static analysis frameworks for Python.}

%if (%{defined fedora} && 0%{?fedora} < 31) || (%{defined rhel} && 0%{?rhel} < 8)
%bcond_without  python2
%endif

%bcond_with tests

Name:           python-%{pkgname}
Version:        0.17.1
Release:        2%{?dist}
Summary:        An auto completion tool for Python that can be used for text editors
License:        MIT
URL:            https://jedi.readthedocs.org
Source0:        %pypi_source
BuildArch:      noarch


%description %{common_description}


%if %{with python2}
%package -n python2-%{pkgname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%if %{with tests}
BuildRequires:  python2-pytest >= 3.1.0
BuildRequires:  python2-docopt
BuildRequires:  python2-colorama
BuildRequires:  python2-parso >= 0.5.0
%endif
Requires:       python2-parso >= 0.5.0
%{?python_provide:%python_provide python2-%{pkgname}}


%description -n python2-%{pkgname} %{common_description}
%endif


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest >= 3.1.0
BuildRequires:  python%{python3_pkgversion}-docopt
BuildRequires:  python%{python3_pkgversion}-colorama
BuildRequires:  python%{python3_pkgversion}-parso >= 0.5.0
%endif
Requires:       python%{python3_pkgversion}-parso >= 0.5.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version} -p 1
rm -rf %{eggname}.egg-info


%build
%{?with_python2:%py2_build}
%py3_build


%install
%{?with_python2:%py2_install}
%py3_install


%if %{with tests}
%check
%{?with_python2:py.test-%{python2_version} --verbose}
py.test-%{python3_version} --verbose
%endif


%if %{with python2}
%files -n python2-%{pkgname}
%license LICENSE.txt
%doc AUTHORS.txt CHANGELOG.rst README.rst
%{python2_sitelib}/%{libname}
%{python2_sitelib}/%{eggname}-%{version}-py%{python2_version}.egg-info
%endif


%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE.txt
%doc AUTHORS.txt CHANGELOG.rst README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.17.1-1
- Update to 0.17.1

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.15.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 17 2019 Carl George <carl@george.computer> - 0.15.1-1
- Latest upstream

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-2
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Carl George <carl@george.computer> - 0.14.1-1
- Latest upstream
- Disable python2 subpackage on F31+ and EL8+ rhbz#1732815

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Carl George <carl@george.computer> - 0.12.1-2
- Remove _docdir_fmt macro to allow upgrading subpackages separately rhbz#1625015
- Standardize on srcname, modname, eggname, and pkgname macros

* Fri Aug 24 2018 Pavel Raiskup <praiskup@redhat.com> - 0.12.1-1
- new upstream version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Carl George <carl@george.computer> - 0.12.0-3
- Add patch0 to parse correct AST entry for version on Python 3.7.0b5

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-2
- Rebuilt for Python 3.7

* Mon Apr 16 2018 Carl George <carl@george.computer> - 0.12.0-1
- Latest upstream
- Enable test suite
- Share doc and license dir between subpackages

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jul 28 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.10.2-3
- Enable python3 subpackage for EPEL

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 18 2017 Carl George <carl.george@rackspace.com> - 0.10.2-1
- Latest upstream

* Mon Apr 03 2017 Carl George <carl.george@rackspace.com> - 0.10.0-1
- Latest upstream
- Upstream license changed to MIT and Python
- Align spec with Python packaging guidelines

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 07 2015 Petr Hracek <phracek@kiasportyw-brq-redhat-com> - 0.9.0-1
- new upstream version 0.9.0 (#1217032)

* Mon Jan 19 2015 Petr Hracek <phracek@redhat.com> - 0.8.1-1
- new upstream version 0.8.1 (#1178815)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Jan 06 2014 Petr Hracek <phracek@redhat.com> - 0.7.0-3
- Fix: Enable python3 subpackage (#1038398)

* Fri Aug 23 2013 Petr Hracek <phracek@redhat.com> - 0.7.0-1
- new upstream version 0.7.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Petr Hracek <phracek@redhat.com> - 0.6.0-1
- new upstream version 0.6.0

* Wed Apr 17 2013 Petr Hracek <phracek@redhat.com> - 0.5b5-3
- Test suite is available only on dev branch. It will not be used.

* Thu Apr 11 2013 Petr Hracek <phracek@redhat.com> - 0.5b5-2
- Some type warnings.
- Added dependency to python2-devel
- tests were run and 5/679 failed

* Thu Apr 11 2013 Petr Hracek <phracek@redhat.com> - 0.5b5-1
- Initial package.
