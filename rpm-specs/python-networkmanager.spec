Name:      python-networkmanager
Version:   2.1
Release:   9%{?dist}
Summary:   Easy communication with NetworkManager
Source0:   https://pypi.io/packages/source/p/python-networkmanager/python-networkmanager-%{version}.tar.gz
License:   MIT
BuildArch: noarch
URL:       https://github.com/seveas/python-networkmanager

%description
python-networkmanager wraps NetworkManagers D-Bus interface so you can be less
verbose when talking to NetworkManager from python. All interfaces have been
wrapped in classes, properties are exposed as python properties and function
calls are forwarded to the correct interface.


%package -n python3-networkmanager
Summary: %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
Requires: python3-dbus
%{?python_provide:%python_provide python%{python3_pkgversion}-networkmanager}
%description -n python3-networkmanager
python-networkmanager wraps NetworkManagers D-Bus interface so you can be less
verbose when talking to NetworkManager from python. All interfaces have been
wrapped in classes, properties are exposed as python properties and function
calls are forwarded to the correct interface.


%package -n python-networkmanager-doc
Summary: Example files for python-networkmanager
%description -n python-networkmanager-doc
This package provides examples for python-networkmanager


%prep
%autosetup


%build
%py3_build
cd docs
make man

%install
%py3_install

mkdir -p %{buildroot}%{_mandir}/man1/
cp -p docs/_build/man/python-networkmanager.1 %{buildroot}%{_mandir}/man1/

chmod a-x examples/*.py examples/n-m


%files -n python3-networkmanager
%license COPYING
%{python3_sitelib}/NetworkManager.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/python_networkmanager-*.egg-info

%files -n python-networkmanager-doc
%license COPYING
%doc examples
%doc %{_mandir}/man1/python-networkmanager.1.gz


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1-2
- Rebuilt for Python 3.7

* Sat Apr 28 2018 John Dulaney <jdulaney@fedoraproject.org> - 2.1-1
- Update to latest release

* Thu Mar 22 2018 John Dulaney <jdulaney@fedoraproject.org> - 2.0.1-5
- Drop python2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 John Dulaney <jdulaney@fedoraproject.org> - 2.0.1-1
- New release 2.0.1

* Sun Feb 12 2017 John Dulaney <jdulaney@fedoraproject.org> - 1.2.1-7
- Correct typo

* Sun Feb 12 2017 John Dulaney <jdulaney@fedoraproject.org> - 1.2.1-6
- modify chmod making example .py files non-executable

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 John Dulaney <jdulaney@fedoraproject.org> - 1.2.1-4
- Update requires.

* Wed Jan 25 2017 John Dulaney <jdulaney@fedoraproject.org> - 1.2.1-3
- move manpage to docs subpackage and set cp to preserve timestamp

* Tue Jan 17 2017 John Dulaney <jdulaney@fedoraproject.org> - 1.2.1-2
- Add Requires:  python-dbus
- Package examples in doc subpackage
- Clean up python3
- Add Provides:

* Wed Jan 11 2017 John Dulaney <jdulaney@fedoraproject.org> - 1.2.1-1
- Initial Packaging
