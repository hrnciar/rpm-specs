%global srcname ifcfg

Name:           python-%{srcname}
Version:        0.21
Release:        2%{?dist}
Summary:        Python cross-platform network interface discovery (ifconfig/ipconfig/ip)

License:        BSD
URL:            https://github.com/ftao/%{name}
Source0:        https://github.com/ftao/%{name}/archive/releases/%{version}/%{name}-releases-%{version}.tar.gz

BuildArch:      noarch

%description
Ifcfg is a cross-platform library for parsing ifconfig and ipconfig output in
Python. It is useful for pulling information such as IP, Netmask, MAC Address,
Hostname, etc.

A fallback to ip is included for newer Unix systems w/o ifconfig.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  iproute
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if !0%{?rhel} || 0%{?rhel} >= 8
Recommends:     (iproute or net-tools)
%endif

%description -n python%{python3_pkgversion}-%{srcname}
Ifcfg is a cross-platform library for parsing ifconfig and ipconfig output in
Python. It is useful for pulling information such as IP, Netmask, MAC Address,
Hostname, etc.

A fallback to ip is included for newer Unix systems w/o ifconfig.


%prep
%autosetup -p1 -n %{name}-releases-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} -m nose tests


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Scott K Logan <logans@cottsay.net> - 0.21-1
- Update to 0.21 (rhbz#1852561)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.18-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 27 2019 Scott K Logan <logans@cottsay.net> - 0.18-1
- Initial package
