Name:            unifont
Version:         12.0.01
Release:         3%{?dist}
License:         GPLv2+ and GFDL
Url:             https://savannah.gnu.org/projects/unifont
Summary:         Tools and glyph descriptions in a very simple text format

Source0:         https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:         unifont.metainfo.xml

BuildRequires:   gcc
BuildRequires:   perl-generators
BuildRequires:   xorg-x11-font-utils
BuildRequires:   fontforge
BuildRequires:   fontpackages-devel
BuildRequires:   texinfo

%description
A font with a glyph for every visible Unicode Basic Multilingual Plane
code point and more, with supporting utilities to modify the
font. This package contains tools and glyph descriptions.

%package fonts
BuildArch: noarch
Summary: Unicode font with a glyph for every visible BMP code point

Requires:        fontpackages-filesystem

%description fonts
A fixed-width Unicode font with a glyph for every visible Unicode 7.0
Basic Multilingual Plane code point (over 55,000 glyphs) and some
glyphs beyond BMP.

This font strives for very wide coverage rather than beauty, so use it
only as fallback or for special purposes.

%package viewer
BuildArch: noarch
Summary: Graphical viewer for unifont

%description viewer
A graphical viewer for unifont.

%prep
%setup -q -n unifont-%{version}
# Disable rebuilding during installation
sed -i 's/^install: .*/install:/' Makefile
sed -i 's/install -s/install/' src/Makefile

%build
# Makefile is broken with parallel builds
make CFLAGS='%{optflags}'
make -C doc unifont.info

%install
%make_install USRDIR=/usr COMPRESS=0 TTFDEST='$(DESTDIR)/usr/share/fonts/unifont'
find %{buildroot}/usr/share/unifont/ -type f \! -name %{name}.hex -delete
rm -rv %{buildroot}/usr/share/fonts/X11
rm -v %{buildroot}%{_fontdir}/*sample*
rm -v %{buildroot}%{_fontdir}/unifont_*csur*.ttf
install -Dm0644 doc/unifont.info %{buildroot}%{_infodir}/unifont.info
install -Dm0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/unifont.metainfo.xml
# Remove APL font for now
rm %{buildroot}/usr/share/consolefonts/Unifont-APL8x16.psf.gz

%files
%{_bindir}/*
%{_datadir}/%{name}/
%doc NEWS README
%license COPYING
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_infodir}/unifont.*
%exclude %{_bindir}/unifont-viewer

%_font_pkg *.ttf
%{_datadir}/appdata/
%license COPYING

%files viewer
%{_bindir}/unifont-viewer
%license COPYING

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 12.0.01-1
- Update to latest version (more glyphs from Unicode 12.0).

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 15 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 10.0.07-1
- Update to latest version (#1567644)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 9.0.06-1
- Uupdate to latest version (removal of serifs from Cherokee letters,
  Pikto CSUR glyph improvements)

* Sun Sep 11 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 9.0.02-1
- Update to latest version (3 new CSUR scripts, bugfixes)

* Sun Jul  3 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 9.0.01-1
- Update to latest version (increased coverage for Unicode 9.0)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 24 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 7.0.06-1
- Update to new upstream version
- Include unifont_upper.ttf in the package

* Thu Oct 16 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 7.0.04-2
- Add metadata file for the font, not appdata

* Wed Oct 15 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 7.0.04-1
- Update to new upstream version
- Add appdata file for the font

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 01 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 7.0.03-1
- Update to new upstream version

* Mon Jun 30 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 7.0.02-1
- Update to new upstream version

* Sun Jun 22 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 7.0.01-1
- Update to new upstream version
- Split out unifont-viewer subpackage

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3.20140214-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 07 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.3.20140214-1
- Update to new upstream version
- License for info files is changed to GFDL

* Fri Feb 07 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.3.20140204-1
- Update to new upstream version

* Sun Feb 02 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.3.20140202-1
- Update to new upstream version

* Sat Dec 28 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.3.20131221-2
- Move BR: fontpackages-devel to -fonts not to the main package

* Fri Dec 27 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.3.20131221-1
- Update to new upstream version

* Thu Dec 05 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.3.20131020-4
- Do not strip binaries during installation

* Thu Dec 05 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.3.20131020-3
- Fix build flags

* Sun Dec 01 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.3.20131020-2
- Add missing BuildRequires

* Sun Dec 01 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.3.20131020-1
- Initial package
