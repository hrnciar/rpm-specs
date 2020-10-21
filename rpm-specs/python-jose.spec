%global pypi_name python-jose
%global srcname jose
%global _summary JOSE implementation in Python

Name:           python-%{srcname}
Version:        3.2.0
Release:        1%{?dist}
Summary:        %{_summary}

License:        MIT
URL:            http://github.com/mpdavis/python-jose
Source0:        %{pypi_source %pypi_name}
# Due to version of ecdsa 0.15, which is available in YUM repo already
# https://github.com/mpdavis/python-jose/issues/176#issuecomment-642352816
Patch0:         disable-test_key_too_short.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(six) < 2.0
# Backends
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(pycryptodomex) < 4.0.0
BuildRequires:  python3dist(pycryptodomex) >= 3.3.1
BuildRequires:  python3dist(ecdsa) < 1.0
BuildRequires:  python3dist(rsa)
BuildRequires:  python3dist(pyasn1)
BuildRequires:  python3dist(pycrypto) >= 2.6.0
BuildRequires:  python3dist(pycrypto) < 2.7.0
# Run tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-runner)

%description
A JOSE implementation in Python

The JavaScript Object Signing and Encryption (JOSE) technologies - JSON Web
Signature (JWS), JSON Web Encryption (JWE), JSON Web Key (JWK), and JSON Web
Algorithms (JWA) - collectively can be used to encrypt and/or sign content
using a variety of algorithms. While the full set of permutations is extremely
large, and might be daunting to some, it is expected that most applications
will only use a small set of algorithms to meet their needs.

Documentation: https://python-jose.readthedocs.org/en/latest/

%package -n     python3-%{srcname}
Summary:        %{_summary}
%{?python_provide:%python_provide python3-%{srcname}}
 
Requires:       python3dist(ecdsa) < 1.0
Requires:       python3dist(pyasn1)
Requires:       python3dist(rsa)
Requires:       python3dist(six) < 2.0

%description -n python3-%{srcname}
A JOSE implementation in Python

The JavaScript Object Signing and Encryption (JOSE) technologies - JSON Web
Signature (JWS), JSON Web Encryption (JWE), JSON Web Key (JWK), and JSON Web
Algorithms (JWA) - collectively can be used to encrypt and/or sign content
using a variety of algorithms. While the full set of permutations is extremely
large, and might be daunting to some, it is expected that most applications
will only use a small set of algorithms to meet their needs.

Documentation: https://python-jose.readthedocs.org/en/latest/

%package -n     python3-%{srcname}-cryptography
Summary:        %{_summary} with cryptography backend
%{?python_provide:%python_provide python3-%{srcname}-cryptography}

Requires:       python3-jose = %{version}-%{release}
Requires:       python3dist(cryptography)

%description -n python3-%{srcname}-cryptography
Please refer to the description of python3-%{srcname}

%package -n     python3-%{srcname}-pycrypto
Summary:        %{_summary} with pycrypto backend
%{?python_provide:%python_provide python3-%{srcname}-pycrypto}

Requires:       python3-jose = %{version}-%{release}
Requires:       python3dist(pycrypto) >= 2.6.0
Requires:       python3dist(pycrypto) < 2.7.0

%description -n python3-%{srcname}-pycrypto
Please refer to the description of python3-%{srcname}

%package -n     python3-%{srcname}-pycryptodome
Summary:        %{_summary} with pycryptodome backend
%{?python_provide:%python_provide python3-%{srcname}-pycryptodome}

Requires:       python3-jose = %{version}-%{release}
Requires:       python3dist(pycryptodomex) >= 3.3.1
Requires:       python3dist(pycryptodomex) < 4.0.0

%description -n python3-%{srcname}-pycryptodome
Please refer to the description of python3-%{srcname}

%prep
%setup -q -n %{pypi_name}-%{version}
%patch0 -p0
sed -i 's#ecdsa <0.15#ecdsa#' setup.py

rm -rf python_jose.egg-info

%build
%py3_build

%install
%py3_install

%check
# Test base
python3 -m pytest \
    -m "not (cryptography or pycryptodome or pycrypto or backend_compatibility)" \
    tests

# Test the pyca/cryptography backend
python3 -m pytest \
    -m "not (pycryptodome or pycrypto or backend_compatibility)" \
    tests

# Test the pycryptodome backend
python3 -m pytest \
    -m "not (cryptography or pycrypto or backend_compatibility)" \
    tests

# Test the pycrypto backend
python3 -m pytest \
    -m "not (cryptography or pycryptodome or backend_compatibility)" \
    tests

# Test cross-backend compatibility and coexistence
python3 -m pytest tests

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/jose/
%{python3_sitelib}/python_jose-%{version}-py*.egg-info

%files -n python3-%{srcname}-cryptography
%doc README.rst

%files -n python3-%{srcname}-pycrypto
%doc README.rst

%files -n python3-%{srcname}-pycryptodome
%doc README.rst

%changelog
* Mon Oct  5 23:59:32 -03 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.2.0-1
- 3.2.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 17 2020 Chenxiong Qi <qcxhome@gmail.com> - 3.1.0-1
- Initial package.
