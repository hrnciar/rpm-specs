# Created by pyp2rpm-3.3.2

# Enable auto-generation of runtime dependencies
%{?python_enable_dependency_generator}

%global pypi_name notify2

Name:           python-%{pypi_name}
Version:        0.3.1
Release:        8%{?dist}
Summary:        Python interface to DBus notifications

License:        BSD
URL:            https://bitbucket.org/takluyver/pynotify2
Source0:        https://files.pythonhosted.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  %{_bindir}/sphinx-build-3

%description
This is a pure-python replacement for notify-python, using python-dbus
to communicate with the notifications server directly.

It's compatible with Python 2 and 3, and its callbacks can work with
Gtk or Qt applications.


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
# Requires aren't properly stated for dbus-python, so they aren't generated properly
Requires:       python%{python3_pkgversion}-dbus

%description -n python%{python3_pkgversion}-%{pypi_name}
This is a pure-python replacement for notify-python, using python-dbus
to communicate with the notifications server directly.

It's compatible with Python 2 and 3, and its callbacks can work with
Gtk or Qt applications.

%package -n python-%{pypi_name}-doc
Summary:        notify2 documentation
%description -n python-%{pypi_name}-doc
Documentation for notify2

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license docs/license.rst LICENSE
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license docs/license.rst LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 Scott K Logan <logans@cottsay.net> - 0.3.1-3
- Add support for building for EPEL7 (#1685288)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 16 2018 Neal Gompa <ngompa13@gmail.com> - 0.3.1-1
- Initial packaging for Fedora (#1659833)
