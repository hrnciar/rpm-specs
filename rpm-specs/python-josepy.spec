%global pypi_name josepy

%global py3_prefix python%{python3_pkgversion}

%bcond_without python3

%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with docs
%else
%bcond_without docs
%endif

%if 0%{?fedora} >= 30 || 0%{?rhel} >= 8
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        3%{?dist}
Summary:        JOSE protocol implementation in Python

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/josepy
Source0:        %{pypi_source}
Source1:        %{pypi_source}.asc
# Key mentioned in https://github.com/certbot/josepy/blob/master/tools/release.sh#L37
# Keyring generation steps as follows:
#   gpg2 --keyserver pool.sks-keyservers.net --recv-key A2CFB51FA275A7286234E7B24D17C995CD9775F2
#   gpg2 --export --export-options export-minimal A2CFB51FA275A7286234E7B24D17C995CD9775F2 > gpg-A2CFB51FA275A7286234E7B24D17C995CD9775F2.gpg
Source2:        gpg-A2CFB51FA275A7286234E7B24D17C995CD9775F2.gpg
BuildArch:      noarch

# Remove various unpackaged testing dependencies that are used only for linting
Patch0:         0000-ignore-missing-linters.patch

%if 0%{?rhel} && 0%{?rhel} <= 7
Patch1:         0001-allow-old-versions.patch
%endif

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-mock
BuildRequires:  python2-pytest
BuildRequires:  python2-setuptools
%endif

%if %{with python3}
BuildRequires:  %{py3_prefix}-devel
BuildRequires:  %{py3_prefix}-mock
BuildRequires:  %{py3_prefix}-pytest
BuildRequires:  %{py3_prefix}-setuptools

# Used to verify OpenPGP signature
BuildRequires:  gnupg2
%if 0%{?rhel} && 0%{?rhel} == 8
# "gpgverify" macro, not in COPR buildroot by default
BuildRequires:  epel-rpm-macros >= 8-5
%endif
%endif

%if %{with docs}
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
%endif

%description
JOSE protocol implementation in Python using cryptography.

%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2-cryptography
Requires:       python2-setuptools
Requires:       python2-six
BuildRequires:  python2-cryptography
BuildRequires:  python2-setuptools
BuildRequires:  python2-six
%if 0%{?rhel} && 0%{?rhel} <= 7
# EL7 has an unversioned name for this package
Requires:       pyOpenSSL
BuildRequires:  pyOpenSSL
%else
Requires:       python2-pyOpenSSL
BuildRequires:  python2-pyOpenSSL
%endif

%if %{with docs} && !(0%{?rhel} && 0%{?rhel} <= 7)
Recommends:     python-%{pypi_name}-doc
%endif

%description -n python2-%{pypi_name}
JOSE protocol implementation in Python using cryptography.

This is the Python 2 version of the package.
%endif

%if %{with python3}
%package -n     %{py3_prefix}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       %{py3_prefix}-cryptography
Requires:       %{py3_prefix}-pyOpenSSL
Requires:       %{py3_prefix}-setuptools
Requires:       %{py3_prefix}-six
BuildRequires:  %{py3_prefix}-cryptography
BuildRequires:  %{py3_prefix}-pyOpenSSL
BuildRequires:  %{py3_prefix}-setuptools
BuildRequires:  %{py3_prefix}-six

%if %{with docs} && !(0%{?rhel} && 0%{?rhel} <= 7)
Recommends:     python-%{pypi_name}-doc
%endif

%description -n %{py3_prefix}-%{pypi_name}
JOSE protocol implementation in Python using cryptography.

This is the Python 3 version of the package.
%endif

%if %{with docs}
%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}
Conflicts:      python2-%{pypi_name} < 1.1.0-9
Conflicts:      %{py3_prefix}-%{pypi_name} < 1.1.0-9
%description -n python-%{pypi_name}-doc
Documentation for python-%{pypi_name}
%endif

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%py3_build
%endif

# Build documentation
%if %{with docs}
# EL7 has problems building the documentation due to fontawesome-fonts-web only
# being available on x86_64
%{__python3} setup.py install --user
make -C docs man PATH=${HOME}/.local/bin:$PATH SPHINXBUILD=sphinx-build-3
%endif

%install
%if %{with python2}
%py2_install
%endif

%if %{with python3}
%py3_install
%endif

%if %{with docs}
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 docs/_build/man/*.1*
%endif

%check
%if %{with python2}
%{__python2} setup.py test
%endif

%if %{with python3}
%{__python3} setup.py test
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/josepy
%{python2_sitelib}/josepy-%{version}-py?.?.egg-info
%if ! %{with python3}
%{_bindir}/jws
%else
%exclude %{_mandir}/man1/jws.1*
%endif
%endif

%if %{with python3}
%files -n %{py3_prefix}-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/josepy
%{python3_sitelib}/josepy-%{version}-py%{python3_version}.egg-info
%{_bindir}/jws
%endif

%if %{with docs}
%files -n python-%{pypi_name}-doc
%license LICENSE.txt
%doc README.rst
%{_mandir}/man1/*
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.9

* Tue Mar 24 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.3.0-2
- build Python 3 subpackage also in EPEL7

* Wed Jan 29 2020 Felix Schwarz <fschwarz@fedoraproject.org> 1.3.0-1
- Update to 1.3.0 (#1795747)

* Wed Jan 29 2020 Felix Schwarz <fschwarz@fedoraproject.org> 1.2.0-6
- enable GPG source file verification

* Mon Oct 07 2019 Eli Young <elyscape@gmail.com> - 1.2.0-5
- Support EPEL8 builds

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Eli Young <elyscape@gmail.com> - 1.2.0-1
- Update to 1.2.0 (#1725899)

* Thu Jun 27 2019 Eli Young <elyscape@gmail.com> - 1.1.0-9
- Split docs to separate package (#1700273)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Eli Young <elyscape@gmail.com> - 1.1.0-7
- Remove Python 2 package in Fedora 30+ (#1658534)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Eli Young <elyscape@gmail.com> - 1.1.0-5
- Enable tests

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-4
- Rebuilt for Python 3.7

* Fri Jun 29 2018 Eli Young <elyscape@gmail.com> - 1.1.0-3
- Use available python2 metapackages for EPEL7
- Specify binary name for sphinx-build
- Fix permissions on man files

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.7

* Tue Apr 17 2018 Eli Young <elyscape@gmail.com> - 1.1.0-1
- Update to 1.1.0 (#1567455)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Eli Young <elyscape@gmail.com> - 1.0.1-1
- Initial package.
