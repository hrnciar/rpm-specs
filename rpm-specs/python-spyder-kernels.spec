%global pypi_name spyder-kernels

Name:           python-%{pypi_name}
Version:        1.9.1
Release:        2%{?dist}
Epoch:          1
Summary:        Jupyter kernels for the Spyder console

License:        MIT
URL:            https://github.com/spyder-ide/spyder-kernels
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(cloudpickle)
BuildRequires:  python3dist(ipykernel)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wurlitzer)

# for tests
# python3
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(flaky)
BuildRequires:  python3dist(jupyter-client)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pyzmq)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(xarray)

%description
This package provides jupyter kernels used by spyder on its IPython console.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(cloudpickle)
Requires:       python3dist(ipykernel)
Requires:       python3dist(jupyter-client)
Requires:       python3dist(pyzmq)
Requires:       python3dist(wurlitzer)

%description -n python3-%{pypi_name}
This package provides python3 version of jupyter kernels used by spyder on its
 IPython console.


%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# tests not present in pypi source
#export PYTHONPATH={buildroot}{python3_sitelib} pytest-3

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/spyder_kernels
%{python3_sitelib}/spyder_kernels-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:1.9.1-2
- Rebuilt for Python 3.9

* Thu May 07 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.9.1-1
- Update to 1.9.1

* Wed Sep 18 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.2-2
- Add wurlitzer as dependency

* Sun Sep 15 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:0.2.4-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1:0.2.4-3
- Drop python2 version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Mukundan Ragavan <nonamedotc@gmail.com> - 1:0.2.4-1
- version 0.2.4 (required for spyder 3.3.0)

* Sun Jul 08 2018 Mukundan Ragavan <nonamedotc@gmail.com> - 1.0.1-1
- Initial package for review
