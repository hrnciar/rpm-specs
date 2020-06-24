Name:			fcitx-anthy
Version:		0.2.2
Release:		10%{?dist}
Summary:		Anthy Engine for Fcitx
License:		GPLv2+
URL:			https://fcitx-im.org/wiki/Anthy
Source0:		http://download.fcitx-im.org/fcitx-anthy/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	fcitx-devel
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	anthy-devel
BuildRequires:	gcc-c++
Requires:		fcitx
Requires:		dbus-x11

%description
Fcitx-anthy is an Anthy engine wrapper for Fcitx. It provides a Japanese input
method. You can input hiragana and katakana by romaji or using a Japanese
keyboard. And fcitx-anthy also supports converting hiragana or katakana to
kanji.

%prep
%setup -q 


%build
mkdir -pv build
pushd build
%cmake ..
make %{?_smp_mflags} VERBOSE=1

%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
popd

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING AUTHORS README
%{_libdir}/fcitx/%{name}.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/anthy/
%{_datadir}/fcitx/inputmethod/anthy.conf
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/fcitx/imicon/anthy.png
%{_datadir}/icons/hicolor/48x48/status/%{name}.png
%{_datadir}/icons/hicolor/22x22/status/%{name}-symbol.png
%{_datadir}/icons/hicolor/scalable/status/%{name}-*.svg

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 31 2015 Robin Lee <cheeselee@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2
- Requires dbus-x11 (BZ#1248835)
- BR: gcc-c++

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 10 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.2.0-2
- Own the diretory %%{_datadir}/fcitx/anthy/
- description enlarged

* Fri Aug 23 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0, open new review request

* Wed Dec 12 2012 Liang Suilong <liangsuilong@gmail.com> - 0.1.1-1
- Initial Package
