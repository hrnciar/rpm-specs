%global api_ver 3.0

Name:           libxml++30
Version:        3.2.2
Release:        1%{?dist}
Summary:        C++ wrapper for the libxml2 XML parser library

License:        LGPLv2+
URL:            http://libxmlplusplus.sourceforge.net/
Source0:        https://download.gnome.org/sources/libxml++/3.2/libxml++-%{version}.tar.xz

BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen, graphviz
BuildRequires:  gcc-c++
BuildRequires:  glibmm24-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt
BuildRequires:  meson

%description
libxml++ is a C++ wrapper for the libxml2 XML parser library. Its original
author is Ari Johnson and it is currently maintained by Christophe de Vienne
and Murray Cumming.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation for %{name}, includes full API docs
BuildArch:      noarch
Requires:       glibmm24-doc

%description    doc
This package contains the full API documentation for %{name}.


%prep
%autosetup -n libxml++-%{version} -p1


%build
%meson -Dbuild-documentation=true
%meson_build


%install
%meson_install


%files
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/libxml++-%{api_ver}.so.1*

%files devel
%{_includedir}/libxml++-%{api_ver}/
%{_libdir}/libxml++-%{api_ver}.so
%{_libdir}/libxml++-%{api_ver}/
%{_libdir}/pkgconfig/libxml++-%{api_ver}.pc

%files doc
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books
%{_datadir}/devhelp/books/libxml++-%{api_ver}
%{_docdir}/libxml++-%{api_ver}


%changelog
* Mon Oct  5 2020 Kalev Lember <klember@redhat.com> - 3.2.2-1
- Update to 3.2.2
- Switch to meson build system

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 2020 Kalev Lember <klember@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 14 2017 Kalev Lember <klember@redhat.com> - 3.0.1-1
- Initial Fedora packaging
