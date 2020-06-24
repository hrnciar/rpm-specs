%global majorrel 4.3.0
%global commit 36b721ca374d695c10af8137c943f27f12503014
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20190827


Name:		freewrl
Version:	%{majorrel}
Release:	3.%{commitdate}git%{shortcommit}%{?dist}
Summary:	X3D / VRML visualization program
License:	LGPLv3+
URL:		http://freewrl.sourceforge.net
# Source0:	http://sourceforge.net/projects/freewrl/files/freewrl-linux/3.0/%%{name}-%%{version}.tar.bz2
# git clone https://git.code.sf.net/p/freewrl/git freewrl-git
# cd freewrl-git
# cp -a freex3d/ ../freewrl-%%{version}-%%{commitdate}git%%{shortcommit}
# cd ..
# tar --exclude-vcs -cjf %%{name}-%%{version}-%%{commitdate}git%%{shortcommit}.tar.bz2 freewrl-%%{version}-%%{commitdate}git%%{shortcommit}
Source0:	%{name}-%{version}-%{commitdate}git%{shortcommit}.tar.bz2
Source1:	README.FreeWRL.java
# gcc says:
# main/ProdCon.c:427:19: error: too few arguments to function 'cParse'
Patch3:		freewrl-3.0.0-20170208git621ae4e-cparse-stl-fix.patch
# warning: '__builtin_strncpy' output truncated before terminating nul copying 54 bytes from a string of the same length [-Wstringop-truncation]
Patch4:		freewrl-4.3.0-use-memcpy-instead-of-strncpy.patch
# main/ProdCon.c:414:29: warning: implicit declaration of function 'convertAsciiSTL' [-Wimplicit-function-declaration]
# main/ProdCon.c:424:29: warning: implicit declaration of function 'convertBinarySTL' [-Wimplicit-function-declaration]
Patch5:		freewrl-4.3.0-missing-functions.patch
# lots of indent issues caught by -Wmisleading-indentation
Patch6:		freewrl-4.3.0-fix-indent-issues.patch
# lots of signedness fixes like
# io_files.c:627:17: warning: pointer targets in passing argument 1 of 'stlDTFT' differ in signedness [-Wpointer-sign]
Patch7:		freewrl-4.3.0-sign-fixes.patch
BuildRequires:	gcc-c++
BuildRequires:	zlib-devel, freetype-devel, fontconfig-devel
BuildRequires:	imlib2-devel, nspr-devel
BuildRequires:	expat-devel, libXxf86vm-devel, libX11-devel, libXext-devel
BuildRequires:	mesa-libGL-devel, mesa-libGLU-devel, glew-devel, libxml2-devel
BuildRequires:	libjpeg-devel, libpng-devel, java-devel, unzip, wget
BuildRequires:	ImageMagick, desktop-file-utils, chrpath
BuildRequires:	libXaw-devel, libXmu-devel, freealut-devel
BuildRequires:	liblo-devel, libcurl-devel, openal-soft-devel
%ifnarch armv7hl s390x
BuildRequires:	firefox
%endif
BuildRequires:	sox, doxygen, /usr/bin/latex, /usr/bin/mf
BuildRequires:	texlive-texconfig, tex(fmtutil.cnf), tex(multirow.sty)
BuildRequires:	tex(xtab.sty), tex(tocloft.sty), tex(cmr10.tfm)
BuildRequires:	tex(ecrm1000.tfm), tex(sectsty.sty), tex(fancyhdr.sty)
BuildRequires:	tex(natbib.sty), tex(phvr8t.tfm), tex(wasysym.sty)
BuildRequires:	tex(zptmcm7t.tfm), tex(pcrr8t.tfm)
BuildRequires:	tex(adjustbox.sty), tex(language.dat), tex(hanging.sty)
BuildRequires:	texlive-makeindex-bin, texlive-dvips-bin
BuildRequires:	texlive-courier, texlive-helvetic, texlive-gsftopk, texlive-updmap-map
BuildRequires:	tex(stackengine.sty), tex(listofitems.sty), tex(ulem.sty)
BuildRequires:	tex(newunicodechar.sty), tex(etoc.sty)
BuildRequires:	texlive-wasy
BuildRequires:	ode-devel
BuildRequires:	autoconf, automake, libtool
# FIXME: Presumably a packaging bug. Indirectly required by
# some TeX stuff, but not automatically pulled-in.
BuildRequires:  tex(tabu.sty)

Requires:	sox, unzip, wget, ImageMagick

%description
FreeWRL is an X3D / VRML visualization program. This package contains the
standalone commandline tool.

%package devel
Summary:	Development files for FreeWRL
Requires:	freewrl%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Development libraries and headers for FreeWRL.

%package java
Summary:	Java support for FreeWRL
Requires:	java-headless
Requires:	freewrl%{?_isa} = %{version}-%{release}

%description java
Java support for FreeWRL.

%package -n libEAI
Summary:	FreeWRL EAI C support library

%description -n libEAI
FreeWRL EAI C support library.

%package -n libEAI-devel
Summary:	Development files for libEAI
Requires:	libEAI%{?_isa} = %{version}-%{release}

%description -n libEAI-devel
Development libraries and headers for libEAI.

%ifnarch armv7hl s390x
%package plugin
Summary:	Browser plugin for FreeWRL
Requires:	freewrl%{?_isa} = %{version}-%{release}
Requires:	firefox

%description plugin
FreeWRL is an X3D / VRML visualization program. This package contains the
browser plugin for Firefox (and other xulrunner compatible browsers).
%endif

%prep
%setup -q -n %{name}-%{majorrel}-%{commitdate}git%{shortcommit}
cp %{SOURCE1} .
# Don't need it.
rm -rf appleOSX/
%patch3 -p1 -b .cparsestlfix
%patch4 -p1 -b .memcpy
%patch5 -p1 -b .missing-functions
%patch6 -p1 -b .fixindent
%patch7 -p1 -b .signfix
autoreconf --force --install

# hardcoding /usr/local/lib is a no-no
sed -i 's|libpath = "/usr/local/lib"|libpath = "%{_libdir}"|g' src/bin/main.c

%build
%global optflags %{optflags} -Wno-comment -Wno-unused-variable
export LDFLAGS="-Wl,--as-needed"
%configure --with-target=x11 \
	   --enable-fontconfig \
	   --enable-java \
	   --enable-libeai \
	   --disable-osc \
	   --enable-libcurl \
           --enable-rbp \
           --enable-twodee \
           --enable-STL \
	   --disable-static \
	   --with-javadir=/usr/lib/jvm/java-openjdk/jre/lib/ext \
	   --with-javascript=duk \
	   --with-statusbar=hud
make %{?_smp_mflags}
pushd doc
make latex/refman.pdf
popd

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}/
install -p src/java/java.policy %{buildroot}%{_datadir}/%{name}/

# no firefox on armv7hl | s390x
%ifarch armv7hl s390x
rm -rf %{buildroot}%{_libdir}/mozilla/plugins/libFreeWRLplugin.so
%endif

rm -rf %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/mozilla/plugins/*.la

desktop-file-validate %{buildroot}%{_datadir}/applications/freewrl.desktop
chmod -x %{buildroot}%{_datadir}/applications/freewrl.desktop
chmod -x %{buildroot}%{_datadir}/%{name}/java.policy

chrpath --delete %{buildroot}%{_bindir}/freewrl
# chrpath --delete %%{buildroot}%%{_bindir}/freewrl_snd
chrpath --delete %{buildroot}%{_libdir}/libFreeWRLEAI.so.*

%ldconfig_scriptlets

%ldconfig_scriptlets -n libEAI

%files
%doc AUTHORS README TODO
%license COPYING COPYING.LESSER
%{_bindir}/%{name}
%{_bindir}/%{name}_msg
# %%{_bindir}/%%{name}_snd
%{_libdir}/libFreeWRL.so.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}*

%files devel
%doc doc/latex/refman.pdf
%{_includedir}/libFreeWRL.h
%{_libdir}/libFreeWRL.so
%{_libdir}/pkgconfig/libFreeWRL.pc

%files java
%doc README.FreeWRL.java
%{_datadir}/%{name}/
/usr/lib/jvm/java-openjdk/jre/lib/ext/vrml.jar

%files -n libEAI
%license COPYING COPYING.LESSER
%{_libdir}/libFreeWRLEAI.so.*

%files -n libEAI-devel
%{_includedir}/FreeWRLEAI/
%{_libdir}/libFreeWRLEAI.so
%{_libdir}/pkgconfig/libFreeWRLEAI.pc

# Plugin is dead and gone, thanks to Mozilla.
%if 0
%ifnarch armv7hl s390x
%files plugin
%{_libdir}/mozilla/plugins/libFreeWRLplugin.so
%endif
%endif

%changelog
* Thu Jun 18 2020 Tom Callaway <spot@fedoraproject.org> - 4.3.0-3.20190827git36b721c
- fix tex dependencies

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2.20190827git36b721c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Tom Callaway <spot@fedoraproject.org> - 4.3.0-1.20190827git36b721c
- update to latest git master
- apply some code cleanups to make compile quieter

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-11.20170729git4f920cb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Tom Callaway <spot@fedoraproject.org> - 3.0.0-10.20170729git4f920cb
- add lots of missing tex BRs

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-9.20170729git4f920cb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8.20170729git4f920cb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun  1 2018 Tom Callaway <spot@fedoraproject.org> - 3.0.0-7.20170729git4f920cb
- add missing texlive BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6.20170729git4f920cb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 31 2017 Tom Callaway <spot@fedoraproject.org> - 3.0.0-5.20170729git4f920cb
- update again, git master is now proper branch
- reapply curl res fix

* Fri Jul 28 2017 Tom Callaway <spot@fedoraproject.org> - 3.0.0-4.20170708git7a28224
- update to git devel tree
- do not bother with mozilla plugin
- fix code to not immediately and always SEGV

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3.20170208git621ae4e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb  8 2017 Tom Callaway <spot@fedoraproject.org> - 3.0.0-2.20170208git621ae4e
- update to git develop tree
- disable osc
- fix armv7hl weirdness

* Fri May 27 2016 Tom Callaway <spot@fedoraproject.org> - 3.0.0-1
- update to 3.0.0

* Fri Feb 05 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.3.3.1-7
- Add BR: tex(tabu.sty) (Fix F24FTBFS).
- Add %%license.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Tom Callaway <spot@fedoraproject.org> - 2.3.3.1-6
- add missing tex BR

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Tom Callaway <spot@fedoraproject.org> - 2.3.3.1-3
- add missing tex BR

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Tom Callaway <spot@fedoraproject.org> - 2.3.3.1-1
- update to 2.3.3.1

* Tue Apr 22 2014 Tom Callaway <spot@fedoraproject.org> - 2.3.3-1
- update to 2.3.3

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.22.13.1-13
- Use Requires: java-headless rebuild (#1067528)

* Sun Feb  9 2014 Tom Callaway <spot@fedoraproject.org> - 1.22.13.1-12
- fix the fontconfig font matching code to actually work (bz 1062829)

* Tue Dec  3 2013 Tom Callaway <spot@fedoraproject.org> - 1.22.13.1-11
- fix error with -Werror=format-security 

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 1.22.13.1-10
- rebuilt for GLEW 1.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.13.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr  9 2013 Tom Callaway <spot@fedoraproject.org> - 1.22.13.1-8
- use js-devel (xulrunner's jsapi.h is now C++ only)

* Fri Feb  1 2013 Tom Callaway <spot@fedoraproject.org> - 1.22.13.1-7
- three args for JS_GetPrototype today
- fix more abandoned API

* Wed Jan  9 2013 Tom Callaway <spot@fedoraproject.org> - 1.22.13.1-6
- use JS_NewGlobalObject instead of JS_NewCompartmentAndGlobalObject

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.22.13.1-5
- rebuild against new libjpeg

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 1.22.13.1-4
- Rebuild for glew 1.9.0

* Tue Jul 31 2012 Tom Callaway <spot@fedoraproject.org> - 1.22.13.1-3
- fix build, patch out deprecated JS_FinalizeStub, JS_DestroyContextMaybeGC

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Tom Callaway <spot@fedoraproject.org> - 1.22.13.1-1
- update to 1.22.13.1

* Tue Jan 17 2012 Tom Callaway <spot@fedoraproject.org> - 1.22.12-0.7.pre2
- fix compile with gcc 4.7

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.12-0.6.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec  6 2011 Tom Callaway <spot@fedoraproject.org> - 1.22.12-0.5.pre2
- fix build against firefox8 

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.22.12-0.4.pre2
- Rebuild for new libpng

* Tue Aug  9 2011 Tom Callaway <spot@fedoraproject.org> - 1.22.12-0.3.pre2
- move browser plugin to independent subpackage to minimize deps on main package

* Tue Aug  9 2011 Tom Callaway <spot@fedoraproject.org> - 1.22.12-0.2.pre2
- drop Requires: pkgconfig
- delete appleOSX/ dir 

* Wed Jul 27 2011 Tom Callaway <spot@fedoraproject.org> - 1.22.12-0.1.pre2
- pre2

* Tue Jul 19 2011 Tom Callaway <spot@fedoraproject.org> - 1.22.12-0.1.pre1
- initial package
