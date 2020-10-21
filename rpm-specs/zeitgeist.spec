Name:           zeitgeist
Version:        1.0.3
Release:        1%{?dist}
Summary:        Framework providing Desktop activity awareness
# most of the source code is LGPLv2+, except:
# datahub/ is LGPLv3+
# examples/c/ is GPLv3
# extensions/fts++/ is GPLv2+
# src/notify.vala: GPLv2+
# test/c/ is GPLv3
# tools/zeitgeist-explorer/ is GPLv2+
License:        LGPLv2+ and LGPLv3+ and GPLv2+

URL:            https://launchpad.net/zeitgeist
Source0:        %{url}/1.0/%{version}/+download/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  python3-rdflib
BuildRequires:  systemd
BuildRequires:  vala
BuildRequires:  xapian-core-devel

BuildRequires:  pkgconfig(dee-icu-1.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(telepathy-glib)

%{?systemd_requires}

Requires:       dbus
Obsoletes:      zeitgeist-datahub < 0.9.5-4
Obsoletes:      python2-%{name} < 1.0.2-1

%description
Zeitgeist is a service which logs the users's activities and events (files
opened, websites visites, conversations hold with other people, etc.) and
makes relevant information available to other applications.
Note that this package only contains the daemon, which you can use
together with several different user interfaces.

%package        libs
Summary:        Client library for interacting with the Zeitgeist daemon
License:        LGPLv2+

%description    libs
Libzeitgeist is a client library for interacting with the Zeitgeist
daemon.

%package        devel
Summary:        Development files for %{name}
License:        LGPLv2+
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1

## nuke unwanted rpaths, see also
## https://fedoraproject.org/wiki/Packaging/Guidelines#Beware_of_Rpath
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure

%build
%configure --enable-fts --enable-datahub --disable-silent-rules
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete -print

# Remove unused Python bindings.
rm -rf %{buildroot}%{python3_sitelib}

# We install AUTHORS and NEWS with %%doc instead
rm -frv %{buildroot}%{_datadir}/zeitgeist/doc

%check
make check || true

%post
%systemd_user_post %{name}.service
%systemd_user_post %{name}-fts.service

%preun
%systemd_user_preun %{name}.service
%systemd_user_preun %{name}-fts.service

%ldconfig_scriptlets libs


%files
%doc AUTHORS NEWS
%license COPYING COPYING.GPL
%{_bindir}/zeitgeist-daemon
%{_bindir}/zeitgeist-datahub
%{_libexecdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/dbus-1/services/org.gnome.zeitgeist*.service
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/zeitgeist-daemon
%{_mandir}/man1/zeitgeist-*.*
%config(noreplace) %{_sysconfdir}/xdg/autostart/zeitgeist-datahub.desktop
%{_userunitdir}/%{name}.service
%{_userunitdir}/%{name}-fts.service

%files libs
%license COPYING
%{_libdir}/girepository-1.0/Zeitgeist-2.0.typelib
%{_libdir}/libzeitgeist-2.0.so.*

%files devel
%{_includedir}/zeitgeist-2.0/
%{_libdir}/libzeitgeist-2.0.so
%{_libdir}/pkgconfig/zeitgeist-2.0.pc
%{_datadir}/gir-1.0/Zeitgeist-2.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/zeitgeist-2.0.deps
%{_datadir}/vala/vapi/zeitgeist-2.0.vapi
%{_datadir}/vala/vapi/zeitgeist-datamodel-2.0.vapi

%changelog
* Thu Oct 15 2020 David King <amigadave@amigadave.com> - 1.0.3-1
- Update to 1.0.3 (#1888547)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.2-1
- Update to version 1.0.2.
- Drop unused python bindings.
- Drop unnecessary patches.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 David King <amigadave@amigadave.com> - 1.0.1-1
- Update to 1.0.1
- Fix VAPI file for recent Vala (#1668410)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 10 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 David King <amigadave@amigadave.com> - 1.0-5
- Fix service file variable substitution (#1464693)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Feb 21 2017 David King <amigadave@amigadave.com> - 1.0-1
- Update to 1.0
- Use pkgconfig for BuildRequires
- Use python_provide macro

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 26 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.16-4
- Rebuild (xapian 1.4)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 07 2015 Christopher Meng <rpm@cicku.me> - 0.9.16-1
- Update to 0.9.16

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16-0.5.20140808.git.ce9affa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.16-0.4.20140808.git.ce9affa
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16-0.3.20140808.git.ce9affa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Christopher Meng <rpm@cicku.me> - 0.9.16-0.2.20140808.git.ce9affa
- Introduce python-zeitgeist subpkg
- Mark xdg autostart file as noreplace for better UX, Fix BZ#863222

* Fri Aug 08 2014 Christopher Meng <rpm@cicku.me> - 0.9.16-0.1.20140808.git.ce9affa
- Update to 0.9.16 snapshot
- Fix BZ#1126461

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.9.14-4
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul  9 2013 Brian Pepple <bpepple@fedoraproject.org> - 0.9.14-1
- Update to 0.9.14.

* Sun Jun 16 2013 Kalev Lember <kalevlember@gmail.com> - 0.9.13-2
- Fix postun script syntax error

* Fri Jun 14 2013 Deji Akingunola <dakingun@gmail.com> - 0.9.13-1
- Update to 0.9.13

* Sun Apr 14 2013 Kalev Lember <kalevlember@gmail.com> - 0.9.12-1
- Update to 0.9.12 (#949286)
- Obsolete zeitgeist-datahub
- Package up the libzeitgeist-2.0 library
- Update the license tag and add a spec file comment with longer explanations

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 23 2012 Deji Akingunola <dakingun@gmail.com> - 0.9.5-1
- Update to 0.9.5

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Deji Akingunola <dakingun@gmail.com> - 0.9.0-1
- Update to 0.9.0
- Apply upstream patch to fix a crasher bug.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 22 2011 Deji Akingunola <dakingun@gmail.com> - 0.8.2-2
- Revert post-install script to restart zeitgeist daemon on update

* Tue Oct 18 2011 Deji Akingunola <dakingun@gmail.com> - 0.8.2-1
- Update to 0.8.2
- Restart the zeitgeist daemon on update (BZ #627982)

* Wed Jul 20 2011 Deji Akingunola <dakingun@gmail.com> - 0.8.1-1
- Update to 0.8.1

* Fri May 13 2011 Deji Akingunola <dakingun@gmail.com> - 0.8.0-1
- Update to 0.8.0
- Add a hard requires on zeitgeist-datahub

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 Deji Akingunola <dakingun@gmail.com> - 0.7-1
- Update to 0.7

* Fri Aug 06 2010 Deji Akingunola <dakingun@gmail.com> - 0.5.0-1
- Update to 0.5.0

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 15 2010 Deji Akingunola <dakingun@gmail.com> - 0.4.0-1
- Update to 0.4.0

* Wed Apr 21 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.3.1-1
- Update to 0.3.3.1 to fix datasource_registry bug (BZ #586238)

* Wed Apr 21 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.3-1
- Update to 0.3.3

* Wed Jan 20 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.2-1
- Update to 0.3.2

* Thu Jan 14 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.1-1
- Add missing requires (Package reviews)
- Update license tag (Package reviews)
- Update to latest release

* Tue Dec 01 2009 Deji Akingunola <dakingun@gmail.com> - 0.3.0-1
- Update to 0.3.0

* Wed Nov 04 2009 Deji Akingunola <dakingun@gmail.com> - 0.2.1-1
- Initial Fedora packaging
