%global pkg_name flask-paranoid
%global mod_name Flask-Paranoid

Name:       python-%{pkg_name}
Version:    0.2.0
Release:    11%{?dist}
Summary:    Flask Simple user session protection
License:    BSD
URL:        http://github.com/miguelgrinberg/%{pkg_name}
Source0:    https://files.pythonhosted.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz
BuildArch:  noarch

BuildRequires:  python%{python3_pkgversion}-devel

%description
Flask Simple user session protection.

%package -n python%{python3_pkgversion}-%{pkg_name}
Summary:    Flask Simple user session protection
BuildRequires: python%{python3_pkgversion}-flask
Requires:   python%{python3_pkgversion}-flask
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkg_name}}

%description -n python%{python3_pkgversion}-%{pkg_name}
Flask Simple user session protection

%prep
%setup -q -n %{mod_name}-%{version}


%build
%py3_build

%install
%py3_install


%files -n python%{python3_pkgversion}-%{pkg_name}
%{python3_sitelib}/flask_paranoid
%{python3_sitelib}/Flask_Paranoid-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.0-5
- Subpackage python2-flask-paranoid has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-3
- Rebuilt for Python 3.7

* Fri Apr 13 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.2.0-2
- Be more specific in files section

* Thu Mar 01 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.2.0-1
- initial spec file

