%global pypi_name sphinxcontrib-autoprogram

Name:           python-%{pypi_name}
Version:        0.1.5
Release:        12%{?dist}
Summary:        Sphinx extension for documenting CLI programs

License:        BSD
URL:            https://bitbucket.org/birkenfeld/sphinx-contrib
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://bitbucket.org/birkenfeld/sphinx-contrib/raw/1621e337bb236e17d9e3fe4e98976365c06cc5fb/LICENSE
Patch0:         python-sphinxcontrib-autoprogram-test.patch
BuildArch:      noarch

BuildRequires:  python3-sphinx

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-six
BuildRequires:  python3-sphinx

%description
This extension provides an automated way to document CLI programs.
It scans ArgumentParser objects and then expands it into a set of
program and option directives.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python3-sphinx >= 1.2
Requires:       python3-six
%description -n python3-%{pypi_name}
This extension provides an automated way to document CLI programs.
It scans ArgumentParser objects and then expands it into a set of
program and option directives.

%prep
%autosetup -p 1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
cp %SOURCE1 .

%build
%py3_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install


%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/sphinxcontrib
%{python3_sitelib}/sphinxcontrib_autoprogram-%{version}-py%{python3_version}-nspkg.pth
%{python3_sitelib}/sphinxcontrib_autoprogram-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.5-5
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-3
- Rebuilt for Python 3.7

* Thu May 17 2018 mh <mh+fedora@scrit.ch> - 0.1.5-1
- Update to latest upstream (#1578601)

* Sun Apr  1 2018 Tom Hughes <tom@compton.nu> - 0.1.4-1
- Update to 0.1.4 upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.3-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 mh <mh+fedora@scrit.ch> - 0.1.3-1
- Update to latest upstream

* Fri Sep 09 2016 mh <mh+fedora@scrit.ch> - 0.1.2-1
- Initial package.

