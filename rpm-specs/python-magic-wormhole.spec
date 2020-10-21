%{?python_enable_dependency_generator}

%global pypi_name magic-wormhole

%global common_description %{expand:
Get things from one computer to another, safely.

This package provides a library and a command-line tool named wormhole,
which makes it possible to get arbitrary-sized files and directories
(or short pieces of text) from one computer to another. The two
endpoints are identified by using identical "wormhole codes": in
general, the sending machine generates and displays the code, which must
then be typed into the receiving machine.

The codes are short and human-pronounceable, using a
phonetically-distinct wordlist. The receiving side offers tab-completion
on the codewords, so usually only a few characters must be typed.
Wormhole codes are single-use and do not need to be memorized.}

Name:           python-%{pypi_name}
Summary:        Securely transfer data between computers
Version:        0.12.0
Release:        3%{?dist}
License:        MIT

URL:            https://github.com/warner/magic-wormhole
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

# requirements for building the docs
BuildRequires:  python3dist(recommonmark)
BuildRequires:  python3dist(sphinx)

# requirements for running the tests
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(humanize)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pynacl)
BuildRequires:  python3dist(service-identity)
BuildRequires:  python3dist(tqdm) >= 4.13

# common dependencies
BuildRequires:  python3dist(autobahn) >= 0.14.1
BuildRequires:  python3dist(hkdf)
BuildRequires:  python3dist(magic-wormhole-mailbox-server)
BuildRequires:  python3dist(magic-wormhole-transit-relay)
BuildRequires:  python3dist(spake2) = 0.8
BuildRequires:  python3dist(twisted) >= 17.5
BuildRequires:  python3dist(txtorcon) >= 18.0.2

%description %{common_description}


%package -n     magic-wormhole
Summary:        %{summary}

Requires:       python3-%{pypi_name}

%description -n magic-wormhole %{common_description}

This package contains the wormhole program.


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{common_description}


%package -n     python-%{pypi_name}-doc
Summary:        Documentation for %{name}
%description -n python-%{pypi_name}-doc %{common_description}

This package contains the documentation.


%prep
%autosetup -n %{pypi_name}-%{version} -p1

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html

# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%check
%{__python3} setup.py test


%files -n magic-wormhole
%license LICENSE
%doc README.md

%{_bindir}/wormhole


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md

%{python3_sitelib}/wormhole/
%{python3_sitelib}/magic_wormhole-%{version}-py%{python3_version}.egg-info


%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-2
- Rebuilt for Python 3.9

* Sun Apr 05 2020 Fabio Valentini <decathorpe@gmail.com> - 0.12.0-1
- Update to version 0.12.0.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.2-3
- Enable python dependency generator

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.11.2-1
- Initial package.

