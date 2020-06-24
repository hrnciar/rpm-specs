%global srcname drf-yasg

Name:           python-%{srcname}
Version:        1.17.0
%global pyversion %(v=%{version}; echo ${v%%.0*})
Release:        2%{?dist}
Summary:        Automated generation of real Swagger/OpenAPI 2.0 schemas from Django Rest

# Not all license texts are included: https://github.com/axnsan12/drf-yasg/issues/536
License:        BSD and MIT and ASL 2.0
URL:            https://github.com/jschneier/django-storages
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
Automated generation of real Swagger/OpenAPI 2.0 schemas
from Django Rest Framework code.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
# src/drf_yasg/static/immutable.min.js
# License(s): MIT
Provides:       bundled(js-immutable)
# src/drf_yasg/static/insQ.min.js
# License(s): MIT
Provides:       bundled(js-insertion-query) = 1.0.3
# src/drf_yasg/static/redoc/
# License(s): MIT
Provides:       bundled(js-redoc) = 2.0.0~rc.14
# src/drf_yasg/static/redoc-old/
# License(s): MIT
Provides:       bundled(js-redoc) = 1.22.3
# src/drf_yasg/static/swagger-ui-dist/
# License(s): ASL 2.0
Provides:       bundled(js-swagger-ui-dist) = 3.23.11

%description -n python3-%{srcname} %{_description}

Python 3 version.

%package     -n python3-%{srcname}+validation
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}+validation}
Provides:       python3dist(%{srcname}/validation) = %{pyversion}
Provides:       python%{python3_version}dist(%{srcname}/validation) = %{pyversion}
Requires:       python%{python3_version}dist(%{srcname}) = %{pyversion}
Requires:       python%{python3_version}dist(swagger-spec-validator) >= 2.1.0

%description -n python3-%{srcname}+validation %{_description}

"validation" extras. Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr src/*.egg-info

%build
%py3_build

%install
%py3_install

# Tests require too many dependencies
#%%check
#%%python3 -m pytest -v

%files -n python3-%{srcname}
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/drf_yasg/
%{python3_sitelib}/drf_yasg-*.egg-info/

%files -n python3-%{srcname}+validation

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.17.0-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.17.0-1
- Initial package
