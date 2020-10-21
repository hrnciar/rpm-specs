%global desc Sphinx themes for Flask and related projects

%global pkg_name flask-sphinx-themes
%global mod_name Flask-Sphinx-Themes


Name:           python-flask-sphinx-themes
Version:        1.0.2
Release:        11%{?dist}
Summary:        %{desc}
License:        BSD
URL:            https://github.com/pallets/flask-sphinx-themes
Source0:        https://files.pythonhosted.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%description
%{desc}

%package -n python%{python3_pkgversion}-%{pkg_name}
Requires: python%{python3_pkgversion}-sphinx
Summary: %{desc}
%{?python_provide:%python_provide python3-%{pkg_name}}

# Remove in Fedora 33
Provides: python3-sphinx-theme-flask = %{version}-%{release}
Obsoletes: python3-sphinx-theme-flask < 1.0.2-4
%{?python_provide:%python_provide python3-sphinx-theme-flask}

%description -n python%{python3_pkgversion}-%{pkg_name}
%{desc}

%prep
%setup -q -n %{mod_name}-%{version}

%build
%py3_build


%install
%py3_install

%files -n python%{python3_pkgversion}-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/flask_sphinx_themes/
%{python3_sitelib}/Flask_Sphinx_Themes*.egg-info/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-4
- Remove python2 subpackage
- Obsolete python3-sphinx-theme-flask

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-2
- Rebuilt for Python 3.7

* Fri Mar 09 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.0.2-1
- initial version