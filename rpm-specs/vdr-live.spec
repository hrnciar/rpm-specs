# https://projects.vdr-developer.org/git/vdr-plugin-live.git/commit/?id=e582514ede475574842b44ca6792335ff141172d
%global commit0  e582514ede475574842b44ca6792335ff141172d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gitdate 20170623

Name:           vdr-live
Version:        2.3.1
Release:        13.%{gitdate}git%{shortcommit0}%{?dist}
Summary:        An interactive web interface for VDR

# The entire source code is GPLv2+ except live/js/mootools/ which is MIT
License:        GPLv2+ and MIT
URL:            http://projects.vdr-developer.org/projects/plg-live
# how to get the tarball
# go to http://projects.vdr-developer.org/git/vdr-plugin-live.git/commit/
# click the link behind commit, then select the download links below.
Source0:        http://projects.vdr-developer.org/git/vdr-plugin-live.git/snapshot/vdr-plugin-live-%{commit0}.tar.bz2
Source1:        %{name}.conf
# Patch to mark and sort new recordings + more gadgets
# https://www.vdr-portal.de/index.php?attachment/42233-vdr-plugin-live-2018-11-04-diff/
Patch0:         vdr-plugin-live_2018-11-04.diff

BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= 2.2.0
BuildRequires:  pcre-devel
BuildRequires:  tntnet-devel
BuildRequires:  cxxtools-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
Requires:       %{name}-data = %{version}-%{release}

%description
Live, the "Live Interactive VDR Environment", is a plugin providing the
possibility to interactively control the VDR and some of it's plugins by
a web interface.

Unlike external utility programs that communicate with VDR and it's plugins
by SVDRP, Live has direct access to VDR's data structures and is thus very
fast.

%package data
Summary:       Images, themes and JavaScript for %{name}
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}

%description data
This package contains images, themes and JavaScript.

%prep
%setup -q -n vdr-plugin-live-%{commit0}
%patch0 -p1

# delete unused directories and files
find -name .git -type d -or -name gitignore -type d | xargs rm -rfv

# remove bundled tntnet libraries
rm -rf httpd

iconv -f iso-8859-1 -t utf-8 README > README.utf8 ; mv README.utf8 README

sed -i -e 's|std::auto_ptr|std::unique_ptr|' thread.h

%build
make CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" all

%install
make install DESTDIR=%{buildroot}

# live.conf
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/live.conf

%find_lang %{name}

install -dm 755 %{buildroot}%{vdr_resdir}/plugins/live
cp -pR live/* %{buildroot}%{vdr_resdir}/plugins/live


%files -f %{name}.lang
%doc CONTRIBUTORS README
%license COPYING
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/live.conf
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

%files data
%{vdr_resdir}/plugins/live/


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-13.20170623gite582514
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-12.20170623gite582514
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.3.1-11.20170623gite582514
- Update to last git version 20170623gite582514
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-10.20170519git5cb665d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 05 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.3.1-9.20170519git5cb665d
- Add vdr-plugin-live_2018-11-04.diff

* Wed Oct 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.3.1-8.20170519git5cb665d
- Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7.20170519git5cb665d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.3.1-6.20170619git5cb665d
- Rebuilt for vdr-2.4.0

* Wed Feb 14 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.3.1-5.20170619git5cb665d
- Disable parallel make due build error on rawhide

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4.20170519git5cb665d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3.20170519git5cb665d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2.20170519git5cb665d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Martin Gansser <martinkg@fedoraproject.org> - 2.3.1-1.20170619git5cb665d
- Update to recent git 2.3.1-1.20170619git5cb665d

* Tue Feb 14 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-25.20150213git6ea279a
- added %%{name}-libpages-build.patch

* Sat Feb 06 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-24.20150213git6ea279a
- added %%{name}-gcc6.patch

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-23.20150213git6ea279a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-22.20150213git6ea279a
- Rebuilt

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-21.20150213git6ea279a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.0-20.20150213git6ea279a
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.3.0-19.20150213git6ea279a
- Rebuild

* Sat Feb 14 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-18.20150213git6ea279a
- rebuild for new git version

* Thu Feb 12 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-17.20150211git894daa8
- rebuild for new git version
- added Fedora %%optflags for CFLAGS and CXXFLAGS
- cleanup spec file
- mark license files as %%license where available

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-16.20130504git69f84f9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-15.20130504git69f84f9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.3.0-14.20130504git69f84f9
- Rebuild

* Sat Mar 22 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.3.0-13.20130504git69f84f9
- Rebuild

* Thu Feb 06 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-12.20130504git69f84f9
- rebuild against tntnet-2.2.1

* Tue Jan 21 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-11.20130504git69f84f9
- changed to %%{buildroot} macro
- rebuild against tntnet-2.2.1

* Fri Jan 17 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-10.20130504git69f84f9
- added vdr-live-data as requirement
- added gitdate
- added tarball download instructions

* Tue Jan 07 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-9.69f84f9
- rebuild
- changed global spec file declarations

* Sat Jan 04 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-8.20130504git69f84f9
- rebuild
- spec file cleanup

* Fri Jan 03 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-7.69f84f9
- add correct source file

* Sun Dec 29 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-6.69f84f9
- Capitalized first letter
- Fixed spelling

* Sun Dec 29 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-5.69f84f9
- unmark files in sub-package as %%config

* Sun Dec 29 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-4.69f84f9
- added live directory to noarch sub-package 

* Fri Dec 27 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-3.69f84f9
- change release tag
- change license tag

* Sat Dec 21 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-2.20130504git
- rebuild for new git version
- remove bundled tntnet libraries

* Sat May 4 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-1.20130504git
- rebuild for new git version

* Wed Apr 24 2013 Martin Gansser <linux4martin@gmx.de> - 0.3.0-1.20130412git
- rebuild for new git version
- spec file cleanup

* Fri Nov 2 2012 Martin Gansser <linux4martin@gmx.de> - 0.2.0-8.20121009git
- listed BuildRequirements one per line.

* Tue Oct 9 2012 Martin Gansser <linux4martin@gmx.de> - 0.2.0-7.20121009git
- added vdr-1.7.28 compile fix
- added API patch version >= 1.7.30
- rebuild for Fedora 18.

* Mon Aug 6 2012 Martin Gansser <linux4martin@gmx.de> - 0.2.0-6.20120325git
- added live.conf file

* Mon Aug 6 2012 Martin Gansser <linux4martin@gmx.de> - 0.2.0-5.20120325git
- removed Buildroot

* Mon May 14 2012 Martin Gansser <linux4martin@gmx.de> - 0.2.0-4.20120325git
- new release
- more cleanups

* Sun Apr 29 2012 Martin Gansser <linux4martin@gmx.de> - 0.2.0-3.20120218git
- first build for Fedora 17
- fixed vdr macro names
- fixed README file utf encoding

* Mon Sep 19 2011 Sebastian Vahl <fedora@deadbabylon.de> - 0.2.0-2.20110917git
- fix some rpmlint issues and cleanup spec

* Sat Sep 17 2011 Sebastian Vahl <fedora@deadbabylon.de> - 0.2.0-1.20110917git
- initial release
