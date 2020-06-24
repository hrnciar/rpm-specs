# Testing note: According to upstream, the successful generation of
# tthdynamic.c and ttmdynamic.c IS a test.  We do that in %%build.

Name:           tth
Version:        4.12
Release:        7%{?dist}
Summary:        TeX to HTML/MathML translators

License:        GPLv2
URL:            http://hutchinson.belmont.ma.us/tth/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}%{version}.tar.gz
# Header file created by Jerry James from the source code.  It therefore has
# the same copyright and license as tth itself.
Source1:        tth.h
# Avoid buffer underflow
Patch0:         %{name}-buffer-underflow.patch

BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  netpbm-progs
BuildRequires:  tex(color.sty)
BuildRequires:  tex(epsfig.sty)
BuildRequires:  tex(fullpage.sty)
BuildRequires:  tex(graphicx.sty)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(language.dat)
BuildRequires:  tex(makeidx.sty)
BuildRequires:  tex(manfnt.tfm)
BuildRequires:  tex(natbib.sty)
BuildRequires:  tex-bibtex
BuildRequires:  tex-cm
BuildRequires:  tex-dvips
BuildRequires:  tex-ec
BuildRequires:  tex-gsftopk
BuildRequires:  tex-latex-bin
BuildRequires:  tex-makeindex
BuildRequires:  tex-mfware
BuildRequires:  tex-updmap-map

Requires:       coreutils
Requires:       ghostscript
Requires:       netpbm-progs
Requires:       tex(color.sty)
Requires:       tex(epsfig.sty)
Requires:       tex(fullpage.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(language.dat)
Requires:       tex(makeidx.sty)
Requires:       tex(manfnt.tfm)
Requires:       tex(natbib.sty)
Requires:       tex-bibtex
Requires:       tex-cm
Requires:       tex-dvips
Requires:       tex-ec
Requires:       tex-gsftopk
Requires:       tex-helvetic
Requires:       tex-latex-bin
Requires:       tex-makeindex
Requires:       tex-mfware
Requires:       tex-rsfs
Requires:       tex-symbol
Requires:       tex-tex
Requires:       tex-times
Requires:       tex-updmap-map
Requires:       %{name}-tex = %{version}-%{release}

%description
TTH translates TeX, the predominant mark-up language for expressing
mathematics, into HTML, the language of world-wide-web browsers.  It
thereby enables mathematical documents to be made available on the web.
Document structure, using either the Plain or LaTeX macro packages, is
also translated and incorporated in the form of hyperlinks.

TTH is extremely fast and completely portable.  It produces more
compact, faster viewing, web documents than other converters, because it
really translates the equations, instead of converting them to images.

%package tex
Summary:        (La)TeX style files for TTH
BuildArch:      noarch
Requires:       texlive-base

%description tex
(La)TeX style files used by TTH.

%package libs
Summary:        TeX to HTML/MathML translation libraries
Requires:       coreutils
Requires:       ghostscript-core
Requires:       netpbm-progs
Requires:       tex(color.sty)
Requires:       tex(epsfig.sty)
Requires:       tex(fullpage.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(natbib.sty)
Requires:       tex-bibtex
Requires:       tex-cm
Requires:       tex-dvips
Requires:       tex-helvetic
Requires:       tex-latex-bin
Requires:       tex-makeindex
Requires:       tex-rsfs
Requires:       tex-symbol
Requires:       tex-tex
Requires:       tex-times
Requires:       %{name}-tex = %{version}-%{release}

%description libs
Development files for building applications that use TTH.

%package devel
Summary:        Development files for TTH
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development files for building applications that use TTH.

%prep
%autosetup -n %{name} -p1

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Fix a couple of minor warnings
sed -i.orig 's/^main/int &/;/slen/d' tools/tthsplit.c
fixtimestamp tools/tthsplit.c
sed -i.orig 's/^main/#include <stdio.h>\nint &/;/slen/d' tools/choice.c
fixtimestamp tools/choice.c
sed -i.orig 's/^main/#include <stdlib.h>\nint &/;/slen/d' tthgold/tthrfcat.c
fixtimestamp tthgold/tthrfcat.c

# Remove prebuilt binaries
find . -name \*.exe -delete

# Do not try to build with mingw tools
sed -i '/^all/s/\.exe//g' tools/makefile

%build
# The makefiles don't allow for specifying compiler flags, so build manually
make %{?_smp_mflags} tth.c ttm.c
gcc $RPM_OPT_FLAGS $RPM_LD_FLAGS -D_FILE_OFFSET_BITS=64 tth.c -o tth
gcc $RPM_OPT_FLAGS $RPM_LD_FLAGS -D_FILE_OFFSET_BITS=64 ttm.c -o ttm
pushd tools
gcc $RPM_OPT_FLAGS $RPM_LD_FLAGS -D_FILE_OFFSET_BITS=64 choice.c -o choice
gcc $RPM_OPT_FLAGS $RPM_LD_FLAGS -D_FILE_OFFSET_BITS=64 tthsplit.c -o tthsplit
popd
pushd tthfunc
make %{?_smp_mflags} tthdynamic.c tthfunc.c ttmdynamic.c ttmfunc.c
gcc $RPM_OPT_FLAGS $RPM_LD_FLAGS -D_FILE_OFFSET_BITS=64 -fPIC -shared \
    -Wl,-h,libtth.so.0 tthfunc.c -o libtth.so.0.0.0
ln -s libtth.so.0.0.0 libtth.so.0
ln -s libtth.so.0 libtth.so
gcc $RPM_OPT_FLAGS $RPM_LD_FLAGS -D_FILE_OFFSET_BITS=64 -fPIC -shared \
    -Wl,-h,libttm.so.0 ttmfunc.c -o libttm.so.0.0.0
ln -s libttm.so.0.0.0 libttm.so.0
ln -s libttm.so.0 libttm.so
gcc $RPM_OPT_FLAGS $RPM_LD_FLAGS -D_FILE_OFFSET_BITS=64 calltthfunc.c \
    -o calltthfunc -L . -ltth
gcc $RPM_OPT_FLAGS $RPM_LD_FLAGS -D_FILE_OFFSET_BITS=64 callttmfunc.c \
    -o callttmfunc -L . -lttm
popd
pushd tthgold
gcc $RPM_OPT_FLAGS $RPM_LD_FLAGS -D_FILE_OFFSET_BITS=64 tthrfcat.c -o tthrfcat
popd

# Build the manual.  Allow makeindex to write to non-cwd.
export openout_any=r
make manual

%install
# Install the binaries
mkdir -p %{buildroot}%{_bindir}
install -m 0755 -p \
  tools/{latex2gif,ps2gif,ps2gif_transparent,ps2png,tthsplit} \
  tthgold/{tthprep,tthrfcat} \
  tth ttm \
  %{buildroot}%{_bindir}
install -m 0755 -p tools/numbering %{buildroot}%{_bindir}/tth-numbering
install -m 0755 -p tools/structure %{buildroot}%{_bindir}/tth-structure

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
cp -p tth.1 %{buildroot}%{_mandir}/man1
cat > %{buildroot}%{_mandir}/man1/ttm.1 << EOF
.so man1/tth.1
EOF
cp -p %{buildroot}%{_mandir}/man1/ttm.1 %{buildroot}%{_mandir}/man1/latex2gif.1
cp -p %{buildroot}%{_mandir}/man1/ttm.1 %{buildroot}%{_mandir}/man1/ps2gif.1
cp -p %{buildroot}%{_mandir}/man1/ttm.1 \
      %{buildroot}%{_mandir}/man1/ps2gif_transparent.1
cp -p %{buildroot}%{_mandir}/man1/ttm.1 %{buildroot}%{_mandir}/man1/ps2png.1

# Install the libraries
mkdir -p %{buildroot}%{_libdir}
install -m 0755 -p tthfunc/libtth.so.0.0.0 tthfunc/libttm.so.0.0.0 \
  %{buildroot}%{_libdir}
ln -s libtth.so.0.0.0 %{buildroot}%{_libdir}/libtth.so.0
ln -s libtth.so.0 %{buildroot}%{_libdir}/libtth.so
ln -s libttm.so.0.0.0 %{buildroot}%{_libdir}/libttm.so.0
ln -s libttm.so.0 %{buildroot}%{_libdir}/libttm.so

# Install the header
mkdir -p %{buildroot}%{_includedir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_includedir}

# Install the style files
mkdir -p %{buildroot}%{_texmf_main}/tex/generic/%{name}
cp -p tthgold/tth*.sty %{buildroot}%{_texmf_main}/tex/generic/%{name}

%files
%doc CHANGES README *.gif *.png manual/*.html manual/split
%{_bindir}/latex2gif
%{_bindir}/ps2gif
%{_bindir}/ps2gif_transparent
%{_bindir}/ps2png
%{_bindir}/tth
%{_bindir}/tth-numbering
%{_bindir}/tth-structure
%{_bindir}/tthprep
%{_bindir}/tthrfcat
%{_bindir}/tthsplit
%{_bindir}/ttm
%{_mandir}/man1/latex2gif.1*
%{_mandir}/man1/ps2gif.1*
%{_mandir}/man1/ps2gif_transparent.1*
%{_mandir}/man1/ps2png.1*
%{_mandir}/man1/tth.1*
%{_mandir}/man1/ttm.1*

%files tex
%license GPL2.txt
%{_texmf_main}/tex/generic/%{name}/

%files libs
%{_libdir}/libtth.so.*
%{_libdir}/libttm.so.*

%files devel
%doc tthfunc/README.ttmdynamic
%{_libdir}/libtth.so
%{_libdir}/libttm.so
%{_includedir}/tth.h

%changelog
* Fri Jun 12 2020 Jerry James <loganjerry@gmail.com> - 4.12-7
- Update -buffer-underflow patch to upstream version

* Tue Feb  4 2020 Jerry James <loganjerry@gmail.com> - 4.12-6
- Add -buffer-underflow patch to fix FTBFS with GCC 10

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 31 2017 Jerry James <loganjerry@gmail.com> - 4.12-1
- New upstream version

* Wed Sep  6 2017 Jerry James <loganjerry@gmail.com> - 4.10-1
- New upstream version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Jerry James <loganjerry@gmail.com> - 4.08-6
- Require more TeXLive packages

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 4.08-4
- Require TeX fonts that may be referenced in generated docs

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov  5 2015 Jerry James <loganjerry@gmail.com> - 4.08-2
- Remove prebuilt binaries
- Fix subpackage Requires

* Fri Oct 30 2015 Jerry James <loganjerry@gmail.com> - 4.08-1
- Initial RPM
