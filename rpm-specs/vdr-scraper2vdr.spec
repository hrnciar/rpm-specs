# https://github.com/horchi/scraper2vdr/commit/d9f6cb454ebbc951af5d1a4aa7fcc31e772f3bca
%global commit0 d9f6cb454ebbc951af5d1a4aa7fcc31e772f3bca
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global pname   scraper2vdr
%global gitdate 20190128

Name:           vdr-scraper2vdr
Version:        1.0.11
Release:        5.%{gitdate}git%{shortcommit0}%{?dist}
Summary:        A client plugin which provides scraped metadata from EPGD to other plugins
License:        GPL+
URL:            https://github.com/horchi/scraper2vdr
Source0:        https://github.com/horchi/scraper2vdr/archive/%{commit0}/%{name}-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1:        %{name}.conf

BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
BuildRequires:  ImageMagick-c++-devel
BuildRequires:  openssl-devel
%if 0%{?fedora} <= 27
BuildRequires:  mariadb-devel
%else
BuildRequires:  mariadb-connector-c-devel
%endif
BuildRequires:  libcurl-devel
BuildRequires:  imlib2-devel
BuildRequires:  vdr-devel >= 1.7.34
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description 
Scraper2vdr acts as client and provides scraped metadata for tvshows and
movies from epgd to other plugins via its service interface. The plugin 
cares about caching the images locally and also cleans up the images if
not longer needed. 

epgd itself uses the thetvdb.com API for collecting series metadata and
themoviedb.org API for movies. Check the websites of both services for
the terms of use.

%prep
%setup -qn %{pname}-%{commit0}
iconv -f iso-8859-1 -t utf-8 README > README.utf8 ; mv README.utf8 README

# fedora specific
sed -i -e 's|#include <errmsg.h>|#include <mysql/errmsg.h>|' lib/db.c

%build
make CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" %{?_smp_mflags} all

%install
%make_install
# fix the perm
chmod 0755 %{buildroot}/%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/scraper2vdr.conf

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING HISTORY* README*
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/scraper2vdr.conf
%config(noreplace) %{vdr_configdir}/plugins/%{pname}/epg.dat

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-5.20190128gitd9f6cb4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-4.20190128gitd9f6cb4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.11-3.20190128gitd9f6cb4
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2.20190128gitd9f6cb4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.11-1.20190128gitd9f6cb4
- Update to 1.0.11-1.20190128gitd9f6cb4

* Wed Jan 16 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.10-1.20190108gita412d52
- Update to 1.0.10-1.20190108gita412d52

* Tue Aug 28 2018 Michael Cronenworth <mike@cchtml.com> - 1.0.9-5.20180104gitef448e1
- Rebuild for ImageMagick 6.9.10

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4.20180104gitef448e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.9-3.20180104gitef448e1
- Rebuilt for vdr-2.4.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2.20180104gitef448e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.9-1.20180104gitef448e1
- Update to 1.0.9-1.20180104gitef448e1

* Thu Dec 28 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.0.8-1.20171225git194b3be
- Update to 1.0.8-1.20171225git194b3be

* Sat Dec 23 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.0.7-1.20171221gitf06286f
- Update to 1.0.7-1.20171221gitf06286f

* Thu Sep 21 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.0.5-9.20170611git254122b
- Use mariadb-connector-c-devel instead of mariadb-devel only for f28,
  fixes (BZ#1493698).
- Add BR openssl-devel

* Wed Sep 06 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.0.5-8.20170611git254122b
- Rebuild for new ImageMagick 7 reversion

* Tue Sep 05 2017 Adam Williamson <awilliam@redhat.com> - 1.0.5-7.20170611git254122b
- Rebuild for ImageMagick 6 reversion

* Sat Aug 26 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.0.5-6.20170611git254122b
- Rebuild for new ImageMagick

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5.20170611git254122b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Kevin Fenzi <kevin@scrye.com> - 1.0.5-4.20170611git254122b
- Rebuild for new ImageMagick

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3.20170611git254122b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.0.5-2.20170611git254122b
- Add %%{name}-mariadb-fix-build.patch fixes (BZ#1298509).

* Mon Jun 12 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.0.5-1.20170611git254122b
- Update to 1.0.5-1.20170611git254122b

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2.20161205gitc01f745
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.3-1.20161206gitc01f745
- Update to 1.0.3-1.20161206gitc01f745

* Thu Oct 06 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.2-1.20161006git23bf9a9
- Update to 1.0.2-1.20161006git23bf9a9

* Fri Aug 26 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.1-1.20160826gite441ec8
- Bump up version to 1.0.1-1.20160826gite441ec8

* Fri Aug 26 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-2.20160826gite441ec8
- Update to 1.0.0-2.20160826gite441ec8

* Thu Jul 07 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-1.20160704git57e3668
- Update to 1.0.0

* Sat May 21 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.1.25-1.20160520gitff95c71
- Update to 0.1.25

* Tue May 10 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.1.23-1.20160510git2899b3f
- Update to 0.1.23

* Sun Mar 27 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.1.20-1.20160226git80528db
- Update to 0.1.20

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2.20141117git02013ac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 21 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.6-1.20141117git02013ac
- Update to 0.1.6

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.5-4
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar 06 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.5-3
- Rebuild for new libMagick++-6.Q16.so.6

* Thu Feb 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.1.5-2
- Rebuild

* Sat Oct 25 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Sun Sep 28 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4
- added perl command to find errmsg.h header file

* Thu May 15 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.3-2.20140515git2bfb7c7
- rebuild for new git release

* Wed May 14 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3

* Sun May 11 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.2-3.20140511git7231362
- rebuild for new git release

* Sun May 11 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.2-2.20140510gitea862b3
- added patch to build parallel again

* Sat May 10 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.2-1.20140510gitea862b3
- rebuild for new git release
- added Fedora %%optflags for CFLAGS and CXXFLAGS
- Add BR libcurl-devel
- Add BR imlib2-devel

* Fri May 09 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Sat May 03 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.1-6.20140428git30008b3
- fixed description
- replaced RPM_BUILD_ROOT macro through %%{buildroot}

* Fri May 02 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.1-5.20140428git30008b3
- Fix patch path
- Fix bogus date in %%changelog
- Fix comments

* Thu May 01 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.1-4.20140428git30008b3
- added permission fix to solve unstripped-binary-or-object warning

* Mon Apr 28 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.1-3.20140428git30008b3
- rebuild for new git release 

* Mon Apr 28 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-2.20140427gitc538d35
- added conf file

* Sun Apr 27 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-1.20140427gitc538d35
- rebuild for initial release
