# Created by pyp2rpm-3.3.4
%global pypi_name dkimpy

# Tests are missing from pypi tarball
%bcond_with check

Name:           python-%{pypi_name}
Version:        1.0.5
Release:        1%{?dist}
Summary:        DKIM, ARC, and TLSRPT email signing and verification

License:        zlib
URL:            https://launchpad.net/dkimpy
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiodns)
BuildRequires:  python3dist(authres)
BuildRequires:  python3dist(dnspython) >= 1.16
BuildRequires:  python3dist(pynacl)
BuildRequires:  python3dist(setuptools)

%description
dkimpy is a library that implements DKIM (DomainKeys Identified Mail)
email signing and verification.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
dkimpy is a library that implements DKIM (DomainKeys Identified Mail)
email signing and verification.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Drop shebang for these files, as we don't need them
sed -e "s|#!/usr/bin/env python||" -i dkim/{arcsign.py,arcverify.py,dkimsign.py,dkimverify.py,dknewkey.py}

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/arcsign
%{_bindir}/arcverify
%{_bindir}/dkimsign
%{_bindir}/dkimverify
%{_bindir}/dknewkey
%{_mandir}/man1/arcsign.1*
%{_mandir}/man1/arcverify.1*
%{_mandir}/man1/dkimsign.1*
%{_mandir}/man1/dkimverify.1*
%{_mandir}/man1/dknewkey.1*
%{python3_sitelib}/dkim/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Oct 12 2020 Neal Gompa <ngompa13@gmail.com> - 1.0.5-1
- Initial package.
