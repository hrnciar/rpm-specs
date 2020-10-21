%global upstream_name ofxparse


Name:           python-%{upstream_name}
Version:        0.18
Release:        11%{?dist}
Summary:        Python library for working with the OFX (Open Financial Exchange) file format
License:        MIT
URL:            http://sites.google.com/site/ofxparse
Source0:        https://files.pythonhosted.org/packages/source/o/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
# Python 3.9 compatibility, merged but not released yet:
# https://github.com/jseutter/ofxparse/pull/156
Patch1:         85e00b9911c20f9eafb9dbfbf1a18c2c83233ad7.patch
BuildArch:      noarch

%description
ofxparse is a parser for Open Financial Exchange (.ofx) format files. OFX files 
are available from almost any online banking site, so they work well if you 
want to pull together your finances from multiple sources. Online trading 
accounts also provide account statements in OFX files.

%package -n python3-%{upstream_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{upstream_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-six
BuildRequires:  python3-lxml
Requires:       python3-beautifulsoup4
Requires:       python3-six
Requires:       python3-lxml

%description -n python3-%{upstream_name}
ofxparse is a parser for Open Financial Exchange (.ofx) format files. OFX files 
are available from almost any online banking site, so they work well if you 
want to pull together your finances from multiple sources. Online trading 
accounts also provide account statements in OFX files.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{upstream_name}
%license LICENSE
%doc README.rst AUTHORS
%{python3_sitelib}/%{upstream_name}
%{python3_sitelib}/%{upstream_name}*.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.18-10
- Rebuilt for Python 3.9

* Wed Feb 19 2020 Dan Callaghan <djc@djc.id.au> - 0.18-9
- Fix for Python 3.9 compatibility (RHBZ#1792966)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.18-3
- Subpackage python2-ofxparse has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Aug 01 2018 Dan Callaghan <dcallagh@redhat.com> - 0.18-2
- conditionalize Python requirements so they still work in EPEL7

* Wed Aug 01 2018 Dan Callaghan <dcallagh@redhat.com> - 0.18-1
- upstream release 0.18

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.17-4
- Rebuilt for Python 3.7

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.17-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 0.17-1
- Update to 0.17 bug fix release (#1513450)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Dan Callaghan <dcallagh@redhat.com> - 0.16-1
- upstream release 0.16

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.15-5
- Rebuild for Python 3.6

* Sat Oct 08 2016 Björn Esser <fedora@besser82.io> - 0.15-4
- add needed BuildRequires and Requires
- fix BuildRequires for epel7

* Sat Oct 08 2016 Björn Esser <fedora@besser82.io> - 0.15-3
- add conditional for Python3 to build on epel7
- do not remove upstream egg-info

* Mon Aug 01 2016 Dan Callaghan <dcallagh@redhat.com> - 0.15-2
- updated to latest Python guidelines

* Mon Aug 01 2016 Dan Callaghan <dcallagh@redhat.com> - 0.15-1
- upstream release 0.15

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 07 2014 Dan Callaghan <dcallagh@redhat.com> - 0.14-2
- six is needed on Python 2 also

* Fri Dec 27 2013 Dan Callaghan <dcallagh@redhat.com> - 0.14-1
- upstream release 0.14

* Wed Aug 14 2013 Dan Callaghan <dcallagh@redhat.com> - 0.12-1
- initial version
