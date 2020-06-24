Name: wxmacmolplt
Version: 7.7
Release: 13%{?dist}
Summary: A graphics program for plotting 3-D molecular structures and normal modes
License: GPLv2+
URL: http://brettbode.github.io/wxmacmolplt/
# http://brettbode.github.io/wxmacmolplt/downloads.html
# -> https://uofi.box.com/shared/static/7pzccnku3uv0mmf6il6yiqghf4b34lc7.gz
Source0: https://public.boxcloud.com/d/1/Oj-GfT43PM2JETaILGilJVHNB_9f_ljhMpkSNG-NNRrFqGCr2irf1LApKotdcJeRBz9nyiukYmpZqX-P8vjSvV_8WLkMCOnuNcU8YWQVqIgAZ9YZQCDkK6dYL_bOmetSVkXD1vaTjenko7nWGN_su3odl5enZFZu7eL1fpUkzoraljb8yc8PyIkA_SPhvhGuKtNAe1wwmOSeSv-hy_CN4lVLU-C-d0Ye-kI718OQtZQ1IXfb8HekWAi2Nyv3IQtweWREsVi0S1xzr5Y8oWjMBokX9ZcGOoGE9ShfdqPjEw4pIZPliQNL2aECMo60C6AjUU1q6ecN_pvqR-WlGHUGCG3h38ym0n_npMDik3WSgA6no5ElWm2zK3Z_OMn35Ejqc5hnIT_gRFwmiQcZ_Q8HWqzs32K3Ao4EytDH9YT2xnk0b7CDRtCA80eYR7rdanUjgVAUJ2GFFJoVgL7M4aAfnfweJ2OMi1nGkdjgi7j3QV7ENPRWIPHMOU-W2eBdFjdccQyu0Hq_TUSjfI-jzQlHqU6XjPOvOWMhL8Yf3aMcggpRrq4WdnlDkyTK_rI6DwJCRIBoPj5TIWDGq-lHvIkQFyWKo2r94BlLJjDXfO7Zl0nHvyEOqvGSB6FRJ-yzADPhOE_w3tsal-jL_nj0TA8vuuTQdo1pC9ABCAhZr9rDrj8sz4dPkD2UhBJ_qlRS_1ahtz-s99VNl5rQQKyWM_38LK6W5K_ybme8wThICf04EUeVmSG_V9k-Kvc0LOXNkRlENcvGdWd1werEmbMjB6cSsGatbzlxW6WkVk7hBRUUs3o2i9gn05_qBeX2DhZ-wXUx-e-XayK6PtShZAR_gEtG4OOsl5lM8L58XVIKs5H3rnn153W60_v7351si8S2xkE7YEi237F6nK_E3vhdyQ2WI9lW25tEzftzLmkKt-xeDxU7iQG5gc7yWK75AJ1IB9KRY-i219Ws-jJiAnMjWESKwf44yo9k6AOt35aMTeTYy6MeNIdxdKXPMHvPdE0e4CE4LAGGXPnD3Dd98fm00Vzw7TmUrTnIjnsTja_Ir8yp06HhWKspr78hm_PICNgW82_LZuB17Bf0kppLx8bWFRK39VzENhcnTzbLOm61Bi3R3uYFw3gAcKm9KHtzn1iHPQJ3iamZhOEDmlPc33sgK1sRzxCfiwIJl84YUaderMSX-ansPvCGMPA./download#/wxmacmolplt-%{version}.tar.gz
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: glew-devel
BuildRequires: ming-devel
%if 0%{?fedora} >= 25
BuildRequires: wxGTK3-devel
BuildRequires: automake
%else
BuildRequires: wxGTK-devel >= 2.6.3
%endif
Requires: hicolor-icon-theme

%description
MacMolPlt is:
* A modern graphics program for plotting 3-D molecular structures and
  normal modes (vibrations). Modern means:
  o Mouse driven interface for real-time rotation and translation.
  o copy and paste functionality for interfacing to other programs such
    as word processors or other graphics programs (like ChemDraw).
  o simple printing to color or black and white printers (publication
    quality).
  o multiple files open at once.
* It reads a variety of file formats including any GAMESS input, log or
  IRC file directly to create animations of IRC's, DRC's, and
  optimizations. You may also import a $VEC group from any file (such as
  a GAMESS .DAT file). In addition xMol XYZ files, MolDen format files
  and Chemical Markup Language (CML) files are supported. Also some PDB
  file support and MDL MolFile support is included.

%prep
%setup -q

%build
autoreconf -vif
%configure \
  --docdir=%{_pkgdocdir} \
  --with-ming \
%if 0%{?fedora} >= 25
  --with-wx-config=%{_bindir}/wx-config-3.0 \
%endif

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
install -Dpm644 resources/wxmacmolplt.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/wxmacmolplt.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications resources/wxmacmolplt.desktop
rm %{buildroot}%{_pkgdocdir}/LICENSE

%files
%license LICENSE
%{_bindir}/wxmacmolplt
%{_mandir}/man1/wxmacmolplt.1*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/128x128/apps/wxmacmolplt.png
%{_datadir}/wxmacmolplt

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 7.7-10
- Rebuilt for glew 2.1.0

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 7.7-9
- Rebuild with fixed binutils

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 7.7-2
- Rebuild for glew 2.0.0

* Sat Aug 27 2016 Dominik Mierzejewski <rpm@greysector.net> 7.7-1
- update to 7.7
- use wxGTK3 (F25+ only)

* Mon Feb 22 2016 Dominik Mierzejewski <rpm@greysector.net> 7.6.2-1
- update to 7.6.2
- update URL to new upstream location
- drop defattr and use license macro

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 7.5-8
- Rebuild for glew 1.13

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 7.5-6
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Dominik Mierzejewski <rpm@greysector.net> 7.5-4
- enable SWF output (depends on ming)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Dominik Mierzejewski <rpm@greysector.net> 7.5-2
- fix docdir location
- re-run autoreconf before build to fix aarch64 support (rhbz #926733)

* Tue Feb 11 2014 Dominik Mierzejewski <rpm@greysector.net> 7.5-1
- update to 7.5
- update source URL
- drop obsolete spec file parts
- use upstream desktop file and icon

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 7.4.4-3
- rebuilt for GLEW 1.10

* Wed Jul 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 7.4.4-2
- Drop unnecessary --docdir %%configure arg.

* Sun Mar 17 2013 Dominik Mierzejewski <rpm@greysector.net> 7.4.4-1
- updated to 7.4.4
- dropped system glew patch (obsolete)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 7.4.1-8
- Rebuild for glew 1.9.0

* Wed Aug 01 2012 Adam Jackson <ajax@redhat.com> - 7.4.1-7
- -Rebuild for new glew

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.1-5
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 ajax@redhat.com - 7.4.1-3
- Rebuild for new glew soname

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 13 2010 Dominik Mierzejewski <rpm@greysector.net> 7.4.1-1
- updated to 7.4.1

* Wed Dec 02 2009 Dominik Mierzejewski <rpm@greysector.net> 7.4-1
- adapted upstream specfile
- patched to use system glew
- added desktop file and icon from project website
