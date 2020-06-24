Summary: Circuit simulator
Name:    qucs
Version: 0.0.18
Release: 18%{?dist}
License: GPL+
URL:     http://qucs.sourceforge.net/

Source0: http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz

Patch0: qucs-0.0.18-qucsrescodes-progname-typo.patch
# Temporary fix for gcc bug #1299599
Patch1:  %{name}-%{version}-gcc-ppc64le-bug.patch
# Desktop file categories must terminate with a semicolon, bug #1424234
Patch2:  %{name}-0.0.18-Fix-desktop-file.patch

BuildRequires: desktop-file-utils
BuildRequires: qt-devel
BuildRequires: flex
BuildRequires: bison
Requires: freehdl, perl-interpreter, iverilog
Requires: electronics-menu
Requires: mot-adms >= 2.3.4


%description
Qucs is a circuit simulator with graphical user interface.  The
software aims to support all kinds of circuit simulation types,
e.g. DC, AC, S-parameter and harmonic balance analysis.


%package lib
Summary:  Qucs library


%description lib
Qucs circuit simulator library


%package devel
Summary:  Qucs development headers
Requires: %{name}-lib%{?_isa} = %{version}-%{release}


%description devel
Qucs circuit simulator development headers


%prep
%setup -q

%patch0 -p1
%ifarch ppc64le
%patch1 -p1
%endif
%patch2 -p1

# fixing the icon path
sed -i 's|Icon=/usr/share/pixmaps|Icon=/usr/share/qucs/bitmaps|' debian/%{name}.desktop


%build
%configure --disable-dependency-tracking

# remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' qucs-core/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' qucs-core/libtool

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
install -d %{buildroot}%{_datadir}/applications

desktop-file-install \
    --add-category "X-Fedora" \
    --add-category "Engineering" \
    --set-icon "qucs" \
    --dir=%{buildroot}%{_datadir}/applications \
    debian/%{name}.desktop


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/qucs*
%{_bindir}/ps2sp*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_mandir}/man1/*
# the following binaries were introduced in 0.0.17 (repoquery shows no conflicts with other pkgs)
%{_bindir}/alter
%{_bindir}/asco
%{_bindir}/asco-test
%{_bindir}/log
%{_bindir}/monte
%{_bindir}/postp
%{_bindir}/rosen
# introduced in 0.0.18 - adms provided by mot-adms
%exclude %{_bindir}/admsCheck
%exclude %{_bindir}/admsXml
%exclude %{_mandir}/man1/admsXml.*
%exclude %{_mandir}/man1/admsCheck.*
%{_datadir}/icons/*


%files lib
%{_libdir}/libqucs.so.*


%files devel
%{_includedir}/*
%{_libdir}/libqucs.so
%{_libdir}/libqucs.la


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.0.18-14
- rebuilt due new iverilog

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.18-13
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 0.0.18-10
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>
- Correct desktop file installation (bug #1424234)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Rafael Fonseca <rdossant@redhat.com> - 0.0.18-7
- Workaround gcc bug on ppc64le (#1299599)

* Tue Jan 19 2016 Jaromir Capik <jcapik@redhat.com> - 0.0.18-6
- Dropping built-in adms and using the system one (#1230751)
- Fixing the qucrescodes->qucsrescodes program name typo

* Wed Jan 13 2016 Jaromir Capik <jcapik@redhat.com> - 0.0.18-5
- Fixing the icon path (#1279203)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.0.18-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Sep 10 2014 Jaromir Capik <jcapik@redhat.com> - 0.0.18-2
- Disabling the debug

* Tue Sep 02 2014 Jaromir Capik <jcapik@redhat.com> - 0.0.18-1
- Update to 0.0.18

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 05 2014 Jaromir Capik <jcapik@redhat.com> - 0.0.17-3
- Fixing format-security flaws (#1037299)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Jaromir Capik <jcapik@redhat.com> - 0.0.17-1
- Update to 0.0.17
- Fixing Source0 URL

* Fri May 24 2013 Jaromir Capik <jcapik@redhat.com> - 0.0.16-7
- Adding electronics-menu in the requires
- Minor spec file changes according to the latest guidelines

* Mon Apr 08 2013 Jaromir Capik <jcapik@redhat.com> - 0.0.16-6
- aarch64 support (#926417)
- fixing bogus date in the changelog

* Sat Feb 23 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.0.16-5
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 03 2011 Bruno Wolff III <bruno@wolff.to> - 0.0.16-1
- Update to upstream 0.0.16
- Fix FTBFS - bug 631404

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 07 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.15-3
- Patch no longer needed with freehdl-0.0.7

* Sun May 03 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.15-2
- Correct a problem in digital simulation

* Fri May 01 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.15-1
- Update to 0.0.15

* Sat Apr 05 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.14-1
- Update to 0.0.14

* Sat Apr 05 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.13-3
- Modify BR from qt-devel to qt3-devel

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.13-2
- Autorebuild for GCC 4.3

* Tue Jan 01 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.13-1
- Update to 0.0.13

* Sun Sep 09 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.12-4
- Modifiy qucs.desktop BZ 283941

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.0.12-3
- Rebuild for selinux ppc32 issue.

* Sun Jun 17 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.12-2
- Add perl and iverilog as require

* Sun Jun 17 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.12-1
- Update to 0.0.12

* Sat May 05 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.11-2
- Rebuild

* Sun Mar 18 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.11-1
- Update to 0.0.11

* Fri Sep 01 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.10-1
- Update to 0.0.10

* Sat Jun 10 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.9-4
- Solve typo problem in changelog

* Sat Jun 10 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.9-3
- Delete %%{_bindir}/qucsdigi.bat which is a windows bat file and useless under linux
- add --disable-dependency-tracking to %%configure
- add --enable-debug to %%configure to make debuginfo package usefull

* Thu Jun 01 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.9-2
- Delete ${RPM_OPT_FLAGS} modification using -ffriend-injection for "%%{?fedora}" > "4"

* Mon May 29 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.9-1
- Update to 0.0.9

* Mon Jan 23 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.8-1
- Update to 0.0.8
- Add -ffriend-injection to $RPM_OPT_FLAGS for building against gcc-4.1
 
* Fri Nov 4 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.7-8
- Modify ctaegories in qucs.desktop

* Wed Oct 19 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.7-7
- Add qucs-0.0.7-2.diff for the x86_64 target

* Tue Oct 18 2005 Ralf Corsepius <rc040203@freenet.de> - 0.0.7-6
- Add qucs-0.0.7-config.diff to make configure script aware of RPM_OPT_FLAGS.

* Tue Oct 11 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.7-5
-add qucs.desktop
-modify buildroot

* Tue Aug 2 2005 Wojciech Kazubski <wk@ire.pw.edu.pl>
- version 0.0.7.

* Thu Jun 23 2005 Wojciech Kazubski <wk@ire.pw.edu.pl>
- rebuilt for Fedora Core 4

* Mon May 30 2005 Wojciech Kazubski <wk@ire.pw.edu.pl>
- version 0.0.6.

* Thu Mar 3 2005 Wojciech Kazubski <wk@ire.pw.edu.pl>
- version 0.0.5.

* Fri Dec 10 2004 Wojciech Kazubski <wk@ire.pw.edu.pl>
- version 0.0.4 for Fedora Core 3
