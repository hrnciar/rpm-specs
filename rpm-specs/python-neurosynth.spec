%global pypi_name neurosynth

# The test require internet to download data and so cannot be run in koji
# Test disable
%bcond_with tests

Name:		python-%{pypi_name}
Version:	0.3.8
Release:	2%{?dist}
Summary:	Large-scale synthesis of functional neuroimaging data

License:	MIT
URL:		https://github.com/neurosynth/neurosynth
Source0:	%{pypi_source}
BuildArch:	noarch
 
BuildRequires:	python3-devel
BuildRequires:	python3dist(biopython)
BuildRequires:	python3dist(nibabel)
BuildRequires:	python3dist(nose)
BuildRequires:	python3dist(nose) >= 0.10.1
BuildRequires:	python3dist(numpy)
BuildRequires:	python3dist(pandas)
BuildRequires:	python3dist(ply)
BuildRequires:	python3dist(scikit-learn)
BuildRequires:	python3dist(scipy)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(six)

%description
Neurosynth is a Python package for large-scale synthesis of 
functional neuroimaging data.

%package -n	python3-%{pypi_name}
Summary:	%{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:	python3dist(biopython)
Requires:	python3dist(nibabel)
Requires:	python3dist(nose) >= 0.10.1
Requires:	python3dist(numpy)
Requires:	python3dist(pandas)
Requires:	python3dist(ply)
Requires:	python3dist(scikit-learn)
Requires:	python3dist(scipy)
Requires:	python3dist(six)

%description -n	python3-%{pypi_name}
Neurosynth is a Python package for large-scale synthesis of 
functional neuroimaging data.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

for lib in $(find . -type f -name "*.py"); do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

chmod 0644 neurosynth/tests/data/sgacc_mask.nii.gz

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.8-2
- Rebuilt for Python 3.9

* Sun Feb 16 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.8-1
- Update to 0.3.8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.7-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.3.7-2
- Test need download data

* Fri Jun 14 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.3.7-1
- Initial package.
