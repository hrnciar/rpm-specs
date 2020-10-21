Name:           clamz
Version:        0.5
Release:        19%{?dist}
Summary:        Amazon Downloader
License:        GPLv3+
URL:            http://clamz.googlecode.com/
Source0:        http://clamz.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  libcurl-devel, libgcrypt-devel, expat-devel

%description
Clamz is a little command-line program to download MP3 files from
Amazon.com's music store.  It is intended to serve as a substitute
for Amazon's official MP3 Downloader, which is not free software (and
therefore is only available in binary form for a limited set of
platforms.)  Clamz can be used to download either individual songs or
complete albums that you have purchased from Amazon.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} UPDATE_MIME_DATABASE=: UPDATE_DESKTOP_DATABASE=:

%files
%doc README COPYING
%{_bindir}/%{name}
%{_mandir}/*/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 0.5-8
- update mime scriptlet

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Tomáš Mráz <tmraz@redhat.com> - 0.5-5
- Rebuild for new libgcrypt

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 30 2011 Jim Radford <radford@blackbean.org> - 0.5-0
- Upgrade to 0.5 for support for the Amazon Cloud Player

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat May 22 2010 Jim Radford <radford@blackbean.org> - 0.4-3
- Remove obsolete build dependency on desktop-file-install
- Re-remove dependency on shared-mime-info as per
  https://fedoraproject.org/wiki/Packaging/ScriptletSnippets#mimeinfo

* Fri May 21 2010 Jim Radford <radford@blackbean.org> - 0.4-2
- Require shared-mime-info for update-mime-database and packages dir

* Tue May 18 2010 Jim Radford <radford@blackbean.org> - 0.4-1
- Upgrade to 0.4 (4 patches, desktop and mime-info file included upstream)

* Wed Sep 16 2009 Jim Radford <radford@blackbean.org> - 0.2-10
- Fixed desktop dependencies again (#473184)

* Fri Jul 17 2009 Jim Radford <radford@blackbean.org> - 0.2-9
- Add --sane-defaults for use by the .desktop file to default downloads into
      ~/Music/<artist>/<album>/<track> - <title>.<suffix>
  while still allowing previous config file and command line usage.

* Sat Apr 18 2009 Jim Radford <radford@blackbean.org> - 0.2-8
- fedora guidelines now explicitly allow including desktop files
  inline in the spec, so put them back.

* Sat Apr 18 2009 Jim Radford <radford@blackbean.org> - 0.2-7
- Fixed desktop dependencies (#473184).

* Wed Nov 26 2008 Jim Radford <radford@blackbean.org> 0.2-6
- Initial package (#473184).
