%global srcname adal
%global common_description The ADAL for Python library makes it easy for python applications to\
authenticate to AAD in order to access AAD protected web resources.

%global _with_python2 0%{?rhel} || 0%{?fedora} <= 29
%global py2_prefix %{?rhel:python}%{?fedora:python2}
%global _with_py2_tests 1
%global _with_python3 1
# httpretty library is not available for Python 3 in EL
%global _with_py3_tests 0%{?fedora}
# Sphinx version provided by EL is missing the imgmath extension
%global _with_doc 0%{?fedora}
%global pydoc_prefix %{?rhel:python}%{?fedora:python%{python3_pkgversion}}
%global sphinxbuild sphinx-build%{?fedora:-%{python3_version}}

Name:           python-%{srcname}
Version:        1.2.2
Release:        5%{?dist}
Summary:        ADAL for Python

License:        MIT
URL:            https://github.com/AzureAD/azure-activedirectory-library-for-python
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Fix tests with httpretty >= 0.9.0
Patch0:         %{name}-1.2.0-tests.patch

%if 0%{?_with_python2}
BuildRequires:  %{py2_prefix}-devel
BuildRequires:  %{py2_prefix}-setuptools
%if 0%{?_with_py2_tests}
BuildRequires:  %{py2_prefix}-cryptography
BuildRequires:  %{py2_prefix}-dateutil
BuildRequires:  %{py2_prefix}-httpretty
BuildRequires:  %{py2_prefix}-jwt
BuildRequires:  %{py2_prefix}-mock
BuildRequires:  %{py2_prefix}-requests
BuildRequires:  %{?!rhel:%{py2_prefix}-}pytest
%endif
%endif
%if 0%{?_with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if 0%{?_with_py3_tests}
BuildRequires:  python%{python3_pkgversion}-cryptography
BuildRequires:  python%{python3_pkgversion}-dateutil
BuildRequires:  python%{python3_pkgversion}-httpretty
BuildRequires:  python%{python3_pkgversion}-jwt
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-pytest
%endif
%endif
%if 0%{?_with_doc}
BuildRequires:  %{pydoc_prefix}-sphinx
BuildRequires:  %{pydoc_prefix}-sphinx_rtd_theme
%endif
BuildArch:      noarch

%description
%{common_description}


%if 0%{?_with_python2}
%package -n python2-%{srcname}
Summary:        %{summary}
Requires:       %{py2_prefix}-cryptography
Requires:       %{py2_prefix}-dateutil
Requires:       %{py2_prefix}-jwt
Requires:       %{py2_prefix}-requests
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{common_description}
%endif


%if 0%{?_with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
Requires:       python%{python3_pkgversion}-cryptography
Requires:       python%{python3_pkgversion}-dateutil
Requires:       python%{python3_pkgversion}-jwt
Requires:       python%{python3_pkgversion}-requests
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
%{common_description}
%endif


%if 0%{?_with_doc}
%package doc
Summary:        Documentation for %{name}

%description doc
This package provides documentation for %{name}.
%endif


%prep
%autosetup -p0 -n azure-activedirectory-library-for-python-%{version}


%build
%if 0%{?_with_python2}
%py2_build
%endif
%if 0%{?_with_python3}
%py3_build
%endif

%if 0%{?_with_doc}
%make_build -C docs/ html SPHINXBUILD=%{sphinxbuild}
rm docs/build/html/{.buildinfo,.nojekyll}
%endif


%install
%if 0%{?_with_python2}
%py2_install
%endif
%if 0%{?_with_python3}
%py3_install
%endif


%check
%if 0%{?_with_python2} && 0%{?_with_py2_tests}
py.test-%{python2_version}
%endif
%if 0%{?_with_python3} && 0%{?_with_py3_tests}
py.test-%{python3_version}
%endif


%if 0%{?_with_python2}
%files -n python2-%{srcname}
%doc README.md
%license LICENSE
%{python2_sitelib}/%{srcname}/
%{python2_sitelib}/%{srcname}-*.egg-info/
%endif


%if 0%{?_with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/
%endif


%if 0%{?_with_doc}
%files doc
%doc docs/build/html/
%license LICENSE
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-2
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2
- Add sphinx_rtd_theme build dependency for docs generation (fix by Charalampos
  Stratakis)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2.0-2
- Build documentation

* Sat Nov 10 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0
- Enable Python 3 support for EL
