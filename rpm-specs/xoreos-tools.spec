Name:           xoreos-tools
Version:        0.0.5
Release:        4%{?dist}

Summary:        Tools to help the development of xoreos

# licensecheck suggests xoreos-tools is all GPLv3+; the only part that isn't
# is utf8cpp, which we're unbundling.
License:        GPLv3+

URL:            https://xoreos.org/
Source0:        https://github.com/xoreos/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++, glibc-devel
BuildRequires:  zlib-devel, libxml2-devel
BuildRequires:  libtool, gettext-devel, autoconf, automake

# Boost dependencies.
BuildRequires:  boost-devel, boost-system, boost-filesystem, boost-atomic,
BuildRequires:  boost-regex, boost-locale

# Use system utf8cpp rather than bundled copy.
BuildRequires:  utf8cpp-devel

%description
A collection of tools to help with the reverse-engineering of BioWare's
Aurora engine games. xoreos-tools is part of the xoreos project; please
see the xoreos website and its GitHub repositories for details,
especially the main README.md.

Currently, the following tools are included:

* gff2xml: Convert BioWare GFF to XML
* tlk2xml: Convert BioWare TLK to XML
* xml2tlk: Convert XML back to BioWare TLK
* convert2da: Convert BioWare 2DA/GDA to 2DA/CSV
* fixpremiumgff: Repair BioWare GFF files in NWN premium module HAKs
* unerf: Extract BioWare ERF archives
* unherf: Extract BioWare HERF archives
* unrim: Extract BioWare RIM archives
* unnds: Extract Nintendo DS roms
* unnsbtx: Extract Nintendo NSBTX textures into TGA images
* unkeybif: Extract BioWare KEY/BIF archives
* desmall: Decompress "small" (Nintendo DS LZSS, types 0x00 and 0x10) files
* xoreostex2tga: Convert BioWare's texture formats into TGA
* nbfs2tga: Convert Nintendo's raw NBFS images into TGA
* ncgr2tga: Convert Nintendo's NCGR images into TGA
* cbgt2tga: Convert CBGT images into TGA
* cdpth2tga: Convert CDPTH depth images into TGA
* ncsdis: Disassemble NWScript bytecode

%prep
%setup -q

# Remove bundled utf8.
rm -rf utf8cpp
sed '/utf8cpp/d' -i Makefile.am
sed '/utf8cpp/d' -i configure.ac
sed '/utf8cpp/d' -i rules.mk

# Change paths back.
sed 's,utf8cpp/,,g' -i src/common/*

%build
./autogen.sh
%configure

%make_build

%install
%make_install

# We'll get the documentation manually.
rm -rf %{buildroot}%{_docdir}/xoreos-tools

%check
%make_build check

%files

# Scripts.
%{_bindir}/erf
%{_bindir}/ssf2xml
%{_bindir}/xml2ssf
%{_bindir}/cbgt2tga
%{_bindir}/cdpth2tga
%{_bindir}/convert2da
%{_bindir}/desmall
%{_bindir}/fixpremiumgff
%{_bindir}/gff2xml
%{_bindir}/nbfs2tga
%{_bindir}/ncgr2tga
%{_bindir}/ncsdis
%{_bindir}/tlk2xml
%{_bindir}/unerf
%{_bindir}/unherf
%{_bindir}/unkeybif
%{_bindir}/unnds
%{_bindir}/unnsbtx
%{_bindir}/unrim
%{_bindir}/xml2tlk
%{_bindir}/xoreostex2tga

# man pages.
%{_mandir}/man1/erf.1*
%{_mandir}/man1/ssf2xml.1*
%{_mandir}/man1/xml2ssf.1*
%{_mandir}/man1/cbgt2tga.1*
%{_mandir}/man1/cdpth2tga.1*
%{_mandir}/man1/convert2da.1*
%{_mandir}/man1/desmall.1*
%{_mandir}/man1/fixpremiumgff.1.*
%{_mandir}/man1/gff2xml.1.*
%{_mandir}/man1/nbfs2tga.1.*
%{_mandir}/man1/ncgr2tga.1.*
%{_mandir}/man1/ncsdis.1.*
%{_mandir}/man1/tlk2xml.1.*
%{_mandir}/man1/unerf.1.*
%{_mandir}/man1/unherf.1.*
%{_mandir}/man1/unkeybif.1.*
%{_mandir}/man1/unnds.1.*
%{_mandir}/man1/unnsbtx.1.*
%{_mandir}/man1/unrim.1.*
%{_mandir}/man1/xml2tlk.1.*
%{_mandir}/man1/xoreostex2tga.1.*

%doc *.md AUTHORS ChangeLog TODO
%license COPYING

%changelog
* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 0.0.5-4
- Rebuilt for Boost 1.73

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 25 2019 Ben Rosser <rosser.bjr@gmail.com> - 0.0.5-2
- Enable test suite (rhbz#1764497).

* Sat Aug 31 2019 Ben Rosser <rosser.bjr@gmail.com> - 0.0.5-1
- Update to latest upstream release (rhbz#1637220).

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Ben Rosser <rosser.bjr@gmail.com> 0.0.4-2
- Remove spurious rm -rf of the buildroot from install section.
- Switch to make build/install macros.

* Mon Feb 15 2016 Ben Rosser <rosser.bjr@gmail.com> 0.0.4-1
- Initial package.
