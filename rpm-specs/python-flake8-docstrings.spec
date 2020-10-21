%global srcname flake8-docstrings

Name:           python-%{srcname}
Version:        1.5.0
Release:        4%{?dist}
Summary:        A plugin to flake8 to include checks provided by pep257

License:        MIT
URL:            https://gitlab.com/pycqa/%{srcname}
Source0:        https://gitlab.com/pycqa/%{srcname}/-/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
A simple module that adds an extension for the fantastic pydocstyle tool to
flake8.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined python_disable_dependency_generator}
Requires:       python%{python3_pkgversion}-flake8 >= 3
Requires:       python%{python3_pkgversion}-pydocstyle >= 2.1
%endif # python_disable_dependency_generator


%description -n python%{python3_pkgversion}-%{srcname}
A simple module that adds an extension for the fantastic pydocstyle tool to
flake8.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc HISTORY.rst README.rst
%{python3_sitelib}/flake8_docstrings.py
%{python3_sitelib}/__pycache__/flake8_docstrings.cpython-*.pyc
%{python3_sitelib}/flake8_docstrings-%{version}-py%{python3_version}.egg-info/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Scott K Logan <logans@cottsay.net> - 1.5.0-1
- Update to 1.5.0 (rhbz#1742465)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Scott K Logan <logans@cottsay.net> - 1.2.0-2
- Fix pydocstyle version requirement

* Thu Mar 21 2019 Scott K Logan <logans@cottsay.net> - 1.2.0-1
- Initial package
