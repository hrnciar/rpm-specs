# Enable LTO
%global optflags        %{optflags} -flto
%global build_ldflags   %{build_ldflags} -flto

%global uuid    org.gnome.HexGL

Name:           gnome-hexgl
Version:        0.2.0
Release:        3%{?dist}
Summary:        Gthree port of HexGL

# The entire source code is GPLv3+ except sounds which is CC-BY
License:        MIT and CC-BY
URL:            https://github.com/alexlarsson/gnome-hexgl
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/alexlarsson/gthree/issues/66
ExcludeArch:    armv7hl i686

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.48.0
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gthree-1.0) >= 0.2.0
BuildRequires:  pkgconfig(gtk+-3.0)
Requires:       hicolor-icon-theme
Requires:       %{name}-data = %{version}-%{release}

%description
%{summary}.


%package        data
BuildArch:      noarch

Summary:        Data files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    data
Data files for %{name}.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{uuid}.desktop


%files
%license COPYING sounds/LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_metainfodir}/*.xml

%files data
%{_datadir}/%{name}


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.0-2
- Update to 0.2.0

* Fri Mar 29 2019 Artem Polishchuk <ego.cordatus@gmail.com>
- Initial package
