%global pypi_name django-health-check

Name:           python-%{pypi_name}
Version:        3.11.0
Release:        3%{?dist}
Summary:        Checks for various conditions and provides reports

License:        MIT
URL:            https://github.com/KristianOellegaard/django-health-check
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-sphinx

%global _description\
A Django application that provides health check capabilities.\
Many of these checks involve connecting to back-end services and ensuring\
basic operations are successful.

%description %_description

%package -n python3-%{pypi_name}
Summary:        %summary
Requires:       python3-django
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%package -n python-%{pypi_name}-doc
Summary:        Documentation for django-health-check
%description -n python-%{pypi_name}-doc
Documentation for django-health-check

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

# TODO: Enable once pytest-django is packaged
# https://lists.fedoraproject.org/archives/list/python-devel@lists.fedoraproject.org/thread/QTZIBOTA5XHNOLEF22K46XC74LZ7OQP5/
# %%check
# export DJANGO_SETTINGS_MODULE=tests.testapp.settings
# %%{__python3} -m pytest tests

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/health_check/
%{python3_sitelib}/django_health_check-*.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.11.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 David Moreau Simard <dmsimard@redhat.com> - 3.11.0-1
- First version of the package
