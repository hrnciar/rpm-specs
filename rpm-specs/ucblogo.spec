Name:           ucblogo
Version:        6.1
Release:        2%{?dist}
Summary:        An interpreter for the Logo programming language

License:        GPLv3+
Source:         https://github.com/jrincayc/ucblogo-code/archive/version_%{version}.tar.gz
Source1:        %{name}.desktop
URL:            https://people.eecs.berkeley.edu/~bh/logo.html
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  texi2html
BuildRequires:  tetex-dvips
BuildRequires:  ghostscript
BuildRequires:  libbsd-devel
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  libSM-devel
BuildRequires:  libICE-devel
BuildRequires:  ncurses-devel
BuildRequires:  wxGTK3-devel
BuildRequires:  ghostscript-tools-dvipdf
BuildRequires:  desktop-file-utils
Requires(post):  /sbin/install-info
Requires(preun): /sbin/install-info
Requires: hicolor-icon-theme

%description
Berkeley Logo (ucblogo) is an interpreter for the Logo programming
language. Logo is a computer programming language designed for use by
learners, including children. This dialect of Logo features
random-access arrays, variable number of inputs to user-defined
procedures, various error handling improvements, comments and
continuation lines, first-class instruction and expression templates,
and macros.

%package doc
Summary: Documentation for ucblogo
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
This package includes HTML and PDF documentation for ucblogo
and the Program Logic Manual (plm)

%prep
%setup -q -n ucblogo-code-version_%{version}


# correct directories /usr/lib -> /usr/share and /usr/local ->  /usr
sed -i 's|/local/lib/logo|/share/logo|g' *.c README.md
sed -i 's|/lib/logo|/share/logo|g' *.c makefile*
sed -i "s|/usr/local/bin/logo|%{_bindir}/logo|g" docs/usermanual.texi
sed -i "s|/usr/local/bin/logo|%{_bindir}/logo|g" README.md
sed -i "s|/usr/local/info|%{_datadir}/info|g" README.md

find -name 'CVS' | xargs rm -rf
find -name '.svn' | xargs rm -rf


%build
# build WX version
%configure --with-wx-config=/usr/bin/wx-config-3.0
make %{_smp_mflags} logo
mv logo logo-wx
# build traditional version
make clean
%configure --x-includes=%{_includedir} --x-libraries=%{_libdir} --with-x --with-wx-config=no
make %{_smp_mflags}
# build docs
make make-docs


%install
#Note: makefile does not support DESTDIR
%makeinstall

install -m0755 logo-wx ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/info
mv -f ${RPM_BUILD_ROOT}%{_prefix}/info/* ${RPM_BUILD_ROOT}%{_datadir}/info
rm -fr ${RPM_BUILD_ROOT}%{_prefix}/info
rm -fr ${RPM_BUILD_ROOT}%{_datadir}/logo/docs
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps
install -p -m 644 ucblogo.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps

rm -f ${RPM_BUILD_ROOT}%{_bindir}/install-logo-mode

%post
/sbin/install-info %{_infodir}/ucblogo.info --entry="* UCBLogo: (ucblogo).     Berkeley Logo User Manual." --section="Programming Languages"  %{_infodir}/dir 2>/dev/null || :

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete  %{_infodir}/ucblogo.info --entry="* UCBLogo: (ucblogo).        Berkeley Logo User Manual." --section="Programming Languages"  %{_infodir}/dir 2>/dev/null || :
fi

%files
%doc README.md changes.txt
%license LICENSE
%{_bindir}/*
%{_datadir}/logo
%{_infodir}/*
%{_mandir}/man1/logo*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%files doc
%doc docs/html docs/usermanual.pdf plm

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 26 2019 Joshua Cogliati <jrincayc@yahoo.com> - 6.1-1
- new release 6.1

* Fri Sep 27 2019 Joshua Cogliati <jrincayc@yahoo.com> - 6.0-27
- Removing emacs mode and created separate doc package

* Fri Sep 13 2019 Joshua Cogliati <jrincayc@yahoo.com> - 6.0-26
- Updated to support wxGTK3, added man page and desktop file

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.0-24
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 08 2016 Filipe Rosset <rosset.filipe@gmail.com> - 6.0-20
- Spec clean up + rebuilt

* Sat Jul  9 2016 Gérard Milmeister <gemi@bluewin.ch> - 6.0-19
- Fixed include problem

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 6.0-16
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul  1 2014 Matěj Cepl <mcepl@redhat.com> - 6.0-14
- Fix FTBFS (#992830) using patch by Dave Allan

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb  7 2011 Gérard Milmeister <gemi@bluewin.ch> - 6.0-7
- rebuild for f14
- fixed manual building makefile

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 6.0-6
- rebuilt against wxGTK-2.8.11-2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 22 2008 Gerard Milmeister <gemi@bluewin.ch> - 6.0-2
- re-add emacs logo-mode from previous release as a separate package

* Thu Nov 20 2008 Gerard Milmeister <gemi@bluewin.ch> - 6.0-1
- new release 6.0

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.5-10
- Autorebuild for GCC 4.3

* Thu Feb 22 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.5-9
- add patch for fixing ncurses problem

* Wed Feb 21 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.5-8
- add fix to use cursesw instead of curses

* Wed Feb 21 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.5-7
- replace BR libtermcap-devel by BR ncurses-devel

* Sun Feb 11 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.5-6
- rebuild to use ncurses

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.5-5
- Rebuild for FE6

* Thu Jun 29 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.5-4
- added BR texi2html
- added BR libXt-devel
- added include and libs options for X11 to configure

* Sat Jun  3 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.5-3
- added BuildReq: texinfo-tex
- make owned the directory %%{_datadir}/emacs/site-lisp/site-start.d

* Sun Aug 14 2005 Gerard Milmeister <gemi@bluewin.ch> - 5.5-2
- New Version 5.5

* Mon Mar  7 2005 Gerard Milmeister <gemi@bluewin.ch> - 5.4-1
- New Version 5.4

* Thu Feb 26 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:5.3-0.fdr.2
- Install info files
- Install emacs site-start file

* Sun Oct 26 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:5.3-0.fdr.1
- First Fedora release
