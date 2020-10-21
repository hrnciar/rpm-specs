Name:           python-qcelemental
Version:        0.12.0
Release:        5%{?dist}
Summary:        Periodic table, physical constants, and molecule parsing for quantum chemistry
License:        BSD
URL:            https://github.com/MolSSI/QCElemental
Source0:        https://github.com/MolSSI/QCElemental/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(networkx)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pint)
#BuildRequires:  python3dist(py3dmol)
BuildRequires:  python3-pydantic
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-runner
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description
QCElemental is a resource module for quantum chemistry containing
physical constants and periodic table data from NIST and molecule
handlers.

Periodic Table and Physical Constants data are pulled from NIST srd144
and srd121, respectively (details) in a renewable manner (class around
NIST-published JSON file).

This project also contains a generator, validator, and translator for
Molecule QCSchema.

%package -n     python3-qcelemental
Summary:        %{summary}
%{?python_provide:%python_provide python3-qcelemental}
 
Requires:       python3dist(networkx)
Requires:       python3dist(numpy)
Requires:       python3dist(pint)
#Requires:       python3dist(py3dmol)
Requires:       python3-pydantic
Requires:       python3-pytest
Requires:       python3-pytest-cov
Requires:       python3dist(sphinx)
Requires:       python3dist(sphinx-rtd-theme)

%description -n python3-qcelemental
QCElemental is a resource module for quantum chemistry containing
physical constants and periodic table data from NIST and molecule
handlers.

Periodic Table and Physical Constants data are pulled from NIST srd144
and srd121, respectively (details) in a renewable manner (class around
NIST-published JSON file).

This project also contains a generator, validator, and translator for
Molecule QCSchema.

%prep
%setup -q -n QCElemental-%{version}
# Remove bundled egg-info
rm -rf QCElemental.egg-info

%build
%py3_build

# Build docs; doesn't work since sphinx-automodapi isn't available on Fedora
#python3 setup.py build_sphinx

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-qcelemental
%license LICENSE
%doc README.md
%{python3_sitelib}/qcelemental
%{python3_sitelib}/qcelemental-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Susi Lehtola <susi.lehtola@gmail.com> - 0.12.0-2
- Fix FTBFS: also pytest-cov is needed.

* Mon Jan 06 2020 Susi Lehtola <susi.lehtola@gmail.com> - 0.12.0-1
- Update to 0.12.0.
- Review fixes.

* Sat Jul 27 2019 Susi Lehtola <susi.lehtola@gmail.com> - 0.5.0-1
- Initial package.
