%global srcname sphinx_ansible_theme

Name:           python-%{srcname}
Version:        0.3.1
Release:        2%{?dist}
Summary:        A reusable Ansible Sphinx Theme

License:        MIT and BSD
URL:            https://github.com/ansible-community/%{srcname}
Source:         %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinx-notfound-page
BuildRequires:  python3-setuptools_scm_git_archive

# docs requirements
BuildRequires:  python3-sphinx

%global _description %{expand:
A reusable Ansible Sphinx Theme. This theme is building on top
of RTD Theme and adds customization's needed for building projects
which are part of Ansible ecosystem}

%description %{_description}

%package -n python-%{srcname}-doc
Summary: %summary
%description -n python-%{srcname}-doc
Documentation for sphinx_ansible_theme

%package -n python3-%{srcname}
Summary:    %summary
Requires:   python3-sphinx
Requires:   fontawesome-fonts
Requires:   fontawesome-fonts-web
Recommends: python-%{srcname}-doc
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{_description}

%prep
%setup -q -n %{srcname}-%{version}

%build
%py3_build
# generate html docs
PYTHONPATH=. sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -vr html/.{doctrees,buildinfo}


%install
%py3_install
pushd %{buildroot}%{python3_sitelib}/%{srcname}/static/fonts
rm -f FontAwesome.otf
rm -f fontawesome-webfont.*
ln -s %{_datadir}/fonts/fontawesome/FontAwesome.otf .
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.eot .
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.svg .
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.ttf .
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.woff .
ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.woff2 .
popd

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}*

%files -n python-%{srcname}-doc
%doc html
%license LICENSE

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.3.1-1
- initial commit
