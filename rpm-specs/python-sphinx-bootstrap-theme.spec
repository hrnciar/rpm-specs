%global srcname sphinx-bootstrap-theme

%global common_sum A sphinx theme that integrates the Bootstrap framework
%global common_desc \
This sphinx theme integrates the Booststrap CSS / Javascript framework \
with various layout options, hierarchical menu navigation, and mobile-friendly \
responsive design.  It is configurable, extensible and can use any number \
of different Bootswatch CSS themes.

%global jquery_version 1.12.4
%global bootstrap_version 3.4.1

Name:           python-%{srcname}
Version:        0.8.0
Release:        6%{?dist}
Summary:        %{common_sum}

License:        MIT and ASL 2.0
URL:            http://ryan-roemer.github.com/%{srcname}
Source0:        https://github.com/ryan-roemer/sphinx-bootstrap-theme/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif
BuildRequires:  web-assets-devel


%description
%{common_desc}


%package -n python3-%{srcname}
Summary:        %{common_sum}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if 0%{?rhel}
Provides:       bundled(glyphicons-halflings-fonts)
%else
Requires:       glyphicons-halflings-fonts
%endif
Requires:       web-assets-filesystem
Provides:       bundled(jquery) = %{jquery_version}
Requires:       python3-sphinx

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_desc}


%prep
%autosetup -n %{srcname}-%{version}
rm -rf *.egg-info


%build
%py3_build


%install
%py3_install

# Remove the bundled fonts on RHEL
%if 0%{?rhel}
for d in %{python3_sitelib}; do
  %{__rm} %{buildroot}${d}/sphinx_bootstrap_theme/bootstrap/static/bootstrap-%{bootstrap_version}/fonts/glyphicons-halflings-regular.ttf
  %{__ln_s} -f %{_datadir}/fonts/glyphicons-halflings/glyphicons-halflings-regular.ttf \
    %{buildroot}${d}/sphinx_bootstrap_theme/bootstrap/static/bootstrap-%{bootstrap_version}/fonts/glyphicons-halflings-regular.ttf
done
%endif


%files -n python3-%{srcname}
%license LICENSE.txt
%doc *.rst
%{python3_sitelib}/sphinx_bootstrap_theme
%{python3_sitelib}/sphinx_bootstrap_theme-%{version}-py%{python3_version}.egg-info


%changelog
* Thu Aug 20 2020 Stuart Campbell <stuart@stuartcampbell.me> - 0.8.0-6
- Always bundle JQuery (#1866729)
- Only bundle fonts on RHEL

* Fri Aug 14 2020 Stuart Campbell <stuart@stuartcampbell.me> - 0.8.0-5
- Do not use system webassets for F33+

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct  7 2019 Orion Poplawski <orion@nwra.com> - 0.8.0-1
- Update to 0.8.0
- Do not use system webassets on RHEL8
- Cleanup spec

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.13-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.13-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.13-10
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.13-8
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.13-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Stuart Campbell <sic@fedoraproject.org> - 0.4.13-3
- fix problem in using non existent package in el7

* Mon Jan 16 2017 Björn Esser <besser82@fedoraproject.org> - 0.4.13-2
- Update to latest upstream-release

* Mon Jan 16 2017 Björn Esser <besser82@fedoraproject.org> - 0.4.5-4
- Spec-file optmization

* Thu Nov 17 2016 Stuart Campbell <sic@fedoraproject.org> - 0.4.5-3
- Added check and disable python 3 for el.

* Sat Jun 18 2016 Stuart Campbell <sic@fedoraproject.org> - 0.4.5-2
- Removed bundled JQuery and added links to central version

* Thu Nov 05 2015 Stuart Campbell <sic@fedoraproject.org> - 0.4.5-1
- Initial package for fedora only
