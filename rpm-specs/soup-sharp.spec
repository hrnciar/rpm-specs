%global commit          0f36d103e567da1d1a8b5c43e1457c3d0c30393b
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20190810

Name:       soup-sharp
Version:    2.42.2
Release:    3.%{snapshotdate}git%{shortcommit}%{?dist}
Summary:    .NET bindings for libsoup

License:    LGPLv3+
URL:        https://github.com/stsundermann/soup-sharp
Source0:    %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(gtk-sharp-3.0)
BuildRequires:  pkgconfig(gapi-3.0)
BuildRequires:  pkgconfig(monodoc)
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
Requires:       pkgconfig(gapi-3.0)

ExclusiveArch:  %{mono_arches}

%description
WebKit-sharp is .NET bindings for the WebKit rendering engine.

%package devel
Summary:    Development files for soup-sharp
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   pkgconfig

%description devel
Development files for soup-sharp.

%package doc
Summary:        Documentation files for soup-sharp
Requires:       %{name} = %{version}-%{release}
Requires:       monodoc
BuildArch:      noarch

%description doc
Documentation files for soup-sharp

%prep
%autosetup -n %{name}-%{commit}
sed -i "s|\r||g" AUTHORS

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static
# No parallel make, race condition with monodoc
make

%install
%make_install
# remove .la files
rm -f %{buildroot}%{_libdir}/libsoupsharpglue-%{version}.la

%files
%doc AUTHORS README.md
%license COPYING
%{_monodir}/
%{_datadir}/gapi-3.0/soup-sharp-api.xml
%{_libdir}/libsoupsharpglue-%{version}.so

%files devel
%{_libdir}/pkgconfig/soup-sharp-*.pc

%files doc
%{_prefix}/lib/monodoc/sources/soup-sharp*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.42.2-3.20190810git0f36d10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.42.2-2.20190810git0f36d10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 23:23:13 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com>- 2.24.2-1.20190810git0f36d10
- Initial package, based upon Kyle Harms <kyle.harms@gmail.com> work
