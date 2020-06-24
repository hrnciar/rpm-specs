%global pypi_name autopep8
%global py3_name python3-%{pypi_name}

Name:           python-autopep8
Version:        1.4.3
Release:        7%{?dist}
Summary:        The package autopep8 formats Python code based on the output of the pep8 utility

License:        MIT
URL:            http://pypi.python.org/pypi/autopep8
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
autopep8 formats Python code based on the output of the pep8 utility.

%package -n %{py3_name}
Summary:        The package autopep8 formats Python code based on the output of the pep8 utility

%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-pycodestyle
Requires:       python3-pycodestyle

%description -n %{py3_name}
autopep8 formats Python code based on the output of the pep8 utility.


%prep
%autosetup -n autopep8-%{version}
sed -i -e '1d' autopep8.py
touch test/__init__.py #test needs to be a python module otherwise test will fial


%build

%py3_build


%check
# rpmbuild forces the use of LANG=C which fails unit tests

%{__python3} setup.py test


%install
%py3_install
mv %{buildroot}%{_bindir}/%{pypi_name} %{buildroot}%{_bindir}/%{py3_name}
pushd %{buildroot}%{_bindir}
ln -s %{py3_name} %{pypi_name}-3
ln -s %{py3_name} %{pypi_name}-%{python3_version}
popd


%files -n %{py3_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/__pycache__/*
%{_bindir}/%{py3_name}
%{_bindir}/%{pypi_name}-3
%{_bindir}/%{pypi_name}-%{python3_version}



%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Matthias Runge <mrunge@redhat.com> - 1.4.3-1
- update to 1.4.3, drop python2 subpackage

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.4-10
- Drop explicit locale setting for python3, use C.UTF-8 for python2
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.4-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.4-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.4-3
- Rebuild for Python 3.6

* Fri Nov 25 2016 Matthias Runge <mrunge@redhat.com> - 1.2.4-2
- fix __pycache__ ownership

* Tue Nov 01 2016 Matthias Runge <mrunge@redhat.com> - 1.2.4-1
- update to 1.2.4
- update python3 executable name in new style (rhbz#1341315)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Robert Kuska <rkuska@redhat.com> - 1.2.1-1
- Update to 1.2.1

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Aug 28 2015 Nikola Dipanov <ndipanov@redhat.com> - 1.2-1
- Update to upstream version 1.2

* Sat Jul 11 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 1.1.1-1
- Upstream 1.1.1
- Use python versioned macros
- Add missing dist in release tag
- Add python3 subpackage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 13 2013 Nikola Dipanov <ndipanov@redhat.com> - 0.9.2-1
- Update to upstream version 0.9.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 06 2012 Nikola Dipanov <ndipanov@redhat.com> - 0.8-1
- initial build
