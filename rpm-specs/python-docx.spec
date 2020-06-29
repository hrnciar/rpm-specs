%global pname docx

# behave is currently broken, so we disable behave tests
%bcond_with behave

Name:		python-docx
Version:	0.8.5
Release:	22%{?dist}
Summary:	Create and update Microsoft Word .docx files

License:	MIT
URL:		https://github.com/python-openxml/python-docx
Source0:	https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
 
%global _description\
Python library for creating and updating Microsoft Word (.docx) files.

%description %_description

%package -n python3-%{pname}
Summary:	Create and update Microsoft Word .docx files
Requires:       python3-lxml
%{?python_provide:%python_provide python3-%{pname}}
BuildRequires:	python3-devel
BuildRequires:	python3-lxml
#Testing requirements
BuildRequires:	python3-pyparsing	>= 2.0.1
BuildRequires:	python3-mock		>= 1.0.1
BuildRequires:	python3-flake8		>= 2.0
BuildRequires:	python3-pytest		>= 2.5
%if %{with behave}
BuildRequires:	python3-behave
%endif

%description -n python3-%{pname} %_description

%prep
%setup -qn %{name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest
%if %{with behave}
%{__python3} -m behave --stop
%endif

%files -n python3-%{pname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pname}
%{python3_sitelib}/python_%{pname}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.5-22
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.5-20
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.5-19
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.5-16
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.5-14
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.5-13
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.5-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)
- Move python3-lxml form py2 to py3 subpkg
- Add python_provide to py3 subpackage

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.5-10
- Python 2 binary package renamed to python2-docx
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.5-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 13 2015 Kushal Khandelwal <kushal124@gmail.com> - 0.8.5-2
- Fix dependency requirement.

* Mon Mar 9 2015 Kushal Khandelwal <kushal124@gmail.com> - 0.8.5-1
- update to 0.8.5

* Fri Feb 20 2015 Kushal Khandelwal <kushal124@gmail.com> - 0.8.2-1
- Initial package.
