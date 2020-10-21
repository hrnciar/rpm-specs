# FIXME: Tests disabled: https://github.com/TelepathyIM/telepathy-idle/issues/7
%if 0%{?rhel}
%global run_tests 0
%else
%global run_tests 0
%endif

Name:           telepathy-idle
Version:        0.2.0
Release:        20%{?dist}
Summary:        IRC connection manager for Telepathy

License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	telepathy-glib-devel >= 0.21.0
BuildRequires:	libxslt
BuildRequires:	python3
BuildRequires:	git
%if %{run_tests}
# Build Requires needed for tests.
BuildRequires:	python2
BuildRequires:	python2-dbus
BuildRequires:	pygobject2
%endif

Requires:	telepathy-filesystem

# https://github.com/TelepathyIM/telepathy-idle/pull/8
Patch0: 0001-tools-Fix-errors-running-glib-ginterface-gen-under-P.patch
Patch1: 0002-tools-Remove-outdated-is-unicode-checks.patch
# https://gitlab.freedesktop.org/telepathy/telepathy-idle/-/merge_requests/3
Patch2: properly-handle-long-irc-messages.patch
# https://gitlab.freedesktop.org/telepathy/telepathy-idle/-/merge_requests/2
Patch3: fix-critical.patch

%description
A full-featured IRC connection manager for the Telepathy project.


%prep
%autosetup -S git


%if %{run_tests}
%check
#make check
%endif


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc AUTHORS COPYING NEWS
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{_mandir}/man8/%{name}.8*


%changelog
* Tue Oct 13 2020 Kalev Lember <klember@redhat.com> - 0.2.0-20
- Backport mcatanzaro patch to fix criticals when removing idle sources

* Fri Oct 09 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.0-20
- Correct upstream URL

* Fri Oct 09 2020 Kalev Lember <klember@redhat.com> - 0.2.0-19
- Backport mcatanzaro patch to correctly handle long IRC messages

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 17 2020 Bastien Nocera <bnocera@redhat.com> - 0.2.0-16
+ telepathy-idle-0.2.0-16
- Disable all tests for now, as they require Python 2
- Port code generation tools to Python3

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Jan Beran <jaberan@redhat.com> - 0.2.0-14
- Avoid using compression format when listing manpages

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.0-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct  3 2013 Brian Pepple <bpepple@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0.

* Wed Sep 18 2013 Brian Pepple <bpepple@fedoraproject.org> - 0.1.17-1
- Update to 0.1.17.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May  1 2013 Brian Pepple <bpepple@fedoraproject.org> - 0.1.16-1
- Update to 0.1.16.

* Wed Apr 24 2013 Brian Pepple <bpepple@fedoraproject.org> - 0.1.15-1
- Update to 0.1.15.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.1.14-1
- Update to 0.1.14.

* Wed Nov 14 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.1.13-1
- Update to 0.1.13.
- Drop make-j patch. Fixed upstream.

* Tue Oct  2 2012 Dan Winship <danw@redhat.com> - 0.1.12-2
- Add a patch from upstream for "make -j" reliability

* Fri Aug  3 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.1.12-1
- Update to 0.1.12.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-3
- Make tests conditional. (#831344)

* Mon Jan 09 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-2
- Rebuild for new gcc.

* Sun Oct 30 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-1
- Update to 0.1.11.

* Wed May 11 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.1.10-1
- Update to 0.1.10.

* Mon Apr 11 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9.

* Fri Feb 11 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.1.8-1
- Update to 0.1.8.
- Bump min version of tp-glib needed.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec  7 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.1.7-2
- Bump.

* Tue Dec  7 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7.
- Bump min version of tp-glib needed.
- Add BR on python-twisted, dbus-python, and pygobject2 for tests.
- Drop buildroot & clean section. No longer needed.

* Fri Feb 19 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.1.6-1
- Update to 0.1.6.

* Mon Sep 14 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5.
- Drop glibc patch.  Fixed upstream.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.1.4-3
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 27 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4.
- Add patch to fix glibc compilation bug.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3.
- Bump minimum version of tp-glib-devel needed.

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 0.1.2-4
- rebuild with new openssl

* Fri Feb  8 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.1.2-3
- Rebuild for gcc-4.3.

* Wed Dec  5 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.2-2
- rebuild for new libssl.so.6/libcrypto.so.6

* Sat Nov 24 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2.
- Add BR for telepathy-glib-devel, libxslt, & python.

* Tue Aug 21 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.1-3
- Rebuild.

* Sun Aug  5 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.1-2
- Update license tag.

* Tue Jun 19 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1.
- Add check section for tests.
- Add BR on telepathy-glib-unstable-static.

* Mon Apr 16 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.0.5-1
- Initial spec file.

