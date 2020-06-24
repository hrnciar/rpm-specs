Name: kpassgen
Version: 1.4
Release: 18%{dist}
Summary: Random password creator

License: GPLv2
URL: http://kde-apps.org/content/show.php/KPassGen?content=108673
Source0: http://sourceforge.net/projects/kpassgen/files/1.x/kpassgen-%{version}.tar.gz
Source1: kpassgen.png

BuildRequires: kdelibs4-devel cmake make qt-devel desktop-file-utils
Requires: qt qt-x11

%description
Generates a set of random passwords of any length that can include the letter
a-z,A-Z,numbers,symbols and characters that QString can handle or hex values

%prep
%setup -q -n kpassgen

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} .. -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed"
popd
make %{?_smp_mflags} -C %{_target_platform}

%install
rm -rf %{buildroot}
make install/fast -C %{_target_platform} DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
desktop-file-validate %{buildroot}/%{_datadir}/applications/kde4/kpassgen.desktop

%post
touch --no-create %{_datadir}/pixmaps &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/pixmaps &>/dev/null
gtk-update-icon-cache %{_datadir}/pixmaps &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/pixmaps &>/dev/null || :

%files
%doc COPYING
%{_kde4_bindir}/kpassgen
%{_kde4_datadir}/applications/kde4/kpassgen.desktop
%{_kde4_datadir}/config.kcfg/*.kcfg
%{_kde4_datadir}/kde4/apps/kpassgen/kpassgenui.rc
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4-8
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 12 2011 changelog entry
  - Kpassgen 1.4 added

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
  - Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 siddharth Sharma <siddharths@fedoraproject.org> - 1.3-2
  - Build Require fix and Require fix
  - BuildRequires: desktop-file-utils
  - Requires: qt qt-x11

* Thu Dec 23 2010 siddharth Sharma <siddharths@fedoraproject.org> - 1.3-1
  - Initial Release 1

