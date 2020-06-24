# Needs access to pypi so doesn't run in koji
%global with_tests 0

Name:           pychromecast
Version:        6.0.0
Release:        1%{?dist}
Summary:        Python library to communicate with the Google Chromecast

License:        MIT
URL:            https://github.com/home-assistant-libs/pychromecast
Source0:        https://github.com/home-assistant-libs/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?with_tests}
BuildRequires:  python3-six
BuildRequires:  python3-netifaces
BuildRequires:  python3-zeroconf
BuildRequires:  python3-protobuf
%endif

%description
Library for Python 3 to communicate with the Google Chromecast. It
currently supports:

-  Auto discovering connected Chromecasts on the network
-  Start the default media receiver and play any online media
-  Control playback of current playing media
-  Implement Google Chromecast api v2
-  Communicate with apps via channels
-  Easily extendable to add support for unsupported namespaces
-  Multi-room setups with Audio cast devices

%package -n python3-chromecast
Summary:  Library for Python 3 to communicate with the Google Chromecast
%{?python_provide:%python_provide python3-chromecast}

%description -n python3-chromecast
Library for Python 3 to communicate with the Google Chromecast. It
currently supports:

-  Auto discovering connected Chromecasts on the network
-  Start the default media receiver and play any online media
-  Control playback of current playing media
-  Implement Google Chromecast api v2
-  Communicate with apps via channels
-  Easily extendable to add support for unsupported namespaces
-  Multi-room setups with Audio cast devices

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install

%check
%if %{with_tests}
%{__python3} setup.py test
%endif

%files -n python3-chromecast
%license LICENSE
%{python3_sitelib}/*

%changelog
* Thu Jun 04 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 6.0.0-1
- Update to 6.0.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.2.0-2
- Rebuilt for Python 3.9

* Wed May 13 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 5.2.0-1
- Update to 5.2.0

* Sun May 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 5.1.0-1
- Update to 5.1.0

* Tue Apr 14 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 4.2.3-1
- Update to 4.2.3

* Tue Mar 17 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 4.2.0-1
- Update to 4.2.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Peter Robinson <pbrobinson@fedoraproject.org> 4.1.1-1
- Update to 4.1.1

* Thu Oct 17 2019 Peter Robinson <pbrobinson@fedoraproject.org> 4.1.0-1
- Update to 4.1.0

* Wed Sep 11 2019 Peter Robinson <pbrobinson@fedoraproject.org> 4.0.1-1
- Update to 4.0.1
- Add dependency on casttube

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.5.2-1
- Update to 2.5.2

* Wed Feb 13 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.5.0-1
- Update to 2.5.0

* Thu Feb  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.4.0-1
- Update to 2.4.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.3.0-1
- Update to 2.3.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-2
- Rebuilt for Python 3.7

* Tue Apr 10 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.2.0-1
- Update to 2.2.0
- Drop python2 package (retired upstream, no Fedora users)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.3-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Dec 11 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.3-1
- Update to 1.0.3

* Mon Nov 20 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.1-1
- Update to 1.0.1

* Sat Jul 29 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.2-1
- Update to 0.8.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.1-1
- Update to 0.8.1

* Sat Feb 18 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.0-1
- Update to 0.8.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.7-3
- Fix python3 provides

* Fri Dec  2 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.7-2
- Package updates

* Mon Oct 31 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.7-1
- initial packaging
