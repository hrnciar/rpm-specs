# Created by pyp2rpm-3.3.4
%global pypi_name widgetsnbextension

Name:           python-%{pypi_name}
Version:        3.5.1
Release:        2%{?dist}
Summary:        Interactive HTML widgets for Jupyter notebooks

License:        BSD
URL:            http://ipython.org
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python-jupyter-filesystem

%description
Interactive HTML widgets for Jupyter notebooks.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(notebook) >= 4.4.1
Requires:       python-jupyter-filesystem

# sagemath included the files of this package
# https://bugzilla.redhat.com/show_bug.cgi?id=1856311
Conflicts:      sagemath-jupyter < 9.1-2

%description -n python3-%{pypi_name}
Interactive HTML widgets for Jupyter notebooks.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

# Move config file from /usr/etc to /etc
mkdir -p %{buildroot}%{_sysconfdir}/jupyter/nbconfig/notebook.d/
mv {%{buildroot}%{_prefix}/etc,%{buildroot}%{_sysconfdir}}/jupyter/nbconfig/notebook.d/widgetsnbextension.json

%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{_datadir}/jupyter/nbextensions/jupyter-js-widgets/
%config(noreplace) %{_sysconfdir}/jupyter/nbconfig/notebook.d/widgetsnbextension.json

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Lumír Balhar <lbalhar@redhat.com> - 3.5.1-1
- Initial package.
