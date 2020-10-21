%global pypi_name coverage_pth

Name:           python-%{pypi_name}
Version:        0.0.2
Release:        8%{?dist}
Summary:        Coverage PTH file to enable coverage at the virtualenv level

# See github repo for license information
License:        BSD
URL:            https://github.com/dougn/coverage_pth
Source0:        %pypi_source
Source1:        https://raw.githubusercontent.com/dougn/%{pypi_name}/master/LICENSE.txt
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A .pth file to site-packages to enable coverage.py.

%package -n     python3-%{pypi_name}
Summary:        Coverage PTH file to enable coverage at the virtualenv level
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-coverage

# since there are no .py files, this is not picked automatically
Requires:       python(abi) = %{python3_version}

%description -n python3-%{pypi_name}
A .pth file to site-packages to enable coverage.py.
Python 3 version.

%prep
%autosetup -n %{pypi_name}-%{version}
cp %{SOURCE1} .

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}.pth

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.2-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.2-2
- Require python(abi)

* Fri Aug 10 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.2-1
- Update to 0.0.2
- Remove the python2 package

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 17 2016 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-2
- Add license file form Github

* Sat Mar 12 2016 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-1
- Initial package
