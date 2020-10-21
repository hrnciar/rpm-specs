# The garbage collector does not work with PIE
%undefine _hardened_build

# TODO: review desktop entry associations (does text/* work?)
# TODO: zero-length /usr/share/xemacs-21.5-b26/lisp/dump-paths.el
# TODO: non-ASCII in buffer tabs

%bcond_with     gtk
%bcond_with     wnn
%bcond_with     xaw3d
%bcond_with     xfs
%bcond_with     xim
%bcond_without  mule
%bcond_without  nox
%ifarch ia64
# no-expdyn-ia64 patch, https://bugzilla.redhat.com/show_bug.cgi?id=106744#c39
%bcond_with     modules
%else
%bcond_without  modules
%endif

%global snap    20200331hge2ac728aa576

Name:           xemacs
Version:        21.5.34
Release:        38%{?snap:.%{snap}}%{?dist}
Summary:        Different version of Emacs

%global majver %(cut -d. -f1-2 <<<%{version})

License:        GPLv3+
URL:            http://www.xemacs.org/
%if 0%{?snap:1}
Source0:        %{name}-%{snap}.tar.xz
%else
Source0:        http://ftp.xemacs.org/xemacs-%{majver}/xemacs-%{version}.tar.gz
%endif
Source1:        %{name}.appdata.xml
Source2:        xemacs.desktop
Source3:        dotxemacs-init.el
Source4:        default.el
Source5:        xemacs-sitestart.el
Source6:        gnuclient.desktop

# Fedora-specific.  Don't run the check-features Makefile target.  It checks
# that necessary packages are installed, but they aren't installed while
# building an RPM.
Patch0:         %{name}-21.5.25-mk-nochk-features.patch
# Experimental patch.  Fix WNN support.  This patch is no longer sufficient.
# WNN still doesn't work.
Patch1:         %{name}-21.5.25-wnnfix-128362.patch
# Fedora-specific.  Don't force ISO-8859 fonts.
Patch2:         %{name}-21.5.34-utf8-fonts.patch
# Experimental patch, to be sent upstream eventually.  Don't use
# -export-dynamic on IA64; leads to segfaults due to function pointer issues.
Patch3:         %{name}-21.5.27-no-expdyn-ia64-106744.patch
# Fedora-specific.  Default to courier instead of lucidatypewriter.
Patch4:         %{name}-21.5.28-courier-default.patch
# Fedora-specific.  Recognize the Fedora X server.
Patch5:         %{name}-21.5.29-x-server.patch
# Submitted upstream by Henry Thompson: fix playing sounds through ALSA
Patch6:         %{name}-21.5.34-alsaplay.patch
# Submitted upstream 28 Dec 2017: do not rely on integer overflow wrapping
Patch7:         %{name}-21.5.34-overflow.patch
# Submitted upstream 28 Dec 2017: better computation of data start address
Patch8:         %{name}-21.5.34-data-start.patch
# Submitted upstream 22 Jul 2020: Use strsignal() in preference to sys_siglist
Patch9:         %{name}-21.5.34-strsignal.patch

BuildRequires:  compface-devel
BuildRequires:  desktop-file-utils
%if %{with mule}
%if %{with wnn}
BuildRequires:  FreeWnn-devel
%endif
%endif
BuildRequires:  gcc
BuildRequires:  gdbm-devel
BuildRequires:  giflib-devel
BuildRequires:  gmp-devel
BuildRequires:  gpm-devel
BuildRequires:  openldap-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  texinfo
BuildRequires:  xmkmf
%if %{with gtk}
BuildRequires:  pkgconfig(gtk+-3.0)
%else
BuildRequires:  xorg-x11-xbitmaps
%if %{with xaw3d}
BuildRequires:  pkgconfig(xaw3d)
%else
BuildRequires:  neXtaw-devel
%endif
%endif
# Note: no xemacs-packages-extra dependency here, need main pkg to build it.
Requires:       xemacs-packages-base
Requires:       %{name}-common = %{version}-%{release}
Requires:       xorg-x11-fonts-ISO8859-1-75dpi
Requires:       xorg-x11-fonts-ISO8859-1-100dpi
Requires:       xorg-x11-fonts-misc
Requires(post): alternatives
Requires(post): coreutils
Requires(postun): alternatives
Requires(postun): coreutils
Provides:       xemacs(bin) = %{version}-%{release}

%global xver    %(echo %{version} | sed -e 's/\\.\\([0-9]\\+\\)$/-b\\1/')
%global xbuild  %(echo %{_build} | sed -e 's/^\\([^-]*-[^-]*-[^-]*\\).*/\\1/')

%description
XEmacs is a highly customizable open source text editor and
application development system.  It is protected under the GNU General
Public License and related to other versions of Emacs, in particular
GNU Emacs.  Its emphasis is on modern graphical user interface support
and an open software development model, similar to Linux.

This package contains XEmacs built for X Windows%{?with_mule: with MULE support}.

%package        common
Summary:        Lisp files and other common files for XEmacs
Requires:       %{name}-filesystem = %{version}-%{release}
Requires(post): alternatives
Requires(preun): alternatives

%description    common
XEmacs is a highly customizable open source text editor and
application development system.  It is protected under the GNU General
Public License and related to other versions of Emacs, in particular
GNU Emacs.  Its emphasis is on modern graphical user interface support
and an open software development model, similar to Linux.

This package contains lisp and other common files for XEmacs.

%package        nox
Summary:        Different version of Emacs built without X Windows support
# Note: no xemacs-packages* dependencies here, we need -nox to build the
# base package set.
Requires:       %{name}-common = %{version}-%{release}
Requires(post): alternatives
Requires(post): coreutils
Requires(postun): alternatives
Provides:       xemacs(bin) = %{version}-%{release}

%description    nox
XEmacs is a highly customizable open source text editor and
application development system.  It is protected under the GNU General
Public License and related to other versions of Emacs, in particular
GNU Emacs.  Its emphasis is on modern graphical user interface support
and an open software development model, similar to Linux.

This package contains XEmacs built without X Windows support.

%package        xft
Summary:        Different version of Emacs built with Xft/fontconfig support
Requires:       %{name}-common = %{version}-%{release}
Requires:       xemacs-packages-base
Requires(post): alternatives
Requires(post): coreutils
Requires(postun): alternatives
Provides:       xemacs(bin) = %{version}-%{release}

%description    xft
XEmacs is a highly customizable open source text editor and
application development system.  It is protected under the GNU General
Public License and related to other versions of Emacs, in particular
GNU Emacs.  Its emphasis is on modern graphical user interface support
and an open software development model, similar to Linux.

This package contains XEmacs built with Xft and fontconfig support.

%package        info
Summary:        XEmacs documentation in GNU texinfo format
BuildArch:      noarch
Requires(post): info
Requires(preun): info

%description    info
XEmacs is a highly customizable open source text editor and
application development system.  It is protected under the GNU General
Public License and related to other versions of Emacs, in particular
GNU Emacs.  Its emphasis is on modern graphical user interface support
and an open software development model, similar to Linux.

This package contains XEmacs documentation in GNU texinfo format.

%package        devel
Summary:        Development files for XEmacs
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
XEmacs is a highly customizable open source text editor and
application development system.  It is protected under the GNU General
Public License and related to other versions of Emacs, in particular
GNU Emacs.  Its emphasis is on modern graphical user interface support
and an open software development model, similar to Linux.

This package contains XEmacs development support files.

%package        filesystem
Summary:        XEmacs filesystem layout
BuildArch:      noarch

%description    filesystem
XEmacs is a highly customizable open source text editor and
application development system.  It is protected under the GNU General
Public License and related to other versions of Emacs, in particular
GNU Emacs.  Its emphasis is on modern graphical user interface support
and an open software development model, similar to Linux.

This package contains directories that are required by other packages that
add functionality to XEmacs.

%prep
%autosetup -p0 -n %{name}-%{?snap:beta}%{!?snap:%{version}}
find . -type f -name "*.elc" -o -name "*.info*" -delete
sed -i -e /tetris/d lisp/menubar-items.el

sed -e 's/"lib"/"%{_lib}"/' lisp/setup-paths.el > lisp/setup-paths.el.new
touch -r lisp/setup-paths.el lisp/setup-paths.el.new
mv -f lisp/setup-paths.el.new lisp/setup-paths.el

for f in man/internals/internals.texi man/lispref/mule.texi man/xemacs-faq.texi CHANGES-beta
do
    iconv -f iso-8859-1 -t utf-8 -o $f.utf8 $f
    touch -r $f $f.utf8
    mv -f $f.utf8 $f
done

# Get reproducible builds by setting the compiling username
mkdir ~/.xemacs
echo >> ~/.xemacs/custom.el << EOF
(custom-set-variables
 '(user-mail-address "mockbuild@fedoraproject.org"))
EOF


%build
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CFLAGS
export EMACSLOADPATH=$PWD/lisp:$PWD/lisp/mule
export LDFLAGS="$RPM_LD_FLAGS -Wl,--as-needed"

# The --with-*dir args can probably go away in the future if/when upstream
# configure learns to honor standard autofoo dirs better.
common_options="
    --mandir=%{_mandir}/man1
    --with-archlibdir=%{_libdir}/xemacs-%{xver}/%{xbuild}
%if %{with modules}
    --with-moduledir=%{_libdir}/xemacs-%{xver}/%{xbuild}/modules
%endif
    --with-lispdir=%{_datadir}/xemacs-%{xver}/lisp
    --with-etcdir=%{_datadir}/xemacs-%{xver}/etc
    --with-system-packages=%{_datadir}/xemacs
    --without-msw
%if %{with mule}
    --with-mule
    --with-unicode-internal
    --without-canna
%endif
    --with-clash-detection
    --with-database=gdbm
    --with-ldap
    --without-postgresql
    --with-mail-locking=lockf
    --with-pop
    --without-hesiod
    --with-tls=openssl
    --with-pdump
%if ! %{with modules}
    --without-modules
%endif
    --with-debug
    --with-error-checking=none
    --enable-bignum=gmp
    --with-union-type
"

%if %{with nox}
# build without X
%configure $common_options \
    --with-docdir=%{_libdir}/xemacs-%{xver}/doc-nox \
    --with-sound=none \
    --with-xim=no \
    --without-wnn \
    --without-x
make EMACSDEBUGPATHS=yes # toplevel parallel make fails
mv lib-src/DOC{,-nox}
mv src/xemacs{,-nox-%{xver}}
mv lib-src/config.values{,-nox}
mv Installation{,-nox}
%endif

# build with Xft
%configure $common_options \
    --with-docdir=%{_libdir}/xemacs-%{xver}/doc-xft \
    --with-sound=nonative,alsa \
    --with-xft=all \
%if %{with gtk}
    --with-gtk \
    --with-gnome \
%else
    --with-athena=%{?with_xaw3d:3d}%{!?with_xaw3d:next} \
    --with-menubars=lucid \
    --with-widgets=athena \
    --with-dialogs=athena \
    --with-scrollbars=lucid \
    --with-xim=%{?with_xim:xlib}%{!?with_xim:no} \
%endif
%if ! %{with wnn}
    --without-wnn
%endif
make EMACSDEBUGPATHS=yes # toplevel parallel make fails
mv lib-src/DOC{,-xft}
mv src/xemacs{,-xft-%{xver}}
mv lib-src/config.values{,-xft}
mv Installation{,-xft}

# build with X
%configure $common_options \
    --with-docdir=%{_libdir}/xemacs-%{xver}/doc \
    --with-sound=nonative,alsa \
%if %{with xft}
    --with-xft=all \
%else
%if %{with xfs}
    --with-xfs \
%endif
%endif
%if %{with gtk}
    --with-gtk \
    --with-gnome \
%else
    --with-athena=%{?with_xaw3d:3d}%{!?with_xaw3d:next} \
    --with-menubars=lucid \
    --with-widgets=athena \
    --with-dialogs=athena \
    --with-scrollbars=lucid \
    --with-xim=%{?with_xim:xlib}%{!?with_xim:no} \
%endif
%if ! %{with wnn}
    --without-wnn
%endif

make EMACSDEBUGPATHS=yes # toplevel parallel make fails

cat << \EOF > xemacs.pc
prefix=%{_prefix}
%if %{with modules}
includedir=%{_libdir}/xemacs-%{xver}/%{xbuild}/include
sitemoduledir=%{_libdir}/xemacs/site-modules
%endif
sitestartdir=%{_datadir}/xemacs/site-packages/lisp/site-start.d
sitepkglispdir=%{_datadir}/xemacs/site-packages/lisp

Name: xemacs
Description: Different version of Emacs
Version: %{version}
%if %{with modules}
Cflags: -I${includedir}
%endif
EOF

cat > macros.xemacs << EOF
%%_xemacs_version %{majver}
%%_xemacs_ev %{?epoch:%{epoch}:}%{version}
%%_xemacs_evr %{?epoch:%{epoch}:}%{version}-%{release}
%%_xemacs_sitepkgdir %{_datadir}/xemacs/site-packages
%%_xemacs_sitelispdir %{_datadir}/xemacs/site-packages/lisp
%%_xemacs_sitestartdir %{_datadir}/xemacs/site-packages/lisp/site-start.d
%%_xemacs_bytecompile /usr/bin/xemacs -q -no-site-file -batch -eval '(push "." load-path)' -f batch-byte-compile
%if %{with modules}
%%_xemacs_includedir %{_libdir}/xemacs-%{xver}/%{xbuild}/include
%%_xemacs_sitemoduledir %{_libdir}/xemacs/site-modules
%endif
EOF

%install
%make_install

# Compress the .el files
find %{buildroot}%{_datadir}/xemacs-%{xver} -name \*.el -exec gzip --best {} \+

%if %{with nox}
# install nox files
echo ".so man1/xemacs.1" > $RPM_BUILD_ROOT%{_mandir}/man1/xemacs-nox.1
install -pm 755 src/xemacs-nox-%{xver} $RPM_BUILD_ROOT%{_bindir}
ln -s xemacs-nox-%{xver} $RPM_BUILD_ROOT%{_bindir}/xemacs-nox
install -dm 755 $RPM_BUILD_ROOT%{_libdir}/xemacs-%{xver}/doc-nox
install -pm 644 lib-src/DOC-nox \
    $RPM_BUILD_ROOT%{_libdir}/xemacs-%{xver}/doc-nox/DOC
install -pm 644 lib-src/config.values-nox \
    $RPM_BUILD_ROOT%{_libdir}/xemacs-%{xver}/doc-nox/config.values
%endif

# install xft files
echo ".so man1/xemacs.1" > $RPM_BUILD_ROOT%{_mandir}/man1/xemacs-xft.1
install -pm 755 src/xemacs-xft-%{xver} $RPM_BUILD_ROOT%{_bindir}
ln -s xemacs-xft-%{xver} $RPM_BUILD_ROOT%{_bindir}/xemacs-xft
install -dm 755 $RPM_BUILD_ROOT%{_libdir}/xemacs-%{xver}/doc-xft
install -pm 644 lib-src/DOC-xft \
    $RPM_BUILD_ROOT%{_libdir}/xemacs-%{xver}/doc-xft/DOC
install -pm 644 lib-src/config.values-xft \
    $RPM_BUILD_ROOT%{_libdir}/xemacs-%{xver}/doc-xft/config.values

# these clash with GNU Emacs
mv $RPM_BUILD_ROOT%{_bindir}/etags{,.xemacs}
rm -f $RPM_BUILD_ROOT%{_bindir}/{ctags,rcs-checkin,b2m}
mv $RPM_BUILD_ROOT%{_mandir}/man1/etags{,.xemacs}.1
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/ctags.1
rm -f $RPM_BUILD_ROOT%{_infodir}/{cl,widget}.info*

# these clash with other packages
rm -f $RPM_BUILD_ROOT%{_infodir}/info*
rm -f $RPM_BUILD_ROOT%{_infodir}/standards*
rm -f $RPM_BUILD_ROOT%{_infodir}/termcap*
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

desktop-file-install --mode=644 --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
    %{SOURCE2}

desktop-file-install --mode=644 --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
    %{SOURCE6}

# AppData file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata

# site-start.el
install -dm 755 \
    $RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/lisp/site-start.d
install -pm 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/lisp/site-start.el

# default.el
install -pm 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/lisp

# default user init file
install -Dpm 644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/skel/.xemacs/init.el

# icon
install -Dpm 644 etc/xemacs-icon.svg \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/xemacs.png

# macro file
install -Dpm 644 macros.xemacs $RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d/macros.%{name}

# Empty directories for external packages to use
mkdir -m 0755 $RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/etc
mkdir -m 0755 $RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/info
mkdir -m 0755 $RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/lib-src
mkdir -m 0755 $RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/man
mkdir -m 0755 $RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/pkginfo

# make sure nothing is 0400
chmod -R a+rX $RPM_BUILD_ROOT%{_prefix}
chmod a+x $RPM_BUILD_ROOT%{_datadir}/xemacs-%{xver}%{_sysconfdir}/xemacs-fe.sh

# clean up unneeded stuff (TODO: there's probably much more)
find $RPM_BUILD_ROOT%{_prefix} -name "*~" | xargs -r rm
rm $RPM_BUILD_ROOT%{_libdir}/xemacs-%{xver}/%{xbuild}/gzip-el.sh
rm $RPM_BUILD_ROOT{%{_bindir}/gnuattach,%{_mandir}/man1/gnuattach.1}
pushd $RPM_BUILD_ROOT%{_datadir}/xemacs-%{xver}/etc
rm -r InstallGuide tests XKeysymDB *.1
popd

# Generate file list and make site-packages lisp files config files.
# (Note: The double-quote before "(noreplace)" is only to work around
# a bug in rpm-spec-mode).
find $RPM_BUILD_ROOT \
  \( -path $RPM_BUILD_ROOT%{_datadir}/xemacs-%{xver} -o \
     -path $RPM_BUILD_ROOT%{_datadir}/xemacs-%{xver}/\* -o \
     -path $RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/lisp/\* \) -a \
  \( \( -type d -not -name site-start.d -fprintf base-files "%%%%dir /%%P\n" \) -o \
     \( -type f -path $RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/lisp/\*.el.gz -not -exec test -e {}c \; -fprintf base-files "%%%%config""(noreplace) /%%P\n" \) -o \
     \( -type f -fprintf base-files "/%%P\n" \) \)

install -Dpm 644 xemacs.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/xemacs.pc

%check
%make_build check


%post
%{_sbindir}/alternatives --install %{_bindir}/xemacs xemacs \
    %{_bindir}/xemacs-%{xver} 80

%postun
[ -e %{_bindir}/xemacs-%{xver} ] || \
%{_sbindir}/alternatives --remove xemacs %{_bindir}/xemacs-%{xver}

%post nox
%{_sbindir}/alternatives --install %{_bindir}/xemacs xemacs \
    %{_bindir}/xemacs-nox-%{xver} 40 || :

%postun nox
[ -e %{_bindir}/xemacs-nox-%{xver} ] || \
%{_sbindir}/alternatives --remove xemacs %{_bindir}/xemacs-nox-%{xver} || :

%post xft
%{_sbindir}/alternatives --install %{_bindir}/xemacs xemacs \
    %{_bindir}/xemacs-xft-%{xver} 40 || :

%postun xft
[ -e %{_bindir}/xemacs-xft-%{xver} ] || \
%{_sbindir}/alternatives --remove xemacs %{_bindir}/xemacs-xft-%{xver} || :

%post common
%{_sbindir}/alternatives --install %{_bindir}/etags etags \
    %{_bindir}/etags.xemacs 40 || :

%preun common
[ $1 -ne 0 ] || \
%{_sbindir}/alternatives --remove etags %{_bindir}/etags.xemacs || :


%files
%doc Installation
# gnuclient needs X libs, so not in -common
%{_bindir}/gnuclient
%{_bindir}/gnudoit
%ghost %{_bindir}/xemacs
%{_bindir}/xemacs-%{xver}
%{_libdir}/xemacs-%{xver}/doc/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/gnuclient.desktop
%{_datadir}/icons/hicolor/scalable/apps/xemacs.png
%{_mandir}/man1/gnuclient.1*
%{_mandir}/man1/gnudoit.1*

%if %{with nox}
%files nox
%doc Installation-nox
%ghost %{_bindir}/xemacs
%{_bindir}/xemacs-nox
%{_bindir}/xemacs-nox-%{xver}
%{_libdir}/xemacs-%{xver}/doc-nox/
%{_mandir}/man1/xemacs-nox.1*
%endif

%files xft
%doc Installation-xft
%ghost %{_bindir}/xemacs
%{_bindir}/xemacs-xft
%{_bindir}/xemacs-xft-%{xver}
%{_libdir}/xemacs-%{xver}/doc-xft/
%{_mandir}/man1/xemacs-xft.1*

%files common -f base-files
%doc INSTALL README PROBLEMS CHANGES-beta etc/NEWS etc/TUTORIAL
%license COPYING
%{_bindir}/etags.xemacs
%{_bindir}/ootags
%{_bindir}/xemacs-script
%dir %{_libdir}/xemacs-%{xver}/
%dir %{_libdir}/xemacs-%{xver}/%{xbuild}/
%{_libdir}/xemacs-%{xver}/%{xbuild}/[acdfghprsvwy]*
%{_libdir}/xemacs-%{xver}/%{xbuild}/m[am]*
%{_libdir}/xemacs-%{xver}/%{xbuild}/movemail
%if %{with modules}
%{_libdir}/xemacs/
%dir %{_libdir}/xemacs-%{xver}/%{xbuild}/modules/
%{_libdir}/xemacs-%{xver}/%{xbuild}/modules/auto-autoloads.el
%{_libdir}/xemacs-%{xver}/%{xbuild}/modules/auto-autoloads.elc
%{_libdir}/xemacs-%{xver}/%{xbuild}/modules/eldap.ell
%endif
%{_rpmconfigdir}/macros.d/macros.%{name}
%config(noreplace) %{_sysconfdir}/skel/.xemacs/
%{_mandir}/man1/etags.xemacs.1*
%{_mandir}/man1/gnuserv.1*
%{_mandir}/man1/xemacs.1*

%files info
%license COPYING
%{_infodir}/*.info*

%files devel
%if %{with modules}
%{_bindir}/ellcc
%{_libdir}/xemacs-%{xver}/%{xbuild}/include/
%endif
%{_libdir}/pkgconfig/xemacs.pc

%files filesystem
%dir %{_datadir}/xemacs
%dir %{_datadir}/xemacs/site-lisp
%dir %{_datadir}/xemacs/site-packages
%dir %{_datadir}/xemacs/site-packages/etc
%dir %{_datadir}/xemacs/site-packages/info
%dir %{_datadir}/xemacs/site-packages/lib-src
%dir %{_datadir}/xemacs/site-packages/lisp
%dir %{_datadir}/xemacs/site-packages/lisp/site-start.d
%dir %{_datadir}/xemacs/site-packages/man
%dir %{_datadir}/xemacs/site-packages/pkginfo

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.34-38.20200331hge2ac728aa576
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Jerry James <loganjerry@gmail.com> - 21.5.34-37.20200331hge2ac728aa576
- Update to latest mercurial snapshot for miscellaneous bug fixes
- Add -strsignal patch to fix build with latest glibc

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 21.5.34-36.20190323hgc0ed7ef9a5a1
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.34-35.20190323hgc0ed7ef9a5a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 28 2020 Jerry James <loganjerry@gmail.com> - 21.5.34-3420190323hgc0ed7ef9a5a1
- Replace libdb with gdbm
- Use pkgconfig BRs

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.34-34.20190323hgc0ed7ef9a5a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 21 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 21.5.34-33.20190323hgc0ed7ef9a5a1
- Obsolete -el subpackage
- Remove needless use of %%defattr
- Simplify generation of file list
- Enable test suite

* Thu Mar 21 2019 Jerry James <loganjerry@gmail.com> - 21.5.34-33.20190323hgc0ed7ef9a5a1
- Update to latest mercurial snapshot for miscellaneous bug fixes
- Switch from NSS to OpenSSL
- Build with openldap support
- Compress the Lisp source files

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.34-32.20171230hg92757c2b8239
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 14 2018 Peter Robinson <pbrobinson@fedoraproject.org> 21.5.34-31.20171230hg92757c2b8239
- Update alternatives dep

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.34-30.20171230hg92757c2b8239
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar  3 2018 Jerry James <loganjerry@gmail.com> - 21.5.34-29.20171230hg92757c2b8239
- Update to latest mercurial snapshot for miscellaneous bug fixes
- Remove obsolete scriptlets
- Drop upstreamed -endian, -gcpro, and -format-overflow patches
- Install a scalable icon

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 21.5.34-28.20171227hg27f66ce6ab71
- Rebuild (giflib)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.34-27.20171227hg27f66ce6ab71
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 28 2017 Jerry James <loganjerry@gmail.com> - 21.5.34-26.20171227hg27f66ce6ab71
- Update to latest mercurial snapshot for Unicode support
- Add -gcpro patch to fix FTBFS
- Add -overflow patch to fix possible bad code generation
- Add -data-start patch to fix FTBFS on ppc64/ppc64le
- Add -endian patch to fix FTBFS on ppc64/s390x

* Tue Nov 28 2017 Jerry James <loganjerry@gmail.com> - 21.5.34-26.20171125hg700dd03e6a31
- Update to latest mercurial snapshot for miscellaneous bug fixes
- Drop Canna support (bz 1517235)

* Sat Aug  5 2017 Jerry James <loganjerry@gmail.com> - 21.5.34-25.20170628hg97140cfdeca7
- Update to latest mercurial snapshot for miscellaneous bug fixes

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.34-24.20170124hgf412e9f093d4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.34-23.20170124hgf412e9f093d4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Jerry James <loganjerry@gmail.com> - 21.5.34-22.20170124hgf412e9f093d4
- Rebuild for NSS 3.29.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.34-21.20170124hgf412e9f093d4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Jerry James <loganjerry@gmail.com> - 21.5.34-20.20170124hgf412e9f093d4
- Update to latest mercurial snapshot to really fix bz 1408201
- Drop upstreamed -with-output-to-string patch

* Sat Jan 14 2017 Jerry James <loganjerry@gmail.com> - 21.5.34-19.20170114hg29e551281d78
- Update to latest mercurial snapshot (bz 1408201)
- Use glibc malloc on all platforms
- Add -with-output-to-string patch

* Tue Oct 18 2016 Jerry James <loganjerry@gmail.com> - 21.5.34-18.20161013hg39f002ba1b8c
- Update to latest mercurial snapshot

* Fri Jun  3 2016 Jerry James <loganjerry@gmail.com> - 21.5.34-17.20160603hga561e02bb626
- Update to fix NSS breakage
- Drop upstreamed -tls and -setsid patches

* Sat May 28 2016 Jerry James <loganjerry@gmail.com> - 21.5.34-16.20160507hgd5b51c618ef8
- Update to latest mercurial snapshot
- Fix M-x shell under tcsh (bz 1222897, 1260785)

* Sat Feb 20 2016 Jerry James <loganjerry@gmail.com> - 21.5.34-15.20160104hg4d03958b4080
- Update to latest mercurial snapshot

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.34-14.20150929hga76c9268bb72
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 30 2015 Michal Toman <mtoman@fedoraproject.org> - 21.5.34-13.20150929hga76c9268bb72
- Use system malloc on 32-bit MIPS (bz 1294893)

* Sat Oct  3 2015 Jerry James <loganjerry@gmail.com> - 21.5.34-12.20150929hga76c9268bb72
- Update to snapshot: fixes multiple bugs
- Add -alsaplay patch to fix playing sounds through ALSA

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21.5.34-11.20150420hg23178aa71f8b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 Jerry James <loganjerry@gmail.com> - 21.5.34-10.20150420hg23178aa71f8b
- Update to snapshot: fixes multiple bugs
- Drop upstreamed -c11 patch
- Enable NSS support

* Mon Feb  9 2015 Jerry James <loganjerry@gmail.com> - 21.5.34-9.20140605hgacf1c26e3019
- Add -c11 patch to fix build failure with gcc 5.0
- Set compiling username to get reproducible builds
- Use license macro

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21.5.34-8.20140605hgacf1c26e3019
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21.5.34-7.20140605hgacf1c26e3019
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun  5 2014 Jerry James <loganjerry@gmail.com> - 21.5.34-6.20140605hgacf1c26e3019
- Update to snapshot: fixes bz 1095405 and allows diagnosis of bz 1078159
- Update snapshot creating script to use bitbucket and maximally compress
- Don't need to exclude texinfo info files; upstream has dropped them

* Wed Feb  5 2014 Jerry James <loganjerry@gmail.com> - 21.5.34-5
- Disable XIM by default.  It hasn't worked since the release of Fedora 19 due
  to a fixed size buffer inside libX11 that is too small (see _XimProtoCreateIC
  in modules/im/ximcp/imDefIc.c), and nobody has complained.
- Update location of rpm macro file for rpm >= 4.11

* Tue Nov 12 2013 Jerry James <loganjerry@gmail.com> - 21.5.34-4
- Add an AppData file

* Fri Oct 25 2013 Jerry James <loganjerry@gmail.com> - 21.5.34-3
- Update the -utf8-fonts patch to remove more references to iso8859 fonts

* Wed Oct  2 2013 Jerry James <loganjerry@gmail.com> - 21.5.34-2
- Don't package the texinfo info files; they clash with texinfo 5.2

* Thu Aug 22 2013 Jerry James <loganjerry@gmail.com> - 21.5.34-1
- New upstream version
- Drop upstreamed -menubar, -aarch64, and -texinfo patches
- Drop unnecessary sed BR

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21.5.33-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 Jerry James <loganjerry@gmail.com> - 21.5.33-6
- Rebuild for libpng 1.6

* Mon Apr  8 2013 Jerry James <loganjerry@gmail.com> - 21.5.33-5
- Add -texinfo patch to fix problems with texinfo 5 (bz 923365)
- Add -aarch64 patch (bz 926766)
- Build with libdb version 5
- Emacs started shipping cl and widget info files, so we drop them

* Tue Feb  5 2013 Jerry James <loganjerry@gmail.com> - 21.5.33-4
- Update -menubar patch so :visible keyword is accepted in menus (bz 890565)

* Mon Jan 21 2013 Jerry James <loganjerry@gmail.com> - 21.5.33-3
- Add -menubar patch to fix bz 890565

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 21.5.33-2
- rebuild due to "jpeg8-ABI" feature drop

* Mon Jan  7 2013 Jerry James <loganjerry@gmail.com> - 21.5.33-1
- New upstream version
- Drop upstreamed view-mode patch

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 21.5.32-2
- rebuild against new libjpeg

* Mon Aug  6 2012 Jerry James <loganjerry@gmail.com> - 21.5.32-1
- New upstream version
- Drop upstreamed patches
- Running autoconf no longer necessary
- Drop conditionals for ancient versions of Fedora
- Package X versions of lib-src binaries to get gnuclient linked with -lXau

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21.5.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 21.5.31-4
- Rebuild for GCC 4.7
- Minor spec file cleanups

* Mon Nov  7 2011 Jerry James <loganjerry@gmail.com> - 21.5.31-3
- Rebuild with new libpng

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 21.5.31-2.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 21.5.31-2.1
- rebuild with new gmp

* Fri Aug  5 2011 Jerry James <loganjerry@gmail.com> - 21.5.31-2
- Build --with-union-type to avoid a make-int bug in lisp-disunion.h
- Add view-mode patch (bz 709399)
- Add get-other-frame patch from upstream
- Add lib-src patch to eliminate unnecessary linkage

* Tue May  3 2011 Jerry James <loganjerry@gmail.com> - 21.5.31-1
- Update to 21.5.31
- License is now GPLv3+
- Drop upstreamed patches: x-paths, image-overflow, no-xft, png, tty-font,
  etags-memmove, arabic, dired, infodir
- Rebase and renumber remaining patches
- Drop workaround for ancient alternatives bug

* Tue Mar  1 2011 Jerry James <loganjerry@gmail.com> - 21.5.29-18
- Make -filesystem subpackage be noarch.

* Tue Mar  1 2011 Jerry James <loganjerry@gmail.com> - 21.5.29-17
- Add filesystem subpackage (bz 672093).
- Add gnuclient desktop file.
- Fix CFLAGS so -fno-strict-aliasing actually gets used.
- Add . to the default load-path in _xemacs_bytecompile.
- Update Requires for pre/post(un) scripts.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21.5.29-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  1 2010 Jerry James <loganjerry@gmail.com> - 21.5.29-15
- Don't create /var/lock/xemacs; it is not used (bz 656723).
- Drop the BuildRoot tag.
- Ship COPYING with the -info subpackage.

* Wed Nov 10 2010 Jerry James <loganjerry@gmail.com> - 21.5.29-14
- Create and own subdirectories of site-packages

* Tue Jul  6 2010 Jerry James <loganjerry@gmail.com> - 21.5.29-13
- Add db4 support (bz 581614).
- Add -xft subpackage (bz 356961).
- Recognize Fedora's X server.

* Tue Mar  2 2010 Jerry James <loganjerry@gmail.com> - 21.5.29-12
- Remove the bitmap-fonts dependency.

* Thu Jan  7 2010 Jerry James <loganjerry@gmail.com> - 21.5.29-11
- New upstream patch for bz 547840.
- Add dired patch for large files (bz 550145).
- Replace "lzma" with "xz" for snapshots.

* Mon Dec 21 2009 Jerry James <loganjerry@gmail.com> - 21.5.29-10
- Don't crash with a Persian keyboard layout (bz 547840)

* Tue Dec  8 2009 Jerry James <loganjerry@gmail.com> - 21.5.29-9
- Add patch to use memmove in etags (bz 545399).

* Mon Nov  9 2009 Jerry James <loganjerry@gmail.com> - 21.5.29-8
- Move macros.xemacs to the -common subpackage (bz 533611).
- Updated TTY font patch from upstream.

* Tue Nov  3 2009 Jerry James <loganjerry@gmail.com> - 21.5.29-7
- Make the desktop file consistent with Emacs (bz 532296).

* Wed Oct 28 2009 Jerry James <loganjerry@gmail.com> - 21.5.29-6
- Bring back the courier font patch; that was a red herring.
- Really, seriously fix bz 512623 with a TTY font patch.
- Fix the version number in macros.xemacs.
- Build with bignum support.
- Turn off OSS support.

* Wed Sep 23 2009 Jerry James <loganjerry@gmail.com> - 21.5.29-5
- Final fix for bz 512623, which is actually two bugs, because ...
- ... the courier font patch breaks TTY font detection.  Removed that patch
  and Require bitmap-fonts to supply the original font name.
- Add macros.xemacs (bz 480546)
- Add png patch to fix a problem with reading PNG files

* Wed Aug 26 2009 Jerry James <loganjerry@gmail.com> - 21.5.29-4
- Use upstream's attempt at fixing #512623 instead of mine, which didn't work.

* Mon Aug 24 2009 Jerry James <loganjerry@gmail.com> - 21.5.29-3
- Fix image overflow bug (CVE-2009-2688).
- Fix calling xft-font-create-object in non-Xft builds (#512623).
- Rebase patches to eliminate fuzz/offsets.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21.5.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 20 2009 Ville Skyttä <ville.skytta at iki.fi> - 21.5.29-1
- Update to 21.5.29; gtk-gcc4, finder-lisp-dir, 3d-athena, autoconf262,
  doc-encodings, revert-modified, and xemacs-base-autoloads patches applied
  upstream.

* Thu Mar 12 2009 Ville Skyttä <ville.skytta at iki.fi> - 21.5.28-13
- Add possibility to build upstream hg snapshots.
- Add dependency on xorg-x11-fonts-misc (#478370, Carl Brune).
- Include Installation{,-nox} in docs.

* Sun Mar  8 2009 Ville Skyttä <ville.skytta at iki.fi> - 21.5.28-12
- Make XFontSet support optional at build time and disable it by default
  to work around #478370.

* Thu Feb 26 2009 Ville Skyttä <ville.skytta at iki.fi> - 21.5.28-11
- Apply upstream autoload changes to be able to build recent XEmacs packages.
- Make support for XIM optional at build time, still enabled by default.
- Drop support for building without stack protector compiler flags.
- Make -info subpackage noarch when built for Fedora >= 10.
- Improve icon cache and desktop database refresh scriptlets.
- Use %%global instead of %%define.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21.5.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jul 20 2008 Ville Skyttä <ville.skytta at iki.fi> - 21.5.28-9
- Rebuild.

* Sun Jul  6 2008 Ville Skyttä <ville.skytta at iki.fi> - 21.5.28-8
- Apply upstream fix for detection of 3D Athena widget sets.

* Sun Jul  6 2008 Ville Skyttä <ville.skytta at iki.fi> - 21.5.28-7
- Fix build with autoconf >= 2.62 (#449626).

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 21.5.28-6
- Autorebuild for GCC 4.3

* Fri Aug 17 2007 Ville Skyttä <ville.skytta at iki.fi> - 21.5.28-5
- Turn on syntax highlighting by default only if lazy-lock is available.
- Requires(post): coreutils in main package and -nox.
- Scriptlet cleanups.
- License: GPLv2+

* Sat Jun 30 2007 Ville Skyttä <ville.skytta at iki.fi> - 21.5.28-4
- Turn on syntax highlighting with lazy-lock by default.
- Drop Application and X-Fedora categories and Encoding from desktop entry.
- Move diff-switches default from skeleton init.el to site-start.el.

* Sun Jun 24 2007 Ville Skyttä <ville.skytta at iki.fi> - 21.5.28-3
- Apply upstream fix for #245017.

* Wed Jun  6 2007 Ville Skyttä <ville.skytta at iki.fi> - 21.5.28-2
- Set more dirs explicitly until upstream configure honors them better.
- Borrow DESTDIR install patch from openSUSE.
- Add pkgconfig file to -devel.

* Mon May 21 2007 Ville Skyttä <ville.skytta at iki.fi> - 21.5.28-1
- 21.5.28, module path fix applied upstream.
- Patch to retain courier as the default font.
- Fix some corrupt characters in docs.

* Fri May 18 2007 Ville Skyttä <ville.skytta at iki.fi> - 21.5.27-9
- Require one of the actual editor variants in -common.
- Require -common in -el, drop duplicate dir ownerships.

* Wed Jan 24 2007 Ville Skyttä <ville.skytta at iki.fi> - 21.5.27-8
- Fix canna_api.ell install/load paths (#222559).
- Fix site-start.el locale setup when the LANG env var is unset.

* Thu Jan  4 2007 Ville Skyttä <ville.skytta at iki.fi> - 21.5.27-7
- Don't run autoconf during build.

* Wed Jan  3 2007 Ville Skyttä <ville.skytta at iki.fi> - 21.5.27-6
- Fix site-start.el coding system setup in non-UTF8 locales (#213582).
- Fix "--without modules" build.

* Mon Oct  2 2006 Ville Skyttä <ville.skytta at iki.fi> - 21.5.27-5
- Rebuild.

* Wed Sep 20 2006 Ville Skyttä <ville.skytta at iki.fi> - 21.5.27-4
- Disable graphical progress bar by default (#188973).
- Make Wnn support optional at build time, disabled by default.

* Sun Sep 10 2006 Ville Skyttä <ville.skytta at iki.fi> - 21.5.27-3
- Adjust to split xemacs-packages-{base,extra}.
- Provide xemacs(bin) in main package and -nox.

* Sat Sep  2 2006 Ville Skyttä <ville.skytta at iki.fi> - 21.5.27-2
- Fix build when previous revision of the same XEmacs version is installed.
- BuildRequire compface-devel instead of compface.
- Turn error checking off.
- Specfile cleanups.

* Tue May 16 2006 Ville Skyttä <ville.skytta at iki.fi> - 21.5.27-1
- 21.5.27, maximize patch included upstream.
- Drop no longer needed find-paths patch.
- Fix alternatives setup.

* Sun May  7 2006 Ville Skyttä <ville.skytta at iki.fi> - 21.5.26-5
- Apply upstream fix for window maximization problems (#111225).

* Sun Apr 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 21.5.26-4
- Bring StartupWMClass in desktop entry up to date.
- Fix non-MULE build.

* Sat Apr 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 21.5.26-3
- Don't expect to find ellcc if building without modules (#188929).
- New --with/--without rpmbuild flags:
  - xft: enable/disable Xft support, default disabled.
  - nox: enable/disable building the non-X version, default enabled
  - modules: enable/disable module support, default arch-dependent.
- Re-enable XFontSet support for menubars for non-Xft builds (from openSUSE).
- Move gnuserv to -common, gnudoit to base package, drop gnuattach.
- Split ellcc and headers to -devel subpackage.
- Drop unneeded libXaw-devel build dependency.
- Move -nox "man page" to -nox subpackage.
- Fix GTK build and glade detection for it.
- Avoid -common dependency on ALSA.

* Thu Apr  6 2006 Ville Skyttä <ville.skytta at iki.fi> - 21.5.26-2
- Borrow Mike Fabian's site-start.el work from the SuSE package.

* Tue Apr  4 2006 Ville Skyttä <ville.skytta at iki.fi> - 21.5.26-1
- 21.5.26 (WIP).
- Make %%{_bindir}/xemacs an alternative (main/nox).
- Convert some info docs to UTF-8.

* Fri Mar 31 2006 Ville Skyttä <ville.skytta at iki.fi> - 21.5.25-1
- 21.5.25 (WIP).
- Trim pre-21.5 %%changelog entries.
