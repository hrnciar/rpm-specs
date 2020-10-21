%global upstream_name nose-progressive


Name:           python-%{upstream_name}
Version:        1.5.1
Release:        22%{?dist}
Summary:        Nose plugin to show a progress bar and tracebacks during tests
License:        GPLv2+
URL:            https://github.com/erikrose/nose-progressive
Source0:        http://pypi.python.org/packages/source/n/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
# LICENSE fetched from https://raw.githubusercontent.com/erikrose/nose-progressive/c2011a2b82408fe18e14476b7db7202135398d63/LICENSE
# Pull request to include it in tarballs: https://github.com/erikrose/nose-progressive/pull/68
Source1:        LICENSE
# https://github.com/erikrose/nose-progressive/pull/69
Patch0:         %{name}-fix-tracebacks-on-python3.4.patch
BuildArch:      noarch

%description
nose-progressive is a nose plugin which displays progress in a stationary 
progress bar, freeing the rest of the screen (as well as the scrollback buffer) 
for the compact display of test failures, which it formats beautifully and 
usefully. It displays failures and errors as soon as they occur and avoids 
scrolling them off the screen in favor of less useful output. It also offers 
a number of other human-centric features to speed the debugging process.

%package -n python3-%{upstream_name}
Summary:        Nose plugin to show a progress bar and tracebacks during tests
%{?python_provide:%python_provide python3-%{upstream_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose >= 1.2.1
BuildRequires:  python3-blessings
Requires:       python3-nose >= 1.2.1
Requires:       python3-blessings

%description -n python3-%{upstream_name}
nose-progressive is a nose plugin which displays progress in a stationary 
progress bar, freeing the rest of the screen (as well as the scrollback buffer) 
for the compact display of test failures, which it formats beautifully and 
usefully. It displays failures and errors as soon as they occur and avoids 
scrolling them off the screen in favor of less useful output. It also offers 
a number of other human-centric features to speed the debugging process.

%prep
%setup -q -n %{upstream_name}-%{version}
cp -p %{SOURCE1} .
rm -r nose_progressive.egg-info

%patch0 -p1

# %%py3_build, because that breaks use_2to3.

%build

%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root %{buildroot}

%check
nosetests-%{python3_version} build/lib

%files -n python3-%{upstream_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/noseprogressive
%{python3_sitelib}/nose_progressive*.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-21
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-19
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-18
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-16
- Subpackage python2-nose-progressive has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-13
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Dan Callaghan <dcallagh@redhat.com> - 1.5.1-10
- renamed python-nose-progressive to python2-nose-progressive

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Apr 30 2014 Dan Callaghan <dcallagh@redhat.com> - 1.5.1-1
- new upstream bug fix release 1.5.1 (license changed to MIT)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Dan Callaghan <dcallagh@redhat.com> - 1.5-2
- fix tests

* Mon Apr 29 2013 Dan Callaghan <dcallagh@redhat.com> - 1.5-1
- new upstream bug fix release 1.5

* Wed Mar 27 2013 Dan Callaghan <dcallagh@redhat.com> - 1.4.1-1
- new upstream bug fix release 1.4.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Dan Callaghan <dcallagh@redhat.com> - 1.4-1
- new upstream release 1.4

* Tue Dec 04 2012 Dan Callaghan <dcallagh@redhat.com> - 1.3-3
- fix RPM macro in comment

* Mon Dec 03 2012 Dan Callaghan <dcallagh@redhat.com> - 1.3-2
- remove bundled egg-info from upstream tarball

* Fri Nov 30 2012 Dan Callaghan <dcallagh@redhat.com> - 1.3-1
- initial version
