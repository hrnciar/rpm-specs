# set upstream name variable
%global srcname slixmpp


Name:           python-slixmpp
Version:        1.4.2
Release:        6%{?dist}
Summary:        Slixmpp is an XMPP library for Python 3.5+

License:        MIT
URL:            https://github.com/poezio/%{srcname}
Source0:        https://github.com/poezio/%{srcname}/archive/slix-%{version}/%{name}-%{version}.tar.gz

# Fix Python 3.9 compatibility
# Resolved upstream: https://lab.louiz.org/poezio/slixmpp/-/merge_requests/38
Patch0: fix-py39-compat.patch

BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  gcc
BuildRequires:  libidn-devel
# for docs
BuildRequires:  python3-sphinx
# for tests
#BuildRequires:  gnupg
Requires:       python3-pyasn1-modules
Requires:       python3-aiodns


%description
Slixmpp is an MIT licensed XMPP library for Python 3.5+. It is a fork
of SleekXMPP. Goals is to only rewrite the core of the library (the low
level socket handling, the timers, the events dispatching) in order to
remove all threads.



%package -n python3-%{srcname}
Summary:        Slixmpp is an XMPP library for Python 3.5+
Requires:       python3-pyasn1-modules
Requires:       python3-aiodns
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Slixmpp is an MIT licensed XMPP library for Python 3.5+. It is a fork
of SleekXMPP. Goals is to only rewrite the core of the library (the low
level socket handling, the timers, the events dispatching) in order to
remove all threads.


%package -n python-%{srcname}-doc
Summary:        Documentation for Slixmpp
BuildArch:      noarch
Requires:       python3-%{srcname}

%description -n python-%{srcname}-doc
Slixmpp is an MIT licensed XMPP library for Python 3.4+. It is a fork
of SleekXMPP. Goals is to only rewrite the core of the library (the low
level socket handling, the timers, the events dispatching) in order to
remove all threads.

This package contains documentation in reST and HTML formats.



%prep
%autosetup -n %{srcname}-slix-%{version} -p1


%build
%py3_build

# Build sphinx documentation
pushd docs/
make html
popd # docs


%install
%py3_install

# Install html docs
mkdir -p %{buildroot}%{_pkgdocdir}/
cp -pr docs/_build/html %{buildroot}%{_pkgdocdir}/

# Move sources
mv -f %{buildroot}%{_pkgdocdir}/html/_sources/ %{buildroot}%{_pkgdocdir}/rst/

# Remove buildinfo sphinx documentation
rm -rf %{buildroot}%{_pkgdocdir}/html/.buildinfo

# Fix non-standard modes (775)
chmod 755 %{buildroot}%{python3_sitearch}/%{srcname}/stringprep.cpython-*.so


%check
# tests disabled



%files -n python3-%{srcname}
%license LICENSE
%doc CONTRIBUTING.rst README.rst
# For arch-specific packages: sitearch
%{python3_sitearch}/%{srcname}-%{version}-*.egg-info/
%{python3_sitearch}/%{srcname}/


%files -n python-%{srcname}-doc
%doc examples/
%{_pkgdocdir}/



%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.4.2-5
- Fix Python 3.9 compatibility (#1817778)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 25 2019 Matthieu Saulnier <fantom@fedoraproject.org> - 1.4.2-1
- Bump version to 1.4.2

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 18 2018 Florent Le Coz <louiz@louiz.org> - 1.4.0-1
- Update to 1.4.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-6
- Rebuilt for Python 3.7

* Sat Apr 28 2018 Matthieu Saulnier <fantom@fedoraproject.org> - 1.3.0-5
- Disable tests in %%check section

* Wed Apr 25 2018 Matthieu Saulnier <fantom@fedoraproject.org> - 1.3.0-4
- Add Requires python3-aiodns
- Remove Patch0 remove-aiodns-dependancy

* Wed Apr 18 2018 Matthieu Saulnier <fantom@fedoraproject.org> - 1.3.0-3
- Fix file ownership in doc subpackage
- Add Requires python3-pyasn1-modules in python3 subpackage

* Mon Apr  2 2018 Matthieu Saulnier <fantom@fedoraproject.org> - 1.3.0-2
- Rename main package to python-slixmpp
- Cleanup specfile
- Replace build and install commands with %%py3_build and %%py3_install
- Split in python3 subpackage
- Split in doc subpackage

* Sun Apr  1 2018 Matthieu Saulnier <fantom@fedoraproject.org> - 1.3.0-1
- Initial package
