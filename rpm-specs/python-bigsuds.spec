%{?python_enable_dependency_generator}
%global srcname bigsuds
%global sum Library for F5 Networks iControl API


%if (%{defined rhel} && 0%{?rhel} < 8) || (%{defined fedora} && 0%{?fedora} < 30)
%bcond_without python2
%endif
%bcond_without python3

Name:           python-%{srcname}
Version:        1.0.6
Release:        17%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/F5Networks/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

Patch0:         python-bigsuds-1.0.6-Fix_deps_on_suds_and_mox.patch

BuildArch:      noarch
%if 0%{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%if 0%{?el6}%{?el7}
BuildRequires:  python-suds
BuildRequires:  python-nose
BuildRequires:  python-six
%{!?el6:BuildRequires:  python-mox}
%else
BuildRequires:  python2-suds
BuildRequires:  python2-nose
BuildRequires:  python2-six
BuildRequires:  python2-mox
%endif
BuildRequires:  python2-mock
%endif
%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-suds
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-mock
# No python3-mox available, only python2 flavor
#BuildRequires:  python3-mox
BuildRequires:  python%{python3_pkgversion}-six
%endif

%description
%{sum}.

%if 0%{?with_python2}
%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}
%if %{undefined __pythondist_requires}
%if 0%{?el6}%{?el7}
Requires:       python-suds
%else
Requires:       python2-suds
%endif
%endif

%description -n python2-%{srcname}
%{sum}.
%endif

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-suds
%endif

%description -n python%{python3_pkgversion}-%{srcname}
%{sum}.
%endif


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove erroneous shebang
sed -i -e '/^#!\//, 1d' bigsuds.py


%build
%{?with_python2:%py2_build}
%{?with_python3:%py3_build}


%install
%{?with_python2:%py2_install}
%{?with_python3:%py3_install}

%check
%{?with_python2:%{__python2} test_bigsuds.py}
%{?with_python3:%{__python3} test_bigsuds.py}


%if 0%{?with_python2}
%files -n python2-%{srcname}
%license LICENSE
%doc CHANGELOG README.md TERMS_OF_USE
%{python2_sitelib}/*
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc CHANGELOG README.md TERMS_OF_USE
%{python3_sitelib}/*
%endif


%changelog
* Mon Oct 05 2020 Xavier Bachelot <xavier@bachelot.org> - 1.0.6-17
- Explicitely BR: python-setuptools

* Fri Aug 14 2020 Xavier Bachelot <xavier@bachelot.org> - 1.0.6-16
- Fix FTI on F33 (RHBZ#1838948)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-14
- Rebuilt for Python 3.9

* Tue May 12 2020 Xavier Bachelot <xavier@bachelot.org> - 1.0.6-13
- Fix FTI on F32 (RHBZ#1834086)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.6-7
- Enable python dependency generator

* Tue Jan 08 2019 Xavier Bachelot <xavier@bachelot.org> - 1.0.6-6
- Enable python3 build on EL7.

* Fri Sep 28 2018 Xavier Bachelot <xavier@bachelot.org> - 1.0.6-5
- Don't build python2 sub-package for Fedora 30 and EL8 (RHBZ#1630949).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Xavier Bachelot <xavier@bachelot.org> - 1.0.6-3
- Fix Requires: on EL.

* Fri Jul 06 2018 Xavier Bachelot <xavier@bachelot.org> - 1.0.6-2
- Fix typo.

* Wed Dec 13 2017 Xavier Bachelot <xavier@bachelot.org> - 1.0.6-1
- Initial package.
