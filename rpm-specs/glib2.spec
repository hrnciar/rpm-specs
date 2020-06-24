Name: glib2
Version: 2.65.0
Release: 2%{?dist}
Summary: A library of handy utility functions

License: LGPLv2+
URL: http://www.gtk.org
Source0: http://download.gnome.org/sources/glib/2.65/glib-%{version}.tar.xz

# Avoid requiring a too new gtk-doc version for building glib
Patch0: gtk-doc-1-32.patch

BuildRequires: chrpath
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gtk-doc
BuildRequires: perl-interpreter
# for sys/inotify.h
BuildRequires: glibc-devel
BuildRequires: libattr-devel
BuildRequires: libselinux-devel
BuildRequires: meson
# for sys/sdt.h
BuildRequires: systemtap-sdt-devel
BuildRequires: pkgconfig(libelf)
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(libpcre)
BuildRequires: pkgconfig(mount)
BuildRequires: pkgconfig(zlib)
BuildRequires: python3-devel

# for GIO content-type support
Recommends: shared-mime-info

# glib 2.59.0 hash table changes broke older gcr versions / password prompts in gnome-shell
Conflicts: gcr < 3.28.1

%description
GLib is the low-level core library that forms the basis for projects
such as GTK+ and GNOME. It provides data structure handling for C,
portability wrappers, and interfaces for such runtime functionality
as an event loop, threads, dynamic loading, and an object system.


%package devel
Summary: A library of handy utility functions
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The glib2-devel package includes the header files for the GLib library.

%package doc
Summary: A library of handy utility functions
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
The glib2-doc package includes documentation for the GLib library.

%package fam
Summary: FAM monitoring module for GIO
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: gamin-devel

%description fam
The glib2-fam package contains the FAM (File Alteration Monitor) module for GIO.

%package static
Summary: glib static
Requires: %{name}-devel = %{version}-%{release}

%description static
The %{name}-static subpackage contains static libraries for %{name}.

%package tests
Summary: Tests for the glib2 package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The glib2-tests package contains tests that can be used to verify
the functionality of the installed glib2 package.

%prep
%autosetup -n glib-%{version} -p1

%build
# Bug 1324770: Also explicitly remove PCRE sources since we use --with-pcre=system
rm glib/pcre/*.[ch]
%meson \
    --default-library=both \
    -Dman=true \
    -Ddtrace=true \
    -Dsystemtap=true \
    -Dgtk_doc=true \
    -Dfam=true \
    -Dinstalled_tests=true

%meson_build

%install
%meson_install
# Since this is a generated .py file, set it to a known timestamp for
# better reproducibility.
# Also copy the timestamp for other .py files, because meson doesn't
# do this, see https://github.com/mesonbuild/meson/issues/5027.
touch -r gio/gdbus-2.0/codegen/config.py.in %{buildroot}%{_datadir}/glib-2.0/codegen/*.py
chrpath --delete %{buildroot}%{_libdir}/*.so

# Perform byte compilation manually to avoid issues with
# irreproducibility of the default invalidation mode, see
# https://www.python.org/dev/peps/pep-0552/ and
# https://bugzilla.redhat.com/show_bug.cgi?id=1686078
export PYTHONHASHSEED=0
%py_byte_compile %{__python3} %{buildroot}%{_datadir}

mv %{buildroot}%{_bindir}/gio-querymodules %{buildroot}%{_bindir}/gio-querymodules-%{__isa_bits}
sed -i -e "/^gio_querymodules=/s/gio-querymodules/gio-querymodules-%{__isa_bits}/" %{buildroot}%{_libdir}/pkgconfig/gio-2.0.pc

touch %{buildroot}%{_libdir}/gio/modules/giomodule.cache

%find_lang glib20

%transfiletriggerin -- %{_libdir}/gio/modules
gio-querymodules-%{__isa_bits} %{_libdir}/gio/modules &> /dev/null || :

%transfiletriggerpostun -- %{_libdir}/gio/modules
gio-querymodules-%{__isa_bits} %{_libdir}/gio/modules &> /dev/null || :

%transfiletriggerin -- %{_datadir}/glib-2.0/schemas
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%transfiletriggerpostun -- %{_datadir}/glib-2.0/schemas
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f glib20.lang
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/libglib-2.0.so.*
%{_libdir}/libgthread-2.0.so.*
%{_libdir}/libgmodule-2.0.so.*
%{_libdir}/libgobject-2.0.so.*
%{_libdir}/libgio-2.0.so.*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/gapplication
%{_datadir}/bash-completion/completions/gdbus
%{_datadir}/bash-completion/completions/gio
%{_datadir}/bash-completion/completions/gsettings
%dir %{_datadir}/glib-2.0
%dir %{_datadir}/glib-2.0/schemas
%dir %{_libdir}/gio
%dir %{_libdir}/gio/modules
%ghost %{_libdir}/gio/modules/giomodule.cache
%{_bindir}/gio
%{_bindir}/gio-querymodules*
%{_bindir}/glib-compile-schemas
%{_bindir}/gsettings
%{_bindir}/gdbus
%{_bindir}/gapplication
%{_mandir}/man1/gio.1*
%{_mandir}/man1/gio-querymodules.1*
%{_mandir}/man1/glib-compile-schemas.1*
%{_mandir}/man1/gsettings.1*
%{_mandir}/man1/gdbus.1*
%{_mandir}/man1/gapplication.1*

%files devel
%{_libdir}/lib*.so
%{_libdir}/glib-2.0
%{_includedir}/*
%{_datadir}/aclocal/*
%{_libdir}/pkgconfig/*
%{_datadir}/glib-2.0/gdb
%{_datadir}/glib-2.0/gettext
%{_datadir}/glib-2.0/schemas/gschema.dtd
%{_datadir}/glib-2.0/valgrind/glib.supp
%{_datadir}/bash-completion/completions/gresource
%{_bindir}/glib-genmarshal
%{_bindir}/glib-gettextize
%{_bindir}/glib-mkenums
%{_bindir}/gobject-query
%{_bindir}/gtester
%{_bindir}/gdbus-codegen
%{_bindir}/glib-compile-resources
%{_bindir}/gresource
%{_datadir}/glib-2.0/codegen
%attr (0755, root, root) %{_bindir}/gtester-report
%{_mandir}/man1/glib-genmarshal.1*
%{_mandir}/man1/glib-gettextize.1*
%{_mandir}/man1/glib-mkenums.1*
%{_mandir}/man1/gobject-query.1*
%{_mandir}/man1/gtester-report.1*
%{_mandir}/man1/gtester.1*
%{_mandir}/man1/gdbus-codegen.1*
%{_mandir}/man1/glib-compile-resources.1*
%{_mandir}/man1/gresource.1*
%{_datadir}/gdb/
%{_datadir}/gettext/
%{_datadir}/systemtap/

%files doc
%doc %{_datadir}/gtk-doc/html/*

%files fam
%{_libdir}/gio/modules/libgiofam.so

%files static
%{_libdir}/libgio-2.0.a
%{_libdir}/libglib-2.0.a
%{_libdir}/libgmodule-2.0.a
%{_libdir}/libgobject-2.0.a
%{_libdir}/libgthread-2.0.a

%files tests
%{_libexecdir}/installed-tests
%{_datadir}/installed-tests

%changelog
* Mon Jun 22 2020 Kalev Lember <klember@redhat.com> - 2.65.0-2
- Update gio-2.0.pc with correct gio-querymodules name when renaming it
  (#1849441)

* Mon Jun 22 2020 Kalev Lember <klember@redhat.com> - 2.65.0-1
- Update to 2.65.0

* Wed May 20 2020 Kalev Lember <klember@redhat.com> - 2.64.3-1
- Update to 2.64.3

* Tue Apr 28 2020 Tomas Popela <tpopela@redhat.com> - 2.64.2-2
- Backport fix for a race condition in GCancellable (rhbz#1825230)

* Fri Apr 10 2020 Kalev Lember <klember@redhat.com> - 2.64.2-1
- Update to 2.64.2

* Wed Mar 11 2020 Kalev Lember <klember@redhat.com> - 2.64.1-1
- Update to 2.64.1

* Mon Mar 02 2020 Kalev Lember <klember@redhat.com> - 2.64.0-1
- Update to 2.64.0

* Mon Feb 24 2020 Kalev Lember <klember@redhat.com> - 2.63.6-1
- Update to 2.63.6

* Wed Feb 12 2020 Kalev Lember <klember@redhat.com> - 2.63.5-3
- Backport a patch to work around SELinux policies not allowing
  SYS_sched_setattr (#1795524)

* Fri Feb 07 2020 Michael Catanzaro <mcatanzaro@redhat.com> - 2.63.5-2
- Add patch for CVE-2020-6750 and related issues.

* Mon Feb 03 2020 Kalev Lember <klember@redhat.com> - 2.63.5-1
- Update to 2.63.5

* Wed Jan 29 2020 Stephen Gallagher <sgallagh@redhat.com> - 2.63.4-3
- Fix GThreadPool initialization that is breaking createrepo_c (BZ #1795052)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.63.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Kalev Lember <klember@redhat.com> - 2.63.4-1
- Update to 2.63.4

* Mon Dec 16 2019 Kalev Lember <klember@redhat.com> - 2.63.3-1
- Update to 2.63.3

* Mon Dec 02 2019 Kalev Lember <klember@redhat.com> - 2.63.2-1
- Update to 2.63.2

* Fri Oct 04 2019 Kalev Lember <klember@redhat.com> - 2.63.0-1
- Update to 2.63.0

* Fri Oct 04 2019 Kalev Lember <klember@redhat.com> - 2.62.1-1
- Update to 2.62.1

* Fri Sep 06 2019 Kalev Lember <klember@redhat.com> - 2.62.0-1
- Update to 2.62.0

* Tue Sep 03 2019 Kalev Lember <klember@redhat.com> - 2.61.3-1
- Update to 2.61.3

* Mon Aug 12 2019 Kalev Lember <klember@redhat.com> - 2.61.2-1
- Update to 2.61.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.61.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 David King <amigadave@amigadave.com> - 2.61.1-2
- Fix CVE-2019-12450 (#1719142)
- Consistently use buildroot macro

* Fri May 24 2019 Kalev Lember <klember@redhat.com> - 2.61.1-1
- Update to 2.61.1

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 2.61.0-2
- Rebuild with Meson fix for #1699099

* Mon Apr 15 2019 Kalev Lember <klember@redhat.com> - 2.61.0-1
- Update to 2.61.0

* Mon Apr 15 2019 Kalev Lember <klember@redhat.com> - 2.60.1-1
- Update to 2.60.1

* Wed Mar 13 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.60.0-3
- Switch back to timestamp-based pyc invalidation mode

* Wed Mar  6 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.60.0-2
- Make sure all .py files have fixed timestamps (fixes issue with
  parallel installability of i686 and amd64 -devel packages)
- Switch to explicit byte compilation to override invalidation mode

* Mon Mar 04 2019 Kalev Lember <klember@redhat.com> - 2.60.0-1
- Update to 2.60.0

* Mon Feb 18 2019 Kalev Lember <klember@redhat.com> - 2.59.3-1
- Update to 2.59.3

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 2.59.2-1
- Update to 2.59.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.59.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Kalev Lember <klember@redhat.com> - 2.59.1-1
- Update to 2.59.1

* Thu Jan 03 2019 Kalev Lember <klember@redhat.com> - 2.59.0-1
- Update to 2.59.0
- Switch to the meson build system

* Tue Dec 18 2018 Kalev Lember <klember@redhat.com> - 2.58.2-1
- Update to 2.58.2

* Fri Oct 05 2018 Kalev Lember <klember@redhat.com> - 2.58.1-2
- Fix multilib -devel installs (#1634778)

* Fri Sep 21 2018 Kalev Lember <klember@redhat.com> - 2.58.1-1
- Update to 2.58.1

* Wed Sep 05 2018 Kalev Lember <klember@redhat.com> - 2.58.0-1
- Update to 2.58.0

* Thu Aug 2 2018 Ondrej Holy <oholy@redhat.com> - 2.57.2-1
- Update to 2.57.2

* Fri Jul 20 2018 Ondrej Holy <oholy@redhat.com> - 2.57.1-1
- Update to 2.57.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.56.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.56.1-5
- Rebuilt for Python 3.7

* Thu Jun 14 2018 Debarshi Ray <rishi@fedoraproject.org> - 2.56.1-4
- Backport patch to fix possible invalid pointer in dbus callback in the FD.o
  notification backend (RH #1584916)

* Sun May 27 2018 Kalev Lember <klember@redhat.com> - 2.56.1-3
- Fix multilib -devel installs (#1581067)

* Sun May 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.56.1-2
- Include upstream patch to fix gdbus-codegen with meson 0.46.

* Sun Apr 08 2018 Kalev Lember <klember@redhat.com> - 2.56.1-1
- Update to 2.56.1

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 2.56.0-1
- Update to 2.56.0

* Wed Feb 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.55.2-3
- Undo disabling mangling

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 2.55.2-2
- Disable brp-mangle-shebangs shebangs

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 2.55.2-1
- Update to 2.55.2
- Drop ldconfig scriptlets

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.55.1-3
- Switch to %%ldconfig_scriptlets

* Thu Jan 18 2018 Kalev Lember <klember@redhat.com> - 2.55.1-2
- gmain: Partial revert of recent wakeup changes

* Mon Jan 08 2018 Kalev Lember <klember@redhat.com> - 2.55.1-1
- Update to 2.55.1
- Drop upstreamed systemtap multilib fix

* Tue Dec 19 2017 Kalev Lember <klember@redhat.com> - 2.55.0-1
- Update to 2.55.0

* Wed Nov 01 2017 Kalev Lember <klember@redhat.com> - 2.54.2-1
- Update to 2.54.2

* Fri Oct 06 2017 Kalev Lember <klember@redhat.com> - 2.54.1-1
- Update to 2.54.1

* Mon Sep 11 2017 Kalev Lember <klember@redhat.com> - 2.54.0-1
- Update to 2.54.0

* Tue Sep 05 2017 Kalev Lember <klember@redhat.com> - 2.53.7-1
- Update to 2.53.7

* Sat Aug 19 2017 Kalev Lember <klember@redhat.com> - 2.53.6-1
- Update to 2.53.6

* Mon Aug 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.53.5-1
- Update to 2.53.5

* Tue Aug 01 2017 Kalev Lember <klember@redhat.com> - 2.53.4-4
- Backport glib-mkenums flags annotation parsing fixes

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.53.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 2.53.4-2
- Revert a GKeyFile introspection ABI change

* Tue Jul 18 2017 Kalev Lember <klember@redhat.com> - 2.53.4-1
- Update to 2.53.4

* Thu Jun 22 2017 Kalev Lember <klember@redhat.com> - 2.53.3-1
- Update to 2.53.3

* Thu Jun 8 2017 Owen Taylor <otaylor@redhat.com> - 2.53.2-2
- Make triggers also compile schemas in /app/share/glib-2.0/schemas

* Wed May 24 2017 Florian Müllner <fmuellner@redhat.com> - 2.53.2-1
- Update to 2.53.2

* Mon May 15 2017 Kalev Lember <klember@redhat.com> - 2.52.2-2
- Backport a gmain GWakeup patch to fix timedatex high CPU usage (#1450628)

* Tue May 09 2017 Kalev Lember <klember@redhat.com> - 2.52.2-1
- Update to 2.52.2

* Tue Apr 11 2017 Colin Walters <walters@verbum.org> - 2.52.1-3
- Backport patches for gmain wakeup for qemu
  See: https://bugzilla.gnome.org/show_bug.cgi?id=761102

* Tue Apr 11 2017 Colin Walters <walters@verbum.org> - 2.52.1-2
- Explictly remove PCRE sources
- Related: https://bugzilla.redhat.com/show_bug.cgi?id=1324770

* Tue Apr 11 2017 Kalev Lember <klember@redhat.com> - 2.52.1-1
- Update to 2.52.1

* Mon Mar 20 2017 Kalev Lember <klember@redhat.com> - 2.52.0-1
- Update to 2.52.0

* Thu Mar 16 2017 Kalev Lember <klember@redhat.com> - 2.51.5-1
- Update to 2.51.5

* Thu Mar 02 2017 Kalev Lember <klember@redhat.com> - 2.51.4-2
- Remove the dependency on dbus-launch again (#927212)

* Wed Mar 01 2017 David King <amigadave@amigadave.com> - 2.51.4-1
- Update to 2.51.4
- Add a Requires on dbus-launch (#927212)
- Use pkgconfig for BuildRequires

* Tue Feb 14 2017 Richard Hughes <rhughes@redhat.com> - 2.51.2-1
- Update to 2.51.2

* Mon Feb 13 2017 Richard Hughes <rhughes@redhat.com> - 2.51.1-1
- Update to 2.51.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.51.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.51.0-2
- Rebuild for Python 3.6

* Sun Oct 30 2016 Kalev Lember <klember@redhat.com> - 2.51.0-1
- Update to 2.51.0

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 2.50.1-1
- Update to 2.50.1

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 2.50.0-1
- Update to 2.50.0

* Tue Sep 13 2016 Kalev Lember <klember@redhat.com> - 2.49.7-1
- Update to 2.49.7
- Don't set group tags

* Sun Aug 28 2016 Kalev Lember <klember@redhat.com> - 2.49.6-1
- Update to 2.49.6

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 2.49.5-1
- Update to 2.49.5
- Own /usr/share/gdb and /usr/share/systemtap directories

* Tue Aug 16 2016 Miro Hrončok <mhroncok@redhat.com> - 2.49.4-3
- Use Python 3 for the RPM Python byte compilation

* Wed Jul 27 2016 Ville Skyttä <ville.skytta@iki.fi> - 2.49.4-2
- Switch to Python 3 (#1286284)

* Thu Jul 21 2016 Kalev Lember <klember@redhat.com> - 2.49.4-1
- Update to 2.49.4

* Sun Jul 17 2016 Kalev Lember <klember@redhat.com> - 2.49.3-1
- Update to 2.49.3

* Wed Jun 22 2016 Richard Hughes <rhughes@redhat.com> - 2.49.2-1
- Update to 2.49.2

* Wed Jun 01 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 2.49.1-2
- Soften shared-mime-info dependency (#1266118)

* Fri May 27 2016 Florian Müllner <fmuellner@redhat.com> - 2.49.1-1
- Update to 2.49.1

* Tue May 10 2016 Kalev Lember <klember@redhat.com> - 2.48.1-1
- Update to 2.48.1

* Wed Apr 06 2016 Colin Walters <walters@redhat.com> - 2.48.0-2
- Explicitly require system pcre, though we happened to default to this now
  anyways due to something else pulling PCRE into the buildroot
  Closes rhbz#1287266

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 2.48.0-1
- Update to 2.48.0

* Thu Mar 17 2016 Richard Hughes <rhughes@redhat.com> - 2.47.92-1
- Update to 2.47.92

* Wed Feb 24 2016 Colin Walters <walters@redhat.com> - 2.47.6.19.gad2092b-2
- git snapshot to work around https://bugzilla.gnome.org/show_bug.cgi?id=762637
- Add --with-python=/usr/bin/python explicitly to hopefully fix a weird
  issue I am seeing where librepo fails to build in epel7 with this due to
  us requiring /bin/python.

* Wed Feb 17 2016 Richard Hughes <rhughes@redhat.com> - 2.47.6-1
- Update to 2.47.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 David King <amigadave@amigadave.com> - 2.47.5-1
- Update to 2.47.5

* Wed Dec 16 2015 Kalev Lember <klember@redhat.com> - 2.47.4-1
- Update to 2.47.4

* Wed Nov 25 2015 Kalev Lember <klember@redhat.com> - 2.47.3-1
- Update to 2.47.3

* Wed Nov 25 2015 Kalev Lember <klember@redhat.com> - 2.47.2-1
- Update to 2.47.2

* Mon Nov 09 2015 Kevin Fenzi <kevin@scrye.com> - 2.47.1-2
- Add full path redirect output to null and || : to triggers.

* Wed Oct 28 2015 Kalev Lember <klember@redhat.com> - 2.47.1-1
- Update to 2.47.1

* Mon Oct 19 2015 Kalev Lember <klember@redhat.com> - 2.46.1-2
- Backport an upstream fix for app launching under wayland (#1273146)

* Wed Oct 14 2015 Kalev Lember <klember@redhat.com> - 2.46.1-1
- Update to 2.46.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 2.46.0-1
- Update to 2.46.0

* Mon Sep 14 2015 Kalev Lember <klember@redhat.com> - 2.45.8-1
- Update to 2.45.8

* Tue Sep 01 2015 Kalev Lember <klember@redhat.com> - 2.45.7-1
- Update to 2.45.7

* Wed Aug 19 2015 Kalev Lember <klember@redhat.com> - 2.45.6-1
- Update to 2.45.6

* Wed Aug 19 2015 Kalev Lember <klember@redhat.com> - 2.45.5-1
- Update to 2.45.5

* Fri Aug 14 2015 Matthias Clasen <mclasen@redhat.com> - 2.45.4-2
- Add file triggers for gio modules and gsettings schemas

* Tue Jul 21 2015 David King <amigadave@amigadave.com> - 2.45.4-1
- Update to 2.45.4

* Wed Jun 24 2015 Kalev Lember <klember@redhat.com> - 2.45.3-2
- Backport a patch to fix notification withdrawing in gnome-software

* Wed Jun 24 2015 David King <amigadave@amigadave.com> - 2.45.3-1
- Update to 2.45.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.45.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 David King <amigadave@amigadave.com> - 2.45.2-1
- Update to 2.45.2

* Thu Apr 30 2015 Kalev Lember <kalevlember@gmail.com> - 2.45.1-1
- Update to 2.45.1

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 2.44.0-1
- Update to 2.44.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 2.43.92-1
- Update to 2.43.92

* Mon Mar 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.43.91-1
- Update to 2.43.91

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 2.43.90-2
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Wed Feb 18 2015 David King <amigadave@amigadave.com> - 2.43.90-1
- Update to 2.43.90
- Update man pages glob in files section

* Tue Feb 10 2015 Matthias Clasen <mclasen@redhat.com> - 2.43.4-1
- Update to 2.43.4

* Tue Jan 20 2015 David King <amigadave@amigadave.com> - 2.43.3-1
- Update to 2.43.3

* Wed Dec 17 2014 Kalev Lember <kalevlember@gmail.com> - 2.43.2-1
- Update to 2.43.2

* Tue Nov 25 2014 Kalev Lember <kalevlember@gmail.com> - 2.43.1-1
- Update to 2.43.1

* Thu Oct 30 2014 Florian Müllner <fmuellner@redhat.com> - 2.43.0-1
- Update to 2.43.0

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 2.42.0-1
- Update to 2.42.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 2.41.5-1
- Update to 2.41.5

* Thu Sep  4 2014 Matthias Clasen <mclasen@redhat.com> 2.41.4-3
- Don't remove rpath from gdbus-peer test - it doesn't work without it

* Thu Sep 04 2014 Bastien Nocera <bnocera@redhat.com> 2.41.4-2
- Fix banshee getting selected as the default movie player

* Tue Sep 02 2014 Kalev Lember <kalevlember@gmail.com> - 2.41.4-1
- Update to 2.41.4

* Sat Aug 16 2014 Kalev Lember <kalevlember@gmail.com> - 2.41.3-1
- Update to 2.41.3

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.41.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 23 2014 Stef Walter <stefw@redhat.com> - 2.41.2-2
- Fix regression with GDBus array encoding rhbz#1122128

* Mon Jul 14 2014 Kalev Lember <kalevlember@gmail.com> - 2.41.2-1
- Update to 2.41.2

* Sat Jul 12 2014 Tom Callaway <spot@fedoraproject.org> - 2.41.1-2
- fix license handling

* Tue Jun 24 2014 Richard Hughes <rhughes@redhat.com> - 2.41.1-1
- Update to 2.41.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.41.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 2.41.0-1
- Update to 2.41.0

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 2.40.0-1
- Update to 2.40.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 2.39.92-1
- Update to 2.39.92

* Tue Mar 04 2014 Richard Hughes <rhughes@redhat.com> - 2.39.91-1
- Update to 2.39.91

* Tue Feb 18 2014 Richard Hughes <rhughes@redhat.com> - 2.39.90-1
- Update to 2.39.90

* Tue Feb 04 2014 Richard Hughes <rhughes@redhat.com> - 2.39.4-1
- Update to 2.39.4

* Tue Jan 14 2014 Richard Hughes <rhughes@redhat.com> - 2.39.3-1
- Update to 2.39.3

* Sun Dec 22 2013 Richard W.M. Jones <rjones@redhat.com> - 2.39.2-2
- Re-add static subpackage so that we can build static qemu as
  an AArch64 binfmt.

* Tue Dec 17 2013 Richard Hughes <rhughes@redhat.com> - 2.39.2-1
- Update to 2.39.2

* Mon Dec 09 2013 Richard Hughes <rhughes@redhat.com> - 2.39.1-2
- Backport a patch from master to stop gnome-settings-daemon crashing.

* Thu Nov 14 2013 Richard Hughes <rhughes@redhat.com> - 2.39.1-1
- Update to 2.39.1

* Mon Oct 28 2013 Richard Hughes <rhughes@redhat.com> - 2.39.0-1
- Update to 2.39.0

* Tue Sep 24 2013 Kalev Lember <kalevlember@gmail.com> - 2.38.0-1
- Update to 2.38.0

* Tue Sep 17 2013 Kalev Lember <kalevlember@gmail.com> - 2.37.93-1
- Update to 2.37.93

* Mon Sep 02 2013 Kalev Lember <kalevlember@gmail.com> - 2.37.7-1
- Update to 2.37.7

* Wed Aug 21 2013 Debarshi Ray <rishi@fedoraproject.org> - 2.37.6-1
- Update to 2.37.6

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 2.37.5-2
- Perl 5.18 rebuild

* Thu Aug  1 2013 Debarshi Ray <rishi@fedoraproject.org> - 2.37.5-1
- Update to 2.37.5

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.37.4-2
- Perl 5.18 rebuild

* Tue Jul  9 2013 Matthias Clasen <mclasen@redhat.com> - 2.37.4-1
- Update to 2.37.4

* Thu Jun 20 2013 Debarshi Ray <rishi@fedoraproject.org> - 2.37.2-1
- Update to 2.37.2

* Tue May 28 2013 Matthias Clasen <mclasen@redhat.com> - 2.37.1-1
- Update to 2.37.1
- Add a tests subpackage

* Sat May 04 2013 Kalev Lember <kalevlember@gmail.com> - 2.37.0-1
- Update to 2.37.0

* Sat Apr 27 2013 Thorsten Leemhuis <fedora@leemhuis.info> - 2.36.1-2
- Fix pidgin freezes by applying patch from master (#956872)

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 2.36.1-1
- Update to 2.36.1

* Mon Mar 25 2013 Kalev Lember <kalevlember@gmail.com> - 2.36.0-1
- Update to 2.36.0

* Tue Mar 19 2013 Matthias Clasen <mclasen@redhat.com> - 2.35.9-1
- Update to 2.35.9

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> - 2.35.8-1
- Update to 2.35.8

* Tue Feb 05 2013 Kalev Lember <kalevlember@gmail.com> - 2.35.7-1
- Update to 2.35.7

* Tue Jan 15 2013 Matthias Clasen <mclasen@redhat.com> - 2.35.4-1
- Update to 2.35.4

* Thu Dec 20 2012 Kalev Lember <kalevlember@gmail.com> - 2.35.3-1
- Update to 2.35.3

* Sat Nov 24 2012 Kalev Lember <kalevlember@gmail.com> - 2.35.2-1
- Update to 2.35.2

* Thu Nov 08 2012 Kalev Lember <kalevlember@gmail.com> - 2.35.1-1
- Update to 2.35.1
- Drop upstreamed codegen-in-datadir.patch
