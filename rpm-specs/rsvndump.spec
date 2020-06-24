Name:           rsvndump
Version:        0.6
Release:        16%{?dist}
Summary:        Remote Subversion repository dumping tool

License:        GPLv3+
URL:            http://rsvndump.sourceforge.net
Source0:        http://downloads.sourceforge.net/rsvndump/rsvndump-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  asciidoc
BuildRequires:  gettext
BuildRequires:  subversion-devel
BuildRequires:  xmlto

%description
rsvndump is a command line tool that is able to dump a subversion repository
that resides on a remote server. All data is dumped in the format that can be
read/written by svnadmin, so the data produced by rsvndump can easily be
imported into a new subversion repository.

%prep
%setup -q

%build
%configure --enable-man
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING THANKS
%{_bindir}/rsvndump
%{_mandir}/man1/rsvndump.1*

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Kalev Lember <kalevlember@gmail.com> - 0.6-1
- Update to 0.6

* Tue Mar 13 2012 Kalev Lember <kalevlember@gmail.com> - 0.5.8-1
- Update to 0.5.8

* Fri Jan 27 2012 Kalev Lember <kalevlember@gmail.com> - 0.5.7-1
- Update to 0.5.7 (#755525)
- Dropped the RPM_OPT_FLAGS workaround; the configure script now
  properly honours CFLAGS

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 Kalev Lember <kalevlember@gmail.com> - 0.5.6-2
- Use RPM_OPT_FLAGS, fixes regression in 0.5.6 (#722792)

* Sat Jul 16 2011 Kalev Lember <kalevlember@gmail.com> - 0.5.6-1
- Update to 0.5.6
- Removed %%check section as the package no longer ships unit tests
- Cleaned up the spec file for modern rpmbuild

* Sat Mar 05 2011 Kalev Lember <kalev@smartlink.ee> - 0.5.5-1
- Update to 0.5.5

* Tue Feb 15 2011 Kalev Lember <kalev@smartlink.ee> - 0.5.4-1
- Update to 0.5.4

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Mar 19 2010 Kalev Lember <kalev@smartlink.ee> - 0.5.3-1
- Initial RPM release
