# what it's called on pypi
%global srcname python-multipart
# what it's imported as
%global libname multipart
# name of egg info directory
%global eggname python_multipart
# package name fragment
%global pkgname %{libname}

%global _description \
python-multipart is an Apache2 licensed streaming multipart parser for Python.

%if %{defined rhel}
%bcond_without python2
%bcond_without python2_tests
%bcond_without python3_other
%bcond_with    python3_other_tests
%endif

%bcond_without python3
%bcond_without python3_tests


Name:           python-%{pkgname}
Version:        0.0.5
Release:        8%{?dist}
Summary:        A streaming multipart parser for Python
License:        ASL 2.0
URL:            https://github.com/andrew-d/python-multipart
Source0:        %pypi_source
# https://github.com/andrew-d/python-multipart/pull/18
Patch0:         use-standard-library-mock-when-available.patch
BuildArch:      noarch


%description %{_description}


%if %{with python2}
%package -n python2-%{pkgname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%if %{with python2_tests}
BuildRequires:  python2-pytest
BuildRequires:  python2-mock
BuildRequires:  python2-pyyaml
BuildRequires:  python2-six
%endif
Requires:       python2-six
%{?python_provide:%python_provide python2-%{pkgname}}


%description -n python2-%{pkgname} %{_description}
%endif


%if %{with python3}
%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with python3_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-PyYAML
BuildRequires:  python%{python3_pkgversion}-six
%endif
Requires:       python%{python3_pkgversion}-six
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{_description}
%endif


%if %{with python3_other}
%package -n python%{python3_other_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
%if %{with python3_other_tests}
BuildRequires:  python%{python3_other_pkgversion}-pytest
BuildRequires:  python%{python3_other_pkgversion}-PyYAML
BuildRequires:  python%{python3_other_pkgversion}-six
%endif
Requires:       python%{python3_other_pkgversion}-six


%description -n python%{python3_other_pkgversion}-%{pkgname} %{_description}
%endif


%prep
%autosetup -n %{srcname}-%{version} -p 1
rm -rf %{eggname}.egg-info


%build
%{?with_python2:%py2_build}
%{?with_python3:%py3_build}
%{?with_python3_other:%py3_other_build}


%install
%{?with_python2:%py2_install}
%{?with_python3:%py3_install}
%{?with_python3_other:%py3_other_install}


%check
%{?with_python2_tests:PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} --verbose multipart/tests}
%{?with_python3_tests:PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} --verbose multipart/tests}
%{?with_python3_other_tests:PYTHONPATH=%{buildroot}%{python3_other_sitelib} py.test-%{python3_other_version} --verbose multipart/tests}


%if %{with python2}
%files -n python2-%{pkgname}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/%{libname}
%exclude %{python2_sitelib}/%{libname}/tests
%{python2_sitelib}/%{eggname}-%{version}-py%{python2_version}.egg-info
%endif


%if %{with python3}
%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{libname}
%exclude %{python3_sitelib}/%{libname}/tests
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info
%endif


%if %{with python3_other}
%files -n python%{python3_other_pkgversion}-%{pkgname}
%license LICENSE.txt
%doc README.rst
%{python3_other_sitelib}/%{libname}
%exclude %{python3_other_sitelib}/%{libname}/tests
%{python3_other_sitelib}/%{eggname}-%{version}-py%{python3_other_version}.egg-info
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.5-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.5-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.5-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Carl George <carl@george.computer> - 0.0.5-2
- Only build python2 subpackage on RHEL

* Sun Oct 14 2018 Carl George <carl@george.computer> - 0.0.5-1
- Initial package
