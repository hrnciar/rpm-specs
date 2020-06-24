%global srcname click-threading
%global pyname click_threading
%global sum Multithreaded support for python click apps

Name:           python-%{srcname}
Version:        0.4.4
Release:        12%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/click-contrib/%{srcname}
Source0:        https://pypi.python.org/packages/82/5f/6f61961ab1310c12fd90d5dd036b86134e9ad35b48e50207a23b6fbaa2fb/click-threading-0.4.4.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-click >= 0.5

%description
Multithreaded support for python click (CLI creation kit) applications.

%package -n     python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-click >= 0.5

%description -n python3-%{srcname}
Multithreaded support for python 3 click (CLI creation kit) applications.


%prep
%setup -q -n %{srcname}-%{version}



%build

%py3_build


%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pyname}
%{python3_sitelib}/%{pyname}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.4-6
- Subpackage python2-click-threading has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.4-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Oct 01 2017 Michele Baldessari <michele@acksyn.org> - 0.4.4-1
- New upstream

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Michele Baldessari <michele@acksyn.org> - 0.4.2-1
- New upstream

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jun 19 2016 Michele Baldessari <michele@acksyn.org> - 0.4.0-1
- New upstream

* Wed Feb 03 2016 Michele Baldessari <michele@acksyn.org> - 0.1.2-2
- Some spec fixes

* Sat Nov 28 2015 Michele Baldessari <michele@acksyn.org> - 0.1.2-1
- Initial packaging
