%global pypi_name lfpy
%global pretty_name LFPy

%global desc %{expand: \
LFPy is a Python-module for calculation of extracellular potentials from
multi-compartment neuron models. It relies on the NEURON simulator ( and uses
the Python interface ( it provides.LFPy provides a set of easy-to-use Python
classes for setting up your model, running your simulations and calculating the
extracellular potentials arising from activity in your model neuron. If you
have a model...}

%global py_version python3-
%global py_dist python3.8dist


Name:           python-lfpy
Version:        2.0.7
Release:        8%{?dist}
Summary:        Model extracellular potentials of multicompartment neuron models built on NEURON

License:        GPLv3
URL:            http://LFPy.readthedocs.io
Source0:        %{pypi_source %pretty_name}

# Requires NEURON, so limited to arches that NEURON and Random123 support
ExcludeArch:    mips64r2 mips32r2 s390
# Upstream does not support powerpc or 32bit arches
# https://github.com/LFPy/LFPy/issues/173
# Bug: ppc: https://bugzilla.redhat.com/show_bug.cgi?id=1838565
# Bug: armv7hl: https://bugzilla.redhat.com/show_bug.cgi?id=1838564
ExcludeArch:    %{power64} %{ix86} armv7hl


%?python_enable_dependency_generator

BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist cython}
BuildRequires:  %{py3_dist h5py}
BuildRequires:  %{py3_dist neuron}
BuildRequires:  neuron-devel
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist setuptools}

BuildRequires:  python3-mpi4py-openmpi
BuildRequires:  python3-mpi4py-mpich
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
BuildRequires:  rpm-mpi-hooks

%description
%{desc}


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{desc}

%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:   %{py3_dist h5py}
Requires:   %{py3_dist numpy}
Requires:   %{py3_dist scipy}
Requires:   %{py3_dist neuron}
Requires:   python3-mpi4py-openmpi
Requires:   python3-mpi4py-mpich

%prep
%autosetup -n %{pretty_name}-%{version}
# Remove bundled egg-info
rm -rf %{pretty_name}.egg-info

# Remove mpi4py from requirements
sed -i '/mpi4py/ d' setup.py

for lib in $(find . -type f -name "*.py"); do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%build
%py3_build

%install
%py3_install


%check
# https://github.com/LFPy/LFPy/blob/master/continuous_integration/test_script.sh#L16
%{_mpich_load}
pytest-%{python3_version} LFPy/test/test*py
%{_mpich_unload}

%{_openmpi_load}
pytest-%{python3_version} LFPy/test/test*py
%{_openmpi_unload}


# Remove unneeded test files: they include objects and libraries generated from neuron.
rm -rf %{buildroot}/%{python3_sitearch}/%{pretty_name}/test/
# Remove associated debuginfo files
rm -rf %{buildroot}/usr/lib/debug/%{python3_sitearch}/%{pretty_name}/test/


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitearch}/%{pretty_name}
%{python3_sitearch}/%{pretty_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.7-6
- Rebuilt for Python 3.9

* Thu May 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.7-5
- Re-enable tests
- Add arches that we cannot build on
- List bugs for for ExcludeArch

* Thu May 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.7-4
- Update supported architectures

* Wed May 13 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.7-3
- Cosmetic changes to spec
- Add missing Requires/BR on neuron
- Enable test
- List supported arches
- Remove unneeded test files

* Wed May 13 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.7-2
- Remove auto-generated mpi4py requires, we use explicitly mention the necessary packages in Requires

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 31 2019 Luis Bazan <lbazan@fedoraproject.org> - 2.0.3-6
- fix typos in spec

* Mon Aug 26 2019 Luis Bazan <lbazan@fedoraproject.org> - 2.0.3-5
- fix comment #14 BZ #1727491

* Mon Aug 26 2019 Luis Bazan <lbazan@fedoraproject.org> - 2.0.3-4
- fix mixed space and tabs
- non-executable script

* Mon Aug 26 2019 Luis Bazan <lbazan@fedoraproject.org> - 2.0.3-3
- fix some typos and import source

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-2
- Rebuilt for Python 3.8

* Thu Jun  6 2019 victortyau <victortyau@gmail.com> 2.0.3-1
- Initial package for fedora
