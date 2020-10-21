%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}}

Summary:        Automate BGP filter generation based on routing database information
Name:           bgpq4
Version:        0.0.6
Release:        2%{?dist}
License:        BSD
URL:            https://github.com/bgp/bgpq4
Source0:        https://github.com/bgp/bgpq4/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} > 6)
BuildRequires:  discount
%else
BuildRequires:  python-markdown
BuildRequires:  sed
%endif

%description
The bgpq4 utility can be used to generate BGP filter configurations
such as prefix lists, (extended) access lists, policy statement terms
and AS path lists based on routing database information and supports
output formats for BIRD, Cisco, Huawei, Juniper, MikroTik, Nokia and
OpenBGPD routers as well as generic JSON.

%prep
%setup -q
%if 0%{?rhel} == 6
sed -e '/^AC_PACKAGE_URL/d' -e 's/-std=gnu11/-std=gnu99/' -i configure.ac
%endif
autoreconf --install

%build
%configure --docdir=%{_pkgdocdir}
%make_build

%install
%make_install

%files
%license COPYRIGHT
%doc README.md CHANGES bgpq4.html
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 16 2020 Robert Scheck <robert@fedoraproject.org> 0.0.6-1
- Upgrade to 0.0.6 (#1847220)
- Initial spec file for Fedora and Red Hat Enterprise Linux
