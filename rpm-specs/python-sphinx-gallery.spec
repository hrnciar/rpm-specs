%global srcname sphinx-gallery

Name:           python-%{srcname}
Version:        0.7.0
Release:        2%{?dist}
Summary:        Sphinx extension to automatically generate an examples gallery

License:        BSD
URL:            http://sphinx-gallery.readthedocs.io/en/latest/
Source0:        https://github.com/sphinx-gallery/sphinx-gallery/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
A Sphinx extension that builds an HTML version of any Python script and puts
it into an examples gallery.


%if 0%{?fedora} < 30
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
# For tests
BuildRequires:  python2-coverage
BuildRequires:  python2-matplotlib
BuildRequires:  python2-pillow
BuildRequires:  python2-pytest-cov
BuildRequires:  python2-pytest-runner
BuildRequires:  python2-scipy
BuildRequires:  python2-sphinx
Requires:       python2-matplotlib
Requires:       python2-pillow
Requires:       python2-sphinx
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
A Sphinx extension that builds an HTML version of any Python script and puts
it into an examples gallery.
%endif


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# For tests
BuildRequires:  python%{python3_pkgversion}-coverage
BuildRequires:  python%{python3_pkgversion}-matplotlib
BuildRequires:  python%{python3_pkgversion}-pillow
BuildRequires:  python%{python3_pkgversion}-pytest-cov
BuildRequires:  python%{python3_pkgversion}-pytest-runner
BuildRequires:  python%{python3_pkgversion}-scipy
BuildRequires:  python%{python3_pkgversion}-sphinx
Requires:       python%{python3_pkgversion}-matplotlib
Requires:       python%{python3_pkgversion}-pillow
Requires:       python%{python3_pkgversion}-sphinx
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
A Sphinx extension that builds an HTML version of any Python script and puts
it into an examples gallery.


%prep
%setup -qn %{srcname}-%{version}
# Remove bundled eggs
rm -rf %{srcname}.egg-info
# Test uses network
sed -i -e '/^addopt/s/$/ -k "not test_embed_code_links_get_data and not test_embed_links"/' setup.cfg


%build
%if 0%{?fedora} < 30
%py2_build
%endif
%py3_build


%install
%if 0%{?fedora} < 30
%py2_install
%endif
%py3_install
# No need for copy_sphinxgallery.sh
rm -r %{buildroot}%{_bindir}


%check
#export LANG=en_US.UTF-8
%if 0%{?fedora} < 30
%__python2 setup.py test
rm .coverage
%endif
%__python3 setup.py test


%if 0%{?fedora} < 30
%files -n python2-%{srcname}
%license LICENSE
%doc CHANGES.rst README.rst
%{python2_sitelib}/sphinx_gallery-%{version}-py%{python2_version}.egg-info/
%{python2_sitelib}/sphinx_gallery/
%endif

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinx_gallery-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/sphinx_gallery/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-2
- Rebuilt for Python 3.9

* Fri May 22 2020 Orion Poplawski <orion@nwra.com> - 0.7.0-1
- Update to 0.7.0

* Fri May 08 2020 Orion Poplawski <orion@nwra.com> - 0.6.2-1
- Update to 0.6.2

* Thu Apr 09 2020 Orion Poplawski <orion@nwra.com> - 0.6.1-1
- Update to 0.6.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Orion Poplawski <orion@nwra.com> - 0.5.0-1
- Update to 0.5.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 9 2019 Orion Poplawski <orion@nwra.com> - 0.3.1-1
- Update to 0.3.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 7 2018 Orion Poplawski <orion@nwra.com> - 0.2.0-1
- Update to 0.2.0
- Drop Python 2 package for Fedora 30+ (bugz #1628982)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.13-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 27 2017 Orion Poplawski <orion@nwra.com> - 0.1.13-1
- Update to 0.1.13

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-4
- Rebuild for Python 3.6

* Mon Nov 21 2016 Orion Poplawski <orion@cora.nwra.com> - 0.1.5-3
- Add upstream patch to fix UnicodeDecodeError

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 0.1.5-2
- Use github source, ship LICENSE
- Update URL
- Add needed requires

* Tue Nov 15 2016 Orion Poplawski <orion@cora.nwra.com> - 0.1.5-1
- Initial Fedora package