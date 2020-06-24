%if (0%{?fedora} && 0%{?fedora} < 19)  || (0%{?rhel} && 0%{?rhel} < 7)
%global with_desktop_vendor_tag 1
%endif

%global git_snapshot 1

%if 0%{?git_snapshot}
%global         gitdate       20200316
%global         gitcommit     cb2992e23409829ff672da12413b95d9638439d0
%global         shortcommit   %(c=%{gitcommit}; echo ${c:0:7})

%global         tarballdate   20200328
%global         tarballtime   1539

%global         gitversion    D%{gitdate}git%{shortcommit}
%endif

%undefine        _changelog_trimtime

Name:           lxterminal
Version:        0.3.2
Release:        6%{?gitversion:.%{?gitversion}}%{?dist}
Summary:        Desktop-independent VTE-based terminal emulator
Summary(de):    Desktop-unabhängiger VTE-basierter Terminal Emulator

License:        GPLv2+
URL:            http://lxde.sourceforge.net/
%if 0%{?git_snapshot}
Source0:        %{name}-%{version}-%{tarballdate}T%{tarballtime}.tar.gz
%else
Source0:        http://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.xz
%endif
# Shell script to create tarball from git scm
Source100:      create-lxterminal-git-bare-tarball.sh


%if 0%{?git_snapshot}
BuildRequires:	git
%endif

BuildRequires:	gcc
%if 0%{?fedora} >= 31
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(vte-2.91)
%else
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.18.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.6.0
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(vte)
%endif

BuildRequires:	%{_bindir}/xsltproc
BuildRequires:	docbook-utils
BuildRequires:	docbook-style-xsl

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	gettext

%if 0%{?git_snapshot}
BuildRequires:  automake
BuildRequires:  libtool
%endif

%description
LXterminal is a VTE-based terminal emulator with support for multiple tabs. 
It is completely desktop-independent and does not have any unnecessary 
dependencies. In order to reduce memory usage and increase the performance 
all instances of the terminal are sharing a single process.

%description -l de
LXTerminal ist ein VTE-basierter Terminalemulator mit Unterstützung für 
mehrere Reiter. Er ist komplett desktop-unabhängig und hat keine unnötigen 
Abhängigkeiten. Um den Speicherverbrauch zu reduzieren und die Leistung zu
erhöhen teilen sich alle Instanzen des Terminals einen einzigen Prozess.

%prep
%if 0%{?git_snapshot} > 0

%setup -q -c -T -a 0
git clone ./%{name}.git
cd %{name}

git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-owner@fedoraproject.org"

git checkout -b %{version}-fedora %{gitcommit}

cp -a [A-Z]* ..
%endif

%if 0%{?git_snapshot} < 1
%setup -q
%endif

%build
%if 0%{?git_snapshot}
cd %{name}
sh autogen.sh
%endif

%configure \
%if 0%{?fedora} >= 31
	--enable-gtk3 \
%endif
	--enable-man \
	--disable-silent-rules \
	%{nil}

make %{?_smp_mflags}

%install
%if 0%{?git_snapshot}
cd %{name}
%endif

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

desktop-file-install \
%if 0%{?with_desktop_vendor_tag}
  --vendor fedora \
%endif
  --delete-original                                        \
  --remove-category=Utility                                \
  --add-category=System                                    \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications          \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

%if 0%{?git_snapshot}
cd ..
%endif

%find_lang %{name}


%files -f %{name}.lang
%doc	AUTHORS
%license	COPYING
%doc	NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}*.1*


%changelog
* Sat Mar 28 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.2-6.D20200316gitcb2992e
- Update to the latest git

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5.D20190717gitcb2992e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.2-4.D20190717gitcb2992e
- Update to the latest git
- F-31+: use vte-2.91 + gtk3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.2-1
- 0.3.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6.D20180225git3779fce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.1-5.D20180225git3779fce
- Use latest git, switch to git bare
- PR patch for unixsocket.c optimization issue merged upstream

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-3
- Remove obsolete scriptlets

* Mon Dec 25 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.1-2
- Add PR patch for unixsocket.c optimization / startup issue

* Mon Nov  6 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.1-1
- 0.3.1

* Fri Sep  8 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-6.D20170822git1e9f2d4d
- Update to the latest git

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-3
- Upstream git patch to address CVE-2016-10369 (bug 1449114)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 26 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-1
- 0.3.0

* Sun Dec 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-8.D20161208git9e61321c
- Update to the latest git

* Sun Dec  4 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-7.D20161202git6da8eae6
- Update to the latest git

* Wed Aug 10 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-6.D20160809git80291921
- Update to the latest git
  - https://github.com/lxde/lxterminal/pull/21
  - https://github.com/lxde/lxterminal/issues/20

* Thu Aug  4 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-5.D20160607gitd4014424
- Try the latest git

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4.D20151126gitbe658ad3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-3.D20151126gitbe658ad3
- Try the latest git

* Thu Jul 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-2
- Fix scriptlet

* Thu Jun 18 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-1
- 0.2.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.1.11-7
- Really drop desktop vendor tag.

* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - 0.1.11-6
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.1.11-2
- Rebuild for new libpng

* Tue Aug 30 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.11-1
- Update to 0.1.11
- Remove upstreamed vte patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 01 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9
- Add patch for vte >= 0.20.0

* Mon Jul 19 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.8-1
- Update to 0.1.8
- Drop all previous patches, they are part of 0.1.8
- Update German translation

* Thu May 27 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.7-2
- Major code rework from git (fixes #571591 and 596358)

* Wed Mar 03 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7

* Wed Feb 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.6-3
- Add patch to fix DSO linking (#564717)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.6-1
- Update to 0.1.6
- Remove missing-icons.patch, changes got upstreamed

* Tue Jun 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.5-2
- Rebuilt for libvte SONAME bump

* Wed May 20 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5
- Fix icon for Info menu entry

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 26 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Sat Jun 28 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3
- Add the new manpage

* Fri Jun 20 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-1
- Initial Fedora package
