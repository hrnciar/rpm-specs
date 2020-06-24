########################################################################
# Top definitions from spectemplate-fonts-1-full.spec
########################################################################

Version: 4.48
Release: 7%{?dist}
URL:     http://terminus-font.sourceforge.net/

%global foundry           %{nil}
%global fontlicense       OFL
#
# The following directives are lists of space-separated shell globs
#   – matching files associated with the font family,
#   – as they exist in the build root,
#   — at the end of the %%build stage:
# – legal files (licensing…)
%global fontlicenses      OFL.txt
# – exclusions from the “fontlicenses” list
%global fontlicensesex    %{nil}
# – documentation files
%global fontdocs          README README-BG docs/README.fedora
# – exclusions from the “fontdocs” list
%global fontdocsex        %{fontlicenses}

%global fontfamily        terminus
%global fontsummary       Clean fixed width font
# A container for additional subpackage declarations.
%global fontpkgheader     %{expand:
#Obsoletes: 
}
#
# More shell glob lists:
# – font family files
%global fonts             Terminus.otb Terminus-Bold.otb
# – exclusions from the “fonts” list)
%global fontsex           %{nil}
# – fontconfig files
%global fontconfs         %{SOURCE10}
# – exclusions from the “fontconfs” list
%global fontconfsex       %{nil}
# – appstream files, if any (generated automatically otherwise)
%global fontappstreams    %{nil}
# – exclusions from the “fontappstreams” list
%global fontappstreamsex  %{nil}
#
%global fontdescription   %{expand:
The Terminus Font is a clean, fixed with bitmap font designed for long\
(8 and more hours per day) work with computers.\
\
I contains more than 1300 characters, covers about 120 language sets and\
supports ISO8859-1/2/5/7/9/13/15/16, Paratype-PT154/PT254, KOI8-R/U/E/F,\
Esperanto, and many IBM, Windows and Macintosh code pages, as well as\
the IBM VGA, vt100 and xterm pseudo graphic characters.\
\
The sizes present are 6x12, 8x14, 8x16, 10x18, 10x20, 11x22, 12x24,\
14x28, and 16x32. The weights are normal and bold (except for 6x12),\
plus CRT VGA-bold for 8x14 and 8x16.
}

########################################################################
# Local macro definitions (i.e. not from spectemplate-fonts-1-full.spec)
########################################################################

# The basename for upstream's source tarball
%global archivename terminus-font-%{version}

# This is the directory where we install our console fonts.
# Owned by the kbd package, which hardcodes it as /lib/kbd (without macros).
%global console_fontdir /lib/kbd/consolefonts

# The ExcludeArch from the grub2.spec file
#
# There might be a better way to detect whether this platform has
# grub2 available, but this should do the job at least for the time
# being.
%if 0%{?fedora} >= 29
%global grub2_exclude_arches s390 s390x
%else
%global grub2_exclude_arches s390 s390x %{arm}
%endif

# Owned by the grub2-common package
%global grub2_fontdir   /usr/share/grub

%global legacy_x11_fontdir   /usr/share/fonts/terminus-fonts-legacy-x11

# Font catalog
%global catalog %{_sysconfdir}/X11/fontpath.d

%if %{?epoch: 1}%{?!epoch: 0}
%global evr %{epoch}:%{version}-%{release}
%else
%global evr %{version}-%{release}
%endif


# From spectemplate-fonts-1-full.spec
Source0:  https://downloads.sourceforge.net/terminus-font/%{archivename}.tar.gz
Source10: 63-%{fontpkgname}.conf

# Local definitions
Source21:      %{name}-console-README.fedora
Source22:      %{name}-legacy-x11-README.fedora
Source23:      %{name}-Xresources.example
Source24:      %{name}-README.fedora

# For generating *.otb (OpenType bitmap font) files
Source42:      bitmapfonts2otb.py
Patch42:       %{name}-opentype-bitmap-via-fonttosfnt.patch
BuildRequires: /usr/bin/ftdump
BuildRequires: /usr/bin/fonttosfnt
BuildRequires: python3 > 3.5.0

# For generating legacy fonts (*.pcf)
BuildRequires: /usr/bin/bdftopcf
BuildRequires: /usr/bin/mkfontdir

%ifnarch %{grub2_exclude_arches}
BuildRequires: /usr/bin/grub2-mkfont
%endif


%fontpkg


%package console
Requires:   kbd
Summary:    Clean fixed width font (console version)
License:    OFL

%description console
%fontdescription
This package contains the fonts to use with the Linux console.


%ifnarch %{grub2_exclude_arches}
%package grub2
Requires:   grub2-common
Summary:    Clean fixed width font (grub2 version)
License:    OFL

%description grub2
%fontdescription
This package contains the fonts to use with the grub2 boot loader.
%endif


%package legacy-x11
Summary:    Clean fixed width font (legacy PCF version)
License:    OFL
# Require the fontconfig file
Requires:   %{name} = %{evr}

%description legacy-x11
%fontdescription
This package contains the font variants to use with software still
relying on legacy PCF font rendering methods (e.g. GNU Emacs 26).


%prep
%setup -q -n %{archivename}
# Convert upstream files to UTF-8 and Unix end of lines if necessary
# Optional arguments:
# -e [encoding] source OS encoding (auto-detected otherwise)
# -n            do not recode files, only adjust folding and end of lines
#linuxtext *.txt
cp -p "%{SOURCE42}" bin/
%patch42 -p1 -b .opentype-bitmap-via-fonttosfnt
patch -s -p1 -b --suffix .dv1 -fuzz=0 -i alt/dv1.diff
patch -s -p1 -b --suffix .ij1 -fuzz=0 -i alt/ij1.diff
iconv -f WINDOWS-1251 -t utf-8 -o README-BG README-BG


%build
./configure --prefix=%{_prefix} \
            --x11dir=%{legacy_x11_fontdir} --psfdir=%{console_fontdir}
env GZIP=--best make %{?_smp_mflags} PCF='$(PCF_10646_1) $(PCF_8BIT)' pcf psf psf-vgaw otb

%ifnarch %{grub2_exclude_arches}
# generate *.pf2 for the grub2 bootloader
for bdf in ter-*[bn].bdf; do
  /usr/bin/grub2-mkfont -o "$(basename "$bdf" .bdf).pf2" "$bdf"
done
%endif

# Fedora specific docs and examples
mkdir -p docs/console docs/legacy-x11
cp -p "%{SOURCE21}" docs/console/README.fedora
cp -p "%{SOURCE22}" docs/legacy-x11/README.fedora
cp -p "%{SOURCE23}" docs/legacy-x11/Xresources.example
cp -p "%{SOURCE24}" docs/README.fedora

%fontbuild


%install
make DESTDIR="%{buildroot}" PCF='$(PCF_10646_1) $(PCF_8BIT)' install-psf install-psf-ref install-psf-vgaw install-pcf

%ifnarch %{grub2_exclude_arches}
# install *.pf2 for the grub2 bootloader
install -m 0755 -d %{buildroot}%{grub2_fontdir}
install -m 0644 -t %{buildroot}%{grub2_fontdir} ter-*.pf2
%endif

# We cannot run mkfontdir in %%post because %%post is generated by %%_font_pkg
install -m 0755 -d %{buildroot}%{catalog}
ln -s %{legacy_x11_fontdir} %{buildroot}%{catalog}/%{fontfamily}:unscaled
/usr/bin/mkfontdir %{buildroot}%{legacy_x11_fontdir}

%fontinstall


%check
%fontcheck


%fontfiles


%files legacy-x11
%doc README
%doc docs/legacy-x11/README.fedora
%doc docs/legacy-x11/Xresources.example
%{catalog}/%{fontfamily}:unscaled
%dir %{legacy_x11_fontdir}/
%{legacy_x11_fontdir}/fonts.dir
%{legacy_x11_fontdir}/ter-112b.pcf.gz
%{legacy_x11_fontdir}/ter-112n.pcf.gz
%{legacy_x11_fontdir}/ter-114b.pcf.gz
%{legacy_x11_fontdir}/ter-114n.pcf.gz
%{legacy_x11_fontdir}/ter-116b.pcf.gz
%{legacy_x11_fontdir}/ter-116n.pcf.gz
%{legacy_x11_fontdir}/ter-118b.pcf.gz
%{legacy_x11_fontdir}/ter-118n.pcf.gz
%{legacy_x11_fontdir}/ter-120b.pcf.gz
%{legacy_x11_fontdir}/ter-120n.pcf.gz
%{legacy_x11_fontdir}/ter-122b.pcf.gz
%{legacy_x11_fontdir}/ter-122n.pcf.gz
%{legacy_x11_fontdir}/ter-124b.pcf.gz
%{legacy_x11_fontdir}/ter-124n.pcf.gz
%{legacy_x11_fontdir}/ter-128b.pcf.gz
%{legacy_x11_fontdir}/ter-128n.pcf.gz
%{legacy_x11_fontdir}/ter-132b.pcf.gz
%{legacy_x11_fontdir}/ter-132n.pcf.gz
%{legacy_x11_fontdir}/ter-212b.pcf.gz
%{legacy_x11_fontdir}/ter-212n.pcf.gz
%{legacy_x11_fontdir}/ter-214b.pcf.gz
%{legacy_x11_fontdir}/ter-214n.pcf.gz
%{legacy_x11_fontdir}/ter-216b.pcf.gz
%{legacy_x11_fontdir}/ter-216n.pcf.gz
%{legacy_x11_fontdir}/ter-218b.pcf.gz
%{legacy_x11_fontdir}/ter-218n.pcf.gz
%{legacy_x11_fontdir}/ter-220b.pcf.gz
%{legacy_x11_fontdir}/ter-220n.pcf.gz
%{legacy_x11_fontdir}/ter-222b.pcf.gz
%{legacy_x11_fontdir}/ter-222n.pcf.gz
%{legacy_x11_fontdir}/ter-224b.pcf.gz
%{legacy_x11_fontdir}/ter-224n.pcf.gz
%{legacy_x11_fontdir}/ter-228b.pcf.gz
%{legacy_x11_fontdir}/ter-228n.pcf.gz
%{legacy_x11_fontdir}/ter-232b.pcf.gz
%{legacy_x11_fontdir}/ter-232n.pcf.gz
%{legacy_x11_fontdir}/ter-512b.pcf.gz
%{legacy_x11_fontdir}/ter-512n.pcf.gz
%{legacy_x11_fontdir}/ter-514b.pcf.gz
%{legacy_x11_fontdir}/ter-514n.pcf.gz
%{legacy_x11_fontdir}/ter-516b.pcf.gz
%{legacy_x11_fontdir}/ter-516n.pcf.gz
%{legacy_x11_fontdir}/ter-518b.pcf.gz
%{legacy_x11_fontdir}/ter-518n.pcf.gz
%{legacy_x11_fontdir}/ter-520b.pcf.gz
%{legacy_x11_fontdir}/ter-520n.pcf.gz
%{legacy_x11_fontdir}/ter-522b.pcf.gz
%{legacy_x11_fontdir}/ter-522n.pcf.gz
%{legacy_x11_fontdir}/ter-524b.pcf.gz
%{legacy_x11_fontdir}/ter-524n.pcf.gz
%{legacy_x11_fontdir}/ter-528b.pcf.gz
%{legacy_x11_fontdir}/ter-528n.pcf.gz
%{legacy_x11_fontdir}/ter-532b.pcf.gz
%{legacy_x11_fontdir}/ter-532n.pcf.gz
%{legacy_x11_fontdir}/ter-712b.pcf.gz
%{legacy_x11_fontdir}/ter-712n.pcf.gz
%{legacy_x11_fontdir}/ter-714b.pcf.gz
%{legacy_x11_fontdir}/ter-714n.pcf.gz
%{legacy_x11_fontdir}/ter-716b.pcf.gz
%{legacy_x11_fontdir}/ter-716n.pcf.gz
%{legacy_x11_fontdir}/ter-718b.pcf.gz
%{legacy_x11_fontdir}/ter-718n.pcf.gz
%{legacy_x11_fontdir}/ter-720b.pcf.gz
%{legacy_x11_fontdir}/ter-720n.pcf.gz
%{legacy_x11_fontdir}/ter-722b.pcf.gz
%{legacy_x11_fontdir}/ter-722n.pcf.gz
%{legacy_x11_fontdir}/ter-724b.pcf.gz
%{legacy_x11_fontdir}/ter-724n.pcf.gz
%{legacy_x11_fontdir}/ter-728b.pcf.gz
%{legacy_x11_fontdir}/ter-728n.pcf.gz
%{legacy_x11_fontdir}/ter-732b.pcf.gz
%{legacy_x11_fontdir}/ter-732n.pcf.gz
%{legacy_x11_fontdir}/ter-912b.pcf.gz
%{legacy_x11_fontdir}/ter-912n.pcf.gz
%{legacy_x11_fontdir}/ter-914b.pcf.gz
%{legacy_x11_fontdir}/ter-914n.pcf.gz
%{legacy_x11_fontdir}/ter-916b.pcf.gz
%{legacy_x11_fontdir}/ter-916n.pcf.gz
%{legacy_x11_fontdir}/ter-918b.pcf.gz
%{legacy_x11_fontdir}/ter-918n.pcf.gz
%{legacy_x11_fontdir}/ter-920b.pcf.gz
%{legacy_x11_fontdir}/ter-920n.pcf.gz
%{legacy_x11_fontdir}/ter-922b.pcf.gz
%{legacy_x11_fontdir}/ter-922n.pcf.gz
%{legacy_x11_fontdir}/ter-924b.pcf.gz
%{legacy_x11_fontdir}/ter-924n.pcf.gz
%{legacy_x11_fontdir}/ter-928b.pcf.gz
%{legacy_x11_fontdir}/ter-928n.pcf.gz
%{legacy_x11_fontdir}/ter-932b.pcf.gz
%{legacy_x11_fontdir}/ter-932n.pcf.gz
%{legacy_x11_fontdir}/ter-c12b.pcf.gz
%{legacy_x11_fontdir}/ter-c12n.pcf.gz
%{legacy_x11_fontdir}/ter-c14b.pcf.gz
%{legacy_x11_fontdir}/ter-c14n.pcf.gz
%{legacy_x11_fontdir}/ter-c16b.pcf.gz
%{legacy_x11_fontdir}/ter-c16n.pcf.gz
%{legacy_x11_fontdir}/ter-c18b.pcf.gz
%{legacy_x11_fontdir}/ter-c18n.pcf.gz
%{legacy_x11_fontdir}/ter-c20b.pcf.gz
%{legacy_x11_fontdir}/ter-c20n.pcf.gz
%{legacy_x11_fontdir}/ter-c22b.pcf.gz
%{legacy_x11_fontdir}/ter-c22n.pcf.gz
%{legacy_x11_fontdir}/ter-c24b.pcf.gz
%{legacy_x11_fontdir}/ter-c24n.pcf.gz
%{legacy_x11_fontdir}/ter-c28b.pcf.gz
%{legacy_x11_fontdir}/ter-c28n.pcf.gz
%{legacy_x11_fontdir}/ter-c32b.pcf.gz
%{legacy_x11_fontdir}/ter-c32n.pcf.gz
%{legacy_x11_fontdir}/ter-d12b.pcf.gz
%{legacy_x11_fontdir}/ter-d12n.pcf.gz
%{legacy_x11_fontdir}/ter-d14b.pcf.gz
%{legacy_x11_fontdir}/ter-d14n.pcf.gz
%{legacy_x11_fontdir}/ter-d16b.pcf.gz
%{legacy_x11_fontdir}/ter-d16n.pcf.gz
%{legacy_x11_fontdir}/ter-d18b.pcf.gz
%{legacy_x11_fontdir}/ter-d18n.pcf.gz
%{legacy_x11_fontdir}/ter-d20b.pcf.gz
%{legacy_x11_fontdir}/ter-d20n.pcf.gz
%{legacy_x11_fontdir}/ter-d22b.pcf.gz
%{legacy_x11_fontdir}/ter-d22n.pcf.gz
%{legacy_x11_fontdir}/ter-d24b.pcf.gz
%{legacy_x11_fontdir}/ter-d24n.pcf.gz
%{legacy_x11_fontdir}/ter-d28b.pcf.gz
%{legacy_x11_fontdir}/ter-d28n.pcf.gz
%{legacy_x11_fontdir}/ter-d32b.pcf.gz
%{legacy_x11_fontdir}/ter-d32n.pcf.gz
%{legacy_x11_fontdir}/ter-f12b.pcf.gz
%{legacy_x11_fontdir}/ter-f12n.pcf.gz
%{legacy_x11_fontdir}/ter-f14b.pcf.gz
%{legacy_x11_fontdir}/ter-f14n.pcf.gz
%{legacy_x11_fontdir}/ter-f16b.pcf.gz
%{legacy_x11_fontdir}/ter-f16n.pcf.gz
%{legacy_x11_fontdir}/ter-f18b.pcf.gz
%{legacy_x11_fontdir}/ter-f18n.pcf.gz
%{legacy_x11_fontdir}/ter-f20b.pcf.gz
%{legacy_x11_fontdir}/ter-f20n.pcf.gz
%{legacy_x11_fontdir}/ter-f22b.pcf.gz
%{legacy_x11_fontdir}/ter-f22n.pcf.gz
%{legacy_x11_fontdir}/ter-f24b.pcf.gz
%{legacy_x11_fontdir}/ter-f24n.pcf.gz
%{legacy_x11_fontdir}/ter-f28b.pcf.gz
%{legacy_x11_fontdir}/ter-f28n.pcf.gz
%{legacy_x11_fontdir}/ter-f32b.pcf.gz
%{legacy_x11_fontdir}/ter-f32n.pcf.gz
%{legacy_x11_fontdir}/ter-g12b.pcf.gz
%{legacy_x11_fontdir}/ter-g12n.pcf.gz
%{legacy_x11_fontdir}/ter-g14b.pcf.gz
%{legacy_x11_fontdir}/ter-g14n.pcf.gz
%{legacy_x11_fontdir}/ter-g16b.pcf.gz
%{legacy_x11_fontdir}/ter-g16n.pcf.gz
%{legacy_x11_fontdir}/ter-g18b.pcf.gz
%{legacy_x11_fontdir}/ter-g18n.pcf.gz
%{legacy_x11_fontdir}/ter-g20b.pcf.gz
%{legacy_x11_fontdir}/ter-g20n.pcf.gz
%{legacy_x11_fontdir}/ter-g22b.pcf.gz
%{legacy_x11_fontdir}/ter-g22n.pcf.gz
%{legacy_x11_fontdir}/ter-g24b.pcf.gz
%{legacy_x11_fontdir}/ter-g24n.pcf.gz
%{legacy_x11_fontdir}/ter-g28b.pcf.gz
%{legacy_x11_fontdir}/ter-g28n.pcf.gz
%{legacy_x11_fontdir}/ter-g32b.pcf.gz
%{legacy_x11_fontdir}/ter-g32n.pcf.gz
%{legacy_x11_fontdir}/ter-i12b.pcf.gz
%{legacy_x11_fontdir}/ter-i12n.pcf.gz
%{legacy_x11_fontdir}/ter-i14b.pcf.gz
%{legacy_x11_fontdir}/ter-i14n.pcf.gz
%{legacy_x11_fontdir}/ter-i16b.pcf.gz
%{legacy_x11_fontdir}/ter-i16n.pcf.gz
%{legacy_x11_fontdir}/ter-i18b.pcf.gz
%{legacy_x11_fontdir}/ter-i18n.pcf.gz
%{legacy_x11_fontdir}/ter-i20b.pcf.gz
%{legacy_x11_fontdir}/ter-i20n.pcf.gz
%{legacy_x11_fontdir}/ter-i22b.pcf.gz
%{legacy_x11_fontdir}/ter-i22n.pcf.gz
%{legacy_x11_fontdir}/ter-i24b.pcf.gz
%{legacy_x11_fontdir}/ter-i24n.pcf.gz
%{legacy_x11_fontdir}/ter-i28b.pcf.gz
%{legacy_x11_fontdir}/ter-i28n.pcf.gz
%{legacy_x11_fontdir}/ter-i32b.pcf.gz
%{legacy_x11_fontdir}/ter-i32n.pcf.gz
%{legacy_x11_fontdir}/ter-k12b.pcf.gz
%{legacy_x11_fontdir}/ter-k12n.pcf.gz
%{legacy_x11_fontdir}/ter-k14b.pcf.gz
%{legacy_x11_fontdir}/ter-k14n.pcf.gz
%{legacy_x11_fontdir}/ter-k16b.pcf.gz
%{legacy_x11_fontdir}/ter-k16n.pcf.gz
%{legacy_x11_fontdir}/ter-k18b.pcf.gz
%{legacy_x11_fontdir}/ter-k18n.pcf.gz
%{legacy_x11_fontdir}/ter-k20b.pcf.gz
%{legacy_x11_fontdir}/ter-k20n.pcf.gz
%{legacy_x11_fontdir}/ter-k22b.pcf.gz
%{legacy_x11_fontdir}/ter-k22n.pcf.gz
%{legacy_x11_fontdir}/ter-k24b.pcf.gz
%{legacy_x11_fontdir}/ter-k24n.pcf.gz
%{legacy_x11_fontdir}/ter-k28b.pcf.gz
%{legacy_x11_fontdir}/ter-k28n.pcf.gz
%{legacy_x11_fontdir}/ter-k32b.pcf.gz
%{legacy_x11_fontdir}/ter-k32n.pcf.gz
%{legacy_x11_fontdir}/ter-p12b.pcf.gz
%{legacy_x11_fontdir}/ter-p12n.pcf.gz
%{legacy_x11_fontdir}/ter-p14b.pcf.gz
%{legacy_x11_fontdir}/ter-p14n.pcf.gz
%{legacy_x11_fontdir}/ter-p16b.pcf.gz
%{legacy_x11_fontdir}/ter-p16n.pcf.gz
%{legacy_x11_fontdir}/ter-p18b.pcf.gz
%{legacy_x11_fontdir}/ter-p18n.pcf.gz
%{legacy_x11_fontdir}/ter-p20b.pcf.gz
%{legacy_x11_fontdir}/ter-p20n.pcf.gz
%{legacy_x11_fontdir}/ter-p22b.pcf.gz
%{legacy_x11_fontdir}/ter-p22n.pcf.gz
%{legacy_x11_fontdir}/ter-p24b.pcf.gz
%{legacy_x11_fontdir}/ter-p24n.pcf.gz
%{legacy_x11_fontdir}/ter-p28b.pcf.gz
%{legacy_x11_fontdir}/ter-p28n.pcf.gz
%{legacy_x11_fontdir}/ter-p32b.pcf.gz
%{legacy_x11_fontdir}/ter-p32n.pcf.gz
%{legacy_x11_fontdir}/ter-u12b.pcf.gz
%{legacy_x11_fontdir}/ter-u12n.pcf.gz
%{legacy_x11_fontdir}/ter-u14b.pcf.gz
%{legacy_x11_fontdir}/ter-u14n.pcf.gz
%{legacy_x11_fontdir}/ter-u16b.pcf.gz
%{legacy_x11_fontdir}/ter-u16n.pcf.gz
%{legacy_x11_fontdir}/ter-u18b.pcf.gz
%{legacy_x11_fontdir}/ter-u18n.pcf.gz
%{legacy_x11_fontdir}/ter-u20b.pcf.gz
%{legacy_x11_fontdir}/ter-u20n.pcf.gz
%{legacy_x11_fontdir}/ter-u22b.pcf.gz
%{legacy_x11_fontdir}/ter-u22n.pcf.gz
%{legacy_x11_fontdir}/ter-u24b.pcf.gz
%{legacy_x11_fontdir}/ter-u24n.pcf.gz
%{legacy_x11_fontdir}/ter-u28b.pcf.gz
%{legacy_x11_fontdir}/ter-u28n.pcf.gz
%{legacy_x11_fontdir}/ter-u32b.pcf.gz
%{legacy_x11_fontdir}/ter-u32n.pcf.gz
%{legacy_x11_fontdir}/ter-x12b.pcf.gz
%{legacy_x11_fontdir}/ter-x12n.pcf.gz
%{legacy_x11_fontdir}/ter-x14b.pcf.gz
%{legacy_x11_fontdir}/ter-x14n.pcf.gz
%{legacy_x11_fontdir}/ter-x16b.pcf.gz
%{legacy_x11_fontdir}/ter-x16n.pcf.gz
%{legacy_x11_fontdir}/ter-x18b.pcf.gz
%{legacy_x11_fontdir}/ter-x18n.pcf.gz
%{legacy_x11_fontdir}/ter-x20b.pcf.gz
%{legacy_x11_fontdir}/ter-x20n.pcf.gz
%{legacy_x11_fontdir}/ter-x22b.pcf.gz
%{legacy_x11_fontdir}/ter-x22n.pcf.gz
%{legacy_x11_fontdir}/ter-x24b.pcf.gz
%{legacy_x11_fontdir}/ter-x24n.pcf.gz
%{legacy_x11_fontdir}/ter-x28b.pcf.gz
%{legacy_x11_fontdir}/ter-x28n.pcf.gz
%{legacy_x11_fontdir}/ter-x32b.pcf.gz
%{legacy_x11_fontdir}/ter-x32n.pcf.gz


%files console
%doc README
%doc README-BG
%doc docs/console/README.fedora
%doc %{console_fontdir}/README.terminus
# VGAW fonts
%{console_fontdir}/ter-114v.psf.gz
%{console_fontdir}/ter-116v.psf.gz
%{console_fontdir}/ter-214v.psf.gz
%{console_fontdir}/ter-216v.psf.gz
%{console_fontdir}/ter-714v.psf.gz
%{console_fontdir}/ter-716v.psf.gz
%{console_fontdir}/ter-914v.psf.gz
%{console_fontdir}/ter-916v.psf.gz
%{console_fontdir}/ter-c14v.psf.gz
%{console_fontdir}/ter-c16v.psf.gz
%{console_fontdir}/ter-d14v.psf.gz
%{console_fontdir}/ter-d16v.psf.gz
%{console_fontdir}/ter-g14v.psf.gz
%{console_fontdir}/ter-g16v.psf.gz
%{console_fontdir}/ter-h14v.psf.gz
%{console_fontdir}/ter-h16v.psf.gz
%{console_fontdir}/ter-i14v.psf.gz
%{console_fontdir}/ter-i16v.psf.gz
%{console_fontdir}/ter-k14v.psf.gz
%{console_fontdir}/ter-k16v.psf.gz
%{console_fontdir}/ter-m14v.psf.gz
%{console_fontdir}/ter-m16v.psf.gz
%{console_fontdir}/ter-p14v.psf.gz
%{console_fontdir}/ter-p16v.psf.gz
%{console_fontdir}/ter-u14v.psf.gz
%{console_fontdir}/ter-u16v.psf.gz
%{console_fontdir}/ter-v14v.psf.gz
%{console_fontdir}/ter-v16v.psf.gz
# normal and bold (non-VGAW specific) fonts
%{console_fontdir}/ter-112n.psf.gz
%{console_fontdir}/ter-114b.psf.gz
%{console_fontdir}/ter-114n.psf.gz
%{console_fontdir}/ter-116b.psf.gz
%{console_fontdir}/ter-116n.psf.gz
%{console_fontdir}/ter-118b.psf.gz
%{console_fontdir}/ter-118n.psf.gz
%{console_fontdir}/ter-120b.psf.gz
%{console_fontdir}/ter-120n.psf.gz
%{console_fontdir}/ter-122b.psf.gz
%{console_fontdir}/ter-122n.psf.gz
%{console_fontdir}/ter-124b.psf.gz
%{console_fontdir}/ter-124n.psf.gz
%{console_fontdir}/ter-128b.psf.gz
%{console_fontdir}/ter-128n.psf.gz
%{console_fontdir}/ter-132b.psf.gz
%{console_fontdir}/ter-132n.psf.gz
%{console_fontdir}/ter-212n.psf.gz
%{console_fontdir}/ter-214b.psf.gz
%{console_fontdir}/ter-214n.psf.gz
%{console_fontdir}/ter-216b.psf.gz
%{console_fontdir}/ter-216n.psf.gz
%{console_fontdir}/ter-218b.psf.gz
%{console_fontdir}/ter-218n.psf.gz
%{console_fontdir}/ter-220b.psf.gz
%{console_fontdir}/ter-220n.psf.gz
%{console_fontdir}/ter-222b.psf.gz
%{console_fontdir}/ter-222n.psf.gz
%{console_fontdir}/ter-224b.psf.gz
%{console_fontdir}/ter-224n.psf.gz
%{console_fontdir}/ter-228b.psf.gz
%{console_fontdir}/ter-228n.psf.gz
%{console_fontdir}/ter-232b.psf.gz
%{console_fontdir}/ter-232n.psf.gz
%{console_fontdir}/ter-712n.psf.gz
%{console_fontdir}/ter-714b.psf.gz
%{console_fontdir}/ter-714n.psf.gz
%{console_fontdir}/ter-716b.psf.gz
%{console_fontdir}/ter-716n.psf.gz
%{console_fontdir}/ter-718b.psf.gz
%{console_fontdir}/ter-718n.psf.gz
%{console_fontdir}/ter-720b.psf.gz
%{console_fontdir}/ter-720n.psf.gz
%{console_fontdir}/ter-722b.psf.gz
%{console_fontdir}/ter-722n.psf.gz
%{console_fontdir}/ter-724b.psf.gz
%{console_fontdir}/ter-724n.psf.gz
%{console_fontdir}/ter-728b.psf.gz
%{console_fontdir}/ter-728n.psf.gz
%{console_fontdir}/ter-732b.psf.gz
%{console_fontdir}/ter-732n.psf.gz
%{console_fontdir}/ter-912n.psf.gz
%{console_fontdir}/ter-914b.psf.gz
%{console_fontdir}/ter-914n.psf.gz
%{console_fontdir}/ter-916b.psf.gz
%{console_fontdir}/ter-916n.psf.gz
%{console_fontdir}/ter-918b.psf.gz
%{console_fontdir}/ter-918n.psf.gz
%{console_fontdir}/ter-920b.psf.gz
%{console_fontdir}/ter-920n.psf.gz
%{console_fontdir}/ter-922b.psf.gz
%{console_fontdir}/ter-922n.psf.gz
%{console_fontdir}/ter-924b.psf.gz
%{console_fontdir}/ter-924n.psf.gz
%{console_fontdir}/ter-928b.psf.gz
%{console_fontdir}/ter-928n.psf.gz
%{console_fontdir}/ter-932b.psf.gz
%{console_fontdir}/ter-932n.psf.gz
%{console_fontdir}/ter-c12n.psf.gz
%{console_fontdir}/ter-c14b.psf.gz
%{console_fontdir}/ter-c14n.psf.gz
%{console_fontdir}/ter-c16b.psf.gz
%{console_fontdir}/ter-c16n.psf.gz
%{console_fontdir}/ter-c18b.psf.gz
%{console_fontdir}/ter-c18n.psf.gz
%{console_fontdir}/ter-c20b.psf.gz
%{console_fontdir}/ter-c20n.psf.gz
%{console_fontdir}/ter-c22b.psf.gz
%{console_fontdir}/ter-c22n.psf.gz
%{console_fontdir}/ter-c24b.psf.gz
%{console_fontdir}/ter-c24n.psf.gz
%{console_fontdir}/ter-c28b.psf.gz
%{console_fontdir}/ter-c28n.psf.gz
%{console_fontdir}/ter-c32b.psf.gz
%{console_fontdir}/ter-c32n.psf.gz
%{console_fontdir}/ter-d12n.psf.gz
%{console_fontdir}/ter-d14b.psf.gz
%{console_fontdir}/ter-d14n.psf.gz
%{console_fontdir}/ter-d16b.psf.gz
%{console_fontdir}/ter-d16n.psf.gz
%{console_fontdir}/ter-d18b.psf.gz
%{console_fontdir}/ter-d18n.psf.gz
%{console_fontdir}/ter-d20b.psf.gz
%{console_fontdir}/ter-d20n.psf.gz
%{console_fontdir}/ter-d22b.psf.gz
%{console_fontdir}/ter-d22n.psf.gz
%{console_fontdir}/ter-d24b.psf.gz
%{console_fontdir}/ter-d24n.psf.gz
%{console_fontdir}/ter-d28b.psf.gz
%{console_fontdir}/ter-d28n.psf.gz
%{console_fontdir}/ter-d32b.psf.gz
%{console_fontdir}/ter-d32n.psf.gz
%{console_fontdir}/ter-g12n.psf.gz
%{console_fontdir}/ter-g14b.psf.gz
%{console_fontdir}/ter-g14n.psf.gz
%{console_fontdir}/ter-g16b.psf.gz
%{console_fontdir}/ter-g16n.psf.gz
%{console_fontdir}/ter-g18b.psf.gz
%{console_fontdir}/ter-g18n.psf.gz
%{console_fontdir}/ter-g20b.psf.gz
%{console_fontdir}/ter-g20n.psf.gz
%{console_fontdir}/ter-g22b.psf.gz
%{console_fontdir}/ter-g22n.psf.gz
%{console_fontdir}/ter-g24b.psf.gz
%{console_fontdir}/ter-g24n.psf.gz
%{console_fontdir}/ter-g28b.psf.gz
%{console_fontdir}/ter-g28n.psf.gz
%{console_fontdir}/ter-g32b.psf.gz
%{console_fontdir}/ter-g32n.psf.gz
%{console_fontdir}/ter-h12n.psf.gz
%{console_fontdir}/ter-h14b.psf.gz
%{console_fontdir}/ter-h14n.psf.gz
%{console_fontdir}/ter-h16b.psf.gz
%{console_fontdir}/ter-h16n.psf.gz
%{console_fontdir}/ter-h18b.psf.gz
%{console_fontdir}/ter-h18n.psf.gz
%{console_fontdir}/ter-h20b.psf.gz
%{console_fontdir}/ter-h20n.psf.gz
%{console_fontdir}/ter-h22b.psf.gz
%{console_fontdir}/ter-h22n.psf.gz
%{console_fontdir}/ter-h24b.psf.gz
%{console_fontdir}/ter-h24n.psf.gz
%{console_fontdir}/ter-h28b.psf.gz
%{console_fontdir}/ter-h28n.psf.gz
%{console_fontdir}/ter-h32b.psf.gz
%{console_fontdir}/ter-h32n.psf.gz
%{console_fontdir}/ter-i12n.psf.gz
%{console_fontdir}/ter-i14b.psf.gz
%{console_fontdir}/ter-i14n.psf.gz
%{console_fontdir}/ter-i16b.psf.gz
%{console_fontdir}/ter-i16n.psf.gz
%{console_fontdir}/ter-i18b.psf.gz
%{console_fontdir}/ter-i18n.psf.gz
%{console_fontdir}/ter-i20b.psf.gz
%{console_fontdir}/ter-i20n.psf.gz
%{console_fontdir}/ter-i22b.psf.gz
%{console_fontdir}/ter-i22n.psf.gz
%{console_fontdir}/ter-i24b.psf.gz
%{console_fontdir}/ter-i24n.psf.gz
%{console_fontdir}/ter-i28b.psf.gz
%{console_fontdir}/ter-i28n.psf.gz
%{console_fontdir}/ter-i32b.psf.gz
%{console_fontdir}/ter-i32n.psf.gz
%{console_fontdir}/ter-k12n.psf.gz
%{console_fontdir}/ter-k14b.psf.gz
%{console_fontdir}/ter-k14n.psf.gz
%{console_fontdir}/ter-k16b.psf.gz
%{console_fontdir}/ter-k16n.psf.gz
%{console_fontdir}/ter-k18b.psf.gz
%{console_fontdir}/ter-k18n.psf.gz
%{console_fontdir}/ter-k20b.psf.gz
%{console_fontdir}/ter-k20n.psf.gz
%{console_fontdir}/ter-k22b.psf.gz
%{console_fontdir}/ter-k22n.psf.gz
%{console_fontdir}/ter-k24b.psf.gz
%{console_fontdir}/ter-k24n.psf.gz
%{console_fontdir}/ter-k28b.psf.gz
%{console_fontdir}/ter-k28n.psf.gz
%{console_fontdir}/ter-k32b.psf.gz
%{console_fontdir}/ter-k32n.psf.gz
%{console_fontdir}/ter-m12n.psf.gz
%{console_fontdir}/ter-m14b.psf.gz
%{console_fontdir}/ter-m14n.psf.gz
%{console_fontdir}/ter-m16b.psf.gz
%{console_fontdir}/ter-m16n.psf.gz
%{console_fontdir}/ter-m18b.psf.gz
%{console_fontdir}/ter-m18n.psf.gz
%{console_fontdir}/ter-m20b.psf.gz
%{console_fontdir}/ter-m20n.psf.gz
%{console_fontdir}/ter-m22b.psf.gz
%{console_fontdir}/ter-m22n.psf.gz
%{console_fontdir}/ter-m24b.psf.gz
%{console_fontdir}/ter-m24n.psf.gz
%{console_fontdir}/ter-m28b.psf.gz
%{console_fontdir}/ter-m28n.psf.gz
%{console_fontdir}/ter-m32b.psf.gz
%{console_fontdir}/ter-m32n.psf.gz
%{console_fontdir}/ter-p12n.psf.gz
%{console_fontdir}/ter-p14b.psf.gz
%{console_fontdir}/ter-p14n.psf.gz
%{console_fontdir}/ter-p16b.psf.gz
%{console_fontdir}/ter-p16n.psf.gz
%{console_fontdir}/ter-p18b.psf.gz
%{console_fontdir}/ter-p18n.psf.gz
%{console_fontdir}/ter-p20b.psf.gz
%{console_fontdir}/ter-p20n.psf.gz
%{console_fontdir}/ter-p22b.psf.gz
%{console_fontdir}/ter-p22n.psf.gz
%{console_fontdir}/ter-p24b.psf.gz
%{console_fontdir}/ter-p24n.psf.gz
%{console_fontdir}/ter-p28b.psf.gz
%{console_fontdir}/ter-p28n.psf.gz
%{console_fontdir}/ter-p32b.psf.gz
%{console_fontdir}/ter-p32n.psf.gz
%{console_fontdir}/ter-u12n.psf.gz
%{console_fontdir}/ter-u14b.psf.gz
%{console_fontdir}/ter-u14n.psf.gz
%{console_fontdir}/ter-u16b.psf.gz
%{console_fontdir}/ter-u16n.psf.gz
%{console_fontdir}/ter-u18b.psf.gz
%{console_fontdir}/ter-u18n.psf.gz
%{console_fontdir}/ter-u20b.psf.gz
%{console_fontdir}/ter-u20n.psf.gz
%{console_fontdir}/ter-u22b.psf.gz
%{console_fontdir}/ter-u22n.psf.gz
%{console_fontdir}/ter-u24b.psf.gz
%{console_fontdir}/ter-u24n.psf.gz
%{console_fontdir}/ter-u28b.psf.gz
%{console_fontdir}/ter-u28n.psf.gz
%{console_fontdir}/ter-u32b.psf.gz
%{console_fontdir}/ter-u32n.psf.gz
%{console_fontdir}/ter-v12n.psf.gz
%{console_fontdir}/ter-v14b.psf.gz
%{console_fontdir}/ter-v14n.psf.gz
%{console_fontdir}/ter-v16b.psf.gz
%{console_fontdir}/ter-v16n.psf.gz
%{console_fontdir}/ter-v18b.psf.gz
%{console_fontdir}/ter-v18n.psf.gz
%{console_fontdir}/ter-v20b.psf.gz
%{console_fontdir}/ter-v20n.psf.gz
%{console_fontdir}/ter-v22b.psf.gz
%{console_fontdir}/ter-v22n.psf.gz
%{console_fontdir}/ter-v24b.psf.gz
%{console_fontdir}/ter-v24n.psf.gz
%{console_fontdir}/ter-v28b.psf.gz
%{console_fontdir}/ter-v28n.psf.gz
%{console_fontdir}/ter-v32b.psf.gz
%{console_fontdir}/ter-v32n.psf.gz


%ifnarch %{grub2_exclude_arches}
%files grub2
%doc README
%doc README-BG
%{grub2_fontdir}/ter-u12b.pf2
%{grub2_fontdir}/ter-u12n.pf2
%{grub2_fontdir}/ter-u14b.pf2
%{grub2_fontdir}/ter-u14n.pf2
%{grub2_fontdir}/ter-u16b.pf2
%{grub2_fontdir}/ter-u16n.pf2
%{grub2_fontdir}/ter-u18b.pf2
%{grub2_fontdir}/ter-u18n.pf2
%{grub2_fontdir}/ter-u20b.pf2
%{grub2_fontdir}/ter-u20n.pf2
%{grub2_fontdir}/ter-u22b.pf2
%{grub2_fontdir}/ter-u22n.pf2
%{grub2_fontdir}/ter-u24b.pf2
%{grub2_fontdir}/ter-u24n.pf2
%{grub2_fontdir}/ter-u28b.pf2
%{grub2_fontdir}/ter-u28n.pf2
%{grub2_fontdir}/ter-u32b.pf2
%{grub2_fontdir}/ter-u32n.pf2
%endif


%changelog
* Tue Jun  2 2020 Akira TAGOH <tagoh@redhat.com> - 4.48-7
- Workaround wrong weight in Terminus.otb in fontconfig config file.
  Resolves: rhbz#1823637

* Sat Apr 25 2020 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.48-6
- complete spec file rewrite based on spectemplate-fonts-1-full.spec
- split off legacy PCF files into -legacy-x11 subpackage

* Tue Apr  7 2020 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.48-5
- List *.otb files explicitly (without wildcards)
- Updated package descriptions and spec comments for more accuracy

* Wed Feb  5 2020 Peng Wu <pwu@redhat.com> - 4.48-4
- Use bitmapfonts2otb.py to combine bitmap fonts

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan  3 2020 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.48-2
- Stop shipping VGA fonts in grub subpackage
- Build OTB fonts for compatibility with pango >= 1.44 (#1748495)

* Tue Aug 27 2019 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.48-1
- Update to upstream release terminus-font-4.48
- Ship the Hebrew characters introduced by terminus-font-4.48

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.47-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.47-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 27 2019 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.47-4
- Only build -grub2 subpackage when arch/dist actually has grub2
- Address and silence rpmlint warnings

* Tue Jan 15 2019 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.47-3
- Update to upstream release terminus-font-4.47

* Tue Jan 15 2019 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.46-3
- Continue shipping the 8bit versions of *.pcf files (#1664054)

* Tue Dec 18 2018 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.46-2
- Add grub2 subpackage with *.pf2 fonts

* Tue Dec 18 2018 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.46-1
- Update to terminus-font-4.46

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.40-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.40-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.40-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.40-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.40-5
- Fix terminus-fonts-console README.fedora instructions on checking the initramfs.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.40-3
- Fix spelling issue in %%description
- iconv README-BG from WINDOWS-1251 to utf-8

* Sun Jan 17 2016 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.40-2
- Update to terminus-font-4.40 (#1095285)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 10 2014 Jens Petersen <petersen@redhat.com> - 4.39-1
- update to 4.39

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 28 2013 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.38-3
- Improve instructions for F18+ to console README.fedora (#1000491)

* Sat Nov 16 2013 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.38-2
- Add instructions for F18+ to terminus-fonts-console README.fedora (#1000491)

* Mon Sep 16 2013 Parag <paragn AT fedoraproject DOT org> - 4.38-1
- Update to new 4.38 version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 12 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.36-1
- Update to terminus-font-4.36

* Sat May 21 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.35-1
- Update to terminus-font-4.35
- Actually ship the size 18 fonts (upstream fix)

* Mon May  2 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.34-1
- Update to terminus-font-4.34
- Remove patch for alt/ge1.diff (4.34 uses ge1 by default)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb  1 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.32-1
- Update to 4.32

* Fri Jul 16 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.30-2
- Added License tag to -console subpackage.
- Added note about rebuilding initramfs after changing /etc/sysconfig/i18n.
- Changed URL, SourceN, PatchN to use new location at sourceforge.net.

* Fri Dec  4 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.30-1
- update to 4.30 release:
  - new size 22 (not very good)
  - 25 additional characters
  - various small fixes

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 25 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.28-8
- Rebuild for Fedora 11 to pick up font autodeps (#491973)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.28-6
- fix fontpackages-devel requirement to >= 1.18 (for _fontdir ownership)

* Fri Feb 20 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.28-5
- Add information to the fontconfig file
- no need to %%dir %%{_fontdir} in fontpackages-devel >= 1.20
- Use %%{_sysconfdir} instead of /etc
- Change all %%define instances to %%global
- Drop filesystem requirement for F-10 and later
- Use macro for common parts of descriptions
- Remove unneeded Provides:
- drop unnecessary comment

* Thu Feb 19 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.28-4
- change catalog(ue) spelling to US English
- remove unnecessary macro definition of %%tarname
- properly define consolefontdir (no macros)

* Thu Feb 19 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.28-3
- generate fonts.dir at build time (bug 483589)

* Wed Feb 18 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 4.28-2
- initial package for new Fedora Font Policy
