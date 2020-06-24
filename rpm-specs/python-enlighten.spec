%global pypi_name enlighten
%global sum  Enlighten Progress Bar
%global desc Enlighten Progress Bar is console progress bar module for Python.\
The main advantage of Enlighten is it allows writing to stdout and stderr\
without any redirection.

%bcond_without python3

# Drop Python 2 with Fedora 30 and EL8
%if (0%{?fedora} && 0%{?fedora} < 30) || (0%{?rhel} && 0%{?rhel} < 8)
  %bcond_without python2
%else
  %bcond_with python2
%endif


Name:           python-%{pypi_name}
Version:        1.6.0
Release:        2%{?dist}
Summary:        %{sum}

License:        MPLv2.0
URL:            https://github.com/Rockhopper-Technologies/enlighten
Source0:        %{pypi_source}
BuildArch:      noarch

%if 0%{?el6}
Patch0:     el6_req_fixes.patch
%endif
%if 0%{?el7}
Patch1:     el7_req_fixes.patch
%endif

%if %{with python2}
BuildRequires:  python2-setuptools
BuildRequires:  python2-devel
BuildRequires:  python2-mock

# python-blessed is unversioned in epel 6 and 7
%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires:  python-blessed
%else
BuildRequires:  python2-blessed
%endif

# Additional build requirements for Python 2.6
%if 0%{?el6}
BuildRequires:  python-ordereddict
BuildRequires:  python-unittest2
%endif
%endif

%if %{with python3}
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-blessed
%endif

%if 0%{?with_python3_other}
BuildRequires:  python%{python3_other_pkgversion}-setuptools
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-blessed
%endif

%description
%{desc}


# Python 2 package
%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{pypi_name}}

# python-blessed is unversioned in epel 6 and 7
%if 0%{?rhel} && 0%{?rhel} < 8
Requires:  python-blessed
%else
Requires:  python2-blessed
%endif

%description -n python2-%{pypi_name}
%{desc}
%endif


# Python 3 package
%if %{with python3}
%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-blessed

%description -n python%{python3_pkgversion}-%{pypi_name}
%{desc}
%endif


# Python 3 other package
%if 0%{?with_python3_other}
%package -n     python%{python3_other_pkgversion}-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{pypi_name}}
Requires:       python%{python3_other_pkgversion}-blessed

%description -n python%{python3_other_pkgversion}-%{pypi_name}
%{desc}
%endif


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%py3_build
%endif

%if 0%{?with_python3_other}
%py3_other_build
%endif


%install
%if 0%{?with_python3_other}
%py3_other_install
%endif

%if %{with python3}
%py3_install
%endif

%if %{with python2}
%py2_install
%endif


%check
%if %{with python2}
%{__python2} setup.py test
%endif

%if %{with python3}
%{__python3} setup.py test
%endif

%if 0%{?with_python3_other}
%{__python3_other} setup.py test
%endif


%if %{with python2}
%files -n python2-%{pypi_name}
%doc README*
%doc examples
%license LICENSE
%{python2_sitelib}/enlighten*
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README*
%doc examples
%license LICENSE
%{python3_sitelib}/enlighten*
%endif

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pypi_name}
%doc README*
%doc examples
%license LICENSE
%{python3_other_sitelib}/enlighten*
%endif


%changelog
* Sat Jun 20 2020 Avram Lubkin <aviso@rockhopper.net> - 1.6.0-2
- Update EL7 patch

* Fri Jun 19 2020 Avram Lubkin <aviso@rockhopper.net> - 1.6.0-1
- Update to 1.6.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-2
- Rebuilt for Python 3.9

* Sun Mar 29 2020 Avram Lubkin <aviso@rockhopper.net> - 1.5.1-1
- Update to 1.5.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Avram Lubkin <aviso@rockhopper.net> - 1.4.0-1
- Update to 1.4.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Avram Lubkin <aviso@rockhopper.net> - 1.3.0-1
- Update to 1.3.0

* Sat Mar 30 2019 Avram Lubkin <aviso@rockhopper.net> - 1.2.0-1
- Update to 1.2.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 16 2018 Avram Lubkin <aviso@rockhopper.net> - 1.1.0-1
- Update to 1.1.0

* Sun Nov 04 2018 Avram Lubkin <aviso@rockhopper.net> - 1.0.7-6
- Remove Python 2 packages in Fedora 30+ (bz#1641299)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-4
- Rebuilt for Python 3.7

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.7-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 28 2017 Avram Lubkin <aviso@rockhopper.net> - 1.0.7-1
- Update to 1.0.7

* Fri Oct 13 2017 Avram Lubkin <aviso@rockhopper.net> - 1.0.6-1
- Initial package.
