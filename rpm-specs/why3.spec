# NOTE: Upstream has said that the Frama-C support is still experimental, and
# less functional than the corresponding support in why2.  They recommend not
# enabling it for now.  We abide by their wishes.  Revisit this decision each
# release.

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           why3
Version:        1.3.3
Release:        1%{?dist}
Summary:        Software verification platform

# See LICENSE for the terms of the exception
License:        LGPLv2 with exceptions
URL:            http://why3.lri.fr/
Source0:        https://gforge.inria.fr/frs/download.php/file/38367/%{name}-%{version}.tar.gz
# Man pages written by Jerry James using text found in the sources.  Hence,
# the copyright and license are the same as for the upstream sources.
Source1:        %{name}-man.tar.xz
# Desktop file written by Jerry James
Source2:        %{name}.desktop
# AppData file written by Jerry James
Source3:        %{name}.appdata.xml

# https://bugzilla.redhat.com/show_bug.cgi?id=1874879
ExcludeArch: s390x

BuildRequires:  coq
BuildRequires:  emacs-proofgeneral
BuildRequires:  flocq
BuildRequires:  latexmk
BuildRequires:  libappstream-glib
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp5-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lablgtk3-sourceview3-devel
BuildRequires:  ocaml-menhir
BuildRequires:  ocaml-num-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-zarith-devel
BuildRequires:  ocaml-zip-devel
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinxcontrib-bibtex}
BuildRequires:  tex(capt-of.sty)
BuildRequires:  tex(comment.sty)
BuildRequires:  tex(fncychap.sty)
BuildRequires:  tex(framed.sty)
BuildRequires:  tex(latex)
BuildRequires:  tex(needspace.sty)
BuildRequires:  tex(tabulary.sty)
BuildRequires:  tex(upquote.sty)
BuildRequires:  tex(wrapfig.sty)
BuildRequires:  tex-urlbst
BuildRequires:  emacs xemacs xemacs-packages-extra
BuildRequires:  graphviz

Requires:       gtksourceview3%{?_isa}
Requires:       hicolor-icon-theme
Requires:       texlive-base%{?_isa}
Requires:       vim-filesystem

Recommends:     bash-completion

Provides:       bundled(jquery)

# The corresponding Provides is not generated, so filter this out
%global __requires_exclude ocaml\\\(Why3\\\)

# This can be removed when F36 reaches EOL
Obsoletes:      why < 2.41-12
Provides:       why = 2.41-12%{?dist}
Obsoletes:      why-jessie < 2.41-12
Provides:       why-jessie = 2.41-12%{?dist}
Obsoletes:      why-pvs-support < 2.41-12
Provides:       why-pvs-support = 2.41-12%{?dist}

%description
Why3 is the next generation of the Why software verification platform.
Why3 clearly separates the purely logical specification part from
generation of verification conditions for programs.  It features a rich
library of proof task transformations that can be chained to produce a
suitable input for a large set of theorem provers, including SMT
solvers, TPTP provers, as well as interactive proof assistants.

%package examples
Summary:        Example inputs
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description examples
Example source code with why3 annotations.

%package emacs
Summary:        Emacs support file for %{name} files
Requires:       %{name} = %{version}-%{release}
Requires:       emacs(bin)
BuildArch:      noarch

%description emacs
This package contains an Emacs support file for working with %{name} files.

%package xemacs
Summary:        XEmacs support file for %{name} files
Requires:       %{name} = %{version}-%{release}
Requires:       xemacs(bin)
BuildArch:      noarch

%description xemacs
This package contains an XEmacs support file for working with %{name} files.

%package all
Summary:        Complete Why3 software verification platform suite
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       alt-ergo coq cvc4 E gappa yices-tools z3 zenon

# This can be removed when F36 reaches EOL
Obsoletes:      why-all < 2.41-12
Provides:       why-all = 2.41-12%{?dist}

%description all
This package provides a complete software verification platform suite
based on Why3, including various automated and interactive provers.

%package -n ocaml-%{name}
Summary:        Software verification library for ocaml
Requires:       ocaml-num%{?_isa}
Requires:       ocaml-zip-devel%{?_isa}

%description -n ocaml-%{name}
This package contains an ocaml library that exposes the functionality
of why3 to applications.

%package -n ocaml-%{name}-devel
Summary:        Development files for using the ocaml-%{name} library
Requires:       ocaml-%{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-menhir%{?_isa}
Requires:       ocaml-num-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}
Requires:       ocaml-seq-devel%{?_isa}

%description -n ocaml-%{name}-devel
This package contains development files needed to build applications
that use the ocaml-%{name} library.

%package proofgeneral
Summary:        Why3 integration with ProofGeneral
Requires:       %{name} = %{version}-%{release}
Requires:       emacs-proofgeneral
BuildArch:      noarch

%description proofgeneral
This package provides a why3 plugin for ProofGeneral.

%prep
%autosetup -p0
%setup -q -T -D -a 1

fixtimestamp() {
  touch -r $1.orig $1
  rm $1.orig
}

# Use the correct compiler flags, keep timestamps, and harden the build due to
# network use.  Link the binaries with runtime compiled with -fPIC.
# This avoids many link-time errors.
sed -e "s|-Wall|$RPM_OPT_FLAGS|;s/ -O -g//" \
    -e "s/cp /cp -p /" \
    -e "s|^OLINKFLAGS =.*|& -runtime-variant _pic -ccopt \"$RPM_LD_FLAGS\"|" \
    -i Makefile.in

# Remove spurious executable bits
find -O3 examples -type f -perm /0111 -exec chmod a-x {} \+
chmod a+x examples/*.sh

# Update the ProofGeneral integration instructions
sed -i.orig 's,(MY_PATH_TO_WHY3)/share/whyitp,%{_emacs_sitelispdir},' share/whyitp/README
fixtimestamp share/whyitp/README

%build
%configure --enable-verbose-make
make #%%{?_smp_mflags}
make doc
rm -f doc/html/.buildinfo examples/use_api/.merlin.in

%install
%make_install
make install-lib DESTDIR=%{?buildroot} INSTALL="%{__install} -p"

%ifarch %{ocaml_native_compiler}
# Install the native coq files
cd lib/coq
for dir in $(find . -name .coq-native); do
  cp -a $dir %{buildroot}%{_libdir}/%{name}/coq/$dir
done
cd -
%endif

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
cd man
for f in *.1; do
  sed "s/@version@/%{version}/" $f > %{buildroot}%{_mandir}/man1/$f
  touch -r $f %{buildroot}%{_mandir}/man1/$f
done
cd ..

# Install the bash completion file
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
cp -p share/bash/%{name} %{buildroot}%{_datadir}/bash-completion/completions

# Install the zsh completion file
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
cp -p share/zsh/_why3 %{buildroot}%{_datadir}/zsh/site-functions

# Install the LaTeX style
mkdir -p %{buildroot}%{_texmf}/tex/latex/why3
cp -p share/latex/why3lang.sty %{buildroot}%{_texmf}/tex/latex/why3

# Move the gtksourceview language file to the right place
mkdir -p %{buildroot}%{_datadir}/gtksourceview-3.0
mv %{buildroot}%{_datadir}/%{name}/lang \
   %{buildroot}%{_datadir}/gtksourceview-3.0/language-specs

# Install the desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

# Install the icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable
cp -p share/images/src/logo-kim.svg \
      %{buildroot}%{_datadir}/icons/hicolor/scalable/%{name}.svg

# Install the AppStream metadata
mkdir -p %{buildroot}%{_metainfodir}
cp -p %{SOURCE3} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

# Move the vim file to the right place
mkdir -p %{buildroot}%{_datadir}/vim/vimfiles
mv %{buildroot}%{_datadir}/%{name}/vim/ftdetect \
   %{buildroot}%{_datadir}/%{name}/vim/syntax \
   %{buildroot}%{_datadir}/vim/vimfiles

# Byte compile the (X)Emacs support files
mkdir -p %{buildroot}%{_xemacs_sitelispdir}
cp -p %{buildroot}%{_emacs_sitelispdir}/%{name}.el \
   %{buildroot}%{_xemacs_sitelispdir}
cp -p share/whyitp/whyitp.el %{buildroot}%{_emacs_sitelispdir}
pushd %{buildroot}%{_xemacs_sitelispdir}
%{_xemacs_bytecompile} %{name}.el
cd %{buildroot}%{_emacs_sitelispdir}
%{_emacs_bytecompile} %{name}.el whyitp.el
popd

# Remove misplaced documentation
rm -fr %{buildroot}%{_datadir}/doc

# Fix permissions
chmod 0755 %{buildroot}%{_bindir}/* \
           %{buildroot}%{_libdir}/%{name}/commands/* \
           %{buildroot}%{_libdir}/%{name}/plugins/*.cmxs \
           %{buildroot}%{_libdir}/ocaml/%{name}/*.cmxs

%files
%doc AUTHORS CHANGES.md README.md doc/html doc/latex/manual.pdf
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/bash-completion/completions/why3
%{_datadir}/gtksourceview-3.0/language-specs/%{name}.lang
%{_datadir}/gtksourceview-3.0/language-specs/%{name}c.lang
%{_datadir}/gtksourceview-3.0/language-specs/%{name}py.lang
%{_datadir}/icons/hicolor/scalable/%{name}.svg
%{_datadir}/vim/vimfiles/ftdetect/%{name}.vim
%{_datadir}/vim/vimfiles/syntax/%{name}.vim
%{_datadir}/zsh/
%{_texmf}/tex/latex/why3/
%{_libdir}/%{name}/
%{_mandir}/man1/%{name}*
%{_metainfodir}/%{name}.appdata.xml

%files -n ocaml-%{name}
%dir %{_libdir}/ocaml/%{name}/
%{_libdir}/ocaml/%{name}/META
%{_libdir}/ocaml/%{name}/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{name}/*.cmxs
%endif

%files -n ocaml-%{name}-devel
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{name}/*.a
%{_libdir}/ocaml/%{name}/*.cmx
%{_libdir}/ocaml/%{name}/*.cmxa
%else
%{_libdir}/ocaml/%{name}/*.cma
%endif

%files examples
%doc examples

%files emacs
%{_emacs_sitelispdir}/%{name}.el*

%files xemacs
%{_xemacs_sitelispdir}/%{name}.el*

%files proofgeneral
%doc share/whyitp/README
%{_emacs_sitelispdir}/whyitp.el*

# "why3-all" is a meta-package; it just depends on other packages, so that
# it's easier to install a useful suite of tools.  Thus, it has no files:
%files all

%changelog
* Fri Sep 25 2020 Jerry James <loganjerry@gmail.com> - 1.3.3-1
- Version 1.3.3

* Wed Sep 02 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.1-14
- OCaml 4.11.1 rebuild

* Tue Sep  1 2020  Jerry James <loganjerry@gmail.com> - 1.3.1-13
- Rebuild for coq 8.12.0

* Mon Aug 24 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.1-13
- OCaml 4.11.0 rebuild

* Thu Aug  6 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-12
- Rebuild for ocaml-lablgtk3 3.1.1 and ocaml-menhir 20200624

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-10
- Rebuild for coq 8.11.2

* Sat Jun 13 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-9
- Rebuild for flocq 3.3.1
- Build the coq files with the native compiler when possible

* Wed May 20 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-8
- Rebuild for coq 8.11.1

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.1-7
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Sun Apr 12 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-6
- Make the dependencies on ocaml-num and ocaml-zip explicit (bz 1795083)

* Wed Apr  8 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-5
- Rebuild for flocq 3.2.1

* Sun Apr 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.1-4
- Update all OCaml dependencies for RPM 4.16.

* Wed Apr  1 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-3
- Do not build with mlmpfr; symbols clash with mlgmpidl, causing frama-c to
  fail to start
- Obsolete the why2 packages

* Sat Mar 28 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-2
- Remove useless BRs and Rs (bz 1817878)

* Wed Mar 25 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-1
- Version 1.3.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Jerry James <loganjerry@gmail.com> - 1.2.1-3
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-2
- OCaml 4.09.0 (final) rebuild.

* Tue Oct 29 2019 Jerry James <loganjerry@gmail.com> - 1.2.1-1
- New upstream release
- Add -proofgeneral subpackage
- Add desktop and AppData files

* Fri Oct 11 2019 Jerry James <loganjerry@gmail.com> - 1.2.0-6
- Rebuild for ocaml-menhir 20190924

* Fri Sep  6 2019 Jerry James <loganjerry@gmail.com> - 1.2.0-5
- Rebuild for ocaml-zarith 1.9

* Thu Aug  1 2019 Jerry James <loganjerry@gmail.com> - 1.2.0-4
- Also install the library, for consumption by frama-c

* Thu Aug  1 2019 Jerry James <loganjerry@gmail.com> - 1.2.0-3
- Rebuild for flocq 3.2.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Jerry James <loganjerry@gmail.com> - 1.2.0-1
- New upstream release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Jerry James <loganjerry@gmail.com> - 1.1.1-1
- New upstream release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.88.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Richard W.M. Jones <rjones@redhat.com> - 0.88.3-4
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.88.3-3
- Bump release and rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.88.3-2
- OCaml 4.07.0-rc1 rebuild.

* Mon Feb 12 2018 Jerry James <loganjerry@gmail.com> - 0.88.3-1
- New upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.88.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec  9 2017 Jerry James <loganjerry@gmail.com> - 0.88.2-1
- New upstream release

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 0.88.1-1
- New upstream version 0.88.1.
- OCaml 4.06.0 rebuild.

* Sat Oct  7 2017 Jerry James <loganjerry@gmail.com> - 0.88.0-1
- New usptream release

* Thu Oct  5 2017 Jerry James <loganjerry@gmail.com> - 0.87.3-12
- Rebuild for flocq 2.6.0

* Wed Sep 06 2017 Richard W.M. Jones <rjones@redhat.com> - 0.87.3-11
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.87.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.87.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 0.87.3-8
- Bump release and rebuild.

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 0.87.3-7
- Bump release and rebuild.

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 0.87.3-6
- Bump release and rebuild.

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 0.87.3-5
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 0.87.3-4
- OCaml 4.04.1 rebuild.

* Fri Mar 24 2017 Jerry James <loganjerry@gmail.com> - 0.87.3-3
- Rebuild to fix coq consistency issue

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.87.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Jerry James <loganjerry@gmail.com> - 0.87.3-1
- New upstream release

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 0.87.2-4
- Rebuild for OCaml 4.04.0.

* Fri Oct 28 2016 Jerry James <loganjerry@gmail.com> - 0.87.2-3
- Rebuild for coq 8.5pl3
- Remove obsolete scriptlets
- Fix install location of why3lang.sty

* Thu Sep 29 2016 Jerry James <loganjerry@gmail.com> - 0.87.2-2
- Rebuild for flocq 2.5.2 and gappalib-coq 1.3.1

* Fri Sep  2 2016 Jerry James <loganjerry@gmail.com> - 0.87.2-1
- New upstream release

* Wed Jul 13 2016 Jerry James <loganjerry@gmail.com> - 0.87.1-2
- Rebuild for coq 8.5pl2

* Wed Jun  1 2016 Jerry James <loganjerry@gmail.com> - 0.87.1-1
- New upstream release

* Fri Apr 22 2016 Jerry James <loganjerry@gmail.com> - 0.87.0-3
- Rebuild for coq 8.5pl1

* Sat Apr 16 2016 Jerry James <loganjerry@gmail.com> - 0.87.0-2
- Rebuild for ocaml-ocamlgraph 1.8.7

* Fri Mar 18 2016 Jerry James <loganjerry@gmail.com> - 0.87.0-1
- New upstream release
- Drop boomy icon removal; upstream no longer ships them

* Fri Feb 12 2016 Jerry James <loganjerry@gmail.com> - 0.86.3-1
- New upstream release
- Use camlp4 in preference to camlp5

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.86.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Jerry James <loganjerry@gmail.com> - 0.86.2-2
- Rebuild for ocaml-zarith 1.4.1 and ocaml-menhir 20151112

* Wed Oct 14 2015 Jerry James <loganjerry@gmail.com> - 0.86.2-1
- New upstream release
- Do not ship the nonfree boomy icons

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 0.86.1-2
- ocaml-4.02.2 final rebuild.

* Mon Jun 22 2015 Jerry James <loganjerry@gmail.com> - 0.86.1-1
- New upstream release

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 0.86-2
- ocaml-4.02.2 rebuild.

* Sat May 16 2015 Jerry James <loganjerry@gmail.com> - 0.86-1
- New upstream release

* Sat Apr 11 2015 Jerry James <loganjerry@gmail.com> - 0.85-9
- Rebuild for coq 8.4pl6

* Wed Mar 18 2015 Jerry James <loganjerry@gmail.com> - 0.85-8
- Rebuild for ocaml-ocamlgraph 1.8.6

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 0.85-7
- Note bundled jquery
- Fix sed expression separators for new RPM_OPT_FLAGS and RPM_LD_FLAGS

* Wed Feb 18 2015 Richard W.M. Jones <rjones@redhat.com> - 0.85-6
- ocaml-4.02.1 rebuild.

* Thu Nov  6 2014 Jerry James <loganjerry@gmail.com> - 0.85-5
- Rebuild for ocaml-camlp5 6.12

* Thu Oct 30 2014 Jerry James <loganjerry@gmail.com> - 0.85-4
- Rebuild for coq 8.4pl5

* Tue Oct 14 2014 Jerry James <loganjerry@gmail.com> - 0.85-3
- Rebuild for ocaml-zarith 1.3

* Thu Sep 18 2014 Jerry James <loganjerry@gmail.com> - 0.85-2
- Bump and rebuild

* Wed Sep 17 2014 Jerry James <loganjerry@gmail.com> - 0.85-1
- New upstream release
- New source URL

* Tue Sep  2 2014 Jerry James <loganjerry@gmail.com> - 0.84-1
- New upstream release
- Fix license handling

* Mon Aug 25 2014 Jerry James <loganjerry@gmail.com> - 0.83-14
- Rebuild for new gappalib-coq build

* Sun Aug 24 2014 Richard W.M. Jones <rjones@redhat.com> - 0.83-13
- ocaml-4.02.0+rc1 rebuild.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.83-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug  4 2014 Jerry James <loganjerry@gmail.com> - 0.83-11
- Rebuild for new gappalib-coq build

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 0.83-10
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Fri Aug 01 2014 Richard W.M. Jones <rjones@redhat.com> - 0.83-9
- OCaml 4.02.0 beta rebuild.

* Thu Jun 26 2014 Jerry James <loganjerry@gmail.com> - 0.83-8
- Linking with -z relro -z now breaks plugins; omit "-z now"

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.83-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Jerry James <loganjerry@gmail.com> - 0.83-6
- Rebuild for coq 8.4pl4

* Mon Apr 21 2014 Jerry James <loganjerry@gmail.com> - 0.83-5
- Rebuild for flocq 2.3.0 and ocamlgraph 1.8.5
- Drop unnecessary sqlite-devel BR

* Tue Apr 15 2014 Richard W.M. Jones <rjones@redhat.com> - 0.83-4
- Remove ocaml_arches macro (RHBZ#1087794).

* Mon Mar 24 2014 Jerry James <loganjerry@gmail.com> - 0.83-3
- Apply upstream fix for building with ocaml-zarith
- Fix file encodings
- Fix permission bits

* Tue Mar 18 2014 Jerry James <loganjerry@gmail.com> - 0.83-2
- Back out the post-release fix to the Coq printer, which breaks Frama-C

* Fri Mar 14 2014 Jerry James <loganjerry@gmail.com> - 0.83-1
- New upstream release
- Use cvc4 instead of cvc3

* Wed Feb 26 2014 Jerry James <loganjerry@gmail.com> - 0.82-2
- Rebuild for ocamlgraph 1.8.4
- BR ocaml-findlib instead of ocaml-findlib-devel

* Fri Dec 13 2013 Jerry James <loganjerry@gmail.com> - 0.82-1
- New upstream release
- Drop upstreamed patches
- Add -examples subpackage
- Install LaTeX style
- Turn off frama-c support at upstream's request

* Mon Sep 30 2013 Jerry James <loganjerry@gmail.com> - 0.81-6
- Apply upstream fix for change in the alt-ergo timelimit option

* Tue Sep 17 2013 Jerry James <loganjerry@gmail.com> - 0.81-5
- Rebuild for OCaml 4.01.0
- Enable debuginfo for the ocaml sources

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.81-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Jerry James <loganjerry@gmail.com> - 0.81-3
- Rebuild for frama-c Fluorine 20130601

* Thu May 23 2013 Jerry James <loganjerry@gmail.com> - 0.81-2
- Rebuild for frama-c Fluorine 20130501

* Fri May 10 2013 Jerry James <loganjerry@gmail.com> - 0.81-1
- New upstream release
- Disable PVS support for now; it requires the NASA libraries
- Fix the conflict between the why and why3 Emacs packages (bz 913522)
- Disable parallel builds due to intermittent build failures

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.73-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Jerry James <loganjerry@gmail.com> - 0.73-4
- Rebuild for coq 8.4pl1

* Fri Dec 14 2012 Richard W.M. Jones <rjones@redhat.com> - 0.73-3
- Rebuild for OCaml 4.00.1.

* Thu Aug 23 2012 Jerry James <loganjerry@gmail.com> - 0.73-2
- Rebuild for coq 8.4

* Thu Aug  2 2012 Jerry James <loganjerry@gmail.com> - 0.73-1
- New upstream release

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Jerry James <loganjerry@gmail.com> - 0.71-2
- Add missing sqlite-devel BR
- Do not move the coq plugin
- Generate debuginfo for the sole C program
- Add man pages

* Fri Dec 16 2011 Jerry James <loganjerry@gmail.com> - 0.71-1
- Initial RPM
