%global pypi_name XStatic-jquery-ui

Name:           python-%{pypi_name}
Version:        1.12.0.1
Release:        11%{?dist}
Summary:        jquery-ui (XStatic packaging standard)

# According 
# https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses
# http://creativecommons.org/publicdomain/zero/1.0/legalcode
# is abbreviated CCO.
# This package has the same license as jquery-ui:
# https://github.com/jquery/jqueryui.com/blob/master/LICENSE.txt
License:        CC0
URL:            http://jqueryui.com/
Source0:        https://pypi.python.org/packages/64/d6/3ae9619abb32a05951686bd657256ba417b4e96373d99a739a7ed39363ef/XStatic-jquery-ui-1.12.0.1.tar.gz
BuildArch:      noarch

%description
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       xstatic-jquery-ui-common

%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-XStatic-jQuery

%description -n python3-%{pypi_name}
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 3 build of %{pypi_name}.

%package -n xstatic-jquery-ui-common
Summary:        %{summary}

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-jquery-ui-common
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package contains the javascript files.

%prep
%autosetup -n %{pypi_name}-%{version}
# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/jquery_ui'|" xstatic/pkg/jquery_ui/__init__.py

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}%{_jsdir}/jquery_ui
mv %{buildroot}%{python3_sitelib}/xstatic/pkg/jquery_ui/data/* %{buildroot}%{_jsdir}/jquery_ui
rmdir %{buildroot}%{python3_sitelib}/xstatic/pkg/jquery_ui/data/
# fix execute flags for js
chmod 644 %{buildroot}%{_jsdir}/jquery_ui/*.js

%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/xstatic/pkg/jquery_ui
%{python3_sitelib}/XStatic_jquery_ui-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/XStatic_jquery_ui-%{version}-py%{python3_version}-nspkg.pth

%files -n xstatic-jquery-ui-common
%doc README.txt
%{_jsdir}/jquery_ui

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.12.0.1-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.0.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.0.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.12.0.1-5
- Subpackage python2-XStatic-jquery-ui has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.12.0.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.10.4.1-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Thu Apr 6 2017 Radomir Dopieralski <rdopiera@redhat.com> - 1.12.0.1-2
- Fix directory names
* Thu Apr 6 2017 Radomir Dopieralski <rdopiera@redhat.com> - 1.12.0.1-1
- Upgrade to new version due to https://nodesecurity.io/advisories/127
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.10.4.1-6
- Rebuild for Python 3.6

* Wed Oct 12 2016 Jan Beran <jberan@redhat.com> - 1.10.4.1-5
- Provides a Python 3 subpackage

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.4.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Matthias Runge <mrunge@redhat.com> - 1.10.4.1-1
- Initial package (rhbz#1135430).
