%global srcname django-storages

Name:           python-%{srcname}
Version:        1.8
Release:        2%{?dist}
Summary:        Support for many storage backends in Django

License:        BSD
URL:            https://github.com/jschneier/django-storages
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%package     -n python3-%{srcname}+azure
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}+azure}
Provides:       python3dist(%{srcname}/azure) = %{version}
Provides:       python%{python3_version}dist(%{srcname}/azure) = %{version}
Requires:       python%{python3_version}dist(%{srcname}) = %{version}
Requires:       (python%{python3_version}dist(azure-storage-blob) >= 1.3.1 with python%{python3_version}dist(azure-storage-blob) < 12.0.0)

%description -n python3-%{srcname}+azure %{_description}

"azure" extras. Python 3 version.

%package     -n python3-%{srcname}+boto
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}+boto}
Provides:       python3dist(%{srcname}/boto) = %{version}
Provides:       python%{python3_version}dist(%{srcname}/boto) = %{version}
Requires:       python%{python3_version}dist(%{srcname}) = %{version}
Requires:       python%{python3_version}dist(boto) >= 2.32.0

%description -n python3-%{srcname}+boto %{_description}

"boto" extras. Python 3 version.

%package     -n python3-%{srcname}+boto3
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}+boto3}
Provides:       python3dist(%{srcname}/boto3) = %{version}
Provides:       python%{python3_version}dist(%{srcname}/boto3) = %{version}
Requires:       python%{python3_version}dist(%{srcname}) = %{version}
Requires:       python%{python3_version}dist(boto3) >= 1.4.4

%description -n python3-%{srcname}+boto3 %{_description}

"boto3" extras. Python 3 version.

%package     -n python3-%{srcname}+dropbox
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}+dropbox}
Provides:       python3dist(%{srcname}/dropbox) = %{version}
Provides:       python%{python3_version}dist(%{srcname}/dropbox) = %{version}
Requires:       python%{python3_version}dist(%{srcname}) = %{version}
Requires:       python%{python3_version}dist(dropbox) >= 7.2.1

%description -n python3-%{srcname}+dropbox %{_description}

"dropbox" extras. Python 3 version.

%package     -n python3-%{srcname}+google
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}+google}
Provides:       python3dist(%{srcname}/google) = %{version}
Provides:       python%{python3_version}dist(%{srcname}/google) = %{version}
Requires:       python%{python3_version}dist(%{srcname}) = %{version}
Requires:       python%{python3_version}dist(google-cloud-storage) >= 1.15.0

%description -n python3-%{srcname}+google %{_description}

"google" extras. Python 3 version.

%package     -n python3-%{srcname}+libcloud
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}+libcloud}
Provides:       python3dist(%{srcname}/libcloud) = %{version}
Provides:       python%{python3_version}dist(%{srcname}/libcloud) = %{version}
Requires:       python%{python3_version}dist(%{srcname}) = %{version}
Requires:       python%{python3_version}dist(apache-libcloud)

%description -n python3-%{srcname}+libcloud %{_description}

"libcloud" extras. Python 3 version.

%package     -n python3-%{srcname}+sftp
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}+sftp}
Provides:       python3dist(%{srcname}/sftp) = %{version}
Provides:       python%{python3_version}dist(%{srcname}/sftp) = %{version}
Requires:       python%{python3_version}dist(%{srcname}) = %{version}
Requires:       python%{python3_version}dist(paramiko)

%description -n python3-%{srcname}+sftp %{_description}

"sftp" extras. Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info

%build
%py3_build

%install
%py3_install

# Tests require too many dependencies
#%%check
#export DJANGO_SETTINGS_MODULE=tests.settings
#%%python3 -m pytest -v tests

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python3_sitelib}/storages/
%{python3_sitelib}/django_storages-*.egg-info/

%files -n python3-%{srcname}+azure
%files -n python3-%{srcname}+boto
%files -n python3-%{srcname}+boto3
%files -n python3-%{srcname}+dropbox
# Missing dependency for google connector
#files -n python3-%{srcname}+google
%files -n python3-%{srcname}+libcloud
%files -n python3-%{srcname}+sftp

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.8-1
- Initial package
