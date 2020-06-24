# Run X11 tests
%{bcond_without perl_Prima_enables_x11_test}
# Support bidirectional text with FriBidi library
%{bcond_without perl_Prima_enables_fribidi}
# Use GTK2 file dialogs and fonts
%{bcond_without perl_Prima_enables_gtk2}
# Use HarfBuzz library for rendering a text
%{bcond_without perl_Prima_enables_harfbuzz}
# Support colorful cursor via Xcursor
%{bcond_without perl_Prima_enables_xcursor}
# Support FreeType fonts via xft
%{bcond_without perl_Prima_enables_xft}
# Support WebP image format
%{bcond_without perl_Prima_enables_wepb}

Name:           perl-Prima
Version:        1.59
Release:        2%{?dist}
Summary:        Perl graphic toolkit
# img/codec_jpeg.c:     EXIF parser is based on io-jpeg.c from gdk-pixbuf
#                       (LGPLv2+)
# img/imgscale.c:       Resizing filters are baes on magick/resize.c from
#                       ImageMagick (ImageMagick)
# include/unix/queue.h: BSD
# pod/prima-gencls.pod: BSD
# Prima.pm:             BSD
# Prima/PS/Unicode.pm:  BSD
# Copying:              BSD text
# LICENSE:              BSD text
# img/codec_X11.c:      MIT
# pod/Prima/Widget/place.pod:   TCL
# src/Drawable.c:               TCL
# examples/tiger.eps:   AGPLv3+   (bundled from GhostScript? CPAN RT#122271)
License:        BSD and MIT and TCL and ImageMagick and LGPLv2+ and AGPLv3+
URL:            https://metacpan.org/release/Prima
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KARASIK/Prima-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  giflib-devel
BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# pkgconfig is optional, but it provides better compiler options, so use it
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
%if %{with perl_Prima_enables_fribidi}
BuildRequires:  pkgconfig(fribidi)
%endif
%if %{with perl_Prima_enables_gtk2}
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.7
%endif
%if %{with perl_Prima_enables_harfbuzz}
BuildRequires:  pkgconfig(harfbuzz)
%endif
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
%if %{with perl_Prima_enables_wepb}
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(libwebpmux)
%endif
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
%if %{with perl_Prima_enables_xcursor}
BuildRequires:  pkgconfig(xcursor)
%endif
BuildRequires:  pkgconfig(xext)
%if %{with perl_Prima_enables_xft}
BuildRequires:  pkgconfig(xft)
%endif
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
# Getopt::Long not used at tests
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::RefHash)
# Optional run-time:
# gv not used at a tests
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(open)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
%if %{with perl_Prima_enables_x11_test}
# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  font(:lang=en)
# Tests exhibit a proportional font
BuildRequires:  liberation-sans-fonts
%endif
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Suggests:       gv
# Public modules without package keyword:
Provides:       perl(Prima::noARGV) = %{version}

%{?perl_default_filter}

# Do not export private modules (not starting with "Prima")
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\((am|apc|bi|bs|bt|ci|cl|cm|CodeEditor|cr|cs|CustomPodView|Divider|dmfp|dt|Editor|fdo|fds|fe|fp|fr|fra|frr|fs|fw|gm|gr|grow|gsci|gt|gui|ict|im|is|ItemsOutline|kb|km|le|lj|lp|mb|mbi|MenuOutline|MPropListViewer|mt|MyOutline|nt|PackPropListViewer|PropListViewer|rop|Round3D|sbmp|ss|sv|ta|tb|tka|tm|tno|tns|tw|wc|ws)\\)

# Filter under-specified provides
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Prima\\)$

%description
Prima is a general purpose extensible graphical user interface toolkit with
a rich set of standard widgets and an emphasis on 2D image processing tasks.
A Perl program using PRIMA looks and behaves identically on X, Win32.

%package Test
Summary:        Test tools for Prima Perl graphic toolkit
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description Test
This Perl module contains a small set or tool used for testing of
Prima-related code together with standard Perl Test:: suite.


%prep
%setup -q -n Prima-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 \
    OPTIMIZE="$RPM_OPT_FLAGS" \
    CYGWIN_WINAPI=0 \
    DEBUG=0 \
    VERBOSE=1 \
    WITH_FRIBIDI=%{with perl_Prima_enables_fribidi} \
    WITH_GTK2=%{with perl_Prima_enables_gtk2} \
    WITH_GTK3=0 \
    WITH_HARFBUZZ=%{with perl_Prima_enables_harfbuzz} \
    WITH_ICONV=1 \
    WITH_OPENMP=1 \
    WITH_XFT=%{with perl_Prima_enables_xft}
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset DISPLAY XDG_SESSION_TYPE
%if %{with perl_Prima_enables_x11_test}
    xvfb-run -d make test
%else
    make test
%endif

%files
%license Copying LICENSE AGPLv3
# "examples" directory is installed into perl_vendorarch
%doc Changes README.md
%{_bindir}/*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/prima-gencls.pod
%{perl_vendorarch}/Prima*
%exclude %{perl_vendorarch}/Prima/Stress.*
%exclude %{perl_vendorarch}/Prima/Test.*
%{_mandir}/man1/*
%{_mandir}/man3/*
%exclude %{_mandir}/man3/Prima::Stress.*
%exclude %{_mandir}/man3/Prima::Test.*

%files Test
%{perl_vendorarch}/Prima/Stress.*
%{perl_vendorarch}/Prima/Test.*
%{_mandir}/man3/Prima::Stress.*
%{_mandir}/man3/Prima::Test.*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.59-2
- Perl 5.32 rebuild

* Fri Jun 05 2020 Petr Pisar <ppisar@redhat.com> - 1.59-1
- 1.59 bump

* Mon Mar 16 2020 Petr Pisar <ppisar@redhat.com> - 1.58-1
- 1.58 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Petr Pisar <ppisar@redhat.com> - 1.57-1
- 1.57 bump
- Fix alpha calculation in ropMultiply
- Fix color resampling on big-endian machines (CPAN RT#131016)
- Fix underscore location in a menu
- Fix text baseline

* Wed Aug 21 2019 Petr Pisar <ppisar@redhat.com> - 1.56-1
- 1.56 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.55-2
- Perl 5.30 rebuild

* Mon Mar 25 2019 Petr Pisar <ppisar@redhat.com> - 1.55-1
- 1.55 bump

* Mon Feb 04 2019 Petr Pisar <ppisar@redhat.com> - 1.54-1
- 1.54 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.53-1
- 1.53 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.52-6
- Perl 5.28 rebuild

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 1.52-5
- Rebuild (giflib)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Petr Pisar <ppisar@redhat.com> - 1.52-1
- 1.52 bump
- License changed to "BSD and MIT and TCL and ImageMagick and LGPLv2+ and
  AGPLv3+"

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-2
- Perl 5.26 rebuild

* Wed Apr 26 2017 Petr Pisar <ppisar@redhat.com> - 1.51-1
- 1.51 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Petr Pisar <ppisar@redhat.com> - 1.50-1
- 1.50 bump

* Thu Sep 29 2016 Petr Pisar <ppisar@redhat.com> - 1.49-1
- 1.49 bump

* Fri Sep 02 2016 Petr Pisar <ppisar@redhat.com> - 1.48-1
- 1.48 bump

* Mon Jun 06 2016 Petr Pisar <ppisar@redhat.com> - 1.47-1
- 1.47 bump
- License changed to "BSD and MIT and TCL and ImageMagick and LGPLv2+"

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.46-3
- Perl 5.24 rebuild

* Mon Mar 21 2016 Petr Pisar <ppisar@redhat.com> - 1.46-2
- Fix bars on big endian (bug #1318734)

* Thu Mar 17 2016 Petr Pisar <ppisar@redhat.com> - 1.46-1
- 1.46 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Petr Pisar <ppisar@redhat.com> - 1.45-1
- 1.45 bump

* Wed Aug 05 2015 Petr Pisar <ppisar@redhat.com> - 1.44-1
- 1.44 bump

* Tue Jun 23 2015 Petr Pisar <ppisar@redhat.com> - 1.43-4
- Build-require open Perl module (bug #1234731)
- Replace dependency on glibc-headers with gcc (bug #1230488)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.43-2
- Perl 5.22 rebuild

* Mon Apr 13 2015 Petr Pisar <ppisar@redhat.com> - 1.43-1
- 1.43 bump

* Mon Mar 16 2015 Petr Pisar <ppisar@redhat.com> - 1.42-2
- Provide perl(Prima::noX11)

* Thu Mar 12 2015 Petr Pisar <ppisar@redhat.com> - 1.42-1
- 1.42 bump

* Wed Nov 12 2014 Petr Pisar <ppisar@redhat.com> - 1.41-1
- 1.41 bump

* Fri Sep 19 2014 Petr Pisar <ppisar@redhat.com> - 1.40-1
- 1.40 bump

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.37-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 26 2013 Petr Pisar <ppisar@redhat.com> 1.37-1
- Specfile autogenerated by cpanspec 1.78.
