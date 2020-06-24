%global commit c67b52658bb1b73db178ad81bfc76ae0402b2a2a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           koan
Version:        2.9.0
Release:        0.10.20200412git%{?shortcommit}%{?dist}
Summary:        Kickstart over a network

License:        GPLv2+
URL:            https://github.com/cobbler/koan
Source0:        https://github.com/cobbler/koan/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildArch:      noarch

BuildRequires:  /usr/bin/pathfix.py
Requires:       python%{python3_pkgversion}-koan = %{version}-%{release}

%description
Koan stands for kickstart-over-a-network and allows for both network
installation of new virtualized guests and reinstallation of an existing
system. For use with a boot-server configured with Cobbler.


%package -n python%{python3_pkgversion}-koan
Summary:        koan python%{python3_pkgversion} module
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_enable_dependency_generator}
%if 0%{?el7}
Requires:       python%{python3_pkgversion}-distro
Requires:       python%{python3_pkgversion}-ethtool
Requires:       python%{python3_pkgversion}-libvirt
Requires:       python%{python3_pkgversion}-netifaces
Requires:       python%{python3_pkgversion}-simplejson
%endif
Requires:       virt-install

%description -n python%{python3_pkgversion}-koan
koan python%{python3_pkgversion} module.


%prep
%autosetup -p1 -n %{name}-%{commit}
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" bin

%build
%py3_build

%install
%py3_install

%files
%license COPYING
%doc README
%{_bindir}/koan
%{_bindir}/cobbler-register

%files -n python%{python3_pkgversion}-koan
%license COPYING
%{python3_sitelib}/koan/
%{python3_sitelib}/koan*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.9.0-0.10.20200412gitc67b526
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Orion Poplawski <orion@nwra.com> - 2.9.0-0.9.202004012gitc67b526
- Update to latest git

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-0.8.20191125gitcff96a0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Orion Poplawski <orion@nwra.com> - 2.9.0-0.7.20191125gitcff96a0
- Add requirement on netifaces

* Mon Nov 25 2019 Orion Poplawski <orion@nwra.com> - 2.9.0-0.6.20191125gitcff96a0
- Update to latest git

* Fri Nov 15 2019 Orion Poplawski <orion@nwra.com> - 2.9.0-0.5.20191115git18df5d4
- Update to latest git
- Use automatic python dependencies
- Use proper snapshot release tag

* Thu Nov  7 2019 Orion Poplawski <orion@nwra.com> - 2.9.0-0.4.git
- Update to latest git

* Fri Oct 18 2019 Orion Poplawski <orion@nwra.com> - 2.9.0-0.3.git
- Add patch to support cobbler 2 servers
- Add patch to fix quoting with grubby on EL8

* Fri Oct 11 2019 Orion Poplawski <orion@nwra.com> - 2.9.0-0.2.git
- Split out again from cobbler
