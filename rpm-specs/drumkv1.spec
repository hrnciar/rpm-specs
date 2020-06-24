Summary:       An old-school drum-kit sampler
Name:          drumkv1
Version:       0.9.14
Release:       1%{?dist}
License:       GPLv2+
URL:           https://%{name}.sourceforge.io
Source0:       https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Do not strip executables
Patch0:        drumkv1-nostrip.patch

BuildRequires: gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsndfile-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: lv2-devel
BuildRequires: desktop-file-utils
BuildRequires: libsndfile-devel
BuildRequires: liblo-devel
BuildRequires: libappstream-glib
Requires:      hicolor-icon-theme

%description
%{name} is an old-school all-digital drum-kit sampler synthesizer with
stereo fx.

%package -n lv2-%{name}
Summary:       An LV2 port of %{name}
Requires:      lv2

%description -n lv2-%{name}
An LV2 plugin of the %{name} synth

%prep
%autosetup -p1

# Remove cruft from appdata file
pushd src/appdata
iconv -f utf-8 -t ascii//IGNORE -o tmpfile %{name}.appdata.xml 2>/dev/null || :
mv -f tmpfile %{name}.appdata.xml
popd

%build
%configure
%make_build

%install
%make_install
chmod +x %{buildroot}%{_libdir}/lv2/%{name}.lv2/%{name}.so

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%doc AUTHORS README ChangeLog
%license COPYING
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_bindir}/%{name}_jack
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/man/man1/%{name}.*
%{_metainfodir}/%{name}.appdata.xml

%files -n lv2-%{name}
%doc AUTHORS README ChangeLog
%license COPYING
%{_libdir}/lv2/%{name}.lv2/

%changelog
* Sun May 24 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.14-1
- Update to 0.9.14

* Mon Apr 20 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.13-2
- Validate AppData

* Sun Apr 19 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.13-1
- Update to 0.9.13
- Enable OSC support
- Some spec cleanup

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Brendan Jones <brendan.jones.it@gmail.com> - 0.9.10-1
- Update to 0.9.10

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Brendan Jones <brendan.jones.it@gmail.com> - 0.9.2-1
- Update to 0.9.2

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.6-2
- Remove obsolete scriptlets

* Sun Dec 24 2017 Brendan Jones <brendan.jones.it@gmail.com> - 0.8.6-1
- Update to 0.8.6

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 25 2017 Brendan Jones <brendan.jones.it@gmail.com> - 0.8.3-1
- Update to 0.8.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 27 2016 Brendan Jones <brendan.jones.it@gmail.com> - 0.7.6-3
- Install desktop file

* Tue Sep 20 2016 Brendan Jones <brendan.jones.it@gmail.com> - 0.7.6-2
- Add missing libsndfile

* Tue Sep 20 2016 Brendan Jones <brendan.jones.it@gmail.com> - 0.7.6-1
- Update to 0.7.6

* Sat Apr 23 2016 Brendan Jones <brendan.jones.it@gmail.com> 0.7.4-1
- Update to 0.7.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 21 2015 Brendan Jones <brendan.jones.it@gmail.com> 0.7.1-1
- Update to 0.7.1
- enable Qt5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Brendan Jones <brendan.jones.it@gmail.com> 0.6.2-1
- Update to 0.6.2

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar 22 2015 Brendan Jones <brendan.jones.it@gmail.com> 0.6.1-1
- Update to 0.6.1


* Tue Feb 03 2015 Brendan Jones <brendan.jones.it@gmail.com> 0.6.0-1
- Update to 0.6.0

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 0.5.1-2
- update mime scriptlet

* Thu Sep 25 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.5.1-1
- Update to 0.5.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 08 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.5.0-2
- Fix FTBFS on secondary 64bit arches

* Tue Jul 08 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.5.0-1
- Update to 0.5.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 11 2014 Brendan Jones <brendan.jones.it@gmail.com> 0.3.6-1
- Update to 0.3.6

* Fri Oct 04 2013 Dan Horák <dan[at]danny.cz> 0.3.5-2
- update also src_lv2ui.pro for all 64-bit arches

* Tue Oct 01 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.3.5-1
- Update to 0.3.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.3.4-1
- Update to 0.3.4

* Fri Mar 08 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.3.2-1
- New upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.3.0-1
- New upstream release

* Mon Nov 19 2012 Dan Horák <dan[at]danny.cz> 0.1.0-5
- updated for all 64-bit arches

* Sat Nov 17 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.1.0-4
- Renable hidden source directories
- Add COPYING to lv2 plugin
- Force LV2 path in configure
- Correct arch handling
- Remove explicit version requires on lv2

* Thu Nov 15 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.1.0-3
- Remove hidden source directories

* Fri Oct 26 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.1.0-2
- Clean up spec

* Thu Oct 25 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.1.0-1
- Initial build
