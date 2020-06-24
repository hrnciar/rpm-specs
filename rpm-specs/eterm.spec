Summary:       Enlightened terminal emulator
Name:          eterm
Version:       0.9.6
Release:       23%{?dist}
License:       BSD
Source0:       http://www.eterm.org/download/Eterm-%{version}.tar.gz
Source1:       http://www.eterm.org/download/Eterm-bg-%{version}.tar.gz
Source2:       eterm.png
Patch0:        eterm-0.9.6-gcc10.patch
URL:           http://www.eterm.org/
Requires:      xorg-x11-fonts-misc
Requires:      xorg-x11-fonts-ISO8859-1-75dpi
Requires:      xorg-x11-fonts-ISO8859-1-100dpi
BuildRequires: desktop-file-utils
BuildRequires: gawk
BuildRequires: gcc
BuildRequires: glibc-common
BuildRequires: imlib2-devel
BuildRequires: libXmu-devel
BuildRequires: libast-devel
BuildRequires: pcre-devel
BuildRequires: sed
Provides:      Eterm = %{version}-%{release}
Obsoletes:     Eterm <= 0.9.2
%description
Eterm is a color vt102 terminal emulator with enhanced graphical
capabilities.  Eterm is intended to be a replacement for xterm for
Enlightenment window manager users, but it can also be used as a
replacement for xterm by users without Enlightenment.  Eterm supports
various themes and is very configurable, in keeping with the
philosophy of Enlightenment.

%prep
%setup -a 1 -q -n Eterm-%{version}
%patch0 -p1
for f in ChangeLog ; do
    mv $f $f.iso88591
    iconv -o $f -f iso88591 -t utf8 $f.iso88591
    rm -f $f.iso88591
done

%build
export PERL=%{__perl}
%configure --enable-multi-charset \
           --enable-escreen       \
           --enable-auto-encoding \
           --enable-trans         \
           --disable-etwin        \
           --disable-mmx          \
           --disable-rpath
sed -i -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

echo -e "[Desktop Entry]
Encoding=UTF-8
Name=Eterm
TryExec=Eterm
Exec=Eterm
Icon=eterm
Type=Application
Categories=Utility;TerminalEmulator;System;" > eterm.desktop

install -D -m 0644 eterm.desktop             \
  %{buildroot}%{_datadir}/applications/eterm.desktop
desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/eterm.desktop
install -D -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/eterm.png
rm -f %{buildroot}/%{_libdir}/libEterm.{a,la,so}

%files
%license LICENSE
%doc doc/Eterm_reference.html doc/Eterm.tcap 
%doc doc/Eterm.ti doc/README.Escreen
%doc README ReleaseNotes ReleaseNotes.1 ChangeLog
%{_bindir}/Esetroot
%{_bindir}/Etbg
%{_bindir}/Etbg_update_list
%{_bindir}/Etcolors
%{_bindir}/Eterm
%{_bindir}/Etsearch
%{_bindir}/Ettable
%{_bindir}/kEsetroot
%{_libdir}/libEterm-%{version}.so
%{_mandir}/man1/Eterm.1*
%{_datadir}/Eterm
%{_datadir}/applications/eterm.desktop
%{_datadir}/pixmaps/eterm.png

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 22 2019 Terje Rosten <terje.rosten@ntnu.no> - 0.9.6-22
- Fix GCC 10 build

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Terje Rosten <terje.rosten@ntnu.no> - 0.9.6-18
- Some clean up

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.6-8
- Drop desktop vendor tag.

* Sun Feb 24 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.9.6-7
- Revert #860326 (Ref: #867970 and #841471)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 08 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.9.6-5
- Fix startup dir issue (bz #860326)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 0.9.6-3
- Rebuild against PCRE 8.30

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.9.6-1
- 0.9.6
- Don't use %%makeinstall
- Fix ChangeLog
- Drop patches
- Remove rpath
- Fix defattr and files listing

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Mar 01 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.9.5-7
- Remove req. on bitmap-fonts, not needed.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 01 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.9.5-5
- Add xorg-x11-fonts-misc to req.

* Sun Mar 01 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.9.5-4
- Add more fonts to req.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 10 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.9.5-2
- Add patch to remove KDE cut-paste patch

* Tue Aug 12 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.9.5-1
- 0.9.5
- Remove CVE-2008-1692 patch now upstream
- Add req on bitmap-fonts to bring in some fonts (bz #454937)

* Tue Apr 08 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.9.4-10
- Closing CVE-2008-1692

* Sat Feb 09 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.9.4-9
- Rebuild

* Tue Aug 28 2007 Terje Rosten <terje.rosten@ntnu.no> - 0.9.4-8
- Need gawk to build

* Tue Aug 28 2007 Terje Rosten <terje.rosten@ntnu.no> - 0.9.4-7
- Rebuild

* Mon Jun 25 2007 Terje Rosten <terje.rosten@ntnu.no> - 0.9.4-6
- Remove Application from Categories list in desktop file

* Sun Nov 26 2006 Terje Rosten <terje.rosten@ntnu.no> - 0.9.4-5
- Move to System Tools menu (bz #241054)

* Sun Nov 26 2006 Terje Rosten <terje.rosten@ntnu.no> - 0.9.4-4
- Add patch to build with automake-1.10
- Add smp flags to make

* Sat Nov 25 2006 Terje Rosten <terje.rosten@ntnu.no> - 0.9.4-3
- Use automake-1.9

* Fri Nov 24 2006 Terje Rosten <terje.rosten@ntnu.no> - 0.9.4-2
- Add libXmu-devel and pcre-devel to BuildReq
- Simplify desktop file handling
- Add --disable-etwin to configure

* Sat Sep  2 2006 Terje Rosten <terje.rosten@ntnu.no> - 0.9.4-1
- 0.9.4
- LICENSE now included in upstream package
- Add rpath patch
- Touching Makefile.am, add auto* tools buildreq.

* Sun Feb 19 2006 Terje Rosten <terje.rosten@ntnu.no> - 0.9.3-2
- Add LICENSE
- UTF-8 specfile
- Fix buildroot var
- Not explicit depend on libast

* Sun Feb 19 2006 Terje Rosten <terje.rosten@ntnu.no> - 0.9.3-1
- 0.9.3

* Wed Nov 13 2002 Che
- initial rpm release
