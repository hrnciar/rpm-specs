%global pypi_name jinja2-cli
%global _docdir_fmt %{name}

%global sum CLI interface to Jinja2
%global desc A CLI interface to Jinja2 which supports data in ini, json, querystring, yaml, \
yml and toml formats.


Name:           python-%{pypi_name}
Version:        0.7.0
Release:        6%{?dist}
Summary:        %sum

License:        BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://github.com/mattrobenolt/jinja2-cli/archive/0.7.0/jinja2-cli-0.7.0.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-jinja2

%description
%desc


%package -n     python3-%{pypi_name}
Summary:        %sum
BuildArch:      noarch
Requires:       python3-jinja2
Requires:       python3-PyYAML
Requires:       python3-toml
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%desc


%prep
%setup -qn %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install

# Remove tests from install (not good folder)
rm -rf %{buildroot}%{python3_sitelib}/tests


%check
# Copy test template
py.test-%{python3_version}


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/jinja2
%{python3_sitelib}/jinja2_cli-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/jinja2cli/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Julien Enselme <jujens@jujens.eu> - 0.7.0-1
- Update to 0.7.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-7
- Subpackage python2-jinja2-cli has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 16 2017 Julien Enselme <jujens@jujens.eu> - 0.6.0-1
- Update to 0.6.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 0.5.0-2
- Rebuilt for python 3.5

* Fri Oct 2 2015 Julien Enselme <jujens@jujens.eu> - 0.5.0-1
- Initial package
