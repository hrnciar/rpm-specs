%global pypi_name pytest-vcr
%global file_name pytest_vcr
%global desc Py.test plugin for managing VCR.py cassettes


Name:           python-%{pypi_name}
Version:        1.0.2
Release:        7%{?dist}
Summary:        %{desc}

License:        MIT
URL:            https://pypi.python.org/pypi/pytest-vcr
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest >= 2.7
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
Requires:       python3-pytest >= 2.7
Requires:       python3-vcrpy
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}


%prep
%setup -qn %{pypi_name}-%{version}
rm -rf *.egg-info


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{file_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{file_name}.py*
%{python3_sitelib}/__pycache__/%{file_name}*.py*


%changelog
* Tue Jun 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.0.2-7
- BR python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.0.2-1
- 1.0.2

* Mon Apr 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.0.1-2
- Drop python 2.

* Thu Jan 31 2019 Gwyn Ciesla <limburgher@gmail.com> - 1.0.1-1
- 1.0.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Dec 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.3.0-2
- Source0, Requires fix.

* Thu Dec 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.3.0-1
- Inital package
