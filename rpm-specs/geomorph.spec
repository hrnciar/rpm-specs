Name:           geomorph
Version:        0.62
Release:        11%{?dist}
Summary:        A height field editor for Linux
License:        GPLv2
URL:            http://geomorph.sourceforge.net
Source0:        http://sourceforge.net/projects/geomorph/files/geomorph/%{version}/%{name}-%{version}.tar.gz
Source1:        geomorph.desktop
Source2:        geomorph.appdata.xml
Source3:        geomorph.png
Patch0:         geomorph-format-security.patch
Patch1:         geomorph-array-bounds.patch
Patch2:         geomorph-glxbadcontext.patch
Patch3:         geomorph-gnusource.patch
Patch4:         geomorph-x_alloc.patch
Patch5:         geomorph-missing-string-headers.patch
Patch6:         geomorph-missing-custom-headers.patch
Patch7:         geomorph-define-get_current_dir_name-function.patch
Patch8:         geomorph-explicit-braces.patch
Patch9:         geomorph-int-to-pointer-cast.patch
Patch10:        geomorph-uninitialized-values.patch
Patch11:        geomorph-return-functions.patch
Patch12:        geomorph-printf-format.patch
Patch13:        geomorph-pointer-to-int-cast.patch
Patch14:        geomorph-pointer-sign.patch
Patch15:        geomorph-remove-gettext-at-compile-time.patch
Patch16:        geomorph-arg-not-used.patch
Patch17:        geomorph-incompatible-pointer-types.patch
Patch18:        geomorph-no-common.patch
#Patch20:        geomorph-update-autotools.patch

BuildRequires:  gcc
BuildRequires:  gtkglext-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
#BuildRequires:  /usr/bin/autoreconf
#BuildRequires:  gettext-devel
#BuildRequires:  automake
Requires:       povray

%description
Geomorph is a height field generator and editor for the Linux operating system.
A height field is a kind of topographic map.  It is a 2D projection of a 
3D landscape.
Geomorph generates square images and shows a 3D preview of the resulting
landscape.  The resulting 2D image can be processed with a tool like Povray
for rendering the landscape.

%prep
%setup -qn %{name}-%{version}
%patch0 -p1 -b .format-security
%patch1 -p1 -b .array-bounds
%patch2 -p1 -b .glxbadcontext
%patch3 -p1 -b .gnusource
%patch4 -p1 -b .x_alloc
%patch5 -p1 -b .missing-string-headers
%patch6 -p1 -b .missing-custom-headers
%patch7 -p1 -b .define-get_current_dir_name-function
%patch8 -p1 -b .explicit-braces
%patch9 -p1 -b .int-to-pointer-cast
%patch10 -p1 -b .uninitialized-values
%patch11 -p1 -b .return-functions
%patch12 -p1 -b .printf-format
%patch13 -p1 -b .pointer-to-int-cast
%patch14 -p1 -b .pointer-sign
%patch15 -p1 -b .remove-gettext-at-compile-time
%patch16 -p1 -b .arg-not-used
%patch17 -p1 -b .incompatible-pointer-types
%patch18 -p1 -b .no-common.patch
#%patch20 -p1 -b .update-autotools
#autoreconf -vfi

# to avoid rpmlint warnings
# Remove exe bit from pixmaps
find . -name \*.xpm -exec chmod -x {} \;
# Switch to UTF-8
for file in LISEZMOI AFAIRE FAQ-fr
do
    iconv -f ISO-8859-1 -t UTF-8 $file > $file.utf8
    touch -r $file $file.utf8
    mv -f $file.utf8 $file
done
# Tarball contains an already compiled app.
# Remove and recompile it.
%{__rm} -f scenes/colmap

# Remove Hardcoded path
for file in install-step1-dir install-step2-rcfile install-step3-menu \
    install-step4-desktop install-user src/app/app.c src/app/main.c
do
    sed -i -e '/^VERSION/ s#=.*#=%{version}#g' \
        -e 's#/usr/local/share/geomorph#%{_datadir}/geomorph#g' \
        $file
done

%configure \
    --disable-rpath

%build
pushd scenes
%{__cc} ${RPM_OPT_FLAGS} -Wl,-z,relro,-z,now -o colmap colmap.c
popd
make %{?_smp_mflags}

%install
make install DESTDIR="%{buildroot}"
%find_lang %{name}
mv %{buildroot}%{_datadir}/geomorph/%{version}/scenes/colmap %{buildroot}%{_bindir}/
%{__rm} -f %{buildroot}%{_datadir}/geomorph/%{version}/scenes/colmap.c
# Create directories
%{__mkdir_p} %{buildroot}%{_datadir}/icons
%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{__mkdir_p} %{buildroot}%{_datadir}/appdata
# Copy new desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
# Copy icon file
%{__cp} %{SOURCE3} %{buildroot}%{_datadir}/icons
%{__cp} GeoMorph.xpm %{buildroot}%{_datadir}/icons
# Copy appdata
%{__cp} %{SOURCE2} %{buildroot}%{_datadir}/appdata

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files -f %{name}.lang
%doc ABOUT-NLS AFAIRE AUTHORS ChangeLog FAQ FAQ-fr LISEZMOI NEWS README TODO geomorphrc_de geomorphrc_en geomorphrc_fr
%{_bindir}/geomorph
%{_bindir}/colmap
%{_datadir}/geomorph
%{_datadir}/applications/geomorph.desktop
%{_datadir}/icons/geomorph.png
%{_datadir}/icons/GeoMorph.xpm
%{_datadir}/appdata/geomorph.appdata.xml

%changelog
* Tue Apr 07 2020 Didier Fabert <didier.fabert@gmail.com> - 0.62-11
- Fix no-common build issue

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 19 2016 Didier Fabert <didier.fabert@gmail.com> 0.62-2
- Bugfix: crash after PovRay rendering
- Fix a lot of compilation warnings

* Mon May 09 2016 Didier Fabert <didier.fabert@gmail.com> 0.62-1
- New upstream version

* Fri May 06 2016 Didier Fabert <didier.fabert@gmail.com> - 0.60.1-9
- Fix Gdk-ERROR: The program 'geomorph' received an X Window System error.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 18 2015 Didier Fabert <didier.fabert@gmail.com> 0.60.1-7
- Add RELRO flags to compile colmap

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 14 2015 Didier Fabert <didier.fabert@gmail.com> 0.60.1-5
- Add appdata and change icon format (xpm to png)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Didier Fabert <didier.fabert@gmail.com> 0.60.1-2
- Follow Fedora Guidelines

* Tue Feb 14 2012 Didier Fabert <didier.fabert@gmail.com> 0.60.1-1
- First Release
