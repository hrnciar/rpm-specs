%global commit fb04954d48425dfa9d7014e733736c1802ba9733
%global codate 20191003
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           webp-pixbuf-loader
Version:        0.0.1
Release:        9.%{codate}git%{shortcommit}%{?dist}
Summary:        WebP image loader for GTK+ applications

License:        LGPLv2+
URL:            https://github.com/aruiz/webp-pixbuf-loader
Source0:        https://github.com/aruiz/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        https://www.gnu.org/licenses/old-licenses/lgpl-2.1.txt

BuildRequires:  meson
BuildRequires:  gcc gcc-c++
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  libwebp-devel

Requires:       gdk-pixbuf2%{?_isa}

%description
webp-pixbuf-loader contains a plugin to load WebP images in GTK+ applications

%prep
%setup -q -n %{name}-%{commit}

%build
%meson -Dgdk_pixbuf_query_loaders_path=gdk-pixbuf-query-loaders-%{__isa_bits}
%meson_build

%install
%meson_install
cp -av %{SOURCE1} COPYING

%files
%license COPYING
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-webp.so

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-9.20191003gitfb04954
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct  3 2019 Yanko Kaneti <yaneti@declera.com> - 0.0.1-8.20191003gitfb04954
- Newer snapshot moving to meson

* Mon Sep 30 2019 Yanko Kaneti <yaneti@declera.com> - 0.0.1-7.20190930gitddbcacf
- Pick an upstream crasher fix with a recent snapshot

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-6.20180710git9b92950
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5.20180710git9b92950
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-4.20180710git9b92950
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Yanko Kaneti <yaneti@declera.com> - 0.0.1-3.20180710git9b92950
- Initial packaging
- Address review commments (#1599839)
- Add license text from gnu.org
- BR: gcc-c++ for some Cmake reason
