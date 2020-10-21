%bcond_without tests

# Fail to build
# Requires sphinx-automodapi
%bcond_with docs

%global pypi_name chaospy

%global desc %{expand: \
Chaospy is a numerical tool for performing uncertainty quantification using
polynomial.}

Name:           python-%{pypi_name}
Version:        3.3.8
Release:        1%{?dist}
Summary:        Numerical tool for performing uncertainty quantification using polynomial
License:        MIT
URL:            https://github.com/jonathf/chaospy
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires: pyproject-rpm-macros
BuildRequires: %{py3_dist lockfile}
BuildRequires: %{py3_dist pep517}
BuildRequires: %{py3_dist poetry}
BuildRequires: %{py3_dist scipy}
BuildRequires: %{py3_dist numpoly}

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pylint}
BuildRequires:  %{py3_dist pytest-cov}
BuildRequires:  %{py3_dist pep517}
%endif

%if %{with docs}
BuildRequires: %{py3_dist sphinx}
BuildRequires: %{py3_dist sphinxcontrib-bibtex}
%endif

Requires: %{py3_dist networkx}
Requires: %{py3_dist numpy}
Requires: %{py3_dist scipy}
Requires: %{py3_dist numpoly}
Requires: %{py3_dist scikit-learn}
Requires: %{py3_dist lockfile}
Requires: %{py3_dist pep517}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%if %{with docs}
make SPHINXBUILD=sphinx-build-3 html -C docs
rm -rf html/build/.doctrees
rm -rf html/build/.buildinfo
%endif

%install
%pyproject_install

%check
%if %{with tests}
export PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitelib}
pytest-%{python3_version} tests --deselect tests/quad/test_interface.py::test_1d_gauss_hermite_quadrature
%endif

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%files doc
%license LICENSE.txt
%doc docs/tutorials
%if %{with docs}
%doc doc/build/html
%endif

%changelog
* Wed Aug 12 2020 Luis Bazan <lbazan@fedoraproject.org> - 3.3.8-1
- New usptream version

* Sat Aug 08 2020 Luis Bazan <lbazan@fedoraproject.org> - 3.3.6-1
- New usptream version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.3.3-1
- Update to latest upstream
- Fix FTI
- Re-enable tests

* Fri Jun 26 2020 Luis Bazan <lbazan@fedoraproject.org> - 3.3.2-1
- New usptream version

* Thu Jun 04 2020 Luis Bazan <lbazan@fedoraproject.org> - 3.2.12-1
- New usptream version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.11-3
- Rebuilt for Python 3.9

* Fri May 22 2020 Luis Bazan <lbazan@fedoraproject.org> - 3.2.11-2
- Rebuild

* Wed May 13 2020 Luis Bazan <lbazan@fedoraproject.org> - 3.2.11-1
- New upstream version

* Tue Apr 21 2020 Luis Bazan <lbazan@fedoraproject.org> - 3.2.10-1
- New upstream version

* Fri Feb 28 2020 Luis Bazan <lbazan@fedoraproject.org> - 3.2.4-1
- New upstream version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Luis Bazan <lbazan@fedoraproject.org> - 3.1.1-2
- Fix Bogus date changelog

* Fri Jan 10 2020 Luis Bazan <lbazan@fedoraproject.org> - 3.1.1-1
- New upstream version

* Wed Jan 08 2020 Luis Bazan <lbazan@fedoraproject.org> - 3.1.0-1
- New upstream version

* Mon Dec 23 2019 Luis Bazan <lbazan@fedoraproject.org> - 3.0.17-1
- New upstream version

* Thu Nov 14 2019 Aniket Pradhan <major@fedoraproject.org> - 3.0.16-1
- Update to v3.0.16

* Sun Oct 27 2019 Ankur Sinha <ankursinha@fedoraproject.org> - 3.0.14-2
- Enable tests

* Fri Oct 25 2019 Ankur Sinha <ankursinha@fedoraproject.org> - 3.0.14-1
- Update to 3.0.14
- Build now uses poetry, so we use new python macros
- https://src.fedoraproject.org/rpms/pyproject-rpm-macros/tree/master

* Tue Sep 24 2019 Luis Bazan <lbazan@fedoraproject.org> - 3.0.11-3
- Rebuild

* Sat Aug 31 2019 Luis Bazan <lbazan@fedoraproject.org> - 3.0.11-2
- disable test

* Sat Aug 31 2019 Luis Bazan <lbazan@fedoraproject.org> - 3.0.11-1
- New upstream version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.7-2
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Luis Bazan <lbazan@fedoraproject.org> - 3.0.7-1
- New upstream version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.6-2
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Ankur Sinha <ankursinha@fedoraproject.org> - 3.0.6-1
- Update to new version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Luis M. Segundo <blackfile@fedoraproject.org> - 3.0.5-1
- New upstream version

* Mon Apr 08 2019 Luis Bazan <lbazan@fedoraproject.org> - 3.0.3-1
- New upstream version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Luis Bazan <lbazan@fedoraproject.org> - 2.3.5-2
- permissions fixed

* Tue Nov 27 2018 Luis Bazan <lbazan@fedoraproject.org> - 2.3.5-1
- New upstream
- change license to MIT

* Mon Nov 26 2018 Luis Bazan <lbazan@fedoraproject.org> - 2.3.4-1
- New upstream
- Fix test thanks (Ankur)
