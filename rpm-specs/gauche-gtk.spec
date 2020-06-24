%global gauche_main_version 0.97

%global snapshot_date 20181110
%global git_sha       0220722c44ef85f2e1b9b14745702c1b923258e8
%global git_revision  %(c=%{git_sha}; echo ${c:0:7})
%global alphatag      %{snapshot_date}git%{git_revision}

Name:           gauche-gtk
Epoch:          1
Version:        0.6
Release:        0.26.%{alphatag}%{?dist}
Summary:        Gauche extension module to use GTK

License:        BSD
URL:            http://practical-scheme.net/
Source0:        https://github.com/shirok/Gauche-gtk2/archive/%{git_sha}.tar.gz#/%{name}-%{version}-%{git_revision}.tar.gz
Patch0:         https://sources.debian.org/data/main/g/gauche-gtk/0.6+git20160927-3/debian/patches/00_no_path_xtra.patch
Patch1:         https://sources.debian.org/data/main/g/gauche-gtk/0.6+git20160927-3/debian/patches/05_install_755.patch
Patch2:         https://sources.debian.org/data/main/g/gauche-gtk/0.6+git20160927-3/debian/patches/06_gdk_pixbuf.patch
Patch3:         https://sources.debian.org/data/main/g/gauche-gtk/0.6+git20160927-3/debian/patches/07-HUGE.patch
Patch4:         https://sources.debian.org/data/main/g/gauche-gtk/0.6+git20160927-3/debian/patches/08-configure-ac-fix.patch
Patch5:         https://sources.debian.org/data/main/g/gauche-gtk/0.6+git20160927-3/debian/patches/09-gen-gpd-fix.patch

BuildRequires:  gcc
BuildRequires:  gauche-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtkglext-devel
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  libICE-devel
BuildRequires:  autoconf
# used in test
BuildRequires:  gauche-gl
BuildRequires:  Xvfb xauth

Requires:       gauche-gl


%description
Gauche extension module to use GTK.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
Development files for %{name}.


%prep
%autosetup -p 1 -n Gauche-gtk2-%{git_sha}
autoconf


%build
%configure --enable-gtkgl --enable-glgd --enable-glgd-pango
%make_build stubs
%make_build OPTFLAGS=


%install
mkdir -p %{buildroot}`gauche-config --syslibdir`
mkdir -p %{buildroot}`gauche-config --sysarchdir`
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.so' -exec chmod 0755 '{}' ';'
chmod -c 644 */*.c # for debuginfo


%check
# 'make check' does not set return code properly, but
# outputs to test.log
xvfb-run -a -w 1 %make_build check
# Gtk test currently fails.
# four known failures reported upstream; fail if more failures occur
# https://github.com/shirok/Gauche-gtk2/issues/2
[ $(grep " ==> ERROR: GOT " src/test.log | wc -l) -le 4 ]



%files
%doc README VERSION examples
%license COPYING
%{_libdir}/gauche-%{gauche_main_version}/site/*/*.so
%{_datadir}/gauche-%{gauche_main_version}/site/lib/.packages/Gauche-gtk2.gpd
%{_datadir}/gauche-%{gauche_main_version}/site/lib/gtk.scm
%{_datadir}/gauche-%{gauche_main_version}/site/lib/gtk
%{_datadir}/gauche-%{gauche_main_version}/site/lib/h2s


%files devel
%{_libdir}/gauche-%{gauche_main_version}/site/include/*


%changelog
* Fri Apr  3 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 1:0.6-0.26.20181110git0220722
- Rebuilt for Gauche 0.9.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6-0.25.20181110git0220722
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6-0.24.20181110git0220722
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6-0.23.20181110git0220722
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 06 2019 Björn Esser <besser82@fedoraproject.org> - 1:0.6-0.22.20160927git6fca535
- Update to new snapshot, fixes FTBFS (#1604053)
- Add Debian patches, fixes FTBFS (#1604053)
- Add BuildRequires: gcc
- Use %%license for COPYING file
- Modernize spec-file

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6-0.21.20121223gitceb4579
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6-0.20.20121223gitceb4579
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1:0.6-0.19.20121223gitceb4579
- Rebuilt for switch to libxcrypt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6-0.18.20121223gitceb4579
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6-0.17.20121223gitceb4579
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6-0.16.20121223gitceb4579
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6-0.15.20121223gitceb4579
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.6-0.14.20121223gitceb4579
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May  4 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1:0.6-0.13.20121223gitceb4579
- Drop ExcludeArch for ppc64

* Thu Dec  4 2014 Michel Alexandre Salim <salimma@fedoraproject.org> - 1:0.6-0.12.20121223gitceb4579
- Rebuild for Gauche 0.9.4 and Gauche-gl 0.6
- Update to latest snapshot

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.6-0.11.20120403gitf7d3f802f3750
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.6-0.10.20120403gitf7d3f802f3750
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.6-0.9.20120403gitf7d3f802f3750
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.6-0.8.20120403gitf7d3f802f3750
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.6-0.7.20120403gitf7d3f802f3750
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 13 2012 Michel Salim <salimma@fedoraproject.org> - 1:0.6-0.6.20120403gitf7d3f802f3750
- Correct the path to test log

* Sun May 13 2012 Michel Salim <salimma@fedoraproject.org> - 1:0.6-0.5.20120403gitf7d3f802f3750
- Rebuild for Gauche 0.9.3.x
- Update to latest snapshot
- Enable graphical tests
- Spec clean-ups

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.6-0.4.20110725git598828842a339
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 22 2011 Michel Salim <salimma@fedoraproject.org> - 1:0.6-0.3.20110725git598828842a339
- Include Epoch field in -devel subpackage's dependence on main package

* Fri Sep 16 2011 Michel Salim <salimma@fedoraproject.org> - 1:0.6-0.2.20110725git598828842a339
- add Epoch field for upgrade path from mislabeled 0.9 release

* Thu Sep 15 2011 Michel Salim <salimma@fedoraproject.org> - 0.6-0.1.20110725git598828842a339
- Updated Git snapshot
- Fix version numbering
- Put header in -devel subpackage
- Fix overlapping directory ownerships
- Enable tests

* Mon Feb 14 2011 Gerard Milmeister <gemi@bluewin.ch> - 0.9-1.git20110214
- New release to match Gauche 0.9

* Sat Aug  1 2009 Gerard Milmeister <gemi@bluewin.ch> - 0.4.1-21
- fix for gtk 2.17

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 20 2009 Gerard Milmeister <gemi@bluewin.ch> - 0.4.1-19
- updated for gauche 0.8.14

* Thu Feb 14 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.4.1-17
- rebuild for gauche 0.8.13

* Mon Aug 20 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.4.1-16
- fix include problem

* Mon Aug 20 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.4.1-15
- fix gtk problem

* Sat Aug 18 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.4.1-14
- exclude arch ppc64, depends on non-existing ppc64 gauche

* Sat Aug 18 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.4.1-13
- rebuild for gauche 0.8.11

* Fri Apr 20 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.4.1-12
- rebuild for gauche 0.8.10

* Thu Feb 22 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.4.1-11
- added fix for using opt flags

* Thu Jan 18 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.4.1-10
- rebuild for gauche 0.8.9

* Mon Nov 13 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.4.1-9
- rebuilt for gauche 0.8.8

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.4.1-8
- Rebuild for FE6

* Fri May  5 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.4.1-7
- Added include flags for freetype
- Added -fPIC flag 

* Wed Feb 23 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:0.4.1-1
- New Version 0.4.1

* Fri Mar 19 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.4-0.fdr.1
- New Version 0.4

* Fri Mar 19 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.3.2-0.fdr.1
- New Version 0.3.2

* Mon Nov 10 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:0.3.1-0.fdr.1
- First Fedora release
