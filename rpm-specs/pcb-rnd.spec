# Build with --debug (1) or --symbols (0)
%global configure_debug       0
%global plugindir             %{_prefix}/lib/%{name}/plugins
%global rpm_has_recommends    %(rpm --version | awk -e '{print ($3 > 4.12)}')
#%%global svn     15165

# gcc 10 and fno-common FTBFS. This define reverts behaviour to gcc -fcommon.
# New version from upstream should be OK with fno-common, so remove this define ASAP
%define _legacy_common_support 1

Name:           pcb-rnd
Version:        2.2.1
Release:        1%{?dist}
Summary:        Modular Printed Circuit Board layout tool

# For a license breakdown info, please refer to https://metadata.ftp-master.debian.org/changelogs/main/p/pcb-rnd/pcb-rnd_2.2.0-1_copyright
License:        GPLv2+ and LGPLv2+ and BSD and MIT
URL:            http://repo.hu/projects/pcb-rnd/index.html
# http://repo.hu/projects/pcb-rnd/developer/packaging/packages.html
#Source0:        %%{name}-%%{svn}.tar.gz
#Source0:        pcb-rnd-%%{version}.tar.gz
Source0:        http://repo.hu/projects/pcb-rnd/releases/pcb-rnd-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  motif-devel
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtkglext-1.0)
BuildRequires:  pkgconfig(libxml-2.0)

Requires:       %{name}-core = %{version}-%{release}
%if %rpm_has_recommends
Recommends:     %{name}-io-standard = %{version}-%{release}
Recommends:     %{name}-io-alien = %{version}-%{release}
Recommends:     %{name}-hid-gtk2-gl = %{version}-%{release}
Recommends:     %{name}-hid-gtk2-gdk = %{version}-%{release}
Recommends:     %{name}-export = %{version}-%{release}
Recommends:     %{name}-export-sim = %{version}-%{release}
Recommends:     %{name}-export-extra = %{version}-%{release}
Recommends:     %{name}-auto = %{version}-%{release}
Recommends:     %{name}-extra = %{version}-%{release}
Recommends:     %{name}-cloud = %{version}-%{release}
Recommends:     %{name}-doc = %{version}-%{release}
%endif

%description
%{name} is a highly modular PCB (Printed Circuit Board) layout tool
with a rich set of plugins for communicating with various external
design tools and other EDA/CAD packages.

%package core
Summary:        Executable with the core functionality

%description core
Includes the data model, the most common action commands, the native file
format and the CLI (batch HID). Does not contain GUI.
Can be used in headless mode or batch/scripted mode for automated processing.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
User manual (html) and manual pages.

%package -n librnd
Summary:        %{name} library, binaries
Requires:       %{name}-core = %{version}-%{release}

%description -n librnd
HID, polygons, infrastructure for 3rd party applications.

%package -n librnd-devel
Summary:        %{name} library, headers
Requires:       %{name}-core = %{version}-%{release}

%description -n librnd-devel
HID, polygons, infrastructure for 3rd party applications.

%package -n librnd-static
Summary:        librnd static libraries
Requires:       librnd-devel = %{version}-%{release}

%description -n librnd-static
librnd static libraries for 3rd party applications.

%package auto
Summary:        Autoroute and autoplace
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-lib-io = %{version}-%{release}

%description auto
Feature plugins for automated component placing and track routing.

%package cloud
Summary:        Networking plugins
Requires:       %{name}-core = %{version}-%{release}

%description cloud
'Cloud' footprint access plugin that integrates edakrill and gedasymbols.org.

%package debug
Summary:        Debug and diagnostics
Requires:       %{name}-core = %{version}-%{release}

%description debug
Extra action commands to help debugging and diagnose problems and bugs.

%package export-extra
Summary:        Export formats: special/extra
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-export = %{version}-%{release}

%description export-extra
Less commonly used export formats:
fidocadj, ipc-356-d, direct printing with lpr.

%package export-sim
Summary:        Export plugins to simulators
Requires:       %{name}-core = %{version}-%{release}

%description export-sim
Export the board in formats that can be used for simulation: openems.

%package export
Summary:        Common export plugins
Requires:       %{name}-core = %{version}-%{release}

%description export
Export the board in vector graphics (svg, ps, eps), raster graphics (png, jpeg,
etc.), gerber, 3d model in openscad, xy for pick and place, BoM, etc.

%package extra
Summary:    Extra action commands and optional functionality
Requires:       %{name}-core = %{version}-%{release}

%description extra
Align objects in grid, optimize tracks, font editor, combine polygons, renumber
subcircuits, apply vendor drill mapping.

%package hid-gtk2-gdk
Summary:        GUI: gtk2, software render
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-lib-gtk = %{version}-%{release}

%description hid-gtk2-gdk
Software rendering on gtk2, using the gdk API.

%package hid-gtk2-gl
Summary:        GUI: gtk2, opengl
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-lib-gtk = %{version}-%{release}
Requires:       %{name}-lib-gl = %{version}-%{release}

%description hid-gtk2-gl
Hardware accelerated (opengl) rendering on gtk2.

%package hid-lesstif
Summary:        GUI: motif/lesstif, software render
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-lib-gui = %{version}-%{release}

%description hid-lesstif
Lightweight GUI and software rendering using the motif (lesstif) toolkit.

%package import-geo
Summary:        Geometry import plugins
Requires:       %{name}-core = %{version}-%{release}

%description import-geo
Import geometry from HPGL plots. HPGL can be produced (plotted)
with most mechanical cads.

%package import-net
Summary:        Netlist/schematics import plugins
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-lib-io = %{version}-%{release}

%description import-net
Import netlist and footprint information from edif, ltspice, mentor graphics,
gschem and tinycad.

%package io-alien
Summary:        File format compatibility with other PCB design software
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-lib-io = %{version}-%{release}

%description io-alien
Load and/or save boards in file formats supported by other EDA tools, such as
KiCAD, Eagle, protel/autotrax, etc.

%package io-standard
Summary:        Commonly used non-native board and footprint file formats
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-lib-io = %{version}-%{release}

%description io-standard
Plugins for tEDAx footprint format and the gEDA/PCB file formats
(footprint and board).

%package lib-gl
Summary:        Support library for rendering with opengl
Requires:       %{name}-core = %{version}-%{release}

%description lib-gl
Support library for rendering with opengl.

%package lib-gtk
Summary:        Support library for building the GUI with gtk
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-lib-gui = %{version}-%{release}

%description lib-gtk
Support library for building the GUI with gtk.

%package lib-gui
Summary:        Support library for building the GUI
Requires:       %{name}-core = %{version}-%{release}

%description lib-gui
Support library for building the GUI.

%package lib-io
Summary:        Support library for alien file formats
Requires:       %{name}-core = %{version}-%{release}

%description lib-io
Support library for alien file formats.

%prep
%setup -q
#%%autosetup -n %%{name}-%%{svn} -p1

%build
# This ./configure command refers to scconfig. See http://repo.hu/projects/scconfig/
./"configure" --CFLAGS="%{build_cflags}" --LDFLAGS="%{build_ldflags} -Wl,--no-as-needed" \
        --libarchdir="%{_lib}" \
        --all=disable --buildin-script --buildin-fp_fs --buildin-draw_fab \
        --buildin-act_read --buildin-drc_query --buildin-mincut --buildin-report \
        --buildin-rubberband_orig --buildin-exto_std --buildin-fp_board --buildin-propedit \
        --buildin-io_lihata --buildin-autocrop --buildin-lib_polyhelp --buildin-draw_csect \
        --buildin-ddraft --buildin-hid_batch --buildin-act_draw --buildin-tool_std \
        --buildin-query --buildin-lib_compat_help --buildin-drc_orig --buildin-shape --buildin-extedit \
        --plugin-export_excellon --plugin-export_fidocadj --plugin-export_lpr --plugin-export_oldconn -plugin-import_pxm_gd \
        --plugin-export_stat --plugin-io_kicad_legacy --plugin-io_eagle --plugin-io_tedax \
        --plugin-import_gnetlist --plugin-import_pxm_pnm --plugin-io_kicad \
        --plugin-import_mucs --plugin-renumber --plugin-import_calay --plugin-smartdisperse \
        --plugin-draw_fontsel --plugin-polycombine --plugin-export_gcode --plugin-export_bom \
        --plugin-ar_cpcb --plugin-lib_hid_pcbui --plugin-import_sch --plugin-teardrops --plugin-shand_cmd \
        --plugin-import_tinycad --plugin-export_openems --plugin-import_ltspice \
        --plugin-export_dxf --plugin-lib_gtk_common \
        --plugin-export_ipcd356 --plugin-import_ttf --plugin-import_mentor_sch --plugin-import_dsn \
        --plugin-export_ps --plugin-hid_gtk2_gdk --plugin-millpath --plugin-djopt --plugin-hid_gtk2_gl \
        --plugin-import_edif --plugin-hid_lesstif --plugin-lib_gensexpr --plugin-import_sch2 \
        --plugin-diag --plugin-lib_wget --plugin-lib_hid_gl --plugin-export_stl --plugin-autoplace --plugin-export_svg \
        --plugin-import_net_cmd --plugin-fp_wget --plugin-fontmode --plugin-import_netlist --plugin-polystitch \
        --plugin-dialogs --plugin-io_dsn --plugin-export_xy --plugin-export_png \
        --plugin-import_hpgl --plugin-import_ipcd356 --plugin-distaligntext --plugin-export_dsn \
        --plugin-lib_netmap --plugin-lib_hid_common --plugin-io_hyp --plugin-cam \
        --plugin-puller --plugin-import_fpcb_nl --plugin-io_pcb --plugin-distalign \
        --plugin-asm --plugin-export_openscad --plugin-jostle \
        --plugin-autoroute --plugin-io_autotrax --plugin-vendordrill --plugin-export_gerber \
        --plugin-import_net_action \
%if %{configure_debug} == 1
        prefix=%{_prefix} --debug
%else
        prefix=%{_prefix} --symbols
%endif

%make_build

%install
%make_install

%files
# Empty (Meta-Package)

%files doc
%doc %{_docdir}/%{name}

%files core
%{_bindir}/bxl2txt
%{_bindir}/fp2preview
%{_bindir}/fp2subc
%{_bindir}/gsch2%{name}
%{_bindir}/pcb-prj2lht
%{_bindir}/%{name}
%{_bindir}/txt2bxl
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/*.conf
%{_mandir}/man1/*
%dir %{_prefix}/lib/%{name}
%dir %{_prefix}/lib/%{name}/plugins
%{_prefix}/lib/%{name}/*.scm
%license COPYING
%doc README Changelog AUTHORS Release_notes

%files -n librnd
%{_libdir}/librnd*.so.2
%{_libdir}/librnd*.so.2.*
%{_libdir}/librnd/gen_conf
%{_libdir}/librnd/puplug

%files -n librnd-devel
%{_libdir}/librnd*.so
%dir %{_includedir}/librnd
%dir %{_includedir}/librnd/core
%dir %{_includedir}/librnd/poly
%dir %{_includedir}/librnd/scconfig
%dir %{_includedir}/librnd/src_3rd
%{_includedir}/librnd/*.h
%{_includedir}/librnd/core/*.h
%{_includedir}/librnd/poly/*.h
%{_includedir}/librnd/scconfig/*.h
%{_includedir}/librnd/src_3rd/*/*.h
%{_includedir}/librnd/src_3rd/*/*/*.h
%{_includedir}/librnd/src_3rd/genvector/genvector_impl.c
%{_datadir}/librnd/librnd.mak

%files -n librnd-static
%{_libdir}/librnd*.a

%files auto
%{plugindir}/ar_cpcb.pup
%{plugindir}/ar_cpcb.so
%{plugindir}/asm.pup
%{plugindir}/asm.so
%{plugindir}/autoplace.pup
%{plugindir}/autoplace.so
%{plugindir}/autoroute.pup
%{plugindir}/autoroute.so
%{plugindir}/export_dsn.pup
%{plugindir}/export_dsn.so
%{plugindir}/import_dsn.pup
%{plugindir}/import_dsn.so
%{plugindir}/import_mucs.pup
%{plugindir}/import_mucs.so
%{plugindir}/smartdisperse.pup
%{plugindir}/smartdisperse.so
%config(noreplace) %{_datadir}/%{name}/asm.conf

%files cloud
%{plugindir}/fp_wget.pup
%{plugindir}/fp_wget.so
%{plugindir}/lib_wget.pup
%{plugindir}/lib_wget.so
%config(noreplace) %{_datadir}/%{name}/fp_wget.conf

%files debug
%{plugindir}/diag.pup
%{plugindir}/diag.so

%files export-extra
%{plugindir}/export_fidocadj.pup
%{plugindir}/export_fidocadj.so
%{plugindir}/export_ipcd356.pup
%{plugindir}/export_ipcd356.so
%{plugindir}/export_lpr.pup
%{plugindir}/export_lpr.so
%{plugindir}/export_oldconn.pup
%{plugindir}/export_oldconn.so
%{plugindir}/export_stl.pup
%{plugindir}/export_stl.so

%files export-sim
%{plugindir}/export_openems.pup
%{plugindir}/export_openems.so

%files export
%{plugindir}/cam.pup
%{plugindir}/cam.so
%{plugindir}/export_bom.pup
%{plugindir}/export_bom.so
%{plugindir}/export_dxf.pup
%{plugindir}/export_dxf.so
%{plugindir}/export_excellon.pup
%{plugindir}/export_excellon.so
%{plugindir}/export_gcode.pup
%{plugindir}/export_gcode.so
%{plugindir}/export_gerber.pup
%{plugindir}/export_gerber.so
%{plugindir}/export_openscad.pup
%{plugindir}/export_openscad.so
%{plugindir}/export_png.pup
%{plugindir}/export_png.so
%{plugindir}/export_ps.pup
%{plugindir}/export_ps.so
%{plugindir}/export_stat.pup
%{plugindir}/export_stat.so
%{plugindir}/export_svg.pup
%{plugindir}/export_svg.so
%{plugindir}/export_xy.pup
%{plugindir}/export_xy.so
%{plugindir}/millpath.pup
%{plugindir}/millpath.so
%config(noreplace) %{_datadir}/%{name}/cam.conf
%config(noreplace) %{_datadir}/%{name}/export_xy.conf

%files extra
%{plugindir}/distalign.pup
%{plugindir}/distalign.so
%{plugindir}/distaligntext.pup
%{plugindir}/distaligntext.so
%{plugindir}/djopt.pup
%{plugindir}/djopt.so
%{plugindir}/fontmode.pup
%{plugindir}/fontmode.so
%{plugindir}/jostle.pup
%{plugindir}/jostle.so
%{plugindir}/polycombine.pup
%{plugindir}/polycombine.so
%{plugindir}/polystitch.pup
%{plugindir}/polystitch.so
%{plugindir}/puller.pup
%{plugindir}/puller.so
%{plugindir}/renumber.pup
%{plugindir}/renumber.so
%{plugindir}/shand_cmd.pup
%{plugindir}/shand_cmd.so
%{plugindir}/teardrops.pup
%{plugindir}/teardrops.so
%{plugindir}/vendordrill.pup
%{plugindir}/vendordrill.so

%files hid-gtk2-gdk
%{plugindir}/hid_gtk2_gdk.pup
%{plugindir}/hid_gtk2_gdk.so

%files hid-gtk2-gl
%{plugindir}/hid_gtk2_gl.pup
%{plugindir}/hid_gtk2_gl.so

%files hid-lesstif
%{plugindir}/hid_lesstif.pup
%{plugindir}/hid_lesstif.so

%files import-geo
%{plugindir}/import_hpgl.pup
%{plugindir}/import_hpgl.so
%{plugindir}/import_pxm_gd.pup
%{plugindir}/import_pxm_gd.so
%{plugindir}/import_pxm_pnm.pup
%{plugindir}/import_pxm_pnm.so
%{plugindir}/import_ttf.pup
%{plugindir}/import_ttf.so

%files import-net
#FIXME: $PREFIX/bin/gsch2pcb-rnd $PREFIX/lib/pcb-rnd/*.scm $PREFIX/share/man/man1/gsch2pcb-rnd.1 
%{plugindir}/import_calay.pup
%{plugindir}/import_calay.so
%{plugindir}/import_edif.pup
%{plugindir}/import_edif.so
%{plugindir}/import_fpcb_nl.pup
%{plugindir}/import_fpcb_nl.so
%{plugindir}/import_gnetlist.pup
%{plugindir}/import_gnetlist.so
%{plugindir}/import_ipcd356.pup
%{plugindir}/import_ipcd356.so
%{plugindir}/import_ltspice.pup
%{plugindir}/import_ltspice.so
%{plugindir}/import_mentor_sch.pup
%{plugindir}/import_mentor_sch.so
%{plugindir}/import_net_action.pup
%{plugindir}/import_net_action.so
%{plugindir}/import_net_cmd.pup
%{plugindir}/import_net_cmd.so
%{plugindir}/import_netlist.pup
%{plugindir}/import_netlist.so
%{plugindir}/import_sch.pup
%{plugindir}/import_sch.so
%{plugindir}/import_sch2.pup
%{plugindir}/import_sch2.so
%{plugindir}/import_tinycad.pup
%{plugindir}/import_tinycad.so
#%%config(noreplace) %%{_datadir}/%%{name}/import_gnetlist.conf

%files io-alien
%{plugindir}/io_autotrax.pup
%{plugindir}/io_autotrax.so
%{plugindir}/io_dsn.pup
%{plugindir}/io_dsn.so
%{plugindir}/io_eagle.pup
%{plugindir}/io_eagle.so
%{plugindir}/io_hyp.pup
%{plugindir}/io_hyp.so
%{plugindir}/io_kicad.pup
%{plugindir}/io_kicad.so
%{plugindir}/io_kicad_legacy.pup
%{plugindir}/io_kicad_legacy.so

%files io-standard
%{plugindir}/io_pcb.pup
%{plugindir}/io_pcb.so
%{plugindir}/io_tedax.pup
%{plugindir}/io_tedax.so

%files lib-gl
%{plugindir}/lib_hid_gl.pup
%{plugindir}/lib_hid_gl.so

%files lib-gtk
%{plugindir}/lib_gtk_common.pup
%{plugindir}/lib_gtk_common.so

%files lib-gui
%{plugindir}/dialogs.pup
%{plugindir}/dialogs.so
%{plugindir}/draw_fontsel.pup
%{plugindir}/draw_fontsel.so
%{plugindir}/lib_hid_common.pup
%{plugindir}/lib_hid_common.so
%{plugindir}/lib_hid_pcbui.pup
%{plugindir}/lib_hid_pcbui.so
%config(noreplace) %{_datadir}/%{name}/dialogs.conf

%files lib-io
%{plugindir}/lib_gensexpr.pup
%{plugindir}/lib_gensexpr.so
%{plugindir}/lib_netmap.pup
%{plugindir}/lib_netmap.so

%changelog
* Wed Apr 22 2020 Alain Vigne <alain vigne 14 gmail com> 2.2.1-1
- New upstream version 2.2.1
- Plugins: Add: drc_query, tool_std, import_gnetlist, import_sch2, import_net_cmd, import_net_action

* Wed Feb 05 2020 Alain Vigne <alain vigne 14 gmail com> 2.2.0-1
- New upstream version 2.2.0
- Add new librnd and librnd-devel subpackages
- Plugins: Remove: lib_gtk_hid
- Plugins: Add: export_stl, millpath, import_hpgl, import_pxm_gd, import_pxm_pnm

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Alain Vigne <alain vigne 14 gmail com> 2.1.3-1
- New upstream version 2.1.3
- Plugins: Add: act_read, export_excellon, lib_hid_pcbui, lib_wget

* Sat May 11 2019 Alain Vigne <alain vigne 14 gmail com> 2.1.2-2
- Fix plugins loading problem, by disabling linker "as-needed" flag

* Tue Apr 23 2019 Alain Vigne <alain vigne 14 gmail com> 2.1.2-1
- New 2.1.2 upstream
- Add build flags to local "configure"

* Sun Feb 10 2019 Alain Vigne <alain vigne 14 gmail com> 2.1.1-1
- New 2.1.1 upstream
- Plugins: Remove: boardflip, lib_gtk_config ; Add: drc_orig, export_oldconn, import_calay

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 25 2018 Alain Vigne <alain vigne 14 gmail com> 2.1.0-1
- New 2.1.0 upstream
- Plugins: Add: asm, ar_cpcb, import_ttf, io_dsn

* Wed Aug 29 2018 Alain Vigne <alain vigne 14 gmail com> 2.0.1-1
- Plugins: Add: script, ddraft, cam, import_fpcb_nl
- Improve .spec file according to suggestions from Fedora reviewer.

* Wed Jun 06 2018 Alain Vigne <alain vigne 14 gmail com> 2.0.0-1
- Plugins: Retire lib_padstack_hash ; Add import_ipcd356
- Improve .spec file according to reviews

* Wed Mar 21 2018 Alain Vigne <alain vigne 14 gmail com> 1.2.8-1
- Initial proposal
