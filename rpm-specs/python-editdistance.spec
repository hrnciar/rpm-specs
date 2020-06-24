%bcond_without tests

%global pypi_name editdistance

%global _description %{expand:
Fast implementation of the edit distance (Levenshtein distance).

This library simply implements Levenshtein distance with C++ and Cython.

The algorithm used in this library is proposed by Heikki Hyyrö,
"Explaining and extending the bit-parallel approximate string matching
algorithm of Myers", (2001).}

Name:           python-%{pypi_name}
Version:        0.5.3
Release:        3%{?dist}
Summary:        Fast implementation of the Levenshtein distance

License:        MIT
URL:            https://github.com/aflc/%{pypi_name}
Source0:        https://github.com/aflc/%{pypi_name}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist Cython}
BuildRequires:  gcc-c++

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# _editdistance.cpp is not generated by the Cython compiler.
find %{pypi_name}/ -name "bycython.cpp" -print -delete
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
# compile the source file "bycython.cpp" manually. setup.py does not do that itself.
cythonize --inplace %{pypi_name}/bycython.pyx
%py3_build

%install
%py3_install

%check
%if %{with tests}
export PYTHONPATH=%{buildroot}%{python3_sitearch}
pytest-%{python3_version}
%endif

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE

# own the installation directory
%dir %{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}/__init__.py
# own the __pycache__ directory
%dir %{python3_sitearch}/%{pypi_name}/__pycache__/
%{python3_sitearch}/%{pypi_name}/__pycache__/*

%{python3_sitearch}/%{pypi_name}/bycython.cpython-*.so
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%exclude %{python3_sitearch}/%{pypi_name}/*.h

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 8 2019 Aniket Pradhan <major AT fedoraproject DOT org> - 0.5.3-1
- Initial build
