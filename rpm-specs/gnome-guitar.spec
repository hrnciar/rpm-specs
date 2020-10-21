# This mono package produces an empty debuginfo package. Hence we disable it
%global debug_package %{nil}

Name:            gnome-guitar
Summary:         A small suite of applications for the guitarist
Version:         0.8.1
Release:         32%{?dist}
License:         GPLv3+
URL:             http://gnome-chord.sourceforge.net/
Source0:         http://downloads.sourceforge.net/gnome-chord/%{name}_cs-%{version}.tar.gz

# Mono only available on these:
ExclusiveArch:   %{mono_arches}

BuildRequires:   desktop-file-utils
BuildRequires:   gnome-sharp-devel
BuildRequires:   gtk-sharp2-devel
BuildRequires:   ImageMagick
BuildRequires:   mono-devel

Requires:        mono(gconf-sharp)
Requires:        hicolor-icon-theme
Requires(pre):   GConf2
Requires(post):  GConf2
Requires(preun): GConf2


%description
Gnome Guitar is chord and scale database for gnome. It can be used as a stand
alone application (for example you could use it to find how to play a specific
chord or scale) or it can integrate with other applications to provide chord
selection and rendering. 

%package devel
Summary:       Development files for %{name}
Requires:      pkgconfig
Requires:      %{name} = %{version}-%{release}

%description devel
Gnome Guitar is chord and scale database for gnome. It can be used as a stand
alone application (for example you could use it to find how to play a specific
chord or scale) or it can integrate with other applications to provide chord
selection and rendering.

This package contains pkg-config files for developing applications that will
use Gnome Guitar.

%prep
%setup -q -n %{name}_cs-%{version}

# Fix permission
chmod 644 gnome-chord/gpl-3.0.txt

# Add pixmaps to the desktop files
echo "Icon=gnome-chord" >> gnome-chord/gnome-chord.desktop
echo "Icon=gnome-scale" >> gnome-scale/gnome-scale.desktop

%build
%configure --disable-schemas-install
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# The provided fonts are non-square. We iron them out with some Magick
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/64x64/apps/
convert gnome-chord/pixmaps/gnome-chord-logo.png -resize 64x64\! \
        $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/64x64/apps/gnome-chord.png
convert gnome-scale/pixmaps/gnome-scale-logo.png -resize 64x64\! \
        $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/64x64/apps/gnome-scale.png

desktop-file-install                                    \
--add-category="AudioVideo"                             \
--add-category="X-AudioVideoTools"                      \
--dir=%{buildroot}%{_datadir}/applications              \
%{buildroot}/%{_datadir}/applications/gnome-chord.desktop

desktop-file-install                                    \
--add-category="AudioVideo"                             \
--add-category="X-AudioVideoTools"                      \
--dir=%{buildroot}%{_datadir}/applications              \
%{buildroot}/%{_datadir}/applications/gnome-scale.desktop


%pre
if [ "$1" -gt 1 ] ; then
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-uninstall-rule \
   %{_sysconfdir}/gconf/schemas/libgnomeguitar.schemas >/dev/null || :
fi

%preun
if [ "$1" -eq 0 ] ; then
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-uninstall-rule \
   %{_sysconfdir}/gconf/schemas/libgnomeguitar.schemas > /dev/null || :
fi

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
   %{_sysconfdir}/gconf/schemas/libgnomeguitar.schemas > /dev/null || :


%files
%doc gnome-chord/gpl-3.0.txt
%config %{_sysconfdir}/gconf/schemas/libgnomeguitar.schemas
%{_bindir}/gnome-chord
%{_bindir}/gnome-scale
%{_libdir}/%{name}_cs/
%{_datadir}/applications/gnome-chord.desktop
%{_datadir}/applications/gnome-scale.desktop
%{_datadir}/icons/hicolor/64x64/apps/gnome-chord.png
%{_datadir}/icons/hicolor/64x64/apps/gnome-scale.png

%files devel
%{_libdir}/pkgconfig/libgnomeguitar.pc
%{_libdir}/pkgconfig/libgnomeguitarui.pc

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-32
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-25
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-21
- mono rebuild for aarch64 support

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.1-18
- Rebuild (mono4)

* Sun Jan 25 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.1-17
- Update mono excludes

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 29 2011 Dan Horák <dan[at]danny.cz> - 0.8.1-10
- updated the supported arch list

* Tue Jan 11 2011 Lakshmi Narasimhan T V <lakshminaras2002@gmail.com> - 0.8.1-9
- Added hicolor-icon-theme in Requires

* Tue Dec 14 2010 Lakshmi Narasimhan <lakshminaras2002@gmail.com> - 0.8.1-8
- Remove excludearch for ppc64
- Change define to global, to be consistent with packaging guidelines at http://fedoraproject.org/wiki/Packaging/Debuginfo

* Mon Oct 26 2009 Dennis Gilmore <Dennis@ausil.us> - 0.8.1-7
- ExcludeArch sparc64

* Wed Aug 05 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.8.1-6
- Update .desktop files
- Add missing Requires

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 29 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.8.1-4
- Rebuild

* Fri May 29 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.8.1-3
- Mono is available in F-11. Remove the ExcludeArch: ppc64

* Mon Mar 09 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.8.1-2
- Add ExcludeArch:ppc64 since mono is not available in this architecture.
- devel subpackage requires pkgconfig

* Sat Mar 07 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.8.1-1
- Initial build
