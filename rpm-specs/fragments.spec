# Fragments requires latest *libtransmission* from master branch with
# all submodules

%global transmission_commit 3d9fd25269ccfc1dacf9c5cd23a3d232e0085150
%global transmission_shortcommit %(c=%{transmission_commit}; echo ${c:0:7})

%global libnatpmp_commit 4d3b9d87bbe7549830c212ce840600619abcf887
%global libnatpmp_shortcommit %(c=%{libnatpmp_commit}; echo ${c:0:7})

%global dht_commit 25e12bb39eea3d433602de6390796fec8a8f3620
%global dht_shortcommit %(c=%{dht_commit}; echo ${c:0:7})

%global libutp_commit fda9f4b3db97ccb243fcbed2ce280eb4135d705b
%global libutp_shortcommit %(c=%{libutp_commit}; echo ${c:0:7})

%global appname Fragments
%global filename de.haeckerfelix.%{appname}
%global transmission_url https://github.com/transmission

Name: fragments
Version: 1.4
Release: 18%{?dist}
Summary: Easy to use BitTorrent client which follows the GNOME HIG

# The entire source code is GPLv3+ except:
# BSD: libnatpmp
# MIT: transmission
License: GPLv3+
URL: https://gitlab.gnome.org/World/Fragments
Source0: %{url}/-/archive/%{version}/%{appname}-%{version}.tar.gz
Source1: %{transmission_url}/transmission/tarball/%{transmission_commit}#/transmission-%{transmission_shortcommit}.tar.gz
Source2: %{transmission_url}/libnatpmp/tarball/%{libnatpmp_commit}#/libnatpmp-%{libnatpmp_shortcommit}.tar.gz
Source3: %{transmission_url}/dht/tarball/%{dht_commit}#/dht-%{dht_shortcommit}.tar.gz
Source4: %{transmission_url}/libutp/tarball/%{libutp_commit}#/libutp-%{libutp_shortcommit}.tar.gz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: intltool
BuildRequires: libappstream-glib
BuildRequires: libb64-devel
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libevent) >= 2.0.0
BuildRequires: pkgconfig(libhandy-0.0)
BuildRequires: pkgconfig(miniupnpc)
BuildRequires: pkgconfig(openssl) >= 0.9.7
BuildRequires: pkgconfig(zlib)

Requires: hicolor-icon-theme

Provides: bundled(dht) = 0.26.git%{dht_shortcommit}
Provides: bundled(libnatpmp) = 0.git%{libnatpmp_shortcommit}
Provides: bundled(libtransmission) = 0.94.git%{transmission_shortcommit}
Provides: bundled(libutp) = 0.git%{libutp_shortcommit}

%description
Fragments is an easy to use BitTorrent client which follows the GNOME HIG and
includes well thought-out features.


%prep
%autosetup -n %{appname}-%{version}
%autosetup -n %{appname}-%{version} -D -T -a 1
%autosetup -n %{appname}-%{version} -D -T -a 2
%autosetup -n %{appname}-%{version} -D -T -a 3
%autosetup -n %{appname}-%{version} -D -T -a 4

mv transmission-transmission-%{transmission_shortcommit}/* \
    /builddir/build/BUILD/%{appname}-%{version}/submodules/transmission
mv transmission-libnatpmp-%{libnatpmp_shortcommit}/* \
    /builddir/build/BUILD/%{appname}-%{version}/submodules/transmission/third-party/libnatpmp
mv transmission-dht-%{dht_shortcommit}/* \
    /builddir/build/BUILD/%{appname}-%{version}/submodules/transmission/third-party/dht
mv transmission-libutp-%{libutp_shortcommit}/* \
    /builddir/build/BUILD/%{appname}-%{version}/submodules/transmission/third-party/libutp

# Just to be sure libtransmission not compiles with bundled openssl
rm -r /builddir/build/BUILD/%{appname}-%{version}/submodules/transmission/third-party/openssl


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*
%{_metainfodir}/*.xml


%changelog
* Tue Sep 29 19:10:31 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4-18
- Rebuild due libevent 2.1.12 with a soname bump 2

* Wed Sep 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4-17
- Rebuild due libevent 2.1.12 with a soname bump
- style: spec

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4-13
- Initial package
