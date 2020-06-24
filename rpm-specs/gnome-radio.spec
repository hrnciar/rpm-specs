# Enable LTO
%global optflags        %{optflags} -flto=$(nproc)
%global build_ldflags   %{build_ldflags} -flto

%global commit      e982347664b4071ab75b86dfeb5de9cf125be64d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20190217

Name:           gnome-radio
Version:        0.1.0
Release:        2.%{date}git%{shortcommit}%{?dist}
Summary:        GNOME Radio

License:        GPLv3+
URL:            http://gnomeradio.org
Source0:        https://gitlab.gnome.org/ole/gnome-radio/-/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
# BuildRequires:  desktop-file-utils
BuildRequires:  gcc
# BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(champlain-gtk-0.12) >= 0.12.10
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-player-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-tag-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.30
# Requires:       hicolor-icon-theme

%description
GNOME Radio is a free network radio software for the GNOME desktop.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
autoreconf
automake --add-missing
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README AUTHORS
%{_bindir}/%{name}

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2.20190217gite982347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20190217gite982347
- Initial package
