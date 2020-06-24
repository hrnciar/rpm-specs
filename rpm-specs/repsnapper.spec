Name:           repsnapper
Version:        2.5
%global         atag a5
Release:        0.4.%{atag}%{?dist}
Summary:        RepRap control software

# repsnapper is GPLv2 as noted in licensing.txt
#
# arcball.cpp and arcball.h are
#      (C) 1999-2003 Tatewake.com and licensed under the MIT license
#      as noted in licensing.txt
#
# Several functions in slicer/geometry.cpp are licensed with non stock MIT-like license
#      as noted in licensing.txt
#      and attached e-mail
#
# Icon is CC-BY, infile metadata
License:        GPLv2 and MIT and softSurfer and CC-BY

URL:            https://github.com/timschmidt/%{name}
Source0:        https://github.com/timschmidt/%{name}/archive/%{version}%{atag}.tar.gz
Source1:        %{name}-softsurfer-copyright-email.txt
Patch0:         %{name}-use-system-libs.patch

# https://bugs.launchpad.net/ubuntu/+source/repsnapper/+bug/1619100
Patch1:         %{name}-ppc64el-asm-generic.patch

# trivial compatibility patch to work with lmfit 7
Patch2:         %{name}-lmfit7.patch

BuildRequires:  amftools-devel
BuildRequires:  cairomm-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glibmm24-devel
BuildRequires:  glib2-devel
BuildRequires:  gtkglext-devel
BuildRequires:  gtkglextmm-devel >= 1.2
BuildRequires:  gtkmm24-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  libxml++-devel
BuildRequires:  libzip-devel
BuildRequires:  lmfit-devel >= 7
BuildRequires:  muParser-devel
BuildRequires:  polyclipping-devel >= 6.1.0
BuildRequires:  poly2tri-devel
BuildRequires:  rapidxml-devel
BuildRequires:  vmmlib-devel

# So that it just works
Requires:       3dprinter-udev-rules

%description
RepSnapper is a host software for controlling the RepRap 3D printer.

%prep
%setup -qn %{name}-%{version}%{atag}
cp %SOURCE1 .

%patch0 -p1
%patch1 -p1
%patch2 -p1
rm -rf libraries/{clipper,vmmlib,amf,lmfit,poly2tri}

# Remove license information of bundled libs
rm -f licenses/{BSL-1.0.txt,LGPL-2.0.txt,vmmlib-license.txt}
grep -v VMMLib licensing.txt > licensing-no-vmmlib.txt && mv -f licensing-no-vmmlib.txt licensing.txt

# Move it to Graphics category
sed -i 's/Utility;/Graphics;/' %{name}.desktop.in
sed -i 's/_Name=%{name}/_Name=RepSnapper/' %{name}.desktop.in

%build
./autogen.sh
%configure
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc HACKING licensing.txt README.asciidoc TODO todo.txt licenses %{name}-softsurfer-copyright-email.txt
%config(noreplace) %{_sysconfdir}/xdg/%{name}/%{name}.conf
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-0.4.a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-0.3.a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-0.2.a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5-0.1.a5
- New version 2.5a5 (#1458461)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.8.a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.7.a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4-0.6.a3
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.5.a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.4.a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-0.3.a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Mon May 08 2017 Miro Hrončok <mhroncok@redhat.com> - 2.4-0.2.a3
- New version 2.4a3 (#1448851)

* Thu Apr 13 2017 Miro Hrončok <mhroncok@redhat.com> - 2.4-0.1.a2
- New version 2.4a2 (#1441875)
- Fixes FTBFS (#1424253, #1377089, #1289560)

* Tue Feb 28 2017 Remi Collet <remi@fedoraproject.org> - 2.3.2-0.12.a5
- rebuild for new libzip

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-0.11.a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 25 2016 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-0.10.a5
- Require 3dprinter-udev-rules

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-0.9.a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-0.8.a5
- Rebuilt for new lmfit

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-0.7.a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Remi Collet <remi@fedoraproject.org> - 2.3.2-0.6.a5
- rebuild for new libzip

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3.2-0.5.a5
- Rebuilt for GCC 5 C++11 ABI change

* Wed Oct 22 2014 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-0.4.a5
- New alpha release
- Patch to support clipper/polyclipping 6.2.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-0.3.a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-0.2.a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-0.1.a4
- New upstream version 2.3.2a4
- Updated for clipper/polyclipping 6.1.3a
- Added appdata file to %%files

* Tue Nov 26 2013 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-0.1.a0
- New upstream version 2.3.1a0

* Tue Aug 27 2013 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-0.6.b3
- New upstream betaversion
- Rebuild for new lmfit, added patch to support it

* Wed Aug 21 2013 Remi Collet <rcollet@redhat.com> - 2.2.0-0.5.a4
- rebuild for new libzip

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-0.4.a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 25 2013 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-0.3.a4
- Rebuilt for new polyclipping

* Mon Jun 03 2013 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-0.2.a4
- Tag 2.2.0a4
- Fixed the font bug (#969624)

* Wed May 08 2013 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-0.1.a2
- Updated to 2.2.0a2
- Removed adding icon manually, as it is in this release
- Added e-mail with updated copyright information of softSurfer code

* Tue Feb 05 2013 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-5
- Moved %%find_lang to %%install

* Tue Feb 05 2013 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-4
- Using new RepSnapper icon

* Thu Jan 31 2013 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-3
- Using system vmmlib, amftools, lmfit, poly2tri
- Polished description a bit
- Change name in .desktop to RepSnapper
- Added comment about license
- Using %%config(noreplace)
- Added icons from #679273

* Wed Jan 30 2013 Volker Fröhlich <volker27@gmx.at> - 2.1.0-2
- Correct patch to link polyclipping
- Make build verbose

* Tue Jan 29 2013 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-1
- Chnaged source to respect GitHub rule
- Dropped %%{?_isa} from BRs
- Dropped group
- Added things to %%doc
- desktop-file-validate
- Using %%{name} macro in %%files
- Changing desktop file category to Multimedia, as at all others RepRap tools
- Using system clipper/polyclipping

* Wed Oct 24 2012 Alon Levy <alevy@redhat.com> - 2.1.0b02-3
- added missing dependencies for mock build

* Tue Oct 23 2012 Alon Levy <alevy@redhat.com> - 2.1.0b02-2
- Address review comments

* Mon Oct 22 2012 Alon Levy <alevy@redhat.com> - 2.1.0b02-1
- Initial spec file submitted for review
