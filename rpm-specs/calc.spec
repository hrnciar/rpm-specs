# Enabling this option invokes section 3 of the LGPL, applying the terms of
# the ordinary GNU General Public License version 2 instead of the LGPL.
# See the included "calc-converted-to-gpl.txt" source file for details.
%define with_readline 1

# This is disabled right now because it prevents correct linking. The issues
# here are related to the issues with linking with readline, in that the 
# split between libraries is poorly defined.
%define with_custom_interface 0

%if %{with_readline}
License:       GPLv2
%else
License:       LGPLv2
%endif

Name:          calc
Version:       2.12.7.2
Release:       5%{?dist}
Summary:       Arbitrary precision arithmetic system and calculator

# Also, https://github.com/lcn2/calc
URL:           http://isthe.com/chongo/tech/comp/calc/
Source0:       https://github.com/lcn2/calc/releases/download/%{version}/calc-%{version}.tar.bz2
Source1:       calc-converted-to-gpl.txt
Source2:       calc-COPYING-GPL

BuildRequires: gcc, sed, util-linux

# for compatibility with the Debian package name
Provides:      apcalc

%if %{with_readline}
# If readline-devel < 5.2-3, READLINE_EXTRAS must be set to 
# "-lhistory -lncurses" or some variant (e.g. -ltinfo).
# If readline-devel < 4.2, something else goes horribly wrong.
BuildRequires: ncurses-devel >= 5.2-26, readline-devel >= 5.2-3
%endif

Recommends:    less >= 358
Recommends:    %{name}-stdrc

%description
Calc is an arbitrary precision C-like arithmetic system that is a
calculator, an algorithm-prototyper, and a mathematical research tool. Calc
comes with a rich set of built-in mathematical and programmatic functions.
%if %{with_readline}
Note: this copy of Calc is linked against the GNU Readline library and has
been converted to the ordinary GPL as per section 3 of the LGPL. See the
included calc-converted-to-gpl.txt document for details.
%endif


%package libs
Summary:       Libraries for the calc arithmetic system

%description libs
Shared libraries used by the calc command line calculator and other programs
using its arbitrary precision arithmetic routines.


%package devel
Summary:        Development files for the calc arithmetic system
Requires:       %{name}-libs = %{version}-%{release}

%description devel
This package contains files necessary to build applications which use the
calc arbitrary precision arithmetic system.


%package stdrc
Summary:      Standard resource files the calc arithmetic system
Requires:     %{name} = %{version}-%{release}

%description stdrc
This package contains the standard calc resource files and several calc
shell scripts. They serve as examples of the calc language and may also be
useful in themselves.



%prep
%setup -q

%if %{with_readline}
  for f in help.c version.c calc.man $( ls help/*|grep  '^help/credit$' ) ; do
    sed -i -e's/version 2.1 \(.*GNU\)/version 2 \1/;s/COPYING\(.\)LGPL/COPYING\1GPL/;s/copying.lgpl/copying-gpl/;s/GNU LGPL/GNU GPL/;s/GNU Lesser General/GNU General/' $f
  done
  cp -p %{SOURCE1} COPYING
  cp -p %{SOURCE2} COPYING-GPL
%endif


%build
# note parallel make (-j3, or whatever) doesn't work correctly.
make DEBUG="%{optflags}" \
%if %{with_custom_interface}
     ALLOW_CUSTOM="-DCUSTOM" \
%else
     ALLOW_CUSTOM="" \
%endif
     LD_SHARE="" \
%if %{with_readline}
     USE_READLINE="-DUSE_READLINE" \
     READLINE_LIB="-lreadline" \
     READLINE_EXTRAS="" \
%else
     USE_READLINE="" \
%endif
     HAVE_FPOS="-DHAVE_NO_FPOS" \
     BINDIR=%{_bindir} \
     LIBDIR=%{_libdir} \
     CALC_SHAREDIR=%{_datadir}/%{name} \
     CALC_INCDIR=%{_includedir}/calc \
     SCRIPTDIR=%{_datadir}/%{name}/cscript \
     MANDIR=%{_mandir}/man1 \
     Q="" V="@" \
     all


%install

make T=%{buildroot} \
%if %{with_custom_interface}
     ALLOW_CUSTOM="-DCUSTOM" \
%else
     ALLOW_CUSTOM="" \
%endif
     BINDIR=%{_bindir} \
     LIBDIR=%{_libdir} \
     CALC_SHAREDIR=%{_datadir}/%{name} \
     CALC_INCDIR=%{_includedir}/calc \
     SCRIPTDIR=%{_datadir}/%{name}/cscript \
     MANDIR=%{_mandir}/man1 \
     install

%if %{with_readline} 
  rm -f %{buildroot}/%{_datadir}/%{name}/help/COPYING-LGPL
  # mode 444 to match the other files
  install -p -m 444 COPYING-GPL %{buildroot}/%{_datadir}/%{name}/help/
  rm -f %{buildroot}/%{_datadir}/%{name}/bindings
%endif

%if ! %{with_custom_interface}
  # if we don't enable the custom interface, don't ship symlinks to it
  rm -f %{buildroot}/%{_libdir}/libcustcalc.so*
%endif

# Changing permissions of executables to 755 to shut up rpmlint.
chmod 755 %{buildroot}%{_datadir}/%{name}/cscript/*
chmod 755 %{buildroot}%{_bindir}/calc

# Fix permissions of libcalc, which upstream is now shipping non-executable
# for some reason
chmod 755 %{buildroot}/%{_libdir}/libcalc.so.%{version}

# move these so the doc macro can find them
mv %{buildroot}%{_datadir}/%{name}/README README-standard-resource
mv cscript/README README-cscript


%check
make chk
     

%ldconfig_scriptlets libs


%files
%if %{with_readline}
%doc BUGS CHANGES README.FIRST README.md
%license COPYING COPYING-GPL
%else
%doc BUGS CHANGES README.FIRST README.md
%license COPYING-LGPL
%endif
%{_bindir}/calc
%{_mandir}/man1/calc.1*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/help
%{_datadir}/%{name}/help/*
%if %{with_custom_interface}
%dir %{_datadir}/%{name}/custhelp
%{_datadir}/%{name}/custhelp/*
%endif
%if ! %{with_readline}
%{_datadir}/%{name}/bindings
%endif

%files libs
%if %{with_readline}
%doc BUGS CHANGES
%license COPYING COPYING-GPL
%else
%doc BUGS CHANGES
%license COPYING-LGPL
%endif
%{_libdir}/libcalc.so.*
%if %{with_custom_interface}
%{_libdir}/libcustcalc.so.*
%endif

%files devel
%doc LIBRARY
%{_libdir}/libcalc.so
%if %{with_custom_interface}    
%{_libdir}/libcustcalc.so
%endif
%dir %{_includedir}/calc
%{_includedir}/calc/*.h

%files stdrc
%doc README-standard-resource README-cscript
%dir %{_datadir}/%{name}/cscript
%{_datadir}/%{name}/cscript/*
%if %{with_custom_interface}
%dir %{_datadir}/%{name}/custom
%{_datadir}/%{name}/custom/*
%endif
%{_datadir}/%{name}/*.cal
%{_datadir}/%{name}/*.line


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.12.7.2-3
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 Matthew Miller <mattdm@fedoraproject.org> - 2.12.7.2-1
- new upstream "unstable" release (building into rawhide)

* Sun Jul 22 2018 Matthew Miller <mattdm@fedoraproject.org> - 2.12.6.7-5
- add gcc to buildreqs

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Matthew Miller <mattdm@fedoraproject.org> - 2.12.6.7-3
- add Provides: apcalc to match the package name in Debian

* Wed May 16 2018 Matthew Miller <mattdm@fedoraproject.org> - 2.12.6.7-2
- version bump for test rebuild

* Mon Mar 05 2018 Matthew Miller <mattdm@fedoraproject.org> - 2.12.6.7-1
- update to upstream "unstable" 2.12.6.7 for rawhide (code cleanups only)
- * misc errors in help corrected
- * various buffer sizes and stacks increased

* Wed Feb 28 2018 Matthew Miller <mattdm@fedoraproject.org> - 2.12.6.6-1
- update to upstream "unstable" 2.12.6.6 for rawhide:

* Thu Feb 08 2018 Matthew Miller <mattdm@fedoraproject.org> - 2.12.6.5-3
- spec file moderization

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Matthew Miller <mattdm@fedoraproject.org> - 2.12.6.5-1
- new upstream stable release
- minor fixes

* Tue Jan 16 2018 Matthew Miller <mattdm@fedoraproject.org> - 2.12.6.4-1
- new upstream devel release.
- minor optimizations and fixes

* Thu Sep  7 2017 Matthew Miller <mattdm@fedoraproject.org> - 2.12.6.3-1
- new upstream devel release.
- Changes all to lucas.cal, so if Lucas primality tests are your thing,
  this release is for you.

* Fri Aug 18 2017 Matthew Miller <mattdm@fedoraproject.org> - 2.12.6.1-1
- new upstream development release (minor bugfixes), build stuff changed
  around, and some changes to stdin handling.
- add new readme files to docs

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun  6 2017 Matthew Miller <mattdm@fedoraproject.org> - 2.12.6.0-1
- new upstream development release (minor bugfixes)
- github release url
- recommend rather than require `less`

* Mon May 22 2017 Matthew Miller <mattdm@fedoraproject.org> - 2.12.5.6-1
- new upstream release 2.15.5.6 (2.15.5.5 only lasted a few hours)
- primarily code cleanup to prepare for move to github
- also, meaning of T in build seems to have inverted, so removing

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.12.5.4-2
- Rebuild for readline 7.x

* Wed Sep 14 2016 Matthew Miller <mattdm@fedoraproject.org> - 2.12.5.4-1
- upstream bump in version number but *no* code changes from 2.12.5.3
  (apparently to support rebuild of upstream packages on RHEL 7.x)
- add Recommends for stdrc subpackage to main package
  
* Tue Feb  9 2016 Matthew Miller <mattdm@fedoraproject.org> - 2.12.5.3-1
- update to 2.12.5.3 (new upstream UNstable version)
- upstream is _only_ OS X file location changes; updating rawhide just for
  the formality

* Sun Feb  7 2016 Matthew Miller <mattdm@fedoraproject.org> - 2.12.5.2-1
- update to 2.12.5.2 (new upstream UNstable version)
- upstream is primarily bugfixes

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Matthew Miller <mattdm@fedoraproject.org> - 2.12.5.0-3
- remove unnecessary defattr as part of cleanup effort

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 13 2014 Matthew Miller <mattdm@fedoraproject.org> - 2.12.5.0-1
- update to 2.12.5.0 (new upstream stable version)
- upstream is primarily bugfixes

* Mon Sep 22 2014 Matthew Miller <mattdm@fedoraproject.org> - 2.12.4.14-1
- update to 2.12.4.14
- see CHANGES -- fixes at least one significant bug in complex number
  comparison, plus  many other bugfixes which should mostly be
  operational, not in the math parts.
- minor tweak to LGPL->GPL conversion logic in specfile
- license tag for both subpackages
- fix wrong versions in changelog going back a couple of years; oops.
  (Affects changelog only, and... retroactively. Sorry.)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 27 2014 Matthew Miller <mattdm@fedoraproject.org> - 2.12.4.13-2
- use license tag for license instead of docs

* Sun Feb 02 2014 Matthew Miller <mattdm@fedoraproject.org> - 2.12.4.13-1
- update to new ultra-minor upstream version. This update includes a
  fix to lucas.cal; if you know what the Lucas primality test is, you
  may want this update, and otherwise you probably do not care.

* Mon Sep 02 2013 Matthew Miller <mattdm@fedoraproject.org> - 2.12.4.12-1
- yet more sample scripts + minor other changes, including ctype-like builtins
- .cal scripts are not linked, so leave those LGPL
- bz #959898. Also, happy Labor Day.

* Sun Aug 11 2013 Matthew Miller <mattdm@fedoraproject.org> - 2.12.4.10-1
- upstream includes more sample scripts + minor other changes

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 20 2013 Matthew Miller <mattdm@fedoraproject.org> - 2.12.4.8-1
- update to newer development version (build system changes only)

* Tue May  7 2013 Matthew Miller <mattdm@fedoraproject.org> - 2.12.4.7-2
- libcalc.so needs to be executable. 

* Tue May  7 2013 Matthew Miller <mattdm@fedoraproject.org> - 2.12.4.7-1
- update to newer development version (minor upstream changes)

* Thu Feb 14 2013 Matthew Miller <mattdm@mattdm.org> - 2.12.4.4-6
- make the license doc conditional more straightforward; old too-clever
  approach was confusing newer rpm
- correct which license file is used when readline isn't selected, in case
  for some reason someone really really wants to avoid conversion to GPL
- fix the date of the first changelog entry to make rpm not whine about it

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 11 2011 Matthew Miller <mattdm@mattdm.org> - 2.12.4.4-2
- update GPL to new address

* Wed Aug 10 2011 Matthew Miller <mattdm@mattdm.org> - 2.12.4.4-1
- update to 2.12.4.4 (latest unstable, but differences from stable
  are small bugfixes)
- vsnprintf bug fix is accepted upstream, so remove patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov  3 2008 Matthew Miller <mattdm@mattdm.org> - 2.12.4.0-3
- fixed extra vsnprintf crash bug

* Mon Oct 27 2008 Matthew Miller <mattdm@mattdm.org> - 2.12.4.0-2
- entangled readline patch is made obsolete by linking changes in
  readline itself. (readline is still too entangled, but
  that's an upstream problem.)

* Mon Oct 27 2008 Matthew Miller <mattdm@mattdm.org> - 2.12.4.0-1
- update to 2.12.4.0
- upstream has switched to bz2 at my request :)
- some of the entangled-readline-fix stuff is upstream, but for a 
  complete fix some coding is needed. (Also, adding libedit as an option
  would be good -- talk to me for details.)
- patch to disable the custom lib completely is upstream. cool.
- add ALLOW_CUSTOM definition to make install section -- changes to upstream
  makefile mean that if that's missing it now tries to build the custom lib
  at that point.
- upstream now doesn't create the custom dir if ALLOW_CUSTOM is off, so we
  no longer need to clean it up. And same with custhelp. There's still an
  upstream bug where libcustomcalc dangling symlinks are created, though.


* Wed Feb 20 2008 Matthew Miller <mattdm@mattdm.org> - 2.12.2.1-12
- add util-linux as a build prereq

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.12.2.1-11
- Autorebuild for GCC 4.3

* Fri Sep 21 2007 Matthew Miller <mattdm@mattdm.org> - 2.12.2.1-10
- add HAVE_FPOS="-DHAVE_NO_FPOS" to make ppc build work properly. Thanks
  to Denis Leroy and David Woodhouse. RH Bug #299581.

* Thu Sep 20 2007 Matthew Miller <mattdm@mattdm.org> - 2.12.2.1-9
- Remove extra license choice information from package release field to
  properly comply with the packaging guidelines so as to not make Spot sad.
  Put a note in the description instead.
- Today is Thursday.

* Wed Sep 19 2007 Matthew Miller <mattdm@mattdm.org> - 2.12.2.1-8
- initial package for Fedora
- clear old and long pre-fedora changelog
- review request rhbug #227570
