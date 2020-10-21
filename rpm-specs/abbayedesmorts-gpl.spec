%global commit 9ce56f69dec5e185058508cb924b1f597a1380e5 
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           abbayedesmorts-gpl
Version:        2.0.1
Release:        13.20170709git%{?dist}
Summary:        Platform game set in 13th century

# Graphics and Sounds are licensed under
# Creative Commons 3.0 Attribution license.
License:        GPLv3 and CC-BY
# Original Windows game by locomalito
# https://locomalito.com/abbaye_des_morts.php
URL:            https://github.com/nevat/abbayedesmorts-gpl 
Source0:        https://github.com/nevat/abbayedesmorts-gpl/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source1:        abbaye.appdata.xml
Patch0:         %{name}-2.0.1-ldflags.patch

BuildRequires:  gcc
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

%description
In the 13th century, the Cathars, who preach about good Christian beliefs, 
were being expelled by the Catholic Church out of the Languedoc region in 
France.

One of them, called Jean Raymond, found an old church in which to hide, not 
knowing that beneath its ruins lay buried an ancient evil.

A style close to Spectrum ZX, with its dark background and bright colors, 
proper fit with the story, because it does look old and somewhat horrifying. 
Also, the gameplay is directly inspired by Manic Miner and Jet Set Willy.


%prep
%autosetup -n %{name}-%{commit}


%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build


%install
%make_install

# Validate desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/abbaye.desktop

# Install AppData file
install -d %{buildroot}%{_datadir}/metainfo
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/abbaye.appdata.xml


%files
%{_bindir}/abbayev2
%{_datadir}/abbayev2
%{_datadir}/metainfo/abbaye.appdata.xml
%{_datadir}/applications/abbaye.desktop
%{_datadir}/pixmaps/abbaye.png
%doc ReadMe.md ChangeLog.md screenshots
%license COPYING


%changelog
* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-13.20170709git
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-12.20170709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-11.20170709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10.20170709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9.20170709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8.20170709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Andrea Musuruane <musuruan@gmail.com> - 2.0.1-7.20170709git
- Added gcc dependency
- Used new AppData directory
- Spec file clean up

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6.20170709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5.20170709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4.20170709git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Andrea Musuruane <musuruan@gmail.com> - 2.0.1-3.20170709git
- Fixed AppData file
- Fixed LDFLAGS usage

* Thu Jul 13 2017 Andrea Musuruane <musuruan@gmail.com> - 2.0.1-2.20170709git
- Updated to new upstream post-release
- Added missing BR

* Sat Jul 08 2017 Andrea Musuruane <musuruan@gmail.com> - 2.0.1-1
- First release

