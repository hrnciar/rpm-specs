# XXX This indicates a bug somewhere.  We are not passing the -g flag
# through when creating the libraries.  However I cannot see exactly
# what is wrong.
%undefine _debugsource_packages

Name:           ocaml-camlimages
Version:        4.2.5
Release:        22%{?dist}
Summary:        OCaml image processing library
License:        LGPLv2 with exceptions

URL:            http://gallium.inria.fr/camlimages/
Source0:        https://bitbucket.org/camlspotter/camlimages/get/%{version}.tar.gz

# This file isn't published any more (that I could find).
# It's probably dated but at least should provide some info on how to
# use the library.
Source1:        camlimages-2.2.0-htmlref.tar.gz

Patch1:         camlimages-4.2.5-add-g-flag.patch
# Fix an example which has safe-string problems.
Patch2:         camlimages-4.2.5-safe-string.patch

BuildRequires:  ocaml, ocaml-findlib-devel, ocaml-omake
BuildRequires:  ocaml-lablgtk-devel
BuildRequires:  xorg-x11-server-utils
BuildRequires:  libpng-devel, libjpeg-devel, libexif-devel
BuildRequires:  libXpm-devel, libgs-devel, freetype-devel
BuildRequires:  giflib-devel
BuildRequires:  libtiff-devel
BuildRequires:  gtk2-devel
Requires:       xorg-x11-server-utils

%description
This is an image processing library, which provides some basic
functions of image processing and loading/saving various image file
formats. In addition the library can handle huge images that cannot be
(or can hardly be) stored into the memory (the library automatically
creates swap files and escapes them to reduce the memory usage).

%package        devel
Summary:        Development files for camlimages
Requires:       %{name}%{?_isa} = %{version}-%{release} 


%description    devel
The camlimages-devel package provides libraries and headers for 
developing applications using camlimages

Includes documentation provided by ocamldoc

%prep
%setup -q -n camlspotter-camlimages-8ca76028cff3
%setup -q -T -D -a 1 -n camlspotter-camlimages-8ca76028cff3
%patch1 -p1
%patch2 -p2

%build
omake CFLAGS="$RPM_OPT_FLAGS" --verbose

%install
# These rules work if the library uses 'ocamlfind install' to install itself.
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
omake install

mkdir -p $RPM_BUILD_ROOT/usr/share/doc/ocaml-camlimages
cp -pr License.txt htmlref $RPM_BUILD_ROOT/usr/share/doc/ocaml-camlimages

%files
%doc README.md License.txt
%{_libdir}/ocaml/camlimages
%exclude %{_libdir}/ocaml/camlimages/*.a
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/camlimages/*.cmxa
%endif
# There aren't any *.cmx files
#%exclude %{_libdir}/ocaml/camlimages/*.cmx
%exclude %{_libdir}/ocaml/camlimages/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner


%files devel
%{_docdir}/%{name}/htmlref/
%{_libdir}/ocaml/camlimages/*.a
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/camlimages/*.cmxa
%endif
# There aren't any *.cmx files
#%{_libdir}/ocaml/camlimages/*.cmx
%{_libdir}/ocaml/camlimages/*.mli


%changelog
* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-22
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-21
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-20
- OCaml 4.11.0 pre-release

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-19
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-18
- OCaml 4.10.0 final.

* Thu Feb 06 2020 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-17
- Remove bogus "lablgtk" dependency.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-15
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-14
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-13
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-12
- OCaml 4.08.1 (final) rebuild.

* Sat Aug 10 2019 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-11
- Rebuild against new ocaml-lablgtk.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-10
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-6
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-5
- OCaml 4.07.0-rc1 rebuild.

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 4.2.5-4
- Rebuild (giflib)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.2.5-3
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 22 2017 Richard W.M. Jones <rjones@redhat.com> - 4.2.5-1
- New upstream version 4.2.5.
- New version fixes compatibility with latest lablgtk.

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 4.2.4-2
- OCaml 4.06.0 rebuild.

* Wed Aug 09 2017 Richard W.M. Jones <rjones@redhat.com> - 4.2.4-1
- New upstream version 4.2.4.
- Replace opt test with ocaml_native_compiler.
- Pass -g option to ocamlopt so debuginfo is generated correctly.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 4.2.2-7
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 4.2.2-4
- OCaml 4.04.2 rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 4.2.2-3
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 4.2.2-1
- New upstream version 4.2.2.
- Drop patch for exif handling which is included upstream.
- Drop patch for warn-error since this is fixed upstream.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 16 2015 Bruno Wolff III <bruno@wolff.to> - 4.1.0-18
- devel shouldn't cover all doc files

* Tue Aug 11 2015 Bruno Wolff III <bruno@wolff.to> - 4.1.0-17
- Don't use %%doc to copy over htmlref for -devel package

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-16
- Bump release and rebuild.

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-15
- OCaml 4.02.3 rebuild.

* Wed Jul 22 2015 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-14
- Enable bytecode compilation.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-13
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-12
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-10
- ocaml-4.02.1 rebuild.

* Fri Oct 31 2014 Bruno Wolff III <bruno@wolff.to> - 4.1.0-9
- Rebuild to link with updated dependencies

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-8
- ocaml-4.02.0 final rebuild.

* Tue Aug 19 2014 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-7
- Kill -warn-error A so we can build on OCaml 4.02.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 15 2014 Bruno Wolff III <bruno@wolff.to> - 4.1.0-5
- Rebuild for ocaml update

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 25 2013 Ville Skyttä <ville.skytta@iki.fi> - 4.1.0-3
- Fix -debuginfo, enable exif and rgb.txt support (#1009155).

* Fri Sep 27 2013 Bruno Wolff III <bruno@wolff.to> - 4.1.0-2
- Try to get actual debug output

* Sun Sep 15 2013 Bruno Wolff III <bruno@wolff.to> - 4.1.0-1
- Update to 4.1.0
- Enable debug output
- Patch for recent libpng is no longer needed

* Sat Sep 14 2013 Bruno Wolff III <bruno@wolff.to> - 4.0.1-13
- Rebuild for OCaml 4.01.0

* Sun Aug 11 2013 Bruno Wolff III <bruno@wolff.to> - 4.0.1-12
- Move to unversioned doc directory
- Fixes FTBFS bug 992390

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 4.0.1-9
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 4.0.1-8
- rebuild against new libjpeg

* Wed Oct 17 2012 Bruno Wolff III <bruno@wolff.to> - 4.0.1-7
- Rebuild for ocaml 4.0.1

* Sun Jul 29 2012 Bruno Wolff III <bruno@wolff.to> - 4.0.1-6
- Rebuild for ocaml 4.0.0 final

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Bruno Wolff III <bruno@wolff.to> - 4.0.1-4
- Rebuild for new ocaml

* Fri May 11 2012 Bruno Wolff III <bruno@wolff.to> - 4.0.1-3
- Rebuild for new libtiff

* Sat Mar 10 2012 Bruno Wolff III <bruno@wolff.to> - 4.0.1-2
- Fixup "should fixes" from review

* Sun Jan 29 2012 Bruno Wolff III <bruno@wolff.to> - 4.0.1-1
- Resurrect ocaml-camlimages
