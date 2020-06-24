Name:           plotdrop
Version:        0.5.3
Release:        24%{?dist}
Summary:        A minimal GNOME front-end to Gnuplot

License:        GPLv2
URL:            http://plotdrop.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.gz
Patch0:         plotdrop-desktop-file.patch

Requires:       gnuplot
BuildRequires:  gcc
BuildRequires:  libglade2-devel gnome-vfs2-devel desktop-file-utils

%description
Plotdrop is a minimal GNOME front-end to Gnuplot.
Plotdrop is designed for quick simple visualization of 2D data series. 
It is not intended to encompass anywhere near the full capabilities of Gnuplot. 

%prep
%setup -q
%patch0 -p1
sed -i "s/CFLAGS = /CFLAGS += /" Makefile
sed -i "s/install -s/install/g" Makefile

%build
export CFLAGS=$RPM_OPT_FLAGS
make %{?_smp_mflags} PREFIX=%{_prefix}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://sourceforge.net/p/plotdrop/bugs/2/
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">plotdrop.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Create graphs and data visualizations</summary>
  <description>
    <p>
      Plotdrop is a simple application for creating quick graphs from
      2D datasets using the GNUPlot backend.
      To use plotdrop, you simply drag and drop a data file from your file browser,
      configure the options and generate your graph.
    </p>
  </description>
  <url type="homepage">http://plotdrop.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://plotdrop.sourceforge.net/screenshot-0.5.jpeg</screenshot>
  </screenshots>
</application>
EOF

# validate desktop file
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/plotdrop.desktop


%files
%doc COPYING Changelog 
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/droplist.glade
%{_datadir}/%{name}/%{name}.png


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.5.3-14
- Add an AppData file for the software center

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.5.3-7
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Arun SAG <sagarun@gmail.com> - 0.5.3-5
- Add gnuplot to requires

* Sun Jan 9 2011 Arun SAG <sagarun@gmail.com> - 0.5.3-4
- Fix the prefix

* Sun Jan 9 2011 Arun SAG <sagarun@gmail.com> - 0.5.3-3
- Fix strip option in makefile

* Sun Dec 12 2010  Arun SAG <sagarun@gmail.com> - 0.5.3-2
- Fix CFLAGS

* Sat Dec 11 2010  Arun SAG <sagarun@gmail.com> - 0.5.3-1
- Initial package
