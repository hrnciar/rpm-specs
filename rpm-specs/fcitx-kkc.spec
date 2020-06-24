Name:		fcitx-kkc
Version:	0.1.0
Release:	17%{?dist}
Summary:	Japanese Kana Kanji Engine for Fcitx

License:	GPLv3+
URL:		http://code.google.com/p/fcitx/
Source0:	http://download.fcitx-im.org/fcitx-kkc/%{name}-%{version}.tar.xz

BuildRequires:	fcitx-devel >= 0.4.8, libkkc-devel >= 0.2.3
BuildRequires:	cmake, gettext, intltool
Requires:	fcitx >= 0.4.8

%description
Fcitx-kkc is a Kana Kanji engine for Fcitx.  It provides Japanese
input method using libkkc.

%prep
%setup -q -n %{name}-%{version}


%build
mkdir -pv build
pushd build
%cmake ..
make VERBOSE=1 %{?_smp_mflags}
popd


%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -rf $RPM_BUILD_ROOT%{_includedir}/fcitx
popd

%find_lang %{name}



%files -f %{name}.lang
%doc
%{_libdir}/fcitx/%{name}.so
%{_libdir}/fcitx/qt/libfcitx-kkc-config.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/fcitx/inputmethod/kkc.conf
%{_datadir}/fcitx/kkc/
%{_datadir}/fcitx/imicon/kkc.png
%{_datadir}/icons/hicolor/64x64/apps/fcitx-kkc.png



%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-12
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.0-6
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 22 2013 Daiki Ueno <dueno@redhat.com> - 0.1.0-3
- Remove header file

* Wed Sep 18 2013 Daiki Ueno <dueno@redhat.com> - 0.1.0-2
- update license to GPLv3+
- drop buildroot cleanup

* Tue Jul  9 2013 Daiki Ueno <dueno@redhat.com> - 0.1.0-1
- initial packaging for Fedora, based on fcitx-libpinyin package

