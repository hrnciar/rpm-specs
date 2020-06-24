%{!?octave_api:%global octave_api %(octave-config -p API_VERSION || echo 0)}
# Set to bcond_with or use --without doc to disable doc build
%bcond_without doc
# Set to bcond_with or use --without octave to disable octave support
%if 0%{?el7}%{?el8}
# EL7 has too old of a swig - https://bugzilla.redhat.com/show_bug.cgi?id=1136487
# EL8 has too old of a swig - https://bugzilla.redhat.com/show_bug.cgi?id=1753475
%bcond_with octave
%else
%bcond_without octave
%endif

# conditionalize Ada support
%ifnarch %{GNAT_arches}
%bcond_with ada
%else
%bcond_without ada
%endif

# conditionalize Ocaml support
%ifarch sparc64 s390 s390x
%bcond_with ocaml
%else
# Missing needed ocaml ppc64 packages on RHEL7 at the moment
%if 0%{?rhel} == 7 
%bcond_with ocaml
%else
%bcond_without ocaml
%endif
%endif

# Let's drop itcl for EPEL8
%if 0%{?rhel} >= 8
%bcond_with itcl
%else
%bcond_without itcl
%endif

#RHEL8 does not have X on s390x
%ifarch s390x
%if 0%{?el8}
%bcond_with check
%else
%bcond_without check
%endif
%else
%bcond_without check
%endif

%global commit 48a56ee63d25d24eeb44f392025953a6e9cc6b3f

Name:           plplot
Version:        5.15.0
Release:        13%{?dist}
Summary:        Library of functions for making scientific plots

License:        LGPLv2+
URL:            http://plplot.sourceforge.net/
Source0:        http://downloads.sourceforge.net/plplot/%{name}-%{version}.tar.gz
#Source0:        https://sourceforge.net/code-snapshots/git/p/pl/plplot/plplot.git/plplot-plplot-%{commit}.zip
Source1:        xorg.conf
# Drop -mieee-fp
Patch0:         plplot-ieee.patch
Patch2:         plplot-multiarch.patch
# Upstream patch to fix in-tree ocaml rpath - plplot-5.15.0-37-g6b215267e
Patch3:         plplot-ocaml-rpath.patch
# Don't use -custom with ocamlc
Patch7:         plplot-ocaml.patch
# Fix safe-string new default in OCaml 4.06.
Patch9:         plplot-5.12.0-safe-string.patch


BuildRequires:  cmake >= 3.13.2
BuildRequires:  libtool-ltdl-devel
BuildRequires:  gcc-gfortran
%if %{with ada}
BuildRequires:  gcc-gnat
BuildRequires:  lapack-devel
%endif
BuildRequires:  swig
%if %{with octave}
BuildRequires:  octave-devel
%global build_octave -DTRY_OCTAVE4=ON
%else
Obsoletes:      %{name}-octave < %{version}-%{release}
%global build_octave -DENABLE_octave:BOOL=OFF
%endif
BuildRequires:  java-devel
BuildRequires:  freetype-devel, qhull-devel , ncurses-devel
BuildRequires:  gd-devel, tcl-devel, tk-devel
%if %{with itcl}
BuildRequires:  itcl-devel, itk-devel
BuildRequires:  iwidgets
%endif
BuildRequires:  python3-devel, python3-numpy
BuildRequires:  perl(XML::DOM), lasi-devel, wxGTK3-devel
BuildRequires:  gnu-free-mono-fonts
BuildRequires:  gnu-free-sans-fonts
BuildRequires:  gnu-free-serif-fonts
%if %{with doc}
BuildRequires:  docbook2X
BuildRequires:  doxygen
BuildRequires:  texlive-xmltex
BuildRequires:  tex(ulem.sty)
# RHEL8 does not ship xmlto-tex
%if 0%{?fedora} || ( 0%{?rhel} && 0%{?rhel} <= 7 )
BuildRequires:  xmlto-tex
%else
BuildRequires:  xmlto
%endif
%endif
%if %{with ocaml}
BuildRequires:  ocaml
# ocaml cairo support disabled upstream
# BuildRequires:  ocaml-cairo-devel
BuildRequires:  ocaml-camlidl-devel
BuildRequires:  ocaml-findlib
%if ! ( 0%{?rhel} >= 8 )
BuildRequires:  ocaml-lablgtk-devel
%endif
BuildRequires:  ocaml-ocamldoc
%endif
BuildRequires:  libharu-devel
BuildRequires:  lua-devel
BuildRequires:  cmake(qt5gui)
BuildRequires:  cmake(qt5printsupport)
BuildRequires:  cmake(Qt5Svg)
#For pyqt5
BuildRequires:  python3-qt5-devel
BuildRequires:  shapelib-devel
# For %check
%if %{with check}
BuildRequires:  xorg-x11-drv-dummy
BuildRequires:  mesa-dri-drivers
%endif
BuildRequires:  chrpath
Requires:       gnu-free-mono-fonts
Requires:       gnu-free-sans-fonts
Requires:       gnu-free-serif-fonts
Requires:       python3-numpy


%description
PLplot is a library of functions that are useful for making scientific
plots.

PLplot can be used from within compiled languages such as C, C++,
FORTRAN and Java, and interactively from interpreted languages such as
Octave, Python, Perl and Tcl.

The PLplot library can be used to create standard x-y plots, semilog
plots, log-log plots, contour plots, 3D surface plots, mesh plots, bar
charts and pie charts. Multiple graphs (of the same or different sizes)
may be placed on a single page with multiple lines in each graph.

A variety of output file devices such as Postscript, png, jpeg, LaTeX
and others, as well as interactive devices such as xwin, tk, xterm and
Tektronics devices are supported. New devices can be easily added by
writing a small number of device dependent routines.

There are almost 2000 characters in the extended character set. This
includes four different fonts, the Greek alphabet and a host of
mathematical, musical, and other symbols. Some devices supports its own
way of dealing with text, such as the Postscript and LaTeX drivers, or
the png and jpeg drivers that uses the Freetype library.


%package        libs
Summary:        Libraries for PLplot
Requires:       %{name}-data = %{version}-%{release}
Obsoletes:      %{name}-perl < 5.14.0-8

%description    libs
%{summary}.


%package        data
Summary:        Data files for PLplot
BuildArch:      noarch

%description    data
%{summary}.


%package        devel
Summary:        Development headers and libraries for PLplot
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
%{summary}.


%package        doc
Summary:        Documentation for PLplot
# Conditional OCaml support prevents this
#BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
%{summary}.


%if %{with ada}
%package        ada
Summary:        Functions for scientific plotting with Ada
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    ada
%{summary}.

%package        ada-devel
Summary:        Development files for using PLplot Ada bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-ada%{?_isa} = %{version}-%{release}
Requires:       gcc-gnat

%description    ada-devel
%{summary}.
%endif


%package        fortran-devel
Summary:        Development files for using PLplot Fortran bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%if 0%{?fedora}
Requires:       gcc-gfortran%{_isa}
%else
Requires:       gcc-gfortran
%endif

%description    fortran-devel
%{summary}.


%package        java
Summary:        Functions for scientific plotting with Java
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if 0%{?fedora} >= 20 || 0%{?rhel} >= 7
Requires:       java-headless
%else
Requires:       java
%endif

%description    java
%{summary}.

%package        java-devel
Summary:        Development files for using PLplot GNOME
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-java%{?_isa} = %{version}-%{release}

%description    java-devel
%{summary}.


%package        lua
Summary:        Functions for scientific plotting with Lua
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       lua

%description    lua
%{summary}.


%if %{with ocaml}
%package        -n ocaml-plplot
Summary:        Functions for scientific plotting with OCaml
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       plplot-ocaml = %{version}-%{release}
Obsoletes:      plplot-ocaml < 5.9.10-3

%description    -n ocaml-plplot
%{summary}.


%package        -n ocaml-plplot-devel
Summary:        Development files for PLplot OCaml
Requires:       ocaml-plplot%{?_isa} = %{version}-%{release}
Provides:       plplot-ocaml-devel = %{version}-%{release}
Obsoletes:      plplot-ocaml-devel < 5.9.10-3

%description    -n ocaml-plplot-devel
%{summary}.
%endif


%if %{with octave}
%package        octave
Summary:        Functions for scientific plotting with Octave
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       octave(api) = %{octave_api}

%description    octave
%{summary}.
%endif


%package        pyqt
Summary:        Functions for scientific plotting with PyQt
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    pyqt
%{summary}.


%package        qt
Summary:        Functions for scientific plotting with Qt
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    qt
%{summary}.

%package        qt-devel
Summary:        Development files for using PLplot with Qt
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-qt%{?_isa} = %{version}-%{release}
Requires:       qt-devel%{?_isa}

%description    qt-devel
%{summary}.


%package        tk
Summary:        Functions for scientific plotting with Tk
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tk
%{summary}.

%package        tk-devel
Summary:        Development files for using PLplot with Tk
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-tk%{?_isa} = %{version}-%{release}
Requires:       tk-devel%{?_isa}

# Do not check any tk examples requires
%global __requires_exclude_from ^%{_datadir}/plplot%{version}/examples/tk/tk.*$

%description    tk-devel
%{summary}.


%package        wxGTK
Summary:        Functions for scientific plotting with wxGTK
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    wxGTK
%{summary}.

%package        wxGTK-devel
Summary:        Development files for using PLplot with wxGTK
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-wxGTK%{?_isa} = %{version}-%{release}
Requires:       wxGTK3-devel%{?_isa}

%description    wxGTK-devel
%{summary}.


%prep
%setup -q
%patch0 -p1 -b .ieee
%patch2 -p1 -b .multiarch
%patch3 -p1 -b .ocaml-rpath
%patch7 -p1 -b .ocaml
%patch9 -p1 -b .safestring
sed -i -e s/5.2/5.3/ cmake/modules/lua.cmake


%build
mkdir fedora
cd fedora
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
export FFLAGS="$RPM_OPT_FLAGS"
# Needed for octave output to not have control characters
unset TERM
printenv
# We assume that tk version is the same as tcl, cannot check without DISPLAY
tkver=$(echo 'puts [info patchlevel]; exit' | tclsh)
%if %{with itcl}
# Hacks to determine versions without DISPLAY
itclver=$(echo %{_libdir}/libitcl*.so | sed -e 's/.*itcl\([0-9.]*\)\.so/\1/')
itkver=$(echo %{_libdir}/libitk*.so | sed -e 's/.*itk\([0-9.]*\)\.so/\1/')
iwidgetsver=$(echo %{_datadir}/tcl*/iwidgets* | sed -e 's/.*iwidgets//')
%endif
%cmake .. \
        -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
        -DFORTRAN_MOD_DIR:PATH=%{_fmoddir} \
        -DUSE_RPATH:BOOL=OFF \
        -DENABLE_ada:BOOL=ON \
        -DENABLE_d:BOOL=ON \
%if %{with itcl}
        -DENABLE_itcl:BOOL=ON \
        -DENABLE_itk:BOOL=ON \
        -DPLPLOT_ITCL_VERSION=$itclver \
        -DPLPLOT_ITK_VERSION=$itkver \
        -DIWIDGETS_VERSIONS_LIST:STRING="$iwidgetsver;$itkver;$itclver" \
        -DUSE_INCRTCL_VERSION_4:BOOL=ON \
%endif
        -DENABLE_lua:BOOL=ON \
        -DENABLE_ocaml:BOOL=ON \
        -DOCAML_INSTALL_DIR:PATH=`ocamlc -where` \
        %{build_octave} \
        -DENABLE_tk:BOOL=ON \
        -DJAVAWRAPPER_DIR:PATH="%{_libdir}/plplot%{version}" \
        -DNON_TRANSITIVE:BOOL=ON \
        -DPL_FREETYPE_FONT_PATH:PATH="/usr/share/fonts/gnu-free" \
        -DPLD_aqt:BOOL=ON \
        -DPLD_ntk:BOOL=ON \
        -DPLD_pstex:BOOL=ON \
        -DPLD_svg:BOOL=ON \
        -DPLD_wxwidgets:BOOL=ON \
        -DPLPLOT_TK_VERSION=$tkver \
        -DPLPLOT_USE_QT5=ON \
%if %{with doc}
        -DXML_DECL:FILEPATH=/usr/share/sgml/xml.dcl \
        -DBUILD_DOC:BOOL=ON \
        -DBUILD_DOX_DOC:BOOL=ON \
%else
        -DPREBUILT_DOC:BOOL=ON \
%endif
        -DBUILD_TEST:BOOL=ON

%make_build VERBOSE=1


%install
cd fedora
%make_install

# Fix up tclIndex files so they are the same on all builds
#for file in $RPM_BUILD_ROOT%{_datadir}/plplot%{version}/examples/*/tclIndex
#do
   #grep '^[# ]' ${file} > tclIndex.hd
   #grep -v '^[# ]' ${file} | sort > tclIndex
   #cat tclIndex.hd tclIndex > ${file}
#done

#Don't pull in script interpreters for example binaries
find $RPM_BUILD_ROOT%{_datadir}/plplot%{version}/examples -type f | xargs chmod -x

%if %{with ocaml}
# Bug in ocamlmklib http://caml.inria.fr/mantis/view.php?id=5943
chrpath -d $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs/dllpl*_stubs.so
%endif


%if %{with check}
%check
cd fedora
cp %SOURCE1 .
if [ -x /usr/libexec/Xorg ]; then
   Xorg=/usr/libexec/Xorg
else
   Xorg=/usr/libexec/Xorg.bin
fi
$Xorg -noreset +extension GLX +extension RANDR +extension RENDER -logfile ./xorg.log -config ./xorg.conf -configdir . :99 &
export DISPLAY=:99
# Exclude ocaml from ppc/ppc64/ppc64le, arm
%ifarch ppc ppc64 ppc64le
ctest -V -E 'ocaml|octave'
%else
%ifarch %{arm} aarch64
ctest -V -E 'java|ocaml|octave'
%else
%ifarch s390x
# Most tests are segfaulting on s390x for some reason in F32+
ctest -V || :
%else
# Octave tests are failing, ignore for now
ctest -V -E 'octave'
# Keep tabs on them though
ctest -V -R 'octave' || :
%endif
%endif
%endif
%endif


%files
%{_bindir}/pltek
%{_bindir}/pstex2eps
%{python3_sitearch}/_plplotc.so
%{python3_sitearch}/plplot.py*
%{python3_sitearch}/plplotc.py*
%{python3_sitearch}/Plframe.py*
%{python3_sitearch}/TclSup.py*
%{python3_sitearch}/__pycache__/plplot.*
%{python3_sitearch}/__pycache__/plplotc.*
%{python3_sitearch}/__pycache__/Plframe.*
%{python3_sitearch}/__pycache__/TclSup.*
%{_infodir}/plplotdoc.info*
%{_mandir}/man1/pltek.1.gz
%{_mandir}/man1/pstex2eps.1.gz
%doc %dir %{_datadir}/plplot%{version}/examples
%doc %{_datadir}/plplot%{version}/examples/plplot-test.sh
%doc %{_datadir}/plplot%{version}/examples/plplot-test-interactive.sh
%doc %{_datadir}/plplot%{version}/examples/python/
%doc %{_datadir}/plplot%{version}/examples/test_python.sh
%doc %{_datadir}/plplot%{version}/examples/Chloe.pgm
%doc %{_datadir}/plplot%{version}/examples/README.Chloe

%files libs
%doc COPYING.LIB Copyright
%{_libdir}/libcsirocsa.so.0*
%{_libdir}/libcsironn.so.0*
%{_libdir}/libplplotcxx.so.15*
%{_libdir}/libplplot.so.17*
%{_libdir}/libplplotfortran.so.0*
%{_libdir}/libqsastime.so.0*
%dir %{_libdir}/plplot%{version}
%dir %{_libdir}/plplot%{version}/drivers
%{_libdir}/plplot%{version}/drivers/cairo.so
%{_libdir}/plplot%{version}/drivers/cairo.driver_info
%{_libdir}/plplot%{version}/drivers/mem.so
%{_libdir}/plplot%{version}/drivers/mem.driver_info
%{_libdir}/plplot%{version}/drivers/ntk.so
%{_libdir}/plplot%{version}/drivers/ntk.driver_info
%{_libdir}/plplot%{version}/drivers/null.so
%{_libdir}/plplot%{version}/drivers/null.driver_info
%{_libdir}/plplot%{version}/drivers/pdf.so
%{_libdir}/plplot%{version}/drivers/pdf.driver_info
%{_libdir}/plplot%{version}/drivers/ps.so
%{_libdir}/plplot%{version}/drivers/ps.driver_info
%{_libdir}/plplot%{version}/drivers/pstex.so
%{_libdir}/plplot%{version}/drivers/pstex.driver_info
%{_libdir}/plplot%{version}/drivers/psttf.so
%{_libdir}/plplot%{version}/drivers/psttf.driver_info
%{_libdir}/plplot%{version}/drivers/svg.so
%{_libdir}/plplot%{version}/drivers/svg.driver_info
%{_libdir}/plplot%{version}/drivers/xfig.so
%{_libdir}/plplot%{version}/drivers/xfig.driver_info
%{_libdir}/plplot%{version}/drivers/xwin.so
%{_libdir}/plplot%{version}/drivers/xwin.driver_info

%files data
%dir %{_datadir}/plplot%{version}
%{_datadir}/plplot%{version}/*.fnt
%{_datadir}/plplot%{version}/*.pal
%{_datadir}/plplot%{version}/*.sh*
%{_datadir}/plplot%{version}/ss/

%files devel
%{_includedir}/plplot/
%exclude %{_includedir}/plplot/pltcl.h
%exclude %{_includedir}/plplot/pltk.h
%exclude %{_includedir}/plplot/qt.h
%exclude %{_includedir}/plplot/wx*
%{_libdir}/cmake/plplot/
%{_libdir}/libcsirocsa.so
%{_libdir}/libcsironn.so
%{_libdir}/libplplotcxx.so
%{_libdir}/libplplot.so
%{_libdir}/libqsastime.so
%{_libdir}/pkgconfig/plplot.pc
%{_libdir}/pkgconfig/plplot-c++.pc
%doc %{_datadir}/plplot%{version}/examples/CMakeLists.txt
%doc %{_datadir}/plplot%{version}/examples/CTest*
%doc %dir %{_datadir}/plplot%{version}/examples/cmake
%doc %dir %{_datadir}/plplot%{version}/examples/cmake/modules
%doc %{_datadir}/plplot%{version}/examples/cmake/modules/language_support.cmake
%if %{with ada}
%doc %{_datadir}/plplot%{version}/examples/cmake/modules/language_support/
%endif
%doc %{_datadir}/plplot%{version}/examples/cmake/modules/pkg-config.cmake
%doc %{_datadir}/plplot%{version}/examples/cmake/modules/plplot_configure.cmake
%doc %{_datadir}/plplot%{version}/examples/cmake/modules/plplot_functions.cmake
%doc %{_datadir}/plplot%{version}/examples/c/
%doc %{_datadir}/plplot%{version}/examples/c++/
%doc %{_datadir}/plplot%{version}/examples/Makefile
%doc %{_datadir}/plplot%{version}/examples/plplot_test/
%doc %{_datadir}/plplot%{version}/examples/test_c.sh
%doc %{_datadir}/plplot%{version}/examples/test_c_interactive.sh
%doc %{_datadir}/plplot%{version}/examples/test_cxx.sh
%doc %{_datadir}/plplot%{version}/examples/test_diff.sh

%{_mandir}/man3/pl*.3*

%files doc
%{_docdir}/%{name}/

%if %{with ada}
%files ada
%{_libdir}/libplplotada.so.4*

%files ada-devel
#Until we find an owner for %{_libdir}/ada/adalib/
%{_libdir}/ada/
#%{_libdir}/ada/adalib/plplotadad/
%{_libdir}/libplplotada.so
%{_libdir}/pkgconfig/plplot-ada.pc
#Until we find an owner for %{_datadir}/ada/adainclude/
%{_datadir}/ada/
#%{_datadir}/ada/adainclude/plplotadad/
%doc %{_datadir}/plplot%{version}/examples/ada/
%doc %{_datadir}/plplot%{version}/examples/test_ada.sh
%endif

%files fortran-devel
%{_fmoddir}/plfortrandemolib.mod
%{_fmoddir}/plplot.mod
%{_fmoddir}/plplot_double.mod
%{_fmoddir}/plplot_graphics.mod
%{_fmoddir}/plplot_private_exposed.mod
%{_fmoddir}/plplot_private_utilities.mod
%{_fmoddir}/plplot_single.mod
%{_fmoddir}/plplot_types.mod
%{_libdir}/libplplotfortran.so
%{_libdir}/libplfortrandemolib.a
%{_libdir}/pkgconfig/plplot-fortran.pc
%doc %{_datadir}/plplot%{version}/examples/fortran/
%doc %{_datadir}/plplot%{version}/examples/test_fortran.sh

%files java
%{_libdir}/plplot%{version}/libplplotjavac_wrap.so
%{_datadir}/java/plplot.jar

%files java-devel
%doc %{_datadir}/plplot%{version}/examples/java/
%doc %{_datadir}/plplot%{version}/examples/test_java.sh

%files lua
%if 0%{?fedora} || 0%{?rhel} >= 8
%{_libdir}/lua/plplot/
%else
%{_libdir}/lua/*/plplot/
%endif
%doc %{_datadir}/plplot%{version}/examples/lua/
%doc %{_datadir}/plplot%{version}/examples/test_lua.sh

%if %{with ocaml}
%files -n ocaml-plplot
# %%dir %%{_libdir}/ocaml/plcairo/
# %%{_libdir}/ocaml/plcairo/META
# %%{_libdir}/ocaml/plcairo/*.cma
# %%{_libdir}/ocaml/plcairo/*.cmi
%dir %{_libdir}/ocaml/plplot/
%{_libdir}/ocaml/plplot/META
%{_libdir}/ocaml/plplot/*.cma
%{_libdir}/ocaml/plplot/*.cmi
%{_libdir}/ocaml/stublibs/*

%files -n ocaml-plplot-devel
%{_libdir}/pkgconfig/plplot-ocaml.pc
# %%{_libdir}/ocaml/plcairo/*.a
# %%{_libdir}/ocaml/plcairo/*.cmxa
# %%{_libdir}/ocaml/plcairo/plcairo.mli
%{_libdir}/ocaml/plplot/*.a
%{_libdir}/ocaml/plplot/*.cmx*
%{_libdir}/ocaml/plplot/plplot.mli
%doc %{_datadir}/plplot%{version}/examples/ocaml/
%doc %{_datadir}/plplot%{version}/examples/test_ocaml.sh
%endif

%if %{with octave}
%files octave
%{_datadir}/plplot_octave/
%{_datadir}/octave/site/m/PLplot/
%{_libdir}/octave/site/oct/*/plplot_octave.oct
%doc %{_datadir}/plplot%{version}/examples/octave/
%doc %{_datadir}/plplot%{version}/examples/test_octave.sh
%doc %{_datadir}/plplot%{version}/examples/test_octave_interactive.sh
%endif

%files pyqt
%{python3_sitearch}/plplot_pyqt5.so

%files qt
%{_libdir}/libplplotqt.so.2*
%{_libdir}/plplot%{version}/drivers/qt.so
%{_libdir}/plplot%{version}/drivers/qt.driver_info

%files qt-devel
%{_includedir}/plplot/qt.h
%{_libdir}/libplplotqt.so
%{_libdir}/pkgconfig/plplot-qt.pc
%doc %{_datadir}/plplot%{version}/examples/cmake/modules/ndp_UseQt4.cmake

%files tk
%{_bindir}/plserver
%{_bindir}/pltcl
%{_libdir}/libplplottcltk.so.14*
%{_libdir}/libplplottcltk_Main.so.1*
%{_libdir}/libtclmatrix.so.10*
%{_libdir}/plplot%{version}/drivers/tk.so
%{_libdir}/plplot%{version}/drivers/tk.driver_info
%{_libdir}/plplot%{version}/drivers/tkwin.so
%{_libdir}/plplot%{version}/drivers/tkwin.driver_info
%{python3_sitearch}/_Pltk_init.so
%{python3_sitearch}/Pltk_init.py
%{python3_sitearch}/__pycache__/Pltk_init.*

%{_datadir}/plplot%{version}/pkgIndex.tcl
%doc %{_datadir}/plplot%{version}/examples/test_tcl.sh
%doc %{_datadir}/plplot%{version}/examples/tcl/
%doc %{_datadir}/plplot%{version}/examples/tk/
%{_datadir}/plplot%{version}/tcl/
%{_mandir}/man1/plserver.1.gz
%{_mandir}/man1/pltcl.1.gz

%files tk-devel
%{_includedir}/plplot/pltcl.h
%{_includedir}/plplot/pltk.h
%{_libdir}/libplplottcltk.so
%{_libdir}/libplplottcltk_Main.so
%{_libdir}/libtclmatrix.so
%{_libdir}/pkgconfig/plplot-tcl.pc
%{_libdir}/pkgconfig/plplot-tcl_Main.pc

%files wxGTK
%{_bindir}/wxPLViewer
%{_libdir}/libplplotwxwidgets.so.1*
%{_libdir}/plplot%{version}/drivers/wxwidgets.so
%{_libdir}/plplot%{version}/drivers/wxwidgets.driver_info

%files wxGTK-devel
%{_includedir}/plplot/wx*
%{_libdir}/libplplotwxwidgets.so
%{_libdir}/pkgconfig/plplot-wxwidgets.pc


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.15.0-13
- Rebuilt for Python 3.9

* Fri May 22 2020 Richard W.M. Jones <rjones@redhat.com> - 5.15.0-12
- Rebuild against camlidl 1.09.
  https://github.com/xavierleroy/camlidl/issues/18

* Wed May 06 2020 Orion Poplawski <orion@nwra.com> - 5.15.0-11
- Use cmake qt5 BuildRequires

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 5.15.0-10
- Bump and rebuild for OCaml 4.11.0+dev2-2020-04-22 rebuild.

* Wed Mar 11 2020 Orion Poplawski <orion@nwra.com> - 5.15.0-9
- Ignore failing tests on s390x

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 5.15.0-8
- OCaml 4.10.0 final.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 5.15.0-6
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 5.15.0-5
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 5.15.0-4
- OCaml 4.09.0 (final) rebuild.

* Thu Nov 07 2019 Orion Poplawski <orion@nwra.com> - 5.15.0-3
- Rebuild with octave 64bit indexes

* Wed Oct 02 2019 Orion Poplawski <orion@nwra.com> - 5.15.0-2
- Rebuild for lasi 1.1.3 soname bump

* Sun Sep 29 2019 Orion Poplawski <orion@nwra.com> - 5.15.0-1
- Update to 5.15.0

* Thu Sep 19 2019 Orion Poplawski <orion@nwra.com> - 5.14.0-8
- Drop octave and itcl for EPEL8
- Drop perl dummy package

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.14.0-7
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 5.14.0-6
- OCaml 4.08.1 (final) rebuild.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 5.14.0-5
- OCaml 4.08.1 (rc2) rebuild.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 5.14.0-3
- Rebuild for octave 5.1

* Tue May 7 2019 Orion Poplawski <orion@nwra.com> - 5.14.0-2
- Apply upstream patch to fix swig 4 compatability

* Sat Feb 9 2019 Orion Poplawski <orion@nwra.com> - 5.14.0-1
- Update to 5.14.0
- Drop noarch docs, different arch components

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Orion Poplawski <orion@cora.nwra.com> - 5.13.0-2
- Rebuild for octave 4.4

* Mon Jul 23 2018 Orion Poplawski <orion@nwra.com> - 5.13.0-1
- Update to 5.13.0
- Switch to python3
- Drop ldconfig and install-info scriptlets

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 5.12.0-12
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 5.12.0-11
- OCaml 4.07.0-rc1 rebuild.

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.12.0-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Christian Dersch <lupinix@mailbox.org> - 5.12.0-8
- rebuilt for GCC 8.x (gfortran so-version bump)

* Tue Dec 12 2017 Orion Poplawski <orion@nwra.com> - 5.12.0-7
- Drop -mieee-fp - libieee.a is no more

* Sat Nov 18 2017 Richard W.M. Jones <rjones@redhat.com> - 5.12.0-6
- OCaml 4.06.0 rebuild.
- Fix safe-string in OCaml >= 4.06.

* Wed Aug 09 2017 Richard W.M. Jones <rjones@redhat.com> - 5.12.0-5
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 5.12.0-2
- OCaml 4.04.2 rebuild.

* Wed Jun 21 2017 Tom Callaway <spot@fedoraproject.org> - 5.12.0-1
- update to 5.12.0
- resolves licensing issue (bz1295175)

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 5.11.1-15
- OCaml 4.04.1 rebuild.

* Wed May 03 2017 Petr Pisar <ppisar@redhat.com> - 5.11.1-14
- Build on s390x (bug #1447529)

* Wed Feb 01 2017 Orion Poplawski <orion@cora.nwra.com> - 5.11.1-13
- Rebuild for gcc 7

* Tue Jan 17 2017 Orion Poplawski <orion@cora.nwra.com> - 5.11.1-12
- Re-enable octave support in F26

* Thu Jan 5 2017 Orion Poplawski <orion@cora.nwra.com> - 5.11.1-11
- Drop octave support in F26 - swig does not yet support octave 4.2
- Add patch for cmake 3.7 support

* Sun Dec 11 2016 Igor Gnatenko <ignatenko@redhat.com> - 5.11.1-10
- Rebuild for shapelib SONAME bump

* Mon Nov 14 2016 Richard W.M. Jones <rjones@redhat.com> - 5.11.1-9
- Rebuild again for OCaml 4.04.0.

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 5.11.1-8
- Rebuild for OCaml 4.04.0.

* Tue Jul 19 2016 Orion Poplawski <orion@cora.nwra.com> - 5.11.1-7
- Split out font and other data into sub-package, make libs require it (bug #1130326)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11.1-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Apr 30 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 5.11.1-5
- Rebuild for qhull-2015.2-1.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Orion Poplawski <orion@cora.nwra.com> - 5.11.1-3
- Rebuild for gcc 6

* Fri Oct 30 2015 Orion Poplawski <orion@cora.nwra.com> - 5.11.1-2
- Add patch for cmake 3.4 support

* Wed Aug 12 2015 Orion Poplawski <orion@cora.nwra.com> - 5.11.1-1
- Update to 5.11.1
- Drop pkgconfig and swig patches applied upstream

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 5.11.0-8
- OCaml 4.02.3 rebuild.

* Fri Jul 24 2015 Richard W.M. Jones <rjones@redhat.com> - 5.11.0-7
- Bump and rebuild for ocaml-cairo.

* Sat Jul 11 2015 Orion Poplawski <orion@cora.nwra.com> - 5.11.0-6
- Add patch for swig 3.0.6 support
- Drop requires for libgnomprint22-devel and libgnomecanvas-devel
  from plplot-devel (bug #1242125)

* Tue Jul 07 2015 Orion Poplawski <orion@cora.nwra.com> - 5.11.0-5
- Rebuild for octave 4.0

* Fri Jun 19 2015 Richard W.M. Jones <rjones@redhat.com> - 5.11.0-4
- Rebuild for ocaml-4.02.2.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 22 2015 Orion Poplawski <orion@cora.nwra.com> - 5.11.0-2
- Add patch to fix pkgconfig libs
- Drop ununsed patches

* Wed Apr 22 2015 Orion Poplawski <orion@cora.nwra.com> - 5.11.0-1
- Update to 5.11.0
- Use dummy X driver for tests
- Drop octave, lua, pkgconfig patches fixed upstream

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 5.10.0-18
- ocaml-4.02.1 rebuild.

* Fri Feb 06 2015 Orion Poplawski <orion@cora.nwra.com> - 5.10.0-17
- Rebuild for gcc ada soname bump
- Add patch for cmake 3.1 support
- Add patch for libgnat-5 support
- Make plplot-devel require gtk2-devel, libgnomecanvas-devel, libgnomeprint22-devel
- Move qt header to plplot-qt-devel and make it require qt-devel
- Move tcl/tk headers to plplot-tk-devel and make it require tk-devel
- Move wx headers to plplot-wxGTK-devel and make it require wxGTK-devel

* Fri Sep 12 2014 Orion Poplawski <orion@cora.nwra.com> - 5.10.0-16
- Exclude ocaml tests on ppc64le (bug #1140767)

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 5.10.0-15
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 5.10.0-14
- Bump release and rebuild.

* Sat Aug 23 2014 Orion Poplawski <orion@cora.nwra.com> - 5.10.0-13
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 4 2014 Orion Poplawski <orion@cora.nwra.com> - 5.10.0-11
- Rebuild for ocaml-4.02.0-0.8.git10e45753.fc22

* Mon Jul 14 2014 Orion Poplawski <orion@cora.nwra.com> - 5.10.0-10
- Rebuild for OCaml 4.02

* Mon Jun 9 2014 Orion Poplawski <orion@cora.nwra.com> - 5.10.0-9
- Add upstream patch to rename HAVE_CONFIG_H

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 5.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Tue May 20 2014 Peter Robinson <pbrobinson@fedoraproject.org> 5.10.0-6
- Fix aarch64 builds

* Tue May 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 5.10.0-5
- User GNAT_arches for Adda arch conditionals rather than specific list

* Thu Apr 10 2014 Orion Poplawski <orion@cora.nwra.com> - 5.10.0-4
- Rebuild for gcc 4.9.0

* Sat Mar 1 2014 Orion Poplawski <orion@cora.nwra.com> - 5.10.0-3
- Re-enable octave

* Mon Feb 24 2014 Orion Poplawski <orion@cora.nwra.com> - 5.10.0-2
- Requires java-headless (bug #1068488)

* Thu Feb 13 2014 Orion Poplawski <orion@cora.nwra.com> - 5.10.0-1
- Update to 5.10.0

* Mon Jan 6 2014 Orion Poplawski <orion@cora.nwra.com> - 5.9.11-3
- Drop octave support for now

* Sun Dec 29 2013 Orion Poplawski <orion@cora.nwra.com> - 5.9.11-2
- Add upstream patch to rename config.h to plplot_config.h

* Sun Dec 29 2013 Orion Poplawski <orion@cora.nwra.com> - 5.9.11-1
- Update to 5.9.11
- Rebase multiarch patch
- Drop upstream soperms, rpmlint patch

* Sat Dec 28 2013 Orion Poplawski <orion@cora.nwra.com> - 5.9.10-4
- Rebuild for octave 3.8.0

* Mon Oct 28 2013 Orion Poplawski <orion@cora.nwra.com> - 5.9.10-3
- Add upstream patch to fix ocaml and octave library permissions
- Add patch to fix various rpmlint issues
- Add patch to drop using -custom when building ocaml bindings
- Rename ocaml sub-packages
- Strip rpath from ocaml libs
- Add %%{?_isa} to requires

* Sun Oct 20 2013 Orion Poplawski <orion@cora.nwra.com> - 5.9.10-2
- Drop very old plplot-gnome obsoletes
- Mark examples as documentation

* Tue Oct 1 2013 Orion Poplawski <orion@cora.nwra.com> - 5.9.10-1
- Update to 5.9.10

* Thu Sep 26 2013 Orion Poplawski <orion@cora.nwra.com> - 5.9.9-22.svn12530
- Update to svn 12530
- Rework doc BRs

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 5.9.9-21.svn12479
- Rebuild for OCaml 4.01.0.

* Fri Aug 23 2013 Orion Poplawski <orion@cora.nwra.com> - 5.9.9-20.svn12479
- Remove unneeded libs from pkgconfig file (bug #998988)
- Remove unneeded requires from devel package

* Mon Aug 12 2013 Orion Poplawski <orion@cora.nwra.com> - 5.9.9-19.svn12479
- Update to svn 12479
- Drop destdir patch fixed upstream
- Build doxygen documentation
- Put documentation into separate -doc subpackage

* Wed Aug 7 2013 Orion Poplawski <orion@cora.nwra.com> - 5.9.9-18.svn12474
- Update to svn 12474
- Add patch to revert doc DESTDIR change

* Wed Aug 7 2013 Orion Poplawski <orion@cora.nwra.com> - 5.9.9-17.svn12281
- Use svn export to build source
- Enable shapelib support

* Wed Aug 7 2013 Orion Poplawski <orion@cora.nwra.com> - 5.9.9-16.svn12281
- Fix doc location
- Add patch for lua 5.2 support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.9-16.svn12281
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 21 2013 Peter Robinson <pbrobinson@fedoraproject.org> 5.9.9-15.svn12281
- Fix building on ARM

* Fri Jan 25 2013 Orion Poplawski <orion@cora.nwra.com> - 5.9.9-14.svn12281
- Rebuild for gcc 4.8

* Sat Dec 15 2012 Orion Poplawski <orion@cora.nwra.com> - 5.9.9-13.svn12281
- Update to svn 12281

* Fri Dec 14 2012 Orion Poplawski <orion@cora.nwra.com> - 5.9.9-12.svn12202
- Add patch from upstream to fix cmake handling

* Wed Oct 17 2012 Orion Poplawski <orion@cora.nwra.com> - 5.9.9-11.svn12202
- Rebuild for ocaml 4.00.1

* Thu Aug 9 2012 Orion Poplawski <orion@cora.nwra.com> - 5.9.9-10.svn12202
- Drop agg support

* Fri Aug 3 2012 Orion Poplawski <orion@cora.nwra.com> - 5.9.9-9.svn12202
- Update to svn 12202
- Rebase multiarch patch

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.9-8.svn12161
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 09 2012 Richard W.M. Jones <rjones@redhat.com> - 5.9.9-7.svn12161
- Rebuild for OCaml 4.00.0.

* Tue Feb 21 2012 Orion Poplawski <orion@cora.nwra.com> - 5.9.9-6.svn12161
- Define CMAKE_INSTALL_LIBDIR, removed from %%cmake macro

* Sat Jan 28 2012 Orion Poplawski <orion@cora.nwra.com> - 5.9.9-5.svn12161
- Update to svn 12161

* Mon Jan 16 2012 Orion Poplawski <orion@cora.nwra.com> - 5.9.9-4.svn12123
- Rebuild for octave 3.6.0
- Add patch to allow octave tests to be run in mock

* Fri Jan 13 2012 Orion Poplawski <orion@cora.nwra.com> - 5.9.9-3.svn12123
- Drop unneeded gnome BRs

* Fri Jan 6 2012 Orion Poplawski <orion@cora.nwra.com> - 5.9.9-2
- Update to svn 12123
- Update multiarch patch
- Drop gnat patch, fixed upstream
- Turn on non-transitive linking
- Drop some unused cmake options

* Tue Nov 1 2011 Orion Poplawski <orion@cora.nwra.com> - 5.9.9-1
- Update to 5.9.9

* Fri Sep 23 2011 Orion Poplawski <orion@cora.nwra.com> - 5.9.8-3
- Rebuild for lasi 1.1.1

* Wed Aug 17 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 5.9.8-2
- Fix FTBFS (gah).
- Drop pdl support for now, since it isn't used anyways by plplot.

* Mon Aug 8 2011 Orion Poplawski <orion@cora.nwra.com> - 5.9.8-1
- Update to 5.9.8
- Drop octave-config patch applied upstream
- Add BR mesa-dri-drivers to get swrast_dri.so for tests
- Drop converting files to UTF-8, they already are
- No longer need the xvfb-run xauth workaround

* Tue Apr 5 2011 Orion Poplawski <orion@cora.nwra.com> - 5.9.7-9
- Add patch to use octave-config to handle moved octave directories

* Mon Feb 21 2011 Orion Poplawski <orion@cora.nwra.com> - 5.9.7-8
- Re-enable epsqt, pdfqt, and svgqt tests.

* Mon Feb 14 2011 Orion Poplawski <orion@cora.nwra.com> - 5.9.7-7
- Disable epsqt, pdfqt, and svgqt tests.  Cannot reproduce failure outside of
  mock.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Orion Poplawski <orion@cora.nwra.com> - 5.9.7-5
- Rebuild for new libgnat
- Add patch for gnat 4.6 support

* Wed Jan 5 2011 Orion Poplawski <orion@cora.nwra.com> - 5.9.7-4
- Rebuild for new ocaml

* Mon Dec 27 2010 Orion Poplawski <orion@cora.nwra.com> - 5.9.7-3
- Don't use %%{_isa} in Requires for gcc-gfortran - not multilib in RHEL

* Tue Oct 12 2010 Orion Poplawski <orion@cora.nwra.com> - 5.9.7-2
- Don't pull in requires from examples
- Fail %%check section if tests fail

* Mon Oct 11 2010 Orion Poplawski <orion@cora.nwra.com> - 5.9.7-1
- Update to 5.9.7
- Rebase multiarch patch
- Drop info patch fixed upstream

* Mon Sep 6 2010 Dan Horák <dan@danny.cz> - 5.9.6-7
- conditionalize Ada and Ocaml support

* Fri Jul 30 2010 Orion Poplawski <orion@cora.nwra.com> - 5.9.6-6
- Add licenses to libs sub-package

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 5.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 5.9.6-4
- rebuilt against wxGTK-2.8.11-2

* Tue Jul 13 2010 - Orion Poplawski <orion@cora.nwra.com> - 5.9.6-3
- Turn off Ada 2007, not useful

* Thu Jul 8 2010 - Orion Poplawski <orion@cora.nwra.com> - 5.9.6-2
- Rebuild for new libgnat

* Wed Jul 7 2010 - Orion Poplawski <orion@cora.nwra.com> - 5.9.6-1
- Update to 5.9.6

* Thu Jan 14 2010 - Orion Poplawski <orion@cora.nwra.com> - 5.9.5-7
- Add BR lapack-devel for ada support
- Add more needed ocaml BRs, plcairo module is now built
- Drop jni patch, fixed with cmake option
- Re-enable qt tests - xvfb no longer crashes

* Wed Nov 25 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.9.5-6
- Update to svn 10696 to fix build issues

* Wed Nov 25 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 5.9.5-5
- Rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Fri Oct 30 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.9.5-4
- Update to svn 10561 to fix build issues
- Update test patch
- Remove obsoleted driver linuxvga

* Mon Oct 26 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.9.5-3
- Create fortran-devel sub-package with fortran development files (bug #523543)

* Thu Oct 22 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.9.5-2
- Move the python plplot_widgetmodule.so to the tk sub-package

* Mon Sep 28 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.9.5-1
- Update to 5.9.5
- Disable qt tests for now until Xvfb bug is fixed.
- Remove ocaml dep code for now - breaks other dep generation

* Wed Aug 26 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.9.4-8
- Update octave patch to hopefully fix remaining issue.
- Re-enable tests

* Wed Aug 26 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.9.4-7
- Add patch from svn to support pdl 2.4.4_05
- Force using gfortran

* Wed Aug 26 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 5.9.4-6
- Build with perl package re-enabled

* Wed Aug 26 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 5.9.4-5
- Temporarily disable check to fix broken deps in rawhide
- Attempt bootstrap build without pdl

* Thu Aug 13 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.9.4-4
- Add patch to support octave 3.2

* Sat Aug 01 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 5.9.4-3
- Rebuilt against updated Octave.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.9.4-1
- Update to 5.9.4
- Drop soversion patch applied upstream

* Mon May 4 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.9.3-2
- Also obsolete plplot-gnome-devel

* Mon May 4 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.9.3-1
- Update to 5.9.3
- Drop gnat-4.4 and f77 patches fixed upstream
- Updated multiarch and test patches
- Add patch to fix up libnistcd.so soversion
- Convert some doc files to UTF-8
- Add lua and lua-devel sub-packages
- Remove rpaths
- Drop gcw driver and pygcw/gnome bindings deprecated upstream
- Drop gd driver deprecated upstream
- Move ldconfig run to plplot-libs, and add to plplot-wxGTK

* Thu Apr 16 2009 Orion Poplawski <orion@cora.nwra.com>
- Only disable ocaml support on sparc64, s390, s390x

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Fri Mar 27 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.9.2-4
- Enable ada on ppc64 (resolves bug#241233)
- freefont is now gnu-free-{mono,sans,serif}-fonts

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.9.2-2
- Add patch to find gnat 4.4
- Add patch to fix f77 example
- Define HAVE_ADA_2007
- Add patch to allow users to run plplot-test.sh (bug #484519)
- Move more tcl files into tk package, examples into main tk package

* Mon Jan 26 2009 - Orion Poplawski <orion@cora.nwra.com> - 5.9.2-1
- Update to 5.9.2
- Need rpaths during build
- Explicitly enable tk, itcl, itk, and pygcw
- Update info and multiarch patches
- Re-enable perl tests
- Add proper ocaml provides/requires
- Add patch to handle newer octave

* Thu Dec  4 2008 Richard W.M. Jones <rjones@redhat.com> - 5.9.0-4.svn8985
- Rebuild for OCaml 3.11.0.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 5.9.0-3.svn8985
- Rebuild for Python 2.6

* Thu Nov 13 2008 - Orion Poplawski <orion@cora.nwra.com> - 5.9.0-2.svn8985
- Update to svn revision 8985
- Rebuild for libtool 2.2
- Change to use %%bcond_with/without
- Bootstrap build - without PDL

* Fri Sep 5 2008 - Orion Poplawski <orion@cora.nwra.com> - 5.9.0-2.svn8752
- Update to svn revision 8752
- Add new gnome-python2 BRs
- Update build_doc BRs
- Add ocaml sub-package for OCaml interface
- Enable "D" interface.
- Re-enable psttfc test, disable perl and compare tests

* Wed Feb 27 2008 - Orion Poplawski <orion@cora.nwra.com> - 5.9.0-1
- Update to 5.9.0
- Re-enable smp builds
- Add ada subpackage

* Fri Jan 18 2008 - Orion Poplawski <orion@cora.nwra.com> - 5.8.0-10
- Add Requries: libtool-ltdl-devel to devel package

* Tue Jan 15 2008 - Orion Poplawski <orion@cora.nwra.com> - 5.8.0-9
- Require numpy (bug #428876)
- Update SVN patch to add support for detecting Tcl version
- Look for itcl 3.4

* Sat Jan 12 2008 - Orion Poplawski <orion@cora.nwra.com> - 5.8.0-8
- Re-enable itcl

* Mon Jan  7 2008 - Orion Poplawski <orion@cora.nwra.com> - 5.8.0-7
- Update to latest svn for Tcl 8.5 support
- Don't build against itcl - does not support tcl 8.5

* Thu Jan  3 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 5.8.0-6
- Rebuild for new Tcl 8.5

* Sun Dec 23 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.8.0-5
- Rebuild for octave 3.0

* Fri Dec 14 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.8.0-4
- Rebuild for new octave api

* Wed Dec  5 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.8.0-3
- Updated multiarch patch for all language example makefiles (bug #342901)

* Thu Nov 29 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.8.0-2
- Rebuild for new octave api

* Mon Nov 19 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.8.0-1
- Update to 5.8.0

* Fri Nov  9 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.7.4-5
- Update to latest svn: adds cairo, drops plmeta, plrender
- Rebuild for new octave api

* Tue Oct 16 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.7.4-4
- Add patch from svn to fix octave bindings for octave 2.9.15, drop
  old version

* Thu Aug 23 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.7.4-3
- Add perl sub-package for PDL/plpot examples

* Thu Aug 23 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.7.4-2
- Rebuild for BuildID

* Tue Aug 14 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.7.4-1
- Update to 5.7.4
- Re-enable ada on x86_64
- Enable PDL tests
- Set HAVE_PTHREAD for the xwin driver

* Wed Aug  8 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.7.3-4
- BR numpy rather than python-numeric - doesn't do anything yet?

* Tue Aug  7 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.7.3-3
- Disable Ada interface on ppc64 until available (bug #241233)
- Add svn patch to fix ada bindings on x86_64 and other issues
- Add build_doc conditional to test doc builds
- Disable octave until plplot supports octave 2.9.11+
- Update license to LGPLv2+
- Exclude psttfc test until fixed

* Mon Apr 16 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.7.3-2
- Use cmake macros

* Mon Mar 26 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.7.3-1
- Update to 5.7.3
- Hack to run itcl examples
- Install Java JNI into %%{_libdir}/plplot%%{_version}
- java package requires java (bug #233905)
- devel requires main package (bug #233905)
- Enable octave api requirement
- Enable new ada interface - not installed yet though
- Renaable pstex driver

* Tue Mar 20 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.7.2-4
- Set PREBUILT_DOC so docs are installed

* Wed Mar 14 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.7.2-3
- Fix up tclIndex files so they are the same on all builds (bug #228172)
- Fix up examples/tk/Makefile for multilib (bug #228172)
- Install python in arch specific dirs (bug #228173)
- Enable itcl
- Update to CVS

* Fri Feb 09 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.7.2-2
- Rebuild for Tcl 8.5

* Tue Jan 23 2007 - Orion Poplawski <orion@cora.nwra.com> - 5.7.2-1
- Update to 5.7.2 which uses cmake
- Add patch to use -nopgcpp with swig java generation
- Enable more drivers

* Thu Dec 14 2006 - Jef Spaleta <jspaleta@gmail.com> - 5.6.1-9
- Bump and build for python 2.5

* Thu Nov  2 2006 - Orion Poplawski <orion@cora.nwra.com> - 5.6.1-8
- Point to the freefont package properly (bug #210517)
- Move libriaries to -libs, -devel requires -libs for multilib support
- Change BR on gnome-python2 to gnome-python2-devel

* Fri Oct  6 2006 - Orion Poplawski <orion@cora.nwra.com> - 5.6.1-7
- Rebuild for new octave API version

* Tue Oct  3 2006 - Orion Poplawski <orion@cora.nwra.com> - 5.6.1-6
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 25 2006 - Orion Poplawski <orion@cora.nwra.com> - 5.6.1-5
- Add needed Requires for -devel packages (bug #202168)
- Patch .info rather than .texi, and actually apply

* Mon Aug 28 2006 - Orion Poplawski <orion@cora.nwra.com> - 5.6.1-4
- Rebuild for new octave API version
- Add patch for texinfo file to fix category

* Mon Aug  7 2006 - Orion Poplawski <orion@cora.nwra.com> - 5.6.1-3
- Add BR ncurses-devel

* Mon Aug  7 2006 - Orion Poplawski <orion@cora.nwra.com> - 5.6.1-2
- Add patch to support octave 2.9.7 (bug #201443)

* Mon May 22 2006 - Orion Poplawski <orion@cora.nwra.com> - 5.6.1-1
- Update to 5.6.1
- Enable f95 bindings
- Remove patches applied upstream
- Now include pkgconfig files
- pstex driver no longer shipped

* Mon Apr 24 2006 - Orion Poplawski <orion@cora.nwra.com> - 5.6.0-1
- Update to 5.6.0 with new psttf driver
- Add wxGTK support

* Fri Feb 24 2006 - Orion Poplawski <orion@cora.nwra.com> - 5.5.3-12
- Rebuild for FC5 gcc/glibc changes

* Wed Feb  1 2006 - Orion Poplawski <orion@cora.nwra.com> - 5.5.3-11
- Package .pyc and .pyo files

* Thu Dec 22 2005 - Orion Poplawski <orion@cora.nwra.com> - 5.5.3-10
- Add patch to strip X check from configure for modular X
- Rework patches to patch configure and avoid autoconf
- Teporarily add BR on libXau-devel and libXdmcp (bz #176313)

* Thu Dec 15 2005 - Orion Poplawski <orion@cora.nwra.com> - 5.5.3-9
- Rebuild for gcc 4.1

* Tue Aug 30 2005 - Orion Poplawski <orion@cora.nwra.com> - 5.5.3-8
- Re-enable java on ppc - should be fixed in upstream rawhide

* Thu Aug 11 2005 - Orion Poplawski <orion@cora.nwra.com> - 5.5.3-7
- Breakout java into its own sub-package, don't build on non x86
- Add patch to fix c test on ppc

* Wed Aug 10 2005 - Orion Poplawski <orion@cora.nwra.com> - 5.5.3-6
- Add patch to find tcl on x86_64
- Add patch to use new octave in devel

* Tue Aug 09 2005 - Orion Poplawski <orion@cora.nwra.com> - 5.5.3-5
- Explicitly turn off unused features in configure
- rpmlint cleanup
- add make check

* Mon Aug 08 2005 - Orion Poplawski <orion@cora.nwra.com> - 5.5.3-4
- Remove smp build due to problems
- Add gnome-python2 BuildRequires

* Mon Aug 08 2005 - Orion Poplawski <orion@cora.nwra.com> - 5.5.3-3
- Split into multipe packages

* Mon Aug 08 2005 - Orion Poplawski <orion@cora.nwra.com> - 5.5.3-2
- Shorten summary
- Fix Source URL

* Thu Aug 04 2005 - Orion Poplawski <orion@cora.nwra.com> - 5.5.3-1
- Initial Fedora Extras release
