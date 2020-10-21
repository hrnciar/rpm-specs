Name:          ifuse
Version:       1.1.4
Release:       2%{?dist}
Summary:       Mount Apple iPhone and iPod touch devices
License:       GPLv2+
URL:           http://www.libimobiledevice.org/
Source0:       https://github.com/libimobiledevice/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: gcc
BuildRequires: fuse-devel
BuildRequires: libimobiledevice-devel
BuildRequires: libplist-devel
Requires: fuse

%description
A fuse filesystem for mounting iPhone and iPod touch devices

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/ifuse
%{_mandir}/man1/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Bastien Nocera <bnocera@redhat.com> - 1.1.4-1
+ ifuse-1.1.4-1
- Update to 1.1.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar  7 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.3-13
- Add gcc BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.3-6
- Rebuild (libimobiledevice)
- Use %%license

* Wed Oct 15 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.3-5
- Rebuild for libimobiledevice 1.1.7

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May  5 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.3-2
- Rebuild for libimobiledevice 1.1.6

* Sun Mar 2  2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.3-1
- New upstream 1.1.3 release

* Tue Oct 8  2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.2-7
- Run autoreconf so patch actually takes effect

* Thu Sep 19 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.2-6
- Add patch to work with newer libimobiledevice (980949)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.2-4
- Rebuild for new libimobiledevice

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.2-1
- New upstream 1.1.2 release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Peter Robinson <pbrobinson@gmail.com> 1.1.1-1
- New upstream 1.1.1 release

* Wed Jan 12 2011 Peter Robinson <pbrobinson@gmail.com> 1.1.0-1
- New upstream 1.1.0 release

* Tue Dec 28 2010 Peter Robinson <pbrobinson@gmail.com> 1.0.0-3
- Rebuild for new libimobiledevice and drop hal requirement

* Wed Nov 17 2010 Peter Robinson <pbrobinson@gmail.com> 1.0.0-2
- Update URLs and spec

* Sun Mar 21 2010 Peter Robinson <pbrobinson@gmail.com> 1.0.0-1
- New upstream stable 1.0.0 release

* Thu Feb  4 2010 Peter Robinson <pbrobinson@gmail.com> 0.9.7-1
- Update to 0.9.7 release, compile against renamed libimobiledevice

* Sun Jan 24 2010 Peter Robinson <pbrobinson@gmail.com> 0.9.6-1
- Update to 0.9.6 release

* Sat Dec 12 2009 Peter Robinson <pbrobinson@gmail.com> 0.9.5-1
- Update to 0.9.5 release for new usbmuxd/libplist 1.0.0 final

* Sat Dec 12 2009 Peter Robinson <pbrobinson@gmail.com> 0.9.4-3
- Rebuild for libplist .so bump

* Wed Oct 28 2009 Peter Robinson <pbrobinson@gmail.com> 0.9.4-2
- Fix included files

* Wed Oct 28 2009 Peter Robinson <pbrobinson@gmail.com> 0.9.4-1
- Update to 0.9.4 release for new usbmuxd 1.0.0-rc1

* Thu Sep 17 2009 Peter Lemenkov <lemenkov@gmail.com> 0.9.3-2
- Rebuilt with new fuse

* Mon Aug 10 2009 Peter Robinson <pbrobinson@gmail.com> 0.9.3-1
- Update to 0.9.3 release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 12 2009 Peter Robinson <pbrobinson@gmail.com> 0.9.1-1
- Update to official 0.9.1 release

* Fri Apr 03 2009 - Bastien Nocera <bnocera@redhat.com> - 0.1.0-8.20090401git5db1ccc
- Update to github version

* Fri Apr 03 2009 - Bastien Nocera <bnocera@redhat.com> - 0.1.0-7.20090308git8d6eebb
- Update to latest master

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-6.20081214gitb0412bf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 16 2008 Peter Robinson <pbrobinson@gmail.com> 0.1.0-5
- Review fixes

* Sun Dec 14 2008 Peter Robinson <pbrobinson@gmail.com> 0.1.0-4
- Actually depend on libiphone. Latest git

* Tue Dec 2 2008 Peter Robinson <pbrobinson@gmail.com> 0.1.0-3
- Fix git file generation

* Mon Dec 1 2008 Peter Robinson <pbrobinson@gmail.com> 0.1.0-2
- Update package to code snapshot package policies

* Sat Nov 29 2008 Peter Robinson <pbrobinson@gmail.com> 0.1.0-1
- Initial package
