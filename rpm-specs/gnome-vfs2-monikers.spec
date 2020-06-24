%define gnome_vfs_version 2.15.3
%define libbonobo_version 2.3.1
%define gconf_version 1.1.1
%define glib_version 2.9.3
%define orbit_version 2.9.0

Summary: Monikers for the GNOME virtual file-system
Name: gnome-vfs2-monikers
Version: 2.15.3
Release: 25%{?dist}
License: LGPLv2+
Source0: http://ftp.gnome.org/pub/gnome/sources/gnome-vfs-monikers/2.15/gnome-vfs-monikers-%{version}.tar.bz2
URL: http://www.gnome.org/
Requires:      gnome-vfs2 >= %{gnome_vfs_version}
BuildRequires:  gcc
BuildRequires: gnome-vfs2-devel >= %{gnome_vfs_version}
BuildRequires: libbonobo-devel >= %{libbonobo_version}
BuildRequires: GConf2-devel >= %{gconf_version}
BuildRequires: glib2-devel >= %{glib_version}
BuildRequires: ORBit2-devel >= %{orbit_version}
BuildRequires: perl(XML::Parser)

%description
GNOME VFS is the GNOME virtual file system. 
Programs using bonobo can use the monikers provided
in this package to access gnome-vfs.

%prep
%setup -q -n gnome-vfs-monikers-%{version}

%build
%configure 
make 

%install
rm -fr $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT 

rm -f $RPM_BUILD_ROOT%{_libdir}/bonobo/monikers/*.{a,la}

for serverfile in $RPM_BUILD_ROOT%{_libdir}/bonobo/servers/*.server; do
    sed -i -e 's|location *= *"/usr/lib\(64\)*/|location="/usr/$LIB/|' $serverfile
done

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING.LIB NEWS 

%{_libdir}/bonobo

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 07 2013 Jon Ciesla <limburgher@gmail.com> - 2.15.3-13
- Drop bonobo-activation-devel BR to fix FTBFS, BZ 992408.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.15.3-5
- Autorebuild for GCC 4.3

* Wed Oct 10 2007 Matthias Clasen <mclasen@redhat.com> - 2.15.3-4
- Rebuild
- Update license field

* Tue Apr 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.15.3-3
- Improve description (#219057)

* Wed Jul 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.3-2
- Incorporate package review feedback

* Wed Jul 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.3-1 
- Initial package
