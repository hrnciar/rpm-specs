%global modname flask-multistatic
%global sum A simple flask plugin to allow overriding static files


Name:               python-flask-multistatic
Version:            1.0
Release:            16%{?dist}
Summary:            %{sum}

License:            BSD
URL:                https://pagure.io/flask-multistatic/
Source0:            https://pypi.python.org/packages/source/f/flask-multistatic/flask-multistatic-%{version}.tar.gz
BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-flask
BuildRequires:      python3-setuptools


%description
Simple flask plugin allowing to override static files, making theming flask
applications really easy.


%package -n         python3-%{modname}
Summary:            %{sum}
Requires:           python3-flask

%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-flask-multistatic
Simple flask plugin allowing to override static files, making theming flask
applications really easy.


%prep
%autosetup -n %{modname}-%{version}

rm -rf %{modname}.egg-info


%build
%py3_build


%install
%py3_install


%files -n python3-%{modname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/flask_multistatic.py*
%{python3_sitelib}/__pycache__/flask_multistatic*
%{python3_sitelib}/flask_multistatic-%{version}-*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0-10
- Subpackage python2-flask-multistatic has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 11 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.0-1
- initial package for Fedora
