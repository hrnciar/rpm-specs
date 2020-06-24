%{?python_enable_dependency_generator}
%global srcname terminado
# python2-tornado package is too old on EPEL

Name:           python-%{srcname}
Version:        0.8.3
Release:        3%{?dist}
Summary:        Terminals served to term.js using Tornado websockets

License:        BSD
URL:            https://github.com/jupyter/terminado
Source0:        https://github.com/jupyter/terminado/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
This is a Tornado websocket backend for the term.js Javascript terminal
emulator library.



%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Terminals served to term.js using Tornado websockets
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-flit
BuildRequires:  python%{python3_pkgversion}-pygments
# For tests
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-ptyprocess
BuildRequires:  python%{python3_pkgversion}-tornado >= 4.0.0
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-ptyprocess
Requires:       python%{python3_pkgversion}-tornado >= 4.0.0
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
This is a Tornado websocket backend for the term.js Javascript terminal
emulator library.


%prep
%setup -q -n %{srcname}-%{version}


%build
# this package has no setup.py, it uses flit
export FLIT_NO_NETWORK=1
flit build --format wheel

%install
# We install the wheel created at %%build
%py3_install_wheel %{srcname}-%{version}-py2.py3-none-any.whl


%check
%{__python3} -m nose -v

 

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}.dist-info


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Orion Poplawski <orion@nwra.com> - 0.8.3-1
- Update to 0.8.3

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 31 2019 Orion Poplawski <orion@nwra.com> - 0.8.2-1
- Update to 0.8.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-8
- Enable python dependency generator

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-7
- Subpackage python2-terminado has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Oct 08 2018 Orion Poplawski <orion@cora.nwra.com> - 0.8.1-6
- BR pip for install

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Petr Viktorin <pviktori@redhat.com> - 0.8.1-4
- Test using nose, which the project's README suggests

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-1
- Updated to 0.8.1 (#1513790)
- The package now uses flit
- The tests are now invoked with pytest
- LICENSE.txt renamed to LICENSE
- Be more explicit in %%files

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Orion Poplawski <orion@cora.nwra.com> - 0.6-2
- Run tests verbosely
- Do not build for python2 on EPEL

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 0.6-1
- Update to 0.6
- Modernize spec

* Mon Jul 27 2015 Orion Poplawski <orion@cora.nwra.com> - 0.5-3
- Add python2-terminado provides

* Fri Jul 10 2015 Orion Poplawski <orion@cora.nwra.com> - 0.5-2
- Build python2/3 from same tree
- BR/R tornado 4.0.0
- Fix changelog version number

* Tue May  5 2015 Orion Poplawski <orion@cora.nwra.com> - 0.5-1
- Initial package
