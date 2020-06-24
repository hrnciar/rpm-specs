%global pkg_name flask-gravatar
%global mod_name Flask-Gravatar

Name:       python-%{pkg_name}
Version:    0.5.0
Release:    10%{?dist}
Summary:    Small extension for Flask to make usage of Gravatar service easy
License:    BSD
URL:        http://github.com/zzzsochi/%{mod_name}/
Source0:    https://files.pythonhosted.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz
BuildArch:  noarch

BuildRequires:  python%{python3_pkgversion}-devel
Buildrequires:  python%{python3_pkgversion}-pytest-runner

%description
Small extension for Flask to make usage of Gravatar service easy.

%package -n python%{python3_pkgversion}-%{pkg_name}
Summary: Small extension for Flask to make usage of Gravatar service easy
Requires:   python%{python3_pkgversion}-flask
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkg_name}}

%description -n python%{python3_pkgversion}-%{pkg_name}
Small extension for Flask to make usage of Gravatar service easy.

%prep
%setup -q -n %{mod_name}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python%{python3_pkgversion}-%{pkg_name}
%doc README.rst CHANGES.rst RELEASE-NOTES.rst AUTHORS
%license LICENSE
%dir %{python3_sitelib}/flask_gravatar/
%dir %{python3_sitelib}/flask_gravatar/__pycache__/
%{python3_sitelib}/flask_gravatar/*.py
%{python3_sitelib}/flask_gravatar/__pycache__/*.py*
%{python3_sitelib}/Flask_Gravatar*.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-4
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.7

* Thu Mar 01 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.5.0-1
- new version 0.5.0

* Thu Mar 01 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.4.2-2
- improve spec file

* Tue Jan  3 2017 Jakub Dorňák <jakub.dornak@misli.cz> - 0.4.2-1
- Initial package
