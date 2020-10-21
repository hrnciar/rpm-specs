%global srcname gatspy 
%global sum General tools for Astronomical Time Series in Python

Name:           python-%{srcname}
Version:        0.3
Release:        17%{?dist}
Summary:        %{sum}

License:        BSD
URL:            http://www.astroml.org/gatspy/
Source0:        http://pypi.python.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-astroML
BuildRequires:  python3-devel
BuildRequires:  python3-supersmoother

%description
Gatspy contains efficient, well-documented implementations of several common
routines for Astronomical time series analysis, including the Lomb-Scargle
periodogram, the Supersmoother method, and others.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-astroML
Requires:       python3-supersmoother
Recommends:     python3-astroML-addons

%description -n python3-%{srcname}
Gatspy contains efficient, well-documented implementations of several common
routines for Astronomical time series analysis, including the Lomb-Scargle
periodogram, the Supersmoother method, and others.

%prep
%setup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
# Disabled for now as tests require online access
#nosetests-%{python3_version} %{srcname}

%files -n python3-%{srcname}
%license LICENSE
%doc CHANGES.md README.md
%{python3_sitelib}/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.3-11
- drop python2 subpackage (#1627385)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3-9
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 0.3-8
- rebuilt

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Apr 21 2016 Christian Dersch <lupinix@mailbox.org> - 0.3-1
- new version (0.3)
- removed patch for tests applied upstream

* Wed Jan 20 2016 Christian Dersch <lupinix@mailbox.org> - 0.2.1-3
- Tests: applied upstream fix and enabled again

* Mon Jan 18 2016 Christian Dersch <lupinix@mailbox.org> - 0.2.1-2
- Disabled tests, they try to fetch data for test online, not allowed within
  Fedora to download additional stuff at build time.

* Sun Jan 03 2016 Christian Dersch <lupinix@mailbox.org> - 0.2.1-1
- Initial spec

