%global pypi_name flask-compress

Name:           python-%{pypi_name}
Version:        1.7.0
Release:        1%{?dist}
Summary:        Compress responses in your Flask app with gzip or brotli

License:        MIT
URL:            https://github.com/colour-science/flask-compress
Source0:        %{pypi_source Flask-Compress}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(brotli)
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(setuptools)

%description
Flask-Compress allows you to easily compress your Flask application's
responses with gzip.

The preferred solution is to have a server (like Nginx) automatically
compress the static files for you. If you don't have that option
Flask-Compress will solve the problem for you.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(brotli)
Requires:       python3dist(flask)
%description -n python3-%{pypi_name}
Flask-Compress allows you to easily compress your Flask application's
responses with gzip.

The preferred solution is to have a server (like Nginx) automatically
compress the static files for you. If you don't have that option
Flask-Compress will solve the problem for you.



%prep
%autosetup -n Flask-Compress-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/flask_compress.py
%{python3_sitelib}/Flask_Compress-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Oct 11 2020 Rafael Fontenelle <rafaelff@gnome.org> - 1.7.0-1
- Update to 1.7.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Rafael Fontenelle <rafaelff@gnome.org> - 1.5.0-2
- use macro for source0

* Tue May 12 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.5.0-1
- Initial package.
