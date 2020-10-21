Name:           qsstv
Version:        9.4.4
Release:        6%{?dist}
Summary:        Qt-based slow-scan TV and fax

License:        GPLv2+
URL:            http://users.telenet.be/on4qz/

#Source0:        http://users.telenet.be/on4qz/qsstv/downloads/%{name}_%{version}.tar.gz
Source0:        http://users.telenet.be/on4qz/qsstv/downloads/%{name}_%{version}.zip
Source1:        qsstv.desktop
Source2:        qsstv.1

BuildRequires:  gcc-c++ doxygen desktop-file-utils
BuildRequires:  fftw-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  hamlib-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  openjpeg-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  libv4l-devel


%description
Qsstv is a program for receiving slow-scan television and fax. These are
modes used by hamradio operators. Qsstv uses a soundcard to send and
receive images.


%package doc
Summary:             User manual for Qsstv.
BuildArch:           noarch
Requires:            %{name} = %{version}-%{release}

%description doc
User manual for Qsstv.


%prep
%autosetup -n %{name}_%{version}

# Honor build flags...
sed -i "s/\-O0/\-O2/g" qsstv/qsstv.pro


%build 
# mode_and_occupancy_code_table has different sizes  in its declaration
# vs its definition.  This is a hard error when using LTO and must be
# resolved before this package can use LTO
%define _lto_cflags %{nil}

qmake-qt5 PREFIX=%{_prefix} CONFIG+=debug QMAKE_CXXFLAGS+="-std=c++14 %{optflags}"
make %{?_smp_mflags}


%install
INSTALL_ROOT=%{buildroot}; export INSTALL_ROOT
make install 

# Install icon
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp -p qsstv/icons/qsstv.png %{buildroot}%{_datadir}/pixmaps/

desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# Install man page borrowed from Debian
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 0644 %{SOURCE2} %{buildroot}%{_mandir}/man1/

find %{buildroot} -type f -name "*.a" -exec rm -f {} \;


%files
%license COPYING
%doc README.txt
%{_bindir}/* 
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*%{name}.desktop
%{_mandir}/man1/%{name}.1*

%files doc
%{_pkgdocdir}/


%changelog
* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 9.4.4-6
- Force C++14 as this code is not C++17 ready

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Jeff Law <law@redhat.com> - 9.4.4-4
- Disable LTO

* Tue Mar 31 2020 Richard Shaw <hobbes1069@gmail.com> - 9.4.4-3
- Rebuild for hamlib 4.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Richard Shaw <hobbes1069@gmail.com> - 9.4.4-1
- Update to 9.4.4.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 2019 Richard Shaw <hobbes1069@gmail.com> - 9.4.1-1
- Update to 9.4.1.

* Thu Apr 18 2019 Richard Shaw <hobbes1069@gmail.com> - 9.3.3-1
- Update to 9.3.3.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 30 2018 Richard Shaw <hobbes1069@gmail.com> - 9.2.6-4
- Rebuild for hamlib 3.3.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Richard Shaw <hobbes1069@gmail.com> - 9.2.6-1
- Upate to latest upstream release.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Richard Shaw <hobbes1069@gmail.com> - 9.2.4-3
- Rebuild for hamlib 3.1.

* Mon Dec 26 2016 Richard Shaw <hobbes1069@gmail.com> - 9.2.4-2
- Rebuild to honor build flags.

* Sat Oct 22 2016 Richard Shaw <hobbes1069@gmail.com> - 9.2.4-1
- Update to latest upstream release.

* Mon Oct 10 2016 Richard Shaw <hobbes1069@gmail.com> - 9.2.2-1
- Beta release.

* Mon Jul 25 2016 Richard Shaw <hobbes1069@gmail.com> - 9.1.8-1
- Update to latest upstream release.

* Mon Jul  4 2016 Richard Shaw <hobbes1069@gmail.com> - 9.1.7-1
- Update to latest upstream release.

* Wed Jun 29 2016 Richard Shaw <hobbes1069@gmail.com> - 9.1.6-1
- Update to latest upstream release.

* Sun Apr 17 2016 Richard Shaw <hobbes1069@gmail.com> - 9.1.5-1
- Update to latest upstream release.

* Sat Apr 16 2016 Richard Shaw <hobbes1069@gmail.com> - 9.1.4-1
- Update to latest upstream release.

* Mon Apr 11 2016 Richard Shaw <hobbes1069@gmail.com> - 9.1.3-1
- Update to latest upstream release.

* Sun Apr 10 2016 Richard Shaw <hobbes1069@gmail.com> - 9.1.1-1
- Update to latest upstream release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
 
* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 8.2.12-2
- use %%qmake_qt5 macro to ensure proper build flags

* Sun Jul 12 2015 Richard Shaw <hobbes1069@gmail.com> - 8.2.12-1
- Fix grey pictures TX for some modes.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 8.2.11-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 23 2015 Richard Shaw <hobbes1069@gmail.com> - 8.2.11-1
- Update to latest upstream release, 8.2.11.
- Fixes CAT control bug.

* Sun Mar  1 2015 Richard Shaw <hobbes1069@gmail.com> - 8.2.10-1
- Update to latest upstream release, 8.2.10.

* Sun Dec  7 2014 Richard Shaw <hobbes1069@gmail.com> - 8.2.9-1
- Update to latest upstream release.

* Sat Oct 11 2014 Richard Shaw <hobbes1069@gmail.com> - 8.2.8-1
- Update to latest upstream release.
- Move documentation to a doc subpackage.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Richard Shaw <hobbes1069@gmail.com> - 8.2.7-1
- Update to latest upstream release.

* Fri Apr  4 2014 Richard Shaw <hobbes1069@gmail.com> - 8.2.6-1
- Update to latest upstream release.

* Sat Mar  8 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 8.2.4-2
- Rebuild against fixed qt to fix -debuginfo (#1074041)

* Sun Mar  2 2014 Richard Shaw <hobbes1069@gmail.com> - 8.2.4-1
- Update to latest upstream release.

* Tue Feb 11 2014 Richard Shaw <hobbes1069@gmail.com> - 8.1.17-1
- Update to latest upstream release.

* Wed Jan 29 2014 Richard Shaw <hobbes1069@gmail.com> - 8.1.14-1
- Update to latest upstream release.

* Sun Jan 26 2014 Richard Shaw <hobbes1069@gmail.com> - 8.1.13-1
- Update to latest upstream release.

* Mon Jan  6 2014 Richard Shaw <hobbes1069@gmail.com> - 8.1.12-1
- Update to latest upstream release.

* Tue Dec 17 2013 Richard Shaw <hobbes1069@gmail.com> - 8.1.3
- Update to latest upstream release.

* Sun Aug 05 2012 Richard Shaw <hobbes1069@gmail.com> - 7.1.7-1
- Update to latest upstream release.

* Fri Nov 27 2009 Lucian Langa <cooly@gnome.eu.org> - 5.3c-6
- improve desktop file (#530838)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3c-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Aug 24 2008 Lucian Langa <cooly@gnome.eu.org> - 5.3c-3
- fix build requires

* Sun Aug 17 2008 Lucian Langa <cooly@gnome.eu.org> - 5.3c-2
- add desktop file

* Sun Aug 10 2008 Lucian Langa <cooly@gnome.eu.org> - 5.3c-1
- Misc cleanups

* Mon Dec 10 2007 Sindre Pedersen Bjørdal - 0.5c-1
- Initial build

