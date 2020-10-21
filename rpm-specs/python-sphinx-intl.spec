%global pypi_name sphinx-intl
%global srcname sphinx_intl
%global cmdname sphinx-intl
%global project_owner sphinx-doc
%global github_name sphinx-intl
%global desc sphinx-intl is a utility tool that provides several features that make it easy \
to translate and to apply translation to Sphinx generated document. Optional: \
support the Transifex service for translation with Sphinx (not packaged yet).


Name:           python-%{pypi_name}
Version:        2.0.1
Release:        2%{?dist}
Summary:        Sphinx utility that make it easy to translate and to apply translation

License:        BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://github.com/%{project_owner}/%{github_name}/archive/%{version}/%{github_name}-%{version}.tar.gz

BuildArch:      noarch

%description
%desc


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-click
BuildRequires:  python%{python3_pkgversion}-babel
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-mock
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-click
Requires:       python%{python3_pkgversion}-babel
Requires:       python%{python3_pkgversion}-sphinx
Conflicts:      python2-%{pypi_name} < 0.9.11-6
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
%desc


%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Correct line encoding in README.rst
sed -i 's/\r$//' README.rst


%build
%py3_build


%install
%py3_install
pushd %{buildroot}%{_bindir}
mv %{cmdname} %{cmdname}-%{python3_version}
ln -s %{cmdname}-%{python3_version} %{cmdname}-3
ln -s %{cmdname}-3 %{cmdname}
popd


%check
# Transifex is not packaged. Remove tests that depens on it.
rm tests/test_*transifex*.py
PYTHONPATH="$(pwd)" py.test-%{python3_version} -v .



%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-%{version}*-py%{python3_version}.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/%{cmdname}-3*
%{_bindir}/%{cmdname}


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Julien Enselme <jujens@jujens.eu> - 2.0.1-1
- Update to 2.0.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Julien Enselme <jujens@jujens.eu> - 2.0.0-1
- Update to 2.0.0

* Wed Mar 06 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.11-6
- Subpackage python2-sphinx-intl has been removed
  See https://fedoraproject.org/wiki/Changes/Sphinx2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.11-4
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.11-2
- Rebuilt for Python 3.7

* Mon Feb 19 2018 Julien Enselme <jujens@jujens.eu> - 0.9.11-1
- Update to 0.9.11

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-3.git20cd0d2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.10-2.git20cd0d2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Sep 14 2017 Julien Enselme <jujens@jujens.eu> - 0.9.10-1.git20cd0d2
- Update to 0.9.10

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-6.gitbf6edc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-5.gitbf6edc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.9-4.gitbf6edc2
- Rebuild for Python 3.6

* Sun Oct 09 2016 Julien Enselme <jujens@jujens.eu> - 0.9.9-3.gitbf6edc2
- Remove duplicated pattern in %%files

* Wed Oct 05 2016 Julien Enselme <jujens@jujens.eu> - 0.9.9-2.gitbf6edc2
- Add LC_ALL for tests to pass in build env

* Wed Sep 14 2016 Julien Enselme <jujens@jujens.eu> - 0.9.9-1.gitbf6edc2
- Initial packaging
