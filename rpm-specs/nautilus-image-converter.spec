Name:           nautilus-image-converter
Version:        0.3.1
Release:        0.19.git430afce31%{?dist}
Summary:        Nautilus extension to mass resize images

License:        GPLv2+
URL:            http://www.bitron.ch/software/nautilus-image-converter.php
# Source code pulled from https://github.com/GNOME/nautilus-image-converter
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}.metainfo.xml
Patch0:         fix-rotate-dialog.patch

BuildRequires:  gcc
BuildRequires:  gtk3-devel >= 3.0.0
BuildRequires:  glib2-devel >= 2.28.0
BuildRequires:  nautilus-devel >= 3.0.0
BuildRequires:  intltool
BuildRequires:  perl(XML::Parser)
BuildRequires:  libappstream-glib
Requires:       ImageMagick
 

%description
Adds a "Resize Images..." menu item to the context menu of all images. This
opens a dialog where you set the desired image size and file name. A click
on "Resize" finally resizes the image(s) using ImageMagick's convert tool.


%prep
%setup -q
%patch0 -p1


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;
# Install metainfo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cp -a %SOURCE1 $RPM_BUILD_ROOT%{_datadir}/appdata


%files -f %{name}.lang
%doc AUTHORS COPYING
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.metainfo.xml
%{_libdir}/nautilus/extensions-3.0/*.so


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-0.19.git430afce31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-0.18.git430afce31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-0.17.git430afce31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-0.16.git430afce31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 22 2018 Tim Jackson <rpm@timj.co.uk> - 0.3.1-0.15.git430afce31
- Add missing BuildRequire on gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-0.14.git430afce31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-0.13.git430afce31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-0.12.git430afce31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-0.11.git430afce31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb  2 2016 Brian Pepple <bpepple@fedoraproject.org> - 0.3.1-0.10.git430afce31
- Add patch for dialog window. (#1297803)
- Ship AppStream metadata file. (#1301337)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-0.9.git430afce31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-0.8.git430afce31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-0.7.git430afce31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-0.6.git430afce31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-0.5.git430afce31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-0.4.git430afce31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-0.3.git430afce31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.3.1-0.2.git430afce31
- Rebuild for new libpng

* Fri Apr 15 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.3.1-0.1.git430afce31
- Update to gtk3 git snapshot.
- Drop buildroot.
- Drop unused variable patch. Fixed upstream.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Apr 25 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.3.0-5
- Removed clean section. No longer needed.

* Wed Jan  6 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.3.0-4
- Update src url.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Mar 28 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0.
- Add patch to fix unused variables compile errors.
- Drop BR on gnome-vfs2-devel.
- Drop extension directory patch. Fixed upstream.

* Fri Feb  8 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.2.1-3
- Rebuild for gcc-4.3.

* Mon Dec 24 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.2.1-2
- Rebuild for change to nautilus extension api change.
- Add patch to use new nautilus extension directory.

* Sat Dec 22 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1.

* Fri Oct  5 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0, which only has translation changes.

* Tue Aug 21 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.0.9-3
- Rebuild.

* Sun Aug  5 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.0.9-2
- Update license tag.

* Sun Dec 17 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.0.9-1
- Update to 0.0.9.

* Thu Dec  7 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.0.8-1
- Update to 0.0.8.

* Thu Dec  7 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.0.7-1
- Update to 0.0.7.

* Wed Dec  6 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.0.6-1
- Update to 0.0.6.

* Thu Sep  7 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.0.5-6
- Add BR on perl(XML::Parser).

* Thu Sep  7 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.0.5-5
- Rebuild for FC6.

* Fri Aug 11 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.0.5-4
- Add BR for nautilus-devel, due to Core change.

* Mon Feb 13 2006 Brian Pepple <bdpepple@ameritech.net> - 0.0.5-3
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Oct 17 2005 Brian Pepple <bdpepple@ameritech.net> - 0.0.5-2
- Update to 0.0.5.

* Mon Oct 10 2005 Brian Pepple <bdpepple@ameritech.net> - 0.0.4-2
- Update to 0.0.4.
- Add BR for gettext & handle translations.
- Change group to follow other nautilus plugins.

* Tue Sep 27 2005 Brian Pepple <bdpepple@ameritech.net> - 0.0.3-2
- Fix ownership of data directory.
- Add dist tag.

* Tue Sep 27 2005 Brian Pepple <bdpepple@ameritech.net> - 0.0.3-1
- Initial Fedora Extras release.

