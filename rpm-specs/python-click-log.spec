%global srcname click-log
%global pyname click_log
%global sum Logging integration for python-click

Name:           python-%{srcname}
Version:        0.3.2
Release:        10%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/click-contrib/%{srcname}
Source0:        https://files.pythonhosted.org/packages/22/44/3d73579b547f0790a2723728088c96189c8b52bd2ee3c3de8040efc3c1b8/click-log-0.3.2.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-click


%description
Logging support to python click (CLI creation kit)
applications.

%package -n     python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-click


%description -n python3-%{srcname}
Logging support to python 3 click (CLI creation kit)
applications.

%prep
%setup -q -n %{srcname}-%{version}




%build

%py3_build


%install
%py3_install

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pyname}
%{python3_sitelib}/%{pyname}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.2-4
- Subpackage python2-click-log has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-2
- Rebuilt for Python 3.7

* Mon Jun 11 2018 Michele Baldessari <michele@acksyn.org> - 0.3.2-1
- New upstream

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 01 2017 Michele Baldessari <michele@acksyn.org> - 0.2.1-1
- New upstream

* Fri Aug 25 2017 Michele Baldessari <michele@acksyn.org> - 0.2.0-1
- New upstream

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Michele Baldessari <michele@acksyn.org> - 0.1.8-1
- New upstream

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-2
- Rebuild for Python 3.6

* Thu Nov 10 2016 Michele Baldessari <michele@acksyn.org> - 0.1.4-1
- New upstream

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 10 2016 Michele Baldessari <michele@acksyn.org> - 0.1.3-3
- Add license tag

* Wed Feb 03 2016 Michele Baldessari <michele@acksyn.org> - 0.1.3-2
- Some spec fixes

* Sun Jan 31 2016 Michele Baldessari <michele@acksyn.org> - 0.1.3-1
- New upstream

* Sat Nov 28 2015 Michele Baldessari <michele@acksyn.org> - 0.1.1-1
- Initial packaging
