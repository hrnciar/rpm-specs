%global ocaml_destdir %{_libdir}/ocaml

Name:           ocaml-ocamlgraph
Version:        1.8.8
Release:        23%{?dist}
Summary:        OCaml library for arc and node graphs

License:        LGPLv2 with exceptions
URL:            http://ocamlgraph.lri.fr/index.en.html
Source0:        http://ocamlgraph.lri.fr/download/ocamlgraph-%{version}.tar.gz
Source1:        ocamlgraph-test.result
# When building the byte variant, do not try to install artifacts that were
# not built.
Patch0:         ocamlgraph-1.8.6-byte-install.patch

# Fix the tests - unclear why this is necessary.
Patch1:         ocamlgraph-1.8.7-fix-tests.patch

BuildRequires:  libart_lgpl-devel
BuildRequires:  libgnomecanvas-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lablgtk-devel
BuildRequires:  ocaml-ocamldoc

%global __requires_exclude ocaml\\\(Sig\\\)
%global libname %(sed -e 's/^ocaml-//' <<< %{name})

%description
Ocamlgraph provides several different implementations of graph data
structures. It also provides implementations for a number of classical
graph algorithms like Kruskal's algorithm for MSTs, topological
ordering of DAGs, Dijkstra's shortest paths algorithm, and
Ford-Fulkerson's maximal-flow algorithm to name a few. The algorithms
and data structures are written functorially for maximal
reusability. Also has input and output capability for Graph Modeling
Language file format and Dot and Neato graphviz (graph visualization)
tools.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%package        tools
Summary:        Graph editing tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    tools
The %{name}-tools package contains graph editing tools for use with
%{name}.


%prep
%setup -q -n %{libname}-%{version}
%ifnarch %{ocaml_native_compiler}
%patch0
%endif
%patch1 -p1

cp -p %{SOURCE1} .

# Fix encoding
for fil in CHANGES COPYING CREDITS; do
  iconv -f latin1 -t utf-8 $fil > $fil.utf8
  touch -r $fil $fil.utf8
  mv -f $fil.utf8 $fil
done


%build
%configure

%ifarch %{ocaml_native_compiler}
%global opt_option OCAMLBEST=opt OCAMLOPT='ocamlopt.opt -g'
%else
%global opt_option OCAMLBEST=byte OCAMLC=ocamlc
%endif
make depend
make %{opt_option}
make doc

# Skip the tests on i386; see https://github.com/ocaml/ocaml/issues/9800
%ifnarch %{ix86}
%ifarch %{ocaml_native_compiler}
%check
make --no-print-directory check >& test
diff -u test ocamlgraph-test.result
%endif
%endif


%install
mkdir -p %{buildroot}%{ocaml_destdir}
make OCAMLFIND_DESTDIR=%{buildroot}%{ocaml_destdir} install-findlib
%ifarch %{ocaml_native_compiler}
install -m 0755 -p graph.cmxs %{buildroot}%{ocaml_destdir}/%{libname}
%endif

# Include all code and examples in the docs
mkdir -p dox-devel/examples
mkdir -p dox-devel/API
cp -p examples/*.ml dox-devel/examples
cp -p doc/* dox-devel/API

# Install the graph editing tools
mkdir -p %{buildroot}%{_bindir}
%ifarch %{ocaml_native_compiler}
install -m 0755 -p editor/editor.opt %{buildroot}/%{_bindir}/ocaml-graph-editor
install -m 0755 -p dgraph/dgraph.opt %{buildroot}%{_bindir}/ocaml-graph-viewer
install -m 0755 -p view_graph/viewgraph.opt \
    %{buildroot}%{_bindir}/ocaml-viewgraph
%else
install -m 0755 -p editor/editor.byte %{buildroot}/%{_bindir}/ocaml-graph-editor
install -m 0755 -p dgraph/dgraph.byte %{buildroot}%{_bindir}/ocaml-graph-viewer
install -m 0755 -p view_graph/viewgraph.byte \
     %{buildroot}%{_bindir}/ocaml-viewgraph
%endif


%files
%doc CREDITS FAQ
%license COPYING LICENSE
%{ocaml_destdir}/%{libname}/
%ifarch %{ocaml_native_compiler}
%exclude %{ocaml_destdir}/*/*.a
%exclude %{ocaml_destdir}/*/*.cmxa
%exclude %{ocaml_destdir}/*/*.cmx
%exclude %{ocaml_destdir}/*/*.o
%endif
%exclude %{ocaml_destdir}/*/*.mli


%files devel
%doc CHANGES README.adoc dox-devel/*
%ifarch %{ocaml_native_compiler}
%{ocaml_destdir}/*/*.a
%{ocaml_destdir}/*/*.cmxa
%{ocaml_destdir}/*/*.cmx
%{ocaml_destdir}/*/*.o
%endif
%{ocaml_destdir}/*/*.mli


%files tools
%{_bindir}/*


%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.8.8-23
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.8.8-22
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-21
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.8.8-19
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.8.8-18
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 1.8.8-17
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 1.8.8-16
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.8.8-15
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.8.8-13
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 1.8.8-12
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.8.8-11
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.8.8-10
- OCaml 4.08.1 (final) rebuild.

* Sat Aug 10 2019 Richard W.M. Jones <rjones@redhat.com> - 1.8.8-9
- Rebuild against new ocaml-lablgtk.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 1.8.8-8
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.8.8-4
- OCaml 4.07.0 (final) rebuild.

* Tue Jun 19 2018 Richard W.M. Jones <rjones@redhat.com> - 1.8.8-3
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Richard W.M. Jones <rjones@redhat.com> - 1.8.8-1
- New upstream version 1.8.8.

* Tue Nov 07 2017 Richard W.M. Jones <rjones@redhat.com> - 1.8.7-11
- OCaml 4.06.0 rebuild.

* Mon Aug 07 2017 Richard W.M. Jones <rjones@redhat.com> - 1.8.7-10
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 1.8.7-7
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 1.8.7-6
- Bump release and rebuild.

* Thu May 11 2017 Richard W.M. Jones <rjones@redhat.com> - 1.8.7-5
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 1.8.7-3
- rebuild for s390x codegen bug

* Sun Nov 06 2016 Richard W.M. Jones <rjones@redhat.com> - 1.8.7-2
- Rebuild for OCaml 4.04.0.

* Sat Apr 16 2016 Jerry James <loganjerry@gmail.com> - 1.8.7-1
- New upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.8.6-5
- OCaml 4.02.3 rebuild.

* Wed Jul 22 2015 Richard W.M. Jones <rjones@redhat.com> - 1.8.6-4
- Enable bytecode builds.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.8.6-3
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.8.6-2
- ocaml-4.02.2 rebuild.

* Wed Mar 18 2015 Jerry James <loganjerry@gmail.com> - 1.8.6-1
- New upstream release
- Reenable documentation generation

* Mon Feb 16 2015 Richard W.M. Jones <rjones@redhat.com> - 1.8.5-10
- ocaml-4.02.1 rebuild.

* Thu Oct 30 2014 Jerry James <loganjerry@gmail.com> - 1.8.5-9
- Rebuild for new ocaml-lablgtk
- Fix license handling

* Sat Aug 30 2014 Richard W.M. Jones <rjones@redhat.com> - 1.8.5-8
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.8.5-7
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Richard W.M. Jones <rjones@redhat.com> - 1.8.5-5
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Wed Jul 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.8.5-4
- OCaml 4.02.0 beta rebuild.
- Disable documentation generation.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 21 2014 Jerry James <loganjerry@gmail.com> - 1.8.5-1
- New upstream release

* Tue Apr 15 2014 Richard W.M. Jones <rjones@redhat.com> - 1.8.4-2
- Remove ocaml_arches macro (RHBZ#1087794).

* Wed Feb 26 2014 Jerry James <loganjerry@gmail.com> - 1.8.4-1
- New upstream release, 1.8.4+dev, where the "+dev" refers to a bug fix
  that was applied immediately after the 1.8.4 release
- Drop upstreamed patch
- Install graph.cmxs and enable the -debuginfo subpackage
- Update expected test results
- BR ocaml-findlib only, not ocaml-findlib-devel
- Install graph editing tools into -tools subpackage
- Fix the bytecode build

* Wed Oct 02 2013 Richard W.M. Jones <rjones@redhat.com> - 1.8.3-5
- Rebuild for ocaml-lablgtk 2.18.

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 1.8.3-4
- Rebuild for OCaml 4.01.0.

* Tue Aug  6 2013 Jerry James <loganjerry@gmail.com> - 1.8.3-3
- Adapt to Rawhide unversioned docdir change (bz 994002)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Jerry James <loganjerry@gmail.com> - 1.8.3-1
- New upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 17 2012 Jerry James <loganjerry@gmail.com> - 1.8.2-2
- Rebuild for OCaml 4.00.1.

* Mon Jul 30 2012 Jerry James <loganjerry@gmail.com> - 1.8.2-1
- New upstream release

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Richard W.M. Jones <rjones@redhat.com> - 1.8.1-3
- Rebuild for OCaml 4.00.0.

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 1.8.1-2
- Rebuild for OCaml 3.12.1

* Tue Oct 25 2011 Jerry James <loganjerry@gmail.com> - 1.8.1-1
- New upstream release

* Mon Jul 11 2011 Jerry James <loganjerry@gmail.com> - 1.7-1
- New upstream release
- Drop unnecessary spec file elements (BuildRoot, etc.)
- Drop dependency generation workaround for Fedora 12 and earlier
- Remove spurious executable bits on source files
- Replace the definition of __ocaml_requires_opts to "-i Sig", which removes
  the legitimate Requires: ocaml(GtkSignal), with __requires_exclude.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 21 2011 Richard W.M. Jones <rjones@redhat.com> - 1.6-2
- Ignore ocaml(Sig) symbol.

* Mon Jan 10 2011 Richard W.M. Jones <rjones@redhat.com> - 1.6-1
- New upstream version 1.6.
- Rebuild for OCaml 3.12.
- Remove obsolete patches and add patch to fix install-findlib rule.

* Wed Feb 10 2010 Alan Dunn <amdunn@gmail.com> - 1.3-3
- Include files (including .cmo files) and install more files that are
  needed by other applications (eg: Frama-C) that depend on
  ocaml-ocamlgraph
- define -> global
- Update for new dependency generator in F13

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.3-2
- Rebuild for OCaml 3.11.2.

* Thu Oct  8 2009 Richard W.M. Jones <rjones@redhat.com> - 1.3-1
- New upstream release 1.3.
- A slightly different viewGraph-related patch is required for this release.

* Fri Aug 07 2009 Alan Dunn <amdunn@gmail.com> - 1.1-1
- New upstream release 1.1.
- Makefile patch updated (still not incorporated upstream).

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0-5
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec  5 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0-3
- Rebuild for OCaml 3.11.0.
- Requires lablgtk2.
- Pull in gtk / libgnomecanvas too.

* Thu Nov 20 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0-1
- New upstream release 1.0.
- Patch0 removed - now upstream.
- Added a patch to fix documentation problem.
- Run tests with 'make --no-print-directory'.

* Wed Aug 13 2008 Alan Dunn <amdunn@gmail.com> 0.99c-2
- Incorporates changes suggested during review:
- License information was incorrect
- rpmlint error now properly justified

* Thu Aug 07 2008 Alan Dunn <amdunn@gmail.com> 0.99c-1
- Initial Fedora RPM release.
