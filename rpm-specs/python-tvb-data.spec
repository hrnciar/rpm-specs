%global pypi_name tvb-data
%global module_name tvb_data

%global desc %{expand: \
The Virtual Brain Project (TVB Project) has the purpose of offering some modern
tools to the Neurosciences community, for computing, simulating and analyzing
functional and structural data of human brains.

Various demonstration datasets for use with The Virtual Brain are provided here.
}

Name:           python-%{pypi_name}
Version:        1.5.9
Release:        4%{?dist}
Summary:        Demo data for The Virtual Brain software

License:        GPLv3+
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://github.com/the-virtual-brain/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# Not included in setup.py
Requires:       %{py3_dist numpy}
Requires:       %{py3_dist nibabel}
Requires:       %{py3_dist pillow}
Requires:       %{py3_dist scipy}
Requires:       %{py3_dist h5py}
Requires:       %{py3_dist mayavi}
Requires:       %{py3_dist networkx}

# Needs packaging but is py2 only, so we can't package it yet
# Upstream currently does not plan to migrate to py3. Trying:
# https://github.com/LTS5/cfflib/issues/7
# Leaving the cff bits in the package at the moment.
Recommends:     %{py3_dist cfflib}
# Cyclic deps. Depends on this package, so using weak deps
Recommends:     %{py3_dist tvb-library}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# Upstream included a commit to prepare for 1.5.10 in the release tar
sed -i 's/1.5.10/1.5.9/' setup.py

%build
%py3_build

%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{module_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{module_name}

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.9-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.9-1
- Update to 1.5.9
- Update autosetup command
- Fix wrong version in setup.py

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.6-8.20191229git7d2d05b
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.6-7.20191229git7d2d05b
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-6.20191229git7d2d05b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-5.20191229git7d2d05b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 06 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.6-4.20181229git7d2d05b
- Add required requires

* Sun Jan 06 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.6-3.20181229git7d2d05b
- Correct license

* Sun Jan 06 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.6-2.20181229git7d2d05b
- Remove empty check
- Add setuptools BR

* Sat Dec 29 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.6-1.20181229git7d2d05b
- Initial build
