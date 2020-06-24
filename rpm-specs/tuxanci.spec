Name:           tuxanci
Version:        0.21.0
Release:        12%{?dist}
Summary:        First Tux shooter multi-player network game
# LICENCE:      GPLv2 text
## unused
# data/font/DejaVuSans.ttf: Bitstream Vera and Public Domain
License:        GPL+
URL:            http://www.tuxanci.org/en/start
Source0:        http://download.tuxanci.org/tuxanci-0.21.0.tar.bz2
Source1:        tuxanci.desktop
Source2:        tuxanci.appdata.xml
Patch1:         0001-SDLmain-is-no-more.patch
Patch2:         0002-dlopen-is-used-outside-server-too.patch
Patch3:         0003-Unbreak-DLIB_INSTALL_DIR.patch
Patch4:         0004-Make-the-icon-square.patch
# Do not install LICENCE file twice, we already put into license directory
Patch5:         tuxanci-0.21.0-Do-not-install-LICENSE.patch
# Do not install bundled fonts
Patch6:         tuxanci-0.21.0-Unbundle-fonts.patch
BuildRequires:  cmake >= 2.6.0
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  ImageMagick
# libappstream-glib for appstream-util
BuildRequires:  libappstream-glib
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  zziplib-devel
Requires:       font(dejavusans)

%description
Tuxanci is a first Tux shooter game supporting single player and multi-player
modes both on a single computer and over the network.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DCMAKE_FONT=%{_datadir}/fonts/dejavu-sans-fonts/DejaVuSans.ttf .
%{make_build}

%install
%{make_install}

# Install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{scalable,48x48}/apps
install -pm644 data/tuxanci.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
convert -geometry 48x48 -depth 8 -background none data/tuxanci.svg \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/tuxanci.png

# Launcher
ln -s tuxanci-%{version} %{buildroot}%{_bindir}/tuxanci
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# Appdata
mkdir -p %{buildroot}%{_datadir}/appdata/
install -pm644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/appdata/tuxanci.appdata.xml

%files
%license LICENCE
%doc %{_docdir}/tuxanci-%{version}
%{_bindir}/tuxanci
%{_bindir}/tuxanci-%{version}
%{_libdir}/tuxanci-%{version}
%{_datadir}/tuxanci-%{version}
%{_datadir}/icons/hicolor
%{_datadir}/applications/tuxanci.desktop
%{_datadir}/appdata/tuxanci.appdata.xml

%changelog
* Mon Apr 27 2020 Petr Pisar <ppisar@redhat.com> - 0.21.0-12
- Convert a PNG icon with ImageMagick (bug #1800209)
- License corrected to "GPL+"
- Use system fonts

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 10 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.21.0-1
- Initial packaging
