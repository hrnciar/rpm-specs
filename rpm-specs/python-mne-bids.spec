# The test require internet to download data and so cannot be run in koji
# Confirmed all tests pass in mock with network access:
# mock -r fedora-rawhide-x86_64 rebuild ./python-mne-bids-0.1-2.fc29.src.rpm
# --enable-network --rpmbuild-opts="--with tests"
# Test disable
%bcond_with tests

%global pypi_name mne-bids

%global desc %{expand: \
This is a repository for creating BIDS compatible data-sets with MNE.
https://mne-tools.github.io/mne-bids/index.html}

Name:           python-%{pypi_name}
Version:        0.4
Release:        2%{?dist}
Summary:        Experimental code for BIDS using MNE
License:        BSD
URL:            https://github.com/mne-tools/mne-bids
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%{?python_enable_dependency_generator}

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-numpy
BuildRequires:  python3-pandas
BuildRequires:  python3-six
BuildRequires:  python3-nose
BuildRequires:  python3-scipy
BuildRequires:  python3-pytest-shutil
BuildRequires:  python3-matplotlib
BuildRequires:  python3-mne

Requires:  python3-mne
Requires:  python3-numpy
Requires:  python3-pandas
Requires:  python3-six
Requires:  python3-nose
Requires:  python3-scipy
Requires:  python3-pytest-shutil
Requires:  python3-matplotlib

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

sed -i 's/mne.externals.six/six/' mne_bids/utils.py

# remove she-bang lines in .py files.
find * -type f -name "*.py" -exec sed -i '/^#![ ]*\/usr\/bin\/.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
export PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitelib}
pytest-%{python3_version} mne_bids
%endif

# Run test require internet
# Example:
# mock -r fedora-rawhide-x86_64 rebuild ./python-mne-bids-0.1-2.fc29.src.rpm --enable-network --rpmbuild-opts="--with tests"

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst examples/README.txt
%{_bindir}/mne_bids
%{python3_sitelib}/mne_bids
%{python3_sitelib}/*-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4-2
- Rebuilt for Python 3.9

* Tue Apr 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4-1
- Update to 0.4
- Remove py2 sub-package

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 27 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.3.1-1
- New upstream version

* Tue Aug 20 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-2
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Luis M. Segundo <blackfile@fedoraproject.org> - 0.3-1
- New upstream version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2-3
- Rebuilt for Python 3.8

* Mon Apr 29 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.2-2
- Fix typo

* Mon Apr 29 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.2-1
- New upstream version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.1-2
- Fix comment 1 in BZ 1652976

* Fri Nov 23 2018 Luis Bazan <lbazan@fedoraproject.org> - 0.1-1
- New upstream
