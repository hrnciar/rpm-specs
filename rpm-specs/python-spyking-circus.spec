# Require mpi for tests, so disabled
%bcond_with tests

%global pypi_name spyking-circus
%global modname circus
%global pmodname spyking_circus

%global _description %{expand: \
SpyKING CIRCUS is a python code to allow fast spike sorting on multi channel
recordings. A publication on the algorithm can be found at
https://elifesciences.org/articles/34518.

It has been tested on datasets coming from in vitro retina with 252 electrodes
MEA, from in vivo hippocampus with tetrodes, in vivo and in vitro cortex data
with 30 and up to 4225 channels, with good results. Synthetic tests on these
data show that cells firing at more than 0.5Hz can be detected, and their
spikes recovered with error rates at around 1%, even resolving overlapping
spikes and synchronous firing. It seems to be compatible with optogenetic
stimulation, based on experimental data obtained in the retina.}

Name:           python-%{pypi_name}
Version:        0.9.7
Release:        3%{?dist}
Summary:        Fast and scalable spike sorting of large-scale extracellular recordings

License:        CeCILL
URL:            https://pypi.org/pypi/%{pypi_name}
Source0:        %pypi_source

# We install the probe files to datadir
Patch0:         set-probe-datadir.patch
BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  /usr/bin/patch
BuildRequires:  %{py3_dist sphinx}
%if %{with tests}
BuildRequires:  %{py3_dist blosc}
BuildRequires:  %{py3_dist colorama}
BuildRequires:  %{py3_dist cython}
BuildRequires:  %{py3_dist h5py}
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist psutil}
BuildRequires:  %{py3_dist scikit-learn}
BuildRequires:  %{py3_dist statsmodels}
BuildRequires:  %{py3_dist tqdm}
%endif
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description


%package -n python3-%{pypi_name}-common
Summary:        Common files for %{name}

%description -n python3-%{pypi_name}-common %_description

# MPICH meta package
%package -n python3-%{pypi_name}-mpich
Summary:        Meta package for %{name}
Requires:       python3-mpi4py-mpich
Requires:       python3-%{pypi_name}%{?_isa} = %{version}-%{release}

%description -n python3-%{pypi_name}-mpich %_description

# OpenMPI meta package
%package -n python3-%{pypi_name}-openmpi
Summary:        Meta package for %{name}
Requires:       python3-mpi4py-openmpi
Requires:       python3-%{pypi_name}%{?_isa} = %{version}-%{release}

%description -n python3-%{pypi_name}-openmpi %_description

%package doc
Summary:        %{summary}
Requires:       python3-%{pypi_name}%{?_isa} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version} -S patch
rm -rf %{pypi_name}.egg-info

# Set the path to datadir
sed -i "s|SED_ME|%{_datadir}/%{pypi_name}/|" setup.py

# remove mpi4py from requires, we add it manually
sed -i "s/'mpi4py', //" setup.py

# Remove env
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

make -C docs_sphinx SPHINXBUILD=sphinx-build-3 html
rm -rf docs/html/{.doctrees,.buildinfo} -vf

%install
%py3_install


%if %{with tests}
%check
nosetests-%{python3_version} tests/
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{modname}
%{python3_sitelib}/%{pmodname}-%{version}-py%{python3_version}.egg-info
%{_bindir}/circus-artefacts
%{_bindir}/circus-folders
%{_bindir}/circus-gui-matlab
%{_bindir}/circus-gui-python
%{_bindir}/circus-multi
%{_bindir}/spyking-circus
%{_bindir}/spyking-circus-launcher
%{_bindir}/spyking-circus-subtask
%{_datadir}/%{pypi_name}

%files doc
%doc docs/html

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-2
- Rebuilt for Python 3.9

* Sun Apr 26 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.7-1
- Update for review
- Remove mpi4py from auto-requires: we add them explicitly for the mpi implementations
- Correct readme.txt

* Sat Apr 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.7-1
- Initial build
