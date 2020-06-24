%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global pkgname lablgtk3

Name:           ocaml-%{pkgname}
Version:        3.1.0
Release:        6%{?dist}
Summary:        OCaml interface to gtk3

License:        LGPLv2+ with exceptions
URL:            http://lablgtk.forge.ocamlcore.org/
Source0:        https://github.com/garrigue/lablgtk/releases/download/%{version}/%{pkgname}-%{version}.tbz
# Fedora only patch: unbundle xml-light
Patch0:         %{name}-xml-light.patch
# Fix the build with -fno-common
# https://github.com/garrigue/lablgtk/pull/105
Patch1:         %{name}-fno-common.patch

BuildRequires:  help2man
BuildRequires:  ocaml >= 4.05.0
BuildRequires:  ocaml-cairo-devel >= 0.6
BuildRequires:  ocaml-camlp5-devel
BuildRequires:  ocaml-dune-devel >= 1.8.0
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-xml-light-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(gtkspell3-3.0)

%global _description %{expand:
LablGTK3 is an Objective Caml interface to gtk3.  It uses the rich
type system of Objective Caml to provide a strongly typed, yet very
comfortable, object-oriented interface to gtk3.}

%description %_description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gtk3-devel%{?_isa}
Requires:       ocaml-cairo-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}.

%package        gtkspell3
Summary:        OCaml interface to gtkspell3
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gtkspell3-devel%{?_isa}

%description    gtkspell3 %_description

This package contains OCaml bindings for gtkspell3.

%package        gtkspell3-devel
Summary:        Development files for %{name}-gtkspell3
Requires:       %{name}-gtkspell3%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    gtkspell3-devel
The %{name}-gtkspell3-devel package contains libraries and signature
files for developing applications that use %{name}-gtkspell3.

%package        sourceview3
Summary:        OCaml interface to gtksourceview3
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gtksourceview3-devel%{?_isa}

%description    sourceview3 %_description

This package contains OCaml bindings for gtksourceview3.

%package        sourceview3-devel
Summary:        Development files for %{name}-sourceview3
Requires:       %{name}-sourceview3%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    sourceview3-devel
The %{name}-sourceview3-devel package contains libraries and signature
files for developing applications that use %{name}-sourceview3.

%prep
%autosetup -n %{pkgname}-%{version} -p1

# This file is empty, so drop it before we make assemble the docs
rm doc/FAQ.text

# Make sure we do not use the bundled copy of xml-light
rm -fr tools/instrospection/xml-light

%build
export LABLGTK_EXTRA_FLAGS=-g
dune build %{?_smp_mflags}

# Build the documentation
dune build %{?_smp_mflags} @doc

# Relink the stublibs with $RPM_LD_FLAGS.
pushd _build/default/src
ocamlmklib -g -ldopt "$RPM_LD_FLAGS" $(pkgconf --libs gtk+-3.0) \
  -o lablgtk3_stubs $(ar t liblablgtk3_stubs.a)
cd ../src-gtkspell3
ocamlmklib -g -ldopt "$RPM_LD_FLAGS" $(pkgconf --libs gtkspell3-3.0) \
  -o lablgtk3_gtkspell3_stubs $(ar t liblablgtk3_gtkspell3_stubs.a)
cd ../src-sourceview3
ocamlmklib -g -ldopt "$RPM_LD_FLAGS" $(pkgconf --libs gtksourceview-3.0) \
  -o lablgtk3_sourceview3_stubs $(ar t liblablgtk3_sourceview3_stubs.a)
popd

# Make the man pages
HELP2MAN="-N --version-string=%{version}"
cd _build/install/default/bin
help2man $HELP2MAN -o ../../../../gdk_pixbuf_mlsource3.1 ./gdk_pixbuf_mlsource3
help2man $HELP2MAN -o ../../../../lablgladecc3.1 ./lablgladecc3
cd -

%install
dune install --destdir=%{buildroot}

# We do not want the dune markers
find _build/default/_doc/_html -name .dune-keep -delete

# We do not want the ml files
find %{buildroot}%{_libdir}/ocaml -name \*.ml -delete

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc

%ifarch %{ocaml_native_compiler}
# Add missing executable bits
find %{buildroot}%{_libdir}/ocaml -name \*.cmxs -exec chmod a+x {} \+
%endif

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
cp -p gdk_pixbuf_mlsource3.1 lablgladecc3.1 %{buildroot}%{_mandir}/man1

%check
dune runtest

%files
%doc CHANGES.md CHANGELOG.API README.md doc
%license LGPL LICENSE
%{_bindir}/gdk_pixbuf_mlsource3
%{_bindir}/lablgladecc3
%dir %{_libdir}/ocaml/lablgtk3
%{_libdir}/ocaml/lablgtk3/META
%{_libdir}/ocaml/lablgtk3/*.cma
%{_libdir}/ocaml/lablgtk3/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/lablgtk3/*.cmxs
%endif
%{_libdir}/ocaml/stublibs/dlllablgtk3_stubs.so
%{_mandir}/man1/gdk_pixbuf_mlsource3.1*
%{_mandir}/man1/lablgladecc3.1*

%files devel
%{_libdir}/ocaml/lablgtk3/lablgtk3.a
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/lablgtk3/lablgtk3.cmxa
%{_libdir}/ocaml/lablgtk3/*.cmx
%endif
%{_libdir}/ocaml/lablgtk3/*.cmt
%{_libdir}/ocaml/lablgtk3/*.cmti
%{_libdir}/ocaml/lablgtk3/*.mli
%{_libdir}/ocaml/lablgtk3/*.h
%{_libdir}/ocaml/lablgtk3/dune-package
%{_libdir}/ocaml/lablgtk3/liblablgtk3_stubs.a
%{_libdir}/ocaml/lablgtk3/opam

%files doc
%doc _build/default/_doc/_html/
%doc _build/default/_doc/_mlds/
%doc _build/default/_doc/_odoc/
%license LGPL LICENSE

%files           gtkspell3
%dir %{_libdir}/ocaml/lablgtk3-gtkspell3
%{_libdir}/ocaml/lablgtk3-gtkspell3/META
%{_libdir}/ocaml/lablgtk3-gtkspell3/gtkSpell.cmi
%{_libdir}/ocaml/lablgtk3-gtkspell3/lablgtk3_gtkspell3.cma
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/lablgtk3-gtkspell3/lablgtk3_gtkspell3.cmxs
%endif
%{_libdir}/ocaml/stublibs/dlllablgtk3_gtkspell3_stubs.so

%files           gtkspell3-devel
%{_libdir}/ocaml/lablgtk3-gtkspell3/dune-package
%{_libdir}/ocaml/lablgtk3-gtkspell3/gtkSpell.cmt
%{_libdir}/ocaml/lablgtk3-gtkspell3/gtkSpell.cmti
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/lablgtk3-gtkspell3/gtkSpell.cmx
%endif
%{_libdir}/ocaml/lablgtk3-gtkspell3/gtkSpell.mli
%{_libdir}/ocaml/lablgtk3-gtkspell3/lablgtk3_gtkspell3.a
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/lablgtk3-gtkspell3/lablgtk3_gtkspell3.cmxa
%endif
%{_libdir}/ocaml/lablgtk3-gtkspell3/liblablgtk3_gtkspell3_stubs.a
%{_libdir}/ocaml/lablgtk3-gtkspell3/opam

%files           sourceview3
%dir %{_libdir}/ocaml/lablgtk3-sourceview3
%{_libdir}/ocaml/lablgtk3-sourceview3/META
%{_libdir}/ocaml/lablgtk3-sourceview3/*.cma
%{_libdir}/ocaml/lablgtk3-sourceview3/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/lablgtk3-sourceview3/lablgtk3_sourceview3.cmxs
%endif
%{_libdir}/ocaml/stublibs/dlllablgtk3_sourceview3_stubs.so

%files           sourceview3-devel
%{_libdir}/ocaml/lablgtk3-sourceview3/dune-package
%{_libdir}/ocaml/lablgtk3-sourceview3/lablgtk3_sourceview3.a
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/lablgtk3-sourceview3/lablgtk3_sourceview3.cmxa
%{_libdir}/ocaml/lablgtk3-sourceview3/*.cmx
%endif
%{_libdir}/ocaml/lablgtk3-sourceview3/*.cmt
%{_libdir}/ocaml/lablgtk3-sourceview3/*.cmti
%{_libdir}/ocaml/lablgtk3-sourceview3/*.mli
%{_libdir}/ocaml/lablgtk3-sourceview3/liblablgtk3_sourceview3_stubs.a
%{_libdir}/ocaml/lablgtk3-sourceview3/opam

%changelog
* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-6
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-5
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-4
- Bump release and rebuild.

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-3
- Update all OCaml dependencies for RPM 4.16.

* Sat Mar  7 2020 Jerry James <loganjerry@gmail.com> - 3.1.0-2
- Build documentation with odoc
- Add _isa flags to Requires in the devel subpackage

* Wed Jan 29 2020 Jerry James <loganjerry@gmail.com> - 3.1.0-1
- Initial RPM
