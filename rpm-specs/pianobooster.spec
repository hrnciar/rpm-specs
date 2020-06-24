Name:            pianobooster
Summary:         A MIDI file player that teaches you how to play the piano
Version:         0.6.4b
Release:         22%{?dist}
License:         GPLv3+
URL:             http://pianobooster.sourceforge.net/
Source0:         http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.gz
Source1:         %{name}.desktop
# link libpthread and libGL explicitly
Patch0:          pianobooster-0.6.4b-explicit-linking.patch
BuildRequires:   cmake
BuildRequires:   qt4-devel
BuildRequires:   desktop-file-utils
BuildRequires:   alsa-lib-devel

%description
A MIDI file player/game that displays the musical notes AND teaches you how
to play the piano. 

PianoBooster is a fun way of playing along with a musical accompaniment and
at the same time learning the basics of reading musical notation.
The difference between playing along to a CD or a standard MIDI file
is that PianoBooster listens and reacts to what you are playing on a
MIDI keyboard.


%prep
%setup -q -n %{name}-src-%{version}
%patch0 -p1 -b .linkpthread

sed -e 's|\r||g' README.txt > README.txt.tmp
touch -r README.txt README.txt.tmp
mv README.txt.tmp README.txt

sed -e 's|\r||g' license.txt > license.txt.tmp
touch -r license.txt license.txt.tmp
mv license.txt.tmp license.txt

find -name '*.cpp' -exec chmod a-x {} \;
find -name '*.h' -exec chmod a-x {} \;

%build
pushd build
%cmake ../src
make %{?_smp_mflags}
popd

%install
rm -rf $RPM_BUILD_ROOT
pushd build
install -d $RPM_BUILD_ROOT/%{_bindir}
install %{name} $RPM_BUILD_ROOT/%{_bindir}
popd

install -d $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications  \
    %{SOURCE1}


install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -m 644 -p src/images/Logo32x32.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -m 644 -p src/images/logo64x64.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%files
%doc license.txt gplv3.txt README.txt
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4b-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4b-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4b-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4b-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4b-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.4b-17
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4b-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4b-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4b-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4b-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.4b-11
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4b-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug  3 2012 Jan Horak <jhorak@redhat.com> - 0.6.4b-6
- Removed -mwindows build parameter

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May 06 2010 Christian Krause <chkr@fedoraproject.org> - 0.6.4b-2
- Link libpthread and libGL explicitly

* Thu May 06 2010 Christian Krause <chkr@fedoraproject.org> - 0.6.4b-1
- Update to new upstream version 0.6.4b (fixes BZ 571030)
- Fix permission problem on source files in debuginfo package

* Sun Dec 06 2009 Christian Krause <chkr@fedoraproject.org> - 0.6.4-1
- Update to new upstream version 0.6.4
- Fix icon permissions

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 17 2009 Christian Krause <chkr@fedoraproject.org> - 0.6.2-4
- preserve timestamps of README.txt and license.txt

* Sun Apr 12 2009 Christian Krause <chkr@fedoraproject.org> - 0.6.2-3
- use %%{name} macro
- provide .desktop file as separate source1
- use sed instead of dos2unix
- use install -p to preserve the timestamps 
- add GenericName to desktop file
- fix typo in icon installation
- enabled parallel build

* Tue Apr 07 2009 Christian Krause <chkr@fedoraproject.org> - 0.6.2-2
Initial spec file.
