%global commit          a59fd76dd730432c76b12ee6347ea66567107ab9
%global snapshotdate    20170219
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:       webkit2-sharp
Version:    0
Release:    0.11%{?snapshotdate:.%{snapshotdate}git%{shortcommit}}%{?dist}
Summary:    C# bindings for WebKit 2 with GTK+ 3

License:    MIT
URL:        https://github.com/hbons/%{name}
%{?shortcommit:
Source0:    %url/archive/%{commit}/%{name}-%{shortcommit}.tar.gz}
%{!?shortcommit:
Source0:    %url/archive/%{commit}/%{name}-%{version}.tar.gz}

Patch0:     %{name}-a59fd76-fix_libdir.patch

Requires:       webkit2gtk3
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(gtk-sharp-3.0)
BuildRequires:  pkgconfig(gapi-3.0)
BuildRequires:  pkgconfig(monodoc)
BuildRequires:  libxslt
BuildRequires:  dos2unix
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  gettext

ExclusiveArch:  %mono_arches

#https://fedoraproject.org/wiki/Packaging:Mono#Empty_debuginfo
%global debug_package %{nil}

%description
C# bindings for WebKit 2 with GTK+ 3


%package devel
Summary:    Development files for WebKit2-sharp
Requires:   %{name} = %{version}-%{release}
Requires:   pkgconfig

%description devel
Development files for WebKit2-sharp


%prep
%{?shortcommit:
%autosetup -n %{name}-%{commit}}
%{!?shortcommit:
%autosetup -n %{name}-%{version}}


%build
./autogen.sh
%configure --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
sed -i 's/\r$//' COPYING
# No parallel make, race condition with monodoc
make


%install
%make_install

find %{buildroot} -name '*.la' -delete


%files
%license COPYING
%doc README.md
%{_prefix}/lib/mono/
%{_datadir}/gapi-3.0/webkit2-sharp-api.xml
%{_libdir}/libwebkit2sharpglue-2.10.9.so


%files devel
%{_libdir}/pkgconfig/webkit2-sharp-4.0.pc
%{_prefix}/lib/monodoc/sources/webkit2-sharp*


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20170219gita59fd76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20170219gita59fd76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20170219gita59fd76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20170219gita59fd76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.7.20170219gita59fd76
- Remove ldconfig

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20170219gita59fd76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20170219gita59fd76
- Disable parallel make

* Fri Jan 12 2018 Tomas Popela <tpopela@redhat.com> - 0-0.4.20170219gita59fd76
- Adapt to the webkitgtk4 rename

* Mon Sep 25 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20170219gita59fd76
- Disable static libraries

* Sun Sep 24 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 0-0.2.20170219gita59fd76
- Improve spec file

* Sun Sep 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170219gita59fd76
- Initial package
