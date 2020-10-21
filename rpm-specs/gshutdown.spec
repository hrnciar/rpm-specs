Name:		gshutdown
Version:	0.2        
Release:	29%{?dist}
Summary:	GShutDown is an advanced shut down utility for GNOME

License:	GPLv2+
URL:		http://gshutdown.tuxfamily.org/
Source0:	http://gshutdown.tuxfamily.org/release/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:	libglade2-devel, desktop-file-utils
BuildRequires:	libnotify-devel, glib2-devel, gettext

Patch0: gshutdown-0.2.libnotify-api.patch
Patch1: gshutdown-0.2.explicitlink.patch
Patch2: gshutdown-0.2-glib.patch
Patch3: gshutdown-0.2-format-security.patch

%description
GShutdown is an advanced shutdown utility which
allows you to schedule the shutdown or the restart
of your computer, or logout your actual session.
Also can be use under Xfce and KDE.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .libnotify-api
%patch1 -p1 -b .explicitlink
%patch2 -p1 -b .glib
%patch3 -p1

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

desktop-file-install					\
	--vendor ""					\
	--dir $RPM_BUILD_ROOT/%{_datadir}/applications	\
	--mode 0644					\
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %{name}




%files -f %{name}.lang
%doc COPYING AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/pixmaps/%{name}.png


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2-23
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 06 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.2-16
- Add gshutdown-0.2.format-security.patch (F21FTBFS RHBZ#1106732, RHBZ#1037106).
- Fix bogus %%changelog entries.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 01 2012 Jon Ciesla <limburgher@gmail.com> - 0.2-12
- Tom Lane's glib fixes for libpng15 rebuild, BZ 843648.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.2-9
- Rebuild for new libpng

* Thu Apr 07 2011 Caolán McNamara <caolanm@redhat.com> - 0.2-8
- Resolves: rhbz#599784 rebuild for new libnotify api, etc.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.2-4
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2-3
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.2-2
- Rebuild for selinux ppc32 issue.

* Mon Jul 09 2007 Xavier Lamien <lxtnow@gmail.com> - 0.2-1
- Updated Release.

* Tue May 01 2007 Xavier lamien <lxtnow@gmail.com> - 0.2-0.3.rc1
- Fixed redundant BR and Requires.

* Thu Jan 04 2007 Xavier lamien <lxtnow@gmail.com> - 0.2-0.2.rc1
- added post and postun for installed icons.
- fixed release tags
- Added timestamp in "make install".
- Removed "--add-category" from desktop-file-install.

* Wed Jan 03 2007 Xavier lamien <lxtnow@gmail.com> - 0.2-0.1.rc1
- Initial RPM release.
